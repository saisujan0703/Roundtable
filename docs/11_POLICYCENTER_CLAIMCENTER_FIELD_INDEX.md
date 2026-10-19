# PolicyCenter to ClaimCenter Cross-System Field Index

**Guidewire Suite Version:** 10.2.1
**PolicyCenter Source:** `C:\GW10\PolicyCenter`
**ClaimCenter Source:** `C:\GW10\ClaimCenter`
**Extraction Date:** 2026-09-26

---

## 1. Overview & Integration Architecture

In an enterprise Guidewire deployment, **PolicyCenter (PC)** is the System of Record (SOR) for accounts, policies, terms, coverages, and insured assets, while **ClaimCenter (CC)** is the SOR for claims, incidents, exposures, reserves, and disbursements.

When a First Notice of Loss (FNOL) occurs, ClaimCenter retrieves or verifies policy information from PolicyCenter via the Policy Search / Retrieval integration plugin. This document provides the authoritative cross-product field dictionary mapping between PolicyCenter entities and ClaimCenter claim intake structures.

---

## 2. Policy & Term Mapping

| Business Concept | PolicyCenter Entity.Field | PC Source File | ClaimCenter Entity.Field | CC Source File | Notes & Transformation |
|------------------|---------------------------|----------------|--------------------------|----------------|------------------------|
| Policy Number | `PolicyPeriod.PolicyNumber` | `metadata/entity/PolicyPeriod.eti` | `Policy.PolicyNumber` | `metadata/entity/Policy.eti` | Direct string match (e.g. `53-263535`) |
| Policy Product / Type | `Policy.ProductCode` | `metadata/entity/Policy.eti` | `Policy.PolicyType` | `metadata/entity/Policy.eti` | PC uses patterncode (`PersonalAuto`); CC uses typelist `PolicyType` (`PersonalAuto`) |
| Term Effective Date | `PolicyPeriod.PeriodStart` | `metadata/entity/PolicyPeriod.eti` | `Policy.EffectiveDate` | `metadata/entity/Policy.eti` | DateTime value representing start of policy coverage period |
| Term Expiration Date | `PolicyPeriod.PeriodEnd` | `metadata/entity/PolicyPeriod.eti` | `Policy.ExpirationDate` | `metadata/entity/Policy.eti` | DateTime value representing expiration boundary |
| Original Effective Date | `Policy.OriginalEffectiveDate` | `metadata/entity/Policy.eti` | `Policy.OrigEffectiveDate` | `metadata/entity/Policy.eti` | Date policy originally written by carrier |
| Policy Status | `PolicyPeriod.Status` | `metadata/entity/PolicyPeriod.eti` | `Policy.Status` | `metadata/entity/Policy.eti` | PC typelist `PolicyPeriodStatus` (`Bound`) maps to CC typelist `PolicyStatus` (`inforce`) |
| Producer Code | `Policy.ProducerCodeOfService.Code` | `metadata/entity/Policy.eti` | `Policy.ProducerCode` | `metadata/entity/Policy.eti` | Managing producer code string |
| Currency | `PolicyPeriod.PreferredCoverageCurrency` | `metadata/entity/PolicyPeriod.eti` | `Policy.Currency` | `metadata/entity/Policy.eti` | Typelist `Currency` (`usd`) |
| Total Vehicles Count | Count of `PersonalAutoLine.Vehicles` | `metadata/entity/PersonalAutoLine.eti` | `Policy.TotalVehicles` | `metadata/entity/Policy.eti` | Denormalized integer count on CC policy snapshot |
| Total Properties Count | Count of `CPLine.CPLocations` | `metadata/entity/CPLine.eti` | `Policy.TotalProperties` | `metadata/entity/Policy.eti` | Denormalized integer count on CC policy snapshot |

---

## 3. Insured & Contact Details Mapping

| Business Concept | PolicyCenter Entity.Field | PC Source File | ClaimCenter Entity.Field | CC Source File | Notes & Transformation |
|------------------|---------------------------|----------------|--------------------------|----------------|------------------------|
| Primary Insured Contact | `Account.AccountHolderContact` | `metadata/entity/Account.eti` | `Claim.Insured` / `ClaimContactRole[insured]` | `metadata/entity/Claim.eti` | PC AccountHolder maps to CC Insured |
| Person First Name | `Person.FirstName` | `metadata/entity/Person.eti` | `Person.FirstName` | `metadata/entity/Person.eti` | Direct string match (Varchar 30) |
| Person Last Name | `Person.LastName` | `metadata/entity/Person.eti` | `Person.LastName` | `metadata/entity/Person.eti` | Direct string match (Varchar 30) |
| Company Name | `Company.Name` | `metadata/entity/Company.eti` | `Company.Name` | `metadata/entity/Company.eti` | Corporate legal name (Varchar 60) |
| Primary Phone Number | `Contact.PrimaryPhoneValue` | `metadata/entity/Contact.eti` | `Contact.PrimaryPhoneValue` | `metadata/entity/Contact.eti` | Standard phone string format |
| Email Address | `Contact.EmailAddress1` | `metadata/entity/Contact.eti` | `Contact.EmailAddress1` | `metadata/entity/Contact.eti` | Varchar 60 email address |
| Tax ID (SSN / FEIN) | `Contact.TaxID` | `metadata/entity/Contact.eti` | `Contact.TaxID` | `metadata/entity/Contact.eti` | Encrypted/masked tax identifier |
| Street Address | `Address.AddressLine1` | `metadata/entity/Address.eti` | `Address.AddressLine1` | `metadata/entity/Address.eti` | Physical street address |
| City | `Address.City` | `metadata/entity/Address.eti` | `Address.City` | `metadata/entity/Address.eti` | City name |
| State | `Address.State` | `metadata/entity/Address.eti` | `Address.State` | `metadata/entity/Address.eti` | Typelist `State` (`TC_CA`, `TC_TX`, etc.) |
| Postal Code | `Address.PostalCode` | `metadata/entity/Address.eti` | `Address.PostalCode` | `metadata/entity/Address.eti` | ZIP / Postal code |

---

## 4. Vehicle Risk Unit Mapping

| Business Concept | PolicyCenter Entity.Field | PC Source File | ClaimCenter Entity.Field | CC Source File | Notes & Transformation |
|------------------|---------------------------|----------------|--------------------------|----------------|------------------------|
| Vehicle Identification (VIN) | `PersonalVehicle.Vin` | `metadata/entity/PersonalVehicle.eti` | `Vehicle.Vin` / `VehicleIncident.Vehicle.Vin` | `metadata/entity/Vehicle.eti` | 17-character ISO standard VIN |
| Model Year | `PersonalVehicle.Year` | `metadata/entity/PersonalVehicle.eti` | `Vehicle.Year` | `metadata/entity/Vehicle.eti` | 4-digit integer year |
| Vehicle Make | `PersonalVehicle.Make` | `metadata/entity/PersonalVehicle.eti` | `Vehicle.Make` | `metadata/entity/Vehicle.eti` | Vehicle manufacturer |
| Vehicle Model | `PersonalVehicle.Model` | `metadata/entity/PersonalVehicle.eti` | `Vehicle.Model` | `metadata/entity/Vehicle.eti` | Vehicle model name |
| License Plate | `PersonalVehicle.LicensePlate` | `metadata/entity/PersonalVehicle.eti` | `Vehicle.LicensePlate` | `metadata/entity/Vehicle.eti` | Vehicle registration plate |
| Registration State | `PersonalVehicle.State` | `metadata/entity/PersonalVehicle.eti` | `Vehicle.State` | `metadata/entity/Vehicle.eti` | Typelist `Jurisdiction` (`TC_CA`) |
| Risk Unit Number | Order in `PersonalAutoLine.Vehicles` | `metadata/entity/PersonalAutoLine.eti` | `VehicleRU.RUNumber` | `metadata/entity/VehicleRU.eti` | Integer risk unit index on policy |

---

## 5. Property Risk Unit Mapping

| Business Concept | PolicyCenter Entity.Field | PC Source File | ClaimCenter Entity.Field | CC Source File | Notes & Transformation |
|------------------|---------------------------|----------------|--------------------------|----------------|------------------------|
| Location Address | `PolicyLocation.AccountLocation.Address` | `metadata/entity/PolicyLocation.eti` | `PolicyLocation.Address` | `metadata/entity/PolicyLocation.eti` | Property physical location |
| Location Number | `PolicyLocation.LocationNum` | `metadata/entity/PolicyLocation.eti` | `PolicyLocation.LocationNumber` | `metadata/entity/PolicyLocation.eti` | Integer location identifier |
| Building Number | `CPBuilding.BuildingNum` | `metadata/entity/CPBuilding.eti` | `Building.BuildingNumber` | `metadata/entity/Building.eti` | Building number on location |
| Property Description | `CPLocation.Description` | `metadata/entity/CPLocation.eti` | `FixedPropertyIncident.PropertyDesc` | `metadata/entity/FixedPropertyIncident.eti` | Descriptive text of property |

---

## 6. Coverage & Term Mapping

| Business Concept | PolicyCenter Product Model Pattern | PC Source File | ClaimCenter Typelist / Entity | CC Source File | Notes & Transformation |
|------------------|------------------------------------|----------------|-------------------------------|----------------|------------------------|
| Auto Liability Coverage | `PALiabilityCov` | `productmodel/.../PALiabilityCov.xml` | `CoverageType.TC_PALIABILITYCOV` | `metadata/typelist/CoverageType.tti` | Maps to `ExposureType.TC_VEHICLEDAMAGE` or `BODILYINJURYDAMAGE` |
| Collision Coverage | `PACollisionCov` | `productmodel/.../PACollisionCov.xml` | `CoverageType.TC_PACOLLISIONCOV` | `metadata/typelist/CoverageType.tti` | Maps to `ExposureType.TC_VEHICLEDAMAGE` |
| Comprehensive Coverage | `PAComprehensiveCov` | `productmodel/.../PAComprehensiveCov.xml` | `CoverageType.TC_PACOMPREHENSIVECOV` | `metadata/typelist/CoverageType.tti` | Physical damage comprehensive |
| Medical Payments | `PAMedPayCov` | `productmodel/.../PAMedPayCov.xml` | `CoverageType.TC_PAMEDPAYCOV` | `metadata/typelist/CoverageType.tti` | Maps to `ExposureType.TC_MEDPAY` |
| Per-Incident Limit | `PackageCovTermPattern` (e.g. 50/100/50) | `productmodel/.../PALiabilityCov.xml` | `Coverage.IncidentLimit` | `metadata/entity/Coverage.eti` | Maximum payment per occurrence |
| Per-Person Limit | `PackageCovTermPattern` | `productmodel/.../PALiabilityCov.xml` | `Coverage.ExposureLimit` | `metadata/entity/Coverage.eti` | Maximum payment per individual exposure |
| Deductible Amount | `OptionCovTermPattern` (e.g. $500) | `productmodel/.../PACollisionCov.xml` | `Deductible.Amount` | `metadata/entity/Deductible.eti` | Insured out-of-pocket obligation |
