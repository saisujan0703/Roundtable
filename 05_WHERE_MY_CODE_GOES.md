# Guidewire PolicyCenter Directory Structure: Where My Code Goes

> **Target Codebase**: Guidewire PolicyCenter 10.2.1 (`project-version=10.2.1.1711`, Platform `10.201.1`, Gosu `1.14.26`)  
> **PolicyCenter Root**: `C:\GW10\PolicyCenter`  
> **Configuration Module**: `C:\GW10\PolicyCenter\modules\configuration`  
> **Generated Documentation**: `C:\Users\Student\Documents\roundtable\docs\05_WHERE_MY_CODE_GOES.md`

---

## 1. Golden Rules for PolicyCenter File Placement

1. **All custom development belongs in `modules/configuration/`**: Never place code outside `modules/configuration` or inside platform runtime folders.
2. **Never edit `config/metadata/` directly**: Base Guidewire entities live in `config/metadata/entity/`. New custom entities and extensions must be placed in `config/extensions/entity/`.
3. **Never edit `generated/` or `generated_classes/`**: These folders are automatically populated by the code generator (`gwb compile` or Studio) and overwritten on each build.
4. **Segregate your code into a distinct package/folder**: Place all Roundtable integration code under `roundtable` packages and folders so they can be easily tracked, tested, and upgraded.

---

## 2. Master Directory Map

Here is the exact mapping of where every Roundtable component must be placed within `modules/configuration/`:

```
C:\GW10\PolicyCenter\modules\configuration\
|
+-- config/
|   +-- extensions/
|   |   +-- entity/
|   |   |   +-- RoundtableBrief.eti                <-- [NEW CUSTOM ENTITY]
|   |   |   +-- PolicyPeriod.Roundtable.etx        <-- [OPTIONAL: EXTENSION TO OOTB ENTITY]
|   |   |
|   |   +-- typelist/
|   |       +-- RoundtableApprovalStatus.tti       <-- [NEW CUSTOM TYPELIST]
|   |
|   +-- displaynames/
|   |   +-- RoundtableBrief.en                     <-- [ENTITY DISPLAY NAME]
|   |
|   +-- locale/
|   |   +-- display.properties                     <-- [UI DISPLAY KEYS / LOCALIZATION]
|   |
|   +-- web/pcf/
|   |   +-- TabBar.pcf                             <-- [EDIT: ADD ROUNDTABLE MENU TAB]
|   |   +-- roundtable/                            <-- [NEW FOLDER: ALL ROUNDTABLE PCF FILES]
|   |       +-- RoundtableBriefListPage.pcf        <-- [LIST VIEW OF BRIEFS]
|   |       +-- RoundtableBriefDetailPage.pcf      <-- [DETAIL VIEW ENTRY POINT]
|   |       +-- RoundtableBriefDV.pcf              <-- [FORM FIELD DETAIL VIEW PANEL]
|   |
|   +-- resources/productmodel/                    <-- [OPTIONAL: COMPILED XML PRODUCT MODEL]
|       +-- products/
|       +-- policylinepatterns/
|
+-- gsrc/
|   +-- roundtable/                                <-- [NEW ROOT PACKAGE FOR GOSU CODE]
|       +-- client/
|       |   +-- RoundtableApiClient.gs             <-- [REST CLIENT FOR FASTAPI CALLS]
|       |
|       +-- web/
|       |   +-- RoundtableUIHelper.gs              <-- [PCF BUTTON & ACTION CONTROLLERS]
|       |
|       +-- apd/
|       |   +-- RoundtableToAPDService.gs          <-- [TRANSLATES BRIEF -> APD ENTITIES]
|       |
|       +-- entity/
|           +-- RoundtableBriefEnhancement.gsx     <-- [GOSU ENHANCEMENT FOR ENTITY]
|
+-- gtest/
    +-- roundtable/                                <-- [AUTOMATED GOSU UNIT & INTEGRATION TESTS]
        +-- RoundtableApiClientTest.gs
        +-- RoundtableToAPDServiceTest.gs
```

---

## 3. Detailed Component Breakdown

### 3.1 Custom Entity & Typelist Files
* **Custom Entity Definition (`.eti`)**:
  - Target Path: `modules/configuration/config/extensions/entity/RoundtableBrief.eti`
  - Defines the database table, columns, data types, indexes, and bean type (`type="retireable"`).
* **Extension to Existing Entity (`.etx`)**:
  - Target Path: `modules/configuration/config/extensions/entity/PolicyPeriod.Roundtable.etx` (if linking briefs to a specific policy submission).
* **Custom Typelist (`.tti`)**:
  - Target Path: `modules/configuration/config/extensions/typelist/RoundtableApprovalStatus.tti`
  - Defines allowable status codes (`Draft`, `PendingReview`, `Approved`, `Rejected`).
* **Display Name (`.en`)**:
  - Target Path: `modules/configuration/config/displaynames/RoundtableBrief.en`
  - Controls string representation when referenced in dropdowns, search results, or logs.

---

### 3.2 PCF UI Files
* **Roundtable UI Subpackage**:
  - Target Directory: `modules/configuration/config/web/pcf/roundtable/`
  - Files to place here:
    1. `RoundtableBriefListPage.pcf`: Table view of briefs.
    2. `RoundtableBriefDetailPage.pcf`: Individual brief inspector.
    3. `RoundtableBriefDV.pcf`: Inputs and text areas for evidence, citations, and 5 team signoffs.
* **Top Navigation Bar**:
  - Existing File: `modules/configuration/config/web/pcf/TabBar.pcf`
  - Add `<Tab id="RoundtableTab" action="RoundtableBriefListPage.go()" label="&quot;Roundtable Briefs&quot;"/>`.

---

### 3.3 Gosu Source Code (`gsrc/`)
All Gosu code must reside under `modules/configuration/gsrc/` using standard Java package naming conventions:

* **FastAPI HTTP / REST Client**:
  - Path: `modules/configuration/gsrc/roundtable/client/RoundtableApiClient.gs`
  - Handles outbound HTTP POST/GET to `http://localhost:8000` (or `ROUNDTABLE_API_URL`), JSON parsing with Jackson `ObjectMapper`, and error handling.
* **PCF Action & Workflow Helpers**:
  - Path: `modules/configuration/gsrc/roundtable/web/RoundtableUIHelper.gs`
  - Methods called by PCF buttons (`updateTeamStatus`, `pushToAPD`).
* **APD Model Integration Service**:
  - Path: `modules/configuration/gsrc/roundtable/apd/RoundtableToAPDService.gs`
  - Gosu service that creates `APDProduct`, `APDProductLine`, `APDCoverage`, and `APDTerm` entities in a transaction bundle.
* **Entity Enhancements (`.gsx`)**:
  - Path: `modules/configuration/gsrc/roundtable/entity/RoundtableBriefEnhancement.gsx`
  - Adds calculated properties (e.g. `brief.IsFullyApproved`) and domain methods directly to the `RoundtableBrief` entity.

---

### 3.4 Display Keys & Localization
* **UI Labels & Messages**:
  - Target Path: `modules/configuration/config/locale/display.properties`
  - Format:
    ```properties
    Roundtable.Brief.Title=Product Decision Brief
    Roundtable.Button.Approve=Approve Brief
    Roundtable.Button.Reject=Reject Brief
    Roundtable.Button.PushAPD=Push to APD
    Roundtable.Message.FullyApproved=All 5 multidisciplinary teams have approved this brief.
    ```
  - Accessed in PCF or Gosu as: `DisplayKey.get("Roundtable.Button.Approve")`.

---

## 4. Compilation & Verification Workflow

After placing files in these locations, use the Guidewire build wrapper (`gwb.bat` located at `C:\GW10\PolicyCenter\gwb.bat`):

1. **Regenerate Java Entities from `.eti` / `.tti`**:
   ```powershell
   cd C:\GW10\PolicyCenter
   .\gwb.bat genEntitySources
   ```
2. **Compile Gosu and Java Classes**:
   ```powershell
   cd C:\GW10\PolicyCenter
   .\gwb.bat compile
   ```
3. **Verify PCF Files**:
   ```powershell
   cd C:\GW10\PolicyCenter
   .\gwb.bat genPcfSources
   ```
4. **Start PolicyCenter Server**:
   ```powershell
   cd C:\GW10\PolicyCenter
   .\gwb.bat serverRun
   # Or launch via: "C:\GW10\PolicyCenter\Start PolicyCenter.lnk"
   ```
5. **Open Studio for Interactive Editing & Debugging**:
   - Launch: `"C:\GW10\PolicyCenter\Start PolicyCenter Studio.lnk"`
   - Studio automatically monitors `modules/configuration` and reloads PCFs, Gosu classes, and display keys with hot-swap enabled during local development.
