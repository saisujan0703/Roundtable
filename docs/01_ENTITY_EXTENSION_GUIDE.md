# Guidewire PolicyCenter Entity Creation & Extension Guide

> **Target Codebase**: Guidewire PolicyCenter 10.2.1 (`project-version=10.2.1.1711`, Platform `10.201.1`, Gosu `1.14.26`, Amazon Corretto JDK 11)  
> **Source Directory**: `C:\GW10\PolicyCenter\modules\configuration`  
> **Generated Documentation**: `C:\Users\Student\Documents\roundtable\docs\01_ENTITY_EXTENSION_GUIDE.md`

---

## 1. Overview of Entity Architecture in PolicyCenter 10

In Guidewire PolicyCenter, the data model is defined via XML metadata files:
* **Base/Platform Entities (`.eti`)**: Located in `modules/configuration/config/metadata/entity/`. These are out-of-the-box (OOTB) entities provided by Guidewire. *Never edit or add files directly in this folder.*
* **Custom Entities (`.eti`)**: Located in `modules/configuration/config/extensions/entity/`. All newly defined application entities must reside here.
* **Entity Extensions (`.etx`)**: Located in `modules/configuration/config/extensions/entity/`. Used to add fields, foreign keys, or arrays to existing base entities (e.g., adding a custom field to `PolicyPeriod` or `Job`).
* **Typelists (`.tti` / `.ttx`)**: Located in `modules/configuration/config/extensions/typelist/`. `.tti` defines a new typelist (enum), while `.ttx` extends an existing typelist.
* **Display Names (`.en`)**: Located in `modules/configuration/config/displaynames/`. Defines how an entity is displayed as a string across the UI and logs.

---

## 2. Real Existing Patterns from the Codebase

### Real Custom Entity Example: `LOBFieldVisibility.eti`
File location in codebase: `modules/configuration/config/extensions/entity/LOBFieldVisibility.eti`
```xml
<?xml version="1.0"?>
<entity
  xmlns="http://guidewire.com/datamodel"
  desc="LOB UI Field Visibility"
  entity="LOBFieldVisibility"
  final="false"
  table="lobfieldvisibility"
  type="retireable">
  <column
    desc="Field path"
    name="Field"
    nullok="false"
    type="shorttext"/>
  <typekey
    desc="Jurisdiction"
    name="Jurisdiction"
    nullok="true"
    typelist="Jurisdiction"/>
  <column
    default="true"
    desc="Visibility of a field"
    name="IsVisible"
    nullok="false"
    type="bit"/>
  <index
    desc="Unique constraint"
    name="lobfieldvisu1"
    unique="true">
    <indexcol
      keyposition="1"
      name="Field"/>
    <indexcol
      keyposition="2"
      name="Jurisdiction"/>
  </index>
</entity>
```

### Real Custom Typelist Example: `DeductibleType.tti`
File location in codebase: `modules/configuration/config/extensions/typelist/DeductibleType.tti`
```xml
<?xml version="1.0"?>
<typelist
  xmlns="http://guidewire.com/typelists"
  desc="Deductible Type"
  name="DeductibleType"
  tableName="DeductibleType">
  <typecode
    code="PerClaim"
    desc="Per Claim"
    name="Per Claim"
    priority="1"/>
  <typecode
    code="PerOccurrence"
    desc="Per Occurrence"
    name="Per Occurrence"
    priority="2"/>
</typelist>
```

### Real Column Type Reference
The column types supported in PolicyCenter 10 are defined in `modules/configuration/config/datatypes/*.dti`:
* `shorttext`: `java.lang.String`, default max 255 chars (from `shorttext.dti`).
* `mediumtext`: `java.lang.String`, max 512 chars (from `mediumtext.dti`).
* `longtext` / `text`: CLOB/text for lengthy text without strict length bounds (from `longtext.dti`, `text.dti`).
* `datetime`: Timestamp with timezone (from `datetime.dti`).
* `bit`: Boolean primitive (from `bit.dti`).
* `integer`: 32-bit signed integer (from `integer.dti`).
* `varchar`: Variable length character data with explicit `<columnParam name="size" value="..."/>`.
* `typekey`: Enum reference to a typelist.

### Entity Types (`type="..."`)
* `retireable` (Recommended): Inherits `KeyableBean`, `VersionableBean`, `EditableBean`, and `RetireableBean`. Automatically includes:
  - `ID`: Primary key.
  - `PublicID`: Unique external identifier string (e.g. `pc:1001` or custom).
  - `BeanVersion`: Optimistic locking counter.
  - `CreateTime`, `CreateUser`: Audit timestamp and user reference.
  - `UpdateTime`, `UpdateUser`: Audit timestamp and user reference.
  - `Retired`: Long integer flag for soft deletes (0 = active, non-zero = retired).
* `editable`: Has `CreateTime`, `CreateUser`, `UpdateTime`, `UpdateUser`, but hard deletes when removed.
* `versionable`: Only has `ID`, `PublicID`, and `BeanVersion`.

---

## 3. Designing the Roundtable "Brief" Custom Entity

For Roundtable, a `Brief` entity stores an AI-assisted product decision brief containing:
1. `Title` (`shorttext`)
2. `ProductIdea` / summary description (`mediumtext` or `shorttext`)
3. `EvidenceText` (`longtext`)
4. `CompetitorComparison` (`longtext`)
5. `DirectionalEstimates` (`longtext`)
6. `Citations` (`longtext` for JSON/Markdown cited sources or an array)
7. Five approval statuses:
   - `ClaimsStatus`
   - `ActuarialStatus`
   - `UnderwritingStatus`
   - `MarketingStatus`
   - `ComplianceStatus`
8. `CreatedDate` (`datetime`)
9. `TargetProductLine` (`varchar` or `typekey` / foreign key)
10. `ApdProductCode` (patterncode/shorttext once written into APD)

### Step 3.1: Define the Typelist `RoundtableApprovalStatus.tti`
**File Target**: `modules/configuration/config/extensions/typelist/RoundtableApprovalStatus.tti`

```xml
<?xml version="1.0"?>
<typelist
  xmlns="http://guidewire.com/typelists"
  desc="Approval status for Roundtable product decision briefs"
  name="RoundtableApprovalStatus"
  tableName="rtapprovalstatus">
  <typecode
    code="Draft"
    desc="Brief is in draft state"
    name="Draft"
    priority="1"/>
  <typecode
    code="PendingReview"
    desc="Brief is submitted and awaiting review"
    name="Pending Review"
    priority="2"/>
  <typecode
    code="Approved"
    desc="Team approved this brief"
    name="Approved"
    priority="3"/>
  <typecode
    code="Rejected"
    desc="Team rejected this brief"
    name="Rejected"
    priority="4"/>
</typelist>
```

### Step 3.2: Define the Custom Entity `RoundtableBrief.eti`
**File Target**: `modules/configuration/config/extensions/entity/RoundtableBrief.eti`

```xml
<?xml version="1.0"?>
<entity
  xmlns="http://guidewire.com/datamodel"
  desc="Roundtable AI-assisted product decision brief"
  entity="RoundtableBrief"
  exportable="true"
  final="false"
  loadable="false"
  table="rt_roundtablebrief"
  type="retireable">
  
  <!-- Basic Metadata -->
  <column
    desc="Title of the proposed product decision brief"
    name="Title"
    nullok="false"
    type="shorttext"/>
    
  <column
    desc="High-level product summary or concept description"
    name="ProductSummary"
    nullok="true"
    type="mediumtext"/>

  <column
    desc="Proposed target PolicyLine or line prefix (e.g. PersonalAuto, CommercialProperty, Cyber)"
    name="TargetLineCode"
    nullok="true"
    type="shorttext"/>

  <!-- Brief Content Sections -->
  <column
    desc="Synthesized evidence and market need text"
    name="EvidenceText"
    nullok="true"
    type="longtext"/>

  <column
    desc="Competitor comparison matrix and analysis"
    name="CompetitorComparison"
    nullok="true"
    type="longtext"/>

  <column
    desc="Directional financial and loss ratio estimates"
    name="DirectionalEstimates"
    nullok="true"
    type="longtext"/>

  <column
    desc="JSON or Markdown formatted list of cited references"
    name="Citations"
    nullok="true"
    type="longtext"/>

  <!-- Dates -->
  <column
    desc="Date and time when the brief was generated"
    name="CreatedDate"
    nullok="false"
    type="datetime"/>

  <column
    desc="Date and time when all five teams completed approvals"
    name="ApprovedDate"
    nullok="true"
    type="datetime"/>

  <!-- Five Team Approval Statuses -->
  <typekey
    default="Draft"
    desc="Approval status from the Claims team"
    name="ClaimsStatus"
    nullok="false"
    typelist="RoundtableApprovalStatus"/>

  <typekey
    default="Draft"
    desc="Approval status from the Actuarial team"
    name="ActuarialStatus"
    nullok="false"
    typelist="RoundtableApprovalStatus"/>

  <typekey
    default="Draft"
    desc="Approval status from the Underwriting team"
    name="UnderwritingStatus"
    nullok="false"
    typelist="RoundtableApprovalStatus"/>

  <typekey
    default="Draft"
    desc="Approval status from the Marketing team"
    name="MarketingStatus"
    nullok="false"
    typelist="RoundtableApprovalStatus"/>

  <typekey
    default="Draft"
    desc="Approval status from the Compliance team"
    name="ComplianceStatus"
    nullok="false"
    typelist="RoundtableApprovalStatus"/>

  <!-- Downstream Integration Status -->
  <column
    default="false"
    desc="Indicates whether this brief has been pushed to APD"
    name="PushedToApd"
    nullok="false"
    type="bit"/>

  <column
    desc="CodeIdentifier of the generated APDProduct in PolicyCenter"
    name="ApdProductCode"
    nullok="true"
    type="shorttext"/>

  <foreignkey
    columnName="APDProductID"
    desc="Foreign key to the generated APDProduct entity (optional link)"
    fkentity="APDProduct"
    name="APDProduct"
    nullok="true"/>

  <!-- Index for quick lookup by Title -->
  <index
    desc="Index for looking up briefs by title"
    name="rtbrief_title_idx"
    unique="false">
    <indexcol
      keyposition="1"
      name="Title"/>
    <indexcol
      keyposition="2"
      name="Retired"/>
  </index>
</entity>
```

### Step 3.3: Define Display Name Configuration
**File Target**: `modules/configuration/config/displaynames/RoundtableBrief.en`

```xml
<?xml version="1.0"?>
<Entity
  name="RoundtableBrief">
  <Columns>
    <Column
      beanPath="RoundtableBrief.Title"
      name="title"/>
  </Columns>
  <DisplayName><![CDATA[
title
  ]]></DisplayName>
</Entity>
```

---

## 4. How Gosu Generates Classes from Entities

PolicyCenter uses code generation plugins defined in `modules/script/gw-build.gradle`:
* `com.guidewire.codegen-entity` runs task `genEntitySources`.
* Running `gwb compile` or triggering a build from Guidewire Studio compiles `.eti` and `.tti` into:
  - Java interfaces: `modules/configuration/generated/entity/RoundtableBrief.java`
  - Java implementations: `modules/configuration/generated/com/guidewire/_generated/entity/RoundtableBriefImpl.java`
  - Typelist classes: `modules/configuration/generated/typekey/RoundtableApprovalStatus.java`

### Using the Entity in Gosu
Once generated, you use the entity like any standard Gosu class:
```gosu
uses gw.transaction.Transaction

Transaction.runWithNewBundle(\bundle -> {
  var brief = new RoundtableBrief(bundle)
  brief.Title = "Commercial Drone Liability Endorsement"
  brief.CreatedDate = java.util.Date.CurrentDate
  brief.ClaimsStatus = RoundtableApprovalStatus.TC_PENDINGREVIEW
  brief.ActuarialStatus = RoundtableApprovalStatus.TC_PENDINGREVIEW
  brief.UnderwritingStatus = RoundtableApprovalStatus.TC_PENDINGREVIEW
  brief.MarketingStatus = RoundtableApprovalStatus.TC_PENDINGREVIEW
  brief.ComplianceStatus = RoundtableApprovalStatus.TC_PENDINGREVIEW
  brief.EvidenceText = "Market research shows 43% increase in commercial drone operations..."
})
```

### Adding Helper Methods with Gosu Enhancement (`.gsx`)
To add business logic to the entity without touching generated code, create an enhancement:
**File Target**: `modules/configuration/gsrc/roundtable/entity/RoundtableBriefEnhancement.gsx`

```gosu
package roundtable.entity

enhancement RoundtableBriefEnhancement : entity.RoundtableBrief {
  
  property get IsFullyApproved() : boolean {
    return this.ClaimsStatus == TC_APPROVED
        and this.ActuarialStatus == TC_APPROVED
        and this.UnderwritingStatus == TC_APPROVED
        and this.MarketingStatus == TC_APPROVED
        and this.ComplianceStatus == TC_APPROVED
  }

  function approveTeam(team : String) {
    switch (team.toLowerCase()) {
      case "claims": this.ClaimsStatus = TC_APPROVED; break
      case "actuarial": this.ActuarialStatus = TC_APPROVED; break
      case "underwriting": this.UnderwritingStatus = TC_APPROVED; break
      case "marketing": this.MarketingStatus = TC_APPROVED; break
      case "compliance": this.ComplianceStatus = TC_APPROVED; break
      default: throw new java.lang.IllegalArgumentException("Unknown team: " + team)
    }
    if (this.IsFullyApproved and this.ApprovedDate == null) {
      this.ApprovedDate = java.util.Date.CurrentDate
    }
  }

  function rejectTeam(team : String) {
    switch (team.toLowerCase()) {
      case "claims": this.ClaimsStatus = TC_REJECTED; break
      case "actuarial": this.ActuarialStatus = TC_REJECTED; break
      case "underwriting": this.UnderwritingStatus = TC_REJECTED; break
      case "marketing": this.MarketingStatus = TC_REJECTED; break
      case "compliance": this.ComplianceStatus = TC_REJECTED; break
      default: throw new java.lang.IllegalArgumentException("Unknown team: " + team)
    }
  }
}
```

---

## 5. Summary Checklist for Adding an Entity

1. Create typelist `.tti` in `modules/configuration/config/extensions/typelist/` (if using new enums).
2. Create entity `.eti` in `modules/configuration/config/extensions/entity/`.
3. Create display name `.en` in `modules/configuration/config/displaynames/`.
4. (Optional) Create enhancement `.gsx` in `modules/configuration/gsrc/roundtable/entity/`.
5. Run `./gwb compile` or build project in Guidewire Studio to generate backing Java/Gosu classes.
