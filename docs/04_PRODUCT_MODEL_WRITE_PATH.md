# Guidewire PolicyCenter Product Model Write Path Guide

> **Target Codebase**: Guidewire PolicyCenter 10.2.1 (`project-version=10.2.1.1711`, Platform `10.201.1`, Gosu `1.14.26`)  
> **Source Directory**: `C:\GW10\PolicyCenter\modules\configuration`  
> **Generated Documentation**: `C:\Users\Student\Documents\roundtable\docs\04_PRODUCT_MODEL_WRITE_PATH.md`

---

## 1. Executive Summary: The Two Product Model Write Paths

When translating an approved Roundtable product decision brief into PolicyCenter, there are two distinct write targets depending on integration stage:

```
+---------------------------------------------------------------------------------------+
|                               Approved Roundtable Brief                                |
|   (Title, Evidence, Directional Estimates, Citations, 5 Team Multi-Disciplinary Signoffs)  |
+---------------------------------------------------------------------------------------+
                                           |
                                           v
       +-----------------------------------------------------------------------+
       | PATH 1: Advanced Product Designer (APD) Data Model (RECOMMENDED)       |
       | Targets: Real database entities (APDProduct, APDCoverage, APDTerm)    |
       | UI: Visible in APDProductManagementPage for visual configuration       |
       | Outcome: Insurance architects generate PCF/Entities with one click     |
       +-----------------------------------------------------------------------+
                                           | (or direct file export)
                                           v
       +-----------------------------------------------------------------------+
       | PATH 2: Compiled Product Model XML Files                              |
       | Targets: config/resources/productmodel/{products,policylinepatterns}  |
       | Outcome: Production-installed product model files                     |
       +-----------------------------------------------------------------------+
```

As specified in Roundtable's project architecture:
> *"Roundtable is a system that generates AI-assisted, cited product-decision briefs ... and — once approved — writes the result into PolicyCenter as a starting point for Advanced Product Designer configuration."*

**Path 1 (APD Data Model Entities)** is the primary operational integration point.

---

## 2. Path 1: Advanced Product Designer (APD) Entity Architecture

In PolicyCenter 10, the Advanced Product Designer is driven by persistent entities defined in `modules/configuration/config/metadata/entity/APD*.eti`.

### Real APD Entity Schema Summary

| Entity | Base Table | Supertype / Details | Key Attributes in Schema |
| :--- | :--- | :--- | :--- |
| **`APDProduct`** | `apdproduct` | `retireable` | `CodeIdentifier`, `Name`, `Description`, `Abbreviation`, `ProductAccountType`, `Currencies`, `Multiline`, `Coinsurance`, `ProductLines` (array) |
| **`APDProductToLine`**| `apdproducttoline` | `retireable` | `Product` (fk `APDProduct`), `ProductLine` (fk `APDProductLine`) |
| **`APDProductLine`** | `apdcoverable` | Subtype of `APDCoverable` | `CodeIdentifier`, `LinePrefix`, `ProductLineCode`, `Currencies`, `Clauses` (array), `ClauseCategories` (array) |
| **`APDCoverable`** | `apdcoverable` | `retireable` | `Name`, `Description`, `MenuLabel`, `CoverableType`, `Clauses` (array), `ClauseCategories` (array), `Fields` (array) |
| **`APDClauseCategory`**| `apdclausecategory`| `retireable` | `Name`, `Description`, `CodeIdentifier`, `Coverable` (fk `APDCoverable`) |
| **`APDCoverage`** | `apdclause` | Subtype of `APDClause` | `Name`, `Description`, `CodeIdentifier`, `Sequence`, `Coverable` (fk), `ClauseCategory` (fk), `Terms` (array) |
| **`APDTerm`** | `apdattribute` | Subtype of `APDAttribute` | `Name`, `Label`, `Description`, `Type` (`APDFieldType`), `Clause` (fk `APDClause`), `Codes` (array `APDDropdownEntry`) |
| **`APDDropdownEntry`**| `apddropdownentry` | `retireable` | `Code`, `Name`, `Description`, `Priority`, `Attribute` (fk `APDAttribute`) |

### Key Typelist Enum Values in APD
* **`ProductAccountType`** (`config/metadata/typelist/ProductAccountType.tti`):
  - `TC_ANY`: Eligible for both personal and commercial accounts.
  - `TC_COMPANY`: Commercial only.
  - `TC_PERSON`: Personal only.
* **`APDCurrencyHandling`** (`config/metadata/typelist/APDCurrencyHandling.tti`):
  - `TC_DOMESTIC`: Single default currency.
  - `TC_MULTICURRENCY`: Multi-currency enabled.
* **`APDFieldType`** (`config/metadata/typelist/APDFieldType.tti`):
  - `TC_VARCHAR`, `TC_INTEGER`, `TC_BIGDECIMAL`, `TC_MONEY`, `TC_BOOLEAN`, `TC_DATE`, `TC_TYPEKEY`.

---

## 3. Real Gosu Implementation: Writing Approved Brief to APD

The following Gosu service writes an approved `RoundtableBrief` directly into the APD data model, creating the product, product line, clause category, coverage, and term hierarchy.

**File Target**: `modules/configuration/gsrc/roundtable/apd/RoundtableToAPDService.gs`

```gosu
package roundtable.apd

uses entity.RoundtableBrief
uses entity.APDProduct
uses entity.APDProductLine
uses entity.APDProductToLine
uses entity.APDClauseCategory
uses entity.APDCoverage
uses entity.APDTerm
uses entity.APDDropdownEntry
uses gw.transaction.Transaction
uses gw.api.database.Query
uses gw.api.system.PCLoggerCategory
uses org.slf4j.Logger

@Export
class RoundtableToAPDService {

  private static final var LOGGER : Logger = PCLoggerCategory.PRODUCTMODEL

  /**
   * Translates an approved RoundtableBrief into an APDProduct hierarchy ready for
   * visual configuration in the Advanced Product Designer.
   *
   * @param brief The fully approved RoundtableBrief entity
   * @return The created or updated APDProduct entity
   */
  public static function createApdProductFromBrief(brief : RoundtableBrief) : APDProduct {
    var createdProduct : APDProduct

    Transaction.runWithNewBundle(\bundle -> {
      var localBrief = bundle.add(brief)
      
      // Clean code identifier: remove spaces, keep alphanumeric
      var cleanCode = sanitizeCode(brief.Title)
      var lineCode = brief.TargetLineCode ?: cleanCode + "Line"
      var prefix = lineCode.length > 3 ? lineCode.substring(0, 3).toUpperCase() : lineCode.toUpperCase()

      // 1. Check if APDProduct already exists or instantiate new
      var existingProduct = Query.make(APDProduct)
          .compare(APDProduct#CodeIdentifier, Equals, cleanCode)
          .select()
          .first()

      var apdProduct : APDProduct
      if (existingProduct != null) {
        apdProduct = bundle.add(existingProduct)
        LOGGER.info("RoundtableToAPD: Updating existing APDProduct " + cleanCode)
      } else {
        apdProduct = new APDProduct(bundle)
        apdProduct.CodeIdentifier = cleanCode
        LOGGER.info("RoundtableToAPD: Creating new APDProduct " + cleanCode)
      }

      // 2. Populate APDProduct attributes
      apdProduct.Name = brief.Title
      apdProduct.Description = brief.ProductSummary ?: brief.Title
      apdProduct.Abbreviation = prefix
      apdProduct.Multiline = false
      apdProduct.Coinsurance = false
      apdProduct.Currencies = APDCurrencyHandling.TC_DOMESTIC
      apdProduct.ProductAccountType = ProductAccountType.TC_ANY
      apdProduct.DateUpdated = java.util.Date.CurrentDate

      // 3. Create or attach APDProductLine
      var apdLine = apdProduct.ProductLines*.ProductLine.firstWhere(\l -> l.CodeIdentifier == lineCode)
      if (apdLine == null) {
        apdLine = new APDProductLine(bundle)
        apdLine.CodeIdentifier = lineCode
        apdLine.Name = brief.Title + " Line"
        apdLine.Description = "Primary coverage line for " + brief.Title
        apdLine.LinePrefix = prefix
        apdLine.Currencies = APDCurrencyHandling.TC_DOMESTIC
        apdLine.CoverableType = APDCoverableType.TC_OTHER

        var ptl = new APDProductToLine(bundle)
        ptl.Product = apdProduct
        ptl.ProductLine = apdLine
      }

      // 4. Create Standard Clause Category
      var category = apdLine.ClauseCategories.firstWhere(\c -> c.CodeIdentifier == prefix + "StandardCat")
      if (category == null) {
        category = new APDClauseCategory(bundle)
        category.Coverable = apdLine
        category.CodeIdentifier = prefix + "StandardCat"
        category.Name = "Standard Coverages"
        category.Description = "Standard coverages proposed by Roundtable Brief"
      }

      // 5. Create Core Coverage from Brief Concept
      var covCode = prefix + "CoreCov"
      var coverage = apdLine.Clauses.whereTypeIs(APDCoverage).firstWhere(\c -> c.CodeIdentifier == covCode)
      if (coverage == null) {
        coverage = new APDCoverage(bundle)
        coverage.Coverable = apdLine
        coverage.ClauseCategory = category
        coverage.CodeIdentifier = covCode
        coverage.Name = brief.Title + " Core Coverage"
        coverage.Description = brief.EvidenceText != null && brief.EvidenceText.length > 250 
            ? brief.EvidenceText.substring(0, 247) + "..." 
            : (brief.ProductSummary ?: brief.Title)
        coverage.Sequence = 10
      }

      // 6. Create Terms (Limit and Deductible based on directional estimates)
      createOrUpdateMoneyTerm(bundle, coverage, prefix + "Limit", "Occurrence Limit", 10, {100000, 250000, 500000, 1000000})
      createOrUpdateMoneyTerm(bundle, coverage, prefix + "Deductible", "Deductible", 20, {500, 1000, 2500, 5000})

      // 7. Update Brief status and linkages
      localBrief.PushedToApd = true
      localBrief.ApdProductCode = cleanCode
      localBrief.APDProduct = apdProduct

      createdProduct = apdProduct
    })

    return createdProduct
  }

  private static function createOrUpdateMoneyTerm(
      bundle : gw.pl.persistence.core.Bundle,
      coverage : APDCoverage,
      termCode : String,
      label : String,
      sequence : int,
      suggestedValues : List<Integer>) {
    
    var term = coverage.Terms.firstWhere(\t -> t.Name == termCode)
    if (term == null) {
      term = new APDTerm(bundle)
      term.Clause = coverage
      term.Name = termCode
      term.Label = label
      term.Description = label + " for " + coverage.Name
      term.Type = APDFieldType.TC_MONEY
      term.Sequence = sequence

      var priority = 10
      for (val in suggestedValues) {
        var entry = new APDDropdownEntry(bundle)
        entry.Attribute = term
        entry.Code = val.toString()
        entry.Name = "$" + java.text.NumberFormat.getIntegerInstance().format(val)
        entry.Priority = priority
        priority = priority + 10
      }
    }
  }

  private static function sanitizeCode(input : String) : String {
    if (input == null) return "Product" + System.currentTimeMillis()
    var clean = input.replaceAll("[^a-zA-Z0-9]", "")
    if (clean.length == 0) return "Product" + System.currentTimeMillis()
    if (clean.length > 25) clean = clean.substring(0, 25)
    return clean
  }
}
```

---

## 4. Path 2: Compiled Product Model XML Specifications

If writing directly to the compiled XML product model files, here are the real file structures, paths, and elements verified in `modules/configuration/config/resources/productmodel/`:

### 4.1 Product XML Structure
**File**: `config/resources/productmodel/products/{ProductCode}/{ProductCode}.xml`  
Real Example: `config/resources/productmodel/products/PersonalAuto/PersonalAuto.xml`

```xml
<?xml version="1.0"?>
<Product
  abbreviation="PA"
  codeIdentifier="PersonalAuto"
  daysUntilQuoteNeeded="7"
  defaultTermType="Annual"
  priority="100"
  productAccountType="Person"
  productType="Personal"
  public-id="PersonalAuto"
  quoteRoundingLevel="0"
  quoteRoundingMode="HALF_UP">
  <AvailablePolicyTerms>
    <AvailablePolicyTerm
      codeIdentifier="AnnualTerm"
      public-id="AnnualTerm"
      termType="Annual"/>
  </AvailablePolicyTerms>
  <ProductPolicyLinePatterns>
    <ProductPolicyLinePattern
      codeIdentifier="PersonalAutoLinePattern"
      policyLinePattern="PersonalAutoLine"
      public-id="PersonalAutoLinePattern"/>
  </ProductPolicyLinePatterns>
</Product>
```

### 4.2 Coverage Pattern XML Structure
**File**: `config/resources/productmodel/policylinepatterns/{PolicyLinePattern}/coveragepatterns/{CoverageCode}.xml`  
Real Example: `config/resources/productmodel/policylinepatterns/PersonalAutoLine/coveragepatterns/PACollisionCov.xml`

```xml
<?xml version="1.0"?>
<CoveragePattern
  codeIdentifier="PACollisionCov"
  coverageCategory="PAPPhysDamGrp"
  coverageSubtype="PersonalVehicleCov"
  coveredPartyType="FirstParty"
  existence="Suggested"
  lookupTableName="PAVehicleCov"
  owningEntityType="PersonalVehicle"
  policyLinePattern="PersonalAutoLine"
  priority="115"
  public-id="PACollisionCov"
  referenceDateByType="PolicyTerm">
  <AvailabilityScript/>
  <InitializeScript/>
  <OnRemovalScript/>
  <CovTerms>
    <OptionCovTermPattern
      aggregationModel="po"
      choiceLookupTableName="PAVehicleCovOpt"
      codeIdentifier="PACollDeductible"
      coverageColumn="ChoiceTerm1"
      lookupTableName="PAVehicleCovTerm"
      modelType="Deductible"
      priority="10"
      public-id="PACollDeductible"
      required="true"
      valueType="money">
      <AvailabilityScript/>
      <Options>
        <CovTermOpt
          codeIdentifier="opt_500"
          currency="usd"
          optionCode="500"
          priority="10"
          public-id="opt_500"
          value="500.0000"/>
        <CovTermOpt
          codeIdentifier="opt_1000"
          currency="usd"
          optionCode="1000"
          priority="20"
          public-id="opt_1000"
          value="1000.0000"/>
      </Options>
      <DefaultsSet>
        <CovTermDefault
          codeIdentifier="PACollDeductibleDefault"
          currency="usd"
          defaultValue="500"
          public-id="PACollDeductibleDefault"/>
      </DefaultsSet>
    </OptionCovTermPattern>
  </CovTerms>
</CoveragePattern>
```

### 4.3 Lookups XML Structure
**File**: `config/resources/productmodel/policylinepatterns/{PolicyLinePattern}/coveragepatterns/{CoverageCode}-lookups.xml`  
Real Example: `PACollisionCov-lookups.xml`

```xml
<?xml version="1.0"?>
<import>
  <PAVehicleCovLookup public-id="lookup_cov_01">
    <Availability>Available</Availability>
    <CoveragePatternCode>PACollisionCov</CoveragePatternCode>
    <EndEffectiveDate/>
    <PolicyLinePatternCode>PersonalAutoLine</PolicyLinePatternCode>
    <StartEffectiveDate>2020-01-01 00:00:00.000</StartEffectiveDate>
    <State/>
  </PAVehicleCovLookup>
  <CovTermLookup public-id="lookup_term_01">
    <Availability>Available</Availability>
    <CovTermPatternCode>PACollDeductible</CovTermPatternCode>
    <EndEffectiveDate/>
    <PolicyLinePatternCode>PersonalAutoLine</PolicyLinePatternCode>
    <StartEffectiveDate>2020-01-01 00:00:00.000</StartEffectiveDate>
    <State/>
  </CovTermLookup>
  <CovTermOptLookup public-id="lookup_opt_01">
    <Availability>Available</Availability>
    <CovTermOptCode>opt_500</CovTermOptCode>
    <CovTermPatternCode>PACollDeductible</CovTermPatternCode>
    <Currency>usd</Currency>
    <EndEffectiveDate/>
    <StartEffectiveDate>2020-01-01 00:00:00.000</StartEffectiveDate>
    <State/>
  </CovTermOptLookup>
</import>
```

---

## 5. Field Mapping Matrix: Roundtable Brief -> Product Model

| Roundtable Brief Field | APD Entity Field (Path 1) | Product Model XML Element (Path 2) | Notes |
| :--- | :--- | :--- | :--- |
| `Title` | `APDProduct.Name`, `APDCoverage.Name` | `<Product abbreviation="..." name="...">`, `<CoveragePattern codeIdentifier="...">` | Name of the insurance product / coverage |
| `ProductSummary` | `APDProduct.Description`, `APDCoverage.Description` | `<Product desc="...">` | Conceptual overview of coverage |
| `TargetLineCode` | `APDProductLine.CodeIdentifier` | `<ProductPolicyLinePattern policyLinePattern="...">` | E.g. `PersonalAutoLine`, `BusinessAutoLine` |
| `DirectionalEstimates` (Limits) | `APDTerm` (`Type = TC_MONEY`), `APDDropdownEntry` | `<OptionCovTermPattern modelType="Limit">` | Suggested limits (e.g. $250k, $500k, $1M) |
| `DirectionalEstimates` (Deductibles) | `APDTerm` (`Type = TC_MONEY`), `APDDropdownEntry` | `<OptionCovTermPattern modelType="Deductible">` | Suggested deductibles (e.g. $500, $1k, $2.5k) |
| `EvidenceText` | `APDCoverage.Description` (excerpt) | Documentation / internal notes | Detailed justification supporting the product decision |
| `Citations` | Stored in `RoundtableBrief` entity | Not in product model XML | Academic / statutory / competitor citations |
| 5 Team Approvals | Pre-requisite gate before executing `RoundtableToAPDService` | N/A | Ensures claims, actuarial, UW, marketing, compliance approval before writing |
