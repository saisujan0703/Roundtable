# Synthetic Insurance Data Generation Schema

**Guidewire Suite Version:** 10.2.1
**Source Installations:** PolicyCenter (`C:\GW10\PolicyCenter`) & ClaimCenter (`C:\GW10\ClaimCenter`)
**Extraction Date:** 2026-09-26

---

## 1. Overview & Specification Standards

This schema specifies the exact rules, constraints, data types, verified typelist allowed values, and generation strategies for producing synthetic insurance datasets suitable for Guidewire PolicyCenter and ClaimCenter.

> [!IMPORTANT]
> All allowed values for `TypeKey` enumerations are strictly grounded in verified source typelist definitions (`.tti` and `.ttx` files) extracted from this environment. No codes are fabricated.

---

## 2. PolicyCenter Synthetic Entity Specifications

### Entity: Account
**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Account.eti`
**Entity Type:** `retireable`

#### AccountNumber
- **Type:** `String (varchar 30)`
- **Required:** Yes (Business requirement)
- **Allowed Values:** Alphanumeric sequence
- **Relationship:** Unique business identifier
- **Generation Strategy:** `ACC-SYN-{7 digits}` (e.g. `ACC-SYN-1049281`)
- **Example Synthetic Value:** `ACC-SYN-4829105`

#### AccountStatus
- **Type:** `TypeKey -> AccountStatus`
- **Required:** Yes
- **Allowed Values:** `Active`, `Pending`, `Withdrawn`, `Merged`
- **Relationship:** Account status lifecycle
- **Generation Strategy:** Weighted pick: `Active` (90%), `Pending` (5%), `Withdrawn` (3%), `Merged` (2%)
- **Example Synthetic Value:** `Active`

#### AccountOrgType
- **Type:** `TypeKey -> AccountOrgType`
- **Required:** No
- **Allowed Values:** `individual`, `solepropship`, `partnership`, `corporation`, `privatecorp`, `llc`, `jointventure`, `commonownership`, `limitedpartnership`, `trustestate`, `executortrustee`, `llp`, `government`, `nonprofit`, `religious`, `other`
- **Relationship:** Determines legal structure
- **Generation Strategy:** `individual` for personal lines; `corporation`, `llc`, or `partnership` for commercial lines
- **Example Synthetic Value:** `llc`

#### PreferredCoverageCurrency
- **Type:** `TypeKey -> Currency`
- **Required:** Yes
- **Allowed Values:** `usd`, `eur`, `gbp`, `cad`, `aud`, `jpy`, `rub`
- **Relationship:** Currency model
- **Generation Strategy:** Constant `usd` for US domestic portfolios
- **Example Synthetic Value:** `usd`

#### AccountHolderContact
- **Type:** `ForeignKey -> Contact`
- **Required:** Yes
- **Relationship:** 1 Account -> 1 primary Contact (`Person` or `Company`)
- **Generation Strategy:** Reference to existing synthetic Contact record
- **Example Synthetic Value:** Reference: `Contact[PublicID=syn:cont:1001]`

#### PrimaryLocation
- **Type:** `ForeignKey -> AccountLocation`
- **Required:** Yes
- **Relationship:** 1 Account -> 1 primary AccountLocation
- **Generation Strategy:** Reference to existing synthetic AccountLocation record
- **Example Synthetic Value:** Reference: `AccountLocation[PublicID=syn:loc:101]`

---

### Entity: Contact (Subtypes: Person, Company)
**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Contact.eti`
**Subtype Sources:** `Person.eti`, `Company.eti`
**Entity Type:** `retireable`

#### Subtype
- **Type:** `TypeKey -> Contact`
- **Required:** Yes
- **Allowed Values:** `Person`, `Company`, `PersonVendor`, `CompanyVendor`, `Place`
- **Generation Strategy:** Direct instantiation based on target policy product
- **Example Synthetic Value:** `Person`

#### FirstName / LastName (Person)
- **Type:** `String (varchar 30)`
- **Required:** Yes (for Person)
- **Allowed Values:** Realistic western names dictionary
- **Generation Strategy:** Random pick from realistic census first/last name tables
- **Example Synthetic Value:** `FirstName: Eleanor`, `LastName: Vance`

#### Name (Company)
- **Type:** `String (varchar 60)`
- **Required:** Yes (for Company)
- **Allowed Values:** Realistic corporate naming conventions
- **Generation Strategy:** Combination of `{ProperNoun} + {IndustryTerm} + {OrgSuffix}`
- **Example Synthetic Value:** `Apex Logistics Solutions, LLC`

#### PrimaryPhone
- **Type:** `TypeKey -> PrimaryPhoneType`
- **Required:** No
- **Allowed Values:** `home`, `work`, `mobile`
- **Generation Strategy:** Random selection
- **Example Synthetic Value:** `mobile`

#### PrimaryAddress
- **Type:** `ForeignKey -> Address`
- **Required:** No (verifiable in schema), Yes (business practical)
- **Relationship:** Contact primary mailing/billing location
- **Generation Strategy:** Reference to synthetic Address record
- **Example Synthetic Value:** Reference: `Address[PublicID=syn:addr:201]`

---

### Entity: Address
**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Address.eti`
**Entity Type:** `retireable`

#### AddressLine1
- **Type:** `String (varchar 60)`
- **Required:** Yes
- **Generation Strategy:** `{StreetNumber} + {StreetName} + {StreetType}`
- **Example Synthetic Value:** `742 Evergreen Terrace`

#### City
- **Type:** `String (varchar 60)`
- **Required:** Yes
- **Generation Strategy:** Pick from valid US Cities database
- **Example Synthetic Value:** `Springfield`

#### State
- **Type:** `TypeKey -> State`
- **Required:** Yes
- **Allowed Values:** `CA`, `TX`, `NY`, `FL`, `IL`, `PA`, `OH`, `WA`, `CO`, `GA`, etc.
- **Generation Strategy:** Valid state matching city and postal code
- **Example Synthetic Value:** `IL`

#### PostalCode
- **Type:** `String (varchar 60)`
- **Required:** Yes
- **Generation Strategy:** Valid 5-digit ZIP matching state
- **Example Synthetic Value:** `62704`

#### Country
- **Type:** `TypeKey -> Country`
- **Required:** Yes
- **Allowed Values:** `US`, `CA`, `GB`, `AU`, `DE`, `FR`, `JP`
- **Generation Strategy:** Constant `US`
- **Example Synthetic Value:** `US`

---

### Entity: Policy & PolicyPeriod
**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Policy.eti` & `PolicyPeriod.eti`
**Entity Type:** Policy is `effdatedcontainer`; PolicyPeriod is `effdatedbranch`

#### Policy.ProductCode
- **Type:** `patterncode (varchar 64)`
- **Required:** Yes
- **Allowed Values:** `PersonalAuto`, `CommercialProperty`, `BusinessAuto`, `BusinessOwners`, `CommercialPackage`, `GeneralLiability`, `HOPHomeowners`, `InlandMarine`, `Manual`, `WorkersComp`, `WC7WorkersComp`
- **Generation Strategy:** Direct assignment based on simulated portfolio distribution
- **Example Synthetic Value:** `PersonalAuto`

#### PolicyPeriod.PolicyNumber
- **Type:** `policynumber (varchar 40)`
- **Required:** Yes (for Bound policies)
- **Generation Strategy:** `POL-SYN-{8 digits}`
- **Example Synthetic Value:** `POL-SYN-91823746`

#### PolicyPeriod.Status
- **Type:** `TypeKey -> PolicyPeriodStatus`
- **Required:** Yes
- **Allowed Values:** `Draft`, `Quoting`, `Quoted`, `Bound`, `Declined`, `NotTaken`, `Expired`, `Withdrawn`, `NonRenewed`, `Canceling`, `Canceled`, `Rescinded`, `Audit`
- **Generation Strategy:** `Bound` (85%) for in-force book of business; `Draft`, `Quoted`, `Canceled` for pipeline
- **Example Synthetic Value:** `Bound`

#### PolicyPeriod.PeriodStart / PeriodEnd
- **Type:** `datetime`
- **Required:** Yes
- **Generation Strategy:** `PeriodStart` = Random date within past 2 years; `PeriodEnd` = `PeriodStart + 1 year` (or `6 months` for Personal Auto)
- **Example Synthetic Value:** `PeriodStart: 2025-01-15T00:00:00Z`, `PeriodEnd: 2026-01-15T00:00:00Z`

#### PolicyPeriod.TermNumber
- **Type:** `integer`
- **Required:** Yes
- **Generation Strategy:** `1` for new submissions; `2..N` for renewals
- **Example Synthetic Value:** `1`

---

### Entity: PersonalVehicle
**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PersonalVehicle.eti`
**Entity Type:** `effdated`

#### Vin
- **Type:** `vin (varchar 40)`
- **Required:** Yes
- **Allowed Values:** 17-character standard ISO 3779 VIN format
- **Generation Strategy:** Valid 17-character synthetic VIN generator with valid check digit
- **Example Synthetic Value:** `1HGCR2F83HA039281`

#### Year / Make / Model
- **Type:** `integer` / `varchar 40` / `varchar 40`
- **Required:** Yes
- **Generation Strategy:** Linked tuple from realistic vehicle make/model database
- **Example Synthetic Value:** `Year: 2021`, `Make: Honda`, `Model: Accord`

#### LicensePlate / LicensePlateState
- **Type:** `varchar 40` / `TypeKey -> State`
- **Required:** No
- **Generation Strategy:** Randomized plate string matching garage state
- **Example Synthetic Value:** `Plate: 7XYZ891`, `State: CA`

---

## 3. ClaimCenter Synthetic Entity Specifications

### Entity: Claim
**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Claim.eti`
**Entity Type:** `retireable`

#### ClaimNumber
- **Type:** `claimnumber (varchar 40)`
- **Required:** Yes
- **Generation Strategy:** `CLM-SYN-{3 digits}-{2 digits}-{6 digits}` (Guidewire standard pattern)
- **Example Synthetic Value:** `CLM-SYN-402-19-847291`

#### State
- **Type:** `TypeKey -> ClaimState`
- **Required:** Yes
- **Allowed Values:** `draft`, `open`, `closed`, `archived`
- **Generation Strategy:** `open` (65%), `closed` (30%), `draft` (5%)
- **Example Synthetic Value:** `open`

#### LossType
- **Type:** `TypeKey -> LossType`
- **Required:** Yes
- **Allowed Values:** `AUTO`, `PR`, `WC`, `GL`, `TRAV`
- **Generation Strategy:** Matches parent Policy line pattern
- **Example Synthetic Value:** `AUTO`

#### LossCause
- **Type:** `TypeKey -> LossCause`
- **Required:** Yes
- **Allowed Values:** `vehcollision`, `rearend`, `rollover`, `theftentire`, `fire`, `waterdamage`, `slipfall`, `strain`
- **Generation Strategy:** Filtered by `LossType`
- **Example Synthetic Value:** `vehcollision`

#### LossDate / ReportedDate
- **Type:** `datetime`
- **Required:** Yes
- **Generation Strategy:** `LossDate` strictly between `Policy.EffectiveDate` and `Policy.ExpirationDate`. `ReportedDate` = `LossDate + (0 to 14 days)`
- **Example Synthetic Value:** `LossDate: 2025-06-12T14:30:00Z`, `ReportedDate: 2025-06-13T09:15:00Z`

---

### Entity: Exposure
**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Exposure.eti`
**Entity Type:** `retireable`

#### ExposureType
- **Type:** `TypeKey -> ExposureType`
- **Required:** Yes
- **Allowed Values:** `vehicledamage`, `bodilyinjurydamage`, `generaldamage`, `propertydamage`, `pip`, `medpay`, `wc_injury`
- **Generation Strategy:** Matched to specific incident and coverage type
- **Example Synthetic Value:** `vehicledamage`

#### State
- **Type:** `TypeKey -> ExposureState`
- **Required:** Yes
- **Allowed Values:** `draft`, `open`, `closed`
- **Generation Strategy:** `open` if Claim is open; `closed` if Claim is closed
- **Example Synthetic Value:** `open`

#### LossParty
- **Type:** `TypeKey -> LossPartyType`
- **Required:** Yes
- **Allowed Values:** `insured`, `third_party`
- **Generation Strategy:** `insured` for collision/comprehensive; `third_party` for liability
- **Example Synthetic Value:** `insured`

---

### Entities: Financial Transactions (Reserve, Payment, Check)
**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Reserve.eti`, `Payment.eti`, `Check.eti`
**Entity Type:** `retireable`

#### Reserve.CostType / CostCategory
- **Type:** `TypeKey -> CostType` / `TypeKey -> CostCategory`
- **Required:** Yes
- **Allowed CostType:** `claimcost`, `aoexpense`, `dcc`
- **Allowed CostCategory:** `body`, `property`, `medical`, `legal`, `auto_parts`, `labor`, `rental`
- **Generation Strategy:** `claimcost` + `body` for vehicle physical damage
- **Example Synthetic Value:** `CostType: claimcost`, `CostCategory: body`

#### Reserve.Amount / Payment.Amount
- **Type:** `currencyamount (money)`
- **Required:** Yes
- **Generation Strategy:** Realistic log-normal distribution ($500 to $15,000 for auto body; $2,000 to $50,000 for injury). Cumulative payments must not exceed total reserves.
- **Example Synthetic Value:** `Reserve: $4,500.00`, `Payment: $3,850.00`

#### Check.PaymentMethod
- **Type:** `TypeKey -> PaymentMethod`
- **Required:** Yes
- **Allowed Values:** `check`, `eft`, `manual`
- **Generation Strategy:** `check` (60%), `eft` (38%), `manual` (2%)
- **Example Synthetic Value:** `check`

#### Check.Status
- **Type:** `TypeKey -> TransactionStatus`
- **Required:** Yes
- **Allowed Values:** `submitting`, `submitted`, `pending_approval`, `approved`, `issued`, `cleared`, `denied`, `stopped`, `voided`
- **Generation Strategy:** `issued` or `cleared` for settled payments
- **Example Synthetic Value:** `cleared`
