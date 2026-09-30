# PolicyCenter Sample Data Catalog

**Guidewire PolicyCenter Version:** 10.2.1.1711 (Platform 10.201.1)
**Installation Location:** `C:\GW10\PolicyCenter`
**Extraction Date:** 2026-09-26

---

## Overview & Compliance

This catalog analyzes sample, reference, and demo datasets bundled with Guidewire PolicyCenter. All datasets are inspected strictly in read-only mode.

> [!NOTE]
> In strict adherence to extraction instructions, all realistic personal information (names, emails, phone numbers, addresses, account numbers, policy numbers, financial sums) has been sanitized and replaced with `<SYNTHETIC_EXAMPLE>` while preserving the underlying data types, schema structures, and business relationships.

---

### Dataset: Small Sample Accounts
**Path:** `C:\GW10\PolicyCenter\modules\configuration\gsrc\gw\sampledata\small\SmallSampleAccountData.gs`
**Format:** Gosu Class / Data Builder (`AccountBuilder`, `AccountContactBuilder`, `AccountLocationBuilder`)
**Entity:** `Account`, `AccountLocation`, `AccountContact`, `Contact`, `IndustryCode`
**Fields:**
- `AccountNumber`: String (`<SYNTHETIC_EXAMPLE>`)
- `PublicId`: String (`pc:ds:1`)
- `AccountHolderContact`: Contact reference (Company / Person)
- `IndustryCode`: ForeignKey -> IndustryCode (`1522` - General Contractors)
- `AccountLocation`: Array -> AccountLocation (`State: TC_TX`, `TC_NY`)
- `AccountContactRole`: Driver, AccountHolder
**Relationships:**
- 1 Account -> 1 AccountHolderContact (`Company` or `Person`)
- 1 Account -> 1..N `AccountLocation` records
- 1 Account -> 1..N `AccountContact` records with roles (`Driver`, `NamedInsured`)
**Example structure:**
```gosu
var builder = new AccountBuilder(false)
  .withPublicId("<SYNTHETIC_EXAMPLE>")
  .withAccountHolderContact(findCompany("<SYNTHETIC_EXAMPLE>", "<SYNTHETIC_EXAMPLE>"))
  .withAccountNumber("<SYNTHETIC_EXAMPLE>")
  .withIndustryCode(findIndustryCode("<SYNTHETIC_EXAMPLE>"))
  .withAccountLocation(new AccountLocationBuilder(1).withState(TC_TX))
  .withAccountContact(new AccountContactBuilder().asDriver().withContact(buildDriver("<SYNTHETIC_EXAMPLE>","<SYNTHETIC_EXAMPLE>")))
```

---

### Dataset: Small Sample Policies & Job Chains
**Path:** `C:\GW10\PolicyCenter\modules\configuration\gsrc\gw\sampledata\small\SmallSamplePolicyData.gs`
**Format:** Gosu Class / Data Builder (`SubmissionBuilder`, `RenewalBuilder`, `CancellationBuilder`, `ReinstatementBuilder`)
**Entity:** `Policy`, `PolicyPeriod`, `Job`, `Submission`, `PolicyChange`, `Renewal`, `Cancellation`, `Reinstatement`
**Fields:**
- `JobNumber`: String (`<SYNTHETIC_EXAMPLE>`)
- `AccountNumber`: String reference (`<SYNTHETIC_EXAMPLE>`)
- `Product`: Product pattern (`PersonalAuto`, `BusinessOwners`, `HOPHomeowners`, `WorkersComp`)
- `EffectiveDate`: Date (`BaseDate - 30 days`)
- `BasedOnPeriod`: ForeignKey -> PolicyPeriod (Points to prior bound period)
**Relationships:**
- Demonstrates strict linear Job Chains:
  `Submission (Bound)` -> `PolicyChange (Bound)` -> `Renewal (Bound)` -> `Cancellation (Flat Refund)` -> `Reinstatement (Active)` -> `Renewal`
**Example structure:**
```gosu
// Submission initiates policy
period = loadSubmission("<SYNTHETIC_EXAMPLE>", "<SYNTHETIC_EXAMPLE>", PCCoercions.makeProductModel<Product>("PersonalAuto"), SampleDataConstants.getBaseDateMinus(30), new String[0], true)

// Policy Change modifies existing period
new PolicyChangeBuilder()
  .withJobNumber("<SYNTHETIC_EXAMPLE>")
  .withBasedOnPeriod(findPeriodByJobNumber("<SYNTHETIC_EXAMPLE>", bundle))
  .create(bundle)

// Cancellation cancels policy with refund option
new CancellationBuilder()
  .withJobNumber("<SYNTHETIC_EXAMPLE>")
  .withBasedOnPeriod(findPeriodByJobNumber("<SYNTHETIC_EXAMPLE>", bundle))
  .canceledByCarrier()
  .withFlatRefund()
  .create(bundle)
```

---

### Dataset: Tiny Sample Community & Organization Data
**Path:** `C:\GW10\PolicyCenter\modules\configuration\gsrc\gw\sampledata\tiny\TinySampleCommunityData.gs`
**Format:** Gosu Class / Data Builder (`OrganizationBuilder`, `ProducerCodeBuilder`, `GroupBuilder`, `UserBuilder`)
**Entity:** `Organization`, `ProducerCode`, `Group`, `User`, `Role`
**Fields:**
- `Organization.Name`: String (`<SYNTHETIC_EXAMPLE>`)
- `Organization.Type`: TypeKey -> `BusinessType` (`agency`, `carrier`)
- `ProducerCode.Code`: String (`<SYNTHETIC_EXAMPLE>`)
- `ProducerCode.Status`: TypeKey -> `ProducerStatus` (`active`)
- `User.Credential.UserName`: String (`<SYNTHETIC_EXAMPLE>`)
**Relationships:**
- 1 Organization -> 1..N `ProducerCode` records
- 1 Organization -> 1 Root `Group` -> 1..N Child `Group` records
- 1 Group -> 1..N `User` members
**Example structure:**
```gosu
var agency = new OrganizationBuilder()
  .withName("<SYNTHETIC_EXAMPLE>")
  .withType(BusinessType.TC_AGENCY)
  .withProducerCode(new ProducerCodeBuilder().withCode("<SYNTHETIC_EXAMPLE>").withStatus(TC_ACTIVE))
  .create(bundle)
```

---

### Dataset: Large Sample Enterprise Policies
**Path:** `C:\GW10\PolicyCenter\modules\configuration\gsrc\gw\sampledata\large\LargeSamplePolicyData.gs`
**Format:** Gosu Class / Scenario Builder
**Entity:** `PolicyPeriod`, `PersonalAutoLine`, `CPLine`, `BOPLine`, `PersonalVehicle`, `CPBuilding`, `BOPLocation`
**Fields:**
- `PolicyNumber`: String (`<SYNTHETIC_EXAMPLE>`)
- `PolicyPeriodStatus`: TypeKey -> `PolicyPeriodStatus` (`Bound`)
- `BaseState`: TypeKey -> `Jurisdiction` (`TC_CA`, `TC_TX`, `TC_IL`)
- `TermType`: TypeKey -> `TermType` (`Annual`, `SixMonths`)
- Coverables: Vehicles with VIN, Year, Make, Model; Buildings with ConstructionType, Sprinklered
**Relationships:**
- Complex commercial and personal line structures with multiple vehicles, multi-state locations, and attached underwriting rules.
**Example structure:**
```gosu
var period = new PolicyPeriodBuilder()
  .withPolicyNumber("<SYNTHETIC_EXAMPLE>")
  .withPeriodStatus(PolicyPeriodStatus.TC_BOUND)
  .withTermType(TermType.TC_ANNUAL)
  .withBaseState(Jurisdiction.TC_CA)
  .create(bundle)
```

---

### Dataset: Workers Compensation Demo Ratebook
**Path:** `C:\GW10\PolicyCenter\modules\configuration\config\content\ratebooks\WC7_RTM_Demo_Rating-v1.xml`
**Format:** XML (`<RateBook>`)
**Entity:** `RateBook`, `RateTableDefinition`, `RateTable`, `RateFactorRow`, `CalcRoutineDefinition`
**Fields:**
- `BookCode`: String (`WC7_RTM_Demo_Rating`)
- `BookName`: String (`WC7 Demo Rating Rate Book`)
- `Edition`: String (`1`)
- `Status`: TypeKey -> `RateBookStatus` (`Stage`, `Approved`, `Active`)
- `PolicyLine`: String (`WC7Line`)
**Relationships:**
- 1 `RateBook` contains multiple `RateTable` instances mapped to rating routines.
**Example structure:**
```xml
<RateBook
  BookCode="WC7_RTM_Demo_Rating"
  BookEdition="1"
  BookName="WC7 Demo Rating Rate Book"
  PolicyLine="WC7Line"
  Status="Active">
  <RateTables>
    <RateTable Definition="WC7BaseRates"/>
  </RateTables>
</RateBook>
```

---

### Dataset: Vendor Specialist Service Tree
**Path:** `C:\GW10\PolicyCenter\modules\configuration\config\sampledata\vendorservicetree.xml`
**Format:** XML (`<SpecialistServices>`)
**Entity:** `SpecialistService`
**Fields:**
- `Code`: String (Unique service hierarchical code)
- `Name`: String (Service description)
- `Parent`: Hierarchical parent service code
**Relationships:**
- Self-referential tree defining taxonomy of specialist vendor services.
**Example structure:**
```xml
<SpecialistService Code="AutoRepair" Name="Auto Repair">
  <SpecialistService Code="BodyShop" Name="Auto Body Repair"/>
  <SpecialistService Code="Glass" Name="Auto Glass Repair"/>
</SpecialistService>
```
