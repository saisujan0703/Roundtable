# PolicyCenter Entity Data Dictionary

**Guidewire PolicyCenter Version:** 10.2.1.1711 (Platform 10.201.1)
**Installation Location:** `C:\GW10\PolicyCenter`
**Extraction Date:** 2026-09-26
**Total Insurance Entities Cataloged:** 485

---

## Overview & Extraction Methodology

This data dictionary provides a complete, source-grounded specification of the PolicyCenter data model. Every entity, attribute, data type, cardinality, foreign key reference, typelist code, and lifecycle property is verified directly against the installed `.eti`, `.etx`, and `.eix` XML metadata files.

### Standard Platform Infrastructure Fields
In Guidewire PolicyCenter, entities automatically inherit core infrastructure fields based on their entity type and implemented delegates:
- **KeyableBean**: `ID` (Primary key, Long/Key, System-generated unique), `PublicID` (Varchar(64), External business identifier).
- **Versionable / Editable**: `BeanVersion` (Optimistic locking integer), `CreateTime` (DateTime), `CreateUser` (FK -> User), `UpdateTime` (DateTime), `UpdateUser` (FK -> User).
- **Retireable**: `Retired` (Long, 0 = Active, non-zero = timestamp of retirement / soft deletion).
- **EffDated (Effective-Dated)**: `BranchValue` (FK -> PolicyPeriod owning branch), `EffectiveDate` (DateTime effective boundary), `ExpirationDate` (DateTime expiration boundary), `ChangeType` (TypeKey -> EffDatedChangeType).

---

## Entity Specifications

### Entity: Account

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Account.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\Account.etx`
**Entity Type:** `retireable`
**Database Table:** `account`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** An account is an entity (person or company) that applies for or purchases one or more policies from the carrier. Account attributes include years in business, industry code (SIC, NAICS, etc) and nature of ops, FEIN identifier, Bureau (WC) number and business entity type (e.g. individual, corp., partenership, etc.)

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| AccountNumber | shorttext | No | - | - | The account number of this account. |
| AccountStatusUpdateTime | datetime | Yes | - | - | Time when account status was last updated |
| BusOpsDesc | varchar | No | - | - | Business and operations description. |
| LinkContacts | bit | Yes | - | - | Default: false Indicates that this Account will sync Contacts with an external Contact Management System. |
| LockedFromMerge | bit | Yes | - | - | Default: false If true then no Policy may be created or retrieved on this Account |
| OriginationDate | datetime | No | - | - | The date the account became a client of the carrier. |
| OtherOrgTypeDescription | varchar | No | - | - | If AccountOrgType is 'other', this value must be filled in |
| StateBureauNum | shorttext | No | - | - | State Bureau number of this account. |
| YearBusinessStarted | year | No | - | - | What year was the business started? |
| Nickname | varchar | No | - | - | A nickname of the account used to distinguish multiple accounts of a single account holder |
| IndustryCode | ForeignKey | No | IndustryCode | - | Industry Code of Account |
| LocationAutoNumberSeq | ForeignKey | No | AutoNumberSequence | - | Sequence to autonumber account locations |
| AccountHolderContact | ForeignKey | Yes | Contact | - | Account Holder Contact denormalized onto Account for performance. |
| PrimaryLocation | ForeignKey | Yes | AccountLocation | - | The primary Location for this Account. |
| AccountOrgType | TypeKey | No | - | AccountOrgType | Organization type of this account Codes (16 total): [individual, solepropship, partnership, corporation, privatecorp, ...] |
| AccountStatus | TypeKey | Yes | - | AccountStatus | Default: Active The status of this account Codes: [Pending, Active, Withdrawn, Merged] |
| PrimaryLanguage | TypeKey | No | - | LanguageType | The account's preferred language Codes: [de, en_US, es, fr, ja] |
| PrimaryLocale | TypeKey | No | - | LocaleType | The account's preferred locale Codes (8 total): [en_US, en_GB, en_CA, en_AU, fr_CA, ...] |
| PreferredCoverageCurrency | TypeKey | Yes | - | Currency | Preferred Coverage Currency Codes (7 total): [usd, eur, gbp, cad, aud, ...] |
| PreferredSettlementCurrency | TypeKey | Yes | - | Currency | Preferred Settlement Currency Codes (7 total): [usd, eur, gbp, cad, aud, ...] |
| ServiceTier | TypeKey | No | - | CustomerServiceTier | Customer Service Tier Codes: [silver, gold, platinum] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| AccountContacts | AccountContact | All the contacts related to this account, including inactive ones. |
| AccountLocations | AccountLocation | The list of account locations for this Account |
| JobGroups | JobGroup | The list of Job Groups of this Account |
| Notes | Note | Notes associated with this account. |
| ProducerCodes | AccountProducerCode | Producer Codes associated with this account. |
| RoleAssignments | AccountUserRoleAssignment | Role Assignments for this account. |
| SourceRelatedAccounts | AccountAccount | Relationships from this account to another one. |
| TargetRelatedAccounts | AccountAccount | Relationships from another account to this one. |

---

### Entity: AccountContact

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\AccountContact.eti`
**Entity Type:** `retireable`
**Database Table:** `accountcontact`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A contact on an account.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Active | bit | Yes | - | - | Default: true Determines whether or not the contact is available to be added to jobs |
| LastUpdateTime | datetime | No | - | - | Date and time of last update |
| TemporaryLastUpdateTime | datetime | No | - | - | Temporary date and time of last update; will eventually be copied to the LastUpdateTime during commit |
| Account | ForeignKey | Yes | Account | - | The account on which this is a contact. |
| Contact | ForeignKey | Yes | Contact | - | The related contact. |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Roles | AccountContactRole | The roles that this contact has played on the account or its policies. |

---

### Entity: AccountContactRole

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\AccountContactRole.eti`
**Entity Type:** `retireable`
**Database Table:** `accountcontactrole`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A role that an contact has played on an account or its policies.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| AccountContact | ForeignKey | Yes | AccountContact | - | The account contact that plays this role. |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Replaces | AccountContactRoleReplacement | The roles that this AccountContactRole has replaced through merges |

---

### Entity: AccountHolder

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\AccountHolder.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** AccountContactRole
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: AccountLocation

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\AccountLocation.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\AccountLocation.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** Address
**Effective-Dated Container Branch Field:** N/A
**Description:** Cross policy locations information in the account level

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Active | bit | Yes | - | - | Default: true Determines whether or not the location is available to be newly added to submissions |
| EmployeeCount | nonnegativeinteger | No | - | - | The number of employees at this location |
| LocationCode | shorttext | No | - | - | The custom location code specified by customer |
| LocationName | shorttext | No | - | - | Shorthand name for this location |
| LocationNum | integer | Yes | - | - | The location number of this location |
| Phone | phone | No | - | - | Phone |
| PhoneExtension | varchar | No | - | - | Phone extension |
| NonSpecific | bit | No | - | - | Default: false Is a non-specific location. |
| Account | ForeignKey | Yes | Account | - | The account on which this is a location |
| PhoneCountry | TypeKey | No | - | PhoneCountryCode | The country associated with this phone number. Codes (245 total): [AC, AD, AE, AF, AG, ...] |

---

### Entity: AccountProducerCode

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\AccountProducerCode.eti`
**Entity Type:** `retireable`
**Database Table:** `accountproducercode`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A producer code for the account.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Account | ForeignKey | Yes | Account | - | The account on which this is a contact. |
| ProducerCode | ForeignKey | Yes | ProducerCode | - | The producer code. |

---

### Entity: Contact

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Contact.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\Contact.etx`
**Entity Type:** `retireable`
**Database Table:** `contact`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Represents a generic contact like a person or a business.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| EmailAddress1 | varchar | No | - | - | Primary email address associated with the contact. |
| EmailAddress2 | varchar | No | - | - | Secondary email address associated with the contact. |
| FaxPhone | phone | No | - | - | Fax number associated with the contact. |
| FaxPhoneExtension | varchar | No | - | - | Fax phone extension. |
| HomePhone | phone | No | - | - | Home phone number associated with the contact. |
| HomePhoneExtension | varchar | No | - | - | Home phone extension. |
| LoadRelatedContacts | bit | Yes | - | - | Default: false This field is deprecated. It was formerly used to determine whether related contacts should be loaded from the Address Book. |
| Name | companyname | No | - | - | This contact's name. |
| Notes | longtext | No | - | - | Notes on this contact. |
| Preferred | bit | Yes | - | - | Default: false Whether the vendor is a preferred vendor. |
| TaxID | ssn | No | - | - | Tax ID for the contact (SSN or EIN). |
| VendorNumber | varchar | No | - | - | Vendor number for the contact. |
| WithholdingRate | percentagedec | No | - | - | The contact's backup withholding rate, or null if backup withholding is not required or is not known to be required. |
| WorkPhone | phone | No | - | - | Business phone number associated with the contact. |
| WorkPhoneExtension | varchar | No | - | - | Business phone extension. |
| Score | integer | No | - | - | Overall review Score for this Contact |
| PrimaryAddress | ForeignKey | No | Address | - | Primary address associated with the contact. |
| FaxPhoneCountry | TypeKey | No | - | PhoneCountryCode | Fax phone country. Codes (245 total): [AC, AD, AE, AF, AG, ...] |
| HomePhoneCountry | TypeKey | No | - | PhoneCountryCode | Home phone country. Codes (245 total): [AC, AD, AE, AF, AG, ...] |
| WorkPhoneCountry | TypeKey | No | - | PhoneCountryCode | Work phone country. Codes (245 total): [AC, AD, AE, AF, AG, ...] |
| PrimaryPhone | TypeKey | No | - | PrimaryPhoneType | Primary phone number type for the contact. Codes: [home, work, mobile] |
| TaxStatus | TypeKey | No | - | TaxStatus | Default: unconfirmed Status of the contact's tax ID; whether it is known or unknown. Codes: [unknown, unconfirmed, confirmed] |
| VendorType | TypeKey | No | - | VendorType | The company's vendor type. Codes (16 total): [indautoinspector, indpropinspector, autorepair, autoglass, towingservice, ...] |
| PrimaryLanguage | TypeKey | No | - | LanguageType | The account's preferred language Codes: [de, en_US, es, fr, ja] |
| PrimaryLocale | TypeKey | No | - | LocaleType | The account's preferred locale Codes (8 total): [en_US, en_GB, en_CA, en_AU, fr_CA, ...] |
| ValidationLevel | TypeKey | No | - | ValidationLevel | Validation level that this object passed (if any) before it was stored. Codes: [loadsave, default, quotable, bindable, readyforissue, quickquotable] |
| PreferredCurrency | TypeKey | No | - | Currency | The contact's preferred currency. Codes (7 total): [usd, eur, gbp, cad, aud, ...] |
| AutoSync | TypeKey | No | - | AutoSync | A status code to indicate whether this entity allows auto-sync or not. Null means disallow. Codes: [Disallow, Allow, Suspended] |
| Fingerprint | OneToOne | No | ContactFingerprint | - | One-to-one link |
| ExternalVersion_Ext | integer | Yes | - | - | [Extension] The version number of this contact in external contact system |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| ContactAddresses | ContactAddress | Secondary addresses associated with the contact. |
| SourceRelatedContacts | ContactContact | Contacts that point to this contact. |
| TargetRelatedContacts | ContactContact | Contacts that this Contact points to. |
| OfficialIDs | OfficialID | TaxIDs associated with this contact |
| CategoryScores | ContactCategoryScore | List of categories and their average scores, associated with this Contact. |
| Tags | ContactTag | List of ContactTags. |
| AccountContacts_Ext | AccountContact | [Extension] All the accountcontacts related to this contact. |

---

### Entity: Person

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Person.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\Person.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** Contact
**Effective-Dated Container Branch Field:** N/A
**Description:** Represents a person as a primary subtype of Contact.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| CellPhone | phone | No | - | - | Mobile phone number associated with the contact. |
| CellPhoneExtension | varchar | No | - | - | Mobile phone extension. |
| DateOfBirth | datetime | No | - | - | Date of birth. |
| FirstName | firstname | No | - | - | First name. |
| FormerName | lastname | No | - | - | Person's former name, if any. |
| LastName | lastname | No | - | - | Last name. |
| LicenseNumber | driverlicense | No | - | - | Driver's license number. |
| MiddleName | firstname | No | - | - | Middle name or initial. |
| NumDependents | integer | No | - | - | Number of dependents the employee has. |
| NumDependentsU18 | integer | No | - | - | Number of dependents under 18. |
| NumDependentsU25 | integer | No | - | - | Number of dependents over 18 and under 25. |
| Occupation | varchar | No | - | - | Occupation. |
| CellPhoneCountry | TypeKey | No | - | PhoneCountryCode | Mobile phone country. Codes (245 total): [AC, AD, AE, AF, AG, ...] |
| Gender | TypeKey | No | - | GenderType | Gender. Codes: [M, F] |
| LicenseState | TypeKey | No | - | Jurisdiction | Driver's license jurisdiction. Codes (98 total): [AK, AL, AR, AZ, CA, ...] |
| MaritalStatus | TypeKey | No | - | MaritalStatus | Marital status. Codes (7 total): [C, D, M, P, S, ...] |
| Prefix | TypeKey | No | - | NamePrefix | Prefix for the person's name. Codes: [mr, mrs, ms, dr] |
| Suffix | TypeKey | No | - | NameSuffix | Suffix for the person's name. Codes (9 total): [jr, sr, c_Ir, c_II, c_III, ...] |
| TaxFilingStatus | TypeKey | No | - | TaxFilingStatusType | State-specific field. Codes: [MarriedJoint, MarriedSep, Single, SingleHH, Widow] |

---

### Entity: Company

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Company.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** Contact
**Effective-Dated Container Branch Field:** N/A
**Description:** Represents an company/business as a primary subtype of Contact.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: Address

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Address.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\Address.etx`
**Entity Type:** `retireable`
**Database Table:** `address`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Address of a person or business.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Description | shorttext | No | - | - | Additional description of mailing address. |
| ValidUntil | datetime | No | - | - | Latest date that this address is valid. |
| SpatialPoint | spatialpoint | No | - | - | Latitude and longitude of this address, represented as an instance of SpatialPoint. |
| BatchGeocode | bit | Yes | - | - | Default: false Boolean field to mark an address to be geocoded (if needed) by the batch geocoding work queue. |
| AddressType | TypeKey | No | - | AddressType | Type of this address record. Codes: [home, business, other, billing] |
| GeocodeStatus | TypeKey | No | - | GeocodeStatus | Default: None Enum giving the status of the latitude and longitude data. Codes: [none, failure, city, postalcode, street, exact] |

---

### Entity: ContactAddress

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\ContactAddress.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\ContactAddress.etx`
**Entity Type:** `joinarray`
**Database Table:** `contactaddress`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Table linking contacts to addresses.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Address | ForeignKey | Yes | Address | - | Associated address. |
| Contact | ForeignKey | Yes | Contact | - | Associated contact. |

---

### Entity: Policy

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Policy.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\Policy.etx`
**Entity Type:** `effdatedcontainer`
**Database Table:** `policy`
**Supertype:** None
**Effective-Dated Container Branch Field:** Periods
**Description:** Policy attributes including account, group and user assignment, product and policy type

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| IssueDate | dateonly | No | - | - | The date on which this policy was issued by the issuing job. |
| NumPriorLosses | nonnegativeinteger | No | - | - | The number of losses. Only applicable for a loss history type of 'attached'. |
| ProductCode | patterncode | Yes | - | - | The Product defining what kind of Policy this is |
| DoNotArchive | bit | Yes | - | - | Default: false Do not archive any of the terms for this Policy. Terms that are already archived will not be automatically retrieved. |
| OriginalEffectiveDate | dateonly | No | - | - | The date on which this policy was originally issued or bound. |
| MovedPolicySourceAccountPublicID | publicid | No | - | - | - |
| Account | ForeignKey | Yes | Account | - | The Account to which this policy belongs.  Note that getting the value of this foreign key may result in the Account being re-retrieved if it is a non-SOR account. |
| MovedPolicySourceAccount | ForeignKey | No | Account | - | The Account to which this policy comes from.  This field is populated if the policy is moved from other account. |
| ProducerCodeOfService | ForeignKey | Yes | ProducerCode | - | The producer code that manages this policy and can modify it.  If external user use producer code security, the user must have this producer code. |
| APDProduct | ForeignKey | No | APDProduct | - | Advanced product development product |
| LossHistoryType | TypeKey | Yes | - | LossHistoryType | Default: nol How the loss history is described for this policy Codes: [nol, man, att] |
| PackageRisk | TypeKey | No | - | PackageRisk | Package Risk Type Codes (8 total): [office, mercantile, motelhotel, apartment, institutional, ...] |
| PrimaryLanguage | TypeKey | No | - | LanguageType | The policy's preferred language Codes: [de, en_US, es, fr, ja] |
| PrimaryLocale | TypeKey | No | - | LocaleType | The policy's preferred locale Codes (8 total): [en_US, en_GB, en_CA, en_AU, fr_CA, ...] |
| PriorTotalIncurred | monetaryamount | No | - | - | The total incurred. Only applicable for a loss history type of 'attached'. |
| PriorPremiums | monetaryamount | No | - | - | Premiums for policy terms prior to PC conversion. This value can be set during conversion on renewal. |
| DividedToNewAccountSourceJoin | OneToOne | No | PolicyPolicyDivide | - | Points to the join table of divided policies. |
| RewrittenToNewAccountSourceJoin | OneToOne | No | PolicyPolicyRewrite | - | Points to the source policy part of the join table if the policy has been rewritten |
| RewrittenToNewAccountDestinationJoin | OneToOne | No | PolicyPolicyRewrite | - | Points to the destination policy part of the join table if the policy has a source policy which has been rewritten |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| AuditInformations | AuditInformation | The audits for this policy |
| Jobs | Job | Jobs of this policy. |
| PriorLosses | LossHistoryEntry | Loss history detail entries. Only applicable for a loss history type of 'manually entered'. |
| Notes | Note | Notes associated with this Policy |
| Periods | PolicyPeriod | Periods of this policy. |
| PriorPolicies | PriorPolicy | Prior policy information for this policyholder. |
| RoleAssignments | PolicyUserRoleAssignment | Role Assignments for this bean. |
| IssueHistories | UWIssueHistory | History of changes to all UW issues associated with this policy |
| UWReferralReasons | UWReferralReason | Referral reasons of the policy |
| RIRiskVLContainers | RIRiskVLContainer | All RI Risk VL Containers for any period on this policy |
| Contingencies | Contingency | Child collection |

---

### Entity: PolicyPeriod

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyPeriod.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\PolicyPeriod.etx`
**Entity Type:** `effdatedbranch`
**Database Table:** `policyperiod`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Policy Period allows a point in time reconstruction of all key policy attributes.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| AssignedRisk | bit | No | - | - | Default: false Flag for policy/risk assigned by state requirement |
| BranchName | shorttext | No | - | - | The reference name of this branch of the job |
| BranchNumber | integer | No | - | - | The number of this branch of the job |
| FailedOOSEValidation | bit | No | - | - | Default: false True if this is a draft PolicyPeriod in an OOS job that has failed validation |
| FailedOOSEEvaluation | bit | No | - | - | Default: false True if this is a PolicyPeriod in an OOS job that has blocking UWIssues at a later slice than the current primary slice |
| TermNumber | integer | No | - | - | A sequence number that starts at 1 and is incremented on a renewal and rewrite, usually to distinguish between different periods of a same policy. |
| PolicyNumber | policynumber | No | - | - | The policy number for this policy period. This value may be different from the core policy number on the associated Policy. |
| PrimaryInsuredName | shorttext | No | - | - | The display name of the primary names insured (denormalization). |
| WrittenDate | dateonly | No | - | - | Nominally, the date this period was created. For reinstatements, it is the written date of the reinstated period. For rewrites, it can be the date of the rewrite or the date of the original period. |
| SingleCheckingPatternCode | patterncode | No | - | - | The code of the pattern to use for creating and scheduling single checking audits |
| SeriesCheckingPatternCode | patterncode | No | - | - | The code of the pattern to use for creating and scheduling a series of checking audits |
| OverrideBillingAllocation | bit | No | - | - | Default: false Whether to override the billing allocation for installments plan |
| BillImmediatelyPercentage | percentagedec | No | - | - | Default: 0 The percentage to bill immediately if overriding billing allocation for installments plan |
| DepositOverridePct | decimal | No | - | - | Override of the default reporting deposit % of the reporting pattern chosen |
| WaiveDepositChange | bit | No | - | - | Default: false Whether to waive the deposit amount change from current policy period and the based on |
| AltBillingAccountNumber | shorttext | No | - | - | The number of the billing account which may only exist in billing system. |
| InvoiceStreamCode | shorttext | No | - | - | The public id of the invoice stream in billing system. |
| QuoteHidden | bit | Yes | - | - | Default: false Whether the quote is hidden from users without permission to view quote |
| EditLocked | bit | Yes | - | - | Default: false Whether the PolicyPeriod is locked from edit by users without permission to edit |
| ValidReinsurance | bit | No | - | - | Default: 1 True if reinsurables were generated sucessfully. |
| RateAsOfDate | datetime | No | - | - | The date the policy should be rated |
| QuoteCloneOriginalPeriod | shorttext | No | - | - | Soft FK to the original policy period that this policy period was cloned from. |
| QuoteCloneSequenceNumber | longint | No | - | - | This is only used during policy quote clone.  It is a sequence number for the cloned quote. |
| QuoteIdentifier | varchar | No | - | - | If this PolicyPeriod originated from a HVQ quote, this field references that quote's ID. |
| Orphaned | bit | Yes | - | - | Default: false Whether this is an orphaned policy period that should be purged by batch process |
| PNIContactDenorm | ForeignKey | No | Contact | - | The primary named insured's contact on the policy. Denorm field so contact is retained when the policyperiod is archived. |
| Job | ForeignKey | No | Job | - | The job this policy period is part of. |
| LocationAutoNumberSeq | ForeignKey | No | AutoNumberSequence | - | Sequence to autonumber policy locations |
| Policy | ForeignKey | Yes | Policy | - | The policy to which this period belongs |
| PolicyTerm | ForeignKey | Yes | PolicyTerm | - | Policy term information associated with this period |
| ProducerCodeOfRecord | ForeignKey | Yes | ProducerCode | - | The producer code that created this policy in this period and should get the commissions. |
| UWCompany | ForeignKey | No | UWCompany | - | Underwriting company that insures this policy.  This can only change on a Cancellation or Rewrite, never mid-term. |
| ActiveWorkflow | ForeignKey | No | PolicyPeriodWorkflow | - | The workflow that is active from the perspective of the UI. This workflow will be polled when the UI is waiting for results. |
| AllocationOfRemainder | TypeKey | No | - | BillingRemainderAllocate | The method to allocate the remainder of cost if overriding billing allocation for installments plan Codes: [SpreadAcrossInstlmnts, OneHundrdPctNxtInstmnt] |
| BaseState | TypeKey | No | - | Jurisdiction | State the policy period is based in. Codes (98 total): [AK, AL, AR, AZ, CA, ...] |
| Segment | TypeKey | No | - | Segment | Market segment this policy period is in. Codes: [low, med, high] |
| Status | TypeKey | Yes | - | PolicyPeriodStatus | The period's status. This field can only be updated via workflow methods available on the various Job entities. Codes (25 total): [New, Draft, Quoted, Quoting, Bound, ...] |
| RefundCalcMethod | TypeKey | No | - | CalculationMethod | The method used to calculate the amount of refund due.  Once a policy is canceled, subsequent policy periods inherit this until it is reinstated, at which point this field is reset to null.  Also returns null if the cancellation cannot be found (e.g. if the cancellation was done in an external system). Codes: [flat, prorata, shortrate] |
| BillingMethod | TypeKey | No | - | BillingMethod | Billing Method (Agency Bill, Direct Bill, etc) Codes: [DirectBill, AgencyBill, ListBill] |
| PreferredCoverageCurrency | TypeKey | Yes | - | Currency | Preferred Coverage Currency Codes (7 total): [usd, eur, gbp, cad, aud, ...] |
| PreferredSettlementCurrency | TypeKey | Yes | - | Currency | Preferred Settlement Currency Codes (7 total): [usd, eur, gbp, cad, aud, ...] |
| TemporaryCloneStatus | TypeKey | No | - | PolicyPeriodCloneStatus | Codes: [Unprocessed, Purgeable] |
| SelectedTermType | TypeKey | No | - | TermType | Codes: [Annual, HalfYear, Other] |
| SpecialHandling | TypeKey | No | - | SpecialHandling | special handling to be applied to the charges on a billing instruction Codes: [billimmediately, billonnext, holdforaudit, holdforauditall] |
| QuoteMaturityLevel | TypeKey | Yes | - | QuoteMaturityLevel | Default: unrated  Codes: [unrated, rated, quoted] |
| InvoicingMethod | TypeKey | Yes | - | InvoicingMethod | Default: DefaultBilling The invoicing method for this PolicyPeriod Codes: [DefaultBilling, CustomBilling, OverriddenInvoiceStream] |
| DepositAmount | monetaryamount | No | - | - | Deposit amount calculated from the deposit % and total cost subject to reporting |
| TotalPremiumRPT | monetaryamount | No | - | - | Total amount of all premium (but not taxes or any other costs) for the entire policy period. The total is denormalized for higher performance UI display and reporting support. |
| TotalCostRPT | monetaryamount | No | - | - | Total amount of all premium, taxes, and any other costs for the entire policy period. The total is denormalized for higher performance UI display and reporting support. |
| TransactionPremiumRPT | monetaryamount | No | - | - | Total change in premium (but not taxes or any other costs) caused by a job. For a job that creates a new policy period (i.e. Submission, Renewal, or Rewrite), the TransactionPremiumRPT will be the same as the TotalPremiumRPT because there were no prior premiums for the period. For mid-term jobs (Policy Change, Cancellation, etc.), this field represents the change in amount from the prior job. The total is denormalized for UI display and reporting support. |
| TransactionCostRPT | monetaryamount | No | - | - | Total change in premium, taxes, and any other costs caused by a job. For a job that creates a new policy period (i.e. Submission, Renewal, or Rewrite), the TransactionCostRPT will be the same as the TotalCostRPT because there were no prior costs for the period. For mid-term jobs (Policy Change, Cancellation, etc.), this field represents the change in amount from the prior job. The total is denormalized for UI display and reporting support. |
| TaxSurchargesRPT | monetaryamount | No | - | - | Total amount of tax and surcharges on the policy period. The total is denormalized for higher performance UI display and reporting support. |
| EstimatedPremium | monetaryamount | No | - | - | User estimate of total premium amount |
| NewInvoiceStream | OneToOne | No | BillingInvoiceStream | - | The new invoice stream created by this policy period. |
| EffectiveDatedFields | OneToOne | No | EffectiveDatedFields | - | Stores fields that change in effective time but do not fit in any policy line. |
| WorksheetContainer | OneToOne | No | WorksheetContainer | - | ArchiveRoot for Worksheet data, if present |
| SelectedPaymentPlan | OneToOne | No | PaymentPlanSummary | - | The selected payment plan for this period |
| InvoiceStreamOverrides | OneToOne | No | InvoiceStreamOverrides | - | Fields which override the default fields of an InvoiceStream. |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| PeriodAnswers | PeriodAnswer | Set of answers for this policy period. |
| Forms | Form | Forms associated with this policy. |
| Lines | PolicyLine | Lines (e.g. Auto, Property,etc.) of this policy. |
| PolicyContactRoles | PolicyContactRole | The policy contact roles of this policy period. |
| UWIssuesIncludingSoftDeleted | UWIssue | Issues generated during policy evaluation. |
| PolicyLocations | PolicyLocation | The period locations. |
| Workflows | PolicyPeriodWorkflow | Set of workflows associated with this period. |
| Notes | Note | Notes associated with this PolicyPeriod. |
| LocationRisks | LocationRisk | All reinsurable risks associated with policy locations on this policy period. |
| PolicyRisks | PolicyRisk | The reinsurable risk associated with this policy period. |
| RIRiskVersionLists | RIRiskVersionList | Child collection |
| PolicyFXRates | PolicyFXRate | fx rates used for monetary amount conversions |
| Contingencies | Contingency | Child collection |
| AsyncQuoteIssues | AsyncQuoteIssue | Child collection |
| BATransactions_Ext | BATransaction | [Extension] Extension child collection |
| BOPTransactions_Ext | BOPTransaction | [Extension] Extension child collection |
| CPTransactions_Ext | CPTransaction | [Extension] Extension child collection |
| GLTransactions_Ext | GLTransaction | [Extension] Extension child collection |
| IMTransactions_Ext | IMTransaction | [Extension] Extension child collection |
| PATransactions_Ext | PATransaction | [Extension] Extension child collection |
| WCTransactions_Ext | WCTransaction | [Extension] Extension child collection |
| HOPTransactions_Ext | HOPTransaction | [Extension] Extension child collection |

---

### Entity: PolicyTerm

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyTerm.eti`
**Entity Type:** `retireable`
**Database Table:** `policyterm`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Contains data that varies by contractual period but not in effective time or real time.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| NonRenewAddExplanation | shorttext | No | - | - | Additional explanation why this policy marked for non renewal |
| NextRenewalCheckDate | dateonly | No | - | - | The date to next evaluate this PolicyTerm for renewal, null indicates to check at the next opportunity |
| NextArchiveCheckDate | dateonly | No | - | - | The date to next evaluate this PolicyTerm for archiving or null if archiving should be checked at the next opportunity |
| LastRestoreDate | dateonly | No | - | - | The date when one or more PolicyPeriod from this PolicyTerm was last retrieved from the archive |
| DaysReported | nonnegativeinteger | Yes | - | - | Default: 0 The number of days for which the total reported premium applies |
| DepositReleased | bit | Yes | - | - | Default: false True if the deposit amount has been released |
| Bound | bit | Yes | - | - | Default: false True on promoting Submission, Rewrite and for Renewal if current mode is not 'Confirm Renewals'. |
| MostRecentTerm | bit | Yes | - | - | Default: false Flags the future-most term for a policy. |
| GenerateReinsurables | bit | Yes | - | - | Default: false Flag for generating reinsurables for reinsurance |
| LossRatioCalculationDate | dateonly | No | - | - | Date of the most recent Loss Ratio calculation |
| Policy | ForeignKey | Yes | Policy | - | The policy that this term applies to |
| AffinityGroup | ForeignKey | No | AffinityGroup | - | The affinity group assigned to this term |
| PolicyTermArchiveState | TypeKey | Yes | - | PolicyTermArchiveState | Default: NotArchived Combined archive state of the policy periods in the policy term. Codes: [NotArchived, PartiallyArchived, FullyArchived] |
| NonRenewReason | TypeKey | No | - | NonRenewalCode | Classifies the reason that the policy is marked as non-renew Codes (8 total): [loss, producertermination, outofbusness, payhistory, change, ...] |
| PreRenewalDirection | TypeKey | No | - | PreRenewalDirection | Indicates the pre-renewal direction,if any, of this policy Codes: [underwriter, assistant, custrep, nonrenewrefer, nonrenew, nottaken] |
| FinalAuditOption | TypeKey | Yes | - | FinalAuditOption | Default: Rules When false, final audit not scheduled; when true, the underwriter forces the audit to be scheduled and started; otherwise, final audit is scheduled, and rules determine whether to start it. Codes: [Rules, Yes, No] |
| TotalEstimatedPremium | monetaryamount | Yes | - | - | The amount of premium estimated for this policy period |
| TotalReportedPremium | monetaryamount | Yes | - | - | The amount of premium reported for this policy period |
| DepositAmount | monetaryamount | No | - | - | The current deposit amount of the policy |
| LossRatioEarnedPremium | monetaryamount | No | - | - | Earned Premium used for Loss Ratio calculation |
| ClaimSystemTotalIncurred | monetaryamount | No | - | - | Total Incurred Amount retrieved from Claim system for Loss Ratio calculation |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Jobs | Job | Jobs that are part of this PolicyTerm |
| NonRenewalExplanations | NonRenewalExplanation | Non-renewal explanations |
| AuditInformations | AuditInformation | The audits for this policy |
| HumanTouchedIssues | UWIssueUniqueID | The issues on which have had manual actions have been performed |
| RestoreRequests | PolicyTermRestoreRequest | Requests that have been made to retrieve this term from the Archive |
| WorksheetContainers | WorksheetContainer | WorksheetContainer objects on each period in the PolicyTerm |

---

### Entity: PolicyLocation

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyLocation.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\PolicyLocation.etx`
**Entity Type:** `effdated`
**Database Table:** `policylocation`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Policy location specific information.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| LocationNum | integer | Yes | - | - | The location number of this location |
| AddressLine1Internal | addressline | No | - | - | Address Line 1 |
| AddressLine2Internal | addressline | No | - | - | Address Line 2 |
| AddressLine3Internal | addressline | No | - | - | Address Line 3 |
| CityInternal | varchar | No | - | - | City. |
| CountyInternal | varchar | No | - | - | County. |
| PostalCodeInternal | postalcode | No | - | - | Postal code; string to handle Zip+4 and international codes. |
| DescriptionInternal | shorttext | No | - | - | Address Description |
| ValidUntilInternal | datetime | No | - | - | Date Valid Until |
| EmployeeCountInternal | nonnegativeinteger | No | - | - | Employee Count |
| TaxLocation | ForeignKey | No | TaxLocation | - | The TaxLocation for this location. |
| IndustryCode | ForeignKey | No | IndustryCode | - | Industry Code of Location |
| AccountLocation | ForeignKey | Yes | AccountLocation | - | The account location this policy location may be synced with.  While the policy location contains policy contract information, the account location contains shared role information. |
| BuildingAutoNumberSeq | ForeignKey | No | AutoNumberSequence | - | Sequence to autonumber buildings |
| StateInternal | TypeKey | No | - | State | State. Codes (142 total): [AK, AL, AR, AZ, CA, ...] |
| CountryInternal | TypeKey | No | - | Country | Country. Codes (243 total): [unknown, AF, AL, DZ, AS, ...] |
| AddressTypeInternal | TypeKey | No | - | AddressType | Type of this address record. Codes: [home, business, other, billing] |
| FireProtectClass | TypeKey | No | - | FireProtectClass | Fire protection class. Codes: [1, 2, 3, 4, 5] |
| OutboundLocationRiskAssessmentTempStore | OneToOne | No | OutboundLocationRiskAssessmentTempStore | - | One-to-one link |
| AddressLine1KanjiInternal_Ext | addressline | No | - | - | [Extension] Address Line 1 Kanji.  Used only for Japanese addresses and will be null otherwise. |
| AddressLine2KanjiInternal_Ext | addressline | No | - | - | [Extension] Address Line 2 Kanji.  Used only for Japanese addresses and will be null otherwise. |
| CityKanjiInternal_Ext | varchar | No | - | - | [Extension] City Kanji.  Used only for Japanese addresses and will be null otherwise. |
| CEDEXInternal_Ext | bit | No | - | - | [Extension] CEDEX: Special business mail delivery flag (France) |
| CEDEXBureauInternal_Ext | varchar | No | - | - | [Extension] CEDEX: Special business mail delivery bureau (France) |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| TerritoryCodes | TerritoryCode | The rating territory codes. |
| LocationNamedInsureds | LocationNamedInsured | The additional named insured covered at this location |
| Buildings | Building | Set of buildings at a location |
| LocationAnswers | LocationAnswer | Set of answers for this location. |
| LocationRisks | LocationRisk | A reinsurable risk associated with a Location |
| LocationRiskAssessments | LocationRiskAssessment | Risk assessment result for this policy location |

---

### Entity: AuditInformation

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\AuditInformation.eti`
**Entity Type:** `retireable`
**Database Table:** `auditinformation`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Contains information about an audit

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Series | bit | Yes | - | - | Default: false To indicate whether this is a series audit; primarily to distinguish between single checking and series checking. |
| AuditPeriodStartDate | datetime | Yes | - | - | Start date of the audit period. |
| AuditPeriodEndDate | datetime | Yes | - | - | End date of the audit period. |
| InitDate | datetime | Yes | - | - | Initialization date of the audit task. |
| DueDate | datetime | Yes | - | - | Due date of the audit. |
| Instructions | longtext | No | - | - | Special instructions for the auditor |
| ReceivedDate | datetime | No | - | - | The date the audit related information was received |
| Waive | bit | No | - | - | Default: false Was the audit waived? |
| ReversalDate | datetime | No | - | - | The date this audit was reversed |
| Escalated | bit | Yes | - | - | Default: false Whether or not this audit has been escalated by the overdue premium report process. |
| NumDaysAfterFirstEscalation | integer | No | - | - | Number of days after the first escalation prompt |
| NumDaysAfterSecondEscalation | integer | No | - | - | Number of days after the second escalation prompt |
| Policy | ForeignKey | Yes | Policy | - | The policy containing this audit task. |
| PolicyTerm | ForeignKey | Yes | PolicyTerm | - | Associated policy term |
| AuditScheduleType | TypeKey | Yes | - | AuditScheduleType | The type of schedule that is used to schedule audits Codes: [CheckingAudit, PremiumReport, FinalAudit, RetrospectiveRating] |
| RevisionType | TypeKey | No | - | RevisionType | The type of revision (revision or reversal) that is applied to this audit Codes: [Revision, Reversal] |
| AuditMethod | TypeKey | Yes | - | AuditMethod | The audit method to be used. Codes: [Estimated, Physical, Voluntary, Phone] |
| ActualAuditMethod | TypeKey | No | - | AuditMethod | Actual audit method used for this audit Codes: [Estimated, Physical, Voluntary, Phone] |
| FirstEscalationPrompt | TypeKey | No | - | AuditEscalationPromptType | The type of first escalation prompt on audit schedule pattern Codes: [DueDate, AuditPeriodEndDate, FirstEscalationDate] |
| SecondEscalationPrompt | TypeKey | No | - | AuditEscalationPromptType | The type of second escalation prompt on audit schedule pattern Codes: [DueDate, AuditPeriodEndDate, FirstEscalationDate] |
| AuditFee | monetaryamount | No | - | - | Fee for this audit |
| Audit | OneToOne | No | Audit | - | The audit job for this audit. |

---

### Entity: LossHistoryEntry

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\LossHistoryEntry.eti`
**Entity Type:** `editable`
**Database Table:** `losshistentry`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Prior loss financial and policy line detail, status and description

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| OccurrenceDate | datetime | No | - | - | The date of the loss event |
| Description | shorttext | No | - | - | Description of the loss |
| PolicyLinePatternCode | patterncode | No | - | - | The applicable policy line for the loss |
| Policy | ForeignKey | No | Policy | - | The policy with which this is associated |
| LossCause | TypeKey | No | - | LossEntryCause | Cause of loss Codes (13 total): [Fire, Lightning, Explosion, WindstormHail, Smoke, ...] |
| LossStatus | TypeKey | No | - | LossEntryStatus | The status of the claim Codes: [Open, Closed] |
| AmountPaid | monetaryamount | No | - | - | The amount paid by the carrier |
| AmountResv | monetaryamount | No | - | - | The amount reserved by the carrier |
| TotalIncurred | monetaryamount | No | - | - | The total incurred amount |

---

### Entity: PriorPolicy

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PriorPolicy.eti`
**Entity Type:** `editable`
**Database Table:** `priorpolicy`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Details prior coverage information including policy term, carrier, premiums and losses

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| PolicyLinePatternCode | patterncode | No | - | - | The applicable policy line for this coverage. |
| Carrier | shorttext | No | - | - | Name of the carrier |
| PolicyNumber | shorttext | No | - | - | Policy number |
| NumLosses | integer | No | - | - | Number of losses in the last 3 years |
| ExpMod | rate | No | - | - | The experience modifier for this prior policy |
| Policy | ForeignKey | No | Policy | - | The policy to which this applies |
| AnnualPremium | monetaryamount | No | - | - | Last year's annual premium |
| TotalPremium | monetaryamount | No | - | - | The total premium for prior coverage |
| TotalLosses | monetaryamount | No | - | - | Total losses in the last 3 years |

---

### Entity: Form

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Form.eti`
**Entity Type:** `effdated`
**Database Table:** `form`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A form (endorsement, coverage form, etc.) instance on a policy

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| EndorsementNumber | integer | No | - | - | The endorsement number of this form.  This field will be null for non-contract forms. |
| FormDescription | shorttext | No | - | - | A short description of what the form should hold. |
| FormNumber | shorttext | No | - | - | The form number to show in the list of forms. |
| FormPatternCode | patterncode | No | - | - | The public-id of the FormPattern associated with this form. |
| InternalFormEffDate | datetime | No | - | - | The date on which the form became effective.  This column will be null if the form was effective as of the period start date. |
| InternalFormExpDate | datetime | No | - | - | The date on which the form ceases to be effective. This may be superseded by the InternalFormRemovalDate column.  This column will be null if the form expires on the period end date. |
| InternalFormRemovalDate | datetime | No | - | - | The date on which the form was removed or superseded.  If the RemovedOrSuperseded field is set to true, a null here means that the form was removed or superseded as of the period start date. |
| RemovedOrSuperseded | bit | No | - | - | Whether or not the form has been removed or superseded. |
| FormTextData | ForeignKey | No | FormTextData | - | The text for this form, which is stored independently so it's only loaded when necessary and not every time forms are queried, requested, or displayed. |
| InferenceTime | TypeKey | No | - | FormInferenceTime | When the form was inferred.  We track this so that the bind process will only re-infer bind-time forms but will leave quote-time forms alone. Codes: [quote, bind] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| FormAssociations | FormAssociation | The list of associations between this form and entities within the policy graph.  In general, these associations should only be used to in the case where multiple copies of a given form are issued and a way is needed to match up a given Form instance to the entity it's associated with. |
| SupersededForms | FormEdgeTable | An array of size 0 or 1 that links this form to the form it superseded, if any. |

---

### Entity: Contingency

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Contingency.eti`
**Entity Type:** `retireable`
**Database Table:** `contingency`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** contingency for policy

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Title | shorttext | Yes | - | - | title for contingency |
| Description | text | Yes | - | - | description for contingency |
| DueDate | datetime | Yes | - | - | Due Date |
| CloseDate | datetime | No | - | - | The date when the Contingency was closed |
| ActionStartDate | datetime | Yes | - | - | date when action will be initiated if contingency is still unresolved |
| ActionStarted | bit | Yes | - | - | Default: false true if action has started |
| Policy | ForeignKey | Yes | Policy | - | Foreign key target: Policy |
| PolicyPeriod | ForeignKey | No | PolicyPeriod | - | Foreign key target: PolicyPeriod |
| CloseUser | ForeignKey | No | User | - | The user who closed the Contingency |
| Status | TypeKey | Yes | - | ContingencyStatus | Contingency status Codes: [Pending, Resolved, Waived, Failed, Action_Initiated] |
| Action | TypeKey | Yes | - | ContingencyAction | The action that will be taken if this contingency is not resolved successfully Codes: [ChangeRetroactively, ChangeRemainderOfTerm, CancelRetroactively, CancelRemainderOfTerm, CancelRewrite] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Activities | Activity | Activities associated with this Contingency |
| Notes | Note | Use Contingency.queryNotes instead. Usage of this property gives access to all Notes without respect user permissions |
| Documents | Document | Use Contingency.queryDocuments(includeHidden) instead. Usage of this property gives access to all Documents without respect user permissions |
| ContingencyJobs | ContingencyJob | Child collection |

---

### Entity: PolicyLine

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyLine.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\PolicyLine.etx`
**Entity Type:** `effdated`
**Database Table:** `policyline`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A line of insurance (e.g. auto, property, etc.) and selected policy line level attributes (i.e. attributes necessary, but not sufficient to rate)

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| NumAddInsured | integer | No | - | - | Default: 0 The number of additional insureds. For Quick Quotes users enter just the number additional insureds instead of all the details |
| PatternCode | patterncode | Yes | - | - | The pattern defining what kind of PolicyLine this is |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| CoverageSymbolGroups | CoverageSymbolGroup | Groups of coverage symbols on this policy line |
| AdditionalInsureds | PolicyAddlInsured | Child collection |
| LineAnswers | PolicyLineAnswer | Set of answers for this policyline. |
| DiagnosticRatingWorksheets | DiagnosticRatingWorksheet | A list of DiagnosticRatingWorksheet entities related to this PolicyLine |

---

### Entity: PersonalAutoLine

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PersonalAutoLine.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\PersonalAutoLine.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PolicyLine
**Effective-Dated Container Branch Field:** N/A
**Description:** Personal Auto line of business.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| PersonalVehicleAutoNumberSeq | ForeignKey | No | AutoNumberSequence | - | Sequence to autonumber vehicles |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| PACosts | PACost | Child collection |
| PALineCoverages | PersonalAutoCov | Line-level coverages for Personal Auto. |
| PALineExclusions | PersonalAutoExcl | Line-level exclusions for Personal Auto. |
| PALineConditions | PersonalAutoCond | Line-level conditions for Personal Auto. |
| PAModifiers | PAModifier | Rating info for the line. |
| Vehicles | PersonalVehicle | Vehicles on this policy line. |
| PolicyDrivers | PolicyDriver | Drivers on this policy line. |
| PolicyDriverMVRs | PolicyDriverMVR | MVRs for all the drivers on this policy line. |

---

### Entity: CommercialPropertyLine

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\CommercialPropertyLine.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\CommercialPropertyLine.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PolicyLine
**Effective-Dated Container Branch Field:** N/A
**Description:** Commercial Property Policy line of business.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| CPBlanketAutoNumberSeq | ForeignKey | No | AutoNumberSequence | - | Sequence to autonumber cp blanket |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| CPBlankets | CPBlanket | CP Blankets on this policy line. |
| CPLocations | CPLocation | Locations on this policy line. |
| CPCosts | CPCost | Child collection |
| CPModifiers | CPModifier | Rating inputs for the line. |
| CPLineCoverages | CommercialPropertyCov | Line-level coverages for Commercial Property. |
| CPLineExclusions | CommercialPropertyExcl | Line-level exclusions for Commercial Property. |
| CPLineConditions | CommercialPropertyCond | Line-level conditions for Commercial Property. |

---

### Entity: BusinessAutoLine

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BusinessAutoLine.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\BusinessAutoLine.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PolicyLine
**Effective-Dated Container Branch Field:** N/A
**Description:** Commercial Auto line of business.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| AutoSymbolsManualEditDate | datetime | No | - | - | Date when the selection of auto symbols was last manually edited |
| CustomAutoSymbolDesc | shorttext | No | - | - | Description of custom covered auto symbol. |
| BusinessVehicleAutoNumberSeq | ForeignKey | No | AutoNumberSequence | - | Sequence to autonumber vehicles |
| Fleet | TypeKey | No | - | FleetType | Vehicle fleet designation. Codes: [Fleet, NonFleet] |
| PolicyType | TypeKey | No | - | BAPolicyType | Type of Commercial Auto policy. Codes: [BA, garage, motor, BAphysdam] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| BACosts | BACost | Child collection |
| BALineCoverages | BusinessAutoCov | Line-level coverages for Commercial Auto. |
| BALineExclusions | BusinessAutoExcl | Line-level exclusions for Commercial Auto. |
| BALineConditions | BusinessAutoCond | Line-level conditions for Commercial Auto. |
| BAModifiers | BAModifier | Rating info for the line. |
| Drivers | CommercialDriver | Drivers on this policy line. |
| Jurisdictions | BAJurisdiction | Child collection |
| Vehicles | BusinessVehicle | Vehicles on this policy line. |

---

### Entity: BusinessOwnersLine

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BusinessOwnersLine.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\BusinessOwnersLine.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PolicyLine
**Effective-Dated Container Branch Field:** N/A
**Description:** Businessowners Policy line of business.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| ViewBundledCoverages | bit | No | - | - | Display or hide bundled coverages |
| EquipmentAutoNumberSeq | ForeignKey | No | AutoNumberSequence | - | Sequence to autonumber tools |
| BlanketType | TypeKey | No | - | BlanketType | Blanket Type Codes (9 total): [decline, build, bus, busbuild, location, ...] |
| SmallBusinessType | TypeKey | No | - | SmallBusinessType | Small Business Type Codes (15 total): [convenience, contractor, condominium, restaurant_fast, office, ...] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| BOPCosts | BOPCost | Child collection |
| BOPLineCoverages | BusinessOwnersCov | Line-level coverages for Business Owners. |
| BOPLineExclusions | BusinessOwnersExcl | Line-level exclusions for Business Owners. |
| BOPLineConditions | BusinessOwnersCond | Line-level conditions for Business Owners. |
| BOPLocations | BOPLocation | Locations on this policy line. |
| BOPModifiers | BOPModifier | Rating info for the line. |
| BOPScheduledEquipments | BOPScheduledEquipment | List of Scheduled Equipment for this policy line. |

---

### Entity: GeneralLiabilityLine

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\GeneralLiabilityLine.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\GeneralLiabilityLine.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PolicyLine
**Effective-Dated Container Branch Field:** N/A
**Description:** General Liability line of business.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| LocationLimits | bit | No | - | - | Do limits apply by location/project? |
| PollutionCleanupExp | bit | No | - | - | User selection for pollution cleanup expense, associated with Pollution liability coverage |
| ClaimsMadeOrigEffDate | datetime | No | - | - | Claims made original effective date |
| RetroactiveDate | datetime | No | - | - | Retroactive date for claims made. |
| SplitLimits | bit | No | - | - | Do split BI/PD split limits apply? |
| GLCoverageForm | TypeKey | No | - | GLCoverageFormType | Default: Occurrence Form of coverage (e.g. Occurrence, Claims Made) Codes: [Occurrence, ClaimsMade] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| GLCosts | GLCost | Child collection |
| Exposures | GLExposure | Exposures covered by this policy line |
| GLModifiers | GLModifier | Rating Modifiers for this policy line |
| GLLineCoverages | GeneralLiabilityCov | Line-level coverages for General Liability. |
| GLLineExclusions | GeneralLiabilityExcl | Line-level exclusions for General Liability. |
| GLLineConditions | GeneralLiabilityCond | Line-level conditions for General Liability. |

---

### Entity: HOPLine

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPLine.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\HOPLine.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PolicyLine
**Effective-Dated Container Branch Field:** N/A
**Description:** Homeowners line of business

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| HOPCosts_Ext | HOPCost | [Extension] Extension child collection |
| HOPLineCoverages_Ext | HOPLineCov | [Extension] Line-level coverages for Homeowners |
| HOPLineExclusions_Ext | HOPLineExcl | [Extension] Line-level exclusions for Homeowners |
| HOPLineConditions_Ext | HOPLineCond | [Extension] Line-level conditions for Homeowners |
| HOPLineModifiers_Ext | HOPLineMod | [Extension] Line-level modifiers for Homeowners |
| HOPCoverageParts_Ext | HOPCoveragePart | [Extension] Coverage Parts for the HOP line |

---

### Entity: InlandMarineLine

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\InlandMarineLine.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\InlandMarineLine.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PolicyLine
**Effective-Dated Container Branch Field:** N/A
**Description:** Inland Marine line of business.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| IMCoverageParts | IMCoveragePart | Coverage Parts for Inland Marine policy line. |
| IMLocations | IMLocation | Locations on this policy line. |
| IMCosts | IMCost | Child collection |

---

### Entity: WorkersCompLine

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\WorkersCompLine.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WorkersCompLine.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PolicyLine
**Effective-Dated Container Branch Field:** N/A
**Description:** Workers' Comp line of business.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| ManuscriptOptionDesc | longtext | No | - | - | The description of the manuscript endorsement |
| GoverningClass | ForeignKey | No | WCClassCode | - | Governing Class Code of policy line. |
| ManuscriptPremium | monetaryamount | No | - | - | The cost associate with the manuscript endorsement |
| ParticipatingPlan | OneToOne | No | WCParticipatingPlan | - | One-to-one link |
| RetrospectiveRatingPlan | OneToOne | No | WCRetrospectiveRatingPlan | - | One-to-one link |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| InclusionPersons | InclusionPerson | Included/excluded individuals. |
| Jurisdictions | WCJurisdiction | Child collection |
| WCAircraftSeats | WCAircraftSeat | Child collection |
| WCCosts | WCCost | Child collection |
| WCCoveredEmployees | WCCoveredEmployee | Child collection |
| WCCoveredEmployeeBases | WCCoveredEmployeeBase | Child collection |
| PolicyLaborClients | PolicyLaborClient | Employees that are leased by a company/person from another. |
| PolicyLaborContractors | PolicyLaborContractor | Employees that are contracted by a company/person to another. |
| PolicyOwnerOfficers | PolicyOwnerOfficer | Owner/officers on this line. |
| WCExcludedWorkplaces | WCExcludedWorkplace | Child collection |
| WCFedCoveredEmployees | WCFedCoveredEmployee | Child collection |
| WCLineCoverages | WorkersCompCov | Line-level coverages for Workers' Comp. |
| WCLineExclusions | WorkersCompExcl | Line-level exclusions for Workers' Comp. |
| WCLineConditions | WorkersCompCond | Line-level conditions for Workers' Comp. |
| WCWaiverOfSubros | WCWaiverOfSubro | Child collection |

---

### Entity: PersonalVehicle

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PersonalVehicle.eti`
**Entity Type:** `effdated`
**Database Table:** `personalvehicle`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Personal Vehicle

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| AnnualMileage | integer | No | - | - | Annual miles for this vehicle |
| BasisAmount | integer | No | - | - | Basis Amount |
| Color | varchar | No | - | - | Color of the vehicle. |
| CommutingMiles | integer | No | - | - | Daily one-way commuting mileage |
| LeaseOrRent | bit | No | - | - | Default: false If this vehicle is leased or rented. |
| LicensePlate | varchar | No | - | - | License plate of the vehicle. |
| Make | varchar | No | - | - | Make of the vehicle. |
| Model | varchar | No | - | - | Model of the vehicle. |
| VehicleNumber | integer | Yes | - | - | Vehicle number |
| QuickQuoteNumber | integer | No | - | - | The vehicle number for quick quote |
| Vin | vin | No | - | - | VIN (vehicle identification number) of the vehicle. |
| Year | year | No | - | - | Vehicle model year |
| GarageLocation | ForeignKey | Yes | PolicyLocation | - | Location of vehicle. |
| PALine | ForeignKey | Yes | PersonalAutoLine | - | Foreign key target: PersonalAutoLine |
| BodyType | TypeKey | No | - | BodyType | Body type of the vehicle. Codes (17 total): [bus, convertible, coupe, fourdoor, pickup, ...] |
| LengthOfLease | TypeKey | No | - | LengthOfLease | The lease period of a leased or a rented vehicle. Codes: [LessSixMonths, SixMonthsOrMore] |
| LicenseState | TypeKey | No | - | State | State in which the vehicle is licensed. Codes (142 total): [AK, AL, AR, AZ, CA, ...] |
| PipCovered | TypeKey | No | - | PipCovered | Indicate how PIP should be rated Codes: [0, 1, 2] |
| PrimaryUse | TypeKey | No | - | VehiclePrimaryUse | Primary use of the vehicle Codes (55 total): [business, pleasure, commuting, mixed, Commercial, ...] |
| VehicleType | TypeKey | No | - | VehicleType | Type of the vehicle. Codes: [Commercial, PP, PublicTransport, Special, auto, other] |
| CostNew | monetaryamount | No | - | - | Original retail cost of car. |
| StatedValue | monetaryamount | No | - | - | User enter stated value of vehicle |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| AdditionalInterests | PAVhcleAddlInterest | Third parties with an additional interest in the vehicle |
| Costs | PersonalAutoCovCost | Child collection |
| Coverages | PersonalVehicleCov | All coverages that apply directly to this vehicle. |
| Drivers | VehicleDriver | All drivers associated with this vehicle |
| PAVehicleModifiers | PAVehicleModifier | Rating info for the vehicle |

---

### Entity: BusinessVehicle

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BusinessVehicle.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\BusinessVehicle.etx`
**Entity Type:** `effdated`
**Database Table:** `businessvehicle`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Business Vehicle

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| Color | varchar | No | - | - | Color of the vehicle. |
| LeaseOrRent | bit | No | - | - | Default: false If this vehicle is leased or rented. |
| LicensePlate | varchar | No | - | - | License plate of the vehicle. |
| Make | varchar | No | - | - | Make of the vehicle. |
| Model | varchar | No | - | - | Model of the vehicle. |
| VehicleClassCode | shorttext | No | - | - | Vehicle classification code |
| VehicleCondition | bit | Yes | - | - | Default: true true if vehicle is new, false if vehicle is used |
| VehicleNumber | integer | Yes | - | - | Vehicle number |
| Vin | vin | No | - | - | VIN (vehicle identification number) of the vehicle. |
| Year | year | No | - | - | Vehicle model year |
| YearPurchased | year | No | - | - | year the vehicle is purchased |
| BALine | ForeignKey | Yes | BusinessAutoLine | - | Foreign key target: BusinessAutoLine |
| Location | ForeignKey | Yes | PolicyLocation | - | Location of the vehicle. |
| BodyType | TypeKey | No | - | BodyType | Body type of the vehicle. Codes (17 total): [bus, convertible, coupe, fourdoor, pickup, ...] |
| DestinationZone | TypeKey | No | - | Zone | Destination zone of vehicle Codes (48 total): [01, 02, 03, 04, 05, ...] |
| Experience | TypeKey | No | - | CombinedDriverExp | Experience of the possible drivers of this vehicle Codes: [AllDriversExpMore5, AllOther, MainDriverExpMore5, MainDriverExpLess5] |
| Industry | TypeKey | No | - | VehicleIndustry | The industry the vehicle is in Codes (8 total): [Truckers, Food, Special, Waste, Farmers, ...] |
| IndustryUse | TypeKey | No | - | VehicleIndustryUse | Vehicle industry use Codes (41 total): [commoncarrier, contractother, contractchemical, contractiron, exemptother, ...] |
| LengthOfLease | TypeKey | No | - | LengthOfLease | The lease period of a leased or a rented vehicle. Codes: [LessSixMonths, SixMonthsOrMore] |
| LicenseState | TypeKey | No | - | State | State in which the vehicle is licensed. Codes (142 total): [AK, AL, AR, AZ, CA, ...] |
| OriginationZone | TypeKey | No | - | Zone | Origination zone of vehicle Codes (48 total): [01, 02, 03, 04, 05, ...] |
| PrimaryUse | TypeKey | No | - | VehiclePrimaryUse | Primary use of the vehicle. Codes (55 total): [business, pleasure, commuting, mixed, Commercial, ...] |
| VehicleRadius | TypeKey | No | - | RadiusCode | Normal radius of operations from principle garage. Codes: [200PlusMiles, 0, 15orLess, 15orMore, LessThan50Miles, 50-200Miles] |
| VehicleSizeClass | TypeKey | No | - | VehicleSizeClass | Weight or size class of the vehicle. Codes (23 total): [LightTruck, MediumTruck, HeavyTruck, HeavyTruckTractor, ExtraHeavyTruck, ...] |
| VehicleType | TypeKey | No | - | VehicleType | Type of the vehicle. Codes: [Commercial, PP, PublicTransport, Special, auto, other] |
| CostNew | monetaryamount | Yes | - | - | Original retail cost of car. |
| StatedValue | monetaryamount | No | - | - | User enter stated value of vehicle |
| DoesUMUIMApply_Ext | bit | No | - | - | [Extension] Deprecated in PC 7.0 - Use vehicle modifier instead. Whether or not UM and UIM coverage applies to this vehicle |
| AntiLockBrakes_Ext | bit | No | - | - | [Extension] Deprecated in PC 7.0 - Use vehicle modifier instead. Whether or not the car has anti-lock brakes |
| AntiTheft_Ext | bit | No | - | - | [Extension] Deprecated in PC 7.0 - Use vehicle modifier instead. Whether or not the car is equipped with an anti-theft device |
| OwnedByPoliticalSub_Ext | bit | No | - | - | [Extension] Deprecated in PC 7.0 - Use vehicle modifier instead. Owned by political subdivision |
| SafeDrivingCert_Ext | bit | No | - | - | [Extension] Deprecated in PC 7.0 - Use vehicle modifier instead. Whether or not the primary driver of the vehicle has a safe driving certificate |
| IntraInterStateUsage_Ext | TypeKey | No | - | IntraInterStateUsage | [Extension] Deprecated in PC 7.0 - Use vehicle modifier instead. IntraInterStateUsage applicable only to MI |
| PipCovered_Ext | TypeKey | No | - | PipCovered | [Extension] Deprecated in PC 7.0 - Use vehicle modifier instead. Indicate how PIP should be rated |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| AdditionalInterests | BAVhcleAddlInterest | Additional interests on this vehicle |
| Costs | BAStateCovVehicleCost | Child collection |
| LineCosts | BALineCovCost | Costs for Commercial Auto Line coverages |
| Coverages | BusinessVehicleCov | All coverages that apply directly to this vehicle. |
| BusinessVehicleModifiers | BusinessVehicleModifier | Rating info for the line. |

---

### Entity: PolicyDriver

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyDriver.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PAPolicyContactRole
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| ApplicableGoodDriverDiscount | bit | No | - | - | Indicates whether this driver qualifies for a Good Driver discount |
| ExcludedInternal | bit | No | - | - | If set, indicates that this driver is part of the policy but is not covered under this policy |
| LicenseNumberInternal | driverlicense | No | - | - | Driver's license number. |
| QuickQuoteNumber | integer | No | - | - | The driver number for quick quote |
| DoNotOrderMVR | bit | No | - | - | Indicates whether MVR records can be ordered for this driver |
| LicenseStateInternal | TypeKey | No | - | Jurisdiction | Driver's license jurisdiction. Codes (98 total): [AK, AL, AR, AZ, CA, ...] |
| NumberOfAccidents | TypeKey | No | - | NumberofAccidents | Number of accidents updated by the Agent Codes: [0, 1, 2, 3, 4, 5] |
| NumberOfViolations | TypeKey | No | - | NumberofAccidents | Number of violations updated by the Agent Codes: [0, 1, 2, 3, 4, 5] |
| PolicyDriverMVR | OneToOne | No | PolicyDriverMVR | - | The MVR summary data for this driver |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| VehicleDrivers | VehicleDriver | The Vehicles that this Driver drives |

---

### Entity: VehicleDriver

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\VehicleDriver.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\VehicleDriver.etx`
**Entity Type:** `effdated`
**Database Table:** `vehicledriver`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Associates a vehicle and a driver in Personal Auto

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| PercentageDriven | integer | Yes | - | - | Default: 100 The percentage this driver drives the vehicle |
| Vehicle | ForeignKey | Yes | PersonalVehicle | - | Foreign key target: PersonalVehicle |
| PolicyDriver | ForeignKey | Yes | PolicyDriver | - | Foreign key target: PolicyDriver |

---

### Entity: CommercialDriver

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\CommercialDriver.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\CommercialDriver.etx`
**Entity Type:** `effdated`
**Database Table:** `commercialdriver`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A driver on a Commercial Auto policy.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| DateOfBirth | datetime | No | - | - | Date of Birth |
| DriverTraining | bit | No | - | - | Has this driver completed a driver training class? |
| FirstName | firstname | No | - | - | First name. |
| GoodDriverDiscount | bit | No | - | - | Indicates whether this driver qualifies for a Good Driver discount |
| HireDate | datetime | No | - | - | When this contact was hired. |
| LastName | lastname | No | - | - | Last name. |
| LicenseNumber | varchar | No | - | - | Driver's license number. |
| MatureDriverTraining | bit | No | - | - | Has the driver completed a mature driver training class? |
| SeqNumber | integer | Yes | - | - | The driver's sequence number used to order the drivers within a policy. |
| Student | bit | No | - | - | Is this driver a student? |
| YearLicensed | year | No | - | - | The year that this contact first acquired a driver's license. |
| BusinessAutoLine | ForeignKey | Yes | BusinessAutoLine | - | Foreign key target: BusinessAutoLine |
| Gender | TypeKey | No | - | GenderType | Gender. Codes: [M, F] |
| LicenseState | TypeKey | No | - | State | Driver's license state. Codes (142 total): [AK, AL, AR, AZ, CA, ...] |
| MaritalStatus | TypeKey | No | - | MaritalStatus | Marital status. Codes (7 total): [C, D, M, P, S, ...] |
| NumberofAccidents | TypeKey | No | - | NumberofAccidents | Number of Accidents Codes: [0, 1, 2, 3, 4, 5] |
| NumberofViolations | TypeKey | No | - | NumberofAccidents | Number of Violations Codes: [0, 1, 2, 3, 4, 5] |
| YearsExperience | TypeKey | No | - | DriverExperience | The number of years of driving experience this contact has. Codes (8 total): [LessThan5, FiveToTen, TenToTwenty, MoreThanTwenty, Morethan2, ...] |
| FirstNameKanji_Ext | firstname | No | - | - | [Extension] First name in Kanji |
| LastNameKanji_Ext | lastname | No | - | - | [Extension] Last name in Kanji. |

---

### Entity: CPLocation

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\CPLocation.eti`
**Entity Type:** `effdated`
**Database Table:** `cplocation`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** CP Location

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| PrincipalOpsDesc | varchar | No | - | - | Principle operations and occupancy. |
| CPLine | ForeignKey | Yes | CommercialPropertyLine | - | Foreign key target: CommercialPropertyLine |
| Location | ForeignKey | Yes | PolicyLocation | - | Location of business exposure, e.g., one or more buildings. |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Coverages | CPLocationCov | All coverages that apply directly to this location. |
| Buildings | CPBuilding | Buildings on this location |

---

### Entity: CPBuilding

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\CPBuilding.eti`
**Entity Type:** `effdated`
**Database Table:** `cpbuilding`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** CP Building

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| Building | ForeignKey | Yes | Building | - | Foreign key target: Building |
| ClassCode | ForeignKey | Yes | CPClassCode | - | Class code of building. |
| CPLocation | ForeignKey | Yes | CPLocation | - | Foreign key target: CPLocation |
| CoverageForm | TypeKey | Yes | - | CoverageForm | Defines the set of coverages that are available; also known as coverage parts. Codes: [BPP, CondoAssoc, CondoUnitOwners] |
| RateType | TypeKey | Yes | - | RateType | Default: Class Rate using a table or specific value. Codes: [Class, Specific] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Coverages | CPBuildingCov | All coverages that apply directly to this building. |
| AdditionalInterests | CPBldgAddlInterest | Additional interests on this building |

---

### Entity: BOPLocation

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BOPLocation.eti`
**Entity Type:** `effdated`
**Database Table:** `boplocation`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** BOP Location

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| CityLimits | bit | No | - | - | Whether the location is within city limits |
| PrincipalOpsDesc | varchar | No | - | - | Principle operations and occupancy. |
| BOPLine | ForeignKey | Yes | BusinessOwnersLine | - | Foreign key target: BusinessOwnersLine |
| Location | ForeignKey | Yes | PolicyLocation | - | Location of business exposure, e.g., one or more buildings. |
| RiskClass | ForeignKey | No | RiskClass | - | Foreign key to Risk Class Codes |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Buildings | BOPBuilding | Buildings on this location |
| Coverages | BOPLocationCov | All coverages that apply directly to this location. |
| LocationAnswers | BOPLocationAnswer | Set of answers for any questions on this location |

---

### Entity: BOPBuilding

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BOPBuilding.eti`
**Entity Type:** `effdated`
**Database Table:** `bopbuilding`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** BOP Building

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BasisAmount | integer | No | - | - | Basis Amount |
| BOPLocation | ForeignKey | Yes | BOPLocation | - | Foreign key target: BOPLocation |
| Building | ForeignKey | Yes | Building | - | Foreign key target: Building |
| ClassCode | ForeignKey | No | BOPClassCode | - | Class code of building. |
| ConstructionType | TypeKey | No | - | BOPConstructionType | Type of building construction Codes: [F, JM, MNC, NC, R] |
| NumDiving | TypeKey | No | - | DivingBoards | Number of diving boards Codes (10 total): [1, 2, 3, 4, 5, ...] |
| NumPools | TypeKey | No | - | SwimmingPools | Number of swimming pools Codes (10 total): [1, 2, 3, 4, 5, ...] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| AdditionalInterests | BOPBldgAddlInterest | Additional interests on this building |
| Coverages | BOPBuildingCov | All coverages that apply directly to this building. |
| Costs | BOPCovBuildingCost | Child collection |

---

### Entity: HOPDwelling

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPDwelling.eti`
**Entity Type:** `effdated`
**Database Table:** `hopdwelling`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Dwellings for Homeowners Line

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| FloodingHazard | bit | No | - | - | Flooding or landslide hazard? |
| NearCommercial | bit | No | - | - | Property within 300 ft of commercial or non-residential property? |
| DistanceToFireStation | positiveinteger | No | - | - | Distance to Fire Station |
| DistanceToFireHydrant | positiveinteger | No | - | - | Distance to Fire Hydrant |
| VisibleToNeighbors | bit | No | - | - | Is the dwelling visible to neighbors |
| TrampolineSafetyNet | bit | No | - | - | Is there a safety net? |
| TrampolineExists | bit | No | - | - | Trampoline exists on property? |
| RoomerBoardersNumber | nonnegativeinteger | No | - | - | Number of roomers or boarders |
| RoofTypeDescription | varchar | No | - | - | Description of Roof Type for type Other |
| RoofingUpgradeDate | year | No | - | - | Date of Roofing Upgrade |
| PrimaryHeatingDescription | varchar | No | - | - | Description of primary heating for type Other |
| PlumbingUpgradeDate | year | No | - | - | Date of Plumbing Upgrade |
| PlumbingTypeDescription | varchar | No | - | - | Description of plumbing for type Other |
| KnownWaterLeakageDescription | varchar | No | - | - | Description of water leakage |
| KnownWaterLeakage | bit | No | - | - | Any water leakage |
| HeatingUpgradeDate | year | No | - | - | Date of Heating Upgrade |
| FireplaceOrWoodStovesNumber | nonnegativeinteger | No | - | - | Number of woodstoves or fire places |
| ElectricalSystemUpgradeDate | year | No | - | - | Date of Electrical System Upgrade |
| Deadbolts | bit | No | - | - | Do all the doors have Deadbolts |
| ConstructionTypeDescription | varchar | No | - | - | Description of construction for type Other |
| YearBuilt | year | No | - | - | Year Built |
| NumberOfFireExtinguishers | nonnegativeinteger | No | - | - | How many fire extinguishers are on premises |
| UnitsNumber | positiveinteger | No | - | - | Number of units between firewall |
| StoriesNumber | positiveinteger | No | - | - | Number of stories in the dwelling |
| InsuredUnits | positiveinteger | No | - | - | Number of units to be insured |
| Location | ForeignKey | Yes | PolicyLocation | - | Foreign key target: PolicyLocation |
| HOPCoveragePart | ForeignKey | No | HOPCoveragePart | - | Foreign key target: HOPCoveragePart |
| CoverageForm | TypeKey | No | - | HOPCoverageForm | The HO coverage form for this dwelling Codes: [ho2, ho3, ho5, ho4, ho6] |
| WiringType | TypeKey | No | - | WiringType | Electrical Wiring Type Codes: [copper, aluminum, KnobAndTube] |
| SprinklerSystemType | TypeKey | No | - | SprinklerSystemType | Sprinkler System Type Codes: [none, full, partial] |
| RoofType | TypeKey | No | - | HOPRoofType | Roof Material Classification Codes (8 total): [composite, asphalt, wood, metal, targravel, ...] |
| ResidenceType | TypeKey | No | - | ResidenceType | Residence Type Codes (8 total): [Fam1, Fam2, Fam3, Fam4, Fam5, ...] |
| PrimaryHeatingFuelTankLocation | TypeKey | No | - | FuelTankLocationType | Location of fuel tank for Oil based heating Codes: [IAGMF, IAGNMF, OAG, OBG] |
| PrimaryHeatingFuelLineLocation | TypeKey | No | - | FuelLineLocationType | Location of fuel line for Oil based heating Codes: [under, through] |
| PrimaryHeatingType | TypeKey | No | - | HeatingType | Dwelling Heating Type Codes: [electric, gas, oil, other] |
| PlumbingType | TypeKey | No | - | PlumbingType | Plumbing Type Codes: [copper, galv, pvc, other] |
| Occupancy | TypeKey | No | - | DwellingOccupancyType | How the dwelling is being occupied Codes: [owner, tenant, vacant, uoccupied, inconst] |
| GarageType | TypeKey | No | - | GarageType | Garage type in dwelling Codes (9 total): [None, Attached-1, Attached-2, Attached-3, Attached-4, ...] |
| Foundation | TypeKey | No | - | FoundationType | Foundation Type Codes: [Slab, RaisedSlab, PierAndBeam, CrawlSpace, FullBasement] |
| FireAlarmType | TypeKey | No | - | FireAlarmType | Fire alarm type Codes: [none, local, monitoringcenter] |
| ElectricalType | TypeKey | No | - | BreakerType | Electrical Type Codes: [CircuitBreaker, Fuses] |
| DwellingUsage | TypeKey | No | - | DwellingUsage | Dwelling Usage Codes: [primary, secondary, seasonal, rental] |
| DwellingLocation | TypeKey | No | - | DwellingLocationType | Dwelling Location Type Codes: [city, fire, prot, unprot, other] |
| ConstructionType | TypeKey | No | - | HOPConstructionType | Dwelling Construction Type Codes: [concrete, frame, masonry, steel, log, other] |
| BurglarAlarmType | TypeKey | No | - | BurglarAlarmType | Burglar Alarm Type Codes: [police, central, local, none] |
| SmokeAlarm | TypeKey | No | - | SmokeAlarms | Smoke Alarms on Premises Codes: [none, allfloors, partial] |
| SecondaryHeatingType | TypeKey | No | - | HeatingType | Secondary Heating Type Codes: [electric, gas, oil, other] |
| ReplacementCost | monetaryamount | No | - | - | Replacement Cost |
| SwimmingPool | OneToOne | No | HOPSwimmingPool | - | One-to-one link |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Coverages | HOPDwellingCov | Coverages directly attached to the Dwelling |
| Exclusions | HOPDwellingExcl | Exclusions directly attached to the Dwelling |
| Conditions | HOPDwellingCond | Conditions directly attached to the Dwelling |
| HOPDwellingMods | HOPDwellingMod | Modifiers directly attached to the Dwelling |
| AdditionalInterests | HOPDwellAddlInterest | Third parties with an additional interest in the Dwelling |
| DwellingAnimals | DwellingAnimal | Animals in the dwelling premises |
| DwellingHazards | DwellingHazard | Hazards in the dwelling premises |

---

### Entity: HOPCoveragePart

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPCoveragePart.eti`
**Entity Type:** `effdated`
**Database Table:** `hopcoveragepart`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Coverage Parts for the HOP line

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| HOPLine | ForeignKey | Yes | HOPLine | - | Foreign key target: HOPLine |
| CoveragePartType | TypeKey | No | - | CoveragePartType | The type of this coverage part (Rental, Condominium, Dwelling) |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| HOPDwellings | HOPDwelling | Dwellings for this Coverage Part |
| Coverages | HOPCoveragePartCov | Coverages directly attached to the HOPCoveragePart |
| Exclusions | HOPCoveragePartExcl | Exclusions directly attached to the HOPCoveragePart |
| Conditions | HOPCoveragePartCond | Conditions directly attached to the HOPCoveragePart |
| HOPCoveragePartMods | HOPCoveragePartMod | Modifiers directly attached to the HOPCoveragePart |

---

### Entity: WCCoveredEmployee

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\WCCoveredEmployee.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WCCoveredEmployeeBase
**Effective-Dated Container Branch Field:** N/A
**Description:** A Workers' Comp Federal Covered Employee

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Costs | WCCovEmpCost | Child collection |

---

### Entity: WC7CoveredEmployee

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7CoveredEmployee.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WC7CoveredEmployeeBase
**Effective-Dated Container Branch Field:** N/A
**Description:** A Workers' Comp Covered Employee

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| WC7Costs | WC7CovEmpCost | Child collection |

---

### Entity: Coverage

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Coverage.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| PatternCode | patterncode | Yes | - | - | The pattern defining what kind of Coverage this is |
| ReferenceDateInternal | datetime | No | - | - | Internal field for storing the reference date of coverages on bound policy periods. Normally the ReferenceDate property should be used instead. |
| Currency | TypeKey | Yes | - | Currency | Currency associated with the coverage Codes (7 total): [usd, eur, gbp, cad, aud, ...] |

---

### Entity: Clause

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Clause.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: PersonalAutoCov

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PersonalAutoCov.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\PersonalAutoCov.etx`
**Entity Type:** `effdated`
**Database Table:** `personalautocov`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A line-level coverage for Personal Auto

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| ChoiceTerm1 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm1Avl | bit | No | - | - | whether or not the ChoiceTerm1 field was available the last time availability was checked |
| ChoiceTerm2 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm2Avl | bit | No | - | - | whether or not the ChoiceTerm2 field was available the last time availability was checked |
| ChoiceTerm3 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm3Avl | bit | No | - | - | whether or not the ChoiceTerm3 field was available the last time availability was checked |
| ChoiceTerm4 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm4Avl | bit | No | - | - | whether or not the ChoiceTerm4 field was available the last time availability was checked |
| ChoiceTerm5 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm5Avl | bit | No | - | - | whether or not the ChoiceTerm5 field was available the last time availability was checked |
| ChoiceTerm6 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm6Avl | bit | No | - | - | whether or not the ChoiceTerm6 field was available the last time availability was checked |
| ChoiceTerm7 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm7Avl | bit | No | - | - | whether or not the ChoiceTerm7 field was available the last time availability was checked |
| ChoiceTerm8 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm8Avl | bit | No | - | - | whether or not the ChoiceTerm8 field was available the last time availability was checked |
| BooleanTerm1 | bit | No | - | - | boolean cov term field |
| BooleanTerm1Avl | bit | No | - | - | whether or not the BooleanTerm1 field was available the last time availability was checked |
| BooleanTerm2 | bit | No | - | - | boolean cov term field |
| BooleanTerm2Avl | bit | No | - | - | whether or not the BooleanTerm2 field was available the last time availability was checked |
| BooleanTerm3 | bit | No | - | - | boolean cov term field |
| BooleanTerm3Avl | bit | No | - | - | whether or not the BooleanTerm3 field was available the last time availability was checked |
| BooleanTerm4 | bit | No | - | - | boolean cov term field |
| BooleanTerm4Avl | bit | No | - | - | whether or not the BooleanTerm4 field was available the last time availability was checked |
| PALine | ForeignKey | Yes | PersonalAutoLine | - | Foreign key target: PersonalAutoLine |
| ChoiceTerm9_Ext | patterncode | No | - | - | [Extension] choice cov term field |
| ChoiceTerm10_Ext | patterncode | No | - | - | [Extension] choice cov term field |
| ChoiceTerm11_Ext | patterncode | No | - | - | [Extension] choice cov term field |
| ChoiceTerm12_Ext | patterncode | No | - | - | [Extension] choice cov term field |
| ChoiceTerm13_Ext | patterncode | No | - | - | [Extension] choice cov term field |
| ChoiceTerm9Avl_Ext | bit | No | - | - | [Extension] whether or not the ChoiceTerm8 field was available the last time availability was checked |
| ChoiceTerm10Avl_Ext | bit | No | - | - | [Extension] whether or not the ChoiceTerm8 field was available the last time availability was checked |
| ChoiceTerm11Avl_Ext | bit | No | - | - | [Extension] whether or not the ChoiceTerm8 field was available the last time availability was checked |
| ChoiceTerm12Avl_Ext | bit | No | - | - | [Extension] whether or not the ChoiceTerm8 field was available the last time availability was checked |
| ChoiceTerm13Avl_Ext | bit | No | - | - | [Extension] whether or not the ChoiceTerm8 field was available the last time availability was checked |
| DirectTerm1_Ext | decimal | No | - | - | [Extension] Direct cov term field |
| DirectTerm1Avl_Ext | bit | No | - | - | [Extension] whether or not the Direct Term 1 field was available the last time availability was checked |
| DirectTerm2_Ext | bit | No | - | - | [Extension] Direct cov term field |
| DirectTerm2Avl_Ext | bit | No | - | - | [Extension] whether or not the Direct Term 2 field was available the last time availability was checked |
| DirectTerm3_Ext | decimal | No | - | - | [Extension] Direct cov term field |
| DirectTerm3Avl_Ext | bit | No | - | - | [Extension] whether or not the Direct Term 3 field was available the last time availability was checked |
| BooleanTerm5_Ext | bit | No | - | - | [Extension] Boolean cov term field |
| DateTerm1_Ext | dateonly | No | - | - | [Extension] Date cov term field |
| BooleanTerm6_Ext | bit | No | - | - | [Extension] Boolean cov term field |
| DateTerm2_Ext | dateonly | No | - | - | [Extension] Date cov term field |
| BooleanTerm7_Ext | bit | No | - | - | [Extension] Boolean cov term field |
| DateTerm3_Ext | dateonly | No | - | - | [Extension] Date cov term field |
| BooleanTerm5Avl_Ext | bit | No | - | - | [Extension] whether or not the Direct Term 1 field was available the last time availability was checked |
| DateTerm1Avl_Ext | bit | No | - | - | [Extension] whether or not the Direct Term 1 field was available the last time availability was checked |
| BooleanTerm6Avl_Ext | bit | No | - | - | [Extension] whether or not the Direct Term 1 field was available the last time availability was checked |
| DateTerm2Avl_Ext | bit | No | - | - | [Extension] whether or not the Direct Term 1 field was available the last time availability was checked |
| BooleanTerm7Avl_Ext | bit | No | - | - | [Extension] whether or not the Direct Term 1 field was available the last time availability was checked |
| DateTerm3Avl_Ext | bit | No | - | - | [Extension] whether or not the Direct Term 1 field was available the last time availability was checked |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Costs | PersonalAutoCovCost | Child collection |

---

### Entity: PersonalVehicleCov

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PersonalVehicleCov.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\PersonalVehicleCov.etx`
**Entity Type:** `effdated`
**Database Table:** `personalvehiclecov`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A vehicle-level coverage for Personal Auto

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| ChoiceTerm1 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm1Avl | bit | No | - | - | whether or not the ChoiceTerm1 field was available the last time availability was checked |
| ChoiceTerm2 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm2Avl | bit | No | - | - | whether or not the ChoiceTerm2 field was available the last time availability was checked |
| BooleanTerm1 | bit | No | - | - | boolean cov term field |
| BooleanTerm1Avl | bit | No | - | - | whether or not the BooleanTerm1 field was available the last time availability was checked |
| PersonalVehicle | ForeignKey | Yes | PersonalVehicle | - | Foreign key target: PersonalVehicle |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Costs | PersonalVehicleCovCost | Child collection |

---

### Entity: BusinessAutoCov

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BusinessAutoCov.eti`
**Entity Type:** `effdated`
**Database Table:** `businessautocov`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A line-level coverage for Commercial Auto

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| DirectTerm1 | decimal | No | - | - | direct cov term field |
| DirectTerm1Avl | bit | No | - | - | whether or not the DirectTerm1 field was available the last time availability was checked |
| DirectTerm2 | decimal | No | - | - | direct cov term field |
| DirectTerm2Avl | bit | No | - | - | whether or not the DirectTerm2 field was available the last time availability was checked |
| DirectTerm3 | decimal | No | - | - | direct cov term field |
| DirectTerm3Avl | bit | No | - | - | whether or not the DirectTerm3 field was available the last time availability was checked |
| DateTerm1 | datetime | No | - | - | datetime cov term field |
| DateTerm1Avl | bit | No | - | - | whether or not the DateTerm1 field was available the last time availability was checked |
| DateTerm2 | datetime | No | - | - | datetime cov term field |
| DateTerm2Avl | bit | No | - | - | whether or not the DateTerm2 field was available the last time availability was checked |
| ChoiceTerm1 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm1Avl | bit | No | - | - | whether or not the ChoiceTerm1 field was available the last time availability was checked |
| ChoiceTerm2 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm2Avl | bit | No | - | - | whether or not the ChoiceTerm2 field was available the last time availability was checked |
| ChoiceTerm3 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm3Avl | bit | No | - | - | whether or not the ChoiceTerm3 field was available the last time availability was checked |
| ChoiceTerm4 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm4Avl | bit | No | - | - | whether or not the ChoiceTerm4 field was available the last time availability was checked |
| ChoiceTerm5 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm5Avl | bit | No | - | - | whether or not the ChoiceTerm5 field was available the last time availability was checked |
| BooleanTerm1 | bit | No | - | - | boolean cov term field |
| BooleanTerm1Avl | bit | No | - | - | whether or not the BooleanTerm1 field was available the last time availability was checked |
| BooleanTerm2 | bit | No | - | - | boolean cov term field |
| BooleanTerm2Avl | bit | No | - | - | whether or not the BooleanTerm2 field was available the last time availability was checked |
| StringTerm1 | shorttext | No | - | - | string cov term field |
| StringTerm1Avl | bit | No | - | - | whether or not the StringTerm1 field was available the last time availability was checked |
| StringTerm2 | shorttext | No | - | - | string cov term field |
| StringTerm2Avl | bit | No | - | - | whether or not the StringTerm2 field was available the last time availability was checked |
| BALine | ForeignKey | No | BusinessAutoLine | - | Foreign key target: BusinessAutoLine |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Costs | BALineCovCost | Costs for Commercial Auto Line coverages |

---

### Entity: BusinessOwnersCov

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BusinessOwnersCov.eti`
**Entity Type:** `effdated`
**Database Table:** `businessownerscov`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A line-level coverage for Business Owners

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| ChoiceTerm1 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm1Avl | bit | No | - | - | whether or not the ChoiceTerm1 field was available the last time availability was checked |
| ChoiceTerm2 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm2Avl | bit | No | - | - | whether or not the ChoiceTerm2 field was available the last time availability was checked |
| ChoiceTerm3 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm3Avl | bit | No | - | - | whether or not the ChoiceTerm3 field was available the last time availability was checked |
| ChoiceTerm4 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm4Avl | bit | No | - | - | whether or not the ChoiceTerm4 field was available the last time availability was checked |
| ChoiceTerm5 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm5Avl | bit | No | - | - | whether or not the ChoiceTerm5 field was available the last time availability was checked |
| ChoiceTerm6 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm6Avl | bit | No | - | - | whether or not the ChoiceTerm6 field was available the last time availability was checked |
| ChoiceTerm7 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm7Avl | bit | No | - | - | whether or not the ChoiceTerm7 field was available the last time availability was checked |
| ChoiceTerm8 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm8Avl | bit | No | - | - | whether or not the ChoiceTerm8 field was available the last time availability was checked |
| ChoiceTerm9 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm9Avl | bit | No | - | - | whether or not the ChoiceTerm9 field was available the last time availability was checked |
| ChoiceTerm10 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm10Avl | bit | No | - | - | whether or not the ChoiceTerm10 field was available the last time availability was checked |
| ChoiceTerm11 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm11Avl | bit | No | - | - | whether or not the ChoiceTerm11 field was available the last time availability was checked |
| ChoiceTerm12 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm12Avl | bit | No | - | - | whether or not the ChoiceTerm12 field was available the last time availability was checked |
| ChoiceTerm13 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm13Avl | bit | No | - | - | whether or not the ChoiceTerm13 field was available the last time availability was checked |
| ChoiceTerm14 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm14Avl | bit | No | - | - | whether or not the ChoiceTerm14 field was available the last time availability was checked |
| ChoiceTerm15 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm15Avl | bit | No | - | - | whether or not the ChoiceTerm15 field was available the last time availability was checked |
| ChoiceTerm16 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm16Avl | bit | No | - | - | whether or not the ChoiceTerm16 field was available the last time availability was checked |
| ChoiceTerm17 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm17Avl | bit | No | - | - | whether or not the ChoiceTerm17 field was available the last time availability was checked |
| ChoiceTerm18 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm18Avl | bit | No | - | - | whether or not the ChoiceTerm18 field was available the last time availability was checked |
| ChoiceTerm19 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm19Avl | bit | No | - | - | whether or not the ChoiceTerm19 field was available the last time availability was checked |
| ChoiceTerm20 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm20Avl | bit | No | - | - | whether or not the ChoiceTerm20 field was available the last time availability was checked |
| DateTerm1 | datetime | No | - | - | datetime cov term field |
| DateTerm1Avl | bit | No | - | - | whether or not the DateTerm1 field was available the last time availability was checked |
| DirectTerm1 | decimal | No | - | - | direct cov term field |
| DirectTerm1Avl | bit | No | - | - | whether or not the DirectTerm1 field was available the last time availability was checked |
| DirectTerm2 | decimal | No | - | - | direct cov term field |
| DirectTerm2Avl | bit | No | - | - | whether or not the DirectTerm2 field was available the last time availability was checked |
| DirectTerm3 | decimal | No | - | - | direct cov term field |
| DirectTerm3Avl | bit | No | - | - | whether or not the DirectTerm3 field was available the last time availability was checked |
| DirectTerm4 | decimal | No | - | - | direct cov term field |
| DirectTerm4Avl | bit | No | - | - | whether or not the DirectTerm4 field was available the last time availability was checked |
| DirectTerm5 | decimal | No | - | - | direct cov term field |
| DirectTerm5Avl | bit | No | - | - | whether or not the DirectTerm5 field was available the last time availability was checked |
| DirectTerm6 | decimal | No | - | - | direct cov term field |
| DirectTerm6Avl | bit | No | - | - | whether or not the DirectTerm6 field was available the last time availability was checked |
| DirectTerm7 | decimal | No | - | - | direct cov term field |
| DirectTerm7Avl | bit | No | - | - | whether or not the DirectTerm7 field was available the last time availability was checked |
| DirectTerm8 | decimal | No | - | - | direct cov term field |
| DirectTerm8Avl | bit | No | - | - | whether or not the DirectTerm8 field was available the last time availability was checked |
| DirectTerm9 | decimal | No | - | - | direct cov term field |
| DirectTerm9Avl | bit | No | - | - | whether or not the DirectTerm9 field was available the last time availability was checked |
| StringTerm1 | shorttext | No | - | - | string cov term field |
| StringTerm1Avl | bit | No | - | - | whether or not the StringTerm1 field was available the last time availability was checked |
| BOPLine | ForeignKey | No | BusinessOwnersLine | - | Foreign key target: BusinessOwnersLine |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Costs | BOPCovCost | Child collection |

---

### Entity: GeneralLiabilityCov

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\GeneralLiabilityCov.eti`
**Entity Type:** `effdated`
**Database Table:** `glcov`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A line-level coverage for General Liability

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BooleanTerm1 | bit | No | - | - | boolean cov term field |
| BooleanTerm1Avl | bit | No | - | - | whether or not the BooleanTerm1 field was available the last time availability was checked |
| ChoiceTerm1 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm1Avl | bit | No | - | - | whether or not the ChoiceTerm1 field was available the last time availability was checked |
| ChoiceTerm2 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm2Avl | bit | No | - | - | whether or not the ChoiceTerm2 field was available the last time availability was checked |
| ChoiceTerm3 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm3Avl | bit | No | - | - | whether or not the ChoiceTerm3 field was available the last time availability was checked |
| ChoiceTerm4 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm4Avl | bit | No | - | - | whether or not the ChoiceTerm4 field was available the last time availability was checked |
| ChoiceTerm5 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm5Avl | bit | No | - | - | whether or not the ChoiceTerm5 field was available the last time availability was checked |
| ChoiceTerm6 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm6Avl | bit | No | - | - | whether or not the ChoiceTerm6 field was available the last time availability was checked |
| ChoiceTerm7 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm7Avl | bit | No | - | - | whether or not the ChoiceTerm7 field was available the last time availability was checked |
| ChoiceTerm8 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm8Avl | bit | No | - | - | whether or not the ChoiceTerm8 field was available the last time availability was checked |
| ChoiceTerm9 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm9Avl | bit | No | - | - | whether or not the ChoiceTerm9 field was available the last time availability was checked |
| ChoiceTerm10 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm10Avl | bit | No | - | - | whether or not the ChoiceTerm9 field was available the last time availability was checked |
| ChoiceTerm11 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm11Avl | bit | No | - | - | whether or not the ChoiceTerm9 field was available the last time availability was checked |
| ChoiceTerm12 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm12Avl | bit | No | - | - | whether or not the ChoiceTerm9 field was available the last time availability was checked |
| DateTerm1 | datetime | No | - | - | datetime cov term field |
| DateTerm1Avl | bit | No | - | - | whether or not the DateTerm1 field was available the last time availability was checked |
| DirectTerm1 | decimal | No | - | - | direct cov term field |
| DirectTerm1Avl | bit | No | - | - | whether or not the DirectTerm1 field was available the last time availability was checked |
| DirectTerm2 | decimal | No | - | - | direct cov term field |
| DirectTerm2Avl | bit | No | - | - | whether or not the DirectTerm2 field was available the last time availability was checked |
| StringTerm1 | shorttext | No | - | - | string cov term field |
| StringTerm1Avl | bit | No | - | - | whether or not the StringTerm1 field was available the last time availability was checked |
| GLLine | ForeignKey | Yes | GeneralLiabilityLine | - | Foreign key target: GeneralLiabilityLine |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Costs | GLCovCost | Child collection |

---

### Entity: HOPDwellingCov

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPDwellingCov.eti`
**Entity Type:** `effdated`
**Database Table:** `hopdwellingcov`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Coverages directly attached to each Dwelling

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BooleanTerm1 | bit | No | - | - | boolean cov term field |
| BooleanTerm1Avl | bit | No | - | - | whether or not the BooleanTerm1 field was available the last time availability was checked |
| BooleanTerm2 | bit | No | - | - | boolean cov term field |
| BooleanTerm2Avl | bit | No | - | - | whether or not the BooleanTerm2 field was available the last time availability was checked |
| BooleanTerm3 | bit | No | - | - | boolean cov term field |
| BooleanTerm3Avl | bit | No | - | - | whether or not the BooleanTerm3 field was available the last time availability was checked |
| ChoiceTerm1 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm1Avl | bit | No | - | - | whether or not the ChoiceTerm1 field was available the last time availability was checked |
| ChoiceTerm2 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm2Avl | bit | No | - | - | whether or not the ChoiceTerm2 field was available the last time availability was checked |
| ChoiceTerm3 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm3Avl | bit | No | - | - | whether or not the ChoiceTerm3 field was available the last time availability was checked |
| ChoiceTerm4 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm4Avl | bit | No | - | - | whether or not the ChoiceTerm4 field was available the last time availability was checked |
| ChoiceTerm5 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm5Avl | bit | No | - | - | whether or not the ChoiceTerm5 field was available the last time availability was checked |
| DateTerm1 | datetime | No | - | - | datetime cov term field |
| DateTerm1Avl | bit | No | - | - | whether or not the DateTerm1 field was available the last time availability was checked |
| DateTerm2 | datetime | No | - | - | datetime cov term field |
| DateTerm2Avl | bit | No | - | - | whether or not the DateTerm2 field was available the last time availability was checked |
| DirectTerm1 | decimal | No | - | - | direct cov term field |
| DirectTerm1Avl | bit | No | - | - | whether or not the DirectTerm1 field was available the last time availability was checked |
| DirectTerm2 | decimal | No | - | - | direct cov term field |
| DirectTerm2Avl | bit | No | - | - | whether or not the DirectTerm2 field was available the last time availability was checked |
| DirectTerm3 | decimal | No | - | - | direct cov term field |
| DirectTerm3Avl | bit | No | - | - | whether or not the DirectTerm3 field was available the last time availability was checked |
| StringTerm1 | shorttext | No | - | - | string cov term field |
| StringTerm1Avl | bit | No | - | - | whether or not the StringTerm1 field was available the last time availability was checked |
| StringTerm2 | shorttext | No | - | - | string cov term field |
| StringTerm2Avl | bit | No | - | - | whether or not the StringTerm2 field was available the last time availability was checked |
| HOPDwelling | ForeignKey | Yes | HOPDwelling | - | Foreign key target: HOPDwelling |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| HOPDwellingCovCosts | HOPDwellingCovCost | Child collection |

---

### Entity: HOPLineCov

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPLineCov.eti`
**Entity Type:** `effdated`
**Database Table:** `hoplinecov`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Coverages for the Homeowners line

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BooleanTerm1 | bit | No | - | - | boolean cov term field |
| BooleanTerm1Avl | bit | No | - | - | whether or not the BooleanTerm1 field was available the last time availability was checked |
| BooleanTerm2 | bit | No | - | - | boolean cov term field |
| BooleanTerm2Avl | bit | No | - | - | whether or not the BooleanTerm2 field was available the last time availability was checked |
| BooleanTerm3 | bit | No | - | - | boolean cov term field |
| BooleanTerm3Avl | bit | No | - | - | whether or not the BooleanTerm3 field was available the last time availability was checked |
| ChoiceTerm1 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm1Avl | bit | No | - | - | whether or not the ChoiceTerm1 field was available the last time availability was checked |
| ChoiceTerm2 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm2Avl | bit | No | - | - | whether or not the ChoiceTerm2 field was available the last time availability was checked |
| ChoiceTerm3 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm3Avl | bit | No | - | - | whether or not the ChoiceTerm3 field was available the last time availability was checked |
| ChoiceTerm4 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm4Avl | bit | No | - | - | whether or not the ChoiceTerm4 field was available the last time availability was checked |
| ChoiceTerm5 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm5Avl | bit | No | - | - | whether or not the ChoiceTerm5 field was available the last time availability was checked |
| DateTerm1 | datetime | No | - | - | datetime cov term field |
| DateTerm1Avl | bit | No | - | - | whether or not the DateTerm1 field was available the last time availability was checked |
| DateTerm2 | datetime | No | - | - | datetime cov term field |
| DateTerm2Avl | bit | No | - | - | whether or not the DateTerm2 field was available the last time availability was checked |
| DirectTerm1 | decimal | No | - | - | direct cov term field |
| DirectTerm1Avl | bit | No | - | - | whether or not the DirectTerm1 field was available the last time availability was checked |
| DirectTerm2 | decimal | No | - | - | direct cov term field |
| DirectTerm2Avl | bit | No | - | - | whether or not the DirectTerm2 field was available the last time availability was checked |
| DirectTerm3 | decimal | No | - | - | direct cov term field |
| DirectTerm3Avl | bit | No | - | - | whether or not the DirectTerm3 field was available the last time availability was checked |
| HOPLine | ForeignKey | Yes | HOPLine | - | Foreign key target: HOPLine |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| HOPLineCovCosts | HOPLineCovCost | Child collection |

---

### Entity: HOPCoveragePartCov

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPCoveragePartCov.eti`
**Entity Type:** `effdated`
**Database Table:** `hopcoveragepartcov`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Coverages directly attached to each HOPCoveragePart

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BooleanTerm1 | bit | No | - | - | boolean cov term field |
| BooleanTerm1Avl | bit | No | - | - | whether or not the BooleanTerm1 field was available the last time availability was checked |
| BooleanTerm2 | bit | No | - | - | boolean cov term field |
| BooleanTerm2Avl | bit | No | - | - | whether or not the BooleanTerm2 field was available the last time availability was checked |
| BooleanTerm3 | bit | No | - | - | boolean cov term field |
| BooleanTerm3Avl | bit | No | - | - | whether or not the BooleanTerm3 field was available the last time availability was checked |
| ChoiceTerm1 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm1Avl | bit | No | - | - | whether or not the ChoiceTerm1 field was available the last time availability was checked |
| ChoiceTerm2 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm2Avl | bit | No | - | - | whether or not the ChoiceTerm2 field was available the last time availability was checked |
| ChoiceTerm3 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm3Avl | bit | No | - | - | whether or not the ChoiceTerm3 field was available the last time availability was checked |
| ChoiceTerm4 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm4Avl | bit | No | - | - | whether or not the ChoiceTerm4 field was available the last time availability was checked |
| ChoiceTerm5 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm5Avl | bit | No | - | - | whether or not the ChoiceTerm5 field was available the last time availability was checked |
| DateTerm1 | datetime | No | - | - | datetime cov term field |
| DateTerm1Avl | bit | No | - | - | whether or not the DateTerm1 field was available the last time availability was checked |
| DateTerm2 | datetime | No | - | - | datetime cov term field |
| DateTerm2Avl | bit | No | - | - | whether or not the DateTerm2 field was available the last time availability was checked |
| DirectTerm1 | decimal | No | - | - | direct cov term field |
| DirectTerm1Avl | bit | No | - | - | whether or not the DirectTerm1 field was available the last time availability was checked |
| DirectTerm2 | decimal | No | - | - | direct cov term field |
| DirectTerm2Avl | bit | No | - | - | whether or not the DirectTerm2 field was available the last time availability was checked |
| DirectTerm3 | decimal | No | - | - | direct cov term field |
| DirectTerm3Avl | bit | No | - | - | whether or not the DirectTerm3 field was available the last time availability was checked |
| HOPCoveragePart | ForeignKey | Yes | HOPCoveragePart | - | Foreign key target: HOPCoveragePart |

---

### Entity: WorkersCompCov

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\WorkersCompCov.eti`
**Entity Type:** `effdated`
**Database Table:** `workerscompcov`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A line-level coverage for Workers' Comp

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| DirectTerm1 | decimal | No | - | - | direct cov term field |
| DirectTerm1Avl | bit | No | - | - | whether or not the DirectTerm1 field was available the last time availability was checked |
| DirectTerm2 | decimal | No | - | - | direct cov term field |
| DirectTerm2Avl | bit | No | - | - | whether or not the DirectTerm2 field was available the last time availability was checked |
| DirectTerm3 | decimal | No | - | - | direct cov term field |
| DirectTerm3Avl | bit | No | - | - | whether or not the DirectTerm3 field was available the last time availability was checked |
| StringTerm1 | shorttext | No | - | - | string cov term field |
| StringTerm1Avl | bit | No | - | - | whether or not the StringTerm1 field was available the last time availability was checked |
| StringTerm2 | shorttext | No | - | - | string cov term field |
| StringTerm2Avl | bit | No | - | - | whether or not the StringTerm2 field was available the last time availability was checked |
| StringTerm3 | shorttext | No | - | - | string cov term field |
| StringTerm3Avl | bit | No | - | - | whether or not the StringTerm3 field was available the last time availability was checked |
| ChoiceTerm1 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm1Avl | bit | No | - | - | whether or not the ChoiceTerm1 field was available the last time availability was checked |
| ChoiceTerm2 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm2Avl | bit | No | - | - | whether or not the ChoiceTerm2 field was available the last time availability was checked |
| ChoiceTerm3 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm3Avl | bit | No | - | - | whether or not the ChoiceTerm3 field was available the last time availability was checked |
| ChoiceTerm4 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm4Avl | bit | No | - | - | whether or not the ChoiceTerm4 field was available the last time availability was checked |
| FedEmpLiabLawTerm1 | patterncode | No | - | - | choice cov term field |
| FedEmpLiabLawTerm1Avl | bit | No | - | - | whether or not the FedEmpLiabLawTerm1 field was available the last time availability was checked |
| WCLine | ForeignKey | No | WorkersCompLine | - | Foreign key target: WorkersCompLine |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Costs | WCCovEmpCost | Child collection |

---

### Entity: ETLCoverageTermPattern

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\ETLCoverageTermPattern.eti`
**Entity Type:** `versionable`
**Database Table:** `etlcovtermpattern`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Code | varchar | Yes | - | - | The Code for the Coverage Term Pattern |
| ColumnName | varchar | Yes | - | - | The column 'Coverage' table that is populated with the Coverage Term Pattern PublicID |
| Name | varchar | Yes | - | - | The Name for the Coverage Term Pattern |
| ModelType | varchar | No | - | - | The Model Type for the pattern. Should Correspond to the ModelType typelist |
| CovTermType | varchar | Yes | - | - | The type of the covTerm |
| PatternID | varchar | Yes | - | - | The Public ID of the source coverage term pattern in the product model |
| CodeIdentifier | varchar | No | - | - | The CodeIdentifier (human readable) of the source coverage term pattern in the product model |
| ClausePattern | ForeignKey | Yes | ETLClausePattern | - | the foreign key to the Clause Pattern for this option |

---

### Entity: CoverageLookup

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\CoverageLookup.eti`
**Entity Type:** `retireable`
**Database Table:** `covlookup`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** An availability lookup for coverage patterns.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| CoveragePatternCode | patterncode | Yes | - | - | - |

---

### Entity: Job

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Job.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\Job.etx`
**Entity Type:** `retireable`
**Database Table:** `job`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Workflow process object relating to one or more versions of a policy

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| CloseDate | datetime | No | - | - | Date and time when this job was closed. |
| Description | mediumtext | No | - | - | Extended description of this job which may include the reason this job was started. |
| JobNumber | varchar | Yes | - | - | The unique identifier for this job. |
| NextPurgeCheckDate | dateonly | No | - | - | The date to next evaluate this Job for purging. If null, purging should be checked at the next opportunity |
| PrimaryInsuredName | shorttext | No | - | - | The display name of the primary names insured (denormalization). |
| SideBySide | bit | Yes | - | - | Default: false True if Side By Side Quoting has been set up for this job. |
| Policy | ForeignKey | Yes | Policy | - | The Policy this Job applies to. |
| PolicyTerm | ForeignKey | Yes | PolicyTerm | - | Foreign key target: PolicyTerm |
| JobGroup | ForeignKey | No | JobGroup | - | The group to which this job belongs. |
| SelectedVersion | ForeignKey | No | PolicyPeriod | - | The selected branch attached to this job. For a single-quote job this will be the only branch, while for a multi-quote job this will be one of the branches that is selected (either explicitly by a user or implicitly by the job behavior). |
| PurgeStatus | TypeKey | Yes | - | PurgeStatus | Default: Unknown Purge status of the job. Codes: [Unknown, NoActionRequired, Pruned] |
| ContingencyInitiator | OneToOne | No | ContingencyJob | - | One-to-one link |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| RoleAssignments | JobUserRoleAssignment | Role Assignments for this job. |
| Periods | PolicyPeriod | Set of PolicyPeriods associated with this job. |
| Notes | Note | Notes associated with this Job. |
| UpFrontPayments | UpFrontPayment | Child collection |

---

### Entity: Submission

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Submission.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\Submission.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** Job
**Effective-Dated Container Branch Field:** N/A
**Description:** Submission process object relating to one or more versions of a policy

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| DateQuoteNeeded | datetime | No | - | - | Date a quote for this submission is needed |
| RejectReasonText | longtext | No | - | - | Text of the letter. |
| SubmissionDate | datetime | Yes | - | - | Date this submission was entered |
| RejectReason | TypeKey | No | - | ReasonCode | The reason that this job was rejected Codes (33 total): [nonpayment, fraud, flatrewrite, midtermrewrite, unresolvedcontingency, ...] |
| BindOption | TypeKey | No | - | BindOption | Default: BindAndIssue Indicates how this submision was bound Codes: [BindOnly, BindAndIssue] |
| QuoteType | TypeKey | Yes | - | QuoteType | What kind of quote is the submission for Codes: [Quick, Full] |

---

### Entity: Issuance

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Issuance.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\Issuance.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** Job
**Effective-Dated Container Branch Field:** N/A
**Description:** Issuance process object relating to one or more versions of a policy

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: PolicyChange

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyChange.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\PolicyChange.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** Job
**Effective-Dated Container Branch Field:** N/A
**Description:** Policy change process

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: Renewal

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Renewal.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\Renewal.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** Job
**Effective-Dated Container Branch Field:** N/A
**Description:** Renewal process

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| RenewalNotifDate | datetime | No | - | - | Date a renewal notification was sent |
| NonRenewalNotifDate | datetime | No | - | - | Date a non-renewal notification was sent |
| NotTakenNotifDate | datetime | No | - | - | Date a not-taken notification was sent |
| EscalateAfterHoldReleased | bit | No | - | - | Default: false Indicates whether a renewal job should be escalated if a policy hold no longer affects it.  If true, creates an activity for the producer to re-examine the renewal. If false, the previously-held renewal is dropped back into automated processing. |
| RenewalCode | TypeKey | No | - | RenewalCode | Renewal reason codes Codes: [goodrisk, assignedrisk, accountfavor, producerfavor, requiredbylaw] |
| NonRenewalCode | TypeKey | No | - | NonRenewalCode | NonRenewal reason codes Codes (8 total): [loss, producertermination, outofbusness, payhistory, change, ...] |

---

### Entity: Cancellation

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Cancellation.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\Cancellation.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** Job
**Effective-Dated Container Branch Field:** N/A
**Description:** Cancellation process

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| CancelProcessDate | datetime | No | - | - | Date the cancellation should be processed by the external system |
| LastNotifiedCancellationDate | datetime | No | - | - | Date of the last time that a cancellation notification was sent to an external system in response to this job. |
| InitialNotificationDate | datetime | No | - | - | Date of the first time that a cancellation notification was sent to an external system in response to this job |
| NotificationAckDate | datetime | No | - | - | Date a cancellation notification acknowledgement was received from an external system |
| NotificationDate | datetime | No | - | - | Date a cancellation notification was sent to an external system |
| RescindNotificationDate | datetime | No | - | - | Date a rescind cancellation notification was sent |
| QuoteOnStart | bit | Yes | - | - | Default: True True if this Cancellation job will be quoted after it's started. |
| CancelReasonCode | TypeKey | No | - | ReasonCode | Cancellation reason codes Codes (33 total): [nonpayment, fraud, flatrewrite, midtermrewrite, unresolvedcontingency, ...] |
| Source | TypeKey | Yes | - | CancellationSource | Party that initiated cancellation (carrier or insures) Codes: [carrier, insured] |

---

### Entity: Reinstatement

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Reinstatement.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\Reinstatement.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** Job
**Effective-Dated Container Branch Field:** N/A
**Description:** Reinstatement process

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| ReinstateCode | TypeKey | No | - | ReinstateCode | Reinstate reason codes Codes: [payment, other] |

---

### Entity: Rewrite

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Rewrite.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\Rewrite.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** Job
**Effective-Dated Container Branch Field:** N/A
**Description:** Rewrite process

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| ChangePolicyNumber | bit | Yes | - | - | Default: false Whether or not a new policy number should be generated for the rewritten policy upon issuance |
| RewriteType | TypeKey | No | - | RewriteType | Type of rewrite Codes: [RewriteFullTerm, RewriteRemainderOfTerm, RewriteNewTerm] |

---

### Entity: RewriteNewAccount

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\RewriteNewAccount.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\RewriteNewAccount.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** Job
**Effective-Dated Container Branch Field:** N/A
**Description:** RewriteNewAccount process

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: Audit

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Audit.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\Audit.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** Job
**Effective-Dated Container Branch Field:** N/A
**Description:** Audit process

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| AuditInformation | ForeignKey | Yes | AuditInformation | - | The audit information pertaining to this audit job |
| PaymentReceived | monetaryamount | No | - | - | The amount of any payment received, e.g. deposit when binding, or payment with premium report |

---

### Entity: PolicyContactRole

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyContactRole.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\PolicyContactRole.etx`
**Entity Type:** `effdated`
**Database Table:** `policycontactrole`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A role that a contact plays within a policy period.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| SeqNumber | integer | No | - | - | The contact sequence number |
| CompanyNameInternal | companyname | No | - | - | Internal field for sharing and revisioning the role's company name. |
| FirstNameInternal | firstname | No | - | - | Internal field for sharing and revisioning the role's first name. |
| LastNameInternal | lastname | No | - | - | Internal field for sharing and revisioning the role's last name. |
| DateOfBirthInternal | datetime | No | - | - | Internal field for sharing and revisioning the date of birth. |
| AccountContactRole | ForeignKey | No | AccountContactRole | - | The account contact role this policy contact role may be synced with.  While the policy contact role contains policy contract information, the account contact role contains shared role information. |
| ContactDenorm | ForeignKey | No | Contact | - | The PolicyContactRole.AccountContactRole.AccountContact.Contact (denormalization). |
| MaritalStatusInternal | TypeKey | No | - | MaritalStatus | Internal field for sharing and revisioning the marital status. Codes (7 total): [C, D, M, P, S, ...] |
| CompanyNameKanjiInternal_Ext | companyname | No | - | - | [Extension] Internal field for sharing and revisioning the role's company name in Kanji.  Used only for Japanese names and will be null otherwise. |
| FirstNameKanjiInternal_Ext | firstname | No | - | - | [Extension] Internal field for sharing and revisioning the role's first name in Kanji.  Used only for Japanese names and will be null otherwise. |
| LastNameKanjiInternal_Ext | lastname | No | - | - | [Extension] Internal field for sharing and revisioning the role's last name in Kanji.  Used only for Japanese names and will be null otherwise. |
| ParticleInternal_Ext | shorttext | No | - | - | [Extension] Particle for (French) name |

---

### Entity: PolicyPriNamedInsured

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyPriNamedInsured.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PolicyNamedInsured
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: PolicyAddlInsured

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyAddlInsured.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PolicyContactRole
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| PolicyLine | ForeignKey | No | PolicyLine | - | The policy line this policy additional insured role is associated with. |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| PolicyAdditionalInsuredDetails | PolicyAddlInsuredDetail | Child collection |

---

### Entity: PolicyBillingContact

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyBillingContact.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PolicyContactRole
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: Cost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Cost.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Basis | ratinglinebasisamount | Yes | - | - | Default: 0 The basis for the cost over the rated term.  The basis type itself may vary (e.g. units of risk, units of money, etc.) |
| ActualAdjRate | rate | Yes | - | - | Default: 1 The adjusted rate (after mod factors are applied) for the cost over the rated term. |
| StandardAdjRate | rate | No | - | - | The adjusted rate (after mod factors are applied) for the cost over the rated term, as calculated based on the standard base rate. |
| OverrideAdjRate | rate | No | - | - | The user-specified override for the adjusted rate. |
| ActualBaseRate | rate | Yes | - | - | Default: 1 The base rate (before mod factors are applied) for the cost over the rated term. |
| StandardBaseRate | rate | No | - | - | The standard base rate (before mod factors are applied) for the cost over the rated term. |
| OverrideBaseRate | rate | No | - | - | The user-specified override for the base rate. |
| OverrideReason | shorttext | No | - | - | Why the override is being applied. |
| NumDaysInRatedTerm | positiveinteger | Yes | - | - | The number of days in the term period used to arrive at the rate. |
| Overridable | bit | Yes | - | - | Default: true Indicates whether this cost can have an override applied; most likely set by the rating engine. |
| SubjectToReporting | bit | Yes | - | - | Default: false Indicates whether this cost is subject to reporting.  If a cost is subject to reporting and a policy has a reporting plan, that cost will only generate charged transactions during report jobs and final audit. |
| ChargeGroup | shorttext | No | - | - | Custom group name to group charges together |
| FXRateConversionUsed | bit | Yes | - | - | Default: false Flags when the PolicyFXRate is used to convert amounts from coverage currency to settlement currency |
| RoundingLevel | integer | No | - | - | Number of decimal places to which this cost should be rounded when prorated |
| BillGroup | shorttext | No | - | - | Custom grouping for costs itemised for billing but collected as one charge |
| RateBook | ForeignKey | No | RateBook | - | Foreign key target: RateBook |
| PolicyFXRate | ForeignKey | No | PolicyFXRate | - | Foreign key target: PolicyFXRate |
| CostCode | ForeignKey | No | CostCode | - | Foreign key target: CostCode |
| RateAmountType | TypeKey | Yes | - | RateAmountType | Default: StdPremium Tax/surcharge, a standard premium, or a non-standard premium Codes: [StdPremium, NonstdPremium, TaxSurcharge] |
| ChargePattern | TypeKey | No | - | ChargePattern | Default: Premium The type of charge (Premium, Taxes, Fee) Codes: [Premium, Taxes, InstallmentFee, ReinstatementFee, PremiumIncludingTaxes] |
| RoundingMode | TypeKey | No | - | RoundingModeType | Rounding mode (e.g. HALF_UP) to be used when prorating Codes (8 total): [UP, DOWN, CEILING, FLOOR, HALF_UP, ...] |
| ProrationMethod | TypeKey | No | - | ProrationMethod | Default: ProRataByDays Procedure used to derive Amount from Term Amount, e.g. day-based pro-rata, or flat Codes: [ProRataByDays, Flat] |
| OverrideSource | TypeKey | Yes | - | OverrideSourceType | Default: manual Source of override, or null if none Codes: [manual, renewalcap] |
| ActualAmount | monetaryamount | Yes | - | - | The current amount for the effDated effective period. |
| ActualAmountBilling | monetaryamount | Yes | - | - | The current amount converted to the settlement currency for the effDated effective period. |
| StandardAmount | monetaryamount | No | - | - | The current amount for the effDated effective period, as calculated based on the standard rates. |
| StandardAmountBilling | monetaryamount | No | - | - | The current amount for the effDated effective period, as calculated based on the standard rates. |
| OverrideAmount | monetaryamount | No | - | - | The user-specified override for the amount. |
| OverrideAmountBilling | monetaryamount | No | - | - | The user-specified override converted to settlement currency for the amount. |
| ActualTermAmount | monetaryamount | Yes | - | - | The cost over an rated term. |
| ActualTermAmountBilling | monetaryamount | Yes | - | - | The cost converted to settlement currency over an rated term. |
| StandardTermAmount | monetaryamount | No | - | - | The cost over an rated term, as calculated based on the standard rates. |
| StandardTermAmountBilling | monetaryamount | No | - | - | The cost over an rated term converted to settlement currency, as calculated based on the standard rates. |
| OverrideTermAmount | monetaryamount | No | - | - | The user-specified override for the term amount. |
| OverrideTermAmountBilling | monetaryamount | No | - | - | The user-specified override converted to settlement currency for the term amount. |

---

### Entity: PACost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PACost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\PACost.etx`
**Entity Type:** `effdated`
**Database Table:** `pacost`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A PersonalAuto unit of price for a period of time that should not be broken up any further.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| PersonalAutoLine | ForeignKey | Yes | PersonalAutoLine | - | Foreign key target: PersonalAutoLine |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Transactions | PATransaction | Child collection |

---

### Entity: BACost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BACost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\BACost.etx`
**Entity Type:** `effdated`
**Database Table:** `bacost`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A Commercial Auto unit of price for a period of time that should not be broken up any further.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BusinessAutoLine | ForeignKey | Yes | BusinessAutoLine | - | Foreign key target: BusinessAutoLine |
| BusinessVehicle | ForeignKey | No | BusinessVehicle | - | The Business Vehicle related to the this Cost |
| Jurisdiction | ForeignKey | No | BAJurisdiction | - | The Jurisdiction related to the this Cost |
| RatedOrder | TypeKey | Yes | - | BARatedOrderType | The order in which this cost was rated. Codes: [CoveragePremium, CancelShortRatePenalty, MinimumPremium, StateTax] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Transactions | BATransaction | Child collection |

---

### Entity: BOPCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BOPCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\BOPCost.etx`
**Entity Type:** `effdated`
**Database Table:** `bopcost`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A BusinessOwners unit of price for a period of time, not to be broken up any further

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BusinessOwnersLine | ForeignKey | Yes | BusinessOwnersLine | - | Foreign key target: BusinessOwnersLine |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Transactions | BOPTransaction | Child collection |

---

### Entity: GLCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\GLCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\GLCost.etx`
**Entity Type:** `effdated`
**Database Table:** `glcost`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A GeneralLiability unit of price for a period of time that should not be broken up any further.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| GeneralLiabilityLine | ForeignKey | Yes | GeneralLiabilityLine | - | Foreign key target: GeneralLiabilityLine |
| SplitType | TypeKey | No | - | GLCostSplitType | The liability limit split type associated with this cost Codes: [BI, PD, CSL] |
| Subline | TypeKey | No | - | GLCostSubline | The subline associated with this cost Codes: [Premises, Products] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Transactions | GLTransaction | Child collection |

---

### Entity: HOPCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\HOPCost.etx`
**Entity Type:** `effdated`
**Database Table:** `hopcost`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A unit of premium or other cost (taxes, fees, etc.) for the Homeowners line.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| HOPLine | ForeignKey | Yes | HOPLine | - | Foreign key target: HOPLine |
| HOPPremiumType | TypeKey | Yes | - | HOPPremiumType | Premium type for Homeowners Codes: [basepremium, adjustmenttobasepremium, otherpremium] |
| Modification | TypeKey | No | - | Modification | Is this cost row a basic premium or a modification premium ? Codes: [modification, base] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Transactions | HOPTransaction | Child collection |

---

### Entity: Transaction

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Transaction.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| EffDate | dateonly | Yes | - | - | The date on which the transaction becomes effective. |
| ExpDate | dateonly | Yes | - | - | The date on which the transaction expires. |
| Written | bit | Yes | - | - | Default: true Whether or not this transaction amount should be counted in written premium calculations. |
| Charged | bit | Yes | - | - | Default: true Whether or not this transaction amount should be charged. |
| ToBeAccrued | bit | Yes | - | - | Default: true Whether or not this transaction amount should be included in earned premium accrual calculations. |
| PostedDate | datetime | No | - | - | The date on which the transaction was posted.  For transactions that haven't yet been posted, this field will be null.  Otherwise, it will be equal to the date on which the job was bound or (in the case of audits) completed. |
| WrittenDate | dateonly | No | - | - | The date on which (for accounting purposes) the premium is considered as written. |
| PolicyFXRate | ForeignKey | No | PolicyFXRate | - | Foreign key target: PolicyFXRate |
| Amount | monetaryamount | Yes | - | - | The transaction amount for the effective time [EffDate, ExpDate). |
| AmountBilling | monetaryamount | Yes | - | - | The transaction amount for the effective time [EffDate, ExpDate). |

---

### Entity: PATransaction

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PATransaction.eti`
**Entity Type:** `effdated`
**Database Table:** `patransaction`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A transaction for the Personal Auto line

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| PACost | ForeignKey | Yes | PACost | - | Foreign key target: PACost |

---

### Entity: BATransaction

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BATransaction.eti`
**Entity Type:** `effdated`
**Database Table:** `batransaction`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A transaction for the Commercial Auto line

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BACost | ForeignKey | Yes | BACost | - | The cost this transaction modifies. |

---

### Entity: PaymentPlanSummary

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PaymentPlanSummary.eti`
**Entity Type:** `retireable`
**Database Table:** `paymentplansummary`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Payment plan summary info from billing system

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| BillingId | shorttext | No | - | - | Stores the billing system's Public ID for this Payment Plan |
| Name | shorttext | No | - | - | Name of this payment plan (only for Installments plans) |
| Notes | shorttext | No | - | - | Notes |
| ReportingPatternCode | patterncode | No | - | - | The code of the pattern to use for creating and scheduling premium reports |
| PolicyPeriod | ForeignKey | No | PolicyPeriod | - | Policy period where the plan summary resides |
| InvoiceFrequency | TypeKey | Yes | - | BillingPeriodicity | Default: monthly The frequency of invoicing (weekly, every two weeks, monthly, etc.) Codes (10 total): [monthly, everyweek, everyotherweek, twicepermonth, everyothermonth, ...] |
| PaymentPlanType | TypeKey | Yes | - | PaymentMethod | Default: Installments The type of this payment plan (typically either Installments or Reporting) Codes: [Installments, ReportingPlan] |
| BillDateOrDueDateBilling | TypeKey | No | - | BillDateOrDueDateBilling | Codes: [BillDateBilling, DueDateBilling] |
| DownPayment | monetaryamount | No | - | - | DownPayment |
| Fee | monetaryamount | No | - | - | The installment fee charged as part of this payment plan with respect to the parent PolicyPeriod. |
| Installment | monetaryamount | No | - | - | Installment |
| TotalFees | monetaryamount | No | - | - | The total fees charged as part of this payment plan with respect to the parent PolicyPeriod. |
| Total | monetaryamount | No | - | - | Total |
| Tax | monetaryamount | No | - | - | Tax charged as part of this payment plan with respect to the parent PolicyPeriod. |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| PaymentMethodsInternal | AllowedPaymentMethod | The list of supported payment methods. |

---

### Entity: ProducerCode

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\ProducerCode.eti`
**Entity Type:** `retireable`
**Database Table:** `producercode`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Identifies producer and underwriting assignment preferences.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Code | shorttext | Yes | - | - | The producer code. |
| Description | shorttext | No | - | - | The producer code description. |
| AppointmentDate | datetime | No | - | - | Indicates when the carrier's relationship with the producer began. |
| TerminationDate | datetime | No | - | - | Indicates when the producer relationship was or will be terminated. |
| AddressPublicID | publicid | No | - | - | - |
| Address | ForeignKey | No | Address | - | The contact for this producer code. |
| Branch | ForeignKey | No | Group | - | The internal (carrier) branch that handles the business for this producer code. |
| PreferredUnderwriter | ForeignKey | No | User | - | The preferred underwriter for a producer code |
| Organization | ForeignKey | Yes | Organization | - | The Organization this producer code belongs to. |
| Parent | ForeignKey | No | ProducerCode | - | The producer code's parent producer code. |
| ProducerStatus | TypeKey | Yes | - | ProducerStatus | Default: Active The status of this producer code. Codes: [Active, Limited, Suspended, Terminating, Terminated] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| GroupProducerCodes | GroupProducerCode | Available producer codes to an external producer group. |
| UserProducerCodes | UserProducerCode | Available producer codes and associated roles to a user. |
| ProducerCodeRoles | ProducerCodeRole | Available roles to a producer code. |
| CommissionPlans | CommissionPlan | Currencies allowed to be used by the producer code as billing currency. |
| AffinityGroupProducerCodes | AffinityGroupProducerCode | Available groups to a producer code. |

---

### Entity: Organization

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Organization.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\Organization.etx`
**Entity Type:** `retireable`
**Database Table:** `organization`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Defines an organization that has a hierarchy of groups

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Carrier | bit | Yes | - | - | Default: false Flag indicating whether this organization corresponds to the carrier itself. |
| MasterAdmin | bit | Yes | - | - | Default: false Flag indicating whether this organization is the superuser organization with admin powers over all organizations. |
| Name | varchar | Yes | - | - | The name of the organization. |
| Contact | ForeignKey | No | Contact | - | Contact entry related to the organization. |
| RootGroup | ForeignKey | Yes | Group | - | The organization's root group. |
| Type | TypeKey | No | - | BusinessType | The type of the organization. Codes: [insurer, agency, broker, mga, feeaudit, feeinspect] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| ZonesToAdmin | OrganizationZoneAdmin | Link to joiner table for zones to admin. |

---

### Entity: User

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\User.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\User.etx`
**Entity Type:** `retireable`
**Database Table:** `user`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Internal system users.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| ExternalUser | bit | Yes | - | - | Default: false If true, the user is an external user, and claims assigned to the user should be treated as externally owned. |
| JobTitle | shorttext | No | - | - | User's job title. |
| Department | shorttext | No | - | - | User's department within the company. |
| SessionTimeoutSecs | integer | No | - | - | User's session timeout value in seconds |
| Contact | ForeignKey | Yes | UserContact | - | Contact entry related to the user. |
| Credential | ForeignKey | Yes | Credential | - | Security credential for the user. |
| UserSettings | ForeignKey | No | UserSettings | - | Settings for this user (formerly known as preferences). |
| Organization | ForeignKey | No | Organization | - | Each user should belong to exactly one organization |
| Language | TypeKey | No | - | LanguageType | User's preferred language. Codes: [de, en_US, es, fr, ja] |
| Locale | TypeKey | No | - | LocaleType | User's preferred locale. Codes (8 total): [en_US, en_GB, en_CA, en_AU, fr_CA, ...] |
| DefaultCountry | TypeKey | No | - | Country | User's default country Codes (243 total): [unknown, AF, AL, DZ, AS, ...] |
| DefaultPhoneCountry | TypeKey | No | - | PhoneCountryCode | User's default phone country Codes (245 total): [AC, AD, AE, AF, AG, ...] |
| TimeZone | TypeKey | No | - | TimeZoneType | User's time zone. Codes (9 total): [US.Eastern, US.East-Indiana, US.Central, US.Mountain, US.Arizona, ...] |
| ExperienceLevel | TypeKey | No | - | UserExperienceType | Experience level of the user. Codes: [low, mid, high] |
| SystemUserType | TypeKey | No | - | SystemUserType | Indicates the type of special system users (for example, default claim owner). This is null for regular users. Codes: [sysadmin, defaultowner, sysservices] |
| VacationStatus | TypeKey | Yes | - | VacationStatusType | Default: atwork The vacation status of this user. Codes: [atwork, onvacation, inactive] |
| ValidationLevel | TypeKey | No | - | ValidationLevel | Validation level that this object passed (if any) before it was stored. Codes: [loadsave, default, quotable, bindable, readyforissue, quickquotable] |
| UserUIPreferences | OneToOne | No | UserUIPreferences | - | One-to-one link |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Attributes | AttributeUser | Attributes for the user. |
| Roles | UserRole | Security roles granted to the user. |
| BackupUsers | UserBackup | Backup users for this user. Though this is an array, users can only have one backup user. |
| Regions | UserRegion | Regions associated with this user. |
| GroupUsers | GroupUser | Groups associated with this user. |

---

### Entity: Group

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Group.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\Group.etx`
**Entity Type:** `retireable`
**Database Table:** `group`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Groups of users.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Name | varchar | Yes | - | - | The group name; this must be unique. |
| WorldVisible | bit | Yes | - | - | Default: true If true, this group is visible to all users, regardless of what groups they belong to. |
| LoadFactor | integer | No | - | - | Default: 100 Percentage value of normal workload to be given to this group. This is used for round-robin assignment. |
| Parent | ForeignKey | No | Group | - | The group's parent group. |
| Organization | ForeignKey | No | Organization | - | The Organization that this group belongs to. |
| Supervisor | ForeignKey | No | User | - | Supervisor of the group. |
| SecurityZone | ForeignKey | Yes | SecurityZone | - | Security zone to which the group belongs. |
| VisibilityZone | ForeignKey | No | Group | - | Group that defines the visibility zone for this group. A visibility zone is defined by a direct child of the root group. The visibility zone of the root group will always be null. |
| GroupType | TypeKey | Yes | - | GroupType | Type of group (describes its function). Codes (32 total): [root, actuary, branch, branchaudit, branchlc, ...] |
| ValidationLevel | TypeKey | No | - | ValidationLevel | Validation level that this object passed (if any) before it was stored. Codes: [loadsave, default, quotable, bindable, readyforissue, quickquotable] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Users | GroupUser | Users belonging to this group. |
| Regions | GroupRegion | Regions associated with this group. |
| AssignableQueues | AssignableQueue | Assignment queues associated with this group. |

---

### Entity: Activity

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Activity.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\Activity.etx`
**Entity Type:** `retireable`
**Database Table:** `activity`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** An activity is a instance of work assigned to a user and belonging to a claim.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Approved | bit | No | - | - | Whether the activity is approved. This is null if not relevant or undecided. |
| AutoGenerated | bit | Yes | - | - | Default: false True if the activity was generated automatically; never fully implemented. Instead, customers can create an extension field and set it after creating an activity in a rule to indicate how the activity was created |
| Description | mediumtext | No | - | - | Description of the activity. |
| EndDate | datetime | No | - | - | Time the event is scheduled to terminate or null if the activity is not a scheduled event. |
| EscalationDate | datetime | No | - | - | When the activity will be escalated if it isn't yet completed; this is null if the activity is never escalated. |
| Escalated | bit | Yes | - | - | Default: false True if the activity has been escalated. |
| ExternallyOwned | bit | Yes | - | - | Default: false Whether the activity is externally owned. |
| TargetDate | datetime | No | - | - | If this activity is a task, time by which a person should complete the task; if not completed by this time, the task is considered overdue. If this activity is an event, the time the event is scheduled to start. |
| Command | mediumtext | No | - | - | A Gosu command to execute for this activity. |
| DocumentTemplate | shorttext | No | - | - | The id of an associated document template. The id and language gets passed to IDocumentTemplateSource to retrieve the DocumentTemplateDescriptor. This property should not be used by applications. |
| EmailTemplate | shorttext | No | - | - | The id of an associated email template. The id gets passed to IEmailTemplateSource to retrieve the EmailTemplateDescriptor. |
| Mandatory | bit | Yes | - | - | Default: false True if the activity must be completed and cannot be skipped. |
| Recurring | bit | Yes | - | - | Default: false Whether this activity is recurring. |
| Subject | shorttext | No | - | - | A brief title for the activity; this is associated with its pattern. |
| ShortSubject | varchar | No | - | - | A very brief title for the activity e.g., displayable in a calendar; this is associated with its pattern. |
| LastViewedDate | datetime | No | - | - | When this activity was last viewed by the assignee. If never viewed, this is null. |
| ApprovalRationale | shorttext | No | - | - | Rationale for approving/rejecting the activity. This field should only be set for approval activities. |
| ApprovalIssue | shorttext | No | - | - | Reason approval is needed. This field should only be set for approval activities. |
| LogicalName | shorttext | No | - | - | Logical name of the activity.  Used by the internal workflow engine. |
| ActivityPattern | ForeignKey | No | ActivityPattern | - | Pattern that created this activity. If it was not created from a pattern, then this is null. |
| CloseUser | ForeignKey | No | User | - | The user who closed this activity. |
| Workflow | ForeignKey | No | Workflow | - | Optional pointer to the workflow this activity is associated with. |
| RelatedActivity | ForeignKey | No | Activity | - | For assignment review activities, points to the activity to be assigned.  Otherwise, this is null. |
| ActivityClass | TypeKey | Yes | - | ActivityClass | Default: task The class of the activity. Codes: [task, event] |
| Priority | TypeKey | Yes | - | Priority | Priority of the activity with respect to other activities. Codes: [urgent, high, normal, low] |
| Status | TypeKey | Yes | - | ActivityStatus | Default: open Status of the activity. Codes: [open, skipped, complete, canceled] |
| Type | TypeKey | Yes | - | ActivityType | Default: general Type of the activity. Codes: [general, approval, assignmentreview, approvaldenied] |
| ValidationLevel | TypeKey | No | - | ValidationLevel | Validation level that this object passed (if any) before it was stored. Codes: [loadsave, default, quotable, bindable, readyforissue, quickquotable] |

---

### Entity: Note

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Note.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\Note.etx`
**Entity Type:** `retireable`
**Database Table:** `note`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Notes added by users

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Body | longtext | No | - | - | Body of the note. |
| Confidential | bit | Yes | - | - | Default: false Whether the note is confidential. |
| Subject | shorttext | No | - | - | Subject or summary of the note. |
| AuthoringDate | datetime | No | - | - | Date on which the note was originally authored.  If null, the CreateTime seves this purpose. |
| Activity | ForeignKey | No | Activity | - | The activity associated with the note. |
| Author | ForeignKey | No | User | - | User who wrote the note. |
| Topic | TypeKey | No | - | notetopictype | Default: general Topic to which the note belongs. Codes (12 total): [general, risk, coverage, gaps, losscontrol, ...] |
| SecurityType | TypeKey | No | - | NoteSecurityType | Type of note; used for access-restriction purposes |
| Language | TypeKey | No | - | LanguageType | The language in which this note is created. Codes: [de, en_US, es, fr, ja] |

---

### Entity: Document

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Document.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\Document.etx`
**Entity Type:** `retireable`
**Database Table:** `document`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Internal representation of a physical or electronic document.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| DocUID | varchar | No | - | - | The Unique Identifier (UID) for this document.     The format of this UID is specific to the deployed Document Management System (DMS), and is passed to the configured IDocumentContentSource implementation. |
| DMS | bit | No | - | - | Whether this document has content stored in a Document Management System. |
| Name | varchar | No | - | - | Human-readable name of the document. |
| MimeType | varchar | No | - | - | The MIME type of this document; for example, application/msword for a Microsoft Word document. |
| Inbound | bit | No | - | - | Whether the document is an inbound, outbound, or stationary (null) document |
| Description | shorttext | No | - | - | Description of the document. |
| DateModified | datetime | No | - | - | Date and time the document was last modified. |
| DateCreated | datetime | No | - | - | Date and time the document was created. |
| Author | varchar | No | - | - | Name of the person who created the document. |
| Recipient | varchar | No | - | - | Name of the intended recipient of the document (if any). |
| DocumentIdentifier | varchar | No | - | - | Short human-readable identifier for the document, often used as an extra storage location for form codes, when name and documenttype are inadequate. |
| Obsolete | bit | No | - | - | Default: false If true, the information in the document can no longer be relied upon to be up-to-date and relevant. This is often used instead of deletion to preserve history. |
| PendingDocUID | varchar | No | - | - | The document is pending, and it's pending storage has Unique Identifier (UID).     The format of this UID is specific to the IDCS implementation. |
| Status | TypeKey | No | - | documentstatustype | The current status of the document, if any. Codes: [draft, approving, approved, final, filed] |
| Section | TypeKey | No | - | documentsection | The section to which this document belongs, if any. Codes (7 total): [bills, medical, indemnity, rehab, legal, ...] |
| SecurityType | TypeKey | No | - | documentsecuritytype | Type of document used for access-restriction purposes, in conjunction with the information in security-config.xml. Codes: [unrestricted, internalonly, sensitive] |
| Type | TypeKey | No | - | documenttype | The specific type of the document, if any. Codes (22 total): [diagram, email, email_sent, inspectionreport, newbusiness, ...] |
| Language | TypeKey | No | - | LanguageType | The language in which this document is created. Codes: [de, en_US, es, fr, ja] |

---

### Entity: UWIssue

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\UWIssue.eti`
**Entity Type:** `effdated`
**Database Table:** `uwissue`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A UWIssue is a raised issue of business concern.  It can be created at any point in the lifetime of a PolicyPeriod.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| ShortDescription | shorttext | No | - | - | The short description of this issue. |
| LongDescription | mediumtext | No | - | - | The long description of this issue. |
| Active | bit | Yes | - | - | Default: true Whether or not this issue is active.  An issue will be marked inactive if it no longer applies to the policy but we want to keep approvals for the issue around in case the issue occurs again. |
| HasApprovalOrRejection | bit | Yes | - | - | Default: false If true then approval this issue has an associated approval. |
| ApprovalValue | shorttext | No | - | - | The limit value to which the issue has been approved |
| AutomaticApprovalCause | shorttext | No | - | - | The operation in progress when automatic approvals were created for auto-approvable issues. Null is used to indicate a human-generated approval. |
| CanEditApprovalBeforeBind | bit | Yes | - | - | Default: true If true then approval still valid with poilcy edits before bind |
| ApprovalInvalidFrom | datetime | No | - | - | The date on which the approval ceases to be valid. This value is null except when DurationType is 1yr or 3yrs. |
| ApprovingUser | ForeignKey | No | User | - | Foreign key target: User |
| ApprovalBlockingPoint | TypeKey | No | - | UWIssueBlockingPoint | The point at which this approval still blocks Codes (7 total): [Rejected, BlocksQuote, BlocksRateRelease, BlocksQuoteRelease, BlocksBind, ...] |
| ApprovalDurationType | TypeKey | No | - | UWApprovalDurationType | A typekey specifying how long the approval is valid; if 1yr or 3yr, then an expiration date is computed. Codes: [NextChange, EndOfTerm, OneYear, ThreeYears, Rescinded] |

---

### Entity: UWReferralReason

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\UWReferralReason.eti`
**Entity Type:** `retireable`
**Database Table:** `uwreferralreason`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A referral reason for a given policy

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| ShortDescription | shorttext | No | - | - | The short description of this issue. |
| LongDescription | mediumtext | No | - | - | The long description of this issue. |
| Policy | ForeignKey | Yes | Policy | - | The policy for which this referral reason applies |
| Status | TypeKey | Yes | - | UWReferralReasonStatus | Default: Open Whether this referral reason is open or closed. Codes: [Open, Closed] |

---

### Entity: PCAnswerDelegate

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PCAnswerDelegate.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| QuestionCode | patterncode | Yes | - | - | Question that this answer answers |
| BooleanAnswer | bit | No | - | - | Yes / no component of answer. |
| DateAnswer | datetime | No | - | - | The answer in date form. |
| TextAnswer | mediumtext | No | - | - | Either the answer's text. |
| IntegerAnswer | integer | No | - | - | Numeric component of answer. |
| ChoiceAnswerCode | patterncode | No | - | - | Choice of the answer. |

---

### Entity: PeriodAnswer

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PeriodAnswer.eti`
**Entity Type:** `effdated`
**Database Table:** `periodanswer`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Links policy period and answer references - answers are persisted text responses to questions in the UI. Specific to PolicyCenter.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |

---

### Entity: PolicyLineAnswer

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyLineAnswer.eti`
**Entity Type:** `effdated`
**Database Table:** `policylineanswer`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A merge table linking answers to a specific policyline. Specific to PolicyCenter.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| PolicyLine | ForeignKey | Yes | PolicyLine | - | Foreign key target: PolicyLine |

---

### Entity: LocationAnswer

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\LocationAnswer.eti`
**Entity Type:** `effdated`
**Database Table:** `locationanswer`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Links location and answer references - answers are persisted text responses to questions in the location ui. Specific to PolicyCenter.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| PolicyLocation | ForeignKey | Yes | PolicyLocation | - | Foreign key target: PolicyLocation |

---

### Entity: BOPLocationAnswer

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BOPLocationAnswer.eti`
**Entity Type:** `effdated`
**Database Table:** `boplocationanswer`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Links location and answer references - answers are persisted text responses to questions in the location ui. Specific to Policy Center

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BOPLocation | ForeignKey | Yes | BOPLocation | - | Foreign key target: BOPLocation |

---

### Entity: APDProduct

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDProduct.eti`
**Entity Type:** `retireable`
**Database Table:** `apdproduct`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Product definition

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| CodeIdentifier | patterncode | No | - | - | The code used within the product model to identify this product |
| Name | shorttext | No | - | - | - |
| Description | shorttext | No | - | - | A description of the product |
| Coinsurance | bit | Yes | - | - | Default: false Whether this product can be subject to coinsurance (and layered) |
| Multiline | bit | Yes | - | - | Default: false Whether this product is multi-line; default false (single line) |
| Abbreviation | varchar | No | - | - | The abbreviation used to identify the line |
| UsesLocationListView | bit | Yes | - | - | Default: false |
| WrittenByThirdParty | bit | Yes | - | - | Default: false If true, this product is written by another insurance company (captured as an organisation) |
| DefinitionSequence | integer | Yes | - | - | Default: 0 Provides a generic sequence number for added definition objects to ensure a unique publicID for a product definition |
| ProductCode | patterncode | No | - | - | The code of the actual product generated from this definition |
| Portal | bit | Yes | - | - | Default: false Whether the product is available in the portal or not |
| DateInstalled | datetime | No | - | - | Date when product was last installed |
| DateUpdated | datetime | No | - | - | Date when product was last updated |
| Currencies | TypeKey | Yes | - | APDCurrencyHandling | Default: domestic  Codes: [domestic, single, basicmulti, fullmulti] |
| ProductAccountType | TypeKey | Yes | - | ProductAccountType | Default: Any Account type of product Codes: [Person, Company, Any] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| ProductLines | APDProductToLine | Child collection |

---

### Entity: APDProductLine

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDProductLine.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** APDCoverable
**Effective-Dated Container Branch Field:** N/A
**Description:** Product line definition

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| ProductLineCode | patterncode | No | - | - | The code of the actual product line generated from this definition |
| CodeIdentifier | patterncode | No | - | - | The code used within the product model to identify this line |
| LinePrefix | varchar | No | - | - | The prefix uses for all objects that belong to this line |
| DefinitionSequence | integer | Yes | - | - | Default: 0 Provides a generic sequence number for added definition objects to ensure a unique publicID for an LOB definition |
| Currencies | TypeKey | Yes | - | APDCurrencyHandling | Default: domestic The currencies used by this line Codes: [domestic, single, basicmulti, fullmulti] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Products | APDProductToLine | Link to the products that use this line |
| Editions | APDProductLineEdition | The editions of this product line |

---

### Entity: APDCoverage

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDCoverage.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** APDClause
**Effective-Dated Container Branch Field:** N/A
**Description:** Coverage definition

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| SeparateBilling | bit | Yes | - | - | Default: false If true, this coverage will create an individual debtors charge items for billing |
| SeparateCollection | bit | Yes | - | - | Default: false If true, this coverage will create an individual debtors charge for cash allocation |
| PricingOrder | integer | Yes | - | - | The order in which the price is calculated (within its set) |
| WrittenByThirdParty | bit | Yes | - | - | Default: false If true, this product is written by another insurance company (captured as an organisation) |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| CostDefinitions | APDCoverageCostDefinition | The definition of costs that apply to this coverage |
| Perils | APDCoveragePeril | The perils included in the coverage |
| ClaimCategories | APDCoverageClaim | The claim categories appropriate to this coverage |

---

### Entity: APDRiskCoverable

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDRiskCoverable.eti`
**Entity Type:** `effdated`
**Database Table:** `riskcoverable`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** The coverable for a manual line

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| SequenceNumber | integer | No | - | - | The index of this risk coverable |
| ManualPolicyLine | ForeignKey | Yes | APDManualPolicyLine | - | The policy line that this belongs |
| Coverable | ForeignKey | Yes | APDCoverable | - | Definition of the coverable |
| Parent | ForeignKey | No | APDRiskCoverable | - | The risk object that this is a part of |
| Location | ForeignKey | No | PolicyLocation | - | The location when this coverable is a location |
| Building | ForeignKey | No | Building | - | The building this coverable is (when it is a building) |
| ThirdPartyUnderwriter | ForeignKey | No | ProducerCode | - | The organisation that underwrites the coverable/line |
| ChildRiskObjectAutoNumberSeq | ForeignKey | No | AutoNumberSequence | - | Sequence to autonumber child risk objects |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| RiskFields | APDRiskField | The fields describing this coverable |
| RiskExposures | APDRiskExposure | A list of things that expose this coverable to risk |
| RiskClauses | APDRiskClause | The cover required for this risk object |
| RiskCosts | APDRiskCost | A cost that makes up the price of the risk |
| CostPricing | APDRiskPricing | Pricing for this coverable that are used to create costs |

---

### Entity: APDExposure

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDExposure.eti`
**Entity Type:** `retireable`
**Database Table:** `apdexposure`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Things that expose a risk object to risk

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Name | shorttext | No | - | - | The name of the type of exposure used in the UI as a title |
| MenuLabel | shorttext | No | - | - | Exposure list label used in the UI |
| Description | shorttext | No | - | - | A description of what the exposure is, e.g. a driver, a class of employees, an industry class |
| TypeName | varchar | No | - | - | The entity used to persist this exposure |
| IsAutoNumbered | bit | Yes | - | - | Default: false Defines if the exposures are to be auto numbered (if this is needed?) |
| Coverable | ForeignKey | No | APDCoverable | - | The coverable for with this defines the risk exposure |
| RiskLocation | TypeKey | Yes | - | APDRiskLocationType | Default: useParent Defines how the jurisdiction/location of this coverable risk is determined Codes: [isLocation, isBuilding, refLocation, useParent] |
| ExposureType | TypeKey | Yes | - | APDExposureType | Default: liab The type of risk resulting from this exposure Codes: [liab, prop, contact, other] |
| ContactRole | TypeKey | No | - | APDExposureContactRole | Where the exposure is a contact, this is the role of that contact on the policy Codes: [driver, named] |
| RatingType | TypeKey | Yes | - | APDExposureRatingType | Default: term Determines how exposure based rating will be applied Codes: [term, basis, mixed] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Fields | APDExposureField | The fields for this exposure type |

---

### Entity: APDField

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDField.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** APDAttribute
**Effective-Dated Container Branch Field:** N/A
**Description:** The base definition of any type of field

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Identifier | bit | Yes | - | - | Default: false |
| Coverable | ForeignKey | Yes | APDCoverable | - | The coverable definition to which this field belongs |

---

### Entity: APDCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDCost.eti`
**Entity Type:** `effdated`
**Database Table:** `apdcost`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A unit of premium or other cost (taxes, fees, etc.) for the Manual Products line.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| ManualPolicyLine | ForeignKey | Yes | APDManualPolicyLine | - | Manual Products line |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Transactions | APDTransaction | APD Transactions |

---

### Entity: APDTerm

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDTerm.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** APDAttribute
**Effective-Dated Container Branch Field:** N/A
**Description:** The base definition of any type of term

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| ScheduleItemAttribute | bit | Yes | - | - | Default: false |
| GenerateAsClauseTerm | bit | Yes | - | - | Default: false If true and ScheduleItemAttribute is also true, this attribute will be generated as a linked clause term, otherwise, it will become a scheduled item property on the clause. |
| Clause | ForeignKey | Yes | APDClause | - | The clause to which this term belongs |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| DropdownColumns | APDDropdownColumn | The columns of values associated with dropdown entries |

---

### Entity: AccountAccount

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\AccountAccount.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\AccountAccount.etx`
**Entity Type:** `retireable`
**Database Table:** `accountaccount`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A relationship between two accounts.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| SourceAccount | ForeignKey | Yes | Account | - | The source account in the relationship. |
| TargetAccount | ForeignKey | Yes | Account | - | The target account in the relationship. |
| RelationshipType | TypeKey | Yes | - | AccountRelationshipType | The type of relationship from the perspective of the source account. Codes: [parent, child, commonowner] |

---

### Entity: AccountContactRoleReplacement

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\AccountContactRoleReplacement.eti`
**Entity Type:** `retireable`
**Database Table:** `acrreplacement`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Indicates that two AccountContactRoles were merged, and which one replaces the other

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| MergedPublicID | publicid | Yes | - | - | The PublicID of the AccountContactRole that was Merged into another |
| ReplacementAccountContactRole | ForeignKey | Yes | AccountContactRole | - | The AccountContactRole that replaced the merged AccountContactRole |

---

### Entity: AccountContactView

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\AccountContactView.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** AccountContact View.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: AccountHolderCountWorkItem

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\AccountHolderCountWorkItem.eti`
**Entity Type:** `keyable`
**Database Table:** `acctholdercountworkitem`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** WorkItem to update Contact.AccountHolderCount

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Contact | softentityreference | Yes | - | - | The ID of the Contact to be updated. |

---

### Entity: AccountingContact

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\AccountingContact.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** AccountContactRole
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: AccountSummary

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\AccountSummary.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Encapsulates the "summary" or "header" fields needed to display the results of an Account search.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: AccountUserRoleAssignment

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\AccountUserRoleAssignment.eti`
**Entity Type:** `retireable`
**Database Table:** `accountuserroleassign`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** User role assignments for Accounts.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Account | ForeignKey | Yes | Account | - | Associated account. |

---

### Entity: APDAttribute

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDAttribute.eti`
**Entity Type:** `retireable`
**Database Table:** `apdattribute`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** The base definition of any attribute

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Label | shorttext | No | - | - | The label for this field on the screen |
| Sequence | integer | Yes | - | - | The order in which the fields are displayed |
| Name | shorttext | No | - | - | The name of the field in the object model |
| Description | shorttext | No | - | - | The description of the field in the object model |
| Jurisdiction | bit | No | - | - | Default: false Identifies that this field is the location that provides the jurisdiction of the risk |
| Typelist | patterncode | No | - | - | The name of the typelist that implements this attribute as a drop down (if relevant) |
| IsDropDownOwner | bit | No | - | - | If set, this attribute is an owner of a dropdown list |
| DoNotRegenerate | bit | No | - | - | If set, this is a typelist whose content is being maintained outside of the product definition |
| Category | shorttext | No | - | - | The category of this attribute |
| Scalable | bit | Yes | - | - | Default: false If true, this attribute should be pro-rated on splits and changes to period width |
| SplitByRatingPeriods | bit | Yes | - | - | Default: false If true, this attribute will have values defined by rating periods |
| OwningDropDown | ForeignKey | No | APDAttribute | - | The attribute that owns the list  |
| Type | TypeKey | Yes | - | APDFieldType | Default: varchar The type of field  Codes (9 total): [varchar, integer, bigdecimal, boolean, date, ...] |
| DropDownType | TypeKey | No | - | APDDropDownType | The way this attribute will be implemented as a dropdown  Codes: [typelist, option, package] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Codes | APDDropdownEntry | The list of available drop down entries |
| Rules | APDAttributeRule | Rules that apply to this attribute |

---

### Entity: APDAttributeRule

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDAttributeRule.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** APDRule
**Effective-Dated Container Branch Field:** N/A
**Description:** Rule associated with an attribute

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Attribute | ForeignKey | Yes | APDAttribute | - | The attribute to which this rule applies |

---

### Entity: APDClaimCostCategory

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDClaimCostCategory.eti`
**Entity Type:** `retireable`
**Database Table:** `apdclaimcostcategory`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A type of cost resulting from a claim; matches CC CostCategory typelist

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| CodeIdentifier | patterncode | No | - | - | The code used within the product model to identify this claim cost category |
| Name | shorttext | No | - | - | The name of the claim cost category as displayed in the UI |
| Description | shorttext | No | - | - | A description of the claim cost category |
| CostType | TypeKey | Yes | - | APDCostType | The type of claim cost Codes: [claimscost, aoexpense, dccexpense] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| RestrictedPerils | APDClaimPeril | The perils to which this cost is restricted; if empty it can be generally used for any claim against associated coverages |

---

### Entity: APDClaimPeril

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDClaimPeril.eti`
**Entity Type:** `retireable`
**Database Table:** `apdclaimperil`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Optional restriction of the claim cost category to a peril

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| ClaimCost | ForeignKey | Yes | APDClaimCostCategory | - | Foreign key target: APDClaimCostCategory |
| Peril | ForeignKey | Yes | APDPeril | - | One of the perils to which this cost category is restricted |

---

### Entity: APDClause

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDClause.eti`
**Entity Type:** `retireable`
**Database Table:** `apdclause`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Clause definition

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| CodeIdentifier | patterncode | No | - | - | The code used within the product model to identify this clause |
| Name | shorttext | No | - | - | The name of the clause as displayed in the UI |
| Description | shorttext | No | - | - | A description of the clause |
| Sequence | integer | No | - | - | The sequence the clauses are to be listed |
| Coverable | ForeignKey | Yes | APDCoverable | - | The risk object that has this cover |
| ClauseCategory | ForeignKey | No | APDClauseCategory | - | The UI category to which the clause belongs |
| ScheduledItem | ForeignKey | No | APDScheduledItem | - | Scheduled item |
| ParentClause | ForeignKey | No | APDClause | - | The parent clause of this clause |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Terms | APDTerm | The terms that qualify this clause |
| Rules | APDClauseRule | Rules that apply to this clause |

---

### Entity: APDClauseCategory

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDClauseCategory.eti`
**Entity Type:** `retireable`
**Database Table:** `apdclausecategory`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A category that groups clauses for data entry

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Name | shorttext | No | - | - | The name of the category |
| Description | shorttext | No | - | - | - |
| CodeIdentifier | patterncode | No | - | - | The pattern code used in the product model definition |
| Sequence | integer | No | - | - | The sequence that coverage categories are displayed. Sequence no. 1 is assumed to be primary coverage |
| Itemised | bit | Yes | - | - | Default: false If itemised, the clauses are listed in their own tab (in the given sequence), otherwise it is available for "library lookup". Only applies to categories of coverages |
| Hidden | bit | Yes | - | - | Default: false Hidden categories do not list the coverages as these are "assumed" by the packaged cover; they may list conditions that provide common terms to the packaged covers |
| Coverable | ForeignKey | Yes | APDCoverable | - | The coverable to which this category belongs |

---

### Entity: APDClauseRule

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDClauseRule.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** APDRule
**Effective-Dated Container Branch Field:** N/A
**Description:** Rule associated with a clause

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Clause | ForeignKey | Yes | APDClause | - | The clause to which this rule applies |

---

### Entity: APDCondition

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDCondition.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** APDClause
**Effective-Dated Container Branch Field:** N/A
**Description:** Condition Definition

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: APDCoreAttribute

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDCoreAttribute.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** APDAttribute
**Effective-Dated Container Branch Field:** N/A
**Description:** Core application field; used for definition of core fields in rules etc.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Coverable | ForeignKey | No | APDCoverable | - | The entity to which this attribute belongs |
| FieldType | TypeKey | Yes | - | APDCoreFieldType | The core field Codes: [APDProduct, UWCompanyCode, BaseState, PreferredCoverageCurrency] |

---

### Entity: APDCostCodeFilter

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDCostCodeFilter.eti`
**Entity Type:** `retireable`
**Database Table:** `apdcosttypefilter`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Cost types included in the accumulation when calculating the basis of another cost

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| CostDefinition | ForeignKey | Yes | APDCostDefinition | - | The cost definition that is filtered |
| CostCode | ForeignKey | Yes | CostCode | - | The cost code included |

---

### Entity: APDCostDefinition

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDCostDefinition.eti`
**Entity Type:** `retireable`
**Database Table:** `apdcostdefinition`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** The definition of a cost

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| SeparateBilling | bit | Yes | - | - | Default: false If true, this cost will create an individual debtors charge for billing |
| SeparateCollection | bit | Yes | - | - | Default: false If true, this cost will create an individual debtors charge for cash allocation |
| PricingOrder | integer | Yes | - | - | The order in which the price is calculated (within its set) |
| CumulativeCostBasis | bit | Yes | - | - | Default: false If true, the basis is the sum of prior calculated costs |
| CostCode | ForeignKey | Yes | CostCode | - | Foreign key target: CostCode |
| Basis | ForeignKey | No | APDAttribute | - | The term/coverable attribute used as the basis, if appropriate |
| RatingScale | TypeKey | No | - | RatingScale | Default: 1 The scale of the basis to which the rate is applied Codes: [1, 100, 1000] |
| JurisdictionFilter | TypeKey | No | - | Jurisdiction | If set, accumulated costs accumulate for only this jurisdiction when calculating the basis Codes (98 total): [AK, AL, AR, AZ, CA, ...] |
| RateAmountTypeFilter | TypeKey | No | - | RateAmountType | If set, accumulated costs accumulate for only this rate amount type when calculating the basis Codes: [StdPremium, NonstdPremium, TaxSurcharge] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| CostSteps | APDCostStepDefinition | The optional steps defined to create this price |
| CostCodeFilters | APDCostCodeFilter | If set, accumulated costs accumulate for only these cost codes when calculating the basis |

---

### Entity: APDCostStepDefinition

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDCostStepDefinition.eti`
**Entity Type:** `retireable`
**Database Table:** `apdcoststepdefinition`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** An optional definition of a step in the calculation of a cost

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Description | shorttext | Yes | - | - | Describes what this step is, including key factors |
| CostDefinition | ForeignKey | Yes | APDCostDefinition | - | The cost for which this is a calculation step |
| PrimaryFactor | ForeignKey | No | APDAttribute | - | Foreign key target: APDAttribute |

---

### Entity: APDCoverable

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDCoverable.eti`
**Entity Type:** `retireable`
**Database Table:** `apdcoverable`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Coverable definition

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Name | shorttext | No | - | - | The name of the line or type of coverable used in the UI as a title |
| MenuLabel | shorttext | No | - | - | Line detail label or coverable list label used in the UI |
| Description | shorttext | No | - | - | A description of what the coverable is, e.g. a vehicle |
| TypeName | varchar | No | - | - | The entity (or subtype for lines) used to persist this coverable |
| HasChildren | bit | Yes | - | - | Default: false Defines if this coverable can have child coverables. |
| ChildrenLabel | shorttext | No | - | - | The label given to the tab or reference to the child objects |
| SeparateBilling | bit | Yes | - | - | Default: false If true, this coverable will create an individual debtors charge items for billing |
| SeparateCollection | bit | Yes | - | - | Default: false If true, this coverable will crate an individual debtors charge for cash allocation |
| HasExposure | bit | Yes | - | - | Default: false |
| ExposureLabel | shorttext | No | - | - | The label given to the tab or reference to the exposure objects |
| WrittenByThirdParty | bit | Yes | - | - | Default: false If true, this product is written by another insurance company (captured as an organisation) |
| HasModifiers | bit | Yes | - | - | Default: false Whether this coverable has modifiers |
| IsAutoNumbered | bit | Yes | - | - | Default: false Defines if the coverable is automatically numbered (ignored for the line) |
| Parent | ForeignKey | No | APDCoverable | - | Foreign key target: APDCoverable |
| CoverableType | TypeKey | No | - | APDCoverableType | The type of coverable, such as property, liability, etc Codes: [prop, propwithliab, liabsingle, liabmulti, comb, other] |
| RiskLocation | TypeKey | Yes | - | APDRiskLocationType | Default: useParent Defines how the jurisdiction/location of this coverable risk is determined Codes: [isLocation, isBuilding, refLocation, useParent] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Clauses | APDClause | All clauses relating to this coverable |
| Fields | APDField | Fields available for this coverable |
| ClauseCategories | APDClauseCategory | The set of clause categories used by this coverable |
| CostDefinitions | APDRiskCostDefinition | The definitions of costs that attach directly to this coverable |
| Exposures | APDExposure | The types of risk exposure for this coverable |
| CoreFields | APDCoreAttribute | Standard PolicyCenter fields that may be referred to in rules |

---

### Entity: APDCoverageClaim

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDCoverageClaim.eti`
**Entity Type:** `retireable`
**Database Table:** `apdcoverageclaim`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** The claim cost categories appropriate to the coverage

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Coverage | ForeignKey | Yes | APDCoverage | - | The coverage that can have the given cost category on a claim |
| ClaimCostCategory | ForeignKey | Yes | APDClaimCostCategory | - | A claim cost allowed for the coverage |

---

### Entity: APDCoverageCostDefinition

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDCoverageCostDefinition.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** APDCostDefinition
**Effective-Dated Container Branch Field:** N/A
**Description:** A definition of a cost for a risk object

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Coverage | ForeignKey | Yes | APDCoverage | - | Foreign key target: APDCoverage |

---

### Entity: APDCoveragePeril

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDCoveragePeril.eti`
**Entity Type:** `retireable`
**Database Table:** `apdcoverageperil`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A peril included in the given coverage

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| PerilLimit | decimal | No | - | - | The fixed amount to be used as the limit |
| Deductible | decimal | No | - | - | The fixed amount to be used as the deductible |
| Coverage | ForeignKey | Yes | APDCoverage | - | Foreign key target: APDCoverage |
| Peril | ForeignKey | Yes | APDPeril | - | Foreign key target: APDPeril |
| LimitAttribute | ForeignKey | No | APDAttribute | - | The attribute that holds the limit for this peril |
| DeductibleAttribute | ForeignKey | No | APDAttribute | - | The attribute that holds the deductible for this peril |

---

### Entity: APDDataField

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDDataField.eti`
**Entity Type:** `effdated`
**Database Table:** `apddatafield`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** The instance of a data field within a manual risk

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| StringValue | shorttext | No | - | - | The value if text or a drop down entry |
| DecimalValue | decimal | No | - | - | The value if a number |
| ScalableDecimalValue | decimal | No | - | - | The value if a scalable number |
| IntegerValue | integer | No | - | - | The value if an integer |
| ScalableIntegerValue | integer | No | - | - | The value if a scalable integer |
| BitValue | bit | No | - | - | The value if a true/false |
| DateValue | datetime | No | - | - | The value if a date/time |
| Attribute | ForeignKey | Yes | APDAttribute | - | The definition of the information captured in this field |
| Location | ForeignKey | No | PolicyLocation | - | The value if it is a location |
| CodeValue | ForeignKey | No | APDDropdownEntry | - | The drop down list entry if this field is a drop down |
| Party | ForeignKey | No | PolicyContactRole | - | The value if it is a party |

---

### Entity: APDDropdownColumn

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDDropdownColumn.eti`
**Entity Type:** `retireable`
**Database Table:** `apddropdowncolumn`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A column for a value associated with a dropdown entry 

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Name | shorttext | No | - | - | The name that describes the value within a package |
| Sequence | integer | No | - | - | The sequence the values are to be listed within a package |
| Term | ForeignKey | Yes | APDTerm | - | The attribute for which this is the dropdown code column definition |
| ValueType | TypeKey | No | - | CovTermModelVal | The type of value Codes (7 total): [money, percent, days, hours, count, ...] |

---

### Entity: APDDropdownEntry

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDDropdownEntry.eti`
**Entity Type:** `retireable`
**Database Table:** `apddropdownentry`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A entry in a drop down list attached to a field

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Name | shorttext | No | - | - | The name displayed in the drop-down |
| Sequence | integer | No | - | - | The sequence in which the codes are to be listed |
| Code | patterncode | No | - | - | The code used if generating this dropdown as a typelist |
| Description | shorttext | No | - | - | The description of this drop down entry |
| Attribute | ForeignKey | Yes | APDAttribute | - | The attribute for which this is a drop down entry |
| Currency | TypeKey | No | - | Currency | The currency of the option/package values Codes (7 total): [usd, eur, gbp, cad, aud, ...] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Values | APDDropdownValue | The values of the option or package for this code |

---

### Entity: APDDropdownEntryRule

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDDropdownEntryRule.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** APDAttributeRule
**Effective-Dated Container Branch Field:** N/A
**Description:** Rules that apply to a dropdown entry

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| DropdownEntry | ForeignKey | Yes | APDDropdownEntry | - | The dropdown entry to which this rule applies |

---

### Entity: APDDropdownValue

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDDropdownValue.eti`
**Entity Type:** `retireable`
**Database Table:** `apddropdownvalue`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** The value of an option/package term

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| DecimalValue | decimal | No | - | - | The value if a number |
| IntegerValue | integer | No | - | - | The value if an integer |
| Dropdown | ForeignKey | Yes | APDDropdownEntry | - | The dropdown entry for which this is the value |
| DropdownColumn | ForeignKey | Yes | APDDropdownColumn | - | The column to which the value belongs within the entry |

---

### Entity: APDEdition

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDEdition.eti`
**Entity Type:** `retireable`
**Database Table:** `apdedition`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** An edition of a base product or a variant

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| EditionCode | patterncode | No | - | - | The name or code given to the edition |
| EffectiveDate | datetime | No | - | - | The date this edition becomes available to select |
| EditionDescription | varchar | No | - | - | The description associated with this edition |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| EditionRules | APDRule | Rules associated with this edition |

---

### Entity: APDExclusion

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDExclusion.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** APDClause
**Effective-Dated Container Branch Field:** N/A
**Description:** Exclusion definition

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: APDExposureField

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDExposureField.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** APDAttribute
**Effective-Dated Container Branch Field:** N/A
**Description:** The definition of a field that is part of the exposure

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| ExposureParty | bit | Yes | - | - | Default: false Identifies that this field is the PolicyContactRole that is the exposure |
| BasisScalingKey | bit | No | - | - | Where the exposure is rated basis scalable, this is part of the key to the exposure |
| Exposure | ForeignKey | Yes | APDExposure | - | The exposure to which this field belongs |

---

### Entity: APDExposurePrice

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDExposurePrice.eti`
**Entity Type:** `effdated`
**Database Table:** `apdexposureprice`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** The price for an exposure where exposure pricing is used

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| Rate | rate | No | - | - | The rate, excluding adjustments, to apply to the basis |
| CoveragePricing | ForeignKey | Yes | APDRiskCovPricing | - | The coverage pricing to which this exposure price belongs |
| RiskExposure | ForeignKey | No | APDRiskExposure | - | The risk exposure being priced |
| RiskCoverable | ForeignKey | No | APDRiskCoverable | - | The risk coverable (as an exposure) being priced |

---

### Entity: APDFunctionOperand

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDFunctionOperand.eti`
**Entity Type:** `retireable`
**Database Table:** `apdfunctionoperand`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Function operand for an APD rule

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Func | TypeKey | Yes | - | APDFunctionType | Function name Codes: [min, max, sum] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| FunctionArguments | APDReference | Function argument references |

---

### Entity: APDGenerated

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDGenerated.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: APDInvolvedParty

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDInvolvedParty.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** AccountContactRole
**Effective-Dated Container Branch Field:** N/A
**Description:** Involved Party Account Contact Role

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: APDLossCause

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDLossCause.eti`
**Entity Type:** `retireable`
**Database Table:** `apdlosscause`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Cause of Loss - used to create/sync with CC LossCause typelist

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| CodeIdentifier | patterncode | No | - | - | The code used within the product model to identify this cause of loss |
| Name | shorttext | No | - | - | The name of the loss cause as displayed in the UI |
| Description | shorttext | No | - | - | A description of the loss cause |
| LossType | TypeKey | Yes | - | APDLossType | The type of loss that this cause results in Codes: [AUTO, GL, PR, TRAV, WC] |

---

### Entity: APDManualPolicyLine

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDManualPolicyLine.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\APDManualPolicyLine.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PolicyLine
**Effective-Dated Container Branch Field:** N/A
**Description:** Manual Products line of business

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| ReferenceDateInternal | datetime | No | - | - | Internal field for storing the reference date of this entity on bound policy periods. |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| RiskCoverables | APDRiskCoverable | All the coverables that make up the manual policy, irrespective of their relationships |
| APDCosts | APDCost | Child collection |

---

### Entity: APDPeril

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDPeril.eti`
**Entity Type:** `retireable`
**Database Table:** `apdperil`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** The peril or subclassification of a coverage; matches to the CoverageSubtype typelist in CC

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| CodeIdentifier | patterncode | No | - | - | The code used within the product model to identify this peril/part of a coverage |
| Name | shorttext | No | - | - | The name of the peril/part of a coverage as displayed in the UI |
| Description | shorttext | No | - | - | A description of the loss cause |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| LossCauses | APDPerilCause | The possible causes of a claim covered by this peril |

---

### Entity: APDPerilCause

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDPerilCause.eti`
**Entity Type:** `retireable`
**Database Table:** `apdperilcause`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** The set of perils that can be claimed against for a cause of loss

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Peril | ForeignKey | Yes | APDPeril | - | The peril that owns this link |
| LossCause | ForeignKey | Yes | APDLossCause | - | The cause of loss that can result in a claim for this peril |

---

### Entity: APDPolicyInvolvedParty

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDPolicyInvolvedParty.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PolicyContactRole
**Effective-Dated Container Branch Field:** N/A
**Description:** Involved Party Policy Contact Role

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: APDPricing

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDPricing.eti`
**Entity Type:** `effdated`
**Database Table:** `apdriskpricing`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Identifies the rate from which a cost is created

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| Rate | rate | No | - | - | The rate, excluding adjustments, to apply to the basis |
| CostDefinition | ForeignKey | Yes | APDCostDefinition | - | The definition of this price |

---

### Entity: APDProductLineEdition

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDProductLineEdition.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** APDEdition
**Effective-Dated Container Branch Field:** N/A
**Description:** A version of a product line

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| ProductLine | ForeignKey | Yes | APDProductLine | - | The product line for which this is an edition (version) |

---

### Entity: APDProductToLine

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDProductToLine.eti`
**Entity Type:** `joinarray`
**Database Table:** `apdproducttoline`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** The many to many line between products and lines

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Product | ForeignKey | Yes | APDProduct | - | Foreign key target: APDProduct |
| ProductLine | ForeignKey | Yes | APDProductLine | - | Foreign key target: APDProductLine |

---

### Entity: APDReference

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDReference.eti`
**Entity Type:** `retireable`
**Database Table:** `apdreference`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A reference to APD attribute

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Attribute | ForeignKey | Yes | APDAttribute | - | Reference to an attribute |
| FunctionOperand | ForeignKey | Yes | APDFunctionOperand | - | Foreign key target: APDFunctionOperand |

---

### Entity: APDRiskClause

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDRiskClause.eti`
**Entity Type:** `effdated`
**Database Table:** `apdriskclause`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A clause attaching to a risk

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| RiskCoverable | ForeignKey | Yes | APDRiskCoverable | - | The risk object for which this coverage provides protection |
| Currency | TypeKey | Yes | - | Currency | The currency used by any terms (and the original currency of costs) Codes (7 total): [usd, eur, gbp, cad, aud, ...] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| RiskTerms | APDRiskTerm | The terms that qualify this clause |
| RiskItems | APDRiskScheduleItem | Items covered by/included in this clause |

---

### Entity: APDRiskCondition

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDRiskCondition.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** APDRiskClause
**Effective-Dated Container Branch Field:** N/A
**Description:** A condition clause qualifying a risk

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Condition | ForeignKey | Yes | APDCondition | - | The condition pattern defining this condition |

---

### Entity: APDRiskCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDRiskCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\APDRiskCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** APDCost
**Effective-Dated Container Branch Field:** N/A
**Description:** A cost that makes up the price of the risk

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| RiskCoverable | ForeignKey | Yes | APDRiskCoverable | - | The coverable to which this cost applies |

---

### Entity: APDRiskCostDefinition

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDRiskCostDefinition.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** APDCostDefinition
**Effective-Dated Container Branch Field:** N/A
**Description:** A definition of a cost attached to a coverable (which can be the line)

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Coverable | ForeignKey | Yes | APDCoverable | - | The type of risk for which this cost is calculated |

---

### Entity: APDRiskCovCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDRiskCovCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\APDRiskCovCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** APDCost
**Effective-Dated Container Branch Field:** N/A
**Description:** A cost that makes up the price of the risk

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| RiskCoverage | ForeignKey | Yes | APDRiskCoverage | - | The coverage to which this cost applies |
| Exposure | ForeignKey | No | APDRiskExposure | - | The exposure to which this relates (when there is exposure based pricing) |
| Risk | ForeignKey | No | APDRiskCoverable | - | The entity to which this relates (when there is entity/coverable based pricing) |

---

### Entity: APDRiskCoverage

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDRiskCoverage.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** APDRiskClause
**Effective-Dated Container Branch Field:** N/A
**Description:** A coverage clause covering a risk

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Coverage | ForeignKey | Yes | APDCoverage | - | The coverage pattern defining this coverage |
| ThirdPartyUnderwriter | ForeignKey | No | ProducerCode | - | The organisation that underwrites the coverage |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| RiskCovCosts | APDRiskCovCost | The cost of this coverage (itemised) |
| CostPricing | APDRiskCovPricing | Pricing for this coverage that are used to create costs |

---

### Entity: APDRiskCovPricing

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDRiskCovPricing.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** APDPricing
**Effective-Dated Container Branch Field:** N/A
**Description:** Pricing that creates a coverage cost

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| RiskCoverage | ForeignKey | Yes | APDRiskCoverage | - | The coverage for which this will create a cost |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| ExposurePrices | APDExposurePrice | The set of prices used when rating by exposure |

---

### Entity: APDRiskExclusion

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDRiskExclusion.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** APDRiskClause
**Effective-Dated Container Branch Field:** N/A
**Description:** An exclusion clause qualifying a risk

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Exclusion | ForeignKey | Yes | APDExclusion | - | The exclusion pattern defining this exclusion |

---

### Entity: APDRiskExposure

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDRiskExposure.eti`
**Entity Type:** `effdated`
**Database Table:** `apdriskexposure`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** An exposure to risk within a manual line

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| Exposure | ForeignKey | Yes | APDExposure | - | The definition of this exposure |
| RiskCoverable | ForeignKey | Yes | APDRiskCoverable | - | The risk for which this is exposure |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Fields | APDRiskExposureField | The fields for the exposure |

---

### Entity: APDRiskExposureField

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDRiskExposureField.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** APDDataField
**Effective-Dated Container Branch Field:** N/A
**Description:** The instance of a field within a manual exposure

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| RiskExposure | ForeignKey | Yes | APDRiskExposure | - | The exposure for which this is a field |

---

### Entity: APDRiskField

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDRiskField.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** APDDataField
**Effective-Dated Container Branch Field:** N/A
**Description:** The instance of a field within a manual risk

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| RiskCoverable | ForeignKey | Yes | APDRiskCoverable | - | The coverable that this field qualifies |

---

### Entity: APDRiskPolicyLine

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDRiskPolicyLine.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** APDRiskCoverable
**Effective-Dated Container Branch Field:** N/A
**Description:** The policy line for a manual risk

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| APDEdition | ForeignKey | No | APDProductLineEdition | - | The edition that provides the rules for this policy line (null means the base rules are used) |

---

### Entity: APDRiskPricing

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDRiskPricing.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** APDPricing
**Effective-Dated Container Branch Field:** N/A
**Description:** The pricing for a coverage cost

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| RiskCoverable | ForeignKey | Yes | APDRiskCoverable | - | The coverable for which this will create a cost |

---

### Entity: APDRiskScheduleItem

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDRiskScheduleItem.eti`
**Entity Type:** `effdated`
**Database Table:** `apdriskscheduleitem`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A item attached to a clause

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| RiskClause | ForeignKey | Yes | APDRiskClause | - | The clause that this field qualifies |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| ItemTerms | APDRiskScheduleTerm | The terms that belong to this schedule item |

---

### Entity: APDRiskScheduleTerm

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDRiskScheduleTerm.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** APDRiskTerm
**Effective-Dated Container Branch Field:** N/A
**Description:** A term that is part of a schedule item

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| RiskItem | ForeignKey | Yes | APDRiskScheduleItem | - | The schedule item that this is part of |

---

### Entity: APDRiskTerm

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDRiskTerm.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** APDDataField
**Effective-Dated Container Branch Field:** N/A
**Description:** The instance of a field within a manual risk

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| RiskClause | ForeignKey | Yes | APDRiskClause | - | The clause that this field qualifies |

---

### Entity: APDRule

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDRule.eti`
**Entity Type:** `retireable`
**Database Table:** `apdrule`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A data rule within the product model

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| DefaultStringValue | shorttext | No | - | - | The value if text or a dropdown entry |
| DefaultDecimalValue | decimal | No | - | - | The value if a number |
| DefaultIntegerValue | integer | No | - | - | The value if an integer |
| DefaultBitValue | bit | No | - | - | The value if a true/false |
| DefaultDateValue | datetime | No | - | - | The value if a date/time |
| DefaultCodeValue | ForeignKey | No | APDDropdownEntry | - | The dropdown list entry if this field is a dropdown |
| DefaultCalculatedValue | ForeignKey | No | APDFunctionOperand | - | A calculated value |
| Edition | ForeignKey | No | APDEdition | - | The edition that this version of the rule applies to (if there is no edition, it is a base rule) |
| RuleType | TypeKey | Yes | - | APDRuleType | The type of rule being implemented Codes: [existence, default, min, max, tag] |
| DefaultExistence | TypeKey | No | - | APDDataExistenceType | The default for an existence rule Codes (11 total): [available, captured, derived, hidden, unavailable, ...] |
| TagType | TypeKey | No | - | APDTagType | The type of tag for a tag rule Codes: [rate, submission, riskscore] |
| DefaultTagValue | TypeKey | No | - | APDTagApplicability | The value if a tag Codes: [applies, doesnotapply] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| RuleElements | APDRuleElement | The full list of rule elements belonging to this rule |

---

### Entity: APDRuleCondition

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDRuleCondition.eti`
**Entity Type:** `retireable`
**Database Table:** `apdrulecondition`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A condition to match

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| ConditionValue | shorttext | No | - | - | The value that will be used to evaluate this condition |
| RuleElement | ForeignKey | Yes | APDRuleElement | - | The rule element for with this a data match component |
| Attribute | ForeignKey | No | APDAttribute | - | The attribute that is to be compared. Either Attribute or Clause must have a value, but not both. |
| Clause | ForeignKey | No | APDClause | - | The clause that is to be compared. Either Attribute or Clause must have a value, but not both. |
| CodeValue | ForeignKey | No | APDDropdownEntry | - | Foreign key target: APDDropdownEntry |
| Operator | TypeKey | Yes | - | APDRuleConditionOperator | Default: equals The type of comparison to perform between the attribute and the value Codes (8 total): [equals, notEquals, lessThan, lessThanOrEqual, greaterThan, ...] |

---

### Entity: APDRuleElement

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDRuleElement.eti`
**Entity Type:** `retireable`
**Database Table:** `apdruleelement`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A set of conditions that make up a rule element

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Sequence | integer | Yes | - | - | The order in which the fields are displayed |
| DefaultStringValue | shorttext | No | - | - | The value if text or a dropdown entry |
| DefaultDecimalValue | decimal | No | - | - | The value if a number |
| DefaultIntegerValue | integer | No | - | - | The value if an integer |
| DefaultBitValue | bit | No | - | - | The value if a true/false |
| DefaultDateValue | datetime | No | - | - | The value if a date/time |
| Rule | ForeignKey | Yes | APDRule | - | The rule to which this element belongs |
| DefaultCodeValue | ForeignKey | No | APDDropdownEntry | - | The dropdown list entry if this field is a dropdown |
| Existence | TypeKey | No | - | APDDataExistenceType | The result for an existence rule Codes (11 total): [available, captured, derived, hidden, unavailable, ...] |
| DefaultTagValue | TypeKey | No | - | APDTagApplicability | The value if a tag Codes: [applies, doesnotapply] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| RuleConditions | APDRuleCondition | The conditions that must match for this rule to fire |

---

### Entity: APDScheduledItem

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDScheduledItem.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** APDCoverable
**Effective-Dated Container Branch Field:** N/A
**Description:** Scheduled item definition

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: APDTransaction

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDTransaction.eti`
**Entity Type:** `effdated`
**Database Table:** `apdtransaction`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A transaction for the Manual Products line

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| APDCost | ForeignKey | Yes | APDCost | - | The cost this transaction modifies. |

---

### Entity: BACededPremium

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BACededPremium.eti`
**Entity Type:** `retireable`
**Database Table:** `bacededpremium`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A CommercialAuto implementation of the RICededPremium delegate

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| BACost | ForeignKey | Yes | BACost | - | Foreign key target: BACost |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| CedingTransactions | BACededPremiumTransaction | Child collection |
| CedingHistory | BACededPremiumHistory | Child collection |

---

### Entity: BACededPremiumHistory

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BACededPremiumHistory.eti`
**Entity Type:** `retireable`
**Database Table:** `bacededpremiumhistory`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A CommercialAuto implementation of the RICededPremiumHistory delegate

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| BACededPremium | ForeignKey | Yes | BACededPremium | - | Foreign key target: BACededPremium |

---

### Entity: BACededPremiumTransaction

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BACededPremiumTransaction.eti`
**Entity Type:** `retireable`
**Database Table:** `bacededpremiumtransaction`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A Commercial Auto implementation of the RICededPremiumTransaction delegate

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| BACededPremium | ForeignKey | Yes | BACededPremium | - | Foreign key target: BACededPremium |
| BACededPremiumHistory | ForeignKey | Yes | BACededPremiumHistory | - | Foreign key target: BACededPremiumHistory |

---

### Entity: BACondLookup

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BACondLookup.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** ConditionLookup
**Effective-Dated Container Branch Field:** N/A
**Description:** BA Condition Lookup Table.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| PolicyType | TypeKey | No | - | BAPolicyType | The policy type of this lookup Codes: [BA, garage, motor, BAphysdam] |

---

### Entity: BACovLookup

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BACovLookup.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** CoverageLookup
**Effective-Dated Container Branch Field:** N/A
**Description:** BA Coverage Lookup Table.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| PolicyType | TypeKey | No | - | BAPolicyType | The policy type of this lookup Codes: [BA, garage, motor, BAphysdam] |

---

### Entity: BAExclLookup

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BAExclLookup.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** ExclusionLookup
**Effective-Dated Container Branch Field:** N/A
**Description:** BA Exclusion Lookup Table.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| PolicyType | TypeKey | No | - | BAPolicyType | The policy type of this lookup Codes: [BA, garage, motor, BAphysdam] |

---

### Entity: BAHiredAutoBasis

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BAHiredAutoBasis.eti`
**Entity Type:** `effdated`
**Database Table:** `bahiredautoinfo`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Information necessary for rating hired auto coverages

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| Basis | integer | No | - | - | Basis amount for hired auto coverage |
| IfAnyExposure | bit | No | - | - | Default: false Option to indicate that coverage is provided with precise liability to be determined later (at audit) |
| Jurisdiction | ForeignKey | Yes | BAJurisdiction | - | The Jurisdiction related to hired auto basis |

---

### Entity: BAHiredSpecPerilCov

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BAHiredSpecPerilCov.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** BAStateCov
**Effective-Dated Container Branch Field:** N/A
**Description:** Hired Auto Specified Causes of Loss

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| HiredCauseOfLoss | TypeKey | No | - | SpecifiedCauseOfLoss | Cause of loss Codes: [fire, firetheft, firetheftstorm, limited] |

---

### Entity: BAJurisdiction

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BAJurisdiction.eti`
**Entity Type:** `effdated`
**Database Table:** `bajurisdiction`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Container for state-level elements

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BALine | ForeignKey | No | BusinessAutoLine | - | Foreign key target: BusinessAutoLine |
| State | TypeKey | No | - | Jurisdiction | The jurisdiction that is covered Codes (98 total): [AK, AL, AR, AZ, CA, ...] |
| HiredAutoBasis | OneToOne | No | BAHiredAutoBasis | - | One-to-one link |
| NonOwnedBasis | OneToOne | No | BANonOwnedBasis | - | One-to-one link |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Costs | BAJurisdictionCost | Child collection |
| Coverages | BAStateCov | All Coverages on this State |
| Exclusions | BAStateExcl | All Exclusions on this State |
| Conditions | BAStateCond | All Conditions on this State |
| BAJurisModifiers | BAJurisModifier | Rating info for the line. |

---

### Entity: BAJurisdictionCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BAJurisdictionCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\BAJurisdictionCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** BACost
**Effective-Dated Container Branch Field:** N/A
**Description:** A cost at the BA Jurisdiction level.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BAJurisdictionCostType | TypeKey | Yes | - | BAJurisdictionCostType | Codes: [CancelShortRatePenalty, StateTax] |

---

### Entity: BAJurisModifier

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BAJurisModifier.eti`
**Entity Type:** `effdated`
**Database Table:** `bajurismodifier`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A modifier for Commercial Auto Jurisdictions

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| Jurisdiction | ForeignKey | Yes | BAJurisdiction | - | The jurisdiction for which this modifier applies |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| BAJurisRateFactors | BAJurisRateFactor | Individual components of the rating factor |

---

### Entity: BAJurisRateFactor

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BAJurisRateFactor.eti`
**Entity Type:** `effdated`
**Database Table:** `bajurisratefactor`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A rate factor is a risk characteristic and its associated numeric value which might have an impact on premium. A common example of Rate Factors are the components of IRPM (individual risk premium modifier).

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BAJurisModifier | ForeignKey | Yes | BAJurisModifier | - | The modifier containing this rate factor |

---

### Entity: BALineCovCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BALineCovCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\BALineCovCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** BACost
**Effective-Dated Container Branch Field:** N/A
**Description:** A  unit of cost for a Commercial Auto Line coverage

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BusinessAutoCov | ForeignKey | Yes | BusinessAutoCov | - | Foreign key target: BusinessAutoCov |

---

### Entity: BALineCovNonownedCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BALineCovNonownedCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\BALineCovNonownedCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** BALineCovCost
**Effective-Dated Container Branch Field:** N/A
**Description:** A unit of price for a Commercial Auto Line coverage rated by state and Nonowned Exposure type

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BANonOwnedLiabCovCostType | TypeKey | Yes | - | BANonOwnedLiabCovCostType | Codes: [Employees, Partners, Volunteers] |

---

### Entity: BAMinimumPremiumCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BAMinimumPremiumCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\BAMinimumPremiumCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** BACost
**Effective-Dated Container Branch Field:** N/A
**Description:** The minimum premium adjustment cost for the Commercial Auto Line

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: BAModifier

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BAModifier.eti`
**Entity Type:** `effdated`
**Database Table:** `bamodifier`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A line-level modifier for Commercial Auto

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BALine | ForeignKey | Yes | BusinessAutoLine | - | Foreign key target: BusinessAutoLine |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| BARateFactors | BARateFactor | Individual components of the rating factor |

---

### Entity: BAModLookup

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BAModLookup.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** ModifierLookup
**Effective-Dated Container Branch Field:** N/A
**Description:** BA Modifier Lookup Table.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| PolicyType | TypeKey | No | - | BAPolicyType | The policy type of this lookup Codes: [BA, garage, motor, BAphysdam] |

---

### Entity: BANonOwnedBasis

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BANonOwnedBasis.eti`
**Entity Type:** `effdated`
**Database Table:** `banonownedinfo`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Information necessary for rating non-owned coverages

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| NumEmployees | integer | No | - | - | Number of employees |
| NumPartners | integer | No | - | - | Number of partners |
| NumVolunteers | integer | No | - | - | Number of volunteers |
| Jurisdiction | ForeignKey | Yes | BAJurisdiction | - | The Jurisdiction for the Non Owned Basis and its coverage |

---

### Entity: BAPolicyContactRole

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BAPolicyContactRole.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PolicyContactRole
**Effective-Dated Container Branch Field:** N/A
**Description:** A PolicyContactRole specific to a Commercial Auto policy line.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BusinessAutoLine | ForeignKey | No | BusinessAutoLine | - | The Commercial Auto policy line this contact role is associated with. |

---

### Entity: BARateFactor

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BARateFactor.eti`
**Entity Type:** `effdated`
**Database Table:** `baratefactor`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A rate factor is a risk characteristic and its associated numeric value which might have an impact on premium. As used here rate factors are applied to base premium rather than rates. A common example of Rate Factors are the components of IRPM (individual risk premium modifier).

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BAModifier | ForeignKey | Yes | BAModifier | - | Foreign key target: BAModifier |

---

### Entity: BARateLookup

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BARateLookup.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** RateFactorLookup
**Effective-Dated Container Branch Field:** N/A
**Description:** BA Rate Factor Lookup Table.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| PolicyType | TypeKey | No | - | BAPolicyType | The policy type of this lookup Codes: [BA, garage, motor, BAphysdam] |

---

### Entity: BaseQuotingWorkItem

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BaseQuotingWorkItem.eti`
**Entity Type:** `keyable`
**Database Table:** `basequotingworkitem`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** WorkItem to asynchronously quote or rate PolicyPeriod

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| RequestingUser | ForeignKey | Yes | User | - | User for which we will generate the quote |
| PolicyPeriod | ForeignKey | Yes | PolicyPeriod | - | The PolicyPeriod to quote |

---

### Entity: BASpecCausesLossCov

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BASpecCausesLossCov.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** BusinessVehicleCov
**Effective-Dated Container Branch Field:** N/A
**Description:** Specified Causes of Loss

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| SpecifiedCauseOfLoss | TypeKey | No | - | SpecifiedCauseOfLoss | Cause of loss Codes: [fire, firetheft, firetheftstorm, limited] |

---

### Entity: BAStateCond

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BAStateCond.eti`
**Entity Type:** `effdated`
**Database Table:** `bastatecond`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A state-level policy condition for Commercial Auto

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BooleanTerm1 | bit | No | - | - | boolean cov term field |
| BooleanTerm1Avl | bit | No | - | - | whether or not the BooleanTerm1 field was available the last time availability was checked |
| BooleanTerm2 | bit | No | - | - | boolean cov term field |
| BooleanTerm2Avl | bit | No | - | - | whether or not the BooleanTerm2 field was available the last time availability was checked |
| ChoiceTerm1 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm1Avl | bit | No | - | - | whether or not the ChoiceTerm1 field was available the last time availability was checked |
| ChoiceTerm2 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm2Avl | bit | No | - | - | whether or not the ChoiceTerm2 field was available the last time availability was checked |
| DirectTerm1 | decimal | No | - | - | direct cov term field |
| DirectTerm1Avl | bit | No | - | - | whether or not the DirectTerm1 field was available the last time availability was checked |
| DirectTerm2 | decimal | No | - | - | direct cov term field |
| DirectTerm2Avl | bit | No | - | - | whether or not the DirectTerm2 field was available the last time availability was checked |
| DateTerm1 | datetime | No | - | - | datetime cov term field |
| DateTerm1Avl | bit | No | - | - | whether or not the DateTerm1 field was available the last time availability was checked |
| DateTerm2 | datetime | No | - | - | datetime cov term field |
| DateTerm2Avl | bit | No | - | - | whether or not the DateTerm2 field was available the last time availability was checked |
| StringTerm1 | shorttext | No | - | - | string cov term field |
| StringTerm1Avl | bit | No | - | - | whether or not the StringTerm1 field was available the last time availability was checked |
| StringTerm2 | shorttext | No | - | - | string cov term field |
| StringTerm1Av2 | bit | No | - | - | whether or not the StringTerm1 field was available the last time availability was checked |
| BAJurisdiction | ForeignKey | No | BAJurisdiction | - | Foreign key target: BAJurisdiction |

---

### Entity: BAStateCov

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BAStateCov.eti`
**Entity Type:** `effdated`
**Database Table:** `bastatecov`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A state-level coverage for Commercial Auto

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BooleanTerm1 | bit | No | - | - | boolean cov term field |
| BooleanTerm1Avl | bit | No | - | - | whether or not the BooleanTerm1 field was available the last time availability was checked |
| BooleanTerm2 | bit | No | - | - | boolean cov term field |
| BooleanTerm2Avl | bit | No | - | - | whether or not the BooleanTerm2 field was available the last time availability was checked |
| BooleanTerm3 | bit | No | - | - | boolean cov term field |
| BooleanTerm3Avl | bit | No | - | - | whether or not the BooleanTerm3field was available the last time availability was checked |
| BooleanTerm4 | bit | No | - | - | boolean cov term field |
| BooleanTerm4Avl | bit | No | - | - | whether or not the BooleanTerm4 field was available the last time availability was checked |
| BooleanTerm5 | bit | No | - | - | boolean cov term field |
| BooleanTerm5Avl | bit | No | - | - | whether or not the BooleanTerm5 field was available the last time availability was checked |
| ChoiceTerm1 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm1Avl | bit | No | - | - | whether or not the ChoiceTerm1 field was available the last time availability was checked |
| ChoiceTerm2 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm2Avl | bit | No | - | - | whether or not the ChoiceTerm2 field was available the last time availability was checked |
| ChoiceTerm3 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm3Avl | bit | No | - | - | whether or not the ChoiceTerm3 field was available the last time availability was checked |
| ChoiceTerm4 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm4Avl | bit | No | - | - | whether or not the ChoiceTerm4 field was available the last time availability was checked |
| ChoiceTerm5 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm5Avl | bit | No | - | - | whether or not the ChoiceTerm5 field was available the last time availability was checked |
| ChoiceTerm6 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm6Avl | bit | No | - | - | whether or not the ChoiceTerm6 field was available the last time availability was checked |
| ChoiceTerm7 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm7Avl | bit | No | - | - | whether or not the ChoiceTerm7 field was available the last time availability was checked |
| ChoiceTerm8 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm8Avl | bit | No | - | - | whether or not the ChoiceTerm8 field was available the last time availability was checked |
| BAJurisdiction | ForeignKey | No | BAJurisdiction | - | Foreign key target: BAJurisdiction |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Costs | BAStateCovCost | Child collection |

---

### Entity: BAStateCovCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BAStateCovCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\BAStateCovCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** BACost
**Effective-Dated Container Branch Field:** N/A
**Description:** The cost for a state-level coverage.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BAStateCov | ForeignKey | Yes | BAStateCov | - | Foreign key target: BAStateCov |

---

### Entity: BAStateCovVehicleCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BAStateCovVehicleCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\BAStateCovVehicleCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** BAStateCovCost
**Effective-Dated Container Branch Field:** N/A
**Description:** The cost for a state-level coverage on a particular business vehicle.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: BAStateCovVehiclePIPCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BAStateCovVehiclePIPCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\BAStateCovVehiclePIPCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** BAStateCovVehicleCost
**Effective-Dated Container Branch Field:** N/A
**Description:** The cost for a state-level PIP coverage on a particular business vehicle.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BAStateCovPIPCostType | TypeKey | Yes | - | BAStateCovPIPCostType | Codes (10 total): [basic, optional, income, medical, rehab, ...] |

---

### Entity: BAStateExcl

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BAStateExcl.eti`
**Entity Type:** `effdated`
**Database Table:** `bastateexcl`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A state-level exclusion for Commercial Auto

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BooleanTerm1 | bit | No | - | - | boolean cov term field |
| BooleanTerm1Avl | bit | No | - | - | whether or not the BooleanTerm1 field was available the last time availability was checked |
| BooleanTerm2 | bit | No | - | - | boolean cov term field |
| BooleanTerm2Avl | bit | No | - | - | whether or not the BooleanTerm2 field was available the last time availability was checked |
| ChoiceTerm1 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm1Avl | bit | No | - | - | whether or not the ChoiceTerm1 field was available the last time availability was checked |
| ChoiceTerm2 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm2Avl | bit | No | - | - | whether or not the ChoiceTerm2 field was available the last time availability was checked |
| DirectTerm1 | decimal | No | - | - | direct cov term field |
| DirectTerm1Avl | bit | No | - | - | whether or not the DirectTerm1 field was available the last time availability was checked |
| DirectTerm2 | decimal | No | - | - | direct cov term field |
| DirectTerm2Avl | bit | No | - | - | whether or not the DirectTerm2 field was available the last time availability was checked |
| DateTerm1 | datetime | No | - | - | datetime cov term field |
| DateTerm1Avl | bit | No | - | - | whether or not the DateTerm1 field was available the last time availability was checked |
| DateTerm2 | datetime | No | - | - | datetime cov term field |
| DateTerm2Avl | bit | No | - | - | whether or not the DateTerm2 field was available the last time availability was checked |
| StringTerm1 | shorttext | No | - | - | string cov term field |
| StringTerm1Avl | bit | No | - | - | whether or not the StringTerm1 field was available the last time availability was checked |
| StringTerm2 | shorttext | No | - | - | string cov term field |
| StringTerm1Av2 | bit | No | - | - | whether or not the StringTerm1 field was available the last time availability was checked |
| BAJurisdiction | ForeignKey | No | BAJurisdiction | - | Foreign key target: BAJurisdiction |

---

### Entity: BatchProcessLease

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BatchProcessLease.eti`
**Entity Type:** `keyable`
**Database Table:** `batchprocesslease`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: BatchProcessLeaseHistory

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BatchProcessLeaseHistory.eti`
**Entity Type:** `keyable`
**Database Table:** `batchprocessleasehistory`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: BAVehicleCovLookup

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BAVehicleCovLookup.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** BACovLookup
**Effective-Dated Container Branch Field:** N/A
**Description:** BAVehicle-Level Coverage Lookup Table.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| VehicleType | TypeKey | No | - | VehicleType | Codes: [Commercial, PP, PublicTransport, Special, auto, other] |

---

### Entity: BAVhcleAddlInterest

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BAVhcleAddlInterest.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** AddlInterestDetail
**Effective-Dated Container Branch Field:** N/A
**Description:** An additional interest on a businsess auto vehicle

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BAVehicle | ForeignKey | Yes | BusinessVehicle | - | Foreign key target: BusinessVehicle |

---

### Entity: BOPAddnlInsuredCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BOPAddnlInsuredCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\BOPAddnlInsuredCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** BOPGeneralPremium
**Effective-Dated Container Branch Field:** N/A
**Description:** A taxable unit of price for a period of time, not to be broken up any further, for a Business Owners additional insured

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| AdditionalInsured | ForeignKey | Yes | PolicyAddlInsured | - | Foreign key target: PolicyAddlInsured |

---

### Entity: BOPBldgAddlInterest

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BOPBldgAddlInterest.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** AddlInterestDetail
**Effective-Dated Container Branch Field:** N/A
**Description:** An additional interest on a building

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BOPBuilding | ForeignKey | Yes | BOPBuilding | - | Foreign key target: BOPBuilding |

---

### Entity: BOPBuildingCov

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BOPBuildingCov.eti`
**Entity Type:** `effdated`
**Database Table:** `bopbuildingcov`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A building-level coverage for Business Owners

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BooleanTerm1 | bit | No | - | - | boolean cov term field |
| BooleanTerm1Avl | bit | No | - | - | whether or not the BooleanTerm1 field was available the last time availability was checked |
| BooleanTerm2 | bit | No | - | - | boolean cov term field |
| BooleanTerm2Avl | bit | No | - | - | whether or not the BooleanTerm2 field was available the last time availability was checked |
| BooleanTerm3 | bit | No | - | - | boolean cov term field |
| BooleanTerm3Avl | bit | No | - | - | whether or not the BooleanTerm3 field was available the last time availability was checked |
| BooleanTerm4 | bit | No | - | - | boolean cov term field |
| BooleanTerm4Avl | bit | No | - | - | whether or not the BooleanTerm4 field was available the last time availability was checked |
| BooleanTerm5 | bit | No | - | - | boolean cov term field |
| BooleanTerm5Avl | bit | No | - | - | whether or not the BooleanTerm5 field was available the last time availability was checked |
| ChoiceTerm1 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm1Avl | bit | No | - | - | whether or not the ChoiceTerm1 field was available the last time availability was checked |
| ChoiceTerm2 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm2Avl | bit | No | - | - | whether or not the ChoiceTerm2 field was available the last time availability was checked |
| ChoiceTerm3 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm3Avl | bit | No | - | - | whether or not the ChoiceTerm3 field was available the last time availability was checked |
| ChoiceTerm4 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm4Avl | bit | No | - | - | whether or not the ChoiceTerm4 field was available the last time availability was checked |
| ChoiceTerm5 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm5Avl | bit | No | - | - | whether or not the ChoiceTerm5 field was available the last time availability was checked |
| DateTerm1 | datetime | No | - | - | datetime cov term field |
| DateTerm1Avl | bit | No | - | - | whether or not the DateTerm1 field was available the last time availability was checked |
| DateTerm2 | datetime | No | - | - | datetime cov term field |
| DateTerm2Avl | bit | No | - | - | whether or not the DateTerm2 field was available the last time availability was checked |
| DirectTerm1 | decimal | No | - | - | direct cov term field |
| DirectTerm1Avl | bit | No | - | - | whether or not the DirectTerm1 field was available the last time availability was checked |
| DirectTerm2 | decimal | No | - | - | direct cov term field |
| DirectTerm2Avl | bit | No | - | - | whether or not the DirectTerm2 field was available the last time availability was checked |
| DirectTerm3 | decimal | No | - | - | direct cov term field |
| DirectTerm3Avl | bit | No | - | - | whether or not the DirectTerm3 field was available the last time availability was checked |
| BOPBuilding | ForeignKey | No | BOPBuilding | - | Foreign key target: BOPBuilding |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Costs | BOPBuildingCovCost | Child collection |

---

### Entity: BOPBuildingCovCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BOPBuildingCovCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\BOPBuildingCovCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** BOPCoveragePremium
**Effective-Dated Container Branch Field:** N/A
**Description:** A taxable unit of price for a period of time, not to be broken up any further, for a Business Owners building coverage

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BOPBuildingCov | ForeignKey | Yes | BOPBuildingCov | - | Foreign key target: BOPBuildingCov |

---

### Entity: BOPCededPremium

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BOPCededPremium.eti`
**Entity Type:** `retireable`
**Database Table:** `bopcededpremium`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A BusinessOwners implementation of the RICededPremium delegate

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| BOPCost | ForeignKey | Yes | BOPCost | - | Foreign key target: BOPCost |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| CedingTransactions | BOPCededPremiumTransaction | Child collection |
| CedingHistory | BOPCededPremiumHistory | Child collection |

---

### Entity: BOPCededPremiumHistory

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BOPCededPremiumHistory.eti`
**Entity Type:** `retireable`
**Database Table:** `bopcededpremiumhistory`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A BusinessOwners implementation of the RICededPremiumHistory delegate

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| BOPCededPremium | ForeignKey | Yes | BOPCededPremium | - | Foreign key target: BOPCededPremium |

---

### Entity: BOPCededPremiumTransaction

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BOPCededPremiumTransaction.eti`
**Entity Type:** `retireable`
**Database Table:** `bopcededpremiumtransaction`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A BusinessOwners implementation of the RICededPremiumTransaction delegate

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| BOPCededPremium | ForeignKey | Yes | BOPCededPremium | - | Foreign key target: BOPCededPremium |
| BOPCededPremiumHistory | ForeignKey | Yes | BOPCededPremiumHistory | - | Foreign key target: BOPCededPremiumHistory |

---

### Entity: BOPClassCode

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BOPClassCode.eti`
**Entity Type:** `retireable`
**Database Table:** `bopclasscode`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Business owners building class codes.  Premium calculations are driven by class codes and both premium and losses are reported by class codes to rating bureaus.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| BOPLiabilityClassGroup | varchar | No | - | - | A value required by the rating engine for BOP. |
| BOPPropertyRateNumber | varchar | No | - | - | A value required by the rating engine for BOP. |
| Classification | mediumtext | No | - | - | The Classification of the code (essentially a short description) |
| Basis | ForeignKey | No | ClassCodeBasis | - | Rating basis for this class code. |

---

### Entity: BOPCovBuildingCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BOPCovBuildingCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\BOPCovBuildingCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** BOPCovCost
**Effective-Dated Container Branch Field:** N/A
**Description:** A taxable unit of price for a period of time, not to be broken up any further, for a Business Owners building coverage

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BOPBuilding | ForeignKey | Yes | BOPBuilding | - | Foreign key target: BOPBuilding |

---

### Entity: BOPCovCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BOPCovCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\BOPCovCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** BOPCoveragePremium
**Effective-Dated Container Branch Field:** N/A
**Description:** A taxable unit of price for a period of time, not to be broken up any further, for a Business Owners coverage

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BusinessOwnersCov | ForeignKey | Yes | BusinessOwnersCov | - | Foreign key target: BusinessOwnersCov |

---

### Entity: BOPCoveragePremium

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BOPCoveragePremium.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** BOPGeneralPremium
**Effective-Dated Container Branch Field:** N/A
**Description:** A taxable unit of price for a period of time, not to be broken up any further, for a Business Owners coverage

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: BOPGeneralPremium

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BOPGeneralPremium.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** BOPTaxable
**Effective-Dated Container Branch Field:** N/A
**Description:** A taxable unit of price for a period of time, not to be broken up any further, for Business Owners

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: BOPLocationCov

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BOPLocationCov.eti`
**Entity Type:** `effdated`
**Database Table:** `boplocationcov`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A location-level coverage for Business Owners

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BooleanTerm1 | bit | No | - | - | boolean cov term field |
| BooleanTerm1Avl | bit | No | - | - | whether or not the BooleanTerm1 field was available the last time availability was checked |
| BooleanTerm2 | bit | No | - | - | boolean cov term field |
| BooleanTerm2Avl | bit | No | - | - | whether or not the BooleanTerm2 field was available the last time availability was checked |
| BooleanTerm3 | bit | No | - | - | boolean cov term field |
| BooleanTerm3Avl | bit | No | - | - | whether or not the BooleanTerm3 field was available the last time availability was checked |
| ChoiceTerm1 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm1Avl | bit | No | - | - | whether or not the ChoiceTerm1 field was available the last time availability was checked |
| ChoiceTerm2 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm2Avl | bit | No | - | - | whether or not the ChoiceTerm2 field was available the last time availability was checked |
| DirectTerm1 | decimal | No | - | - | direct cov term field |
| DirectTerm1Avl | bit | No | - | - | whether or not the DirectTerm1 field was available the last time availability was checked |
| DirectTerm2 | decimal | No | - | - | direct cov term field |
| DirectTerm2Avl | bit | No | - | - | whether or not the DirectTerm2 field was available the last time availability was checked |
| StringTerm1 | shorttext | No | - | - | string cov term field |
| StringTerm1Avl | bit | No | - | - | whether or not the StringTerm1 field was available the last time availability was checked |
| BOPLocation | ForeignKey | No | BOPLocation | - | Foreign key target: BOPLocation |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Costs | BOPLocationCovCost | Child collection |

---

### Entity: BOPLocationCovCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BOPLocationCovCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\BOPLocationCovCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** BOPCoveragePremium
**Effective-Dated Container Branch Field:** N/A
**Description:** A taxable unit of price for a period of time, not to be broken up any further, for a Business Owners location coverage

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BOPLocationCov | ForeignKey | Yes | BOPLocationCov | - | Foreign key target: BOPLocationCov |

---

### Entity: BOPMinPremiumCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BOPMinPremiumCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\BOPMinPremiumCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** BOPTaxable
**Effective-Dated Container Branch Field:** N/A
**Description:** The minimum premium adjustment cost for the Business Owners line

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: BOPModifier

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BOPModifier.eti`
**Entity Type:** `effdated`
**Database Table:** `bopmodifier`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A line-level modifier for Business Owners

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BOPLine | ForeignKey | Yes | BusinessOwnersLine | - | Foreign key target: BusinessOwnersLine |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| BOPRateFactors | BOPRateFactor | Individual components of the rating factor |

---

### Entity: BOPMoneySecCovCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BOPMoneySecCovCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\BOPMoneySecCovCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** BOPLocationCovCost
**Effective-Dated Container Branch Field:** N/A
**Description:** A unit of price for a period of time, not to be broken up any further, for Business Owners money and securities coverage

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| OnPremises | bit | No | - | - | Whether the money covered is on the premises or off it |

---

### Entity: BOPPolicyContactRole

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BOPPolicyContactRole.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PolicyContactRole
**Effective-Dated Container Branch Field:** N/A
**Description:** A PolicyContactRole specific to a BusinessOwners policy line.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BusinessOwnersLine | ForeignKey | No | BusinessOwnersLine | - | The Business Owners policy line this contact role is associated with. |

---

### Entity: BOPRateFactor

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BOPRateFactor.eti`
**Entity Type:** `effdated`
**Database Table:** `bopratefactor`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A rate factor is a risk characteristic and its associated numeric value which might have an impact on premium. As used here rate factors are applied to base premium rather than rates. A common example of Rate Factors are the components of IRPM (individual risk premium modifier).

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BOPModifier | ForeignKey | Yes | BOPModifier | - | Foreign key target: BOPModifier |

---

### Entity: BOPScheduledEquipment

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BOPScheduledEquipment.eti`
**Entity Type:** `effdated`
**Database Table:** `bopscheduledequipment`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** BOP Location

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| Description | shorttext | No | - | - | Description |
| EquipmentValue | integer | No | - | - | Equipment Value |
| SerialNumber | varchar | No | - | - | Equipment Identifier. |
| EquipmentNumber | integer | No | - | - | The index of this equipment |
| BOPLine | ForeignKey | Yes | BusinessOwnersLine | - | Foreign key target: BusinessOwnersLine |

---

### Entity: BOPTaxable

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BOPTaxable.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\BOPTaxable.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** BOPCost
**Effective-Dated Container Branch Field:** N/A
**Description:** A taxable unit of price for a period of time, not to be broken up any further, for Business Owners

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: BOPTaxCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BOPTaxCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\BOPTaxCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** BOPCost
**Effective-Dated Container Branch Field:** N/A
**Description:** State tax costs for Business Owners

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| TaxState | TypeKey | Yes | - | Jurisdiction | Jurisdiction tax that applies Codes (98 total): [AK, AL, AR, AZ, CA, ...] |

---

### Entity: BOPTransaction

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BOPTransaction.eti`
**Entity Type:** `effdated`
**Database Table:** `boptransaction`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A transaction for the Business Owners line

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BOPCost | ForeignKey | Yes | BOPCost | - | The cost this transaction modifies. |

---

### Entity: CPBlanket

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\CPBlanket.eti`
**Entity Type:** `effdated`
**Database Table:** `cpblanket`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Commercial Property Blanket for combining CP coverages into a blanket

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| CPBlanketNum | integer | Yes | - | - | The blanket number |
| CPBlanketDescription | shorttext | No | - | - | Description of the blanket |
| CPBuildingCovName | shorttext | No | - | - | Name of the Building Coverage Pattern when BlanketType is single coverage |
| CPLocation | ForeignKey | No | CPLocation | - | Foreign key target: CPLocation |
| CPLine | ForeignKey | Yes | CommercialPropertyLine | - | Foreign key target: CommercialPropertyLine |
| BlanketType | TypeKey | Yes | - | BlanketType | Identifies the combinations used in the blanket Codes (9 total): [decline, build, bus, busbuild, location, ...] |
| BlanketGroupType | TypeKey | Yes | - | BlanketGroupType | For Direct Loss or Time Element. Codes: [TimeElement, DirectLoss] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Coverages | CPBlanketCov | Blanket coverages that apply directly to this blanket. |
| BuildingCoverages | CPBuildingCov | Building coverages that apply directly to this blanket. |

---

### Entity: CPBlanketCov

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\CPBlanketCov.eti`
**Entity Type:** `effdated`
**Database Table:** `cpblanketcov`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Blanket Coverage

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| DirectTerm1 | decimal | No | - | - | direct cov term field |
| DirectTerm1Avl | bit | No | - | - | whether or not the DirectTerm1 field was available the last time availability was checked |
| ChoiceTerm1 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm1Avl | bit | No | - | - | whether or not the ChoiceTerm1 field was available the last time availability was checked |
| ChoiceTerm2 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm2Avl | bit | No | - | - | whether or not the ChoiceTerm2 field was available the last time availability was checked |
| CPBlanket | ForeignKey | Yes | CPBlanket | - | Foreign key target: CPBlanket |

---

### Entity: CPBldgAddlInterest

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\CPBldgAddlInterest.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** AddlInterestDetail
**Effective-Dated Container Branch Field:** N/A
**Description:** An additional interest on a building

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| CPBuilding | ForeignKey | Yes | CPBuilding | - | Foreign key target: CPBuilding |

---

### Entity: CPBuildingCov

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\CPBuildingCov.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\CPBuildingCov.etx`
**Entity Type:** `effdated`
**Database Table:** `cpbuildingcov`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A building-level coverage for Commercial Property

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BooleanTerm1 | bit | No | - | - | boolean cov term field |
| BooleanTerm1Avl | bit | No | - | - | whether or not the BooleanTerm1 field was available the last time availability was checked |
| BooleanTerm2 | bit | No | - | - | boolean cov term field |
| BooleanTerm2Avl | bit | No | - | - | whether or not the BooleanTerm2 field was available the last time availability was checked |
| BooleanTerm3 | bit | No | - | - | boolean cov term field |
| BooleanTerm3Avl | bit | No | - | - | whether or not the BooleanTerm3 field was available the last time availability was checked |
| ChoiceTerm1 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm1Avl | bit | No | - | - | whether or not the ChoiceTerm1 field was available the last time availability was checked |
| ChoiceTerm2 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm2Avl | bit | No | - | - | whether or not the ChoiceTerm2 field was available the last time availability was checked |
| ChoiceTerm3 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm3Avl | bit | No | - | - | whether or not the ChoiceTerm3 field was available the last time availability was checked |
| ChoiceTerm4 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm4Avl | bit | No | - | - | whether or not the ChoiceTerm4 field was available the last time availability was checked |
| ChoiceTerm5 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm5Avl | bit | No | - | - | whether or not the ChoiceTerm5 field was available the last time availability was checked |
| ChoiceTerm6 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm6Avl | bit | No | - | - | whether or not the ChoiceTerm6 field was available the last time availability was checked |
| ChoiceTerm7 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm7Avl | bit | No | - | - | whether or not the ChoiceTerm7 field was available the last time availability was checked |
| ChoiceTerm8 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm8Avl | bit | No | - | - | whether or not the ChoiceTerm8 field was available the last time availability was checked |
| DateTerm1 | datetime | No | - | - | datetime cov term field |
| DateTerm1Avl | bit | No | - | - | whether or not the DateTerm1 field was available the last time availability was checked |
| DateTerm2 | datetime | No | - | - | datetime cov term field |
| DateTerm2Avl | bit | No | - | - | whether or not the DateTerm2 field was available the last time availability was checked |
| DirectTerm1 | decimal | No | - | - | direct cov term field |
| DirectTerm1Avl | bit | No | - | - | whether or not the DirectTerm1 field was available the last time availability was checked |
| DirectTerm2 | decimal | No | - | - | direct cov term field |
| DirectTerm2Avl | bit | No | - | - | whether or not the DirectTerm2 field was available the last time availability was checked |
| DirectTerm3 | decimal | No | - | - | direct cov term field |
| DirectTerm3Avl | bit | No | - | - | whether or not the DirectTerm3 field was available the last time availability was checked |
| CPBuilding | ForeignKey | No | CPBuilding | - | Foreign key target: CPBuilding |
| CPBlanket | ForeignKey | No | CPBlanket | - | Foreign key target: CPBlanket |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Costs | CPBuildingCovCost | Child collection |

---

### Entity: CPBuildingCovBroadCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\CPBuildingCovBroadCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\CPBuildingCovBroadCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** CPBuildingCovCost
**Effective-Dated Container Branch Field:** N/A
**Description:** A cost for a CPBuildingCov using Broad rates.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: CPBuildingCovCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\CPBuildingCovCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\CPBuildingCovCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** CPCost
**Effective-Dated Container Branch Field:** N/A
**Description:** A unit of price for a period of time, not to be broken up any further, for a Commercial Property building coverage

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| CPBuildingCov | ForeignKey | Yes | CPBuildingCov | - | Foreign key target: CPBuildingCov |

---

### Entity: CPBuildingCovGrp1Cost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\CPBuildingCovGrp1Cost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\CPBuildingCovGrp1Cost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** CPBuildingCovCost
**Effective-Dated Container Branch Field:** N/A
**Description:** A cost for a CPBuildingCov using Group I rates.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: CPBuildingCovGrp2Cost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\CPBuildingCovGrp2Cost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\CPBuildingCovGrp2Cost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** CPBuildingCovCost
**Effective-Dated Container Branch Field:** N/A
**Description:** A cost for a CPBuildingCov using Group II rates.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: CPBuildingCovLookup

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\CPBuildingCovLookup.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** CoverageLookup
**Effective-Dated Container Branch Field:** N/A
**Description:** CPBuilding Coverage Lookup Table.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| CoverageForm | TypeKey | No | - | CoverageForm | Codes: [BPP, CondoAssoc, CondoUnitOwners] |

---

### Entity: CPBuildingCovSpecCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\CPBuildingCovSpecCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\CPBuildingCovSpecCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** CPBuildingCovCost
**Effective-Dated Container Branch Field:** N/A
**Description:** A cost for a CPBuildingCov using Special rates.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: CPCededPremium

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\CPCededPremium.eti`
**Entity Type:** `retireable`
**Database Table:** `cpcededpremium`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A CommercialProperty implementation of the RICededPremium delegate

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| CPCost | ForeignKey | Yes | CPCost | - | Foreign key target: CPCost |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| CedingTransactions | CPCededPremiumTransaction | Child collection |
| CedingHistory | CPCededPremiumHistory | Child collection |

---

### Entity: CPCededPremiumHistory

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\CPCededPremiumHistory.eti`
**Entity Type:** `retireable`
**Database Table:** `cpcededpremiumhistory`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A CommercialProperty implementation of the RICededPremiumHistory delegate

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| CPCededPremium | ForeignKey | Yes | CPCededPremium | - | Foreign key target: CPCededPremium |

---

### Entity: CPCededPremiumTransaction

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\CPCededPremiumTransaction.eti`
**Entity Type:** `retireable`
**Database Table:** `cpcededpremiumtransaction`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A CommercialProperty implementation of the RICededPremiumTransaction delegate

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| CPCededPremium | ForeignKey | Yes | CPCededPremium | - | Foreign key target: CPCededPremium |
| CPCededPremiumHistory | ForeignKey | Yes | CPCededPremiumHistory | - | Foreign key target: CPCededPremiumHistory |

---

### Entity: CPClassCode

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\CPClassCode.eti`
**Entity Type:** `retireable`
**Database Table:** `cpclasscode`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Commercial property building class codes.  Premium calculations are driven by class codes and both premium and losses are reported by class codes to rating bureaus.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Classification | mediumtext | No | - | - | The Classification of the code (essentially a short description) |

---

### Entity: CPCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\CPCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\CPCost.etx`
**Entity Type:** `effdated`
**Database Table:** `cpcost`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A CommercialProperty unit of price for a period of time, not to be broken up any further

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| CommercialPropertyLine | ForeignKey | Yes | CommercialPropertyLine | - | Foreign key target: CommercialPropertyLine |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Transactions | CPTransaction | Child collection |

---

### Entity: CPLocationCov

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\CPLocationCov.eti`
**Entity Type:** `effdated`
**Database Table:** `cplocationcov`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A location-level coverage for Commercial Property

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| ChoiceTerm1 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm1Avl | bit | No | - | - | whether or not the ChoiceTerm1 field was available the last time availability was checked |
| CPLocation | ForeignKey | No | CPLocation | - | Foreign key target: CPLocation |

---

### Entity: CPModifier

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\CPModifier.eti`
**Entity Type:** `effdated`
**Database Table:** `cpmodifier`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A line-level modifier for Commercial Property

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| CPLine | ForeignKey | Yes | CommercialPropertyLine | - | Foreign key target: CommercialPropertyLine |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| CPRateFactors | CPRateFactor | Individual components of the rating factor |

---

### Entity: CPPolicyContactRole

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\CPPolicyContactRole.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PolicyContactRole
**Effective-Dated Container Branch Field:** N/A
**Description:** A PolicyContactRole specific to a CommercialProperty policy line.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| CommercialPropertyLine | ForeignKey | No | CommercialPropertyLine | - | The Commercial Property policy line this contact role is associated with. |

---

### Entity: CPRateFactor

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\CPRateFactor.eti`
**Entity Type:** `effdated`
**Database Table:** `cpratefactor`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A rate factor is a risk characteristic and its associated numeric value which might have an impact on premium. As used here rate factors are applied to base premium rather than rates. A common example of Rate Factors are the components of IRPM (individual risk premium modifier).

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| CPModifier | ForeignKey | Yes | CPModifier | - | Foreign key target: CPModifier |

---

### Entity: CPStateTaxCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\CPStateTaxCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\CPStateTaxCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** CPCost
**Effective-Dated Container Branch Field:** N/A
**Description:** State tax costs for Commercial Property

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| TaxState | TypeKey | Yes | - | Jurisdiction | Jurisdiction tax that applies Codes (98 total): [AK, AL, AR, AZ, CA, ...] |

---

### Entity: CPTransaction

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\CPTransaction.eti`
**Entity Type:** `effdated`
**Database Table:** `cptransaction`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A transaction for the Commercial Property line

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| CPCost | ForeignKey | Yes | CPCost | - | The cost this transaction modifies. |

---

### Entity: GLAddlInsuredCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\GLAddlInsuredCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\GLAddlInsuredCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** GLCost
**Effective-Dated Container Branch Field:** N/A
**Description:** The cost for an additional insured.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| AdditionalInsured | ForeignKey | Yes | PolicyAddlInsured | - | Foreign key target: PolicyAddlInsured |

---

### Entity: GLCededPremium

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\GLCededPremium.eti`
**Entity Type:** `retireable`
**Database Table:** `glcededpremium`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A GeneralLiability implementation of the RICededPremium delegate

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| GLCost | ForeignKey | Yes | GLCost | - | Foreign key target: GLCost |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| CedingTransactions | GLCededPremiumTransaction | Child collection |
| CedingHistory | GLCededPremiumHistory | Child collection |

---

### Entity: GLCededPremiumHistory

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\GLCededPremiumHistory.eti`
**Entity Type:** `retireable`
**Database Table:** `glcededpremiumhistory`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A GeneralLiability implementation of the RICededPremiumHistory delegate

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| GLCededPremium | ForeignKey | Yes | GLCededPremium | - | Foreign key target: GLCededPremium |

---

### Entity: GLCededPremiumTransaction

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\GLCededPremiumTransaction.eti`
**Entity Type:** `retireable`
**Database Table:** `glcededpremiumtransaction`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A GeneralLiability implementation of the RICededPremiumTransaction delegate

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| GLCededPremium | ForeignKey | Yes | GLCededPremium | - | Foreign key target: GLCededPremium |
| GLCededPremiumHistory | ForeignKey | Yes | GLCededPremiumHistory | - | Foreign key target: GLCededPremiumHistory |

---

### Entity: GLClassCode

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\GLClassCode.eti`
**Entity Type:** `retireable`
**Database Table:** `glclasscode`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** General liability class codes.  Premium calculations are driven by class codes and both premium and losses are reported by class codes to rating bureaus.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Classification | mediumtext | No | - | - | The Classification of the code (essentially a short description) |
| Code | shorttext | Yes | - | - | The Class Code for a line of insurance |
| Basis | ForeignKey | No | ClassCodeBasis | - | Rating basis for this class code. |

---

### Entity: GLCovCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\GLCovCost.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** GLCost
**Effective-Dated Container Branch Field:** N/A
**Description:** The cost for a general liability coverage

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| GeneralLiabilityCov | ForeignKey | Yes | GeneralLiabilityCov | - | Foreign key target: GeneralLiabilityCov |

---

### Entity: GLCovExposureCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\GLCovExposureCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\GLCovExposureCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** GLCovCost
**Effective-Dated Container Branch Field:** N/A
**Description:** The cost for a GeneralLiabilityCov on a particular GLExposure.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| GLExposure | ForeignKey | Yes | GLExposure | - | Foreign key target: GLExposure |

---

### Entity: GLExposure

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\GLExposure.eti`
**Entity Type:** `effdated`
**Database Table:** `glexposure`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** An exposure that can be covered.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| ScalableBasisAmount | nonnegativeinteger | No | - | - | Basis amount of exposure if it's a scalable amount |
| FixedBasisAmount | positiveinteger | No | - | - | Basis amount of exposure if it's not a scalable amount |
| Description | shorttext | No | - | - | Description of exposure |
| AuditedBasis | positiveinteger | No | - | - | The basis amount deteremined by an auditor. |
| ClassCodeInternal | ForeignKey | No | GLClassCode | - | Class code of exposure |
| GLLine | ForeignKey | Yes | GeneralLiabilityLine | - | Foreign key target: GeneralLiabilityLine |
| Location | ForeignKey | Yes | PolicyLocation | - | Location of exposure |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Costs | GLCovExposureCost | Child collection |

---

### Entity: GLLineCovCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\GLLineCovCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\GLLineCovCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** GLCovCost
**Effective-Dated Container Branch Field:** N/A
**Description:** Concrete subtype of GLCovCost representing costs for line-level coverages.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: GLLineSchCovItemCov

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\GLLineSchCovItemCov.eti`
**Entity Type:** `effdated`
**Database Table:** `gllineschcovitemcov`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** GL Line level coverage scheduled item with coverage terms

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| GLLineScheduleCovItem | ForeignKey | Yes | GLLineScheduleCovItem | - | Foreign key target: GLLineScheduleCovItem |

---

### Entity: GLLineScheduleCond

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\GLLineScheduleCond.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** GeneralLiabilityCond
**Effective-Dated Container Branch Field:** N/A
**Description:** GL Line Condition with a schedule

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| GLLineScheduledItems | GLLineScheduleCondItem | Scheduled Items |

---

### Entity: GLLineScheduleCondItem

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\GLLineScheduleCondItem.eti`
**Entity Type:** `effdated`
**Database Table:** `gllineschedconditem`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** GL Line level Condition scheduled item

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| Schedule | ForeignKey | Yes | GLLineScheduleCond | - | Foreign key target: GLLineScheduleCond |

---

### Entity: GLLineScheduleCov

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\GLLineScheduleCov.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** GeneralLiabilityCov
**Effective-Dated Container Branch Field:** N/A
**Description:** GL Line coverage with a schedule

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| GLLineScheduledItems | GLLineScheduleCovItem | Scheduled Items |

---

### Entity: GLLineScheduleCovItem

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\GLLineScheduleCovItem.eti`
**Entity Type:** `effdated`
**Database Table:** `gllineschedcovitem`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** GL Line level coverage scheduled item

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| Schedule | ForeignKey | Yes | GLLineScheduleCov | - | Foreign key target: GLLineScheduleCov |
| ScheduledItemClause | OneToOne | No | GLLineSchCovItemCov | - | The coverage that applies to this scheduled item. |

---

### Entity: GLLineScheduleExcl

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\GLLineScheduleExcl.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** GeneralLiabilityExcl
**Effective-Dated Container Branch Field:** N/A
**Description:** GL Line exclusion with a schedule

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| GLLineScheduledItems | GLLineScheduleExclItem | Scheduled Items |

---

### Entity: GLLineScheduleExclItem

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\GLLineScheduleExclItem.eti`
**Entity Type:** `effdated`
**Database Table:** `gllineschedexclitem`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** GL Line level exclusion scheduled item

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| Schedule | ForeignKey | Yes | GLLineScheduleExcl | - | Foreign key target: GLLineScheduleExcl |

---

### Entity: GLModifier

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\GLModifier.eti`
**Entity Type:** `effdated`
**Database Table:** `glmodifier`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A line-level modifier for General Liability

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| GLLine | ForeignKey | Yes | GeneralLiabilityLine | - | Foreign key target: GeneralLiabilityLine |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| GLRateFactors | GLRateFactor | Individual components of the rating factor |

---

### Entity: GlobalAddress

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\GlobalAddress.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\GlobalAddress.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: GlobalContactName

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\GlobalContactName.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\GlobalContactName.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: GlobalPersonName

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\GlobalPersonName.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\GlobalPersonName.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: GLPolicyContactRole

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\GLPolicyContactRole.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PolicyContactRole
**Effective-Dated Container Branch Field:** N/A
**Description:** A PolicyContactRole specific to a GeneralLiability policy line.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| GeneralLiabilityLine | ForeignKey | No | GeneralLiabilityLine | - | The General Liability policy line this contact role is associated with. |

---

### Entity: GLRateFactor

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\GLRateFactor.eti`
**Entity Type:** `effdated`
**Database Table:** `glratefactor`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A rate factor is a risk characteristic and its associated numeric value which might have an impact on premium. As used here rate factors are applied to base premium rather than rates. A common example of Rate Factors are the components of IRPM (individual risk premium modifier).

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| GLModifier | ForeignKey | Yes | GLModifier | - | Foreign key target: GLModifier |

---

### Entity: GLScheduledItem

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\GLScheduledItem.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: GLStateCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\GLStateCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\GLStateCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** GLCost
**Effective-Dated Container Branch Field:** N/A
**Description:** A cost that is attached to a specific state.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| GLState | TypeKey | No | - | Jurisdiction | The jurisdiction that is covered Codes (98 total): [AK, AL, AR, AZ, CA, ...] |
| StateCostType | TypeKey | No | - | GLStateCostType | The name of the specific cost Codes: [TERROR, TAX] |

---

### Entity: GLTransaction

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\GLTransaction.eti`
**Entity Type:** `effdated`
**Database Table:** `gltransaction`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A transaction for the General Liability line

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| GLCost | ForeignKey | Yes | GLCost | - | The cost this transaction modifies. |

---

### Entity: HOPConditionLookup

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPConditionLookup.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** ConditionLookup
**Effective-Dated Container Branch Field:** N/A
**Description:** An availability lookup for HOP condition patterns.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| CoveragePartType | TypeKey | No | - | CoveragePartType | - |
| HOPCoverageForm | TypeKey | No | - | HOPCoverageForm | Codes: [ho2, ho3, ho5, ho4, ho6] |

---

### Entity: HOPCoverageLookup

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPCoverageLookup.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** CoverageLookup
**Effective-Dated Container Branch Field:** N/A
**Description:** An availability lookup for HOP coverage patterns.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| CoveragePartType | TypeKey | No | - | CoveragePartType | - |
| HOPCoverageForm | TypeKey | No | - | HOPCoverageForm | Codes: [ho2, ho3, ho5, ho4, ho6] |

---

### Entity: HOPCoveragePartCond

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPCoveragePartCond.eti`
**Entity Type:** `effdated`
**Database Table:** `hopcoveragepartcond`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Conditions directly attached to each HOPCoveragePart2

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BooleanTerm1 | bit | No | - | - | boolean cov term field |
| BooleanTerm1Avl | bit | No | - | - | whether or not the BooleanTerm1 field was available the last time availability was checked |
| BooleanTerm2 | bit | No | - | - | boolean cov term field |
| BooleanTerm2Avl | bit | No | - | - | whether or not the BooleanTerm2 field was available the last time availability was checked |
| BooleanTerm3 | bit | No | - | - | boolean cov term field |
| BooleanTerm3Avl | bit | No | - | - | whether or not the BooleanTerm3 field was available the last time availability was checked |
| ChoiceTerm1 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm1Avl | bit | No | - | - | whether or not the ChoiceTerm1 field was available the last time availability was checked |
| ChoiceTerm2 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm2Avl | bit | No | - | - | whether or not the ChoiceTerm2 field was available the last time availability was checked |
| ChoiceTerm3 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm3Avl | bit | No | - | - | whether or not the ChoiceTerm3 field was available the last time availability was checked |
| ChoiceTerm4 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm4Avl | bit | No | - | - | whether or not the ChoiceTerm4 field was available the last time availability was checked |
| ChoiceTerm5 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm5Avl | bit | No | - | - | whether or not the ChoiceTerm5 field was available the last time availability was checked |
| DateTerm1 | datetime | No | - | - | datetime cov term field |
| DateTerm1Avl | bit | No | - | - | whether or not the DateTerm1 field was available the last time availability was checked |
| DateTerm2 | datetime | No | - | - | datetime cov term field |
| DateTerm2Avl | bit | No | - | - | whether or not the DateTerm2 field was available the last time availability was checked |
| DirectTerm1 | decimal | No | - | - | direct cov term field |
| DirectTerm1Avl | bit | No | - | - | whether or not the DirectTerm1 field was available the last time availability was checked |
| DirectTerm2 | decimal | No | - | - | direct cov term field |
| DirectTerm2Avl | bit | No | - | - | whether or not the DirectTerm2 field was available the last time availability was checked |
| DirectTerm3 | decimal | No | - | - | direct cov term field |
| DirectTerm3Avl | bit | No | - | - | whether or not the DirectTerm3 field was available the last time availability was checked |
| HOPCoveragePart | ForeignKey | Yes | HOPCoveragePart | - | Foreign key target: HOPCoveragePart |

---

### Entity: HOPCoveragePartExcl

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPCoveragePartExcl.eti`
**Entity Type:** `effdated`
**Database Table:** `hopcoveragepartexcl`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Exclusions directly attached to each HOPCoveragePart

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BooleanTerm1 | bit | No | - | - | boolean cov term field |
| BooleanTerm1Avl | bit | No | - | - | whether or not the BooleanTerm1 field was available the last time availability was checked |
| BooleanTerm2 | bit | No | - | - | boolean cov term field |
| BooleanTerm2Avl | bit | No | - | - | whether or not the BooleanTerm2 field was available the last time availability was checked |
| BooleanTerm3 | bit | No | - | - | boolean cov term field |
| BooleanTerm3Avl | bit | No | - | - | whether or not the BooleanTerm3 field was available the last time availability was checked |
| ChoiceTerm1 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm1Avl | bit | No | - | - | whether or not the ChoiceTerm1 field was available the last time availability was checked |
| ChoiceTerm2 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm2Avl | bit | No | - | - | whether or not the ChoiceTerm2 field was available the last time availability was checked |
| ChoiceTerm3 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm3Avl | bit | No | - | - | whether or not the ChoiceTerm3 field was available the last time availability was checked |
| ChoiceTerm4 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm4Avl | bit | No | - | - | whether or not the ChoiceTerm4 field was available the last time availability was checked |
| ChoiceTerm5 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm5Avl | bit | No | - | - | whether or not the ChoiceTerm5 field was available the last time availability was checked |
| DateTerm1 | datetime | No | - | - | datetime cov term field |
| DateTerm1Avl | bit | No | - | - | whether or not the DateTerm1 field was available the last time availability was checked |
| DateTerm2 | datetime | No | - | - | datetime cov term field |
| DateTerm2Avl | bit | No | - | - | whether or not the DateTerm2 field was available the last time availability was checked |
| DirectTerm1 | decimal | No | - | - | direct cov term field |
| DirectTerm1Avl | bit | No | - | - | whether or not the DirectTerm1 field was available the last time availability was checked |
| DirectTerm2 | decimal | No | - | - | direct cov term field |
| DirectTerm2Avl | bit | No | - | - | whether or not the DirectTerm2 field was available the last time availability was checked |
| DirectTerm3 | decimal | No | - | - | direct cov term field |
| DirectTerm3Avl | bit | No | - | - | whether or not the DirectTerm3 field was available the last time availability was checked |
| HOPCoveragePart | ForeignKey | Yes | HOPCoveragePart | - | Foreign key target: HOPCoveragePart |

---

### Entity: HOPCoveragePartMod

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPCoveragePartMod.eti`
**Entity Type:** `effdated`
**Database Table:** `hopcoveragepartmod`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A modifier for HOPCoveragePart

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| HOPCoveragePart | ForeignKey | Yes | HOPCoveragePart | - | Foreign key target: HOPCoveragePart |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| HOPCoveragePartRateFactors | HOPCoveragePartRF | Individual components of the rating factor |

---

### Entity: HOPCoveragePartRF

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPCoveragePartRF.eti`
**Entity Type:** `effdated`
**Database Table:** `hopcoveragepartrf`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A rate factor is a risk characteristic and its associated numeric value which might have an impact on premium. As used here rate factors are applied to base premium rather than rates. A common example of Rate Factors are the components of IRPM (individual risk premium modifier).

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| HOPCoveragePartModifier | ForeignKey | Yes | HOPCoveragePartMod | - | Foreign key target: HOPCoveragePartMod |

---

### Entity: HOPCovPartSchCondItem

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPCovPartSchCondItem.eti`
**Entity Type:** `effdated`
**Database Table:** `hopcovpartschconditem`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** HOP coverage-part level condition scheduled item

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| Schedule | ForeignKey | Yes | HOPCovPartScheduleCond | - | Foreign key target: HOPCovPartScheduleCond |
| ScheduledItemClause | OneToOne | No | HOPCovPartSchCondItemCond | - | The condition that applies to this scheduled item |

---

### Entity: HOPCovPartSchCondItemCond

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPCovPartSchCondItemCond.eti`
**Entity Type:** `effdated`
**Database Table:** `hopcovpartschconditemcond`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** HOP coverage-part condition scheduled item with coverage terms

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| HOPCovPartSchCondItem | ForeignKey | Yes | HOPCovPartSchCondItem | - | Foreign key target: HOPCovPartSchCondItem |

---

### Entity: HOPCovPartSchCovItemCov

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPCovPartSchCovItemCov.eti`
**Entity Type:** `effdated`
**Database Table:** `hopcovpartschcovitemcov`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** HOP Coverage Part coverage schedule item with coverage terms

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| HOPCovPartScheduleCovItem | ForeignKey | Yes | HOPCovPartScheduleCovItem | - | Foreign key target: HOPCovPartScheduleCovItem |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| HOPCovPartSchCovItemCovCosts | HOPCovPartSchCovItemCovCost | Child collection |

---

### Entity: HOPCovPartSchCovItemCovCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPCovPartSchCovItemCovCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\HOPCovPartSchCovItemCovCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** HOPCost
**Effective-Dated Container Branch Field:** N/A
**Description:** Cost for HOP Coverage Part coverage schedule items with coverage terms

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| HOPCovPartSchCovItemCov | ForeignKey | Yes | HOPCovPartSchCovItemCov | - | Foreign key target: HOPCovPartSchCovItemCov |

---

### Entity: HOPCovPartScheduleCond

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPCovPartScheduleCond.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** HOPCoveragePartCond
**Effective-Dated Container Branch Field:** N/A
**Description:** HOP Coverage Part condition with a schedule

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| HOPCovPartScheduledItems | HOPCovPartSchCondItem | Scheduled Items |

---

### Entity: HOPCovPartScheduleCov

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPCovPartScheduleCov.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** HOPCoveragePartCov
**Effective-Dated Container Branch Field:** N/A
**Description:** HOP Coverage Part coverage with a schedule

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| HOPCovPartScheduledItems | HOPCovPartScheduleCovItem | Scheduled Items |

---

### Entity: HOPCovPartScheduleCovItem

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPCovPartScheduleCovItem.eti`
**Entity Type:** `effdated`
**Database Table:** `hopcovpartschedulecovitem`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** HOP Coverage Part level coverage schedule item

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| Schedule | ForeignKey | Yes | HOPCovPartScheduleCov | - | Foreign key target: HOPCovPartScheduleCov |
| ScheduledItemClause | OneToOne | No | HOPCovPartSchCovItemCov | - | The coverage that applies to this scheduled item |

---

### Entity: HOPCovPartScheduleExcl

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPCovPartScheduleExcl.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** HOPCoveragePartExcl
**Effective-Dated Container Branch Field:** N/A
**Description:** HOP Coverage Part exclusion with a schedule

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| HOPCovPartScheduledItems | HOPCovPartSchExclItem | Scheduled Items |

---

### Entity: HOPCovPartSchExclItem

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPCovPartSchExclItem.eti`
**Entity Type:** `effdated`
**Database Table:** `hopcovpartschexclitem`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** HOP Coverage Part level exclucion schedule item

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| Schedule | ForeignKey | Yes | HOPCovPartScheduleExcl | - | Foreign key target: HOPCovPartScheduleExcl |
| ScheduledItemClause | OneToOne | No | HOPCovPartSchExclItemExcl | - | The exclusion that applies to this scheduled item |

---

### Entity: HOPCovPartSchExclItemExcl

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPCovPartSchExclItemExcl.eti`
**Entity Type:** `effdated`
**Database Table:** `hopcovpartschexclitemexcl`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** HOP Coverage Part schedule item with coverage terms

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| HOPCovPartSchExclItem | ForeignKey | Yes | HOPCovPartSchExclItem | - | Foreign key target: HOPCovPartSchExclItem |

---

### Entity: HOPCovTermLookup

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPCovTermLookup.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** CovTermLookup
**Effective-Dated Container Branch Field:** N/A
**Description:** An availability lookup for HOP coverage term patterns.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| CoveragePartType | TypeKey | No | - | CoveragePartType | - |
| HOPCoverageForm | TypeKey | No | - | HOPCoverageForm | Codes: [ho2, ho3, ho5, ho4, ho6] |

---

### Entity: HOPCovTermOptLookup

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPCovTermOptLookup.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** CovTermOptLookup
**Effective-Dated Container Branch Field:** N/A
**Description:** An availability lookup for HOP coverage term option patterns.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| CoveragePartType | TypeKey | No | - | CoveragePartType | - |
| HOPCoverageForm | TypeKey | No | - | HOPCoverageForm | Codes: [ho2, ho3, ho5, ho4, ho6] |

---

### Entity: HOPCovTermPackLookup

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPCovTermPackLookup.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** CovTermPackLookup
**Effective-Dated Container Branch Field:** N/A
**Description:** An availability lookup for HOP cov term pack patterns.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| CoveragePartType | TypeKey | No | - | CoveragePartType | - |
| HOPCoverageForm | TypeKey | No | - | HOPCoverageForm | Codes: [ho2, ho3, ho5, ho4, ho6] |

---

### Entity: HOPDwellAddlInterest

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPDwellAddlInterest.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** AddlInterestDetail
**Effective-Dated Container Branch Field:** N/A
**Description:** An additional interest on a homeowner's dwelling

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Description | shorttext | No | - | - | Description of additional interest |
| AddlIntEffDate | datetime | No | - | - | Effective date for additional interest |
| AddlIntExpDate | datetime | No | - | - | Expiration date for additional interest |
| HOPDwelling | ForeignKey | Yes | HOPDwelling | - | Foreign key target: HOPDwelling |

---

### Entity: HOPDwellingCond

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPDwellingCond.eti`
**Entity Type:** `effdated`
**Database Table:** `hopdwellingcond`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Conditions directly attached to each Dwelling

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BooleanTerm1 | bit | No | - | - | boolean cov term field |
| BooleanTerm1Avl | bit | No | - | - | whether or not the BooleanTerm1 field was available the last time availability was checked |
| BooleanTerm2 | bit | No | - | - | boolean cov term field |
| BooleanTerm2Avl | bit | No | - | - | whether or not the BooleanTerm2 field was available the last time availability was checked |
| BooleanTerm3 | bit | No | - | - | boolean cov term field |
| BooleanTerm3Avl | bit | No | - | - | whether or not the BooleanTerm3 field was available the last time availability was checked |
| ChoiceTerm1 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm1Avl | bit | No | - | - | whether or not the ChoiceTerm1 field was available the last time availability was checked |
| ChoiceTerm2 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm2Avl | bit | No | - | - | whether or not the ChoiceTerm2 field was available the last time availability was checked |
| ChoiceTerm3 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm3Avl | bit | No | - | - | whether or not the ChoiceTerm3 field was available the last time availability was checked |
| ChoiceTerm4 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm4Avl | bit | No | - | - | whether or not the ChoiceTerm4 field was available the last time availability was checked |
| ChoiceTerm5 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm5Avl | bit | No | - | - | whether or not the ChoiceTerm5 field was available the last time availability was checked |
| DateTerm1 | datetime | No | - | - | datetime cov term field |
| DateTerm1Avl | bit | No | - | - | whether or not the DateTerm1 field was available the last time availability was checked |
| DateTerm2 | datetime | No | - | - | datetime cov term field |
| DateTerm2Avl | bit | No | - | - | whether or not the DateTerm2 field was available the last time availability was checked |
| DirectTerm1 | decimal | No | - | - | direct cov term field |
| DirectTerm1Avl | bit | No | - | - | whether or not the DirectTerm1 field was available the last time availability was checked |
| DirectTerm2 | decimal | No | - | - | direct cov term field |
| DirectTerm2Avl | bit | No | - | - | whether or not the DirectTerm2 field was available the last time availability was checked |
| DirectTerm3 | decimal | No | - | - | direct cov term field |
| DirectTerm3Avl | bit | No | - | - | whether or not the DirectTerm3 field was available the last time availability was checked |
| HOPDwelling | ForeignKey | Yes | HOPDwelling | - | Foreign key target: HOPDwelling |

---

### Entity: HOPDwellingCovCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPDwellingCovCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\HOPDwellingCovCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** HOPCost
**Effective-Dated Container Branch Field:** N/A
**Description:** Costs for dwelling coverages

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| HOPDwellingCov | ForeignKey | Yes | HOPDwellingCov | - | Foreign key target: HOPDwellingCov |

---

### Entity: HOPDwellingExcl

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPDwellingExcl.eti`
**Entity Type:** `effdated`
**Database Table:** `hopdwellingexcl`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Exclusions directly attached to each Dwelling

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BooleanTerm1 | bit | No | - | - | boolean cov term field |
| BooleanTerm1Avl | bit | No | - | - | whether or not the BooleanTerm1 field was available the last time availability was checked |
| BooleanTerm2 | bit | No | - | - | boolean cov term field |
| BooleanTerm2Avl | bit | No | - | - | whether or not the BooleanTerm2 field was available the last time availability was checked |
| BooleanTerm3 | bit | No | - | - | boolean cov term field |
| BooleanTerm3Avl | bit | No | - | - | whether or not the BooleanTerm3 field was available the last time availability was checked |
| ChoiceTerm1 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm1Avl | bit | No | - | - | whether or not the ChoiceTerm1 field was available the last time availability was checked |
| ChoiceTerm2 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm2Avl | bit | No | - | - | whether or not the ChoiceTerm2 field was available the last time availability was checked |
| ChoiceTerm3 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm3Avl | bit | No | - | - | whether or not the ChoiceTerm3 field was available the last time availability was checked |
| ChoiceTerm4 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm4Avl | bit | No | - | - | whether or not the ChoiceTerm4 field was available the last time availability was checked |
| ChoiceTerm5 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm5Avl | bit | No | - | - | whether or not the ChoiceTerm5 field was available the last time availability was checked |
| DateTerm1 | datetime | No | - | - | datetime cov term field |
| DateTerm1Avl | bit | No | - | - | whether or not the DateTerm1 field was available the last time availability was checked |
| DateTerm2 | datetime | No | - | - | datetime cov term field |
| DateTerm2Avl | bit | No | - | - | whether or not the DateTerm2 field was available the last time availability was checked |
| DirectTerm1 | decimal | No | - | - | direct cov term field |
| DirectTerm1Avl | bit | No | - | - | whether or not the DirectTerm1 field was available the last time availability was checked |
| DirectTerm2 | decimal | No | - | - | direct cov term field |
| DirectTerm2Avl | bit | No | - | - | whether or not the DirectTerm2 field was available the last time availability was checked |
| DirectTerm3 | decimal | No | - | - | direct cov term field |
| DirectTerm3Avl | bit | No | - | - | whether or not the DirectTerm3 field was available the last time availability was checked |
| HOPDwelling | ForeignKey | Yes | HOPDwelling | - | Foreign key target: HOPDwelling |

---

### Entity: HOPDwellingMod

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPDwellingMod.eti`
**Entity Type:** `effdated`
**Database Table:** `hopdwellingmod`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A modifier for Dwelling

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| HOPDwelling | ForeignKey | Yes | HOPDwelling | - | Foreign key target: HOPDwelling |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| HOPDwellingRateFactors | HOPDwellingRF | Individual components of the rating factor |
| HOPDwellingModifierCosts | HOPDwellingModifierCost | Child collection |

---

### Entity: HOPDwellingModifierCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPDwellingModifierCost.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** HOPCost
**Effective-Dated Container Branch Field:** N/A
**Description:** Costs for Dwelling modifiers

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| HOPDwellingMod | ForeignKey | Yes | HOPDwellingMod | - | Foreign key target: HOPDwellingMod |

---

### Entity: HOPDwellingNonPerilCovCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPDwellingNonPerilCovCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\HOPDwellingNonPerilCovCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** HOPDwellingCovCost
**Effective-Dated Container Branch Field:** N/A
**Description:** Non peril coverage cost for dwelling

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: HOPDwellingPerilCovCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPDwellingPerilCovCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\HOPDwellingPerilCovCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** HOPDwellingCovCost
**Effective-Dated Container Branch Field:** N/A
**Description:** Peril coverage cost for dwelling

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| RatedPeril | TypeKey | Yes | - | RatedPeril | Rated peril for dwelling coverage cost Codes (14 total): [fire, lightning, windstormhail, explosion, riotcommotion, ...] |

---

### Entity: HOPDwellingRF

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPDwellingRF.eti`
**Entity Type:** `effdated`
**Database Table:** `hopdwellingrf`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A rate factor is a risk characteristic and its associated numeric value which might have an impact on premium. As used here rate factors are applied to base premium rather than rates. A common example of Rate Factors are the components of IRPM (individual risk premium modifier).

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| HOPDwellingModifier | ForeignKey | Yes | HOPDwellingMod | - | Foreign key target: HOPDwellingMod |

---

### Entity: HOPDwellingScheduleCond

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPDwellingScheduleCond.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** HOPDwellingCond
**Effective-Dated Container Branch Field:** N/A
**Description:** HOP Dwelling condition with a schedule

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| HOPDwellScheduledItems | HOPDwellScheduleCondItem | Scheduled Items |

---

### Entity: HOPDwellingScheduleCov

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPDwellingScheduleCov.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** HOPDwellingCov
**Effective-Dated Container Branch Field:** N/A
**Description:** HOP Dwelling coverage with a schedule

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| HOPDwellScheduledItems | HOPDwellScheduleCovItem | Scheduled Items |

---

### Entity: HOPDwellingScheduleExcl

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPDwellingScheduleExcl.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** HOPDwellingExcl
**Effective-Dated Container Branch Field:** N/A
**Description:** HOP Dwelling exclusion with a schedule

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| HOPDwellScheduledItems | HOPDwellScheduleExclItem | Scheduled Items |

---

### Entity: HOPDwellSchCondItemCond

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPDwellSchCondItemCond.eti`
**Entity Type:** `effdated`
**Database Table:** `hopdwellschconditemcond`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** HOP Dwelling condition scheduled item with coverage terms

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| HOPDwellScheduleCondItem | ForeignKey | Yes | HOPDwellScheduleCondItem | - | Foreign key target: HOPDwellScheduleCondItem |

---

### Entity: HOPDwellSchCovItemCov

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPDwellSchCovItemCov.eti`
**Entity Type:** `effdated`
**Database Table:** `hopdwellschcovitemcov`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** HOP Dwelling coverage scheduled item with coverage terms

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| HOPDwellScheduleCovItem | ForeignKey | Yes | HOPDwellScheduleCovItem | - | Foreign key target: HOPDwellScheduleCovItem |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| HOPDwellSchCovItemCovCosts | HOPDwellSchCovItemCovCost | Child collection |

---

### Entity: HOPDwellSchCovItemCovCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPDwellSchCovItemCovCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\HOPDwellSchCovItemCovCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** HOPCost
**Effective-Dated Container Branch Field:** N/A
**Description:** Cost for HOP Dwelling coverage scheduled items with coverage terms

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| HOPDwellSchCovItemCov | ForeignKey | Yes | HOPDwellSchCovItemCov | - | Foreign key target: HOPDwellSchCovItemCov |

---

### Entity: HOPDwellScheduleCondItem

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPDwellScheduleCondItem.eti`
**Entity Type:** `effdated`
**Database Table:** `hopdwellscheduleconditem`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** HOP Dwelling level condition scheduled item

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| Schedule | ForeignKey | Yes | HOPDwellingScheduleCond | - | Foreign key target: HOPDwellingScheduleCond |
| ScheduledItemClause | OneToOne | No | HOPDwellSchCondItemCond | - | The condition that applies to this scheduled item |

---

### Entity: HOPDwellScheduleCovItem

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPDwellScheduleCovItem.eti`
**Entity Type:** `effdated`
**Database Table:** `hopdwellschedulecovitem`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** HOP Dwelling level coverage scheduled item

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| Schedule | ForeignKey | Yes | HOPDwellingScheduleCov | - | Foreign key target: HOPDwellingScheduleCov |
| ScheduledItemClause | OneToOne | No | HOPDwellSchCovItemCov | - | The coverage that applies to this scheduled item |

---

### Entity: HOPDwellScheduleExclItem

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPDwellScheduleExclItem.eti`
**Entity Type:** `effdated`
**Database Table:** `hopdwellscheduleexclitem`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** HOP Dwelling level exclusion scheduled item

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| Schedule | ForeignKey | Yes | HOPDwellingScheduleExcl | - | Foreign key target: HOPDwellingScheduleExcl |
| ScheduledItemClause | OneToOne | No | HOPDwellSchExclItemExcl | - | The exclusion that applies to this scheduled item |

---

### Entity: HOPDwellSchExclItemExcl

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPDwellSchExclItemExcl.eti`
**Entity Type:** `effdated`
**Database Table:** `hopdwellschexclitemexcl`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** HOP Dwelling exclusion scheduled item with coverage terms

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| HOPDwellScheduleExclItem | ForeignKey | Yes | HOPDwellScheduleExclItem | - | Foreign key target: HOPDwellScheduleExclItem |

---

### Entity: HOPDwellSchNonPerilCovItemCovCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPDwellSchNonPerilCovItemCovCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\HOPDwellSchNonPerilCovItemCovCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** HOPDwellSchCovItemCovCost
**Effective-Dated Container Branch Field:** N/A
**Description:** Non peril coverage cost for HOP Dwelling coverage scheduled items with coverage terms

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: HOPDwellSchPerilCovItemCovCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPDwellSchPerilCovItemCovCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\HOPDwellSchPerilCovItemCovCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** HOPDwellSchCovItemCovCost
**Effective-Dated Container Branch Field:** N/A
**Description:** Peril coverage cost for HOP Dwelling coverage scheduled items with coverage terms

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| RatedPeril | TypeKey | Yes | - | RatedPeril | Rated peril for dwelling coverage scheduled item with coverage terms Codes (14 total): [fire, lightning, windstormhail, explosion, riotcommotion, ...] |

---

### Entity: HOPExclusionLookup

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPExclusionLookup.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** ExclusionLookup
**Effective-Dated Container Branch Field:** N/A
**Description:** An availability lookup for HOP exclusion patterns.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| CoveragePartType | TypeKey | No | - | CoveragePartType | - |
| HOPCoverageForm | TypeKey | No | - | HOPCoverageForm | Codes: [ho2, ho3, ho5, ho4, ho6] |

---

### Entity: HOPLineCond

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPLineCond.eti`
**Entity Type:** `effdated`
**Database Table:** `hoplinecond`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Conditions for the Homeowners line

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BooleanTerm1 | bit | No | - | - | boolean cov term field |
| BooleanTerm1Avl | bit | No | - | - | whether or not the BooleanTerm1 field was available the last time availability was checked |
| BooleanTerm2 | bit | No | - | - | boolean cov term field |
| BooleanTerm2Avl | bit | No | - | - | whether or not the BooleanTerm2 field was available the last time availability was checked |
| BooleanTerm3 | bit | No | - | - | boolean cov term field |
| BooleanTerm3Avl | bit | No | - | - | whether or not the BooleanTerm3 field was available the last time availability was checked |
| ChoiceTerm1 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm1Avl | bit | No | - | - | whether or not the ChoiceTerm1 field was available the last time availability was checked |
| ChoiceTerm2 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm2Avl | bit | No | - | - | whether or not the ChoiceTerm2 field was available the last time availability was checked |
| ChoiceTerm3 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm3Avl | bit | No | - | - | whether or not the ChoiceTerm3 field was available the last time availability was checked |
| ChoiceTerm4 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm4Avl | bit | No | - | - | whether or not the ChoiceTerm4 field was available the last time availability was checked |
| ChoiceTerm5 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm5Avl | bit | No | - | - | whether or not the ChoiceTerm5 field was available the last time availability was checked |
| ChoiceTerm6 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm6Avl | bit | No | - | - | whether or not the ChoiceTerm6 field was available the last time availability was checked |
| ChoiceTerm7 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm7Avl | bit | No | - | - | whether or not the ChoiceTerm7 field was available the last time availability was checked |
| ChoiceTerm8 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm8Avl | bit | No | - | - | whether or not the ChoiceTerm8 field was available the last time availability was checked |
| ChoiceTerm9 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm9Avl | bit | No | - | - | whether or not the ChoiceTerm9 field was available the last time availability was checked |
| ChoiceTerm10 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm10Avl | bit | No | - | - | whether or not the ChoiceTerm10 field was available the last time availability was checked |
| ChoiceTerm11 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm11Avl | bit | No | - | - | whether or not the ChoiceTerm11 field was available the last time availability was checked |
| DateTerm1 | datetime | No | - | - | datetime cov term field |
| DateTerm1Avl | bit | No | - | - | whether or not the DateTerm1 field was available the last time availability was checked |
| DateTerm2 | datetime | No | - | - | datetime cov term field |
| DateTerm2Avl | bit | No | - | - | whether or not the DateTerm2 field was available the last time availability was checked |
| DirectTerm1 | decimal | No | - | - | direct cov term field |
| DirectTerm1Avl | bit | No | - | - | whether or not the DirectTerm1 field was available the last time availability was checked |
| DirectTerm2 | decimal | No | - | - | direct cov term field |
| DirectTerm2Avl | bit | No | - | - | whether or not the DirectTerm2 field was available the last time availability was checked |
| DirectTerm3 | decimal | No | - | - | direct cov term field |
| DirectTerm3Avl | bit | No | - | - | whether or not the DirectTerm3 field was available the last time availability was checked |
| StringTerm1 | shorttext | No | - | - | string cov term field |
| StringTerm1Avl | bit | No | - | - | whether or not the StringTerm1 field was available the last time availability was checked |
| StringTerm2 | shorttext | No | - | - | string cov term field |
| StringTerm2Avl | bit | No | - | - | whether or not the StringTerm2 field was available the last time availability was checked |
| HOPLine | ForeignKey | Yes | HOPLine | - | Foreign key target: HOPLine |

---

### Entity: HOPLineCovCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPLineCovCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\HOPLineCovCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** HOPCost
**Effective-Dated Container Branch Field:** N/A
**Description:** Costs for line coverages

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| HOPLineCov | ForeignKey | Yes | HOPLineCov | - | Foreign key target: HOPLineCov |

---

### Entity: HOPLineExcl

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPLineExcl.eti`
**Entity Type:** `effdated`
**Database Table:** `hoplineexcl`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Exclusions for the Homeowners line

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BooleanTerm1 | bit | No | - | - | boolean cov term field |
| BooleanTerm1Avl | bit | No | - | - | whether or not the BooleanTerm1 field was available the last time availability was checked |
| BooleanTerm2 | bit | No | - | - | boolean cov term field |
| BooleanTerm2Avl | bit | No | - | - | whether or not the BooleanTerm2 field was available the last time availability was checked |
| BooleanTerm3 | bit | No | - | - | boolean cov term field |
| BooleanTerm3Avl | bit | No | - | - | whether or not the BooleanTerm3 field was available the last time availability was checked |
| ChoiceTerm1 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm1Avl | bit | No | - | - | whether or not the ChoiceTerm1 field was available the last time availability was checked |
| ChoiceTerm2 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm2Avl | bit | No | - | - | whether or not the ChoiceTerm2 field was available the last time availability was checked |
| ChoiceTerm3 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm3Avl | bit | No | - | - | whether or not the ChoiceTerm3 field was available the last time availability was checked |
| ChoiceTerm4 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm4Avl | bit | No | - | - | whether or not the ChoiceTerm4 field was available the last time availability was checked |
| ChoiceTerm5 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm5Avl | bit | No | - | - | whether or not the ChoiceTerm5 field was available the last time availability was checked |
| DateTerm1 | datetime | No | - | - | datetime cov term field |
| DateTerm1Avl | bit | No | - | - | whether or not the DateTerm1 field was available the last time availability was checked |
| DateTerm2 | datetime | No | - | - | datetime cov term field |
| DateTerm2Avl | bit | No | - | - | whether or not the DateTerm2 field was available the last time availability was checked |
| DirectTerm1 | decimal | No | - | - | direct cov term field |
| DirectTerm1Avl | bit | No | - | - | whether or not the DirectTerm1 field was available the last time availability was checked |
| DirectTerm2 | decimal | No | - | - | direct cov term field |
| DirectTerm2Avl | bit | No | - | - | whether or not the DirectTerm2 field was available the last time availability was checked |
| DirectTerm3 | decimal | No | - | - | direct cov term field |
| DirectTerm3Avl | bit | No | - | - | whether or not the DirectTerm3 field was available the last time availability was checked |
| HOPLine | ForeignKey | Yes | HOPLine | - | Foreign key target: HOPLine |

---

### Entity: HOPLineMod

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPLineMod.eti`
**Entity Type:** `effdated`
**Database Table:** `hoplinemod`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A modifier for Homeowners

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| HOPLine | ForeignKey | Yes | HOPLine | - | Foreign key target: HOPLine |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| HOPLineRateFactors | HOPLineRF | Individual components of the rating factor |
| HOPLineModifierCosts | HOPLineModifierCost | Child collection |

---

### Entity: HOPLineModifierCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPLineModifierCost.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** HOPCost
**Effective-Dated Container Branch Field:** N/A
**Description:** Costs for HOP Line modifiers

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| HOPLineMod | ForeignKey | Yes | HOPLineMod | - | Foreign key target: HOPLineMod |

---

### Entity: HOPLineRF

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPLineRF.eti`
**Entity Type:** `effdated`
**Database Table:** `hoplinerf`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A rate factor is a risk characteristic and its associated numeric value which might have an impact on premium. As used here rate factors are applied to base premium rather than rates. A common example of Rate Factors are the components of IRPM (individual risk premium modifier).

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| HOPLineModifier | ForeignKey | Yes | HOPLineMod | - | Foreign key target: HOPLineMod |

---

### Entity: HOPLineSchCondItemCond

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPLineSchCondItemCond.eti`
**Entity Type:** `effdated`
**Database Table:** `hoplineschconditemcond`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** HOP Line condition scheduled item with coverage terms

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| HOPLineScheduleCondItem | ForeignKey | Yes | HOPLineScheduleCondItem | - | Foreign key target: HOPLineScheduleCondItem |

---

### Entity: HOPLineSchCovItemCov

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPLineSchCovItemCov.eti`
**Entity Type:** `effdated`
**Database Table:** `hoplineschcovitemcov`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** HOP Line coverage scheduled item with coverage terms

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| HOPLineScheduleCovItem | ForeignKey | Yes | HOPLineScheduleCovItem | - | Foreign key target: HOPLineScheduleCovItem |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| HOPLineSchCovItemCovCosts | HOPLineSchCovItemCovCost | Child collection |

---

### Entity: HOPLineSchCovItemCovCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPLineSchCovItemCovCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\HOPLineSchCovItemCovCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** HOPCost
**Effective-Dated Container Branch Field:** N/A
**Description:** Costs for HOP Line Scheduled Items with coverage terms

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| HOPLineSchCovItemCov | ForeignKey | Yes | HOPLineSchCovItemCov | - | Foreign key target: HOPLineSchCovItemCov |

---

### Entity: HOPLineScheduleCond

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPLineScheduleCond.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** HOPLineCond
**Effective-Dated Container Branch Field:** N/A
**Description:** HOP Line condition with a schedule

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| HOPLineScheduledItems | HOPLineScheduleCondItem | Scheduled Items |

---

### Entity: HOPLineScheduleCondItem

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPLineScheduleCondItem.eti`
**Entity Type:** `effdated`
**Database Table:** `hoplinescheduleconditem`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** HOP Line level condition scheduled item

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| Schedule | ForeignKey | Yes | HOPLineScheduleCond | - | Foreign key target: HOPLineScheduleCond |
| ScheduledItemClause | OneToOne | No | HOPLineSchCondItemCond | - | The condition that applies to this scheduled item |

---

### Entity: HOPLineScheduleCov

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPLineScheduleCov.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** HOPLineCov
**Effective-Dated Container Branch Field:** N/A
**Description:** HOP Line coverage with a schedule

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| HOPLineScheduledItems | HOPLineScheduleCovItem | Scheduled Items |

---

### Entity: HOPLineScheduleCovItem

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPLineScheduleCovItem.eti`
**Entity Type:** `effdated`
**Database Table:** `hoplineschedulecovitem`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** HOP Line level coverage scheduled item

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| Schedule | ForeignKey | Yes | HOPLineScheduleCov | - | Foreign key target: HOPLineScheduleCov |
| ScheduledItemClause | OneToOne | No | HOPLineSchCovItemCov | - | The coverage that applies to this scheduled item |

---

### Entity: HOPLineScheduleExcl

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPLineScheduleExcl.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** HOPLineExcl
**Effective-Dated Container Branch Field:** N/A
**Description:** HOP Line exclusion with a schedule

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| HOPLineScheduledItems | HOPLineScheduleExclItem | Scheduled Items |

---

### Entity: HOPLineScheduleExclItem

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPLineScheduleExclItem.eti`
**Entity Type:** `effdated`
**Database Table:** `hoplinescheduleexclitem`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** HOP Line level exclusion scheduled item

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| Schedule | ForeignKey | Yes | HOPLineScheduleExcl | - | Foreign key target: HOPLineScheduleExcl |
| ScheduledItemClause | OneToOne | No | HOPLineSchExclItemExcl | - | The exclusion that applies to this scheduled item |

---

### Entity: HOPLineSchExclItemExcl

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPLineSchExclItemExcl.eti`
**Entity Type:** `effdated`
**Database Table:** `hoplineschexclitemexcl`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** HOP Line exclusion scheduled item with coverage terms

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| HOPLineScheduleExclItem | ForeignKey | Yes | HOPLineScheduleExclItem | - | Foreign key target: HOPLineScheduleExclItem |

---

### Entity: HOPModifierLookup

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPModifierLookup.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** ModifierLookup
**Effective-Dated Container Branch Field:** N/A
**Description:** An availability lookup for HOP modifier patterns.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| CoveragePartType | TypeKey | No | - | CoveragePartType | - |
| HOPCoverageForm | TypeKey | No | - | HOPCoverageForm | Codes: [ho2, ho3, ho5, ho4, ho6] |

---

### Entity: HOPRateFactorLookup

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPRateFactorLookup.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** RateFactorLookup
**Effective-Dated Container Branch Field:** N/A
**Description:** An availability lookup for HOP rate factor patterns.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| CoveragePartType | TypeKey | No | - | CoveragePartType | - |
| HOPCoverageForm | TypeKey | No | - | HOPCoverageForm | Codes: [ho2, ho3, ho5, ho4, ho6] |

---

### Entity: HOPScheduledItem

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPScheduledItem.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: HOPSwimmingPool

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPSwimmingPool.eti`
**Entity Type:** `effdated`
**Database Table:** `hopswimmingpool`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Swimming Pool

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| AdditionalInformation | shorttext | No | - | - | Additional information |
| ApprovedFence | bit | No | - | - | Is there a fence around the property |
| DivingBoard | bit | No | - | - | Is there a diving board |
| Slide | bit | No | - | - | Is there a slide |
| HOPDwelling | ForeignKey | Yes | HOPDwelling | - | Foreign key target: HOPDwelling |
| PoolType | TypeKey | Yes | - | HOPSwimmingPoolType | Default: AboveGround Swimming Pool Type Codes: [AboveGround, InGround] |

---

### Entity: HOPTransaction

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPTransaction.eti`
**Entity Type:** `effdated`
**Database Table:** `hoptransaction`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A transaction for the Homeowners line

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| HOPCost | ForeignKey | Yes | HOPCost | - | The cost this transaction modifies. |

---

### Entity: JobGroup

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\JobGroup.eti`
**Entity Type:** `retireable`
**Database Table:** `jobgroup`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A job group is a grouping of jobs within a single account.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Name | shorttext | Yes | - | - | The name of this group. |
| Account | ForeignKey | Yes | Account | - | The account of this job group. |

---

### Entity: JobLetter

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\JobLetter.eti`
**Entity Type:** `joinarray`
**Database Table:** `jobletter`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Referencess one Job referred to in a letter.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Letter | ForeignKey | Yes | Letter | - | The associated Letter. |
| Job | ForeignKey | Yes | Job | - | The associated Job. |

---

### Entity: JobTypeFilteredLookup

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\JobTypeFilteredLookup.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| JobType | TypeKey | No | - | Job | The job type for which this lookup applies, or null if the lookup is not restricted by job type |

---

### Entity: JobUserRoleAssignment

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\JobUserRoleAssignment.eti`
**Entity Type:** `retireable`
**Database Table:** `jobuserroleassign`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** User role assignments for Jobs.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Job | ForeignKey | Yes | Job | - | Associated job. |

---

### Entity: PACededPremium

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PACededPremium.eti`
**Entity Type:** `retireable`
**Database Table:** `pacededpremium`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A PersonalAuto implementation of the RICededPremium delegate

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| PACost | ForeignKey | Yes | PACost | - | Foreign key target: PACost |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| CedingTransactions | PACededPremiumTransaction | Child collection |
| CedingHistory | PACededPremiumHistory | Child collection |

---

### Entity: PACededPremiumHistory

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PACededPremiumHistory.eti`
**Entity Type:** `retireable`
**Database Table:** `pacededpremiumhistory`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A PersonalAuto implementation of the RICededPremiumHistory delegate

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| PACededPremium | ForeignKey | Yes | PACededPremium | - | Foreign key target: PACededPremium |

---

### Entity: PACededPremiumTransaction

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PACededPremiumTransaction.eti`
**Entity Type:** `retireable`
**Database Table:** `pacededpremiumtransaction`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A PersonalAuto implementation of the RICededPremiumTransaction delegate

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| PACededPremium | ForeignKey | Yes | PACededPremium | - | Foreign key target: PACededPremium |
| PACededPremiumHistory | ForeignKey | Yes | PACededPremiumHistory | - | Foreign key target: PACededPremiumHistory |

---

### Entity: PACoveragePremium

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PACoveragePremium.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PAGeneralPremium
**Effective-Dated Container Branch Field:** N/A
**Description:** A taxable unit of price for a period of time, not to be broken up any further, for a Personal Auto coverage

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: PAGeneralPremium

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PAGeneralPremium.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PATaxable
**Effective-Dated Container Branch Field:** N/A
**Description:** A taxable unit of price for a period of time, not to be broken up any further, for Personal Auto

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: PAModifier

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PAModifier.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\PAModifier.etx`
**Entity Type:** `effdated`
**Database Table:** `pamodifier`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A line-level modifier for Personal Auto

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| PALine | ForeignKey | Yes | PersonalAutoLine | - | Foreign key target: PersonalAutoLine |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| PARateFactors | PARateFactor | Individual components of the rating factor |

---

### Entity: PAMultiPolicyDiscCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PAMultiPolicyDiscCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\PAMultiPolicyDiscCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PAGeneralPremium
**Effective-Dated Container Branch Field:** N/A
**Description:** A taxable unit of price for a period of time, not to be broken up any further, for a Personal Auto multi-policy discount

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: PAPolicyContactRole

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PAPolicyContactRole.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PolicyContactRole
**Effective-Dated Container Branch Field:** N/A
**Description:** A PolicyContactRole specific to a PersonalAuto policy line.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| PersonalAutoLine | ForeignKey | No | PersonalAutoLine | - | The Personal Auto policy line this contact role is associated with. |

---

### Entity: Parameter

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Parameter.eti`
**Entity Type:** `retireable`
**Database Table:** `parameter`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** For internal Guidewire use only.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| ParameterName | varchar | Yes | - | - | Name of the parameter |
| StringValue | varchar | No | - | - | For a string parameter, the parameter value. |
| LongTextValue | longtext | No | - | - | For a long text parameter (clob), the parameter value. |
| IntValue | integer | No | - | - | For an integer parameter, the parameter value. |
| BooleanValue | bit | No | - | - | For a boolean parameter, the parameter value. |
| DateValue | datetime | No | - | - | For a date or time parameter, the parameter value. |
| ComponentType | TypeKey | No | - | ComponentType | Component defining the parameter, or null if it is a system-wide parameter. Codes (29 total): [db, fs, session, tm, assigneng, ...] |
| ParameterType | TypeKey | Yes | - | ParameterType | Identifies the value type (string, longtext, integer, boolean, or date). Codes: [String, Integer, Boolean, Datetime, LongText] |

---

### Entity: PARateFactor

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PARateFactor.eti`
**Entity Type:** `effdated`
**Database Table:** `paratefactor`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A rate factor is a risk characteristic and its associated numeric value which might have an impact on premium. As used here rate factors are applied to base premium rather than rates. A common example of Rate Factors are the components of IRPM (individual risk premium modifier).

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| PAModifier | ForeignKey | Yes | PAModifier | - | Foreign key target: PAModifier |

---

### Entity: PAShortRatePenaltyCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PAShortRatePenaltyCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\PAShortRatePenaltyCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PATaxable
**Effective-Dated Container Branch Field:** N/A
**Description:** A taxable unit of price for a period of time, not to be broken up any further, for a Personal Auto short rate penalty

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: PATaxable

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PATaxable.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PACost
**Effective-Dated Container Branch Field:** N/A
**Description:** A taxable unit of price for a period of time, not to be broken up any further, for Personal Auto

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: PAVehicleCovLookup

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PAVehicleCovLookup.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** CoverageLookup
**Effective-Dated Container Branch Field:** N/A
**Description:** PersonalVehicle Coverage Lookup Table.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| VehicleType | TypeKey | No | - | VehicleType | Codes: [Commercial, PP, PublicTransport, Special, auto, other] |

---

### Entity: PAVehicleModifier

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PAVehicleModifier.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\PAVehicleModifier.etx`
**Entity Type:** `effdated`
**Database Table:** `pavehmodifier`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A vehicle-level modifier for Personal Auto

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| PAVehicle | ForeignKey | Yes | PersonalVehicle | - | Foreign key target: PersonalVehicle |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| PAVehicleRateFactors | PAVehicleRateFactor | Individual components of the rating factor |

---

### Entity: PAVehicleModifierLkup

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PAVehicleModifierLkup.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** ModifierLookup
**Effective-Dated Container Branch Field:** N/A
**Description:** PAVehicle-Level Modifier Lookup Table.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| VehicleType | TypeKey | No | - | VehicleType | Codes: [Commercial, PP, PublicTransport, Special, auto, other] |

---

### Entity: PAVehicleRateFactor

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PAVehicleRateFactor.eti`
**Entity Type:** `effdated`
**Database Table:** `pavehratefactor`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A rate factor is a risk characteristic and its associated numeric value which might have an impact on premium. As used here rate factors are applied to base premium rather than rates. A common example of Rate Factors are the components of IRPM (individual risk premium modifier).

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| PAVehicleModifier | ForeignKey | Yes | PAVehicleModifier | - | Foreign key target: PAVehicleModifier |

---

### Entity: PAVhcleAddlInterest

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PAVhcleAddlInterest.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** AddlInterestDetail
**Effective-Dated Container Branch Field:** N/A
**Description:** An additional interest on a personal auto vehicle

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| PAVehicle | ForeignKey | Yes | PersonalVehicle | - | Foreign key target: PersonalVehicle |

---

### Entity: PaymentGatewayTransaction

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PaymentGatewayTransaction.eti`
**Entity Type:** `keyable`
**Database Table:** `paymentgatewaytransaction`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Entity that holds all payment gateway transactions

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Reference | varchar | Yes | - | - | - |
| SaveForFutureUse | bit | Yes | - | - | Default: false |
| PolicyPeriod | ForeignKey | Yes | PolicyPeriod | - | Foreign key target: PolicyPeriod |

---

### Entity: PolicyAddlInsuredDetail

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyAddlInsuredDetail.eti`
**Entity Type:** `effdated`
**Database Table:** `policyaddlinsureddetail`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A type of Policy Additional Insured on a Line.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| AdditionalInformation | shorttext | No | - | - | Additional information on this policy additional insured. |
| PolicyAddlInsured | ForeignKey | No | PolicyAddlInsured | - | The policy additional insured this policy additional insured type is associated with. |
| AdditionalInsuredType | TypeKey | No | - | AdditionalInsuredType | Insured Type Codes (35 total): [CHAR, CHCHVOL, CLUB, CONCES, CONDO, ...] |

---

### Entity: PolicyAddlInterest

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyAddlInterest.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PolicyContactRole
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| AdditionalInterestDetails | AddlInterestDetail | Details of how this Additional Interest relates to items of interest on the Policy (e.g., a PAVehicle |

---

### Entity: PolicyAddlNamedInsured

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyAddlNamedInsured.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PlcyNonPriNamedInsured
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: PolicyAddress

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyAddress.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\PolicyAddress.etx`
**Entity Type:** `effdated`
**Database Table:** `policyaddress`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Policy address specific information.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| AddressLine1Internal | addressline | No | - | - | Address Line 1 |
| AddressLine2Internal | addressline | No | - | - | Address Line 2 |
| AddressLine3Internal | addressline | No | - | - | Address Line 3 |
| CityInternal | varchar | No | - | - | City. |
| CountyInternal | varchar | No | - | - | County. |
| PostalCodeInternal | postalcode | No | - | - | Postal code; string to handle Zip+4 and international codes. |
| DescriptionInternal | shorttext | No | - | - | Address Description |
| Address | ForeignKey | Yes | Address | - | The address this policy address may be synced with.  While the policy address contains policy contract information, the address contains shared role information. |
| StateInternal | TypeKey | No | - | State | State. Codes (142 total): [AK, AL, AR, AZ, CA, ...] |
| CountryInternal | TypeKey | No | - | Country | Country. Codes (243 total): [unknown, AF, AL, DZ, AS, ...] |
| AddressTypeInternal | TypeKey | No | - | AddressType | Type of this address record. Codes: [home, business, other, billing] |
| AddressLine1KanjiInternal_Ext | addressline | No | - | - | [Extension] Address Line 1 Kanji.  Used only for Japanese addresses and will be null otherwise. |
| AddressLine2KanjiInternal_Ext | addressline | No | - | - | [Extension] Address Line 2 Kanji.  Used only for Japanese addresses and will be null otherwise. |
| CityKanjiInternal_Ext | varchar | No | - | - | [Extension] City Kanji.  Used only for Japanese addresses and will be null otherwise. |
| CEDEXInternal_Ext | bit | No | - | - | [Extension] CEDEX: Special business mail delivery flag (France) |
| CEDEXBureauInternal_Ext | varchar | No | - | - | [Extension] CEDEX: Special business mail delivery bureau (France) |

---

### Entity: PolicyCondition

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyCondition.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| PatternCode | patterncode | Yes | - | - | The pattern defining what kind of Condition this is |
| ReferenceDateInternal | datetime | No | - | - | Internal field for storing the reference date of coverages on bound policy periods. Normally the ReferenceDate property should be used instead. |
| Currency | TypeKey | Yes | - | Currency | Currency associated with the policy condition Codes (7 total): [usd, eur, gbp, cad, aud, ...] |

---

### Entity: PolicyDriverMVR

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyDriverMVR.eti`
**Entity Type:** `effdated`
**Database Table:** `policydrivermvr`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** The Motor Vehicle Record summary data for this policy driver.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| InternalRequestID | varchar | No | - | - | Internal Request identifier. |
| StatusDate | datetime | No | - | - | Date of the last status change. |
| NumberOfAccidents | integer | No | - | - | Number of accidents in the Motor Vehicle Record. |
| NumberOfViolations | integer | No | - | - | Number of violations in the Motor Vehicle Record. |
| Points | integer | No | - | - | Total points assigned by the DMV to the driver |
| PolicyDriver | ForeignKey | Yes | PolicyDriver | - | The driver. |
| PersonalAutoLine | ForeignKey | Yes | PersonalAutoLine | - | The policy line |
| OrderStatus | TypeKey | No | - | MVRStatus | Order status Codes: [ToBeOrdered, Ordered, Ready, Received] |

---

### Entity: PolicyException

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyException.eti`
**Entity Type:** `versionable`
**Database Table:** `policyexception`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Records the action of the policy exception monitor. This table will have at most one row for each PolicyPeriod in the system, indicating the last time it had policy exception rules run on it.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| ExCheckTime | datetime | Yes | - | - | The last time at which policy exception rules were run on the PolicyPeriod. |
| PolicyPeriod | ForeignKey | Yes | PolicyPeriod | - | A foreign key to the PolicyPeriod. |

---

### Entity: PolicyFXRate

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyFXRate.eti`
**Entity Type:** `retireable`
**Database Table:** `policyfxrate`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Policy Foreign Exchange Rate

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Rate | decimal | Yes | - | - | The exchange spot rate at which a currency pair can be bought or sold |
| MarketTime | datetime | No | - | - | The point in time when the market indicated the rate was applicable |
| RetrievedAt | datetime | No | - | - | The point in time when the quotation was obtained from an external source |
| PolicyPeriod | ForeignKey | Yes | PolicyPeriod | - | The policy period to which this foreign exchange rate belongs. |
| FromCurrency | TypeKey | Yes | - | Currency | Base currency or first currency in currency pair Codes (7 total): [usd, eur, gbp, cad, aud, ...] |
| ToCurrency | TypeKey | Yes | - | Currency | quote currency or second currency in currency pair Codes (7 total): [usd, eur, gbp, cad, aud, ...] |
| Market | TypeKey | Yes | - | FXRateMarket | The FXRateMarket for which the rate applies Codes: [static_table] |

---

### Entity: PolicyHold

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyHold.eti`
**Entity Type:** `retireable`
**Database Table:** `policyhold`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Policy hold definition (rules, regions, etc.)

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Description | shorttext | Yes | - | - | A description of the policy hold. |
| PolicyHoldCode | shorttext | Yes | - | - | The unique code of the policy hold that will be used to raise uw issues. |
| StartDate | datetime | Yes | - | - | The start date for the hold. |
| EndDate | datetime | No | - | - | The end date for the hold. |
| UWIssueLongDesc | mediumtext | Yes | - | - | The long description of the selected uw issue. |
| IssueType | ForeignKey | Yes | UWIssueType | - | The uw issue that will be raised when the hold conditions are met. |
| HoldType | TypeKey | Yes | - | UWIssueCheckingSet | The type of the hold (ie., uw hold or regulatory hold) Codes (16 total): [PreQuote, PreRateRelease, PreQuoteRelease, PreBind, PreIssuance, ...] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Rules | PolicyHoldRule | The list of specific rules for this Policy Hold. |
| PolicyHoldZones | PolicyHoldZone | The zones that define this policy hold. |
| HeldJobs | PolicyHoldJob | Jobs that are held by this policy hold along with the last time they were evaluated. |

---

### Entity: PolicyHoldJob

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyHoldJob.eti`
**Entity Type:** `versionable`
**Database Table:** `policyholdjob`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Contains a policy hold and job pair, indicating the last time the job was evaluated against the policy hold.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| LastEvalTime | datetime | Yes | - | - | The last time this job was evaluated against this policy hold. |
| PolicyHold | ForeignKey | Yes | PolicyHold | - | A foreign key to the policy hold. |
| Job | ForeignKey | Yes | Job | - | A foreign key to the job. |
| Period | ForeignKey | No | PolicyPeriod | - | A foreign key to the period. |

---

### Entity: PolicyHoldRule

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyHoldRule.eti`
**Entity Type:** `retireable`
**Database Table:** `policyholdrule`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Rules for a policy hold

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| CovPatternCode | patterncode | No | - | - | The coverage pattern associated with this rule |
| PolicyHold | ForeignKey | No | PolicyHold | - | The policy hold containing this rule |
| PolicyLineType | TypeKey | Yes | - | PolicyLine | The type of policy line associated with this rule |
| JobType | TypeKey | Yes | - | Job | The type of job associated with this rule |
| JobDateType | TypeKey | Yes | - | JobDateType | The date type (effective, written, reference) used to determine whether the job falls within the dates of the hold Codes: [Effective, Written, Reference] |

---

### Entity: PolicyHoldZone

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyHoldZone.eti`
**Entity Type:** `retireable`
**Database Table:** `policyholdzone`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A zone of a policy hold. It contains the zone code, the zone type and the country to which the region belongs.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Code | shorttext | Yes | - | - | The code for this zone, this is the value that should be used for lookups. |
| PolicyHold | ForeignKey | No | PolicyHold | - | The policy hold containing this zone. |
| ZoneType | TypeKey | Yes | - | ZoneType | Type of zone. Codes (13 total): [country, unknown, city, citykanji, county, ...] |
| Country | TypeKey | Yes | - | Country | The country to which the zone belongs. Codes (243 total): [unknown, AF, AL, DZ, AS, ...] |

---

### Entity: PolicyLaborClient

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyLaborClient.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WCLaborContact
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: PolicyLaborContractor

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyLaborContractor.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WCLaborContact
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: PolicyLinePatternFilteredLookup

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyLinePatternFilteredLookup.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| PolicyLinePatternCode | patterncode | Yes | - | - | The policy line pattern code for which this lookup applies |

---

### Entity: PolicyNamedInsured

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyNamedInsured.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PolicyContactRole
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| LocationNamedInsureds | LocationNamedInsured | The named insured covered at this location. |

---

### Entity: PolicyOwnerOfficer

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyOwnerOfficer.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WCPolicyContactRole
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| OwnershipPct | integer | No | - | - | Ownership percentage |
| ClassCode | ForeignKey | No | WCClassCode | - | Class Code of this contact |
| RelationshipTitleInternal | TypeKey | No | - | Relationship | The relationship Codes (54 total): [AmbEmp, ApptOff, AuxPD, BdTrMbr, CEO, ...] |
| Included | TypeKey | No | - | Inclusion | Is this contact included in this policy? Codes: [incl, excl] |
| State | TypeKey | No | - | Jurisdiction | The state in which this contact is definied Codes (98 total): [AK, AL, AR, AZ, CA, ...] |

---

### Entity: PolicyPeriodSummary

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyPeriodSummary.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Encapsulates the "summary" or "header" fields needed to display the results of a PolicyPeriod search.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: PolicyPeriodWorkflow

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyPeriodWorkflow.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** Workflow
**Effective-Dated Container Branch Field:** N/A
**Description:** Workflows for PolicyPeriods

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Processing | bit | No | - | - | Default: false Indicate whether the workflow is currently processing an operation.  Use in the workflow script to             indicate when an operation starts and when it ends. |
| PolicyPeriod | ForeignKey | Yes | PolicyPeriod | - | The PolicyPeriod with which this workflow is associated. |

---

### Entity: PolicyPolicyDivide

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyPolicyDivide.eti`
**Entity Type:** `joinarray`
**Database Table:** `policypolicydivide`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Table linking a divided policy (a split or spun policy) to its source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| DividedPolicy | ForeignKey | Yes | Policy | - | Pointer to the divided policy |
| SourcePolicy | ForeignKey | Yes | Policy | - | Pointer to the source policy |

---

### Entity: PolicyPolicyRewrite

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyPolicyRewrite.eti`
**Entity Type:** `joinarray`
**Database Table:** `policypolicyrewrite`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Table linking a policy that was rewritten to a new account to its source policy.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| RewrittenPolicy | ForeignKey | Yes | Policy | - | Pointer to the rewritten policy |
| SourcePolicy | ForeignKey | Yes | Policy | - | Pointer to the source policy |

---

### Entity: PolicyProductRoot

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyProductRoot.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Policy Product root for availability.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| EffDate | datetime | No | - | - | Policy Period effective date |
| WrittenDate | datetime | No | - | - | Policy Period written date |
| Account | ForeignKey | Yes | Account | - | Owning Account |
| Producer | ForeignKey | Yes | Organization | - | The Organization selected as "producer". |
| ProducerCode | ForeignKey | Yes | ProducerCode | - | The ProducerCode selected to identify "producer". |
| UWCompany | ForeignKey | No | UWCompany | - | The selected Underwriting Company |
| State | TypeKey | Yes | - | Jurisdiction | Default Base State for new Submissions Codes (98 total): [AK, AL, AR, AZ, CA, ...] |
| JobType | TypeKey | Yes | - | Job | - |

---

### Entity: PolicyRisk

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyRisk.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** Reinsurable
**Effective-Dated Container Branch Field:** N/A
**Description:** A reinsurable risk associated with a policy as a whole.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: PolicySecNamedInsured

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicySecNamedInsured.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PlcyNonPriNamedInsured
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: PolicyTermRestoreRequest

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyTermRestoreRequest.eti`
**Entity Type:** `retireable`
**Database Table:** `policytermrestorerequest`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Represents a request to retrieve a PolicyTerm from the Archive.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Reason | shorttext | No | - | - | Reason that this user requested the PolicyTerm be retrieved from the Archive. |
| ShouldCreateActivity | bit | Yes | - | - | Default: true Flag to indicate whether an activity should be created when this request is processed. |
| RequestingUser | ForeignKey | Yes | User | - | The user that initiated this request to restore from the archive. |
| PolicyTerm | ForeignKey | Yes | PolicyTerm | - | The PolicyTerm requested to be retrieved from the archive. |

---

### Entity: PolicyUserRoleAssignment

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyUserRoleAssignment.eti`
**Entity Type:** `retireable`
**Database Table:** `policyuserroleassign`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** User role assignments for Policies.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Policy | ForeignKey | Yes | Policy | - | Associated policy. |

---

### Entity: WCAircraftSeat

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\WCAircraftSeat.eti`
**Entity Type:** `effdated`
**Database Table:** `wcaircraftseat`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Workers' Comp Aircraft Seat Data

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| Description | shorttext | No | - | - | Description |
| AircraftNumber | shorttext | No | - | - | Aircraft N-Number |
| PassengerSeats | positiveinteger | No | - | - | Number of rateable passenger seats |
| WCLine | ForeignKey | Yes | WorkersCompLine | - | Foreign key target: WorkersCompLine |
| State | TypeKey | No | - | Jurisdiction | Codes (98 total): [AK, AL, AR, AZ, CA, ...] |

---

### Entity: WCCededPremium

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\WCCededPremium.eti`
**Entity Type:** `retireable`
**Database Table:** `wccededpremium`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A Workers' Comp implementation of the RICededPremium delegate

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| WCCost | ForeignKey | Yes | WCCost | - | Foreign key target: WCCost |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| CedingTransactions | WCCededPremiumTransaction | Child collection |
| CedingHistory | WCCededPremiumHistory | Child collection |

---

### Entity: WCCededPremiumHistory

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\WCCededPremiumHistory.eti`
**Entity Type:** `retireable`
**Database Table:** `wccededpremiumhistory`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A Workers' Comp implementation of the RICededPremiumHistory delegate

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| WCCededPremium | ForeignKey | Yes | WCCededPremium | - | Foreign key target: WCCededPremium |

---

### Entity: WCCededPremiumTransaction

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\WCCededPremiumTransaction.eti`
**Entity Type:** `retireable`
**Database Table:** `wccededpremiumtransaction`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A Workers' Comp implementation of the RICededPremiumTransaction delegate

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| WCCededPremium | ForeignKey | Yes | WCCededPremium | - | Foreign key target: WCCededPremium |
| WCCededPremiumHistory | ForeignKey | Yes | WCCededPremiumHistory | - | Foreign key target: WCCededPremiumHistory |

---

### Entity: WCClassCode

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\WCClassCode.eti`
**Entity Type:** `retireable`
**Database Table:** `wcclasscode`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Workers' comp class codes.  Premium calculations are driven by class codes and both premium and losses are reported by class codes to rating bureaus.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Classification | mediumtext | No | - | - | The Classification of the code (essentially a short description) |
| ClassIndicator | shorttext | No | - | - | The Class Indicator for the class code |
| Code | shorttext | Yes | - | - | The Class Code for a line of insurance |
| ShortDesc | varchar | No | - | - | short classifcation description for listviews |
| WCDomain | shorttext | Yes | - | - | The string value of the typecode representing the jurisdiction for which this class code value is allowed. For example, if this is a typecode allowed in the US state of California, the value should be 'CA' |
| Basis | ForeignKey | No | ClassCodeBasis | - | Rating basis for this class code. |

---

### Entity: WCCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\WCCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WCCost.etx`
**Entity Type:** `effdated`
**Database Table:** `wccost`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A WorkersComp unit of price for a period of time that should not be broken up any further.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| CalcOrder | integer | Yes | - | - | The order in which this cost was rated. |
| WorkersCompLine | ForeignKey | Yes | WorkersCompLine | - | Foreign key target: WorkersCompLine |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Transactions | WCTransaction | Child collection |

---

### Entity: WCCovEmpCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\WCCovEmpCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WCCovEmpCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WCCost
**Effective-Dated Container Branch Field:** N/A
**Description:** A unit of price for a period of time, not to be broken up any further, for a Workers' Comp employee coverage

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| WCCoveredEmployee | ForeignKey | Yes | WCCoveredEmployee | - | Foreign key target: WCCoveredEmployee |
| WorkersCompCov | ForeignKey | Yes | WorkersCompCov | - | Foreign key target: WorkersCompCov |

---

### Entity: WCCoveredEmployeeBase

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\WCCoveredEmployeeBase.eti`
**Entity Type:** `effdated`
**Database Table:** `wccoveredemployee`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A Workers' Comp Covered Employee

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BasisAmount | integer | No | - | - | Basis Amount |
| IfAnyExposure | bit | No | - | - | Default: false Option to indicate that coverage is provided with precise liability to be determined later (at audit) |
| NumEmployees | positiveinteger | No | - | - | Number of employees |
| ClassCode | ForeignKey | No | WCClassCode | - | Class Code of covered employees |
| Location | ForeignKey | Yes | PolicyLocation | - | Location of covered employees. |
| WorkersCompLine | ForeignKey | Yes | WorkersCompLine | - | Foreign key target: WorkersCompLine |
| SpecialCov | TypeKey | Yes | - | SpecialCov | Special Coverage Class for this set of employees Codes (12 total): [stat, voco, uslh, ocsa, fcmh, ...] |

---

### Entity: WCExcludedWorkplace

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\WCExcludedWorkplace.eti`
**Entity Type:** `effdated`
**Database Table:** `wcexcludedworkplace`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| AddressLine1 | addressline | No | - | - | - |
| AddressLine2 | addressline | No | - | - | - |
| City | varchar | No | - | - | - |
| ExcludedItem | shorttext | No | - | - | - |
| WCLine | ForeignKey | Yes | WorkersCompLine | - | Foreign key target: WorkersCompLine |
| State | TypeKey | No | - | Jurisdiction | Codes (98 total): [AK, AL, AR, AZ, CA, ...] |

---

### Entity: WCFedCoveredEmployee

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\WCFedCoveredEmployee.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WCCoveredEmployeeBase
**Effective-Dated Container Branch Field:** N/A
**Description:** A Workers' Comp Federal Covered Employee

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| RailroadOrVessel | shorttext | No | - | - | Railroad or vessel name for program 1 |

---

### Entity: WCFedLiabClassCode

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\WCFedLiabClassCode.eti`
**Entity Type:** `retireable`
**Database Table:** `wcfedliabclasscode`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A Class Code to Class Code mapping entity

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| MainClassCode | ForeignKey | Yes | WCClassCode | - | The main class code |
| StateActClassCode | ForeignKey | No | WCClassCode | - | The State Act class code |
| USLActClassCode | ForeignKey | No | WCClassCode | - | The USL Act class code |

---

### Entity: WCFormAssociation

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\WCFormAssociation.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** FormAssociation
**Effective-Dated Container Branch Field:** N/A
**Description:** Associates a Workers' Comp waiver of subrogation entity with its related form.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| WCWaiverOfSubro | ForeignKey | No | WCWaiverOfSubro | - | Foreign key target: WCWaiverOfSubro |

---

### Entity: WCJurisdiction

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\WCJurisdiction.eti`
**Entity Type:** `effdated`
**Database Table:** `wcjurisdiction`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Container for state-level elements: coverages, modifiers, etc.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| AnniversaryDateInternal | datetime | No | - | - | Anniversary date for this jurisdiction |
| WCLine | ForeignKey | No | WorkersCompLine | - | Foreign key target: WorkersCompLine |
| State | TypeKey | No | - | Jurisdiction | The jurisdiction that is covered Codes (98 total): [AK, AL, AR, AZ, CA, ...] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Costs | WCJurisdictionCost | Child collection |
| Coverages | WCStateCov | All Coverages on this State |
| RatingPeriodStartDates | RatingPeriodStartDate | Sub-periods within which basis amounts of basis-scalable exposures cannot change. |
| WCModifiers | WCModifier | Rating info for the jurisdiction. |

---

### Entity: WCJurisdictionCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\WCJurisdictionCost.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WCJurisdictionCost.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WCCost
**Effective-Dated Container Branch Field:** N/A
**Description:** A unit of price for a period of time, not to be broken up any further, for a Workers' Comp jurisdiction

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| StatCode | shorttext | No | - | - | The statistic code for classifying premiums and surcharges that are not attributable to a specific employment class code, such as experience modification, premium for increased employer liability limits, expense constant, taxes, etc. |
| WCJurisdiction | ForeignKey | Yes | WCJurisdiction | - | Foreign key target: WCJurisdiction |
| WCJurisdictionCostType | TypeKey | Yes | - | WCJurisdictionCostType | Codes (11 total): [MinPrem, CancelShortRatePenalty, Tax, CIGA, ExpenseConst, ...] |

---

### Entity: WCLaborContact

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\WCLaborContact.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WCPolicyContactRole
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Details | WCLaborContactDetail | Child collection |

---

### Entity: WCLaborContactDetail

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\WCLaborContactDetail.eti`
**Entity Type:** `effdated`
**Database Table:** `wclaborcontactdetail`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| WorkLocation | addressline | No | - | - | The address at which the employees are working |
| DescriptionOfDuties | shorttext | No | - | - | Description of Duties |
| NumberOfEmployees | integer | No | - | - | Number of employees |
| ContractEffectiveDate | dateonly | No | - | - | Effective Date |
| ContractExpirationDate | dateonly | No | - | - | Expiration Date |
| WCLaborContact | ForeignKey | Yes | WCLaborContact | - | Foreign key target: WCLaborContact |
| Inclusion | TypeKey | No | - | Inclusion | Inclusion option. Included or Excluded Codes: [incl, excl] |

---

### Entity: WCModifier

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\WCModifier.eti`
**Entity Type:** `effdated`
**Database Table:** `wcmodifier`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A line-level modifier for Workers' Comp

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| WCJurisdiction | ForeignKey | Yes | WCJurisdiction | - | Foreign key target: WCJurisdiction |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| WCRateFactors | WCRateFactor | Individual components of the rating factor |

---

### Entity: WCParticipatingPlan

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\WCParticipatingPlan.eti`
**Entity Type:** `effdated`
**Database Table:** `participatingplan`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A Workers' Comp participating plan

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| LossConversionFactor | decimal | No | - | - | Loss Conversion Factor |
| Retention | decimal | No | - | - | The retention amount (percent) |
| WorkersCompLine | ForeignKey | Yes | WorkersCompLine | - | Foreign key target: WorkersCompLine |
| PlanID | TypeKey | Yes | - | WCParticipatingPlanID | The ID of this participating plan Codes: [1ystd, 2ystd, 3ystd] |

---

### Entity: WCPolicyContactRole

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\WCPolicyContactRole.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PolicyContactRole
**Effective-Dated Container Branch Field:** N/A
**Description:** A PolicyContactRole specific to a WorkersComp policy line.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| WorkersCompLine | ForeignKey | No | WorkersCompLine | - | The workers comp policy line this contact role is associated with. |

---

### Entity: WCRateFactor

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\WCRateFactor.eti`
**Entity Type:** `effdated`
**Database Table:** `wcratefactor`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A rate factor is a risk characteristic and its associated numeric value which might have an impact on premium. As used here rate factors are applied to base premium rather than rates. A common example of Rate Factors are the components of IRPM (individual risk premium modifier).

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| WCModifier | ForeignKey | Yes | WCModifier | - | Foreign key target: WCModifier |

---

### Entity: WCRetroRatingLetterOfCredit

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\WCRetroRatingLetterOfCredit.eti`
**Entity Type:** `effdated`
**Database Table:** `letterofcredit`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A Letter Of Credit

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| IssuerName | shorttext | No | - | - | The name of the issuer |
| ValidFrom | datetime | Yes | - | - | Date (inclusive) from which this letter of credit is valid. |
| ValidTo | datetime | Yes | - | - | Date (exclusive) at which this letter of credit is no longer valid. |
| WCRetrospectiveRatingPlan | ForeignKey | Yes | WCRetrospectiveRatingPlan | - | The retro plan for which this letter applies |
| Amount | monetaryamount | No | - | - | The amount this letter is providing |

---

### Entity: WCRetrospectiveRatingPlan

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\WCRetrospectiveRatingPlan.eti`
**Entity Type:** `effdated`
**Database Table:** `retroratingplan`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A plan for retrospectively rating a policy line

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BasicPremiumFactor1 | decimal | No | - | - | The (50%) premium factor |
| BasicPremiumFactor2 | decimal | No | - | - | The (100%) premium factor |
| BasicPremiumFactor3 | decimal | No | - | - | The (150%) premium factor |
| ComputationInterval | integer | No | - | - | The computation interval |
| FirstComputationDate | datetime | No | - | - | The data of the first computation |
| IncludeALAE | bit | No | - | - | Include ALocated Loss Adjustment |
| LastComputationDate | datetime | No | - | - | The data of the last computation |
| LossConversionFactor | decimal | No | - | - | Loss Conversion Factor |
| MaxRetroPremiumRatio | decimal | No | - | - | The maximum retro premium ratio |
| MinRetroPremiumRatio | decimal | No | - | - | The minimum retro premium ratio |
| PercentStandardPremium1 | decimal | No | - | - | Default: 50 The (50%) standard premium |
| PercentStandardPremium2 | decimal | No | - | - | Default: 100 The (100%) standard premium |
| PercentStandardPremium3 | decimal | No | - | - | Default: 150 The (150%) standard premium |
| WorkersCompLine | ForeignKey | Yes | WorkersCompLine | - | Foreign key target: WorkersCompLine |
| EstimatedStandardPremium | monetaryamount | No | - | - | The estimated standard premium |
| LossLimitAmount | monetaryamount | No | - | - | Loss limitation amount |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| LettersOfCredit | WCRetroRatingLetterOfCredit | The list of Letters Of Credit |
| StateMultipliers | WCStateMultiplier | The list of Multipliers by State |

---

### Entity: WCStateCov

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\WCStateCov.eti`
**Entity Type:** `effdated`
**Database Table:** `wcstatecov`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A state-level coverage for Workers Comp'

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| ChoiceTerm1 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm1Avl | bit | No | - | - | whether or not the ChoiceTerm1 field was available the last time availability was checked |
| WCJurisdiction | ForeignKey | No | WCJurisdiction | - | Foreign key target: WCJurisdiction |

---

### Entity: WCStateMultiplier

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\WCStateMultiplier.eti`
**Entity Type:** `effdated`
**Database Table:** `statemultiplier`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** State Multipliers

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| FederalExcessLossFactor | decimal | No | - | - | Federal Excess Loss factor |
| FederalTaxMultiplier | decimal | No | - | - | The federal tax multiplier |
| StateExcessLossFactor | decimal | No | - | - | State Excess Loss factor |
| StateTaxMultiplier | decimal | No | - | - | The state tax multiplier |
| WCRetrospectiveRatingPlan | ForeignKey | Yes | WCRetrospectiveRatingPlan | - | The retro plan for which this state multiplier applies |
| State | TypeKey | No | - | Jurisdiction | Codes (98 total): [AK, AL, AR, AZ, CA, ...] |

---

### Entity: WCTransaction

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\WCTransaction.eti`
**Entity Type:** `effdated`
**Database Table:** `wctransaction`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A transaction for the Workers' Comp line

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| WCCost | ForeignKey | Yes | WCCost | - | The cost this transaction modifies. |

---

### Entity: WCWaiverOfSubro

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\WCWaiverOfSubro.eti`
**Entity Type:** `effdated`
**Database Table:** `wcwaiverofsubro`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A Workers' Comp Waiver of Subrogation

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BasisAmount | integer | No | - | - | Basis Amount |
| Description | shorttext | No | - | - | Description |
| IfAnyExposure | bit | No | - | - | Default: false Option to indicate that coverage is provided with precise liability to be determined later (at audit) |
| JobID | shorttext | No | - | - | The job identifier |
| NumEmployees | positiveinteger | No | - | - | Number of employees |
| ClassCode | ForeignKey | No | WCClassCode | - | Class Code of covered employees |
| WCLine | ForeignKey | Yes | WorkersCompLine | - | Foreign key target: WorkersCompLine |
| SpecialCov | TypeKey | Yes | - | SpecialCov | Special Coverage Class for this set of employees Codes (12 total): [stat, voco, uslh, ocsa, fcmh, ...] |
| State | TypeKey | No | - | Jurisdiction | Codes (98 total): [AK, AL, AR, AZ, CA, ...] |
| Type | TypeKey | No | - | WaiverOfSubrogationType | The type of waiver of subro. Codes: [blanket, specific] |

---

### Entity: BANonOwnedLiabCovCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\BANonOwnedLiabCovCost.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** BAStateCovCost
**Effective-Dated Container Branch Field:** N/A
**Description:** The cost for non-owned auto liability coverage for a particular group of people.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BANonOwnedLiabCovCostType | TypeKey | Yes | - | BANonOwnedLiabCovCostType | deprecated - use BALineCovNonownedCost since non owned coverages have now been moved to the line level Codes: [Employees, Partners, Volunteers] |

---

### Entity: PolicyContactRoleKanjiIndexDelegate

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\PolicyContactRoleKanjiIndexDelegate.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: WC7AircraftSeat

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7AircraftSeat.eti`
**Entity Type:** `effdated`
**Database Table:** `wc7aircraftseat`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Workers' Comp Aircraft Seat Data

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| Description | shorttext | No | - | - | Description |
| AircraftNumber | shorttext | No | - | - | Aircraft N-Number |
| PassengerSeats | positiveinteger | No | - | - | Number of rateable passenger seats |
| WCLine | ForeignKey | Yes | WC7WorkersCompLine | - | Foreign key target: WC7WorkersCompLine |
| AircraftSeatCondition | ForeignKey | Yes | WC7WorkersCompCond | - | The parent coverage for maritime covered employees |
| Jurisdiction | TypeKey | No | - | Jurisdiction | Codes (98 total): [AK, AL, AR, AZ, CA, ...] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Costs | WC7AircraftSeatCost | Child collection |

---

### Entity: WC7AircraftSeatCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7AircraftSeatCost.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WC7JurisdictionCost
**Effective-Dated Container Branch Field:** N/A
**Description:** A unit of price for a period of time, not to be broken up any further, for Aircraft seat surcharge

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| WC7AircraftSeat | ForeignKey | Yes | WC7AircraftSeat | - | Foreign key target: WC7AircraftSeat |

---

### Entity: WC7AtomicEnergyCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7AtomicEnergyCost.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WC7Cost
**Effective-Dated Container Branch Field:** N/A
**Description:** A unit of price for a period of time, not to be broken up any further, for an Atomic Energy Exposure

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| WC7AtomicEnergyExposure | ForeignKey | Yes | WC7AtomicEnergyExposure | - | Foreign key target: WC7AtomicEnergyExposure |

---

### Entity: WC7AtomicEnergyExposure

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7AtomicEnergyExposure.eti`
**Entity Type:** `effdated`
**Database Table:** `wc7atomicenergyexp`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A Workers' Comp Atomic Energy Exposure

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BasisAmount | integer | No | - | - | Basis Amount |
| IfAnyExposure | bit | No | - | - | Default: false Option to indicate that coverage is provided with precise liability to be determined later (at audit) |
| Rate | decimal | No | - | - | Rate |
| ClassCode | ForeignKey | No | WC7ClassCode | - | Class Code of exposure |
| Location | ForeignKey | Yes | PolicyLocation | - | Location of exposure. |
| WCLine | ForeignKey | Yes | WC7WorkersCompLine | - | Foreign key target: WC7WorkersCompLine |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| WC7Costs | WC7AtomicEnergyCost | Child collection |

---

### Entity: WC7CededPremium

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7CededPremium.eti`
**Entity Type:** `retireable`
**Database Table:** `wc7cededpremium`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A Workers' Comp implementation of the RICededPremium delegate

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| WC7Cost | ForeignKey | Yes | WC7Cost | - | Foreign key target: WC7Cost |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| CedingTransactions | WC7CededPremiumTransaction | Child collection |
| CedingHistory | WC7CededPremiumHistory | Child collection |

---

### Entity: WC7CededPremiumHistory

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7CededPremiumHistory.eti`
**Entity Type:** `retireable`
**Database Table:** `wc7cededpremiumhistory`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A Workers' Comp implementation of the RICededPremiumHistory delegate

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| WC7CededPremium | ForeignKey | Yes | WC7CededPremium | - | Foreign key target: WC7CededPremium |

---

### Entity: WC7CededPremiumTransaction

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7CededPremiumTransaction.eti`
**Entity Type:** `retireable`
**Database Table:** `wc7cededpremiumtransaction`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A Workers' Comp implementation of the RICededPremiumTransaction delegate

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| WC7CededPremium | ForeignKey | Yes | WC7CededPremium | - | Foreign key target: WC7CededPremium |
| WC7CededPremiumHistory | ForeignKey | Yes | WC7CededPremiumHistory | - | Foreign key target: WC7CededPremiumHistory |

---

### Entity: WC7ClassCode

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7ClassCode.eti`
**Entity Type:** `retireable`
**Database Table:** `wc7classcode`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Workers' comp class codes.  Premium calculations are driven by class codes and both premium and losses are reported by class codes to rating bureaus.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Classification | mediumtext | No | - | - | The Classification of the code |
| Code | shorttext | Yes | - | - | The Class Code for a line of insurance |
| ShortDesc | shorttext | Yes | - | - | Short description for the class code |
| ConstructionType | bit | No | - | - | Default: false Specify whether class code is of construction type as well |
| DiseaseType | bit | No | - | - | Default: false Specify whether class code is of disease type as well |
| CoalMineType | bit | No | - | - | Default: false Specify whether class code is of coal mine disease type as well |
| ARatedType | bit | No | - | - | Default: false Specify whether class code is A Rated |
| Basis | ForeignKey | No | ClassCodeBasis | - | Rating basis for this class code. |
| Jurisdiction | TypeKey | No | - | Jurisdiction | The jurisdiction for which this class code value is allowed. Codes (98 total): [AK, AL, AR, AZ, CA, ...] |
| ClassCodeType | TypeKey | No | - | WC7ClassCodeType | Type of this classcode Codes: [FELA, USLH, Admiralty, Nonratable, AtomicEnergy] |
| ProgramType | TypeKey | No | - | WC7ClassCodeProgramType | Type of program Codes: [ProgramI, ProgramIIStateAct, ProgramIIUSLH] |

---

### Entity: WC7ContactDetail

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7ContactDetail.eti`
**Entity Type:** `effdated`
**Database Table:** `wc7contactdetail`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| WC7Contact | ForeignKey | Yes | WC7PolicyContactRole | - | Foreign key target: WC7PolicyContactRole |
| LaborContactCondition | ForeignKey | No | WC7WorkersCompCond | - | The parent condition for this specific scheduled item |
| LaborContactExclusion | ForeignKey | No | WC7WorkersCompExcl | - | The parent exclusion for this specific scheduled item |

---

### Entity: WC7CoordinatedPolicy

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7CoordinatedPolicy.eti`
**Entity Type:** `effdated`
**Database Table:** `wc7coordinatedpolicy`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| LaborContractorPolicyNumber | shorttext | No | - | - | - |
| ContractProject | shorttext | No | - | - | Contract or Project |
| WCLine | ForeignKey | Yes | WC7WorkersCompLine | - | Foreign key target: WC7WorkersCompLine |
| LaborContractor | ForeignKey | Yes | LaborContractor | - | Foreign key target: LaborContractor |
| MultipleCoordindatedPolicyCond | ForeignKey | Yes | WC7WorkersCompCond | - | The parent condition for coordinated policies |
| StatePerformed | TypeKey | No | - | Jurisdiction | Codes (98 total): [AK, AL, AR, AZ, CA, ...] |

---

### Entity: WC7Cost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7Cost.eti`
**Entity Type:** `effdated`
**Database Table:** `wc7cost`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A WorkersComp unit of price for a period of time that should not be broken up any further.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| CalcOrder | integer | Yes | - | - | The order in which this cost was rated. |
| DisplayOrder | integer | Yes | - | - | The order in which this cost is displayed. |
| StatCode | shorttext | No | - | - | The statistic code for classifying premiums and surcharges that are not attributable to a specific employment class code, such as experience modification, premium for increased employer liability limits, expense constant, taxes, etc. |
| WC7WorkersCompLine | ForeignKey | Yes | WC7WorkersCompLine | - | Foreign key target: WC7WorkersCompLine |
| PremiumLevelType | TypeKey | No | - | WC7PremiumLevelType | Codes (7 total): [TotalManualPremium, SubjectPremium, TotalSubjectPremium, TotalModifiedPremium, TotalStandardPremium, ...] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Transactions | WC7Transaction | Child collection |

---

### Entity: WC7CovCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7CovCost.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WC7Cost
**Effective-Dated Container Branch Field:** N/A
**Description:** A unit of price for a period of time, not to be broken up any further, for a Workers' Comp coverage

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| WC7WorkersCompCov | ForeignKey | Yes | WC7WorkersCompCov | - | Foreign key target: WC7WorkersCompCov |

---

### Entity: WC7CovEmpCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7CovEmpCost.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WC7CovCost
**Effective-Dated Container Branch Field:** N/A
**Description:** A unit of price for a period of time, not to be broken up any further, for a Workers' Comp employee coverage

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| WC7CoveredEmployee | ForeignKey | Yes | WC7CoveredEmployee | - | Foreign key target: WC7CoveredEmployee |
| WC7CovEmpCostType | TypeKey | Yes | - | WC7CovEmpCostType | Codes: [ManualPremium, USLH, CoalMineDisCharge, CatastropheLoading, SupplementalDisease] |

---

### Entity: WC7CoveredEmployeeBase

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7CoveredEmployeeBase.eti`
**Entity Type:** `effdated`
**Database Table:** `wc7coveredemployee`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A Workers' Comp Covered Employee

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BasisAmount | nonnegativeinteger | No | - | - | Basis Amount |
| IfAnyExposure | bit | No | - | - | Default: false Option to indicate that coverage is provided with precise liability to be determined later (at audit) |
| NumEmployees | positiveinteger | No | - | - | Number of employees |
| SpecificDiseaseLoaded | bit | No | - | - | Default: false Option to indicate that coverage is specific disease loaded |
| SupplementalDiseaseLoaded | bit | No | - | - | Default: false Option to indicate that coverage is supplemental disease loaded |
| SupplementalDiseaseLoadingRate | decimal | No | - | - | Supplemental Disease Loading Rate |
| ClassCodeRate | decimal | No | - | - | Rate of Class Code |
| ClassCode | ForeignKey | No | WC7ClassCode | - | Class Code of covered employees |
| Location | ForeignKey | Yes | PolicyLocation | - | Location of covered employees. |
| WC7WorkersCompLine | ForeignKey | Yes | WC7WorkersCompLine | - | Foreign key target: WC7WorkersCompLine |
| GoverningLaw | TypeKey | Yes | - | WC7GoverningLaw | Special Coverage Class for this set of employees Codes (11 total): [state, defenseBaseAct, fedCoalMine, longshoreAndHarbor, migrantAndSeasonalAgricultural, ...] |

---

### Entity: WC7DiseaseCode

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7DiseaseCode.eti`
**Entity Type:** `retireable`
**Database Table:** `wc7diseasecode`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Workers' comp disease stat codes.  Premium calculations are driven by disease stat codes and both premium and losses are reported by disease stat codes to rating bureaus.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Code | shorttext | Yes | - | - | The Disease Code for a line of insurance |
| SupplDiseaseLoadingType | shorttext | Yes | - | - | Description for the code |
| Jurisdiction | TypeKey | No | - | Jurisdiction | The jurisdiction for which this code value is allowed. Codes (98 total): [AK, AL, AR, AZ, CA, ...] |

---

### Entity: WC7ELIncreasedLimitCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7ELIncreasedLimitCost.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WC7CovCost
**Effective-Dated Container Branch Field:** N/A
**Description:** A unit of price for a period of time, not to be broken up any further, for Workers' Comp and Employers liability coverage

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Jurisdiction | TypeKey | Yes | - | Jurisdiction | The jurisdiction this cost applies to Codes (98 total): [AK, AL, AR, AZ, CA, ...] |
| WC7ELIncreasedLimitCostType | TypeKey | Yes | - | WC7ELIncrLimitCostType | Codes: [incrlimitfactor, incrlimitcharge] |

---

### Entity: WC7EmployeeLeasingPlan

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7EmployeeLeasingPlan.eti`
**Entity Type:** `effdated`
**Database Table:** `wc7employeeleasingplan`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Details about the employee leasing plan.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| WC7WorkersCompLine | ForeignKey | Yes | WC7WorkersCompLine | - | Foreign key target: WC7WorkersCompLine |
| ProfessionalEmployeeType | TypeKey | No | - | WC7ProfessionalEmployeeType | The type of employee for the employee leasing plan. Codes: [PEO, Client] |
| PolicyType | TypeKey | No | - | WC7EmployeeLeasingPolicyType | The type of employee leasing policy. Codes: [Master, MCP, MultiplePEO, ClientDirect] |

---

### Entity: WC7EmployeeLeasingPolicyTypeLookup

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7EmployeeLeasingPolicyTypeLookup.eti`
**Entity Type:** `retireable`
**Database Table:** `wc7emppolicytypelookup`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Employee leasing policy type availability lookups

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| PolicyType | TypeKey | No | - | WC7EmployeeLeasingPolicyType | Employee leasing policy type Codes: [Master, MCP, MultiplePEO, ClientDirect] |
| Jurisdiction | TypeKey | No | - | Jurisdiction | Jurisdiction Codes (98 total): [AK, AL, AR, AZ, CA, ...] |
| Availability | TypeKey | Yes | - | AvailabilityType | Availability Codes: [Available, Unavailable] |

---

### Entity: WC7ExcludedLaborContactDetail

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7ExcludedLaborContactDetail.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WC7LaborContactDetail
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: WC7ExcludedOwnerOfficer

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7ExcludedOwnerOfficer.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WC7PolicyOwnerOfficer
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| OwnerOfficerExclusion | ForeignKey | Yes | WC7WorkersCompExcl | - | The owning Clause (Exclusion) for this specific scheduled item |

---

### Entity: WC7ExcludedWorkplace

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7ExcludedWorkplace.eti`
**Entity Type:** `effdated`
**Database Table:** `wc7excludedworkplace`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| AddressLine1 | addressline | No | - | - | - |
| AddressLine2 | addressline | No | - | - | - |
| City | varchar | No | - | - | - |
| ExcludedItem | shorttext | No | - | - | - |
| WCLine | ForeignKey | Yes | WC7WorkersCompLine | - | Foreign key target: WC7WorkersCompLine |
| DesignatedWorkplacesExcl | ForeignKey | Yes | WC7WorkersCompExcl | - | The parent exclusion for workplaces |
| Jurisdiction | TypeKey | No | - | Jurisdiction | Codes (98 total): [AK, AL, AR, AZ, CA, ...] |

---

### Entity: WC7FedCoveredEmployee

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7FedCoveredEmployee.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WC7CoveredEmployeeBase
**Effective-Dated Container Branch Field:** N/A
**Description:** A Workers' Comp Federal Covered Employee

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| FedEmpLiabCoverage | ForeignKey | Yes | WC7WorkersCompCov | - | The parent coverage for federal covered employees |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| WC7Costs | WC7FELACovEmpCost | Child collection |

---

### Entity: WC7FELACovEmpCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7FELACovEmpCost.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WC7Cost
**Effective-Dated Container Branch Field:** N/A
**Description:** A unit of price for a period of time, not to be broken up any further, for a FELA Workers' Comp employee coverage

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| WC7FELACoveredEmployee | ForeignKey | Yes | WC7FedCoveredEmployee | - | Foreign key target: WC7FedCoveredEmployee |
| WC7FELACov | ForeignKey | Yes | WC7WorkersCompCov | - | Foreign key target: WC7WorkersCompCov |
| WC7FELACovEmpCostType | TypeKey | Yes | - | WC7FELACovEmpCostType | Codes: [FELACovEmp, IncreasedLimitsFactor, SupplementalDisease] |

---

### Entity: WC7FormAssociation

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7FormAssociation.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** FormAssociation
**Effective-Dated Container Branch Field:** N/A
**Description:** Associates a Workers' Comp waiver of subrogation entity with its related form.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| WC7WaiverOfSubro | ForeignKey | No | WC7WaiverOfSubro | - | Foreign key target: WC7WaiverOfSubro |

---

### Entity: WC7FormPatternClassCode

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7FormPatternClassCode.eti`
**Entity Type:** `retireable`
**Database Table:** `wc7formpatternclasscode`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A property (datamodel field) of a WC7ClassCode associated with a form pattern.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Code | shorttext | Yes | - | - | The class code. |
| Classification | mediumtext | Yes | - | - | The description of the class code. |
| FormPattern | ForeignKey | Yes | FormPattern | - | The form pattern associated with this coverable property. |
| Jurisdiction | TypeKey | No | - | Jurisdiction | The jurisdiction for which this class code value is allowed. Codes (98 total): [AK, AL, AR, AZ, CA, ...] |

---

### Entity: WC7IncludedLaborContactDetail

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7IncludedLaborContactDetail.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WC7LaborContactDetail
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: WC7IncludedOwnerOfficer

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7IncludedOwnerOfficer.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WC7PolicyOwnerOfficer
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Payroll | positiveinteger | No | - | - | Payroll for the officer |
| WC7ClassCode | ForeignKey | No | WC7ClassCode | - | Class Code of this contact |
| OwnerOfficerCondition | ForeignKey | Yes | WC7WorkersCompCond | - | The owning Clause (Condition) for this specific scheduled item |

---

### Entity: WC7Jurisdiction

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7Jurisdiction.eti`
**Entity Type:** `effdated`
**Database Table:** `wc7jurisdiction`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Container for jurisdiction-level elements: coverages, modifiers, etc.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| AnniversaryDateInternal | datetime | No | - | - | Anniversary date for this jurisdiction |
| WCLine | ForeignKey | No | WC7WorkersCompLine | - | Foreign key target: WC7WorkersCompLine |
| Jurisdiction | TypeKey | No | - | Jurisdiction | The jurisdiction that is covered Codes (98 total): [AK, AL, AR, AZ, CA, ...] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Costs | WC7JurisdictionCost | Child collection |
| Coverages | WC7JurisdictionCov | All Coverages on this Jurisdiction |
| WC7RatingPeriodStartDates | WC7RatingPeriodStartDate | Sub-periods within which basis amounts of basis-scalable exposures cannot change. |
| WC7PremiumDiscounts | WC7PremiumDiscount | Premium discount rate calculated based on last promoted job.  |
| WC7Modifiers | WC7Modifier | Rating info for the jurisdiction. |
| Conditions | WC7JurisdictionCond | All conditions on this jurisdiction |

---

### Entity: WC7JurisdictionCond

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7JurisdictionCond.eti`
**Entity Type:** `effdated`
**Database Table:** `wc7jurisdictioncond`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A jurisdiction-level condition for Workers Comp

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| DirectTerm1 | decimal | No | - | - | direct cov term field |
| DirectTerm1Avl | bit | No | - | - | whether or not the DirectTerm1 field was available the last time availability was checked |
| DirectTerm2 | decimal | No | - | - | direct cov term field |
| DirectTerm2Avl | bit | No | - | - | whether or not the DirectTerm2 field was available the last time availability was checked |
| ChoiceTerm1 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm1Avl | bit | No | - | - | whether or not the ChoiceTerm1 field was available the last time availability was checked |
| ChoiceTerm2 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm2Avl | bit | No | - | - | whether or not the ChoiceTerm2 field was available the last time availability was checked |
| WC7Jurisdiction | ForeignKey | No | WC7Jurisdiction | - | Foreign key target: WC7Jurisdiction |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Costs | WC7JurisdictionCondCost | Child collection |

---

### Entity: WC7JurisdictionCondCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7JurisdictionCondCost.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WC7JurisdictionCost
**Effective-Dated Container Branch Field:** N/A
**Description:** A unit of price for a period of time, not to be broken up any further, for jurisdiction-level conditions for Workers Comp

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| WC7JurisdictionCond | ForeignKey | Yes | WC7JurisdictionCond | - | Foreign key target: WC7JurisdictionCond |

---

### Entity: WC7JurisdictionCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7JurisdictionCost.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WC7Cost
**Effective-Dated Container Branch Field:** N/A
**Description:** A unit of price for a period of time, not to be broken up any further, for a Workers' Comp jurisdiction

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| WC7Jurisdiction | ForeignKey | Yes | WC7Jurisdiction | - | Foreign key target: WC7Jurisdiction |
| JurisdictionCostType | TypeKey | Yes | - | WC7JurisdictionCostType | Codes (25 total): [MinPrem, MinPremFELAMaritime, CancelShortRatePenalty, Tax, CIGA, ...] |

---

### Entity: WC7JurisdictionCov

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7JurisdictionCov.eti`
**Entity Type:** `effdated`
**Database Table:** `wc7jurisdictioncov`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A jurisdiction-level coverage for Workers Comp'

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BooleanTerm1 | bit | No | - | - | boolean cov term field |
| BooleanTerm1Avl | bit | No | - | - | whether or not the BooleanTerm1 field was available the last time availability was checked |
| BooleanTerm2 | bit | No | - | - | boolean cov term field |
| BooleanTerm2Avl | bit | No | - | - | whether or not the BooleanTerm2 field was available the last time availability was checked |
| DirectTerm1 | decimal | No | - | - | direct cov term field |
| DirectTerm1Avl | bit | No | - | - | whether or not the DirectTerm1 field was available the last time availability was checked |
| DirectTerm2 | decimal | No | - | - | direct cov term field |
| DirectTerm2Avl | bit | No | - | - | whether or not the DirectTerm2 field was available the last time availability was checked |
| DirectTerm3 | decimal | No | - | - | direct cov term field |
| DirectTerm3Avl | bit | No | - | - | whether or not the DirectTerm3 field was available the last time availability was checked |
| StringTerm1 | shorttext | No | - | - | string cov term field |
| StringTerm1Avl | bit | No | - | - | whether or not the StringTerm1 field was available the last time availability was checked |
| StringTerm2 | shorttext | No | - | - | string cov term field |
| StringTerm2Avl | bit | No | - | - | whether or not the StringTerm2 field was available the last time availability was checked |
| StringTerm3 | shorttext | No | - | - | string cov term field |
| StringTerm3Avl | bit | No | - | - | whether or not the StringTerm3 field was available the last time availability was checked |
| ChoiceTerm1 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm1Avl | bit | No | - | - | whether or not the ChoiceTerm1 field was available the last time availability was checked |
| ChoiceTerm2 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm2Avl | bit | No | - | - | whether or not the ChoiceTerm2 field was available the last time availability was checked |
| ChoiceTerm3 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm3Avl | bit | No | - | - | whether or not the ChoiceTerm3 field was available the last time availability was checked |
| ChoiceTerm4 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm4Avl | bit | No | - | - | whether or not the ChoiceTerm4 field was available the last time availability was checked |
| ChoiceTerm5 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm5Avl | bit | No | - | - | whether or not the ChoiceTerm5 field was available the last time availability was checked |
| ChoiceTerm6 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm6Avl | bit | No | - | - | whether or not the ChoiceTerm6 field was available the last time availability was checked |
| WC7Jurisdiction | ForeignKey | No | WC7Jurisdiction | - | Foreign key target: WC7Jurisdiction |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Costs | WC7JurisdictionCovCost | Child collection |

---

### Entity: WC7JurisdictionCovCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7JurisdictionCovCost.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WC7JurisdictionCost
**Effective-Dated Container Branch Field:** N/A
**Description:** A unit of price for a period of time, not to be broken up any further, for jurisdiction-level coverages for Workers Comp

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| WC7JurisdictionCov | ForeignKey | Yes | WC7JurisdictionCov | - | Foreign key target: WC7JurisdictionCov |

---

### Entity: WC7JurisdictionMultiplier

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7JurisdictionMultiplier.eti`
**Entity Type:** `effdated`
**Database Table:** `wc7jurisdictionmultiplier`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Jurisdiction Multipliers

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| FederalExcessLossFactor | decimal | No | - | - | Federal Excess Loss factor |
| FederalTaxMultiplier | decimal | No | - | - | The federal tax multiplier |
| JurisdictionExcessLossFactor | decimal | No | - | - | Jurisdiction Excess Loss factor |
| JurisdictionTaxMultiplier | decimal | No | - | - | The Jurisdiction tax multiplier |
| WC7RetrospectiveRatingPlan | ForeignKey | Yes | WC7RetrospectiveRatingPlan | - | The retro plan for which this jurisdiction multiplier applies |
| Jurisdiction | TypeKey | No | - | Jurisdiction | Codes (98 total): [AK, AL, AR, AZ, CA, ...] |

---

### Entity: WC7JurisdictionPremLevelOrder

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7JurisdictionPremLevelOrder.eti`
**Entity Type:** `keyable`
**Database Table:** `wc7jurpremlevelorder`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Premium level calculation order for a given jurisdiction on Workers' comp policy.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| PremiumLevelCalcOrder | integer | Yes | - | - | The order in which the premium levels for calculated for a given jurisdiction. |
| Jurisdiction | TypeKey | No | - | Jurisdiction | The jurisdiction for which this premium level belongs to. Codes (98 total): [AK, AL, AR, AZ, CA, ...] |
| PremiumLevelType | TypeKey | Yes | - | WC7PremiumLevelType | Codes (7 total): [TotalManualPremium, SubjectPremium, TotalSubjectPremium, TotalModifiedPremium, TotalStandardPremium, ...] |

---

### Entity: WC7JurisdictionScheduleAutoNumberSequence

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7JurisdictionScheduleAutoNumberSequence.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| WC7JurisdicSchedAutoNumberSeq | ForeignKey | No | AutoNumberSequence | - | Sequence to autonumber Jurisdiction schedule items |

---

### Entity: WC7JurisdictionScheduleCond

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7JurisdictionScheduleCond.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WC7JurisdictionCond
**Effective-Dated Container Branch Field:** N/A
**Description:** WC7 Jurisdiction Condition with a schedule

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| WC7JurisdictionScheduleCondItems | WC7JurisdictSchedCondItem | Condition scheduled items |

---

### Entity: WC7JurisdictionSplittableARD

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7JurisdictionSplittableARD.eti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7JurisdictionSplittableARD.etx`
**Entity Type:** `keyable`
**Database Table:** `wc7jurisdictionspliteARD`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| SplittableARD | bit | No | - | - | Default: true Defines whether the Jurisdiction is splittableARD. |
| Jurisdiction | TypeKey | No | - | Jurisdiction | The jurisdiction for which this SplittableARD flag is defined. Codes (98 total): [AK, AL, AR, AZ, CA, ...] |
| Apply90DaysARDRule_Ext | bit | No | - | - | [Extension] Determines if 90-days ARD rule apply to the Jurisdiction |

---

### Entity: WC7JurisdictSchedCondItem

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7JurisdictSchedCondItem.eti`
**Entity Type:** `effdated`
**Database Table:** `wc7jurisschedconditem`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** WC7 Jurisdiction level condition scheduled item

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| Schedule | ForeignKey | Yes | WC7JurisdictionScheduleCond | - | Foreign key target: WC7JurisdictionScheduleCond |

---

### Entity: WC7LaborContact

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7LaborContact.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WC7PolicyContactRole
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: WC7LaborContactDetail

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7LaborContactDetail.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WC7ContactDetail
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| WorkLocation | addressline | No | - | - | The address at which the employees are working |
| DescriptionOfDuties | shorttext | No | - | - | Description of Duties |
| NumberOfEmployees | positiveinteger | No | - | - | Number of employees |
| ContractEffectiveDate | dateonly | No | - | - | Effective Date |
| ContractExpirationDate | dateonly | No | - | - | Expiration Date |
| ContractProject | shorttext | No | - | - | Contract or Project |
| LaborContractorPolicyNumber | shorttext | No | - | - | - |
| Jurisdiction | TypeKey | No | - | Jurisdiction | The jurisdiction in which this contact is defined Codes (98 total): [AK, AL, AR, AZ, CA, ...] |
| EntityStatus | TypeKey | No | - | OrganizationType | Entity status Codes (16 total): [individual, partnership, corporation, association, llc, ...] |

---

### Entity: WC7LineScheduleCond

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7LineScheduleCond.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WC7WorkersCompCond
**Effective-Dated Container Branch Field:** N/A
**Description:** WC7 Line Condition with a schedule

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| WC7LineScheduleCondItems | WC7LineScheduleCondItem | Condition scheduled items |

---

### Entity: WC7LineScheduleCondItem

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7LineScheduleCondItem.eti`
**Entity Type:** `effdated`
**Database Table:** `wc7lineschedconditem`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** WC7 Line level condition scheduled item

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| Schedule | ForeignKey | Yes | WC7LineScheduleCond | - | Foreign key target: WC7LineScheduleCond |

---

### Entity: WC7LineScheduleCov

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7LineScheduleCov.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WC7WorkersCompCov
**Effective-Dated Container Branch Field:** N/A
**Description:** WC7 Line Coverage with a schedule

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| WC7LineScheduleCovItems | WC7LineScheduleCovItem | Coverage scheduled items |

---

### Entity: WC7LineScheduleCovItem

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7LineScheduleCovItem.eti`
**Entity Type:** `effdated`
**Database Table:** `wc7lineschedcovitem`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** WC7 Line level coverage scheduled item

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| Schedule | ForeignKey | Yes | WC7LineScheduleCov | - | Foreign key target: WC7LineScheduleCov |

---

### Entity: WC7LineScheduleExcl

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7LineScheduleExcl.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WC7WorkersCompExcl
**Effective-Dated Container Branch Field:** N/A
**Description:** WC7 Line Exclusion with a schedule

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| WC7LineScheduleExclItems | WC7LineScheduleExclItem | Exclusion scheduled items |

---

### Entity: WC7LineScheduleExclItem

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7LineScheduleExclItem.eti`
**Entity Type:** `effdated`
**Database Table:** `wc7lineschedexclitem`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** WC7 Line level exclusion scheduled item

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| Schedule | ForeignKey | Yes | WC7LineScheduleExcl | - | Foreign key target: WC7LineScheduleExcl |

---

### Entity: WC7ManuscriptOption

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7ManuscriptOption.eti`
**Entity Type:** `effdated`
**Database Table:** `wc7manuscriptoption`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Workers' Comp Manuscript Data

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| Description | longtext | No | - | - | The description of the manuscript endorsement |
| Premium | money | No | - | - | The cost associate with the manuscript endorsement |
| WC7Line | ForeignKey | Yes | WC7WorkersCompLine | - | Foreign key target: WC7WorkersCompLine |

---

### Entity: WC7MaritimeCovEmpCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7MaritimeCovEmpCost.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WC7Cost
**Effective-Dated Container Branch Field:** N/A
**Description:** A unit of price for a period of time, not to be broken up any further, for a Maritime Workers' Comp employee coverage

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| WC7MaritimeCoveredEmployee | ForeignKey | Yes | WC7MaritimeCoveredEmployee | - | Foreign key target: WC7MaritimeCoveredEmployee |
| WC7MaritimeCov | ForeignKey | Yes | WC7WorkersCompCov | - | Foreign key target: WC7WorkersCompCov |
| WC7MaritimeCovEmpCostType | TypeKey | Yes | - | WC7MaritimeCovEmpCostType | Codes: [MaritimeCovEmp, IncreasedLimitsFactor, SupplementalDisease] |

---

### Entity: WC7MaritimeCoveredEmployee

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7MaritimeCoveredEmployee.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WC7CoveredEmployeeBase
**Effective-Dated Container Branch Field:** N/A
**Description:** A Workers' Comp Maritime Covered Employee

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Vessel | shorttext | No | - | - | Its the vessel associated with this exposure |
| MaritimeCoverage | ForeignKey | Yes | WC7WorkersCompCov | - | The parent coverage for maritime covered employees |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| WC7Costs | WC7MaritimeCovEmpCost | Child collection |

---

### Entity: WC7Modifier

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7Modifier.eti`
**Entity Type:** `effdated`
**Database Table:** `wc7modifier`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A line-level modifier for Workers' Comp

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| WC7Jurisdiction | ForeignKey | Yes | WC7Jurisdiction | - | Foreign key target: WC7Jurisdiction |
| ExperienceModifierStatus | TypeKey | Yes | - | WC7ExpModStatus | Default: Final Experience Modifier Status Codes: [Preliminary, Final, Contingent] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| WC7RateFactors | WC7RateFactor | Individual components of the rating factor |

---

### Entity: WC7ModifierCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7ModifierCost.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WC7JurisdictionCost
**Effective-Dated Container Branch Field:** N/A
**Description:** A unit of price for a period of time, not to be broken up any further, for jurisdiction-level modifiers for Workers Comp

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| WC7Modifier | ForeignKey | Yes | WC7Modifier | - | Foreign key target: WC7Modifier |

---

### Entity: WC7ParticipatingPlan

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7ParticipatingPlan.eti`
**Entity Type:** `effdated`
**Database Table:** `wc7participatingplan`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A Workers' Comp participating plan

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| LossConversionFactor | decimal | No | - | - | Loss Conversion Factor |
| Retention | decimal | No | - | - | The retention amount (percent) |
| WC7WorkersCompLine | ForeignKey | Yes | WC7WorkersCompLine | - | Foreign key target: WC7WorkersCompLine |
| PlanID | TypeKey | Yes | - | WC7ParticipatingPlanID | The ID of this participating plan Codes: [1ystd, 2ystd, 3ystd] |

---

### Entity: WC7PolicyContactRole

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7PolicyContactRole.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PolicyContactRole
**Effective-Dated Container Branch Field:** N/A
**Description:** A PolicyContactRole specific to a WorkersComp policy line.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| WC7WorkersCompLine | ForeignKey | No | WC7WorkersCompLine | - | The workers comp policy line this contact role is associated with. |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| WC7Details | WC7ContactDetail | Child collection |

---

### Entity: WC7PolicyLaborClient

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7PolicyLaborClient.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WC7LaborContact
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: WC7PolicyLaborContractor

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7PolicyLaborContractor.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WC7LaborContact
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: WC7PolicyOwnerOfficer

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7PolicyOwnerOfficer.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WC7PolicyContactRole
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| WC7OwnershipPct | integer | No | - | - | Ownership percentage |
| RelationshipTitleInternal | TypeKey | No | - | Relationship | The relationship Codes (54 total): [AmbEmp, ApptOff, AuxPD, BdTrMbr, CEO, ...] |
| Jurisdiction | TypeKey | No | - | Jurisdiction | The jurisdiction in which this contact is defined Codes (98 total): [AK, AL, AR, AZ, CA, ...] |

---

### Entity: WC7PremiumDiscount

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7PremiumDiscount.eti`
**Entity Type:** `effdated`
**Database Table:** `wc7premiumdiscount`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** The premium discount rate calculated in the last promoted job (submission/policy change/issuance) for a rating period and jurisdiction used by premium reports.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| StartDate | datetime | Yes | - | - | The start date of the rating period that the discount was calculated for. |
| EndDate | datetime | Yes | - | - | The end date of the rating period that the discount was calculated for. |
| DiscountRate | decimal | No | - | - | Premium discount rate used for this rating period. |
| WC7Jurisdiction | ForeignKey | Yes | WC7Jurisdiction | - | The jurisdiction to which this rating period belongs. |

---

### Entity: WC7RateFactor

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7RateFactor.eti`
**Entity Type:** `effdated`
**Database Table:** `wc7ratefactor`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A rate factor is a risk characteristic and its associated numeric value which might have an impact on premium. As used here rate factors are applied to base premium rather than rates. A common example of Rate Factors are the components of IRPM (individual risk premium modifier).

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| WC7Modifier | ForeignKey | Yes | WC7Modifier | - | Foreign key target: WC7Modifier |

---

### Entity: WC7RatingPeriodStartDate

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7RatingPeriodStartDate.eti`
**Entity Type:** `effdated`
**Database Table:** `wc7ratingperiodstartdate`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A date which marks the beginning of a new rating period. During a rating period the basis amounts for basis-scalable exposures are typically constant.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| StartDate | datetime | Yes | - | - | Date this rating period takes effect. |
| WC7Jurisdiction | ForeignKey | Yes | WC7Jurisdiction | - | The jurisdiction to which this rating period belongs. |
| Type | TypeKey | Yes | - | RPSDType | The type of RPSD (anniversary date, forced re-rate, etc) Codes: [anniversary, forcedrerating, latemod, audit] |

---

### Entity: WC7RatingStepExt

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7RatingStepExt.eti`
**Entity Type:** `keyable`
**Database Table:** `wc7sample_WCRatingStep`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| rateState | varchar | No | - | - | Indicates a row is applicable to a given jurisdiction.  Null indicates a default row which is applicable to all jurisdictions which have no jurisdiction-specific rows for the given effective date. This should be the string value of a typecode in the Jurisdiction typelist. For example, if this is a typecode allowed in the US state of California, the value should be 'CA'. |
| effDate | datetime | No | - | - | The date on which this factor becomes effective (inclusive).  A null date means this has always been effective. |
| expDate | datetime | No | - | - | The date on which this factor expires (exclusive).  A null date means this will always be effective. |
| calcOrder | integer | Yes | - | - | Determines the order in which the steps should be executed. |
| customAction | varchar | No | - | - | If stepAction is Custom, then this indicates which custom action to execute. |
| modifierID | varchar | No | - | - | Should match the modifier pattern's public ID.  If stepAction is Modifier, then this should be non-null to indicate which modifier to look-up for the calculation. |
| factorName | varchar | No | - | - | This field should match the factorName for the correct factor in RateAdjFactor.  Used for taxes and fees.  Also used if the modifier is a boolean type because, if true, the system needs to look up the rate to apply. |
| classcode | varchar | No | - | - | Indicates the class code that should be used for the resulting premiums, if any.  Should be non-null unless this row is not expected to result in a new rating line (e.g. just stores a sub-total). |
| description | varchar | No | - | - | If non-null, this description will be used instead of that of the AggRatingLineType for describing the resulting premiums. |
| includeInReports | bit | No | - | - | Default: true Indicates whether or not this rating step should be performed for premium report jobs |
| stepAction | TypeKey | Yes | - | WCRateStepAction | Explains what action should be taken for this step.  Some steps reuse generic actions and others require a Custom action. Codes: [subtotal, modifier, fee, custom] |
| subtotal | TypeKey | No | - | RateSubtotalType | If step action is Subtotal, then this defines which subtotal to calc and store.  Other step actions also optionally use this to lookup a previously saved subtotal as the basis for the step's calculation. Codes (11 total): [total_premium, wc_manual, wc_subject, wc_modified, wc_standard, ...] |
| rateConversionType | TypeKey | No | - | RateConversionType | If step action looks up a rate and uses it to calculate a new amount, then this field defines how the rate should be interpreted.  (See typelist for a description of options.) Codes: [as_is, diff_from_1, credit] |
| aggCostType | TypeKey | No | - | WC7JurisdictionCostType | Indicates the type of aggregate cost (not specific to a single location/class code exposure unit) to be used for the resulting costs, if any.  Should be non-null unless this row is not expected to result in a new cost (e.g. just stores a sub-total). Codes (25 total): [MinPrem, MinPremFELAMaritime, CancelShortRatePenalty, Tax, CIGA, ...] |
| amountType | TypeKey | No | - | RateAmountType | Indicates the type (standard vs non-standard premium or taxes/surcharges) of the amount calculated, if any.  Should be non-null unless this row is not expected to result in a new rating line (e.g. just stores a sub-total). Codes: [StdPremium, NonstdPremium, TaxSurcharge] |

---

### Entity: WC7RetroRatingLetterOfCredit

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7RetroRatingLetterOfCredit.eti`
**Entity Type:** `effdated`
**Database Table:** `wc7letterofcredit`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A Letter Of Credit

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| Amount | money | No | - | - | The amount this letter is providing |
| IssuerName | shorttext | No | - | - | The name of the issuer |
| ValidFrom | datetime | Yes | - | - | Date (inclusive) from which this letter of credit is valid. |
| ValidTo | datetime | Yes | - | - | Date (exclusive) at which this letter of credit is no longer valid. |
| WC7RetrospectiveRatingPlan | ForeignKey | Yes | WC7RetrospectiveRatingPlan | - | The retro plan for which this letter applies |

---

### Entity: WC7RetrospectiveRatingPlan

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7RetrospectiveRatingPlan.eti`
**Entity Type:** `effdated`
**Database Table:** `wc7retroratingplan`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A plan for retrospectively rating a policy line

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BasicPremiumFactor1 | decimal | No | - | - | The (50%) premium factor |
| BasicPremiumFactor2 | decimal | No | - | - | The (100%) premium factor |
| BasicPremiumFactor3 | decimal | No | - | - | The (150%) premium factor |
| ComputationInterval | integer | No | - | - | The computation interval |
| EstimatedStandardPremium | money | No | - | - | The estimated standard premium |
| FirstComputationDate | datetime | No | - | - | The data of the first computation |
| IncludeALAE | bit | No | - | - | Include ALocated Loss Adjustment |
| LastComputationDate | datetime | No | - | - | The data of the last computation |
| LossConversionFactor | decimal | No | - | - | Loss Conversion Factor |
| LossLimitAmount | money | No | - | - | Loss limitation amount |
| MaxRetroPremiumRatio | decimal | No | - | - | The maximum retro premium ratio |
| MinRetroPremiumRatio | decimal | No | - | - | The minimum retro premium ratio |
| PercentStandardPremium1 | decimal | No | - | - | Default: 50 The (50%) standard premium |
| PercentStandardPremium2 | decimal | No | - | - | Default: 100 The (100%) standard premium |
| PercentStandardPremium3 | decimal | No | - | - | Default: 150 The (150%) standard premium |
| WC7WorkersCompLine | ForeignKey | Yes | WC7WorkersCompLine | - | Foreign key target: WC7WorkersCompLine |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| LettersOfCredit | WC7RetroRatingLetterOfCredit | The list of Letters Of Credit |
| JurisdictionMultipliers | WC7JurisdictionMultiplier | The list of Multipliers by Jurisdiction |

---

### Entity: WC7ScheduledItem

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7ScheduledItem.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| IntCol2 | integer | No | - | - | Integer field2 |
| ClassCode | ForeignKey | No | WC7ClassCode | - | Foreign key target: WC7ClassCode |

---

### Entity: WC7StateConfigLookup

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7StateConfigLookup.eti`
**Entity Type:** `retireable`
**Database Table:** `wc7stateconfiglookup`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Indicates which WC7StateConfig class to use for a jurisdiction

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| ConfigClass | className | Yes | - | - | Subtype of WC7StateConfig |
| Jurisdiction | TypeKey | Yes | - | Jurisdiction | Jurisdiction Codes (98 total): [AK, AL, AR, AZ, CA, ...] |

---

### Entity: WC7SupplDiseaseCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7SupplDiseaseCost.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WC7Cost
**Effective-Dated Container Branch Field:** N/A
**Description:** A unit of price for a period of time, not to be broken up any further, for a Supplementary Disease

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| WC7SupplDiseaseExposure | ForeignKey | Yes | WC7SupplDiseaseExposure | - | Foreign key target: WC7SupplDiseaseExposure |

---

### Entity: WC7SupplDiseaseExposure

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7SupplDiseaseExposure.eti`
**Entity Type:** `effdated`
**Database Table:** `wc7suppldiseaseexp`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A Workers' Comp Disease Exposure

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BasisAmount | integer | No | - | - | Basis Amount |
| IfAnyExposure | bit | No | - | - | Default: false Option to indicate that coverage is provided with precise liability to be determined later (at audit) |
| DiseaseCode | ForeignKey | No | WC7DiseaseCode | - | Disease Code of exposure |
| Location | ForeignKey | Yes | PolicyLocation | - | Location of exposure. |
| WCLine | ForeignKey | Yes | WC7WorkersCompLine | - | Foreign key target: WC7WorkersCompLine |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Costs | WC7SupplDiseaseCost | Child collection |

---

### Entity: WC7TerrorismCovCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7TerrorismCovCost.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WC7CovCost
**Effective-Dated Container Branch Field:** N/A
**Description:** A unit of price for a period of time, not to be broken up any further, for Terrorism Risk Insurance Act Endorsement

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Jurisdiction | TypeKey | Yes | - | Jurisdiction | The jurisdiction this cost applies to Codes (98 total): [AK, AL, AR, AZ, CA, ...] |

---

### Entity: WC7Transaction

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7Transaction.eti`
**Entity Type:** `effdated`
**Database Table:** `wc7transaction`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A transaction for the Workers' Comp line

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| WC7Cost | ForeignKey | Yes | WC7Cost | - | The cost this transaction modifies. |

---

### Entity: WC7WaiverOfSubro

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7WaiverOfSubro.eti`
**Entity Type:** `effdated`
**Database Table:** `wc7waiverofsubro`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A Workers' Comp Waiver of Subrogation

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BasisAmount | integer | No | - | - | Basis Amount |
| Description | shorttext | No | - | - | Description |
| IfAnyExposure | bit | No | - | - | Default: false Option to indicate that coverage is provided with precise liability to be determined later (at audit) |
| JobID | shorttext | No | - | - | The job identifier |
| NumEmployees | positiveinteger | No | - | - | Number of employees |
| SpecificDiseaseLoaded | bit | No | - | - | Default: false Option to indicate that coverage is specific disease loaded |
| WaiverCondition | ForeignKey | Yes | WC7WorkersCompCond | - | The parent condition for waivers |
| ClassCode | ForeignKey | No | WC7ClassCode | - | Class Code of covered employees |
| WCLine | ForeignKey | Yes | WC7WorkersCompLine | - | Foreign key target: WC7WorkersCompLine |
| GoverningLaw | TypeKey | Yes | - | WC7GoverningLaw | Special Coverage Class for this set of employees Codes (11 total): [state, defenseBaseAct, fedCoalMine, longshoreAndHarbor, migrantAndSeasonalAgricultural, ...] |
| Jurisdiction | TypeKey | No | - | Jurisdiction | Codes (98 total): [AK, AL, AR, AZ, CA, ...] |
| Type | TypeKey | No | - | WC7WaiverOfSubrogation | The type of waiver of subro. Codes: [blanket, specific] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| WaiverOfSubroCosts | WC7WaiverOfSubroCost | Child collection |

---

### Entity: WC7WaiverOfSubroCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7WaiverOfSubroCost.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WC7JurisdictionCost
**Effective-Dated Container Branch Field:** N/A
**Description:** A unit of price for a period of time, not to be broken up any further, for a Waiver of Subrogation

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| WC7WaiverOfSubro | ForeignKey | Yes | WC7WaiverOfSubro | - | Foreign key target: WC7WaiverOfSubro |

---

### Entity: WC7WaiverOfSubroSpecificBalanceCost

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7WaiverOfSubroSpecificBalanceCost.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WC7JurisdictionCost
**Effective-Dated Container Branch Field:** N/A
**Description:** A unit of price for a period of time, not to be broken up any further, to balance a Waiver of Subrogation to the Minimum

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| JobID | shorttext | No | - | - | The job identifier |

---

### Entity: WC7WorkersCompCond

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7WorkersCompCond.eti`
**Entity Type:** `effdated`
**Database Table:** `wc7linecond`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A line-level condition for Workers' Comp

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BooleanTerm1 | bit | No | - | - | boolean cov term field |
| BooleanTerm1Avl | bit | No | - | - | whether or not the BooleanTerm1 field was available the last time availability was checked |
| BooleanTerm2 | bit | No | - | - | boolean cov term field |
| BooleanTerm2Avl | bit | No | - | - | whether or not the BooleanTerm2 field was available the last time availability was checked |
| ChoiceTerm1 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm1Avl | bit | No | - | - | whether or not the ChoiceTerm1 field was available the last time availability was checked |
| ChoiceTerm2 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm2Avl | bit | No | - | - | whether or not the ChoiceTerm2 field was available the last time availability was checked |
| DirectTerm1 | decimal | No | - | - | direct cov term field |
| DirectTerm1Avl | bit | No | - | - | whether or not the DirectTerm1 field was available the last time availability was checked |
| DirectTerm2 | decimal | No | - | - | direct cov term field |
| DirectTerm2Avl | bit | No | - | - | whether or not the DirectTerm2 field was available the last time availability was checked |
| DateTerm1 | datetime | No | - | - | datetime cov term field |
| DateTerm1Avl | bit | No | - | - | whether or not the DateTerm1 field was available the last time availability was checked |
| DateTerm2 | datetime | No | - | - | datetime cov term field |
| DateTerm2Avl | bit | No | - | - | whether or not the DateTerm2 field was available the last time availability was checked |
| DirectTerm3 | decimal | No | - | - | direct cov term field |
| DirectTerm3Avl | bit | No | - | - | whether or not the DirectTerm3 field was available the last time availability was checked |
| StringTerm1 | shorttext | No | - | - | string cov term field |
| StringTerm1Avl | bit | No | - | - | whether or not the StringTerm1 field was available the last time availability was checked |
| StringTerm2 | shorttext | No | - | - | string cov term field |
| StringTerm2Avl | bit | No | - | - | whether or not the StringTerm2 field was available the last time availability was checked |
| WCLine | ForeignKey | No | WC7WorkersCompLine | - | Foreign key target: WC7WorkersCompLine |

---

### Entity: WC7WorkersCompCov

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7WorkersCompCov.eti`
**Entity Type:** `effdated`
**Database Table:** `wc7workerscompcov`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A line-level coverage for Workers' Comp

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BooleanTerm1 | bit | No | - | - | boolean cov term field |
| BooleanTerm2 | bit | No | - | - | boolean cov term field |
| DirectTerm1 | decimal | No | - | - | direct cov term field |
| DirectTerm1Avl | bit | No | - | - | whether or not the DirectTerm1 field was available the last time availability was checked |
| DirectTerm2 | decimal | No | - | - | direct cov term field |
| DirectTerm2Avl | bit | No | - | - | whether or not the DirectTerm2 field was available the last time availability was checked |
| DirectTerm3 | decimal | No | - | - | direct cov term field |
| DirectTerm3Avl | bit | No | - | - | whether or not the DirectTerm3 field was available the last time availability was checked |
| StringTerm1 | shorttext | No | - | - | string cov term field |
| StringTerm1Avl | bit | No | - | - | whether or not the StringTerm1 field was available the last time availability was checked |
| StringTerm2 | shorttext | No | - | - | string cov term field |
| StringTerm2Avl | bit | No | - | - | whether or not the StringTerm2 field was available the last time availability was checked |
| StringTerm3 | shorttext | No | - | - | string cov term field |
| StringTerm3Avl | bit | No | - | - | whether or not the StringTerm3 field was available the last time availability was checked |
| ChoiceTerm1 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm1Avl | bit | No | - | - | whether or not the ChoiceTerm1 field was available the last time availability was checked |
| ChoiceTerm2 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm2Avl | bit | No | - | - | whether or not the ChoiceTerm2 field was available the last time availability was checked |
| ChoiceTerm3 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm3Avl | bit | No | - | - | whether or not the ChoiceTerm3 field was available the last time availability was checked |
| ChoiceTerm4 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm4Avl | bit | No | - | - | whether or not the ChoiceTerm4 field was available the last time availability was checked |
| FedEmpLiabLawTerm1 | patterncode | No | - | - | choice cov term field |
| FedEmpLiabLawTerm1Avl | bit | No | - | - | whether or not the FedEmpLiabLawTerm1 field was available the last time availability was checked |
| WCLine | ForeignKey | No | WC7WorkersCompLine | - | Foreign key target: WC7WorkersCompLine |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Costs | WC7CovCost | Child collection |

---

### Entity: WC7WorkersCompExcl

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7WorkersCompExcl.eti`
**Entity Type:** `effdated`
**Database Table:** `wc7lineexcl`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** A line-level exclusion for Workers' Comp

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| BranchValue | ForeignKey | Yes | PolicyPeriod | - | Owning PolicyPeriod branch |
| EffectiveDate | datetime | Yes | - | - | Effective date of this temporal slice |
| ExpirationDate | datetime | Yes | - | - | Expiration date of this temporal slice |
| ChangeType | TypeKey | No | - | EffDatedChangeType | Type of change: slice, merge, add |
| BooleanTerm1 | bit | No | - | - | boolean cov term field |
| BooleanTerm1Avl | bit | No | - | - | whether or not the BooleanTerm1 field was available the last time availability was checked |
| BooleanTerm2 | bit | No | - | - | boolean cov term field |
| BooleanTerm2Avl | bit | No | - | - | whether or not the BooleanTerm2 field was available the last time availability was checked |
| ChoiceTerm1 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm1Avl | bit | No | - | - | whether or not the ChoiceTerm1 field was available the last time availability was checked |
| ChoiceTerm2 | patterncode | No | - | - | choice cov term field |
| ChoiceTerm2Avl | bit | No | - | - | whether or not the ChoiceTerm2 field was available the last time availability was checked |
| DirectTerm1 | decimal | No | - | - | direct cov term field |
| DirectTerm1Avl | bit | No | - | - | whether or not the DirectTerm1 field was available the last time availability was checked |
| DirectTerm2 | decimal | No | - | - | direct cov term field |
| DirectTerm2Avl | bit | No | - | - | whether or not the DirectTerm2 field was available the last time availability was checked |
| DateTerm1 | datetime | No | - | - | datetime cov term field |
| DateTerm1Avl | bit | No | - | - | whether or not the DateTerm1 field was available the last time availability was checked |
| DateTerm2 | datetime | No | - | - | datetime cov term field |
| DateTerm2Avl | bit | No | - | - | whether or not the DateTerm2 field was available the last time availability was checked |
| StringTerm1 | shorttext | No | - | - | string cov term field |
| StringTerm1Avl | bit | No | - | - | whether or not the StringTerm1 field was available the last time availability was checked |
| StringTerm2 | shorttext | No | - | - | string cov term field |
| StringTerm1Av2 | bit | No | - | - | whether or not the StringTerm1 field was available the last time availability was checked |
| WCLine | ForeignKey | No | WC7WorkersCompLine | - | Foreign key target: WC7WorkersCompLine |

---

### Entity: WC7WorkersCompLine

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WC7WorkersCompLine.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PolicyLine
**Effective-Dated Container Branch Field:** N/A
**Description:** Workers' Comp line of business.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| WC7GoverningClass | ForeignKey | No | WC7ClassCode | - | Governing Class Code of policy line. |
| EmployeeLeasingPlan | OneToOne | No | WC7EmployeeLeasingPlan | - | One-to-one link |
| ParticipatingPlan | OneToOne | No | WC7ParticipatingPlan | - | One-to-one link |
| RetrospectiveRatingPlan | OneToOne | No | WC7RetrospectiveRatingPlan | - | One-to-one link |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| WC7Jurisdictions | WC7Jurisdiction | Child collection |
| WC7AircraftSeats | WC7AircraftSeat | Child collection |
| WC7Costs | WC7Cost | Child collection |
| WC7CoveredEmployees | WC7CoveredEmployee | Child collection |
| WC7CoveredEmployeeBases | WC7CoveredEmployeeBase | Child collection |
| WC7BasicClients | WC7PolicyContactRole | Child collection |
| WC7PolicyLaborClients | WC7PolicyLaborClient | Employees that are leased by a company/person from another. |
| WC7PolicyLaborContractors | WC7PolicyLaborContractor | Employees that are contracted by a company/person to another. |
| WC7PolicyOwnerOfficers | WC7PolicyOwnerOfficer | Owner/officers on this line. |
| WC7ExcludedWorkplaces | WC7ExcludedWorkplace | Child collection |
| MultipleCoordinatedPolicies | WC7CoordinatedPolicy | Child collection |
| WC7FedCoveredEmployees | WC7FedCoveredEmployee | Child collection |
| WC7MaritimeCoveredEmployees | WC7MaritimeCoveredEmployee | Child collection |
| WC7LineCoverages | WC7WorkersCompCov | Line-level coverages for Workers' Comp. |
| WC7LineExclusions | WC7WorkersCompExcl | Line-level exclusions for Workers' Comp. |
| WC7LineConditions | WC7WorkersCompCond | Line-level conditions for Workers' Comp. |
| WC7WaiverOfSubros | WC7WaiverOfSubro | Child collection |
| WC7ManuscriptOptions | WC7ManuscriptOption | Child collection |
| WC7SupplDiseaseExposures | WC7SupplDiseaseExposure | Child collection |
| WC7AtomicEnergyExposures | WC7AtomicEnergyExposure | Child collection |

---

### Entity: WCRatingStepExt

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WCRatingStepExt.eti`
**Entity Type:** `keyable`
**Database Table:** `sample_WCRatingStep`
**Supertype:** None
**Effective-Dated Container Branch Field:** N/A
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| rateState | varchar | No | - | - | Indicates a row is applicable to a given jurisdiction.  Null indicates a default row which is applicable to all jurisdictions which have no jurisdiction-specific rows for the given effective date. This should be the string value of a typecode in the Jurisdiction typelist. For example, if this is a typecode allowed in the US state of California, the value should be 'CA'. |
| effDate | datetime | No | - | - | The date on which this factor becomes effective (inclusive).  A null date means this has always been effective. |
| expDate | datetime | No | - | - | The date on which this factor expires (exclusive).  A null date means this will always be effective. |
| calcOrder | integer | Yes | - | - | Determines the order in which the steps should be executed. |
| customAction | varchar | No | - | - | If stepAction is Custom, then this indicates which custom action to execute. |
| modifierID | varchar | No | - | - | Should match the modifier pattern's public ID.  If stepAction is Modifier, then this should be non-null to indicate which modifier to look-up for the calculation. |
| factorName | varchar | No | - | - | This field should match the factorName for the correct factor in RateAdjFactor.  Used for taxes and fees.  Also used if the modifier is a boolean type because, if true, the system needs to look up the rate to apply. |
| classcode | varchar | No | - | - | Indicates the class code that should be used for the resulting premiums, if any.  Should be non-null unless this row is not expected to result in a new rating line (e.g. just stores a sub-total). |
| description | varchar | No | - | - | If non-null, this description will be used instead of that of the AggRatingLineType for describing the resulting premiums. |
| includeInReports | bit | No | - | - | Default: true Indicates whether or not this rating step should be performed for premium report jobs |
| stepAction | TypeKey | Yes | - | WCRateStepAction | Explains what action should be taken for this step.  Some steps reuse generic actions and others require a Custom action. Codes: [subtotal, modifier, fee, custom] |
| subtotal | TypeKey | No | - | RateSubtotalType | If step action is Subtotal, then this defines which subtotal to calc and store.  Other step actions also optionally use this to lookup a previously saved subtotal as the basis for the step's calculation. Codes (11 total): [total_premium, wc_manual, wc_subject, wc_modified, wc_standard, ...] |
| rateConversionType | TypeKey | No | - | RateConversionType | If step action looks up a rate and uses it to calculate a new amount, then this field defines how the rate should be interpreted.  (See typelist for a description of options.) Codes: [as_is, diff_from_1, credit] |
| aggCostType | TypeKey | No | - | WCJurisdictionCostType | Indicates the type of aggregate cost (not specific to a single location/class code exposure unit) to be used for the resulting costs, if any.  Should be non-null unless this row is not expected to result in a new cost (e.g. just stores a sub-total). Codes (11 total): [MinPrem, CancelShortRatePenalty, Tax, CIGA, ExpenseConst, ...] |
| amountType | TypeKey | No | - | RateAmountType | Indicates the type (standard vs non-standard premium or taxes/surcharges) of the amount calculated, if any.  Should be non-null unless this row is not expected to result in a new rating line (e.g. just stores a sub-total). Codes: [StdPremium, NonstdPremium, TaxSurcharge] |

---

