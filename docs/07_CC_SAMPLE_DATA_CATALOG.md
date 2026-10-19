# ClaimCenter Sample Data Catalog

**Guidewire ClaimCenter Version:** 10.2.1.1523 (Platform 10.201.1)
**Installation Location:** `C:\GW10\ClaimCenter`
**Extraction Date:** 2026-09-26

---

## Overview & Compliance

This catalog details the sample claims, policy snapshots, incident models, exposure structures, financial transactions, and reference datasets bundled within Guidewire ClaimCenter. All datasets are inspected strictly in read-only mode.

> [!NOTE]
> In strict compliance with extraction requirements, all realistic personal information (names, emails, phone numbers, addresses, account numbers, policy numbers, claim numbers, financial amounts) has been sanitized and replaced with `<SYNTHETIC_EXAMPLE>` while preserving the underlying schema structures, data types, and business relationships.

---

### Dataset: Personal Auto Claims & Financial Lifecycle
**Path:** `C:\GW10\ClaimCenter\modules\configuration\gsrc\gw\sampledata\SamplePersonalAutoClaims.gs`
**Format:** Gosu Class / Data Builder (`ClaimBuilder`, `PolicyBuilder`, `VehicleRUBuilder`, `ExposureBuilder`, `VehicleIncidentBuilder`, `InjuryIncidentBuilder`, `CheckSetBuilder`, `ReserveSetBuilder`, `ReserveLineBuilder`, `CheckBuilder`)
**Entity:** `Claim`, `Policy`, `VehicleRU`, `Vehicle`, `Exposure`, `VehicleIncident`, `InjuryIncident`, `ReserveLine`, `Reserve`, `Payment`, `Check`, `Activity`, `Note`
**Fields:**
- `ClaimNumber`: String (`<SYNTHETIC_EXAMPLE>`)
- `LossDate`: Date (`BaseDate - 10 days`)
- `LossCause`: TypeKey -> `LossCause` (`vehcollision`, `rearend`)
- `LossType`: TypeKey -> `LossType` (`AUTO`)
- `ClaimState`: TypeKey -> `ClaimState` (`open`)
- `Policy.PolicyNumber`: String (`<SYNTHETIC_EXAMPLE>`)
- `Policy.PolicyType`: TypeKey -> `PolicyType` (`PersonalAuto`)
- `Vehicle.VIN`: String (`<SYNTHETIC_EXAMPLE>`)
- `VehicleIncident.Severity`: TypeKey -> `SeverityType` (`minor`, `major_auto`)
- `Exposure.ExposureType`: TypeKey -> `ExposureType` (`vehicledamage`, `bodilyinjurydamage`, `generaldamage`)
- `Exposure.State`: TypeKey -> `ExposureState` (`open`)
- `Financials`: `ReserveLine` (Claim + Exposure + CostType `claimcost` + CostCategory `body`), `Reserve` amount, `Payment` amount, `Check` (Payee `<SYNTHETIC_EXAMPLE>`, PaymentMethod `check`)
**Relationships:**
- 1 `Claim` -> 1 `Policy` (snapshot or verified link)
- 1 `Claim` -> 1..N `Incident` (`VehicleIncident`, `InjuryIncident`)
- 1 `Claim` -> 1..N `Exposure` (each linked to an `Incident` and a `Coverage`)
- 1 `Exposure` -> 1..N `ReserveLine` -> 1..N `Transaction` (`Reserve`, `Payment`)
- 1 `CheckSet` -> 1 `Check` -> 1..N `Payment`
**Example structure:**
```gosu
var claim = new ClaimBuilder()
  .withClaimNumber("<SYNTHETIC_EXAMPLE>")
  .withLossDate(BaseDate.addDays(-10))
  .withLossCause(TC_VEHCOLLISION)
  .withLossType(TC_AUTO)
  .withPolicy(new PolicyBuilder()
    .withPolicyNumber("<SYNTHETIC_EXAMPLE>")
    .withPolicyType(TC_PERSONALAUTO))

var exposure = new ExposureBuilder()
  .onClaim(claim)
  .withExposureType(TC_VEHICLEDAMAGE)
  .withPrimaryCoverage(TC_PACOLLISIONCOV)
  .withIncident(new VehicleIncidentBuilder()
    .withSeverity(TC_MAJOR_AUTO)
    .withDescription("<SYNTHETIC_EXAMPLE>"))
  .create(bundle)

var checkSet = new CheckSetBuilder()
var reserveLine = new ReserveLineBuilder()
var check = new CheckBuilder()
  .onCheckSet(checkSet)
  .withPaymentMethod(TC_CHECK)
  .withPayee(findContact("<SYNTHETIC_EXAMPLE>"))
```

---

### Dataset: Commercial Auto Fleet Claims
**Path:** `C:\GW10\ClaimCenter\modules\configuration\gsrc\gw\sampledata\SampleCommercialAutoClaims.gs`
**Format:** Gosu Class / Data Builder
**Entity:** `Claim`, `Policy`, `CommercialDriver`, `VehicleRU`, `Exposure`, `VehicleIncident`
**Fields:**
- Commercial fleet policy with company named insured (`<SYNTHETIC_EXAMPLE>`)
- Multi-vehicle collision involving commercial tractor/trailer and third-party claimant
- Policy risk unit sequence numbers (`RUNumber`)
**Relationships:**
- Company named insured owning multiple vehicle risk units.
- Multiple third-party liability exposures linked to one commercial vehicle incident.
**Example structure:**
```gosu
var claim = new ClaimBuilder()
  .withClaimNumber("<SYNTHETIC_EXAMPLE>")
  .withLossType(TC_AUTO)
  .withPolicy(new PolicyBuilder()
    .withPolicyNumber("<SYNTHETIC_EXAMPLE>")
    .withPolicyType(TC_COMMERCIALAUTO))
```

---

### Dataset: Commercial Property Claims
**Path:** `C:\GW10\ClaimCenter\modules\configuration\gsrc\gw\sampledata\SampleCommercialPropertyClaims.gs`
**Format:** Gosu Class / Data Builder
**Entity:** `Claim`, `Policy`, `PropertyRU`, `FixedPropertyIncident`, `PropertyContentsIncident`, `Exposure`
**Fields:**
- `LossCause`: TypeKey -> `LossCause` (`fire`, `waterdamage`, `wind`)
- `FixedPropertyIncident`: Building damage, structural repairs, sprinkler leakage
- `PropertyContentsIncident`: Damaged stock, equipment, inventory
**Relationships:**
- 1 Claim -> 1..N `FixedPropertyIncident` (Building) + 1..N `PropertyContentsIncident` (Contents).
**Example structure:**
```gosu
var claim = new ClaimBuilder()
  .withClaimNumber("<SYNTHETIC_EXAMPLE>")
  .withLossCause(TC_FIRE)
  .withLossType(TC_PR)
  .withIncident(new FixedPropertyIncidentBuilder()
    .withPropertyDesc("<SYNTHETIC_EXAMPLE>")
    .withSeverity(TC_MAJOR_PROP))
```

---

### Dataset: General Liability Claims
**Path:** `C:\GW10\ClaimCenter\modules\configuration\gsrc\gw\sampledata\SampleGeneralLiabilityClaims.gs`
**Format:** Gosu Class / Data Builder
**Entity:** `Claim`, `Exposure`, `InjuryIncident`, `Matter`, `ClaimContact`
**Fields:**
- Slip and fall / premises liability claims
- `InjuryIncident`: Bodily injury, medical treatments, hospital records
- `Matter`: Attached litigation record with trial details and legal defense counsel
**Relationships:**
- Demonstrates relationship between third-party injury exposure and litigation (`Matter`).
**Example structure:**
```gosu
var claim = new ClaimBuilder()
  .withLossType(TC_GL)
  .withLossCause(TC_SLIPFALL)
  .withMatter(new MatterBuilder()
    .withMatterName("<SYNTHETIC_EXAMPLE>")
    .withTrialDate(BaseDate.addDays(120)))
```

---

### Dataset: Workers Compensation Claims
**Path:** `C:\GW10\ClaimCenter\modules\configuration\gsrc\gw\sampledata\SampleWorkersCompClaims.gs`
**Format:** Gosu Class / Data Builder
**Entity:** `Claim`, `Exposure`, `InjuryIncident`, `BodyPartDetails`, `ClaimContactRole`
**Fields:**
- `EmploymentInjury`: Boolean (`true`)
- `ClaimantRprtdDate`: Date
- `BodyPartDetails`: PrimaryBodyPart (`TC_TRUNK`, `TC_ARM`), DetailedBodyPart
- `LostWages`: Boolean (`true`)
**Relationships:**
- Injured worker linked as `Claimant` and `Employee`. Employer linked as `Insured`.
**Example structure:**
```gosu
var claim = new ClaimBuilder()
  .withLossType(TC_WC)
  .withEmploymentInjury(true)
  .withClaimant(findPerson("<SYNTHETIC_EXAMPLE>"))
  .withIncident(new InjuryIncidentBuilder()
    .withLostWages(true)
    .withMedicalTreatmentType(TC_HOSPITAL))
```

---

### Dataset: Homeowners Claims (HO2, HO4, HO5, HO6)
**Path:** `C:\GW10\ClaimCenter\modules\configuration\gsrc\gw\sampledata\SampleHOPClaimWithHO2Policy.gs`
**Format:** Gosu Class / Data Builder
**Entity:** `Claim`, `Policy`, `DwellingIncident`, `PropertyContentsIncident`, `LivingExpensesIncident`
**Fields:**
- Comprehensive homeowners perils (windstorm, frozen pipe burst, theft)
- `DwellingIncident`: Roof damage, interior water damage
- `LivingExpensesIncident`: Additional living expense (ALE) while dwelling uninhabitable
**Relationships:**
- Multi-incident structure: 1 Dwelling claim with concurrent contents loss and ALE exposure.
**Example structure:**
```gosu
var claim = new ClaimBuilder()
  .withLossType(TC_PR)
  .withIncident(new DwellingIncidentBuilder().withDescription("<SYNTHETIC_EXAMPLE>"))
  .withIncident(new LivingExpensesIncidentBuilder().withDescription("<SYNTHETIC_EXAMPLE>"))
```

---

### Dataset: Catastrophe Declarations
**Path:** `C:\GW10\ClaimCenter\modules\configuration\gsrc\gw\sampledata\SampleCatastrophes.gs`
**Format:** Gosu Class / Data Builder (`CatastropheBuilder`, `CatastropheZoneBuilder`)
**Entity:** `Catastrophe`, `CatastropheZone`, `CatastrophePeril`
**Fields:**
- `CatastropheNumber`: String (`<SYNTHETIC_EXAMPLE>`)
- `Name`: String (`<SYNTHETIC_EXAMPLE>`)
- `Type`: TypeKey -> `CatastropheType` (`iso`, `internal`)
- `CatastropheZone`: Postal codes and states in impact zone
**Relationships:**
- 1 `Catastrophe` links to multiple `Claim` instances occurring within the declared date/zone boundary.
**Example structure:**
```gosu
var cat = new CatastropheBuilder()
  .withName("<SYNTHETIC_EXAMPLE>")
  .withCatastropheNumber("<SYNTHETIC_EXAMPLE>")
  .withType(TC_ISO)
  .withCatastropheZone(new CatastropheZoneBuilder().withZoneName("<SYNTHETIC_EXAMPLE>"))
  .create(bundle)
```

---

### Dataset: Service Request Metric Limits
**Path:** `C:\GW10\ClaimCenter\modules\configuration\config\sampledata\servicerequestmetriclimits.xml`
**Format:** XML
**Entity:** `ServiceRequestMetricLimit`
**Fields:**
- `MetricUnit`: TypeKey -> `MetricUnit` (`days`, `hours`, `currency`)
- `TargetValue`: Decimal value for target completion SLA
- `YellowValue`, `RedValue`: Alert threshold levels
**Relationships:**
- Configures SLA monitoring thresholds for vendor service requests.
**Example structure:**
```xml
<ServiceRequestMetricLimit MetricUnit="days" TargetValue="3" YellowValue="5" RedValue="7"/>
```
