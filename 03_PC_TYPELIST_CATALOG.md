# PolicyCenter Typelist Catalog

**Guidewire PolicyCenter Version:** 10.2.1.1711 (Platform 10.201.1)
**Installation Location:** `C:\GW10\PolicyCenter`
**Extraction Date:** 2026-09-26
**Total Unique Typelists Discovered:** 579

---

## Overview & Methodology

This catalog documents every verified typelist extracted from the Guidewire PolicyCenter installation metadata (`.tti`) and extension (`.ttx`) definitions. Typelists represent enumerated types in Guidewire and define valid closed sets of business values for dropdowns, status fields, policy lifecycle triggers, coverage terms, and contact classifications.

Each typelist entry contains:
1. **Typelist Name**: Identifier used in Gosu and entity XML schemas (`typelist` attribute).
2. **Source Path**: Exact file path on this VM verifying the definition.
3. **Description**: Verifiable documentation from the typelist XML metadata.
4. **Valid Codes Table**: Code, Display Name, Retired status, and synthetic generation relevance.

---

## Typelist Definitions

### Typelist: AccountOrgType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\AccountOrgType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\AccountOrgType.ttx`
**Description:** Organization type of accounts
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| individual | Individual | No | Individual |
| solepropship | Sole proprietorship | No | Sole proprietorship |
| partnership | Partnership | No | Partnership |
| corporation | Corporation - public | No | Corporation - public |
| privatecorp | Corporation - private | No | Corporation - private |
| llc | LLC | No | Limited liability company |
| jointventure | Joint venture | No | Joint venture |
| commonownership | Common ownership | No | Common ownership |
| limitedpartnership | Limited partnership | No | Limited partnership |
| trustestate | Trust or estate | No | Trust or estate |
| executortrustee | Executor or trustee | No | Executor or trustee |
| llp | LLP | No | LLP |
| government | Government entity | No | Government entity |
| nonprofit | Non or not for profit corp. | No | Non or not for profit corp |
| religious | Religious organization | No | Religious organization |
| other | Other | No | Other |

---

### Typelist: AccountPaymentMethod

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\AccountPaymentMethod.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\AccountPaymentMethod.ttx`
**Description:** Defines available payment methods
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| ach | ACH/EFT | No | ACH/EFT |
| creditcard | Credit Card | No | Credit Card |
| responsive | Send Invoice | No | Send Invoice |
| wire | Wire | Yes | Wire |
| unsupported | Unsupported | Yes | Unsupported Account PaymentMethod |

---

### Typelist: AccountRelationshipType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\AccountRelationshipType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\AccountRelationshipType.ttx`
**Description:** Type of relationship between accounts
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| parent | Parent of | No | Parent of |
| child | Child of | No | Child of |
| commonowner | Common Ownership | No | Common Ownership |

---

### Typelist: AccountStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\AccountStatus.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\AccountStatus.ttx`
**Description:** The status of the account
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Pending | Pending | No | The account is ready for data entry, but data entry is still ongoing and the account is not considered fully open. |
| Active | Active | No | The account is fully ready and open, and submissions have been created for it. |
| Withdrawn | Withdrawn | No | The account has been withdrawn from consideration for business with the carrier. |
| Merged | Merged | No | The account has been merged into another account and is available for read only access. |

---

### Typelist: ActivityCategory

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ActivityCategory.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\ActivityCategory.ttx`
**Description:** All available categories of activities
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| approval | Approval | Yes | Approval |
| correspondence | Correspondence | No | Correspondence |
| interview | Interview | No | Interview |
| newmail | New mail | No | New mail |
| reminder | Reminder | No | Reminder |
| request | Request | No | Request |
| response | Response | No | Response |
| approvaldenied | Approval denied | Yes | Approval denied |
| general | General | No | General |
| uwreview | Underwriter Review | No | An activity related to the underwriter review cycle.  Only one of these should be open against a job at a time. |

---

### Typelist: ActivityClass

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ActivityClass.tti`
**Description:** The class of the activity
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| task | Task | No | Task |
| event | Event | No | Event |

---

### Typelist: ActivityPatternLevel

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ActivityPatternLevel.tti`
**Description:** Level of the ActivityPattern.
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| All | All | No | ActivityPattern is at all level |
| Account | Account | No | ActivityPattern is at account level |
| Policy | Policy | No | ActivityPattern is at policy level |
| Job | Job | No | ActivityPattern is at job level |

---

### Typelist: ActivityStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ActivityStatus.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\ActivityStatus.ttx`
**Description:** The status of the activity
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| open | Open | No | Open |
| skipped | Skipped | No | Skipped |
| complete | Complete | No | Complete |
| canceled | Canceled | No | Canceled activity that is still visible to the user |

---

### Typelist: ActivityType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ActivityType.tti`
**Description:** The type of activity
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| general | General | No | General |
| approval | Approval | No | Approval |
| assignmentreview | Assignment Review | No | Assignment Review |
| approvaldenied | Approval Denied | No | Approval Denied |

---

### Typelist: AdditionalInsuredType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\AdditionalInsuredType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\AdditionalInsuredType.ttx`
**Description:** Different types of additional insured on a policy line or exposure unit
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| CHAR | Charitable Institutions | No | Charitable Institutions |
| CHCHVOL | Church Members, Officers and Volunteer Workers | No | Church Members, Officers and Volunteer Workers |
| CLUB | Club Members | No | Club Members |
| CONCES | Concessionaires Trading Under Your Name | No | Concessionaires Trading Under Your Name |
| CONDO | Townhouse Associations | No | Townhouse Associations |
| CONTROL | Controlling Interest | No | Controlling Interest |
| COOWN | Co-Owner of Insured Premises | No | Co-Owner of Insured Premises |
| DESIG | Designated Person or Organization | No | Designated Person or Organization |
| ELECT | Elective or Appointive Executive Officers of Public Corporation | No | Elective or Appointive Executive Officers of Public Corporation |
| ENG | Engineers, Architects or Surveyors | No | Engineers, Architects or Surveyors |
| ENGNOT | Engineers, Architects or Surveyors Not Engaged By the Named Insured | No | Engineers, Architects or Surveyors Not Engaged By the Named Insured |
| EXEC | Executors, Administrators, Trustees or Beneficiaries | No | Executors, Administrators, Trustees or Beneficiaries |
| GOVPERM | State or Political Subdivisions - Permits | No | State or Political Subdivisions - Permits |
| GOVPREM | State or Political Subdivisions - Permits Relating to Premises | No | State or Political Subdivisions - Permits Relating to Premises |
| GOVPREMOWN | State or Political Subdivisions - Permits Relating to Premises - Owner / Lessees | No | State or Political Subdivisions - Permits Relating to Premises - Owner / Lessees |
| GRANTFRAN | Grantor of Franchise | No | Grantor of Franchise |
| GRANTLICREQ | Grantor of Licenses - Automatic Status is required | No | Grantor of Licenses - Automatic Status is required |
| GRANTLICSCH | Grantor of Licenses - Scheduled | No | Grantor of Licenses - Scheduled |
| LESSEQUIP | Lessor of Leased Equipment | No | Lessor of Leased Equipment |
| LESSEQUIPAUTO | Lessor of Leased Equipment-Automatic Status When Required in Lease Agreement | No | Lessor of Leased Equipment-Automatic Status When Required in Lease Agreement |
| LESSOR | Lessor | No | Lessor |
| MGRPREM | Managers or Lessors of Premises | No | Managers or Lessors of Premises |
| MORT | Mortgagee, Assignee or Receiver | No | Mortgagee, Assignee or Receiver |
| OILGAS | Oil or Gas Operations - Nonoperating, Co-owners | No | Oil or Gas Operations - Nonoperating, Co-owners |
| OLC | Owners, Lessees or Contractors | No | Owners, Lessees or Contractors |
| OLCCOMPLETE | Owners, Lessees or Contractors - Completed Operations | No | Owners, Lessees or Contractors - Completed Operations |
| OLCCONST | Owners, Lessees or Contractors with Additional Insured Requirement In Construction Contract | No | Owners, Lessees or Contractors with Additional Insured Requirement In Construction Contract |
| OLCSCHED | Owners, Lessees or Contractors - Scheduled Person or Organization | No | Owners, Lessees or Contractors - Scheduled Person or Organization |
| OWNLAND | Owners or Other Interests From Whom Land Has Been Leased | No | Owners or Other Interests From Whom Land Has Been Leased |
| VENDOR | Vendors | No | Vendors |
| HOA | Homeowners Association | No | Homeowners Association |
| LANDLORD | Landlord | No | Landlord |
| LEASECO | Leasing Company | No | Leasing Company |
| COA | Condo Association | No | Condo Association |
| STUDENT | Student | No | Student |

---

### Typelist: AdditionalInterestType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\AdditionalInterestType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\AdditionalInterestType.ttx`
**Description:** Different types of additional interest on a policy line or exposure unit
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| CONSALE | Contract of Sale | No | Contract of Sale |
| LENDLOSS | Lenders Loss Payable | No | Lenders Loss Payable |
| LESSOR | Lessor | No | Lessor |
| LIEN | Lienholder | No | Lienholder |
| LOSSP | Loss Payee | No | Loss Payee |
| LOSSPAY | Loss Payable | No | Loss Payable |
| FIRSTMORTGAGEE | First Mortgagee | No | First Mortgagee |
| SECONDMORTGAGEE | Second Mortgagee | No | Second Mortgagee |
| THIRDMORTGAGEE | Third Mortgagee | No | Third Mortgagee |
| ADDITIONALMORTGAGEE | Additional Mortgagee | No | Additional Mortgagee |
| CERTHOLDER | Certificate Holder | No | Certificate Holder |
| THIRDPARTYDESIGNEE | Third Party Designee | No | Third Party Designee |
| LANDLORD | Landlord | No | Landlord |
| LEASINGCOMPANY | Leasing Company | No | Leasing Company |

---

### Typelist: AdditionalPropertyType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\AdditionalPropertyType.tti`
**Description:** Type of Additional Covered Property
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| building | Building | No | Building |
| personalproperty | Personal Property | No | Personal Property |

---

### Typelist: AddressType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\AddressType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\AddressType.ttx`
**Description:** Types of mailing addresses
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| home | Home | No | Home |
| business | Business | No | Business |
| other | Other | No | Other |
| billing | Billing | No | Billing |

---

### Typelist: AffinityGroupType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\AffinityGroupType.tti`
**Description:** AffinityGroupType
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Open | Open | No | Open |
| Closed | Closed | No | Closed |

---

### Typelist: AggregateLimits

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\AggregateLimits.tti`
**Description:** AggregateLimits
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Location | Location | No | Location |
| Project | Project | No | Project |

---

### Typelist: AlarmCertification

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\AlarmCertification.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\AlarmCertification.ttx`
**Description:** Alarm Certification
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| UL | UL | No | UL |

---

### Typelist: AlarmClass

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\AlarmClass.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\AlarmClass.ttx`
**Description:** Alarm class
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| A | A | No | A |
| B | B | No | B |
| C | C | No | C |
| NotULAlarm | Not UL Alarm | No | Not UL Alarm |

---

### Typelist: AlarmDescription

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\AlarmDescription.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\AlarmDescription.ttx`
**Description:** Alarm Description
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| BOT | Local and central | No | Local and central |
| CE | Central station | No | Central station |
| CEK | Central station with keys | No | Central station with keys |
| CEN | Central station without keys | No | Central station without keys |
| LIM | Limited mercantile with no guard response | No | Limited mercantile with no guard response |
| LMK | Limited mercantile with guard responses and keys | No | Limited mercantile with guard responses and keys |
| LO | Local gong without keys | No | Local gong without keys |
| LOC | Local | No | Local |
| LOK | Local gong with keys | No | Local gong with keys |
| None | No installation | No | No installation |
| POL | Police connect | No | Police connect |

---

### Typelist: AlarmGrade

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\AlarmGrade.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\AlarmGrade.ttx`
**Description:** Alarm Grade
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Premises1 | Premises 1 | No | Premises 1 |
| Premises2 | Premises 2 | No | Premises 2 |
| Premises3 | Premises 3 | No | Premises 3 |
| HoldupPanic | Holdup/panic | No | Holdup/panic |
| NotULAlarm | Not UL Alarm | No | Not UL Alarm |

---

### Typelist: AnimalBreed

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\AnimalBreed.tti`
**Description:** Animal Breed
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Akitas | Akitas | No | Akitas |
| BullTerriers | Bull Terriers | No | Bull Terriers |
| Chows | Chows | No | Chows |
| DobermanPinschers | Doberman Pinschers | No | Doberman Pinschers |
| GermanShepherds | German Shepherds | No | German Shepherds |
| PitBulls | Pit Bulls | No | Pit Bulls |
| Rottweilers | Rottweilers | No | Rottweilers |
| StaffordshireBullTerriers | Staffordshire Bull Terriers | No | Staffordshire Bull Terriers |
| AMixOfAnyOfTheseBreeds | A mix of any of these breeds | No | A mix of any of these breeds |
| WolfHybrids | Wolf Hybrids | No | Wolf Hybrids |
| Reptiles | Reptiles | No | Reptiles |
| Monkeys | Monkeys | No | Monkeys |
| WildCats | Wild Cats | No | Wild Cats |
| Other | Other | No | Other |

---

### Typelist: AnimalType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\AnimalType.tti`
**Description:** Animal Type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Dog | Dog | No | Dog |
| Exotic | Exotic | No | Exotic |
| Other | Other | No | Other |

---

### Typelist: AntiTheft

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\AntiTheft.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\AntiTheft.ttx`
**Description:** Anti-theft
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| anti1 | Anti-theft I | No | Anti-theft I |
| anti2 | Anti-theft II | No | Anti-theft II |
| anti3 | Anti-theft III | No | Anti-theft III |

---

### Typelist: AntiTheftType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\AntiTheftType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\AntiTheftType.ttx`
**Description:** Auto Anti Theft type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| none | None | No | None |
| alarmonly | Alarm only | No | Alarm only |
| disable | Disabling device | No | Disabling device |
| gpslocator | GPS locating device | No | GPS locating device |

---

### Typelist: APDCoreEntityType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\APDCoreEntityType.tti`
**Description:** Entries that provide core fields to APD rules
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Policy | Policy | No | Policy |
| PolicyPeriod | PolicyPeriod | No | PolicyPeriod |

---

### Typelist: APDCoreFieldType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\APDCoreFieldType.tti`
**Description:** Defines which core fields are avaiable for use in rules
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| APDProduct | Product | No | The APD product that is being used; from the Policy |
| UWCompanyCode | Underwriting Company | No | Underwriting company for the policy; from the PolicyPeriod |
| BaseState | Base Jurisdiction | No | Base jurisdiction of the policy; from the PolicyPeriod |
| PreferredCoverageCurrency | Contract Currency | No | Contract Currency (preferred coverage currency) |

---

### Typelist: APDCostDefinitionType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\APDCostDefinitionType.tti`
**Description:** Type of charge breakdown item that a cost definition row applies to
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| covcost | CoverageCost | No | Applies to coverage costs |
| cblcost | CoverableCost | No | Applies to coverable costs |
| coverage | Coverage | No | Applies to coverages |
| coverable | Coverable | No | Applies to coverables |

---

### Typelist: APDCostType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\APDCostType.tti`
**Description:** Claim cost types - matches/subset of CC CostType typelist
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| claimscost | Claim Cost | No | Loss payments to claimants or repairers |
| aoexpense | Expenses - A&O | No | Adjusting and other expenses |
| dccexpense | Expenses - D&CC | No | Defence and cost containment expenses |

---

### Typelist: APDCoverableType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\APDCoverableType.tti`
**Description:** Style of coverable, e.g. property, liability
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| prop | Property Only | No | Provides cover for loss, damage, etc. to property |
| propwithliab | Property With Associated Liability | No | Provides cover for loss, damage, etc. to property and liability associated with the property |
| liabsingle | Liability Only - Single Risk | No | Provides cover for liability for a single set of risk exposure |
| liabmulti | Liability Only - Multiple Risks | No | Provides cover for liability for a number of sets of risk exposure |
| comb | Combined Property and Liability | No | A combined package of property and liability risks |
| other | Other Casualty Risk | No | Other risks that have risk groups, cover and exposure |

---

### Typelist: APDCurrencyHandling

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\APDCurrencyHandling.tti`
**Description:** Defines if the product is multi-currency
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| domestic | Domestic | No | The local (base/reporting) currency is used |
| single | Single | No | The policy simply uses the desired coverage currency |
| basicmulti | Multiple original | No | Multiple original currencies can be used with a single settlement currency |
| fullmulti | Multiple settlement and original currencies | No | Full multicurrency/multi-national risks |

---

### Typelist: APDDataExistenceType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\APDDataExistenceType.tti`
**Description:** How the data should exist
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| available | Available | No | This option is available and can be selected |
| captured | User Entered | No | This data attribute is captured in the UI |
| derived | Derived | No | This data attribute is derived and displayed. It cannot be overridden in the UI |
| hidden | Hidden | No | This data attribute is derived and stored but not shown on the UI |
| unavailable | Unavailable | No | This entity/term is unavailable and cannot be added |
| required | Required | No | This data is captured and required/clause is required |
| suggested | Suggested | No | It is suggested that this data is captured/clause included |
| optional | Optional | No | Is optionally captured/clause may be optionally included |
| capturedbind | User Entered: Required for Bind | No | This data attribute is captured in the UI and is required to bind |
| capturedissue | User Entered: Required for Issue | No | This data attribute is captured in the UI and is required to issue |
| capturedquote | User Entered: Required for Quote | No | This data attribute is captured in the UI and is required to quote |

---

### Typelist: APDDropDownType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\APDDropDownType.tti`
**Description:** The kind of drop down (only really applicable to clause terms as fields can only be a typelist)
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| typelist | Typelist | No | This dropdown is populated and managed by a typelist |
| option | Option | No | Option term |
| package | Package | No | Package term |

---

### Typelist: APDExposureContactRole

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\APDExposureContactRole.tti`
**Description:** The role of the contact where a contact is the exposure
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| driver | Driver | No | The exposure is a named driver |
| named | Named Insured | No | The exposure is a named insured |

---

### Typelist: APDExposureRatingType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\APDExposureRatingType.tti`
**Description:** Defines if term rates or basis irrespective of terms is used for rating (or mixed)
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| term | Pro-rata for term | No | Term premiums are calculated and then pro-rated for the term |
| basis | Scaled within period | No | Rated on the basis amount irrespective of term |
| mixed | Mixed rating | No | Pro-ration or basis scaled rated is determined by the individual exposure |

---

### Typelist: APDExposureType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\APDExposureType.tti`
**Description:** Type of exposure, e.g. liability risk or property risk
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| liab | Liability | No | Provides an exposure to liability |
| prop | Property | No | Provides an exposure to property loss/damage |
| contact | Party | No | A specific party is the exposure |
| other | Other | No | Some other type of exposure |

---

### Typelist: APDFieldType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\APDFieldType.tti`
**Description:** The type of field
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| varchar | Text | No | A name or description consisting of characters, numbers, etc |
| integer | Number | No | A number with no decimal places |
| bigdecimal | Decimal (14,2) | No | An amount or percentage with up to 2 decimal places |
| boolean | True/false | No | A true/false indicator |
| date | Date-time | No | A date, optionally with the time |
| money | Monetary amount | No | An amount in the chosen currency |
| typekey | Drop-down list | No | A list of choices to select from |
| location | Location | No | A location of the risk |
| party | Involved party | No | An involved party attaching as a PolicyContactRole |

---

### Typelist: APDFunctionType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\APDFunctionType.tti`
**Description:** The type of the function used for a calculated value
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| min | Minimum | No | Find the minimum in a set of values |
| max | Maximum | No | Find the maximum in a set of values |
| sum | Sum | No | Find the sum of all values in a set |

---

### Typelist: APDLossType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\APDLossType.tti`
**Description:** All available types of claims - matches/subset of CC LossType typelist
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| AUTO | Auto | No | Auto |
| GL | Liability | No | Liability |
| PR | Property | No | Property |
| TRAV | Travel | No | Travel |
| WC | Workers' Comp | No | Workers' Comp |

---

### Typelist: APDRiskLocationType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\APDRiskLocationType.tti`
**Description:** Used to define from where the location of the risk is obtained
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| isLocation | Risk is a location | Yes | The coverable is a type of location |
| isBuilding | Risk is a building at a location | Yes | The coverable is a type of building |
| refLocation | Risk includes location reference | No | The coverable includes a foreign key to a policy location that must be selected by the user |
| useParent | Risk is at parent's location | No | For the line, this is the policy base location/jurisdiction. |

---

### Typelist: APDRuleConditionOperator

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\APDRuleConditionOperator.tti`
**Description:** Types of comparisons to perform in rule conditions
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| equals | = | No | Equals |
| notEquals | != | No | Is not equal to |
| lessThan | < | No | Less than |
| lessThanOrEqual | <= | No | Less than or equal to |
| greaterThan | > | No | Greater than |
| greaterThanOrEqual | >= | No | Greater than or equal to |
| selected | Is selected | No | Is selected |
| notSelected | Is not selected | No | Is not selected |

---

### Typelist: APDRuleType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\APDRuleType.tti`
**Description:** The type of data rule being defined
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| existence | Existence | No | Data existence rule |
| default | Default | No | Default value |
| min | Minimum | No | Minimum amount for an attribute |
| max | Maximum | No | Maximum amount for an attribute |
| tag | Tag | No | Tag for an attribute |

---

### Typelist: APDRuleValueType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\APDRuleValueType.tti`
**Description:** The type of rule value
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| fixed | Fixed | No | Fixed value |
| calculated | Calculated | No | Calculated value |

---

### Typelist: APDTagApplicability

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\APDTagApplicability.tti`
**Description:** Defines whether or not a tag is applicable to its owning element
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| applies | Applies | No | Applies |
| doesnotapply | Does not apply | No | Does not apply |

---

### Typelist: APDTagType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\APDTagType.tti`
**Description:** Not specified in source
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| rate | Rate | No | Tag for rate action |
| submission | Submission | No | Tag for create submission action |
| riskscore | Risk Score | No | Tag for risk score calculation action |

---

### Typelist: ApprovalStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ApprovalStatus.tti`
**Description:** The approval status of an approvable entity
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| unapproved | Unapproved | No | Pending approval |
| approved | Approved | No | The entity has been approved |
| rejected | Rejected | No | The entity has been rejected |

---

### Typelist: ArbitrationType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ArbitrationType.tti`
**Description:** ArbitrationType
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| nonbinding | nonbinding | No | Non-binding |
| binding | binding | No | Binding |

---

### Typelist: ArchiveFinalStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ArchiveFinalStatus.tti`
**Description:** The final status of the archive store or retrieve action
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| succeeded | Succeeded | No | The store or retrieve succeeded completely |
| failedprestore | Failed Prestore | No | Something after the prepare call and before the store call failed |
| failedstore | Failed Store | No | The store failed |
| failedcommit | Failed Commit | No | The store or retrieve failed to commit |
| failedupgrade | Failed Upgraded | No | The retrieve failed to upgrade |
| failedimport | Failed Import | No | The retrieve failed to import |
| upgradewarnings | Upgraded with Warnings | No | The retrieve upgraded with warnings |

---

### Typelist: ArchiveMethod

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ArchiveMethod.tti`
**Description:** The method by which an entity should be archived.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Standard | Standard | No | The entity is to be sent to the standard archive. |
| Purge | Purge | No | The entity is to be removed from the system, permanently and unrecoverably. |

---

### Typelist: ArchiveSourceStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ArchiveSourceStatus.tti`
**Description:** The status of the archive source
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| notstarted | Not Started | No | archiving has not been started yet |
| notenabled | Not Enabled | No | archiving has not been enabled |
| notconfig | Not Configured | No | The service has not been configured |
| available | Available | No | The service is available |
| queue | Queue Available | No | The service is not available but allow queuing of user request |
| failure | Failure | No | The last attempt to archive failed |
| manually | Manually Flagged | No | The service was manually flaged unavailable |

---

### Typelist: ArchiveState

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ArchiveState.tti`
**Description:** state of the data in archive process
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| archived | Archived | No | Graph has been archived |
| retrieving | Retrieving | No | Graph is marked for retrieving |

---

### Typelist: AreaLeased

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\AreaLeased.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\AreaLeased.ttx`
**Description:** Percentage of area leased
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 100 | 100% | No | 100% |
| 90 | 90% | No | 90% |
| 80 | 80% | No | 80% |
| 70 | 70% | No | 70% |
| 60 | 60% | No | 60% |
| 50 | 50% | No | 50% |
| 40 | 40% | No | 40% |
| 30 | 30% | No | 30% |
| 20 | 20% | No | 20% |
| 10 | 10% | No | 10% |
| 0 | N/A | No | N/A |

---

### Typelist: ArrangementType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ArrangementType.tti`
**Description:** Type of arrangement of a reinsurance agreement (Treaty or Facultative).
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Treaty | Treaty | No | Treaty |
| Facultative | Facultative | No | Facultative |

---

### Typelist: AssignmentSearchType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\AssignmentSearchType.tti`
**Description:** Possible search types for assignment
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| User | User | No | User |
| Group | Group | No | Group |
| Queue | Queue | No | Queue |

---

### Typelist: AssignmentSelectionType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\AssignmentSelectionType.tti`
**Description:** Possible selection types for the assignment pop-up
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| FromList | FromList | No | FromList |
| FromSearch | FromSearch | No | FromSearch |

---

### Typelist: AssignmentStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\AssignmentStatus.tti`
**Description:** Assignment status of an assignable entity
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| assigned | Assigned | No | Entity is assigned; AssignedUserID and AssignedGroupID are both non-null |
| pendingassignment | Pending assignment | No | Assignable is waiting for its containing entity to be assigned or reviewed; AssignedUserID and AssignedGroupID may be null or non-null |
| manual | Manual | No | Entity is waiting to be manually assigned or reviewed; a non-null AssignedUserID means pending review |
| unassigned | Unassigned | No | Entity is unassigned; AssignedUserID and AssignedGroupID are both null |

---

### Typelist: AsyncQuoteIssueType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\AsyncQuoteIssueType.tti`
**Description:** All possible message types caused by asynchronous quoting
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Info | Info | No | Info message |
| Warning | Warning | No | Warning message |
| Error | Error | No | Error message |
| DisplayableException | DisplayableException | No | DisplayableException issue. This type of issue halts the quote process. |

---

### Typelist: AttachmentBasisType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\AttachmentBasisType.tti`
**Description:** Defines how applicable reinsurance agreements are determined at the time of ceding premiums or recovering on losses.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| PolicyAttachment | Policy Attachment | No | A risk on a policy is associated with an agreement based on the policy period effective date. All premiums and all losses for the period are associated with RI based on that period start date. Essentially, the entire policy is attached to an RI agreement. |
| LossDateEarned | Loss Date Attachment (Earned Premium) | No | A risk on a policy is associated with an agreement where its effective range overlaps the agreement's period.  Losses are recovered as of loss date (or claims made date).    Ceded premiums are paid based on earned premiums that fall within the treaty period. |
| LossDateWritten | Loss Date Attachment (Written Premium) | No | A risk on a policy is associated with an agreement where its effective range overlaps the agreement's period.  Losses are recovered as of loss date (or claims made date).    Ceded premiums are paid based on written premiums that fall within the treaty period. |
| CoveragePeriod | Coverage Period Attachment | No | Loss are paid if they occur within the effective dates of the agreement. Premiums are ceded based on the premium (DWP) that will be earned within the period of coverage being provided. |

---

### Typelist: AuditBusinessDayAdjust

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\AuditBusinessDayAdjust.tti`
**Description:** Audit business day adjustment
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| ActualDay | Actual Day | No | Actual Day |
| PreviousBusinessDay | Previous Business Day | No | Previous business day |
| NextBusinessDay | Next Business Day | No | Next business day |

---

### Typelist: AuditEscalationPromptType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\AuditEscalationPromptType.tti`
**Description:** The type of escalation prompt
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| DueDate | Due Date | No | Due Date |
| AuditPeriodEndDate | Audit Period End Date | No | Audit Period End Date |
| FirstEscalationDate | First Escalation Date | No | First Escalation Date |

---

### Typelist: AuditFrequency

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\AuditFrequency.tti`
**Description:** Audit frequency
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Monthly | Monthly | No | Monthly |
| Quarterly | Quarterly | No | Quarterly |

---

### Typelist: AuditIntervalComputeType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\AuditIntervalComputeType.tti`
**Description:** Audit interval computation type
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| PolicyMonth | Policy Month | No | Policy Month |
| CalendarMonth | Calendar Month | No | Calendar Month |

---

### Typelist: AuditMethod

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\AuditMethod.tti`
**Description:** Audit method
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Estimated | Estimated | No | An insured is not fully cooperative and the carrier must complete the policy based on estimated exposure amounts. |
| Physical | Physical | No | An auditor visits the insured, inspects the operations, and reviews the records. |
| Voluntary | Voluntary | No | The insured reports actual exposure amounts (Voluntary Payroll Reporting). |
| Phone | Phone | No | The auditor contacts the insured to gather audit information. |

---

### Typelist: AuditReportDateDirection

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\AuditReportDateDirection.tti`
**Description:** Audit report date direction
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Before | before | No | before |
| After | after | No | after |

---

### Typelist: AuditScheduleType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\AuditScheduleType.tti`
**Description:** Audit schedule type
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| CheckingAudit | Checking Audit | No | Checking audit |
| PremiumReport | Premium Report | No | Premium report |
| FinalAudit | Final Audit | No | Final audit |
| RetrospectiveRating | Retrospective Rating | No | Retrospective rating |

---

### Typelist: AutoIncrease

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\AutoIncrease.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\AutoIncrease.ttx`
**Description:** Automatic increase in coverages
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 0 | Decline | No | Decline |
| 2 | 2% | No | 2% |
| 4 | 4% | No | 4% |
| 6 | 6% | No | 6% |
| 8 | 8% | No | 8% |
| 10 | 10% | No | 10% |

---

### Typelist: AutoSync

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\AutoSync.tti`
**Description:** The status code for auto-sync
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Disallow | Disallow | No | Disallow |
| Allow | Allow | No | Allow |
| Suspended | Suspended | No | Suspended |

---

### Typelist: Availability

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\Availability.tti`
**Description:** The availability of an underwriting company.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| yes | Available | No | The underwriting company is available. |
| maybe | Maybe available | No | The underwriting company may be available. |
| no | Not available | No | The underwriting company is not available. |

---

### Typelist: AvailabilityType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\AvailabilityType.tti`
**Description:** Availability Type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Available | Available | No | Available |
| Unavailable | Unavailable | No | Not Available |

---

### Typelist: BAJurisdictionCostType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\BAJurisdictionCostType.tti`
**Description:** The type of cost at the BAJurisdiction level
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| CancelShortRatePenalty | Cancellation Short-Rate Penalty | No | Penalty applied for short-rate cancellations. |
| StateTax | State Tax | No | State Tax |

---

### Typelist: BankAccountType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\BankAccountType.tti`
**Description:** Defines available types of bank accounts
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| checking | Checking | No | Checking |
| savings | Savings | No | Savings |

---

### Typelist: BANonOwnedLiabCovCostType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\BANonOwnedLiabCovCostType.tti`
**Description:** The type of people that a particular non-owned auto liability coverage cost is for.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Employees | Employees | No | Employees |
| Partners | Partners | No | Partners |
| Volunteers | Volunteers | No | Volunteers |

---

### Typelist: BAPolicyType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\BAPolicyType.tti`
**Description:** Commercial Auto policy type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| BA | Business Auto | No | Business Auto |
| garage | Garagekeepers | No | Garagekeepers |
| motor | Motor Carrier and Truckers | No | Motor Carrier and Truckers |
| BAphysdam | Business Auto Physical Damage | No | Business Auto Physical Damage |

---

### Typelist: BARatedOrderType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\BARatedOrderType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\BARatedOrderType.ttx`
**Description:** The order in which a BA cost is rated.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| CoveragePremium | Coverage premiums | No | Premiums from rating coverages. |
| CancelShortRatePenalty | Cancellation short rate penalty | No | Premium from application of a cancellation short rate penalty |
| MinimumPremium | Minimum premium adjustment | No | Minimum premium adjustment |
| StateTax | State tax | No | State tax |

---

### Typelist: BasisType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\BasisType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\BasisType.ttx`
**Description:** Basis Type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| claim | Per claim | No | Per claim |
| occurrence | Per occurrence | No | Per occurrence |

---

### Typelist: BAStateCovPIPCostType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\BAStateCovPIPCostType.tti`
**Description:** The type of PIP coverage where the cost applies.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| basic | Basic | No | Basic |
| optional | Optional | No | Optional |
| income | Wage Loss | No | Wage Loss |
| medical | Medical | No | Medical |
| rehab | Rehab | No | Rehab |
| services | Services | No | Services |
| managedcare | Managed Care | No | Managed Care |
| death | Death | No | Death |
| funeral | Funeral | No | Funeral |
| guest | Guest | No | Guest |

---

### Typelist: BatchProcessType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\BatchProcessType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\BatchProcessType.ttx`
**Description:** Types of batch processes
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| ActivityEsc | Activity Escalation | No | Activity escalation monitor |
| Archive | Archiving Item Writer | No | Identify archiving work and create work items. |
| DeferredUpgradeTasks | DeferredUpgradeTasks | No | Execute database upgrade tasks that were deferred |
| BulkPurge | BulkPurge | No | Purge records through table updates |
| ProcessHistoryPurge | ProcessHistoryPurge | No | Purge batch process history data |
| WorkQueueInstrumentationPurge | WorkQueueInstrumentationPurge | No | Purge instrumentation data for work queues |
| WorkItemSetPurge | WorkItemSetPurge | No | Purge WorkItemSet data |
| DataDistribution | Data Distribution | No | Data distribution for the database |
| DBConsistencyCheck | Database Consistency Check | No | Database consistency checks |
| DBStats | Database statistics | No | Database statistics |
| MSDMVReport | Microsoft Perf Report | No | Microsoft database performance report generation |
| OraAWRReport | Oracle AWR Report | No | Oracle database AWR performance report generation |
| GroupException | Group Exception | No | Group exception Monitor |
| UserException | User Exception | No | User exception Monitor |
| Workflow | Workflow | No | Will execute the workflow writer. |
| ContactAutoSync | ContactAutoSync | No | Automatically synchronize the local contact that are out of syn and marked 'allow' auto-sync. |
| Geocode | Geocode Writer | No | Geocoding Addresses queue writer. |
| StatReport | Stat Report Writer | No | Stat Report work queue writer |
| ProcessCompletionMonitor | Process Completion Monitor | No | Invoke plugin on completion of monitored worker queue |
| PurgeProfilerData | Purge Profiler Data | No | Purge profiler data at regular intervals |
| PurgeWorkflowLogs | Purge Workflow Logs | No | Purge completed workflows logs, this executes gw.processes.PurgeWorkflowLogs.gs |
| PurgeWorkflows | Purge Workflow | No | Purge completed workflows after resetting any referenced workflows, this executes gw.processes.PurgeWorkflow.gs |
| PurgeFailedWorkItems | Purge Failed Work Items | No | Purge failed work items from all queues. |
| PurgeTransactionIds | Purge old transaction ids | No | Purge external transaction id that no longer need to be tracked, by age. |
| PopulateSearchColumns | Populate searchColumn columns | No | Populate searchColumn columns from their original sources. |
| PurgeClusterMembers | Purge Cluster Members | No | Purge old ClusterMember entities |
| PhoneNumberNormalizer | Phone number normalizer | No | Performs a normalization of phone numbers contact |
| StagingTableImport | Staging Table Import | No | Asynchronous operation on staging tables (encrypt, statistics, integrity check, load, delete excluded, populate excluded) |
| FindUsagesOfUpgradedTypecodes | FindUsagesOfUpgradedTypecodes | No | During the back out of a rolling upgrade, looks for typecodes that were inserted during the rolling upgrade. These usages need to be fixed before we can back out. |
| BackOutRollingUpgrade | BackOutRollingUpgrade | No | Back out a rolling upgrade |
| CreatePerfOnlyIndexes | Loader Create Indexes | No | Recreate perf-only indexes when the loader finishes the big insert/select from staging to operational tables |
| DestroyContactForPersonalData | Destroy Contact For Personal Data | No | Destroy contacts that have been requested by an external system |
| RemoveOldContactDestructionRequest | Purge Old Contact Destruction Request | No | Remove destruction requests for contacts that have been destroyed. |
| ArchiveReferenceTrackingSync | Archive Reference Tracking Sync | No | Ensures that the archive document references table is in sync with the archive store. |
| NotifyExternalSystemForPersonalData | Notify External System For Personal Data | No | Picks up all contact destruction tests that are in final state and notifies external system |
| OpenPolicyException | Open Policy Exception | No | Policy Exception Monitor for open policies |
| BoundPolicyException | Bound Policy Exception | No | Policy Exception Monitor for bound policies |
| ClosedPolicyException | Closed Policy Exception | No | Policy Exception Monitor for closed policies |
| PolicyRenewalStart | Policy Renewal Start | No | Policy Renewal Start monitor |
| FormTextDataDelete | Form Text Data Delete | No | Deletes orphaned, purged, or archived FormTextData |
| AuditTask | AuditTask | No | Audit task monitor |
| OverduePremiumReport | Overdue Premium Report | No | Monitor for overdue premium reports |
| TeamScreens | Team Screens | No | Collect summary counts for team screens |
| JobExpire | Job Expiration | No | Expire a job if no action has been taken upon it for a configured period of time. |
| PremiumCeding | PremiumCeding | No | Reinsurance ceding of premium |
| PolicyHoldJobEval | Policy Hold Job Evaluation | No | Evaluates jobs against the policy holds blocking it |
| AccountWithdraw | Account Withdraw Evaluation | No | Evaluates accounts and closes them. |
| ActivityRetire | Retire Activities | No | Retires canceled activities after configured time |
| ArchivePolicyTerm | Archive policy terms | No | Policy term archiving monitor |
| RestorePolicyTerm | Retrieve policy terms | No | Policy term retrieve from archive monitor |
| ImpactTestingTestPrep | Impact Testing Test Case Preparation | No | Prepares policy periods for impact testing |
| ImpactTestingTestRun | Impact Testing Test Case Run | No | Runs the test periods through the rating algorithm |
| ImpactTestingExport | Impact Testing Export | No | Exports the test periods to Excel |
| Purge | Purge | No | Purges Entities which are no longer needed |
| PurgeOrphanedPolicyPeriod | Purge Orphaned Policy Periods | No | Purges policy periods orphaned as a result of preemption |
| ResetPurgeStatusAndCheckDates | Reset Purge Status and Check Dates | No | Reset purge status and purge/prune dates on Job |
| PurgeMessageHistory | Purge Message History | No | Purges old messages from the message history table |
| PurgeWorksheets | Purge Rating Worksheets | No | Purge WorksheetContainer objects |
| ExtractWorksheets | Extract Rating Worksheets | No | Extract rating worksheet data from WorksheetContainer objects and flag these objects for purging |
| PolicyRenewalClearCheckDate | Clear Policy Renewal Check Dates | No | Clears existing Policy Renewal Check Dates |
| ApplyPendingAccountDataUpdates | Apply Pending Account Data Updates | No | Apply any of the pending updates to account data. |
| SolrDataImport | Solr Data Import | No | Performs a full data import of the app database into the Solr/Lucene index |
| PurgeQuoteClones | Purge Quote Clones | No | Purge Quote Clones: Purge temporary cloned policy periods |
| AccountHolderCount | AccountHolderCount | No | Adjust AccountHolderCount value on Contact |
| PolicyLocationsRiskAssessment | PolicyLocationsRiskAssessment | No | Retrieves risk assessments for all the locations on a policy period |
| PurgeRiskAssessmentTempStore | PurgeRiskAssessmentTempStore | No | Purges all temporary risk assessment entities |
| HandleUnresolvedContingency | Handle Unresolved Contingency | No | Handles all the contingencies which are unresolved |
| RecalculateContingencyActionStartDate | Recalculate Contingency Action Start Date | No | Recalculate action start date for all contingencies where action has not started |
| AsyncQuoting | Asynchronous Quoting | No | Quote PolicyPeriods asynchronously |
| AsyncRating | Asynchronous Rating | No | Rate PolicyPeriods asynchronously |
| BulkSubmission | Bulk Submission Job | No | This job creates documents asynchronously using Bulk API |

---

### Typelist: BatchProcessTypeUsage

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\BatchProcessTypeUsage.tti`
**Description:** This defines the usages of this typelist
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Schedulable | Schedulable | No | This indicates that this BatchProcessType is schedulable |
| UIRunnable | UI Runnable | No | This indicates that this BatchProcessType is runnable from the UI |
| APIRunnable | API Runnable | No | This indicates that this BatchProcessType is runnable from the API |
| MaintenanceOnly | Maintenance Only | No | This indicates that this BatchProcessType is only runnable while the server is at maintenance run level |

---

### Typelist: BIDependencyType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\BIDependencyType.tti`
**Description:** Business Income Dependency
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Contributing | Contributing Locations | No | Contributing Locations |
| Recipient | Recipient Locations | No | Recipient Locations |
| Manufacturing | Manufacturing Locations | No | Manufacturing Locations |
| Leader | Leader Locations | No | Leader Locations |

---

### Typelist: BillDateOrDueDateBilling

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\BillDateOrDueDateBilling.tti`
**Description:** Whether invoice dates are computed from a fixed bill date or from a fixed due date.  With BillDateBilling the bill date is specified and the due date is computed from the specified bill date. With DueDateBilling the due date is specified and the bill date is computed from the specified due date.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| BillDateBilling | Bill Date | No | Bill date billing |
| DueDateBilling | Due Date | No | Due date billing |

---

### Typelist: BillingLevel

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\BillingLevel.tti`
**Description:** Billing Level 
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Account | Account | No | All charges can share invoice streams and default unapplied |
| PolicyDefaultUnapplied | Policy (Separate Funds by Account) | No | Policies cannot share invoice streams but do share default unapplied |
| PolicyDesignatedUnapplied | Policy (Separate Funds by Policy) | No | Policies cannot share invoice streams and use their own designated unapplieds |

---

### Typelist: BillingMethod

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\BillingMethod.tti`
**Description:** Billing Method
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| DirectBill | Direct Bill | No | Direct Bill Billing Method |
| AgencyBill | Agency Bill | No | Agency Bill Billing Method |
| ListBill | List Bill | No | List Bill Billing Method |

---

### Typelist: BillingPeriodicity

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\BillingPeriodicity.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\BillingPeriodicity.ttx`
**Description:** A Periodicity is how often something happens.
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| monthly | Monthly | No | Monthly |
| everyweek | Every Week | No | Every Week |
| everyotherweek | Every Other Week | No | Every Other Week |
| twicepermonth | Twice Per Month | No | Twice Per Month |
| everyothermonth | Every Other Month | No | Every Other Month |
| quarterly | Quarterly | No | Quarterly |
| everyfourmonths | Every Four Months | No | Every Four Months |
| everysixmonths | Every Six Months | No | Every Six Months |
| everyyear | Every Year | No | Every Year |
| everyotheryear | Every Other Year | No | Every Other Year |

---

### Typelist: BillingRemainderAllocate

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\BillingRemainderAllocate.tti`
**Description:** BillingRemainderAllocate
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| SpreadAcrossInstlmnts | Spread across installments | No | Spread across installments |
| OneHundrdPctNxtInstmnt | 100% on next installment | No | 100% on next installment |

---

### Typelist: BillingTransactionType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\BillingTransactionType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\BillingTransactionType.ttx`
**Description:** Transaction type
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| deposit | Deposit | No | Deposit |
| payment | Payment w/report | No | Payment w/report |
| midtermchange | Mid-term change | No | Payment for a mid-term change |
| latefee | Late fee | No | Late fee |
| deposittransfer | Deposit transfer | No | Deposit transfer |
| depositaddition | Deposit - additional | No | Deposit - additional |
| installment | Installment | No | Installment |
| feeinstallment | Fee - installment | No | Fee - installment |
| deductibleclaim | Deductible - claim | No | Deductible - claim |
| coinsurance | Coinsurance - claim | No | Coinsurance - claim |
| premiumadditional | Premium - additional | No | Premium - additional |
| premiumreturn | Premium - return | No | Premium - return |
| assessment | Assessment - mandated | No | Assessment - mandated |
| surchargeexternal | Surcharge - mandated | No | Surcharge - mandated |
| surchargeinternal | Surcharge - company | No | Surcharge - company |
| commission | Commission | No | Commission |

---

### Typelist: BindOption

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\BindOption.tti`
**Description:** Indicates what type of binding was used for the submission
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| BindOnly | BindOnly | No | Bind Only |
| BindAndIssue | BindAndIssue | No | Bind and Issue |

---

### Typelist: BlanketGroupType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\BlanketGroupType.tti`
**Description:** Categorizes coverages for inclusion in a blanket
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| TimeElement | Time Element | No | Time Element |
| DirectLoss | Direct Loss | No | Direct Loss |

---

### Typelist: BlanketType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\BlanketType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\BlanketType.ttx`
**Description:** Blanket Type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| decline | Decline | No | Decline |
| build | Building | No | Building |
| bus | Business Personal Property | No | Business personal property |
| busbuild | Building and Contents - by building | No | Each building and business personal property |
| location | Building and Contents - by location | No | Per location: all building and business personal property |
| all | All Building and Contents | No | All building and business personal property |
| singleloc | Single Location | No | One or more buildings at this location |
| multiloc | Multiple Locations | No | One or more locations (including one or more buildings) |
| singlecov | Single Coverage | No | Single coverage |

---

### Typelist: BlockingAction

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\BlockingAction.tti`
**Description:** A list of actions to take when a question is answered incorrectly.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| warnuser | Warn user | No | Show a warning on the same page |
| blockuser | Block user | No | Show an error message and block user on a page |

---

### Typelist: BodyType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\BodyType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\BodyType.ttx`
**Description:** Body Type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| bus | Bus | No | Bus |
| convertible | Convertible | No | Convertible |
| coupe | Coupe | No | Coupe |
| fourdoor | Four-door sedan | No | Four-door sedan |
| pickup | Pickup truck | No | Pickup truck |
| suv | SUV | No | SUV |
| twodoor | Two-door sedan | No | Two-door sedan |
| van | Van | No | Van |
| wagon | Station wagon | No | Station wagon |
| tractor | Tractor | No | Tractor |
| truck | Truck | No | Truck |
| trailer | Trailer | No | Trailer |
| util-trailer | Utility trailer | No | Utility trailer |
| motorcycle | Motorcycle | No | Motorcycle |
| atv | ATV | No | All Terrain Vehicle |
| snowmobile | Snowmobile | No | Snowmobile |
| rv | RV/Motor Home | No | RV/Motor Home |

---

### Typelist: BOPConstructionType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\BOPConstructionType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\BOPConstructionType.ttx`
**Description:** Types of building construction
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| F | Frame | No | Frame |
| JM | Joisted masonry | No | Joisted masonry |
| MNC | Masonry non-combustible | No | Masonry non-combustible |
| NC | Non-combustible | No | Non-combustible |
| R | Fire resistive/superior | No | Fire resistive/superior |

---

### Typelist: BreakerType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\BreakerType.tti`
**Description:** Circuit Breakers or Fuses
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| CircuitBreaker | Circuit Breaker | No | Circuit Breaker |
| Fuses | Fuses | No | Fuses |

---

### Typelist: BuildingAlarmType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\BuildingAlarmType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\BuildingAlarmType.ttx`
**Description:** Building alarm type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| local | Local | No | Local |
| central | Central station | No | Central station |
| police | Police station | No | Police station |

---

### Typelist: BuildingImprType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\BuildingImprType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\BuildingImprType.ttx`
**Description:** Types of building improvements
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Heating | Heating | No | Heating |
| Plumbing | Plumbing | No | Plumbing |
| Roofing | Roofing | No | Roofing |
| Wiring | Wiring | No | Wiring |
| Other | Other | No | Other |

---

### Typelist: BuildingSideType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\BuildingSideType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\BuildingSideType.ttx`
**Description:** Building sides
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Front | Front | No | Front |
| Rear | Rear | No | Rear |
| Left | Left | No | Left |
| Right | Right | No | Right |

---

### Typelist: BurglarAlarmType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\BurglarAlarmType.tti`
**Description:** Burglar Alarm Type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| police | Police Station | No | Connected to Police Station |
| central | Central Station | No | Connected to Central Station |
| local | Local | No | Local |
| none | None | No | None |

---

### Typelist: BurglarySafeguard

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\BurglarySafeguard.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\BurglarySafeguard.ttx`
**Description:** Burglary safeguard
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| WatchmanSignal | Watchman w/signal | No | Watchman w/signal |
| WatchmanClock | Watchman w/clock | No | Watchman w/clock |
| Watchman | Watchman | No | Watchman |
| NoWatchman | No Watchman | No | No Watchman |

---

### Typelist: BusinessClass

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\BusinessClass.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\BusinessClass.ttx`
**Description:** Business Class
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| manufacturer | Manufacturer | No | Manufacturer |
| wholesaler | Wholesaler | No | Wholesaler |
| insuranceAgent | Insurance Agent | No | Insurance Agent |
| other | Other | No | Other |

---

### Typelist: BusinessType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\BusinessType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\BusinessType.ttx`
**Description:** Types of external organizations
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| insurer | Insurer | No | This is the one true carrier, one and only one of these should be defined, and it should be defined in the bootstrap. |
| agency | Agency | No | This is an agency |
| broker | Broker | No | This is a broker |
| mga | Managing general agent | No | Managing general agent |
| feeaudit | Fee audit company | No | Fee audit company |
| feeinspect | Fee inspection company | No | Fee inspection company |

---

### Typelist: BusinessTypeCategory

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\BusinessTypeCategory.tti`
**Description:** The categories of external organizations defininig behavior
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| carrier | Carrier | No | This is the one true carrier, it should be defined in the bootstrap |
| producer | Producer | No | This is an organization that has produces work and therefore has producer codes |

---

### Typelist: CalcRoutineParamName

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\CalcRoutineParamName.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\CalcRoutineParamName.ttx`
**Description:** Used for defining the parameter names that can be set in a calculation parameter set
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| policyline | PolicyLine | No | Policy Line |
| ratedate | RateDate | No | Rate Date |
| coverage | Coverage | No | Coverage |
| costdata | CostData | No | CostData |
| ratinginfo | RatingInfo | No | Rating Information |
| taxablebasis | TaxableBasis | No | Taxable Basis |
| state | State | No | State |
| previoustermamount | PreviousTermAmount | No | Previous term amount, e.g. for renewal capping |
| vehicle | Vehicle | No | Vehicle |
| papipnj | PIPNJCoverage | No | PA PIP New Jersey Coverage |
| building | Building | No | Building |
| cpbldgcov | CPBldgCoverage | No | CP Building Coverage |
| cpbppcov | CPBPPCoverage | No | CP Business Personal Property Coverage |
| cpdeductfactorname | CPDeductibleFactorName | No | CP Deductible Factor Name |
| driverassignmentinfo | DriverAssignmentInfo | No | Driver Assignment Information |
| assigneddriver | AssignedDriver | No | Assigned Driver |
| currentdriver | CurrentDriver | No | Current Driver |
| wc7affinitygroup | WC7AffinityGroup | No | Groups and Associations eligible for dividends or special rating. |
| wc7affinitygroupjurisdiction | WC7AffinityGroupJurisdiction | No | Jurisdictions that a particular affinity group is available to. |
| wc7affinitygroupproducercode | WC7AffinityGroupProducerCode | No | The producer code to affinity group availability relationship. |
| wc7affinitygroupproduct | WC7AffinityGroupProduct | No | Products that a particular affinity group is available to.. |
| wc7affinitygrouptype | WC7AffinityGroupType | No | WC7AffinityGroupType |
| wc7aircraftseat | WC7AircraftSeat | No | Workers' Comp Aircraft Seat Data |
| wc7aircraftseatsurchargemaximum | WC7AircraftSeatSurchargeMaximum | No | Workers' Comp Aircraft Seat Maximum Surcharge Lookup Value |
| wc7aircraftmaximumadjustment | WC7AircraftMaximumAdjustment | No | Workers' Comp Amount to Adjust Aircraft Cost by to cap at Maximum Surcharge over Period |
| wc7cededpremium | WC7CededPremium | No | A Workers' Comp implementation of the RICededPremium delegate |
| wc7cededpremiumhistory | WC7CededPremiumHistory | No | A Workers' Comp implementation of the RICededPremiumHistory delegate |
| wc7cededpremiumtransaction | WC7CededPremiumTransaction | No | A Workers' Comp implementation of the RICededPremiumTransaction delegate |
| wc7classcode | WC7ClassCode | No | Workers' comp class codes.  Premium calculations are driven by class codes and both premium and losses are reported by class codes to rating bureaus. |
| wc7classcodefeddomains | WC7ClassCodeFedDomains | No | A type of class code (FELA, Maritime, etc) |
| wc7classcodeprogramtype | WC7ClassCodeProgramType | No | Types of programs |
| wc7classcodetype | WC7ClassCodeType | No | Types of class codes |
| wc7cost | WC7Cost | No | A WorkersComp unit of price for a period of time that should not be broken up any further. |
| wc7covempcost | WC7CovEmpCost | No | A unit of price for a period of time, not to be broken up any further, for a Workers' Comp employee coverage |
| wc7coveredemployee | WC7CoveredEmployee | No | A Workers' Comp Covered Employee |
| wc7coveredemployeebase | WC7CoveredEmployeeBase | No | A Workers' Comp Covered Employee |
| wc7covprogramtype | WC7CovProgramType | No | WC Coverage program type |
| wc7excludedlaborcontactdetail | WC7ExcludedLaborContactDetail | No | The details about the labor contact (e.g. labor client or labor contractor) on an exclusion.   |
| wc7excludedownerofficer | WC7ExcludedOwnerOfficer | No | A person who has a meaningful equity/ownership interest in an insuredbusiness entity.   |
| wc7excludedworkplace | WC7ExcludedWorkplace | No | Defines an exclusion for workplaces. |
| wc7exposureratingeffdate | WC7ExposureRatingEffDate | No | The exposure's rating effective date |
| wc7exposureratingexpdate | WC7ExposureRatingExpDate | No | The exposure's rating expiration date |
| wc7fedcoveredemployee | WC7FedCoveredEmployee | No | A Workers' Comp Federal Covered Employee |
| wc7fedempliabact | WC7FedEmpLiabAct | No | Federal Employers Liability coverage Act type |
| wc7formassociation | WC7FormAssociation | No | Associates a Workers' Comp waiver of subrogation entity with its related form. |
| wc7governinglaw | WC7GoverningLaw | No | What kind of special coverage does this group of employees have? |
| wc7includedlaborcontactdetail | WC7IncludedLaborContactDetail | No | The details about the labor contact (e.g. labor client or labor contractor) on a condition.   |
| wc7includedownerofficer | WC7IncludedOwnerOfficer | No | A person who has a meaningful equity/ownership interest in an insuredbusiness entity.   |
| wc7jurisdiction | WC7Jurisdiction | No | Container for jurisdiction-level elements: coverages, modifiers, etc. |
| wc7jurisdictioncost | WC7JurisdictionCost | No | A unit of price for a period of time, not to be broken up any further, for a Workers' Comp jurisdiction |
| wc7jurisdictioncosttype | WC7JurisdictionCostType | No | The type of a WC Jurisdiction Cost. |
| wc7jurisdictioncov | WC7JurisdictionCov | No | A jurisdiction-level coverage for Workers Comp' |
| wc7jurisdictionmultiplier | WC7JurisdictionMultiplier | No | Jurisdiction Multipliers |
| wc7laborcontact | WC7LaborContact | No | A WC7PolicyContactRole for WC Labor containing WC7LaborContactDetails. |
| wc7laborcontactdetail | WC7LaborContactDetail | No | The details about the WC labor contact (e.g. labor client or labor contractor).    |
| wc7liabilityact | WC7LiabilityAct | No | Liability acts |
| wc7lineschedulecond | WC7LineScheduleCond | No | WC7 Line Condition with a schedule |
| wc7linescheduleconditem | WC7LineScheduleCondItem | No | WC7 Line level condition scheduled item |
| wc7lineschedulecov | WC7LineScheduleCov | No | WC7 Line Coverage with a schedule |
| wc7lineschedulecovitem | WC7LineScheduleCovItem | No | WC7 Line level coverage scheduled item |
| wc7linescheduleexcl | WC7LineScheduleExcl | No | WC7 Line Exclusion with a schedule |
| wc7linescheduleexclitem | WC7LineScheduleExclItem | No | WC7 Line level exclusion scheduled item |
| wc7manuscriptoption | WC7ManuscriptOption | No | Workers' Comp Manuscript Data |
| wc7maritimecoveredemployee | WC7MaritimeCoveredEmployee | No | A Workers' Comp Maritime Covered Employee |
| wc7modifier | WC7Modifier | No | A line-level modifier for Workers' Comp |
| wc7participatingplan | WC7ParticipatingPlan | No | A Workers' Comp participating plan |
| wc7participatingplanid | WC7ParticipatingPlanID | No | The type of WC participating plan. |
| wc7personorg | WC7PersonOrg | No | Person or Organization? |
| wc7policycontactrole | WC7PolicyContactRole | No | A PolicyContactRole specific to a WorkersComp policy line. |
| wc7policylaborclient | WC7PolicyLaborClient | No | The third party labor contractor or professional employee organization(PEO) that staffs an insured entity with long-term workers.   |
| wc7policylaborcontractor | WC7PolicyLaborContractor | No | The insured entity that provides employees on a long term basis to workat/for a third party business entity.   |
| wc7policyownerofficer | WC7PolicyOwnerOfficer | No | A person who has a meaningful equity/ownership interest in an insuredbusiness entity.   |
| wc7ratefactor | WC7RateFactor | No | A rate factor is a risk characteristic and its associated numeric value which might have an impact on premium. As used here rate factors are applied to base premium rather than rates. A common example of Rate Factors are the components of IRPM (individual risk premium modifier). |
| wc7ratingperiodstartdate | WC7RatingPeriodStartDate | No | A date which marks the beginning of a new rating period. During a rating period the basis amounts for basis-scalable exposures are typically constant. |
| wc7ratingstepext | WC7RatingStepExt | No | A sample table storing additional steps for rating Workers Comp policies after the basic calculation of  manual premiums (premiums for each location/class code exposure unit).   |
| wc7retroratingletterofcredit | WC7RetroRatingLetterOfCredit | No | A Letter Of Credit |
| wc7retrospectiveratingplan | WC7RetrospectiveRatingPlan | No | A plan for retrospectively rating a policy line |
| wc7transaction | WC7Transaction | No | A transaction for the Workers' Comp line |
| wc7voluntarycomp | WC7VoluntaryComp | No | Voluntary compensation type |
| wc7waiverofsubro | WC7WaiverOfSubro | No | A Workers' Comp Waiver of Subrogation |
| wc7waiverofsubrogation | WC7WaiverOfSubrogation | No | The type of waiver of subro. |
| wc7waiverminimumadjustment | WC7WaiverMinimumAdjustment | No | The amount to adjust this waiver by |
| wc7workerkind | WC7WorkerKind | No | What kind of worker? |
| wc7workerscompcond | WC7WorkersCompCond | No | A line-level condition for Workers' Comp |
| wc7workerscompcov | WC7WorkersCompCov | No | A line-level coverage for Workers' Comp |
| wc7workerscompexcl | WC7WorkersCompExcl | No | A line-level exclusion for Workers' Comp |
| wc7workerscompline | WC7WorkersCompLine | No | Workers' Comp line of business. |
| classcodebasis | ClassCodeBasis | No | Class Code Basis |
| wc7diseasecode | WC7DiseaseCode | No | Supplementary Disease Code |
| wc7suppldiseaseexposure | WC7SupplDiseaseExposure | No | Supplementary Disease Basis |
| wc7totalpayrollamount | WC7TotalPayrollAmount | No | Total payroll amount |
| wc7totalpremiumamount | WC7TotalPremium | No | Total premium amount |
| wc7modifierfactor | WC7ModifierFactor | No | Modifier Factor |
| wc7totalmanualpremium | WC7TotalManualPremium | No | Total Manual Premium |
| wc7eachaccidentlimit | WC7EachAccidentLimit | No | Each Accident Limit |
| wc7diseasepolicylimit | WC7DiseasePolicyLimit | No | Disease Policy Limit |
| wc7deductibleclasscode | WC7DeductibleClassCode | No | Deductible classcode with highest total manual premium |
| wc7classfactor | WC7ClassFactor | No | A class factor for Workers' Comp |
| wc7subjectpremium | WC7SubjectPremium | No | Subject premium |
| wc7minimumpremiumparam | WC7MinimumPremiumParam | No | Minimum Premium Parameter (writable) |
| wc7expenseconstant | WC7ExpenseConstant | No | Expense Constant |
| wc7stopgapflatcharge | WC7StopGapFlatCharge | No | Stop Gap Flat Charge |
| wc7proratedminimumpremium | WC7ProratedMinimumPremium | No | Minimum Premium that is prorated across all rating periods |
| wc7totalmodifiedpremium | WC7TotalModifiedPremium | No | Total Modified premium |
| wc7benefitsdeductiblecov | WC7BenefitsDeductibleCov | No | Benefits Deductible Coverage |
| wc7totalstandardpremium | WC7TotalStandardPremium | No | Total Standard Premium for jurisdiction |
| wc7totalpremiumdiscountamount | WC7TotalPremiumDiscountAmount | No | Total Premium discount calculated for rating period |
| wc7premiumdiscountamount | WC7PremiumDiscountAmount | No | Premium Discount (writable param)calculated for each discount level |
| wc7standardpremiumforlevel | WC7StandardPremiumForLevel | No | Portion of Standard Premium for a discount level |
| wc7premiumdiscountlevelamount | WC7PremiumDiscountLevelAmount | No | Premium Discount Level Amount |
| proratedpremiumtotal | ProratedPremiumTotal | No | The total prorated premium amount |
| wc7statcodeparam | WC7StatCodeParam | No | Stat Code (writable) |
| wc7classcoderate | WC7ClassCodeRate | No | Class Code Rate |
| wc7specificwaiverminimum | WC7SpecificWaiverMinimum | No | Specific Waiver Minimum |
| wc7atomicenergyexposure | WC7AtomicEnergyExposure | No | Atomic Energy Exposure |
| wc7ratingeffdate | WC7RatingEffDate | No | The rating effective date |
| wc7ratingexpdate | WC7RatingExpDate | No | The rating expiration date |
| hopbasepremiuminfo | HOPBasePremiumInfo | No | HOP Base Premium Information |
| hopdwelling | HOPDwelling | No | HOP Dwelling |
| hopcoveragepart | HOPCoveragePart | No | HOP Coverage Part |
| hopmodifierbasis | HOP Modifier Basis | No | HOP Basis to be used for Rating Modification |
| hopmodifier | HOP Modifier Code | No | HOP Modifier Code to be used in Modifier Rate lookup |
| hopmodifiervalue | HOP Modifier Value | No | HOP Modifier Value to be used in Modifier Rate lookup |

---

### Typelist: CalcStepCategory

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\CalcStepCategory.tti`
**Description:** The categories of steps used in Calculation routines
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| assignment | Assignment Operators | No | Assignment-related steps |
| continue | Continue | No | Continue steps |
| flowcontrol | Flow Control | No | Flow control steps |
| nooperand | No Operand | No | Steps with no operands |
| voidfunction | Void function steps | No | Steps with void functions |

---

### Typelist: CalcStepOperandCategory

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\CalcStepOperandCategory.tti`
**Description:** The categories of operand used in Calculation routines
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| simple | Simple Operands | No | Allowed to be passed as arguments for functions and table lookups |

---

### Typelist: CalcStepOperandType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\CalcStepOperandType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\CalcStepOperandType.ttx`
**Description:** The operands used in Calculation routines
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| localvar | Local Variable | No | Local Variable |
| ratetable | Rate Table | No | Rate Table Lookup |
| ratefunc | Rate Function | No | Excecute Rate Function |
| constant | Constant | No | Constant Assignment |
| conditional | Conditional | No | Conditional Expression |
| comparison | Comparison | No | Comparison Expression |
| inscope | In-Scope | No | In Scope Values |
| rounding | Rounding | No | Rounding |
| Collection | Set of typekey values | No | Collection of constant (typekey) values |
| loopvar | Loop Iteration Variable | No | Loop Iteration Variable |

---

### Typelist: CalcStepOperatorCategory

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\CalcStepOperatorCategory.tti`
**Description:** The categories of operator used in Calculation routines
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| mathematical | Math Operators | No | Mathematical operators |
| assignment | Assignment Operators | No | Assignment-related operators |
| logical | Logical Operators | No | Logical operators |
| comparator | Comparison Operators | No | Comparison operators |
| grouping | Parentheses | No | Parentheses |
| rightassociative | Right-associative Operators | No | Right-associative operators |
| rounding | Rounding Operators | No | Rounding operators |
| optrounding | Additional rounding Operators | No | Additional rounding operators |
| inclusion | Inclusion and Exclusion operators | No | Operators that test inclusion in a collection |

---

### Typelist: CalcStepOperatorType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\CalcStepOperatorType.tti`
**Description:** The operators used in Calculation routines
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| addition | + | No | Addition |
| subtraction | - | No | Subtraction |
| multiplication | * | No | Multiplication |
| division | / | No | Division |
| store | <-- | No | Store |
| and | AND | No | And |
| or | OR | No | Or |
| not | NOT | No | Not |
| lessthan | < | No | Less Than |
| lessthanorequal | <= | No | Less Than Or Equal |
| greaterthan | > | No | Greater Than |
| greaterthanorequal | >= | No | Greater Than Or Equal |
| equal | = | No | Equals |
| notequal | <> | No | Not Equal |
| halfup | R | No | Half Up |
| down | RD | No | Down |
| up | RU | No | Up |
| halfeven | RE | No | Half Even |
| halfdown | HD | No | Half Down |
| ceiling | RC | No | Ceiling |
| floor | RF | No | Floor |
| unnecessary | NR | No | No Rounding Necessary |
| in | IN | No | is-one-of operator |
| notin | NOT IN | No | not-one-of operator |

---

### Typelist: CalcStepType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\CalcStepType.tti`
**Description:** The type of each step used in Calculation routines
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| continue | Continue Step | No | Steps which do not have an explicit instruction |
| assignment | Assignment Step | No | Assignment-related step |
| if | IF | No | If |
| elseif | ELSEIF | No | Elseif |
| else | ELSE | No | Else |
| endif | ENDIF | No | Endif |
| comment | -- Section Comment | No | Section Comment |
| voidfunction | Void function step | No | Step related to a function with no return value |
| loop | LOOP | No | Start of loop over Iterable or array |
| endloop | ENDLOOP | No | End of loop over and Iterable or array |

---

### Typelist: CalculationMethod

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\CalculationMethod.tti`
**Description:** Calculation methods for calculating refunds etc...
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| flat | Flat | No | Flat |
| prorata | Pro rata | No | Pro rata |
| shortrate | Short rate | No | Short rate |

---

### Typelist: CancellationSource

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\CancellationSource.tti`
**Description:** Party that initiated the cancellation
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| carrier | Insurer | No | Cancellation initiated by carrier |
| insured | Insured | No | Cancellation initiated by insured |

---

### Typelist: CauseOfLoss

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\CauseOfLoss.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\CauseOfLoss.ttx`
**Description:** Cause of Loss for a Coverage
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| standard | Standard | No | Standard |
| Perils | Named Perils | No | Named Perils |
| Special | Special | No | Special |
| Specified | Specified Causes | Yes | Specified Causes |
| Fire | Fire | Yes | fire |
| FireTheft | Fire and theft | Yes | Fire and theft |
| FireTheftstorm | Fire, theft, and windstorm | Yes | Fire, theft and, windstorm |
| Limited | Limited specified causes of loss | Yes | Limited specified causes of loss |
| basic | Basic | No | Basic |
| broad | Broad | No | Broad |
| ComprehensivePerils | Comprehensive Perils | No | Comprehensive Perils |
| SpecialPerils | Special Perils | No | SpecialPerils |

---

### Typelist: CharacterSet

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\CharacterSet.tti`
**Description:** Character sets available for print/export
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| *(None defined)* | *Dynamic or database-driven* | No | Typelist populated dynamically at runtime or via database table |

---

### Typelist: ChargePattern

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ChargePattern.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\ChargePattern.ttx`
**Description:** The type of charge will be stored in billing system
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Premium | Premium | No | Premium |
| Taxes | Taxes | No | Taxes |
| InstallmentFee | Installment Fee | No | Installment Fee |
| ReinstatementFee | Reinstatement Fee | No | Reinstatement Fee |
| PremiumIncludingTaxes | Premium including taxes | No | Premium including taxes (typically used in EMEA where charges have taxes automatically included) |

---

### Typelist: ClassCodeType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ClassCodeType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\ClassCodeType.ttx`
**Description:** A type of class code (NCCI, GL, etc)
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| BOP | BOP | No | A BOP code |
| GL | GL | No | A GL code |
| CA | CA | No | A commercial auto code |
| CP | CP | No | A Property code |
| CR | CR | No | A Crime code |
| NCCI | NCCI | No | A NCCI code |
| CA_WC | CA_WC | No | A California WC code |
| DE_WC | DE_WC | No | A DE WC code |
| PA_WC | PA_WC | No | A PA WC code |
| MI_WC | MI_WC | No | A MI WC code |
| NJ_WC | NJ_WC | No | A NJ WC code |
| NY_WC | NY_WC | No | A NY WC code |
| TX_WC | TX_WC | No | A TX WC code |
| MA_WC | MA_WC | No | A MA WC code |
| MN_WC | MN_WC | No | A MN WC code |
| NC_WC | NC_WC | No | A NC WC code |
| WI_WC | WI_WC | No | A WI WC code |

---

### Typelist: Coinsurance

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\Coinsurance.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\Coinsurance.ttx`
**Description:** Coinsurance percentage values
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 80 | 80% | No | 80% |
| 90 | 90% | No | 90% |
| 100 | 100% | No | 100% |

---

### Typelist: CombinedDriverExp

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\CombinedDriverExp.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\CombinedDriverExp.ttx`
**Description:** Driver experiences on the vehicle
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| AllDriversExpMore5 | All drivers experience greater than 5 years | No | All drivers experience greater than 5 years |
| AllOther | Other | No | Other |
| MainDriverExpMore5 | Main driver experience greater than 5 years | No | Main driver experience greater than 5 years |
| MainDriverExpLess5 | Main driver experience less than 5 years | No | Main driver experience less than 5 years |

---

### Typelist: ComponentType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ComponentType.tti`
**Description:** Identifiers for the components in the system
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| db | Database | No | Database |
| fs | Filesystem | No | Filesystem |
| session | SessionManager | No | Session Manager |
| tm | TransactionManager | No | Transaction Manager |
| assigneng | AssignmentEngine | No | Assignment Engine |
| clock | DBClock | No | Database Clock |
| escalation | EscalationManager | No | Escalation Manager |
| ruleeng | RuleEngine | No | Rule Engine |
| segmenteng | SegmentationEngine | No | Segmentation Engine |
| statemach | StateMachine | No | State Machine |
| workplan | WorkplanGenerator | No | Workplan Generator |
| statistics | StatisticsCalculator | No | Calculates statistics on a scheduled basis |
| cache | Cache | No | Server cache |
| businesscalendar | BusinessCalendar | No | Business calendar for use in statistics calculations |
| eventcenter | EventCenter | No | Handles sending of remote events |
| auth | AuthenticationManager | No | Manages users and passwords in the product database |
| scheduler | Scheduler | No | Schedules tasks to be executed in the future |
| lifecyclemgr | EntityLifecycleManager | No | Manages entity lifecycle rulesets |
| searcheng | SearchEngine | No | Search Engine |
| approval | ApprovalEngine | No | Approval Engine |
| validation | ValidationManager | No | Validation Manager |
| deduction | DeductionEngine | No | Deduction Engine |
| notification | NotificationEngine | No | Notification Engine |
| qplexor | QPlexor | No | Manages sync messages and acknowledgements |
| eventdispatcher | EventDispatcher | No | Receives sync events and generates messages |
| velocity | VelocitySupport | No | Velocity template support |
| configuration | Configuration | No | Configuration component |
| clusterchannel | ClusterChannel | No | Cluster communication channel |
| jmxagent | JMXAgent | No | Manages an MBeanServer and JMX adaptors |

---

### Typelist: ConsistencyCheckType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ConsistencyCheckType.tti`
**Description:** Type of consistency check
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 0lengthstringcheck | 0 length string check | No | Verifies no 0 length strings within varchar column |
| adtvaluescheck | ADT values check | No | Verifies values are valid for abstract data types |
| appspecificcheck | Application-specific check | No | Verifies application-specific relationships in the database |
| arrayrequiredmatch | Array required match | No | Verifies that every row in the container has a nonempty array |
| assignmentcheck | Assignment check | No | Verifies that the database is consistent relative to assignment |
| beanversioncheck | Bean version check | No | Verifies that the database is consistent relative to bean versions |
| caseinsensitivecheck | Linguistic search denorm check | No | Verifies that the linguistic search denorm columns are in sync with the associated source columns |
| searchdenormcheck | Search denorm check | No | Verifies that the search denorm columns are in sync with the associated source columns |
| checkconstraintcheck | Check constraint check | No | Verifies data is valid relative to check constraints |
| consistentchildren | Consistent children | No | Verifies that the consistent children property holds |
| customcheck | Custom check | No | Custom consistency check declared in a data model file |
| datetimeorderingcheck | Datetime ordering check | No | Verifies data is valid relative to datetime orderings |
| effdatedregistrycheck | Effdated registry check | No | Verifies that an effdated table appears in the effdated registry of all referenced branches |
| fkcheck | Foreign key check | No | Verifies foreign key references when RI is not enforced in the database |
| fksubtypecheck | Foreign key subtype check | No | Verifies foreign key reference to a subtype is to correct subtype |
| jointablecheck | Join table check | No | Verifies data is valid relative to jointable declarations |
| localizedcolumncheck | Localized column check | No | Verifies required localized columns have values for all languages |
| maxkeycheck | Max key check | No | Verifies data in max key table is in synch with table |
| revisioningcheck | Revisioning check | No | Verifies that the database is consistent relative to revisioning |
| subtypecolumncheck | Subtype column check | No | Verifies subtype column contains valid values |
| subtypenonnullcheck | Subtype non-null check | No | Verifies non-nullable subtype-specific columns have non-null values for subtype rows |
| subtypespecificcheck | Subtype-specific column check | No | Verifies subtype-specific columns are null when row is a different subtype |
| typekeycheck | Typekey check | No | Verifies typekey column contains valid values |
| typelisttablecheck | Typelist table check | No | Verifies values in typelist table and data model are in sync |
| upgradewarningcheck | Upgrade warning check | No | Verifies that data will pass associated version check at the beginning of the upgrade to a subsequent version of the product |
| onetoonecheck | One-to-one check | No | Verifies that one-to-one relationships have at most one referring entity |
| onetoonenonnullcheck | One-to-one non-null check | No | Verifies that non-nullable one-to-one relationships have at least one referring entity |
| edgefknonnullcheck | Edge foreign key non-null check | No | Verifies that non-nullable edge foreign key relationships have one referring entity |

---

### Typelist: ConstructionType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ConstructionType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\ConstructionType.ttx`
**Description:** Types of building construction
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| F | Frame | No | Frame |
| JMR | Joisted Masonry (reinforced) | No | Joisted Masonry (reinforced) |
| JMNR | Joisted Masonry (not reinforced) | No | Joisted Masonry (not reinforced) |
| NCLS | Non-Combustible (light steel) | No | Non-Combustible (light steel) |
| NCNLS | Non-Combustible (not light steel) | No | Non-Combustible (not light steel) |
| MNCR | Masonry Non-Combustible (reinforced) | No | Masonry Non-Combustible (reinforced) |
| MNCNR | Masonry Non-Combustible (not reinforced) | No | Masonry Non-Combustible (not reinforced) |
| FRLSNR | Fire Resistive (light steel/not reinforced) | No | Fire Resistive (light steel/not reinforced) |
| FRLSR | Fire Resistive (light steel/reinforced) | No | Fire Resistive (light steel/reinforced) |
| FRNLSNR | Fire Resistive (not light steel/not reinforced) | No | Fire Resistive (not light steel/not reinforced) |
| FRNLSR | Fire Resistive (not light steel/reinforced) | No | Fire Resistive (not light steel/reinforced) |
| MFR | Modified Fire Resistive | No | Modified Fire Resistive |

---

### Typelist: ContactBidiRel

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ContactBidiRel.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\ContactBidiRel.ttx`
**Description:** Bi-directional representations of contact relationships. This list is used in the presentation of a contact's relationships. Entries in this list come in pairs. One half of the pair corresponds to an entry in the ContactRel typelist. The other half represents the inverse of the first half of the relationship. Pairs are defined in the ab/contact-relationship-config.xml files.
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| guardian | Parent / Guardian | No | Parent of a child or Guardian of a ward. |
| ward | Child / Ward | No | Child or ward |
| employer | Employer | No | Employer |
| employee | Employee | No | Employee of an employer |
| primarycontact | Primary Contact | No | Primary contact |
| primarycontactfor | Primary Contact For | No | PrimaryContact For |
| thirdpartyinsurer | Third-Party Insurer | No | Third-Party Insurer |
| thirdpartyinsured | Third-Party Insured | No | Third-Party Insured |
| collectionagency | Collection Agency | No | Collection Agency |
| case | Assigned Case | No | Assigned Case |

---

### Typelist: ContactChangeResolution

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ContactChangeResolution.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\ContactChangeResolution.ttx`
**Description:** Resolution status of a PendingContactChange
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| approved | Approved | No | Approved |
| rejected | Rejected | No | Rejected |
| more_info_req | More Information Required | No | More Information Required |
| already_applied | Already Applied | No | Already Applied |

---

### Typelist: ContactClass

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ContactClass.tti`
**Description:** The classification of a contact
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| general | Basic | No | Basic contact with no specific classification |
| user | User | No | User |
| vendor | Vendor | No | Vendor |
| venue | Legal Venue | No | Authority that handles legal matters (for example, a court house) |

---

### Typelist: ContactCreationApprovalStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ContactCreationApprovalStatus.tti`
**Description:** Approval status of contact for creation
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| pending_approval | Pending Approval | No | Pending Approval |
| approved | Approved | No | Approved |
| rejected | Rejected | No | Rejected |

---

### Typelist: ContactDestructionStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ContactDestructionStatus.tti`
**Description:** Status in the Contact Purge Process
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| New | New | No | New Request |
| ReRun | ReRun | No | The contact destruction request needs to be rerun |
| ManualInterventionRequired | Manual Intervention Required | No | Requires manual intervention from a person. |
| Partial | Partial | No | The contact was partially purged |
| NotDestroyed | Not Destroyed | No | Contact was looked at and was determined that it should not be destroyed. |
| Completed | Completed | No | Request has been processed and the contact should have been destroyed. |

---

### Typelist: ContactDestructionStatusCategory

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ContactDestructionStatusCategory.tti`
**Description:** The categories if the Contact DestructionStatus is in a final state to nofity external systems
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| DestructionStatusFinished | Destruction Status Finished | No | The contact destruction request has been finished |
| DestructionStatusNotProcessed | Destruction Status Not Processed | No | The contact destruction request has not been processed |
| ReadyToBeNotified | Ready To Be Notified | No | The Contact Destruction Request is ready to be notified |
| ReadyToAttemptDestruction | Ready To Attempt Destruction | No | This contact purge request is ready to be sent to the destroyer |

---

### Typelist: ContactLinkStatusType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ContactLinkStatusType.tti`
**Description:** Represents the link status of a Contact with its associated Address Book Contact.
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| NOT_FOUND | Not found | No | No associated Address Book Contact found. |
| OUT_OF_SYNC | Out of sync | No | The Contact is out of sync with the associated Address Book Contact. |
| IN_SYNC | In sync | No | The Contact is in sync with the associated Address Book Contact. |

---

### Typelist: ContactMatchResultType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ContactMatchResultType.tti`
**Description:** Represents the result of definitive match search.
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| CLOSE_MATCH | Close match | No | At least one contact in the Address Book closely matched a given contact. |
| POSSIBLE_MATCH | Plausible match | No | One or more contacts in the Address Book possibly matched a given contact. |
| PLAUSIBLE_MATCH | Plausible match | No | A definitive match was found that matches a contact in the Address Book in terms of potential match fields. |
| IMPLAUSIBLE_MATCH | Implausible match | No | A definitive match was found, but the contact does not match in terms of potential match fields. |
| INCOMPATIBLE_TYPE | Incompatible type match | No | A definitive match was found, but its type is incompatible with the type of the candidate contact. That is, the matched contact could not be cast to the type of the candidate contact. |
| NO_MATCH | No match | No | No match was found. |

---

### Typelist: ContactRel

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ContactRel.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\ContactRel.ttx`
**Description:** Types of relationships a contact can have with another contact
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| guardian | Parent / Guardian | No | Parent of a child or Guardian of a ward. |
| employer | Employer | No | Employer |
| primarycontact | Primary Contact | No | Primary contact |
| thirdpartyinsurer | Third-Party Insurer | No | Third-Party Insurer |
| collectionagency | Collection Agency | No | Collection Agency |

---

### Typelist: ContactRelCons

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ContactRelCons.tti`
**Description:** This typelist is obsolete and should not be used
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| exclusive | Exclusive | No | Exclusive |

---

### Typelist: ContactSearchResultType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ContactSearchResultType.tti`
**Description:** Represents the result of definitive match search.
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| SUCCESS | Success | No | Address book search succeeded |
| TOO_LOOSE_SEARCH | Too Loose Search Criteria | No | Search criteria is too loose and executing may require too much of the DB resources. Search not executed. |

---

### Typelist: ContactSearchType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ContactSearchType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\ContactSearchType.ttx`
**Description:** The type of contact search
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| internal | Address Book | No | Address Book |

---

### Typelist: ContactTagType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ContactTagType.tti`
**Description:** Types of contact tags
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| client | Client | No | Client |
| claimparty | Claim Party | No | Claim Party |
| vendor | Vendor | No | Vendor |

---

### Typelist: ContactType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ContactType.tti`
**Description:** The type of contact
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| company | Company | No | Company |
| person | Person | No | Person |

---

### Typelist: ContingencyAction

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ContingencyAction.tti`
**Description:** ContingencyAction
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| ChangeRetroactively | Change policy retroactively | No | Change policy retroactively |
| ChangeRemainderOfTerm | Change policy for remainder of term | No | Change policy for remainder of term |
| CancelRetroactively | Cancel retroactively | No | Cancel retroactively |
| CancelRemainderOfTerm | Cancel remainder of term | No | Cancel remainder of term |
| CancelRewrite | Cancel / Rewrite | No | Cancel / Rewrite |

---

### Typelist: ContingencyStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ContingencyStatus.tti`
**Description:** ContingencyStatus
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Pending | Pending | No | This contingency is pending completion |
| Resolved | Resolved | No | This contingency has been resolved |
| Waived | Waived | No | This contingency has been waived |
| Failed | Failed | No | The conditions of this contigency not met by the due date |
| Action_Initiated | Action Initiated | No | The action associated with the contingency has been initiated by the HandleUnresolvedContingencyWorkQueue |

---

### Typelist: ContractEffectivePeriod

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ContractEffectivePeriod.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\ContractEffectivePeriod.ttx`
**Description:** Use for searching reinsurance agreements and programs.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| ComingYear | Coming Year | No | For The Next 12 Months |
| LastYear | Last Year | No | For The Last 12 Months |
| Custom | Custom Dates | No | Specific Effective and Expiration Dates |

---

### Typelist: ContractorType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ContractorType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\ContractorType.ttx`
**Description:** Contractor Type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| SmallContractor | Small Contractor | No | Small Contractor |
| BuildingContractor | Building Contractor | No | Building Contractor |
| HeavyConstruction | Heavy Construction | No | Heavy Construction |
| RoadBuilding | Road / Building | No | Road / Building |

---

### Typelist: ContractStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ContractStatus.tti`
**Description:** Status of a reinsurance agreement or program.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Draft | Draft | No | Not yet finalized and ready for use. |
| Active | Active | No | Finalized and currently usable. |

---

### Typelist: CoordinatePIP

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\CoordinatePIP.tti`
**Description:** CoordinatePIP
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| PIPOtherMed | PIPOtherMed | No | Medical |
| PIPOtherWork | PIPOtherWork | No | Work Loss |
| PIPOtherMedandWork | PIPOtherMedandWork | No | Medical & Work Loss |

---

### Typelist: Country

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\Country.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\Country.ttx`
**Description:** List of regions, or countries
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| unknown | Unknown | Yes | Placeholder typecode for fields that should be populated with another Country |
| AF | Afghanistan | No | Afghanistan |
| AL | Albania | No | Albania |
| DZ | Algeria | No | Algeria |
| AS | American Samoa | No | American Samoa |
| AD | Andorra | No | Andorra |
| AO | Angola | No | Angola |
| AI | Anguilla | No | Anguilla |
| AQ | Antarctica | No | Antarctica |
| AG | Antigua and Barbuda | No | Antigua and Barbuda |
| AR | Argentina | No | Argentina |
| AM | Armenia | No | Armenia |
| AW | Aruba | No | Aruba |
| AU | Australia | No | Australia |
| AT | Austria | No | Austria |
| AZ | Azerbaijan | No | Azerbaijan |
| BS | Bahamas | No | Bahamas |
| BH | Bahrain | No | Bahrain |
| BD | Bangladesh | No | Bangladesh |
| BB | Barbados | No | Barbados |
| BY | Belarus | No | Belarus |
| BE | Belgium | No | Belgium |
| BZ | Belize | No | Belize |
| BJ | Benin | No | Benin |
| BM | Bermuda | No | Bermuda |
| BT | Bhutan | No | Bhutan |
| BO | Bolivia | No | Bolivia |
| BA | Bosnia and Herzegovina | No | Bosnia and Herzegovina |
| BW | Botswana | No | Botswana |
| BV | Bouvet Island (Bouvetoya) | No | Bouvet Island (Bouvetoya) |
| BR | Brazil | No | Brazil |
| IO | British Indian Ocean Territory (Chagos Archipelago) | No | British Indian Ocean Territory (Chagos Archipelago) |
| VG | British Virgin Islands | No | British Virgin Islands |
| BN | Brunei | No | Brunei |
| BG | Bulgaria | No | Bulgaria |
| BF | Burkina Faso | No | Burkina Faso |
| BI | Burundi | No | Burundi |
| KH | Cambodia | No | Cambodia |
| CM | Cameroon | No | Cameroon |
| CA | Canada | No | Canada |
| CV | Cape Verde | No | Cape Verde |
| KY | Cayman Islands | No | Cayman Islands |
| CF | Central African Republic | No | Central African Republic |
| TD | Chad | No | Chad |
| CL | Chile | No | Chile |
| CN | China | No | China |
| CX | Christmas Island | No | Christmas Island |
| CC | Cocos (Keeling) Islands | No | Cocos (Keeling) Islands |
| CO | Colombia | No | Colombia |
| KM | Comoros | No | Comoros |
| CG | Congo - Brazzaville | No | Congo - Brazzaville |
| CD | Congo - Kinshasa | No | Congo - Kinshasa |
| CK | Cook Islands | No | Cook Islands |
| CR | Costa Rica | No | Costa Rica |
| HR | Croatia | No | Croatia |
| CU | Cuba | No | Cuba |
| CY | Cyprus | No | Cyprus |
| CZ | Czech Republic | No | Czech Republic |
| CI | Ivory Coast | No | Ivory Coast |
| DK | Denmark | No | Denmark |
| DJ | Djibouti | No | Djibouti |
| DM | Dominica | No | Dominica |
| DO | Dominican Republic | No | Dominican Republic |
| EC | Ecuador | No | Ecuador |
| EG | Egypt | No | Egypt |
| SV | El Salvador | No | El Salvador |
| GQ | Equatorial Guinea | No | Equatorial Guinea |
| ER | Eritrea | No | Eritrea |
| EE | Estonia | No | Estonia |
| ET | Ethiopia | No | Ethiopia |
| FO | Faroe Islands | No | Faroe Islands |
| FK | Falkland Islands (Malvinas) | No | Falkland Islands (Malvinas) |
| FJ | Fiji, Republic of the Fiji Islands | No | Fiji, Republic of the Fiji Islands |
| FI | Finland | No | Finland |
| FR | France | No | France |
| GF | French Guiana | No | French Guiana |
| PF | French Polynesia | No | French Polynesia |
| TF | French Southern Territories | No | French Southern Territories |
| GA | Gabon | No | Gabon |
| GM | Gambia | No | Gambia |
| GE | Georgia | No | Georgia |
| DE | Germany | No | Germany |
| GH | Ghana | No | Ghana |
| GI | Gibraltar | No | Gibraltar |
| GR | Greece | No | Greece |
| GL | Greenland | No | Greenland |
| GD | Grenada | No | Grenada |
| GP | Guadeloupe | No | Guadeloupe |
| GU | Guam | No | Guam |
| GT | Guatemala | No | Guatemala |
| GN | Guinea | No | Guinea |
| GW | Guinea-Bissau | No | Guinea-Bissau |
| GY | Guyana | No | Guyana |
| HT | Haiti | No | Haiti |
| HM | Heard and McDonald Islands | No | Heard and McDonald Islands |
| HN | Honduras | No | Honduras |
| HK | Hong Kong SAR China | No | Hong Kong SAR China |
| HU | Hungary | No | Hungary |
| IS | Iceland | No | Iceland |
| IN | India | No | India |
| ID | Indonesia | No | Indonesia |
| IR | Iran | No | Iran |
| IQ | Iraq | No | Iraq |
| IE | Ireland | No | Ireland |
| IL | Israel | No | Israel |
| IT | Italy | No | Italy |
| JM | Jamaica | No | Jamaica |
| JP | Japan | No | Japan |
| JO | Jordan | No | Jordan |
| KZ | Kazakhstan | No | Kazakhstan |
| KE | Kenya | No | Kenya |
| KI | Kiribati | No | Kiribati |
| KP | Korea, North | No | Korea, North |
| KR | Korea, South | No | Korea, South |
| KW | Kuwait | No | Kuwait |
| KG | Kyrgyz Republic | No | Kyrgyz Republic |
| LA | Laos | No | Laos |
| LV | Latvia | No | Latvia |
| LB | Lebanon | No | Lebanon |
| LS | Lesotho | No | Lesotho |
| LR | Liberia | No | Liberia |
| LY | Libya | No | Libya |
| LI | Liechtenstein | No | Liechtenstein |
| LT | Lithuania | No | Lithuania |
| LU | Luxembourg | No | Luxembourg |
| MO | Macau SAR China | No | Macau SAR China |
| MK | Macedonia | No | Macedonia |
| MG | Madagascar | No | Madagascar |
| MW | Malawi | No | Malawi |
| MY | Malaysia | No | Malaysia |
| MV | Maldives | No | Maldives |
| ML | Mali | No | Mali |
| MT | Malta | No | Malta |
| MH | Marshall Islands | No | Marshall Islands |
| MQ | Martinique | No | Martinique |
| MR | Mauritania | No | Mauritania |
| MU | Mauritius | No | Mauritius |
| YT | Mayotte | No | Mayotte |
| MX | Mexico | No | Mexico |
| FM | Micronesia, Federated States of | No | Micronesia, Federated States of |
| MD | Moldova | No | Moldova |
| MC | Monaco | No | Monaco |
| MN | Mongolia | No | Mongolia |
| ME | Montenegro | No | Montenegro |
| MS | Montserrat | No | Montserrat |
| MA | Morocco | No | Morocco |
| MZ | Mozambique | No | Mozambique |
| MM | Myanmar [Burma] | No | Myanmar [Burma] |
| NA | Namibia | No | Namibia |
| NR | Nauru | No | Nauru |
| NP | Nepal | No | Nepal |
| NL | Netherlands | No | Netherlands |
| AN | Netherlands Antilles | No | Netherlands Antilles |
| NC | New Caledonia | No | New Caledonia |
| NZ | New Zealand | No | New Zealand |
| NI | Nicaragua | No | Nicaragua |
| NE | Niger | No | Niger |
| NG | Nigeria | No | Nigeria |
| NU | Niue | No | Niue |
| NF | Norfolk Island | No | Norfolk Island |
| MP | Northern Mariana Islands | No | Northern Mariana Islands |
| NO | Norway | No | Norway |
| OM | Oman | No | Oman |
| PK | Pakistan | No | Pakistan |
| PW | Palau | No | Palau |
| PS | Palestinian Interim Self-Government Authority | No | Palestinian Interim Self-Government Authority |
| PA | Panama | No | Panama |
| PG | Papua New Guinea | No | Papua New Guinea |
| PY | Paraguay | No | Paraguay |
| PE | Peru | No | Peru |
| PH | Philippines | No | Philippines |
| PN | Pitcairn Island | No | Pitcairn Island |
| PL | Poland | No | Poland |
| PT | Portugal | No | Portugal |
| PR | Puerto Rico | No | Puerto Rico |
| QA | Qatar | No | Qatar |
| RO | Romania | No | Romania |
| RU | Russia | No | Russia |
| RW | Rwanda | No | Rwanda |
| RE | Reunion | No | Reunion |
| SH | St. Helena | No | St. Helena |
| KN | St. Kitts and Nevis | No | St. Kitts and Nevis |
| LC | St. Lucia | No | St. Lucia |
| PM | St. Pierre and Miquelon | No | St. Pierre and Miquelon |
| VC | St. Vincent and the Grenadines | No | St. Vincent and the Grenadines |
| WS | Samoa | No | Samoa |
| SM | San Marino | No | San Marino |
| BL | Saint Barthelemy | No | Saint Barthelemy |
| MF | Saint Martin | No | Saint Martin |
| SA | Saudi Arabia | No | Saudi Arabia |
| SN | Senegal | No | Senegal |
| RS | Serbia | No | Serbia |
| SC | Seychelles | No | Seychelles |
| SL | Sierra Leone | No | Sierra Leone |
| SG | Singapore | No | Singapore |
| SK | Slovakia | No | Slovakia |
| SI | Slovenia | No | Slovenia |
| SB | Solomon Islands | No | Solomon Islands |
| SO | Somalia | No | Somalia |
| ZA | South Africa | No | South Africa |
| GS | South Georgia and the South Sandwich Islands | No | South Georgia and the South Sandwich Islands |
| ES | Spain | No | Spain |
| LK | Sri Lanka | No | Sri Lanka |
| SD | Sudan | No | Sudan |
| SR | Suriname | No | Suriname |
| SJ | Svalbard and Jan Mayen Islands | No | Svalbard and Jan Mayen Islands |
| SZ | Swaziland | No | Swaziland |
| SE | Sweden | No | Sweden |
| CH | Switzerland | No | Switzerland |
| SY | Syria | No | Syria |
| ST | Sao Tome and Principe | No | Sao Tome and Principe |
| TW | Taiwan | No | Taiwan |
| TJ | Tajikistan | No | Tajikistan |
| TZ | Tanzania | No | Tanzania |
| TH | Thailand | No | Thailand |
| TL | Timor-Leste | No | Timor-Leste |
| TG | Togo | No | Togo |
| TK | Tokelau (Tokelau Islands) | No | Tokelau (Tokelau Islands) |
| TO | Tonga | No | Tonga |
| TT | Trinidad and Tobago | No | Trinidad and Tobago |
| TN | Tunisia | No | Tunisia |
| TR | Turkey | No | Turkey |
| TM | Turkmenistan | No | Turkmenistan |
| TC | Turks and Caicos Islands | No | Turks and Caicos Islands |
| TV | Tuvalu | No | Tuvalu |
| UM | U.S. Minor Outlying Islands | No | U.S. Minor Outlying Islands |
| VI | U.S. Virgin Islands | No | U.S. Virgin Islands |
| UG | Uganda | No | Uganda |
| UA | Ukraine | No | Ukraine |
| AE | United Arab Emirates | No | United Arab Emirates |
| GB | United Kingdom | No | United Kingdom |
| US | United States | No | United States |
| UY | Uruguay | No | Uruguay |
| UZ | Uzbekistan | No | Uzbekistan |
| VU | Vanuatu | No | Vanuatu |
| VA | Vatican City | No | Vatican City |
| VE | Venezuela | No | Venezuela |
| VN | Vietnam | No | Vietnam |
| WF | Wallis and Futuna Islands | No | Wallis and Futuna Islands |
| EH | Western Sahara | No | Western Sahara |
| YE | Yemen | No | Yemen |
| ZM | Zambia | No | Zambia |
| ZW | Zimbabwe | No | Zimbabwe |

---

### Typelist: CoverageAvailabilityIssue

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\CoverageAvailabilityIssue.tti`
**Description:** Coverage availability issue can be error or warning
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| error | Error | No | Coverage availability issue is an error |
| warning | Warning | No | Coverage availability issue is a warning |

---

### Typelist: CoverageAvailabilityType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\CoverageAvailabilityType.tti`
**Description:** Coverage is available or unavailable
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| available | Available | No | Coverage is available |
| unavailable | Unavailable | No | Coverage is unavailable |

---

### Typelist: CoverageForm

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\CoverageForm.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\CoverageForm.ttx`
**Description:** The set of coverages that apply to the CP Line instance.
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| BPP | Building and Personal Property | No | Building and Personal Property |
| CondoAssoc | Condominium Association | No | Condominium Association |
| CondoUnitOwners | Condominium Unit-Owners | No | Condominium Unit-Owners |

---

### Typelist: CoveragePartType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\CoveragePartType.tti`
**Description:** CoveragePartType
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| *(None defined)* | *Dynamic or database-driven* | No | Typelist populated dynamically at runtime or via database table |

---

### Typelist: CoveragePatternSearchType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\CoveragePatternSearchType.tti`
**Description:** To be used in ClausePatternSearchCriteria to search for specific clause's subtypes.
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Coverage | Coverage | No | Search for Coverages |
| Exclusion | Exclusion | No | Search for Exclusions |
| Condition | Condition | No | Search for Conditions |
| ExclCond | Exclusion and Condition | No | Search for Exclusions and Conditions |

---

### Typelist: CoverageSymbolType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\CoverageSymbolType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\CoverageSymbolType.ttx`
**Description:** A kind of CoverageSymbolPattern, since the patterns often duplicate each other across groups
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| ANY | ANY | No | Any Vehicle |
| OVO | OVO | No | Owned Vehicles Only |
| OPV | OPV | No | Owned Private Passenger Vehicles |
| OCV | OCV | No | Owned Commercial Vehicles |
| SRC | SRC | No | Compulsory State Requirement |
| DVO | DVO | No | Designated Vehicles Only |
| HVO | HVO | No | Hired Vehicles Only |
| NOV | NOV | No | Non Owned Vehicles |
| CUS | CUS | No | Custom Definition |

---

### Typelist: CoveredPartyType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\CoveredPartyType.tti`
**Description:** Categorizes coverages by the type of party covered
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| FirstParty | First Party | No | First Party |
| ThirdParty | Third Party | No | Third Party |

---

### Typelist: CovTermModelAgg

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\CovTermModelAgg.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\CovTermModelAgg.ttx`
**Description:** Coverage Term Model Aggregation
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| ag | Annual aggregate | No | Annual aggregate |
| ei | Each incident | Yes | Each incident |
| pi | Per item | No | Per item |
| pc | Per claim | No | Per claim |
| pp | Per person | No | Per person |
| ea | Each accident | No | Each accident |
| po | Per occurrence | No | Per occurrence |
| cc | Each common cause | No | Each common cause |

---

### Typelist: CovTermModelRest

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\CovTermModelRest.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\CovTermModelRest.ttx`
**Description:** Coverage Term Model Scope
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| acc | Accident | No | Accident |
| bia | Bodily injury by accident | No | Bodily injury by accident |
| bi | Bodily injury | No | Bodily injury |
| bid | Bodily injury by disease | No | Bodily injury by disease |
| bld | Building | No | Building |
| edi | Employee dishonesty | No | Employee dishonesty |
| exp | Expense | No | Expense |
| ind | Indemnity | No | Indemnity |
| med | Medical | No | Medical |
| mni | Medical and indemnity | No | Medical and indemnity |
| pd | Property damage | No | Property damage |
| per | Personal | No | Personal |
| prd | Product | No | Product |
| prp | Property | No | Property |
| pip | PIP | No | PIP |
| bipd | Bodily injury/property damage | No | Bodily injury/property damage |
| pip-wage | PIP Wage Loss Benefits | No | PIP Wage Loss Benefits |
| pip-death | PIP Death Benefits | No | PIP Death Benefits |
| pip-voc | PIP Rehab Benefits | No | PIP Rehab Benefits |
| pip-services | PIP Replacement Services | No | PIP Replacement Services |
| pip-medical | PIP Medical Benefits | No | PIP Medical Benefits |

---

### Typelist: CovTermModelType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\CovTermModelType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\CovTermModelType.ttx`
**Description:** Coverage Term Model Type
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Limit | Limit | No | Limit |
| Deductible | Deductible | No | Deductible |
| Coinsurance | Coinsurance | No | Coinsurance |
| Exclusion | Exclusion | No | Exclusion |
| Other | Other | No | Other |
| Peril | Peril | No | Peril |

---

### Typelist: CovTermModelVal

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\CovTermModelVal.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\CovTermModelVal.ttx`
**Description:** Coverage Term Model Value Type
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| money | Money | No | Money |
| percent | Percent | No | Percent |
| days | Days | No | Days |
| hours | Hours | No | Hours |
| count | Count | No | Integer number of things (e.g., people, etc.) |
| other | Other | No | other |
| boolean | Boolean | Yes | boolean |

---

### Typelist: CovTermUseType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\CovTermUseType.tti`
**Description:** Coverage Term Use Type
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Direct | Direct | No | Direct user entered Value plus TermModel |
| Option | Option | No | Single selectable option |
| Package | Package | No | Selectable Package (set) of options |
| Boolean | Boolean | No | User selection |
| DateTime | Date time | No | Date time value |
| String | String | No | String value |
| Typekey | Typekey | No | Typekey value |

---

### Typelist: CPCauseOfLoss

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\CPCauseOfLoss.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\CPCauseOfLoss.ttx`
**Description:** Property Cause Of Loss
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Basic | Basic | No | Basic |
| Broad | Broad | No | Broad |
| Special | Special | No | Special |

---

### Typelist: CPReportingForm

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\CPReportingForm.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\CPReportingForm.ttx`
**Description:** Reporting Form
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| NonReporting | Non Reporting | No | Non Reporting |
| Daily | Daily | No | Daily |
| Weekly | Weekly | No | Weekly |
| Monthly | Monthly | No | Monthly |
| Quarterly | Quarterly | No | Quarterly |
| Annual | Annual | No | Annual |

---

### Typelist: CPValuationMethod

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\CPValuationMethod.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\CPValuationMethod.ttx`
**Description:** Property Cause Of Loss
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| ReplaceCost | Replacement Cost | No | Replacement Cost |
| FuncValue | Functional Value | No | Functional Value |
| ActualCash | Actual Cash Value | No | Actual Cash Value |
| AgreedAmt | Agreed Amount | No | Agreed Amount |

---

### Typelist: CreditCardIssuer

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\CreditCardIssuer.tti`
**Description:** Defines available credit cards
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| amex | American Express | No | American Express |
| dinersclub | Diners Club | No | Diners Club |
| discover | Discover | No | Discover |
| mastercard | MasterCard | No | MasterCard |
| visa | Visa | No | Visa |

---

### Typelist: CreditCardType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\CreditCardType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\CreditCardType.ttx`
**Description:** Credit Card Type
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| visa | Visa | No | Visa |
| master | MasterCard | No | MasterCard |

---

### Typelist: Currency

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\Currency.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\Currency.ttx`
**Description:** Types of Currencies.
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| usd | USD | No | US Dollar |
| eur | EUR | No | Euro |
| gbp | GBP | No | United Kingdom Pound |
| cad | CAD | No | Canadian Dollar |
| aud | AUD | No | Australian Dollar |
| rub | RUB | No | Russian Ruble |
| jpy | JPY | No | Japanese Yen |

---

### Typelist: CustomerServiceTier

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\CustomerServiceTier.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\CustomerServiceTier.ttx`
**Description:** Represents the customer service tier
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| silver | Silver Customer | No | The service tier for Silver customers |
| gold | Gold Customer | No | The service tier for Gold customers |
| platinum | Platinum Customer | No | The service tier for Platinum customers |

---

### Typelist: CustomHistoryType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\CustomHistoryType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\CustomHistoryType.ttx`
**Description:** Custom history event types, used to support once-only execution of rules
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| *(None defined)* | *Dynamic or database-driven* | No | Typelist populated dynamically at runtime or via database table |

---

### Typelist: DataChangeStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\DataChangeStatus.tti`
**Description:** Status of a DataChange.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Open | Open | No | The gosu was added but not yet run |
| Discarded | Discard | No | The gosu was discarded without being run |
| Executing | Executing | No | The gosu is being executed |
| Failed | Failed | No | The gosu was executed but threw an exception |
| Completed | Completed | No | The gosu was executed and did not throw an exception |

---

### Typelist: DataDistributionType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\DataDistributionType.tti`
**Description:** Type of data distributions
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| app_specific | App specific | No | Data distribution provided by the application |
| assignable | Assignable_by_date | No | Distribution of assignable by date |
| adhoc | Ad hoc | No | Ad hoc distribution supplied as input |

---

### Typelist: DataGenActionType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\DataGenActionType.tti`
**Description:** Action type performed by data-gen
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| restore | Restore | No | Restore DB from pcb. |
| advanceDate | AdvanceDate | No | Advancing all dates field in DB. |
| initialize | Initialize | No | Initialize DB. |

---

### Typelist: DataGenStatusType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\DataGenStatusType.tti`
**Description:** Data-gen action status.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| succeed | Succeed | No | Action succeeded. |
| failed | Failed | No | Action failed. |
| inProgress | InProgress | No | Action in progress. |

---

### Typelist: DateBinDataType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\DateBinDataType.tti`
**Description:** The type of data to be stored in a date binned distribution,   determining which column of a DateBinnedDDValue to display
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Typekey | Typekey | No | A GW Typekey column |
| Boolean | Boolean | No | A Boolean column |

---

### Typelist: DateCalcUnit

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\DateCalcUnit.tti`
**Description:** Delay unit
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| CalendarDays | Calendar Days | No | Date calculations should be made in calendar days. |
| BusinessDays | Business Days | No | Date calculations should be made in business days. |

---

### Typelist: DateFieldsToSearchType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\DateFieldsToSearchType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\DateFieldsToSearchType.ttx`
**Description:** The search options for the date searches in search
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| *(None defined)* | *Dynamic or database-driven* | No | Typelist populated dynamically at runtime or via database table |

---

### Typelist: DateRangeChoiceType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\DateRangeChoiceType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\DateRangeChoiceType.ttx`
**Description:** The predetermined list of date ranges we can search for
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| *(None defined)* | *Dynamic or database-driven* | No | Typelist populated dynamically at runtime or via database table |

---

### Typelist: DateSearchType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\DateSearchType.tti`
**Description:** What kind of date search we are doing
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| fromlist | List | No | Selected from a list |
| enteredrange | Enter Dates | No | An entered range |

---

### Typelist: DayOfWeek

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\DayOfWeek.tti`
**Description:** All of the days of the week
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Monday | Monday | No | Monday |
| Tuesday | Tuesday | No | Tuesday |
| Wednesday | Wednesday | No | Wednesday |
| Thursday | Thursday | No | Thursday |
| Friday | Friday | No | Friday |
| Saturday | Saturday | No | Saturday |
| Sunday | Sunday | No | Sunday |

---

### Typelist: DBUpdateStatsRunnerType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\DBUpdateStatsRunnerType.tti`
**Description:** Type of process running update statistics
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Batch | Batch | No | Batch Process running update statistics |
| Datagen | Datagen | No | Datagen running update statistics |
| Loader | Loader | No | Loader running update statistics |
| TableImport | TableImport | No | TableImport running update statistics |
| Upgrade | Upgrade | No | Upgrade running update statistics |

---

### Typelist: DeductibleBasis

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\DeductibleBasis.tti`
**Description:** DeductibleBasis
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| perclm | perclm | No | Per Claim |
| perocc | perocc | No | Per Occurrence |

---

### Typelist: DeductibleCauseofLoss

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\DeductibleCauseofLoss.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\DeductibleCauseofLoss.ttx`
**Description:** Multiple Deductible Cause of Loss
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 1 | 1 All | No | All covered causes of loss |
| 2 | 2 Except wind/hail | No | All Covered Causes of Loss except Windstorm or Hail |
| 3 | 3 Except theft | No | All covered causes of loss except theft |
| 4 | 4 Except wind/hail/theft | No | All covered causes of loss except windstorm or hail and theft |
| 5 | 5 Windstorm and hail | No | Windstorm or hail |
| 6 | 6 Theft | No | Theft |

---

### Typelist: DepositFrequency

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\DepositFrequency.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\DepositFrequency.ttx`
**Description:** Average frequency of deposits
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Daily | Daily | No | Daily |
| 2_per_week | 2 per week | No | 2 per week |
| 3_per_week | 3 per week | No | 3 per week |
| Weekly | Weekly | No | Weekly |
| Other | Other | No | Other |

---

### Typelist: DepPmntScheduleType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\DepPmntScheduleType.tti`
**Description:** Type of GNP Subtotal for Non-proportional reinsurance agreement.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| FullyInAdvance | Fully In Advance | No | Fully in advance |
| QuarterlyInAdvance | Quarterly In Advance | No | Quarterly in advance |

---

### Typelist: DesignateSitesOps

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\DesignateSitesOps.tti`
**Description:** DesignateSitesOps
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| operation | Operation | No | Operation |
| site | Site | No | Site |

---

### Typelist: DestructionRequestStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\DestructionRequestStatus.tti`
**Description:** Status in the Contact Purge Process
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| DoesNotExist | Does Not Exist | No | Request for destruction does not exist |
| Unprocessed | Unprocessed | No | New Request that has not been processed yet |
| InProgress | In Progress | No | The destruction request is in progress |
| Finished | Finished | No | Request has been processed and the contact should have been destroyed if possible. |

---

### Typelist: DiffReason

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\DiffReason.tti`
**Description:** Reason for calling Diff code
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| PolicyReview | PolicyReview | No | Displaying policy review screen |
| ApplyChanges | ApplyChanges | No | Determine changes to apply from this branch |
| Integration | Integration | No | Determine integration changes |
| MultiVersionJob | MultiVersionJob | No | Multi-version comparison |
| CompareJobs | CompareJobs | No | Compare jobs |
| FindDuplicates | FindDuplicates | No | Determine changes to this branch that are duplicated at another effective time |
| ExpirationDateCheck | ExpirationDateCheck | No | Determine changes to this branch that need to be checked to possibly move up their ExpirationDates |
| Import | Import | No | Comparing differences when importing line entities |

---

### Typelist: DistToWorkSchool

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\DistToWorkSchool.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\DistToWorkSchool.ttx`
**Description:** Distance to Work or School
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Under15Miles | Under 15 miles (one-way) | No | Under 15 miles (one-way) |
| Over15Miles | Over 15 miles (one-way) | No | Over 15 miles (one-way) |

---

### Typelist: DivingBoards

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\DivingBoards.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\DivingBoards.ttx`
**Description:** Number of diving boards
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 1 | 1 | No | 1 |
| 2 | 2 | No | 2 |
| 3 | 3 | No | 3 |
| 4 | 4 | No | 4 |
| 5 | 5 | No | 5 |
| 6 | 6 | No | 6 |
| 7 | 7 | No | 7 |
| 8 | 8 | No | 8 |
| 9 | 9 | No | 9 |
| 10 | 10 | No | 10 |

---

### Typelist: DocumentBindingType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\DocumentBindingType.tti`
**Description:** 
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| EARLY | EARLY | No | Payload for document creation is generated immediately |
| EARLY_DEFERRED | EARLY_DEFERRED | No | Payload for the document creation is generated immediately but asynchronously |
| LATE | LATE | No | Payload for document creation is not generated until the request for that document is issued |

---

### Typelist: DocumentSection

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\DocumentSection.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\DocumentSection.ttx`
**Description:** Section for the document
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| bills | Bills | No | Bills |
| medical | Medical | No | Medical |
| indemnity | Indemnity | No | Indemnity |
| rehab | Rehab | No | Rehab |
| legal | Legal | No | Legal |
| correspondence | Correspondence | No | Correspondence |
| misc | Misc | No | Misc |

---

### Typelist: DocumentSecurityType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\DocumentSecurityType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\DocumentSecurityType.ttx`
**Description:** Type of the document for access-restriction purposes
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| unrestricted | Unrestricted | No | Document that does not require access restriction |
| internalonly | Internal only | No | Document that should not be viewed by people outside the company |
| sensitive | Sensitive | No | Document that is sensitive in nature |

---

### Typelist: DocumentStatusType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\DocumentStatusType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\DocumentStatusType.ttx`
**Description:** Status of the document
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| draft | Draft | No | Draft |
| approving | Approving | No | Approving |
| approved | Approved | No | Approved |
| final | Final | No | Final |
| filed | Filed | Yes | Filed |

---

### Typelist: DocumentTemplateType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\DocumentTemplateType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\DocumentTemplateType.ttx`
**Description:** Type of document that can be generated off of a Policy or other Policy-related entity
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| AuditPackage | Audit Package | No | A package generated for an auditor to complete an audit. |
| CancellationQuote | Cancellation Quote | No | The quote letter for a cancellation |
| PolicyChangeQuote | Policy Change Quote | No | The quote letter for a policy change |
| ReinstatementQuote | Reinstatement Quote | No | The quote letter for a reinstatement |
| RenewalQuote | Renewal Quote | No | The quote letter for a renewal |
| RewriteQuote | Rewrite Quote | No | The quote letter for a rewrite |
| RewriteNewAccountQuote | RewriteNewAccount Quote | No | The quote letter for a rewrite new account |
| SubmissionQuote | Submission Quote | No | The quote letter for a submission |
| DecSheet | Dec Sheet | Yes | Declaration sheet |
| Binder | Binder | No | Binder |

---

### Typelist: DocumentType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\DocumentType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\DocumentType.ttx`
**Description:** Type of document
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| diagram | Diagram | No | Diagram |
| email | Email | No | Email |
| email_sent | Email Sent | No | Email created and sent from within PolicyCenter |
| inspectionreport | Inspection report | No | Inspection report |
| newbusiness | New business application | No | New business application |
| renewalinfo | Renewal information/instructions | No | Renewal information/instructions |
| audit | Audit report | No | Audit report |
| losses | Loss information | No | Loss information |
| mvr | MVR | No | MVR |
| credit | Credit report | No | Credit report |
| statement | Statement | No | Statement |
| letter_received | Letter received | No | Letter received |
| letter_sent | Letter sent | No | Letter sent |
| confirm_letter | Confirmation letter | No | Confirmation letter document |
| decline_letter | Declination letter | No | Declination letter document |
| not_taken_letter | Not-Taken letter | No | Acknowledgement letter for Policy Not-Taken document |
| policy_summary | Policy summary | No | Policy summary |
| quote | Quote | No | Quote |
| decsheet | DecSheet | No | DecSheet |
| binder | Binder | No | Binder |
| loss_history | Loss history | No | Loss history type document |
| other | Other | No | Other |

---

### Typelist: DriverExperience

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\DriverExperience.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\DriverExperience.ttx`
**Description:** Driver experience
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| LessThan5 | Less than 5 | Yes | Less than 5 years of experience |
| FiveToTen | 5 to 10 | Yes | 5 - 10 years of experience |
| TenToTwenty | 10 to 20 | Yes | 10 - 20 years of experience |
| MoreThanTwenty | More than 20 | Yes | Main driver experience less than 5 years |
| Morethan2 | More than 2 years | No | More than 2 years of experience |
| onetotwo | 1 - 2 years | No | 1 - 2 years of experience |
| sixtoelevenmo | 6 - 11 months | No | 6 - 11 months of experience |
| lessthan6mo | Less than 6 months | No | Less than 6 months experience |

---

### Typelist: DwellingLocationType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\DwellingLocationType.tti`
**Description:** Dwelling Location Type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| city | In City Limits | No | In City Limits |
| fire | In Fire District | No | In Fire District |
| prot | In Protected Suburb | No | In protected suburb |
| unprot | In Unprotected Area | No | In unprotected Area |
| other | Other | No | Other |

---

### Typelist: DwellingOccupancyType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\DwellingOccupancyType.tti`
**Description:** Dwelling Occupancy Type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| owner | Owner Occupied | No | Owner Occupied |
| tenant | Tenant Occupied | No | Tenant Occupied |
| vacant | Vacant | No | Vacant |
| uoccupied | Unoccupied | No | Unoccupied |
| inconst | Under Construction | No | Under construction |

---

### Typelist: DwellingUsage

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\DwellingUsage.tti`
**Description:** Dwelling Usage
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| primary | Primary | No | Primary |
| secondary | Secondary | No | Secondary |
| seasonal | Seasonal | No | Seasonal |
| rental | Rental Property | No | Rental Property |

---

### Typelist: EditionStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\EditionStatus.tti`
**Description:** Status of Installed Edition
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| active | Active | No | Currently active installed edition |
| preloaded | Preloaded | No | Loaded installed edition waiting to be activated |
| withdrawn | Withdrawn | No | Previously active edition |

---

### Typelist: EffDatedChangeType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\EffDatedChangeType.tti`
**Description:** Type of change made to this row
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| slice | Slice | No | Change made in slice mode |
| slice_merged | SliceMerged | No | Bean has had its changes resolved if OOSE change |
| merge | Merge | No | Change made by merging forward change |
| window | Window | No | Change made in window mode |
| merge_base | MergeBase | No | The base for merges if entity does not have a BasedOn |

---

### Typelist: EffectivenessGrade

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\EffectivenessGrade.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\EffectivenessGrade.ttx`
**Description:** Building Code Effectiveness Grade
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 00 | N/A | No | N/A |
| 01 | 1 | No | 1 |
| 02 | 2 | No | 2 |
| 03 | 3 | No | 3 |
| 04 | 4 | No | 4 |
| 05 | 5 | No | 5 |
| 06 | 6 | No | 6 |
| 07 | 7 | No | 7 |
| 08 | 8 | No | 8 |
| 09 | 9 | No | 9 |
| 10 | 10 | No | 10 |

---

### Typelist: EmployeeClass

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\EmployeeClass.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\EmployeeClass.ttx`
**Description:** Classification of employee
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Accountants | Accountants and assistants | No | Accountants and assistants |
| Adjusters | Adjusters | No | Adjusters |
| Administrators | Administrators and assistants | No | Administrators and assistants |
| Appraisers | Appraisers and clerks acting as appraisers | No | Appraisers and clerks acting as appraisers |
| Attorneys | Attorneys | No | Attorneys |
| Auditors | Auditors and assistants | No | Auditors and assistants |
| Bookkeepers | Bookkeepers | No | Bookkeepers |
| BusDrivers | Bus drivers | No | Bus drivers |
| Buyers | Buyers and assistants | No | Buyers and Assistants |
| Canvassers | Canvassers (door-to-door salespeople) | No | Canvassers (door-to-door salespeople) |
| Cashiers | Cashiers and assistants | No | Cashiers and assistants |
| Chairpersons | Chairpersons | No | Chairpersons |
| Chefs | Chefs who order food | No | Chefs who order food |
| Collectors | Collectors | No | Collectors |
| ComputerProgrammers | Computer programmers | No | Computer programmers |
| Comptrollers | Comptrollers and assistants | No | Comptrollers and assistants |
| CreditClerks | Credit clerks and managers | No | Credit clerks and managers |
| Custodians | Custodians | No | Custodians |
| DeliveryPersons | Delivery persons | No | Delivery persons |
| Demonstrators | Demonstrators | No | Demonstrators |
| Dietitians | Dietitians who order food | No | Dietitians who order food |
| Drivers | Drivers and drivers' helpers | No | Drivers and drivers' helpers |
| FoodInspectors | Food Inspectors | No | Food Inspectors |
| HeadPharmacists | Head pharmacists | No | Head pharmacists |
| Instructors | Instructors having custody of money/securities | No | Instructors having custody of money/securities |
| Janitors | Janitors | No | Janitors |
| LockerRoomAttendants | Locker room attendants | No | Locker room attendants |
| MaitreDs | Maitre d's and assistants | No | Maitre d's and Assistants |
| Managers | Managers and assistants | No | Managers and Assistants |
| MedicalDirectors | Medical directors | No | Medical directors |
| OutsideMessengers | Outside messengers | No | Outside messengers |
| PayrollDistributers | Payroll distributers | No | Payroll distributers |
| PurchasingAgents | Purchasing agents and assistants | No | Purchasing agents and assistants |
| ReceivingClerks | Receiving clerks | No | Receiving clerks |
| RefineryGaugers | Refinery gaugers handling refined gas/oil | No | Refinery gaugers handling refined gas/oil |
| Salespeople | Salespeople | No | Salespeople |
| SecurityPersonnel | Security personnel | No | Security personnel |
| SrvcStatAttendents | Service station attendents | No | Service station attendents |
| ShippingClerks | Shipping clerks | No | Shipping clerks |
| StockClerks | Stock clerks | No | Stock clerks |
| Storekeepers | Storekeepers | No | Storekeepers |
| StoreroomPersonnel | Storeroom personnel | No | Storeroom personnel |
| Superintendents | Superintendents and assistants | No | Superintendents and assistants |
| Supervisors | Supervisors and assistants | No | Supervisors and assistants |
| TaxiDrivers | Taxi drivers | No | Taxi drivers |
| Teachers | Teachers having custody of money/securities | No | Teachers having custody of money/securities |
| Timekeepers | Timekeepers and assistants | No | Timekeepers and assistants |
| TruckDrivers | Truck drivers | No | Truck drivers |
| WarehousePersonnel | Warehouse personnel | No | Warehouse Personnel |
| WineCellarPersonnel | Wine cellar personnel | No | Wine cellar personnel |
| WineStewards | Wine stewards | No | Wine stewards |

---

### Typelist: EmployeeLeasingType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\EmployeeLeasingType.tti`
**Description:** Leasing type, supplied or received
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| supplied | Supplied | No | Employee supplied to others |
| received | Received | No | Employee received from others |

---

### Typelist: EmployerTypeMA

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\EmployerTypeMA.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\EmployerTypeMA.ttx`
**Description:** Mass. WC Employer Type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Private | PRIVATE EMPLOYER | No | PRIVATE EMPLOYER |
| Public | PUBLIC EMPLOYER | No | PUBLIC EMPLOYER |
| Federal | FEDERAL AGENCY (NO TAXES APPLICABLE) | No | FEDERAL AGENCY (NO TAXES APPLICABLE) |
| NA | NOT APPLICABLE | No | NOT APPLICABLE |

---

### Typelist: EmploymentStatusType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\EmploymentStatusType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\EmploymentStatusType.ttx`
**Description:** Status of employment
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| AFULL | Apprentice - full time | No | Apprentice - full time |
| APART | Apprentice - part time | No | Apprentice - part time |
| OFF | Officer | No | Officer |
| Other | Other | No | Other |
| PART | Partner | No | Partner |
| PI | Piece work | No | Piece work |
| REG | Regular employee full time | No | Regular employee full time |
| RET | Retired | No | Retired |
| SEASN | Seasonal | No | Seasonal |
| STRI | On strike | No | On strike |
| TIME | Part time employee | No | Part time employee |
| UNEM | Unemployed | No | Unemployed |
| UNEMPSCR | Unemployed due to plant shutdown, closing or other reduction | No | Unemployed due to plant shutdown, closing or other reduction |
| VOLUN | Volunteer | No | Volunteer |

---

### Typelist: EmpTheftBlanket

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\EmpTheftBlanket.tti`
**Description:** Employee Theft - Blanket or Scheduled
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| *(None defined)* | *Dynamic or database-driven* | No | Typelist populated dynamically at runtime or via database table |

---

### Typelist: EntitySourceType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\EntitySourceType.tti`
**Description:** Identifies whether entity search/fetch operations should be performed against the internal system or some remote system
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| internal | Internal | No | Search/fetch should be performed internally against the local database |
| external | External | No | Search/fetch should be performed against some remote system via a plugin |

---

### Typelist: ErrorCategory

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ErrorCategory.tti`
**Description:** The type of error for messages that are in error
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| *(None defined)* | *Dynamic or database-driven* | No | Typelist populated dynamically at runtime or via database table |

---

### Typelist: ETLStrings

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ETLStrings.tti`
**Description:** ETLStrings
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| NOT_APPLICABLE | Not Applicable | Yes | NOT APPLICABLE |
| UNKNOWN | Unknown | Yes | UNKNOWN |
| NOT_FOUND | Not Found | Yes | NOT FOUND |
| RECORD_NOT_FOUND | Record Not Found | Yes | RECORD NOT FOUND |
| SUSPENSE_PAYMENT | Suspense Payment | Yes | SUSPENSE_PAYMENT |
| ETL_UNKNOWN | Unknown | No | UNKNOWN |
| ETL_NOT_APPLICABLE | Not Applicable | No | NOT APPLICABLE |
| ETL_NOT_FOUND | Not Found | No | NOT FOUND |
| ETL_RECORD_NOT_FOUND | Record Not Found | No | RECORD NOT FOUND |

---

### Typelist: ExcludedExposureType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ExcludedExposureType.tti`
**Description:** ExcludedExposureType
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| operations | operations | No | operations |
| productswork | products/work | No | products/work |
| services | services | No | services |
| location | location | No | location |

---

### Typelist: ExistenceType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ExistenceType.tti`
**Description:** Defines if a PolicyCenter entity's existence on a policy is required, suggested, or electable.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Required | Required | No | Entity is required to exist on the policy if it is available. |
| Suggested | Suggested | No | Entity is initially added to the policy if it is available, but may be removed/declined by the user. |
| Electable | Electable | No | Entity is initially NOT added to the policy, but may be added to the policy by the user if it is available. |

---

### Typelist: ExpLossPaymentLimits

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ExpLossPaymentLimits.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\ExpLossPaymentLimits.ttx`
**Description:** Extra Expense - Expanded Loss Payment Limits
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 30_60_90_100 | 30%-60%-90%-100% | No | 30%-60%-90%-100% |
| 25_50_75_100 | 25%-50%-75%-100% | No | 25%-50%-75%-100% |
| 20_40_80_100 | 20%-40%-80%-100% | No | 20%-40%-80%-100% |

---

### Typelist: ExpModStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ExpModStatus.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\ExpModStatus.ttx`
**Description:** Experience Mod Status
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| non | Not eligible | No | Risk is not eligible for experience modification. |
| est | Estimated | No | The experience modifier is estimated. |
| fin | Final | No | The experience modifier is final. |

---

### Typelist: ExtendedRptType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ExtendedRptType.tti`
**Description:** ExtendedRptType
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Location | Location | No | Location |
| ProductWork | Product/Work | No | Product/Work |
| Accident | Accident | No | Accident |

---

### Typelist: ExtentProtectionType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ExtentProtectionType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\ExtentProtectionType.ttx`
**Description:** Extent of protection
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Default | Default | No | Default |

---

### Typelist: ExternalToolType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ExternalToolType.tti`
**Description:** The different external tools available
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| word | Microsoft Word | No | Microsoft Word |
| adobe | Adobe Acrobat | No | Adobe Acrobat |
| ie | Microsoft Internet Explorer | No | Microsoft Internet Explorer |

---

### Typelist: ExtRptngProdWorkDateType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ExtRptngProdWorkDateType.tti`
**Description:** ExtRptngProdWorkDateType
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| manufacture | manufacture | No | manufacture |
| sale | sale | No | sale |
| distribution | distribution | No | distribution |
| disposal | disposal | No | disposal |
| completion | completion | No | completion |

---

### Typelist: FactorQueryStrategy

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\FactorQueryStrategy.tti`
**Description:** Define how a query on a rate table is processed
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Memory | Memory | No | The query is processed in memory |
| Database | Database | No | The query is processed in the database |

---

### Typelist: FailoverState

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\FailoverState.tti`
**Description:** FailoverState
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| NotStarted | Not Started | No | Automatic failover not started |
| InProgress | In Progress | No | Automatic failover is in progress |
| Postponed | Postponed | No | Automatic failover is postponed |
| Failed | Failed | No | Automatic failover failed (requires manual intervention) |

---

### Typelist: FedEmpLiabAct

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\FedEmpLiabAct.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\FedEmpLiabAct.ttx`
**Description:** Federal Employers Liability coverage Act type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| mari | Maritime Coverage | No | Maritime Coverage |
| fela | Fed Empl Liab Act | No | Fed Empl Liab Act |

---

### Typelist: FedEmpLiabProgram

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\FedEmpLiabProgram.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\FedEmpLiabProgram.ttx`
**Description:** Federal Employers Liability coverage program type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| ProgramI | Program I | No | Program I |
| ProgramII | Program II | No | Program II |

---

### Typelist: FinalAuditOption

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\FinalAuditOption.tti`
**Description:** Preliminary option whether a final audit will be scheduled and started
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Rules | Determined by business rules | No | Final audit will be scheduled, and business rule will determine if it will be started |
| Yes | Yes | No | Final audit will be scheduled and started |
| No | No | No | Final audit will not be scheduled |

---

### Typelist: FinancialSearchField

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\FinancialSearchField.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\FinancialSearchField.ttx`
**Description:** The search field for financial searches
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Amount | Amount | No | Amount |

---

### Typelist: FireAlarmType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\FireAlarmType.tti`
**Description:** Fire Alarm Type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| none | None | No | No fire alarm |
| local | Alarm - Local | No | Local fire alarm |
| monitoringcenter | Alarm - To Monitoring Center | No | Fire alarm reports to monitoring center |

---

### Typelist: FireLegal

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\FireLegal.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\FireLegal.ttx`
**Description:** Fire legal liability
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 50000 | 50,000 (included) | No | 50,000 (included) |
| 100000 | 100,000 | No | 100,000 |
| 250000 | 250,000 | No | 250,000 |
| 500000 | 500,000 | No | 500,000 |

---

### Typelist: FireProtectClass

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\FireProtectClass.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\FireProtectClass.ttx`
**Description:** Fire protection class
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 1 | Superior | No | Superior |
| 2 | Standard | No | Standard |
| 3 | Limited | No | Limited |
| 4 | Poor | No | Poor |
| 5 | None | No | None |

---

### Typelist: FleetType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\FleetType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\FleetType.ttx`
**Description:** Options for a vehicle's membership in a fleet
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Fleet | 10 or more units | No | 10 or more units |
| NonFleet | Fewer than 10 units | No | Fewer than 10 units |

---

### Typelist: FocusOfExclusion

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\FocusOfExclusion.tti`
**Description:** FocusOfExclusion
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Location | Location | No | Location |
| ProductWork | ProductWork | No | Product/Work |
| Accident | Accident | No | Accident |

---

### Typelist: FormInferenceTime

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\FormInferenceTime.tti`
**Description:** Defines the points in time at which a form can be inferred.  Used both for FormPattern configuration and on the forms themselves to track when they were inferred.
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| quote | Quote Time | No | Indicates that this form was inferred at quote time |
| bind | Bind Time | No | Indicates that this form was inferred at bind time |

---

### Typelist: FoundationType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\FoundationType.tti`
**Description:** Foundation Type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Slab | Slab | No | Slab |
| RaisedSlab | Raised Slab | No | Raised Slab |
| PierAndBeam | Pier and Beam | No | Pier and Beam |
| CrawlSpace | Crawl Space | No | Crawl Space |
| FullBasement | Full Basement | No | Full Basement |

---

### Typelist: FuelLineLocationType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\FuelLineLocationType.tti`
**Description:** Fuel Line Location Type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| under | Underground | No | Underground |
| through | Through Foundation | No | Through Foundation |

---

### Typelist: FuelTankLocationType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\FuelTankLocationType.tti`
**Description:** Fuel Tank Location Type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| IAGMF | Indoor - Masonry Floor | No | Indoor - Masonry Floor |
| IAGNMF | Indoor - No Masonry Floor | No | Indoor - No Masonry Floor |
| OAG | Outdoor Above Ground | No | Outdoor Above Ground |
| OBG | Outdoor Below Ground | No | Outdoor Below Ground |

---

### Typelist: FXRateMarket

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\FXRateMarket.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\FXRateMarket.ttx`
**Description:** Types of foreign exchange rate markets.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| static_table | StaticTable | No | A static table of one-way rates. |

---

### Typelist: GarageType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\GarageType.tti`
**Description:** Garage Type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| None | No Garage | No | No Garage |
| Attached-1 | Attached Garage - 1 Car | No | Attached Garage - 1 Car |
| Attached-2 | Attached Garage - 2 Car | No | Attached Garage - 2 Car |
| Attached-3 | Attached Garage - 3 Car | No | Attached Garage - 3 Car |
| Attached-4 | Attached Garage - 4+ Cars | No | Attached Garage - 4+ Cars |
| Detached-1 | Detached Garage - 1 Car | No | Detached Garage - 1 Car |
| Detached-2 | Detached Garage - 2 Car | No | Detached Garage - 2 Car |
| Detached-3 | Detached Garage - 3 Car | No | Detached Garage - 3 Car |
| Detached-4 | Detached Garage - 4+ Cars | No | Detached Garage - 4+ Cars |

---

### Typelist: GenderType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\GenderType.tti`
**Description:** Gender
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| M | Male | No | Male |
| F | Female | No | Female |

---

### Typelist: GeocodeStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\GeocodeStatus.tti`
**Description:** Describes the status of a geocode on an Address: customers may modify it for different geocoding providers.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| none | None | No | An Address has never been submitted for geocoding. |
| failure | Failure | No | The Geocoding service was unable to geocode the address. |
| city | City | No | The Geocoding service was only able to locate the city from the supplied address. |
| postalcode | Postal Code | No | The Geocoding service was only able to locate the postal code from the supplied address. |
| street | Street | No | The Geocoding service was only able to locate the street from the supplied address. |
| exact | Exact | No | The Geocoding service was able to find an exact match for the supplied address. |

---

### Typelist: GLCostSplitType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\GLCostSplitType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\GLCostSplitType.ttx`
**Description:** The liability limit split type for a GL cost
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| BI | BI | No | Bodily Injury |
| PD | PD | No | Property Damage |
| CSL | CSL | No | Combined Single Limit |

---

### Typelist: GLCostSubline

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\GLCostSubline.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\GLCostSubline.ttx`
**Description:** Subline for this cost
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Premises | Premises | No | Premises and Operations |
| Products | Products | No | Products and Completed Operations |

---

### Typelist: GLCoverageFormType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\GLCoverageFormType.tti`
**Description:** Form of coverage
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Occurrence | Occurrence | No | Occurrence |
| ClaimsMade | Claims Made | No | Claims Made |

---

### Typelist: GLStateCostType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\GLStateCostType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\GLStateCostType.ttx`
**Description:** GLStateCostType
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| TERROR | Terrorism | No | Terrorism |
| TAX | Tax | No | Tax |

---

### Typelist: GNPSubtotalType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\GNPSubtotalType.tti`
**Description:** Type of Gross Net Premium Subtotal for Non-proportional reinsurance agreement.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| GrossPremium | Gross premium | No | Gross premium |
| NetOfProportional | Net of proportional | No | Net of proportional |
| NetOfPerRisk | Net of all per risk | No | Net of all per risk |
| NetOfPerEvent | Net of all per event | No | Net of all per event |
| NetOfPrior | Net of all prior | No | Net of all prior cedings |

---

### Typelist: GroupType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\GroupType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\GroupType.ttx`
**Description:** Types of groups
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| root | Root Group | No | This is the root group of an organization |
| actuary | Actuary unit | No | Actuary unit |
| branch | Branch office | No | Branch office |
| branchaudit | Branch audit | No | Branch audit |
| branchlc | Branch L.C. | No | Branch L.C. |
| branchmkt | Branch marketing | No | Branch marketing |
| branchuw | Branch UW | No | Branch UW |
| clerical | Clerical support | No | Clerical support |
| custserv | Customer service | No | Customer service |
| eservices | Web services unit | No | Web services unit |
| extaudit | Fee audit | No | Fee audit |
| extlc | Fee inspection | No | Fee inspection |
| facre | Fac reinsurance unit | No | Fac reinsurance unit |
| finance | Finance and treasury | No | Finance and treasury |
| general | General | No | General |
| homeofficeadmin | Home office admin services | No | Home office admin services |
| homeofficelc | Home office L.C. | No | Home office L.C. |
| homeofficemkt | Home office marketing | No | Home office marketing |
| homeofficeuw | Home office U.W. | No | Home office UW |
| hq | Corporate headquarters | No | Corporate headquarters |
| mga | Managing general agt | No | Managing general agent |
| policyserve | Policy services | No | Policy services |
| premacct | Premium accounting | No | Premium accounting |
| producer | Producer | No | Producer |
| region | Regional parent group | No | Regional parent group |
| regionlc | Regional L.C. | No | Regional L.C. |
| regionaudit | Regional audit | No | Regional Audit |
| regionuw | Regional UW | No | Regional UW |
| regionmkt | Regional marketing | No | Regional marketing |
| siu | Special investigative unit | No | Special investigative unit |
| solutions | Solutions group | No | Solutions group |
| systemadmin | System administrators | No | System administrators |

---

### Typelist: HazardType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\HazardType.tti`
**Description:** 
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Property | Property | No | Property |
| Liability | Liability | No | Liability |

---

### Typelist: HeatingType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\HeatingType.tti`
**Description:** Type of Heating
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| electric | Electricity | No | Electricity |
| gas | Gas | No | Gas |
| oil | Oil | No | Heating Oil |
| other | Other | No | Other |

---

### Typelist: HistoryType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\HistoryType.tti`
**Description:** The type of claim/exposure history
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| custom | Custom | No | A custom history event happened; see CustomType for details |
| policyedited | Policy edited | No | The policy was edited, and thus marked unverified |
| approval | Approval or Rejection | No | A referral was approved/rejected |

---

### Typelist: HolidayTagCode

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\HolidayTagCode.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\HolidayTagCode.ttx`
**Description:** The holiday tag code
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| general | General | No | General |
| company | Company Holidays | No | Company Holidays |

---

### Typelist: HOPConstructionType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\HOPConstructionType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\HOPConstructionType.ttx`
**Description:** Dwelling Construction Types
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| concrete | Concrete | No | Concrete |
| frame | Frame | No | Frame |
| masonry | Masonry | No | Masonry |
| steel | Steel | No | Steel |
| log | Log | No | Log |
| other | Other | No | Other |

---

### Typelist: HOPCoverageForm

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\HOPCoverageForm.tti`
**Description:** HOP Coverage Form
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| ho2 | HO2 | No | Homeowners (Good) |
| ho3 | HO3 | No | Homeowners (Better) |
| ho5 | HO5 | No | Homeowners (Best) |
| ho4 | HO4 | No | Renters |
| ho6 | HO6 | No | Condo |

---

### Typelist: HOPPremiumType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\HOPPremiumType.tti`
**Description:** Premium type for Homeowners
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| basepremium | Base Premium | No | Base premium |
| adjustmenttobasepremium | Adjustment to Base Premium | No | Adjustment to base premium |
| otherpremium | Other Premium | No | Other premium |

---

### Typelist: HOPRoofType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\HOPRoofType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\HOPRoofType.ttx`
**Description:** Type of building roof
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| composite | Composite | No | Composite |
| asphalt | Asphalt Shingle | No | Asphalt Shingle |
| wood | Wood Shingle | No | Wood Shingle |
| metal | Metal | No | Metal |
| targravel | Tar and Gravel | No | Tar and Gravel |
| slate | Slate | No | Slate |
| tile | Tile | No | Tile |
| other | Other | No | Other |

---

### Typelist: HOPSwimmingPoolType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\HOPSwimmingPoolType.tti`
**Description:** HOP Swimming Pool Type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| AboveGround | Above Ground | No | Above ground |
| InGround | In Ground | No | In ground |

---

### Typelist: ILElementType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ILElementType.tti`
**Description:** The type describing how the logging element is handled (e.g. Profiler-based, manual)
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| profilertag | Profiler Tag | No | The logging element handled by Profiler-based solution. |
| manual | Manual | No | The logging element handled by manual logging instruction put somewhere in the code. |
| workqueue | Work Queue | No | The logging element associated with a work queue |
| job | Job | No | The logging element associated with a job |

---

### Typelist: ImmunityType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ImmunityType.tti`
**Description:** ImmunityType
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Governmental | Governmental | No | Governmental |
| Charitable | Charitable | No | Charitable |

---

### Typelist: ImpactTestCaseProgress

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ImpactTestCaseProgress.tti`
**Description:** ImpactTestCaseProgress
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| new | New | No | New |
| baselineinprogress | BaseLineInProgress | No | Base Line Periods In Progress |
| baselinecomplete | BaseLineComplete | No | Base Line Complete |
| testquoteinprogress | TestQuoteInProgress | No | Test Quote In Progress |
| testquotecomplete | TestQuoteComplete | No | Test Quote Complete |

---

### Typelist: ImpactTestCaseStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ImpactTestCaseStatus.tti`
**Description:** ImpactTestCaseStatus
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Draft | Draft | No | The test case has no policy periods yet |
| Staged | Staged | No | The test case has policy periods; the baseline and test periods are ready to be created |
| Active | Active | No | Test case is ready for test runs |

---

### Typelist: ImpactTestingJobProgress

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ImpactTestingJobProgress.tti`
**Description:** ImpactTestingJobProgress
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| waiting | Waiting | No | Currently waiting to be processed by the batch job |
| processing | Processing | No | Currently being processed by the batch job |
| processed | Processed | No | Has been processed by the batch job |

---

### Typelist: ImpactTestingPrepResult

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ImpactTestingPrepResult.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\ImpactTestingPrepResult.ttx`
**Description:** ImpactTestingPrepResult
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| success | Success | No | The baseline period has been successfully quoted and the test period was created |
| baselinecreationfailed | Baseline period creation failed | No | The baseline period was not created |
| baselinequotefailed | Baseline period quote failed | No | The baseline quote failed |
| testperiodcreationfailed | Test period creation failed | No | The test period creation failed |
| unexpectedfailure | Unexpected failure | No | There was an unexpected failure |

---

### Typelist: ImpactTestingRunResult

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ImpactTestingRunResult.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\ImpactTestingRunResult.ttx`
**Description:** ImpactTestingRunResult
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| success | Success | No | The test period was succesfully quoted |
| testperiodquotefailed | Test period quote failed | No | The test period quote failed |
| unexpectedfailure | Unexpected failure | No | There was an unexpected failure |

---

### Typelist: InboundChunkStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\InboundChunkStatus.tti`
**Description:** The status of Inbound Chunk
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| loading | Loading | No | Records being loaded prior to completion of the file. |
| pending | Pending | No | Records in chunk have not yet been processed. |
| processed | Processed | No | Records in chunk were processed successfully. |
| processed_with_errors | ProcessedWithErrors | No | Records in chunk were processed with errors. |

---

### Typelist: InboundFileStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\InboundFileStatus.tti`
**Description:** The status of an inbound file.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| loaded | Loaded | No | The file has been successfully loaded. |
| duplicate | Duplicate | No | The file was detected as a duplicate. |
| error | Error | No | An error occurred while loading the file. |

---

### Typelist: InboundRecordStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\InboundRecordStatus.tti`
**Description:** The status of an inbound record.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| pending | Pending | No | The record has not yet been processed. |
| processed | Processed | No | The record was processed successfully. |
| error | Error | No | The record could not be processed. |
| skipped | Skipped | No | The record was manually skipped. |
| ignore | Ignore | No | The record should be ignored when processing. |

---

### Typelist: IncidentLimit

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\IncidentLimit.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\IncidentLimit.ttx`
**Description:** Types of incident limits
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| ActualCashValue | Actual cash value | No | Actual cash Value |
| CostRepair | Cost of repair | No | Cost of repair |
| Decline | Decline | No | Decline |

---

### Typelist: IncludeDaysType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\IncludeDaysType.tti`
**Description:** Which days to include in the day count
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| elapsed | Calendar days | No | The number of calendar days elapsed since the starting point; includes all weekends and holidays |
| businessdays | Business days | No | The number of business days since the starting point; does not include weekends and holidays |

---

### Typelist: Inclusion

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\Inclusion.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\Inclusion.ttx`
**Description:** Inclusion Options
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| incl | Include | No | Include |
| excl | Exclude | No | Exclude |

---

### Typelist: IndustryCodeType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\IndustryCodeType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\IndustryCodeType.ttx`
**Description:** A type of industry code (SIC, NAICS, etc)
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| SIC | SIC | No | An SIC code |
| NAICS | NAICS | No | An NAICS code |

---

### Typelist: InflationGuard

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\InflationGuard.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\InflationGuard.ttx`
**Description:** In`flation Guard
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 8 | 8% | No | 8% |
| Other | Other | No | Other |

---

### Typelist: InstalledPolicyLine

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\InstalledPolicyLine.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\InstalledPolicyLine.WC7.ttx`
**Description:** All installed policy lines
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| APD | ManualLine | No | Manual Products |
| BA | BusinessAutoLine | No | BusinessAutoLine |
| BOP | BOPLine | No | BusinessOwnersLine |
| CP | CPLine | No | CommercialPropertyLine |
| GL | GLLine | No | GeneralLiabilityLine |
| HOP | HOPLine | No | HOPLine |
| IM | IMLine | No | InlandMarineLine |
| PA | PersonalAutoLine | No | PersonalAutoLine |
| WC | WorkersCompLine | No | WorkersCompLine |
| WC7 | WC7Line | No | Workers' Comp Line (v7) |

---

### Typelist: InstalledRuleOwnerType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\InstalledRuleOwnerType.tti`
**Description:** The type of property or entity that owns this installed rule
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| RiskObjectProperty | Risk Object Property | No | For entity properties that own a rule (coverable and exposure fields) |
| RiskObjectTypekey | Risk Object Typekey | No | For typekeys that own a rule where the APD dropdown list is a risk object field |
| Clause | Clause | No | For clauses that own a rule |
| ClauseTerm | Clause Term | No | For clause terms that own a rule |
| TermTypekey | Term typekey | No | For typekeys that own a rule which are on a APD term dropdown list |
| TermOptionChoice | Term Option Choice | No | For clause term option choices |
| TermPackageChoice | Term Package Choice | No | For clause term package choices |

---

### Typelist: InstalledRuleValueType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\InstalledRuleValueType.tti`
**Description:** The type of value returned by a default, minimum, or maximum rule on an installed line
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| boolean | Boolean | No | A true/false indicator |
| date | Date | No | A date, optionally with the time |
| decimal | Decimal | No | An amount or percentage with up to 2 decimal places |
| integer | Integer | No | A number with no decimal places |
| string | String | No | A name or description consisting of characters, numbers, etc |
| typekey | Typekey | No | A list of choices to select from |

---

### Typelist: InterestType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\InterestType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\InterestType.ttx`
**Description:** Types of interest
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Tenant | Tenant | No | Tenant |
| Owner | Owner | No | Owner |
| Other | Other | No | Other |

---

### Typelist: IntraInterStateUsage

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\IntraInterStateUsage.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\IntraInterStateUsage.ttx`
**Description:** Intrastate or interstate usage
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 1 | Interstate | No | Interstate |
| 2 | Intrastate | No | Intrastate |
| 3 | Not applicable | No | Not applicable |

---

### Typelist: InvoiceDeliveryMethod

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\InvoiceDeliveryMethod.tti`
**Description:** Defines how the invoice is sent
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| email | Email | No | Invoice is delivered by email |
| mail | Mail | No | Invoice is delivered by mail |

---

### Typelist: InvoicingMethod

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\InvoicingMethod.tti`
**Description:** The different invoicing methods for a PolicyPeriod 
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| DefaultBilling | Default Billing | No | Default billing |
| CustomBilling | Custom Billing | No | Invoicing specified by values for Custom Billing |
| OverriddenInvoiceStream | Overridden Invoice Stream | No | Invoicing specified by values for Invoice Stream Override |

---

### Typelist: IssueSeverity

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\IssueSeverity.tti`
**Description:** The severity of a referral reason
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Blocking | Blocking | No | Unacceptable for any policy |
| High | High | No | Probably serious enough on its own to require a review |
| Medium | Medium | No | Notable enough that an underwriter should probably review |
| Low | Low | No | Probably not important enough to review on its own |

---

### Typelist: JobDateType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\JobDateType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\JobDateType.ttx`
**Description:** The date type (effective, written, reference) used to determine whether the job falls within the dates of a hold
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Effective | Effective Date | No | Effective Date |
| Written | Written Date | No | Written Date |
| Reference | Reference Date | No | Reference Date |

---

### Typelist: Jurisdiction

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\Jurisdiction.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\Jurisdiction.example.ttx`
**Description:** The list of jurisdictions regulating insurance and other licensing within this deployment. This is similar to the State typelist, which is used for addresses and locations. Each code in the Jurisdiction typelist has an additional category set that is based on State typelist. In many deployments, the State and Jurisdiction typelists will be equal
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| AK | Alaska | No | Alaska |
| AL | Alabama | No | Alabama |
| AR | Arkansas | No | Arkansas |
| AZ | Arizona | No | Arizona |
| CA | California | No | California |
| CO | Colorado | No | Colorado |
| CT | Connecticut | No | Connecticut |
| DC | District of Columbia | No | District of Columbia |
| DE | Delaware | No | Delaware |
| FL | Florida | No | Florida |
| GA | Georgia | No | Georgia |
| HI | Hawaii | No | Hawaii |
| IA | Iowa | No | Iowa |
| ID | Idaho | No | Idaho |
| IL | Illinois | No | Illinois |
| IN | Indiana | No | Indiana |
| KS | Kansas | No | Kansas |
| KY | Kentucky | No | Kentucky |
| LA | Louisiana | No | Louisiana |
| MA | Massachusetts | No | Massachusetts |
| MD | Maryland | No | Maryland |
| ME | Maine | No | Maine |
| MI | Michigan | No | Michigan |
| MN | Minnesota | No | Minnesota |
| MO | Missouri | No | Missouri |
| MS | Mississippi | No | Mississippi |
| MT | Montana | No | Montana |
| NC | North Carolina | No | North Carolina |
| ND | North Dakota | No | North Dakota |
| NE | Nebraska | No | Nebraska |
| NH | New Hampshire | No | New Hampshire |
| NJ | New Jersey | No | New Jersey |
| NM | New Mexico | No | New Mexico |
| NV | Nevada | No | Nevada |
| NY | New York | No | New York |
| OH | Ohio | No | Ohio |
| OK | Oklahoma | No | Oklahoma |
| OR | Oregon | No | Oregon |
| PA | Pennsylvania | No | Pennsylvania |
| PR | Puerto Rico | No | Puerto Rico |
| RI | Rhode Island | No | Rhode Island |
| SC | South Carolina | No | South Carolina |
| SD | South Dakota | No | South Dakota |
| TN | Tennessee | No | Tennessee |
| TX | Texas | No | Texas |
| UT | Utah | No | Utah |
| VA | Virginia | No | Virginia |
| VT | Vermont | No | Vermont |
| WA | Washington | No | Washington |
| WI | Wisconsin | No | Wisconsin |
| WV | West Virginia | No | West Virginia |
| WY | Wyoming | No | Wyoming |
| AB | Alberta | No | Alberta |
| BC | British Columbia | No | British Columbia |
| MB | Manitoba | No | Manitoba |
| NB | New Brunswick | No | New Brunswick |
| NL | Newfoundland and Labrador | No | Newfoundland and Labrador |
| NT | Northwest Territories | No | Northwest Territories |
| NS | Nova Scotia | No | Nova Scotia |
| NU | Nunavut | No | Nunavut |
| ON | Ontario | No | Ontario |
| PE | Prince Edward Island | No | Prince Edward Island |
| QC | Quebec | No | Quebec |
| SK | Saskatchewan | No | Saskatchewan |
| YT | Yukon | No | Yukon |
| VI | Virgin Islands | No | Virgin Islands |
| MP | Northern Mariana Islands | No | Northern Mariana Islands |
| MH | Marshall Islands | No | Marshall Islands |
| GU | Guam | No | Guam |
| FM | Federated States of Micronesia | No | Federated States of Micronesia |
| AU_SA | South Australia | No | South Australia |
| AU_NT | Northern Territory | No | Northern Territory |
| AU_QLD | Queensland | No | Queensland |
| AU_NSW | New South Wales | No | New South Wales |
| AU_VIC | Victoria | No | Victoria |
| AU_WA | Western Australia | No | Western Australia |
| AU_TAS | Tasmania | No | Tasmania |
| AU_ACT | A.C.T. | No | Australian Capital Territory |
| AU_JBT | J.B.T. | No | Jervis Bay Territory |
| DE_BY | Bavaria | No | Bavaria |
| DE_BW | Baden-Wuerttemberg | No | Baden-Wuerttemberg |
| DE_BE | Berlin | No | Berlin |
| DE_BB | Brandenburg | No | Brandenburg |
| DE_HB | Bremen | No | Bremen |
| DE_HH | Hamburg | No | Hamburg |
| DE_HE | Hesse | No | Hesse |
| DE_MV | Mecklenburg-Vorpommern | No | Mecklenburg-Vorpommern |
| DE_NI | Lower Saxony | No | Lower Saxony |
| DE_NW | North Rhine-Westphalia | No | North Rhine-Westphalia |
| DE_RP | Rhineland-Palatinate | No | Rhineland-Palatinate |
| DE_ST | Saxony-Anhalt | No | Saxony-Anhalt |
| DE_SH | Schleswig-Holstein | No | Schleswig-Holstein |
| DE_SL | Saarland | No | Saarland |
| DE_SN | Saxony | No | Saxony |
| DE_TH | Thuringia | No | Thuringia |
| JP | Japan | No | Japan |
| FR | France | No | France |
| GB | United Kingdom | No | United Kingdom |

---

### Typelist: JurisdictionType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\JurisdictionType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\JurisdictionType.ttx`
**Description:** Used to categorize Jurisdications.  Each Jurisdiction can be associated with one or more JurisdictionTypes
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| insurance | Insurance | No | Insurance |
| driving_lic | Driver's license | No | Driver's license |
| vehicle_reg | Vehicle registration | No | Vehicle registration |
| ins_tax | Insurance Tax | No | Insurance Tax |
| cons_tax | Consumption tax | No | Consumption tax such as sales tax or VAT |

---

### Typelist: LanguageType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\LanguageType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\LanguageType.ttx`
**Description:** Users' preferred languages
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| de | Deutsch | No | Deutsch |
| en_US | English (US) | No | English (US) |
| es | EspaÃ±ol | No | EspaÃ±ol |
| fr | FranÃ§ais | No | FranÃ§ais |
| ja | æ—¥æœ¬èªž | No | æ—¥æœ¬èªž |

---

### Typelist: LeaseTerminationReason

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\LeaseTerminationReason.tti`
**Description:** Lease Termination Reason
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| GracefulTermination | Graceful Termination | No | The lease gracefully terminated |
| Failure | Failure | No | The lease terminated after an error |
| Transfer | Transfer | No | The lease transferred |
| ServerRestart | Server Restart | No | The orphaned lease terminated by the server restart |
| AutomaticFailover | Automatic Failover | No | The lease terminated by automatic failover |
| ManualFailover | Manual Failover | No | The lease terminated by nodeFailed request |
| FailedFailoverCompletion | Failed failover completion | No | The lease terminated by manual intervention after failover failed |

---

### Typelist: LedgerSide

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\LedgerSide.tti`
**Description:** Defines the accounting classification of an account and the sign of a line item
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| debit | Debit | No | Debit |
| credit | Credit | No | Credit |

---

### Typelist: LengthOfLease

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\LengthOfLease.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\LengthOfLease.ttx`
**Description:** The lease period of a leased or a rented vehicle
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| LessSixMonths | Less than 6 months | No | Less than 6 months |
| SixMonthsOrMore | 6 months or greater | No | 6 months or greater |

---

### Typelist: LetterType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\LetterType.tti`
**Description:** The kind of a Letter entity
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Confirmation | Confirmation | No | Informs that one or more Jobs are being processed |
| Declination | Declination | No | Informs that one or more Jobs have been declined |
| NotTakenAck | Not-Taken | No | Acknowledges that the insured does not want policies from one or more Jobs |

---

### Typelist: LiabilityAct

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\LiabilityAct.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\LiabilityAct.ttx`
**Description:** Liability acts
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| WorkersComp | Workers Comp Acts | No | Workers Comp Acts |
| Federal | Federal Acts | No | Federal Acts |

---

### Typelist: LoadCommandType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\LoadCommandType.tti`
**Description:** Types of load commands
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| errorcleared | Error table cleared | No | Error table cleared |
| exclusioncleared | Exclusion table cleared | No | Exclusion table cleared |
| stagingcleared | Staging tables cleared | No | Staging tables cleared |
| excludeddeleted | Excluded rows deleted | No | Excluded rows deleted from staging tables |
| exclusionpop | Exclusion table populated | No | Exclusion table populated with failed rows from error table |
| integritychecked | Integrity of staging tables checked | No | Integrity of staging tables checked |
| sourceloaded | Source tables loaded | No | Source tables loaded from staging tables |
| zonesourceloaded | Zone Source tables loaded | No | Zone Source tables loaded from staging tables |
| nonexcludeddeleted | Non-excluded rows deleted | Yes | Non-excluded rows deleted from staging tables |
| dbstatsupdated | Database statistics updated on staging tables | No | Database statistics updated on staging tables |
| tablesencrypted | Encrypt data in staging tables | No | Encrypt data in staging tables |

---

### Typelist: LoaderCallbackTimeType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\LoaderCallbackTimeType.tti`
**Description:** Types of LoaderCallback execution times
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| beforeidgeneration | Before ID generation | No | Before ID generation |
| beforeinsertselects | Before insert/selects into source tables | No | Before insert/selects into source tables |
| afterinsertselects | After insert/selects into source tables | No | After insert/selects into source tables |

---

### Typelist: LoadErrorType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\LoadErrorType.tti`
**Description:** Types of load error events
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| consistchildren1 | Consistent children failure within staging tables | No | Consistent children failure found within staging tables |
| consistchildren2 | Consistent children failure between staging and sourcetables | No | Consistent children failure found between staging and source tables |
| requiredmatch | Required match | No | Rows found in staging table with required referencing rows in array table |
| dtordering | Date time ordering | No | Rows found in staging table that violate a date time ordering |
| abstractdatatype | Abstract data type | No | Rows found in staging table with values that violate rules of an abstract data type |
| checkconstraint | Check constraint | No | Rows found in staging table that violate a check constraint |
| uniqconstraint1 | Unique constraint within staging table | No | Rows found in staging table that violate a unique constraint |
| uniqconstraint2 | Unique constraint between source and staging table | No | Rows found in staging table that match rows in source table on all columns of a unique index |
| subtype | Subtype | No | Rows found in table with invalid values for a subtype column |
| subtypespec | Non-nulls in subtype-specific columns | No | Rows found in table with non-null values for one or more subtype-specific columns for a different subtype |
| nonull | Null in non-nullable column | No | Rows found in table with null values for one or more non-nullable columns in the source table |
| nonullsubtype | Null in non-nullable column for subtype | No | Rows found in table with null values for one or more non-nullable columns for the subtype in the source table |
| typekey | Invalid typekey | No | Rows found in table with invalid values for a typekey column |
| foreignkey | Invalid foreign key | No | Rows found in table with invalid values for a foreign key column |
| foreignkeynonadmin | Invalid foreign key to non-admin row | No | Rows found in table with foreign key references to existing row in a non-admin table when only existing rows in admin tables can be referenced |
| foreignkeysub | Foreign references incorrect subtype | No | Rows found in table with foreign key references to incorrect subtype |
| zerolengthstring | 0-length varchar | No | Rows found in table with 0-length strings in varchar columns |
| ppeerror | PostPopulateExecutor failure | No | PostPopulateExecutors failures detected after populating source tables |
| reftoexistingrow | Illegal reference to existing row | No | Rows found in table with foreign key references to an existing row in a source table when such references are not allowed |
| typekeyinset | Verify typekey in set | No | Rows found in table include typekey values that are invalid when loading via the staging tables |
| typekeynotinset | Verify typekey not in set | No | Rows found in table include typekey values that are invalid when loading via the staging tables |
| nomatchlvquery | Verify query returns 0 rows | No | Rows found in staging table by query that should return 0 rows |
| badassignable | Invalid assignable | No | Rows found in staging table that violate rules for assignable objects |
| reftoexistingreffedrow | Illegal reference to already referenced existing row | No | Rows found in table with foreign key references to an existing row in a source table that is already referenced from other existing rows, when such references are not allowed |
| onetoone | Non-nullable one-to-one | No | Not exactly one row found in table for non-nullable one-to-one relationships |
| nullableonetoone | Nullable one-to-one | No | More than one row found in table for nullable one-to-one relationships |
| edgeforeignkey | Non-nullable edge foreign key | No | Not exactly one row found in table for non-nullable edge foreign key relationships |
| monetaryamount | MonetaryAmount inconsistent | No | One or the other of the amount and currency column for a monetary amount contains null when the other does not. |

---

### Typelist: LoadFactorType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\LoadFactorType.tti`
**Description:** Type of load factor privileges a user has
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| loadfactorview | View | No | User can view the load factor levels of other users in the group |
| loadfactoradmin | Admin | No | User can view and modify the load factor levels of other users in the group |

---

### Typelist: LoadStepType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\LoadStepType.tti`
**Description:** Types of load step events
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| errorcleared | Error table cleared | No | Error table cleared |
| exclusioncleared | Exclusion table cleared | No | Exclusion table cleared |
| stagingcleared | Staging tables cleared | No | Staging tables cleared |
| excludeddeleted | Excluded rows deleted | No | Excluded rows deleted from staging tables |
| exclusionpop | Exclusion table populated | No | Exclusion table populated with failed rows from error table |
| integritychecked | Integrity of staging tables checked | No | Integrity of staging tables checked (Entire phase) |
| idsgenerated | IDs generated for staging tables | No | IDs generated for staging tables |
| rownumsgenerated | Row numbers generated for staging tables | No | Row numbers generated for staging tables |
| sourceloaded | Source tables loaded | No | Source tables loaded from staging tables (Entire phase) |
| nonexcludeddeleted | Non-excluded rows deleted | No | Non-excluded rows deleted from staging tables |
| ppesexecuted | PostPopulatorExecutors executed | No | PostPopulatorExecutors executed after populating staging tables |
| consistencychecked | ConsistencyChecker executed | No | Custom consistency checks executed after populating staging tables |
| integrityexecuted | Integrity check queries executed | No | Integrity check queries checks executed |
| insertselects | INSERT SELECTs executed | No | INSERT SELECTs from staging to source tables executed |
| estimatedbstatistics | DB statistics updated with estimates for source tables | No | DB statistics updated with estimates for source tables |
| lcbeforeidgeneration | LoaderCallback before id generation | No | LoaderCallbacks executed before id generation |
| lcbeforeinsertselect | LoaderCallback before execution of insert/selects | No | LoaderCallbacks executed before insert/selects into source tables |
| lcafterinsertselect | LoaderCallback after execution of insert/selects | No | LoaderCallbacks executed after insert/selects into source tables |
| overwrittencleared | Overwritten staging tables and columns cleared | No | Overwritten staging tables and columns cleared |

---

### Typelist: LocaleType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\LocaleType.tti`
**Description:** Users' preferred languages
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| en_US | United States (English) | No | United States (English) |
| en_GB | Great Britain (English) | No | Great Britain (English) |
| en_CA | Canada (English) | No | Canada (English) |
| en_AU | Australia (English) | No | Australia (English) |
| fr_CA | Canada (French) | No | Canada (French) |
| fr_FR | France (French) | No | France (French) |
| de_DE | Germany (German) | No | Germany (German) |
| ja_JP | Japan (Japanese) | No | Japan (Japanese) |

---

### Typelist: LookupColumnDataType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\LookupColumnDataType.tti`
**Description:** Lookup Table Data types
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| String | String | No | String Data Type |
| Integer | Integer | No | Integer data type |
| Decimal | Decimal | No | Decimal data type |
| Boolean | Boolean | No | Boolean (bit) data type |
| Date | Date | No | Date data type |

---

### Typelist: LossCause

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\LossCause.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\LossCause.ttx`
**Description:** Causes of loss
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Basic | Basic | No | Basic |
| Broad | Broad | No | Broad |
| Special | Special | No | Special |
| Earthquake | Earthquake | No | Earthquake |
| NamedPerils | Named perils | No | Named perils |
| AllRisk | All risk | No | All risk |

---

### Typelist: LossEntryCause

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\LossEntryCause.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\LossEntryCause.ttx`
**Description:** Loss history - cause of loss
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Fire | Fire | No | Fire |
| Lightning | Lightning | No | Lightning |
| Explosion | Explosion | No | Explosion |
| WindstormHail | Windstorm or hail | No | Windstorm or Hail |
| Smoke | Smoke | No | Smoke |
| AircraftVehicles | Aircraft or vehicles | No | Aircraft or vehicles |
| RiotCommotion | Riot or civil commotion | No | Riot or civil commotion |
| Vandalism | Vandalism | No | Vandalism |
| SprinklerLeak | Sprinkler leakage | No | Sprinkler leakage |
| SinkholeCollapse | Sinkhole collapse | No | Sinkhole collapse |
| Volcanic | Volcanic action | No | Volcanic action |
| Transportation | Transportation | No | Transportation |
| Other | Other | No | Other |

---

### Typelist: LossEntryStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\LossEntryStatus.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\LossEntryStatus.ttx`
**Description:** Types of loss history
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Open | Open | No | Open |
| Closed | Closed | No | Closed |

---

### Typelist: LossHistoryType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\LossHistoryType.tti`
**Description:** Types of loss history
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| nol | No Loss History | No | No Loss History |
| man | Manually Entered | No | Manually Entered |
| att | Attached | No | Attached |

---

### Typelist: LossPaymentLimits

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\LossPaymentLimits.tti`
**Description:** Extra Expense Loss Payment Limits
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 100_100_100 | 100%-100%-100% | No | 100%-100%-100% |
| 40_80_100 | 40%- 80%-100% | No | 40%- 80%-100% |
| 35_70_100 | 35%-70%-100% | No | 35%-70%-100% |

---

### Typelist: Loyalty

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\Loyalty.tti`
**Description:** Loyalty
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 1year | 1 Year | No | 1 Year |
| 2years | 2 Years | No | 2 Years |
| 3years | 3 Years | No | 3 Years |
| 4years | 4 Years | No | 4 Years |
| 5years_plus | 5 Years Plus | No | 5 Years + |

---

### Typelist: MAEmployerType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\MAEmployerType.tti`
**Description:** What type of employer
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 1 | Private Employer | No | A private employer |
| 2 | Public Employer | No | A public employer |
| 3 | Federal Agency | No | A federal agency (no taxes applicable) |
| N | Not Applicable | No | Not Applicable |

---

### Typelist: ManageWorkflowActionType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ManageWorkflowActionType.tti`
**Description:** Which action was chosen to act on a workflow.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| InvokeTrigger | Invoke Trigger | No | Invoke a trigger on the workflow |
| Suspend | Suspend | No | Suspend the workflow's activity |
| Resume | Resume | No | Resume a suspended workflow |
| SetTimeout | Set Timeout | No | Manually force the timeout for a waiting workflow |
| RetryMessage | Retry Message | No | Retry the last message sent to the workflow |
| Wait | Wait | No | Wait until workflow is no longer active |

---

### Typelist: MaritalStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\MaritalStatus.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\MaritalStatus.ttx`
**Description:** Types of marital status
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| C | Domestic partner | No | Domestic partner |
| D | Divorced | No | Divorced |
| M | Married | No | Married |
| P | Separated | No | Separated |
| S | Single | No | Single |
| U | Unknown | No | Unknown |
| W | Widowed | No | Widowed |

---

### Typelist: MergeConflictResolution

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\MergeConflictResolution.tti`
**Description:** Identifies how a merge conflict was resolved.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| no_conflict | No conflict | No | No merge conflict detected. |
| old_retained | Old value retained | No | The previously existing value (with a later effective date) was retained. |
| new_merged_forward | New value merged forward | No | The new value (with an earlier effective date) was merged forward. |
| user_change | User change post-merge | No | The user manually changed the value after the merge. |

---

### Typelist: MergeConflictStrategy

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\MergeConflictStrategy.tti`
**Description:** Identifies a strategy for resolving merge conflicts.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| retain_old | Retain old future-dated value | No | Strategy that retains the previously existing value with a later effective date. |
| merge_new_forward | Merge new back-dated value forward | No | Strategy that merges the new value with an earlier effective date forward. |

---

### Typelist: MeritRatingCreditType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\MeritRatingCreditType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\MeritRatingCreditType.ttx`
**Description:** Merit Rating Credit
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 33 | 33% | No | 33% |

---

### Typelist: MeritRatingDebitType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\MeritRatingDebitType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\MeritRatingDebitType.ttx`
**Description:** Merit Rating Debit
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 4 | 4% | No | 4% |
| 10 | 10% | No | 10% |

---

### Typelist: MessageDestinationStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\MessageDestinationStatus.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\MessageDestinationStatus.ttx`
**Description:** Message Destination Status
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Retrying | Retrying | No | Retrying |
| Shutdown | Shutdown | No | Shutdown |
| Started | Started | No | Started |
| Suspended | Suspended | No | Suspended |
| Suspending | Suspending | No | Suspending |
| Resuming | Resuming | No | Resuming |
| SuspendedInbound | Suspended Inbound | No | Suspended inbound |
| SuspendedOutbound | Suspended Outbound | No | Suspended outbound |
| Unknown | Unknown | No | Unknown |

---

### Typelist: MessageSearchStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\MessageSearchStatus.tti`
**Description:** Status for searching messages
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| NeedRetry | Messages needing retry | No | Messages that need to be retried. |
| Failed | Failed messages | No | Messages that have failed. |
| Unfinished | Unfinished messages | No | Messages that have not finished. |

---

### Typelist: MiningCoverage

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\MiningCoverage.tti`
**Description:** Mining Coverage Type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| nounderground | No Under Ground | No | No Under Ground |
| ltdunderground | Limited Under Ground | No | Limited Under Ground |
| broadunderground | Broad Under Ground | No | Broad Under Ground |

---

### Typelist: MiscContactType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\MiscContactType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\MiscContactType.ttx`
**Description:** Types of misc Policy Contacts
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| depository | Depository | No | Depository Company |
| publicoffical | Public Official | No | Public Official |
| agent | Agent | No | Agent |
| subcontractor | Sub Contractor | No | Sub Contractor |

---

### Typelist: Modification

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\Modification.tti`
**Description:** Modification to base premium
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| modification | Modification | No | Modification to base premium |
| base | Base | No | Base premium |

---

### Typelist: ModifierDataType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ModifierDataType.tti`
**Description:** Modifier Data Types
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| boolean | boolean | No | Boolean modifier |
| date | date | No | Date modifier |
| rate | rate | No | Rate modifier |
| typekey | typekey | No | Typekey modifier |

---

### Typelist: MoneySecurityType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\MoneySecurityType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\MoneySecurityType.ttx`
**Description:** Location of Money/Security
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| inside | Inside | No | Inside |
| messenger | Messenger | No | Messenger |

---

### Typelist: Months

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\Months.tti`
**Description:** Months
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| january | January | No | January |
| february | February | No | February |
| march | March | No | March |
| april | April | No | April |
| may | May | No | May |
| june | June | No | June |
| july | July | No | July |
| august | August | No | August |
| september | September | No | September |
| october | October | No | October |
| november | November | No | November |
| december | December | No | December |

---

### Typelist: MvrCategory

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\MvrCategory.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\MvrCategory.ttx`
**Description:** Category of a MotorVehicleRecord
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| moving | Moving violation | No | General moving violation, such as a speeding ticket |
| stationary | Stationary violation | No | General stationary violation, such as a parking ticket |
| dui | DUI | No | Citation or conviction for driving under the influence of alcohol or other drugs |

---

### Typelist: MVRIncidentType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\MVRIncidentType.tti`
**Description:** Type of MVR incident
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| ACCI | ACCI | No | Accident |
| CANC | CANC | No | License Canceled |
| CONV | CONV | No | Conviction |
| DEPT | DEPT | No | Departmental Action |
| DISQ | DISQ | No | Disqualification |
| F_R | F/R | No | Financial Responsibility |
| MISC | MISC | No | Miscellaneous |
| PROB | PROB | No | Probation |
| REIN | REIN | No | License reinstated |
| REVO | REVO | No | Revocation |
| SUSP | SUSP | No | License suspended |
| UNCL | UNCL | No | Unclassified |
| VIOL | VIOL | No | Violation |
| WARN | WARN | No | Warning |

---

### Typelist: MvrRecordType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\MvrRecordType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\MvrRecordType.ttx`
**Description:** Type of a MotorVehicleRecord
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| violation | Violation | No | Violation |
| suspension | Suspension | No | Suspension |

---

### Typelist: MVRResponse

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\MVRResponse.tti`
**Description:** Response from the external MVR service provider
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| CLEAR | Clear | No | Match with the Department of Motor Vehicles (DMV) - but with no violations |
| HIT | Hit | No | Match with the Department of Motor Vehicles (DMV) - has violations |
| NOTFOUND | No Hit | No | Did not receive any information. No information in the Department of Motor Vehicles (DMV) database |
| PEND | Pending | No | Awaiting reply from DMV |
| DELAY | Delay | No | Delayed means that the request will take longer that the normal anticipated turnaround time |

---

### Typelist: MVRStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\MVRStatus.tti`
**Description:** MVRStatus
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| ToBeOrdered | To Be Ordered | No | Not Yet Ordered - Internal use only(workflow) |
| Ordered | Ordered | No | Ordered - MVR Result is Pending or Delay |
| Ready | Ready | No | Ready - Internal use only(workflow) |
| Received | Received | No | Received - MVR Result is Clear, Hit, No Hit |

---

### Typelist: NamePrefix

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\NamePrefix.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\NamePrefix.ttx`
**Description:** Name prefixes
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| mr | Mr. | No | Mr. |
| mrs | Mrs. | No | Mrs. |
| ms | Ms. | No | Ms. |
| dr | Dr. | No | Dr. |

---

### Typelist: NameSuffix

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\NameSuffix.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\NameSuffix.ttx`
**Description:** Name suffixes
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| jr | Jr. | No | Jr. |
| sr | Sr. | No | Sr. |
| c_Ir | I | No | I |
| c_II | II | No | II |
| c_III | III | No | III |
| c_IV | IV | No | IV |
| c_md | M.D. | No | M.D. |
| c_phd | PhD. | No | PhD. |
| c_do | D.O. | No | D.O. |

---

### Typelist: NonRenewalCode

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\NonRenewalCode.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\NonRenewalCode.ttx`
**Description:** Non-Renewal Reason Codes
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| loss | Non-Renew - losses | No | Non-Renew - losses |
| producertermination | Non-Renew - producer termination | No | Non-Renew - Producer termination |
| outofbusness | Non-Renew - out of business | No | Non-Renew - out of business |
| payhistory | Non-Renew - payment history | No | Non-Renew - payment history |
| change | Non-Renew - material change | No | Non-Renew - material change |
| reinsurance | Non-Renew - Reinsurance | No | Non-Renew - Reinsurance |
| insuredrequest | Non-Renew - Insured Request | No | Non-Renew - insured request |
| noncompliance | Non-Renew - non-compliance | No | Non-Renew - non-compliance |

---

### Typelist: NoteSecurityType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\NoteSecurityType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\NoteSecurityType.ttx`
**Description:** Type of the note for access-restriction purposes
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| *(None defined)* | *Dynamic or database-driven* | No | Typelist populated dynamically at runtime or via database table |

---

### Typelist: NoteTopicType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\NoteTopicType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\NoteTopicType.ttx`
**Description:** Topic to which this note belongs
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| general | General | No | General |
| risk | Risk characteristics | No | Risk Characteristics |
| coverage | Coverage requests | No | Coverage requests |
| gaps | Coverage gaps | No | coverage Gaps |
| losscontrol | Loss Control | No | Loss control |
| creditworthy | Financial Issues | No | Financial issues |
| meetingsagreements | Meetings/Agreements | No | Meetings/agreements |
| busdevelopment | Business development | No | business Development |
| relationmgt | Relation management | No | Relation Management |
| legal | Legal | No | Legal |
| prerenewal | Pre-renewal direction | No | Pre-renewal direction |
| datadestruction | Data Destruction | No | Data Destruction |

---

### Typelist: NoteType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\NoteType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\NoteType.ttx`
**Description:** Type of note
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| diagram | General | No | General |
| interviewreport | Interview report | No | Interview report |
| actionplan | Action plan | No | Action plan |
| statusreport | Status report | No | Status report |

---

### Typelist: NotificationActionType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\NotificationActionType.tti`
**Description:** Notification configuration action types
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| fraudcancel | Fraud Cancellation | No | Notification requirement in days for fraud cancellation |
| matchange | Material Change Renewal | No | Notification requirement in days for material change renewal |
| nonpaycancel | Non-payment Cancellation | No | Notification requirement in days for non-payment cancellation |
| nonrenew | Non-renewal Renewal | No | Notification requirement in days for non-renewal renewal |
| nonrenewmax | Non-renewal Maximum | No | Non renewal max (in days) |
| nonrenewmin | Non-renewal Minimum | No | Non renewal min (in days) |
| othercancel | Other Cancellation | No | Notification requirement in days for other cancellation |
| otherrenewal | Other Renewal | No | Notification requirement in days for other renewal |
| premincrease | Premium Increase | No | Premium increase notification requirement in days |
| uwothercancel | Other Cancellation in UW Period | No | Other cancel in UW Period |
| uwperiod | Underwriting Period | No | Underwriting period in days |
| cooperation | Failure to cooperate | No | Failure to cooperate |
| hazardincrease | Increase in hazard | No | Increase in hazard |
| rateincrease | Increase in rates | No | Increase in rates |
| license | Driver Lic. Loss/Suspension | No | Driver Lic. Loss/Suspension |
| moralhazard | Moral Hazard | No | Moral Hazard |
| reinsurance | Loss of Reinsurance | No | Loss of Reinsurance |
| uwperiodfraudcancel | Fraud Cancellation in UW Period | No | Fraud Cancellation in UW Period |
| uwperiodhazardincrease | Increase in Hazard in UW Period | No | Increase in Hazard in UW Period |
| uwperiodnonpaycancel | NonPayment in UW Period | No | NonPayment in UW Period |

---

### Typelist: NotificationCategory

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\NotificationCategory.tti`
**Description:** Notification configuration categories
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| cancel | Cancellation | No | Cancellation notification configurations |
| nonrenew | Non-renewal | No | Non-renewal notification configurations |
| renewal | Renewal | No | Renewal notification configurations |
| uwcancel | UW Period Cancellation | No | UW Period Cancellation |

---

### Typelist: NumberOfAccidents

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\NumberOfAccidents.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\NumberOfAccidents.ttx`
**Description:** Number of accidents or violations
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 0 | 0 | No | 0 |
| 1 | 1 | No | 1 |
| 2 | 2 | No | 2 |
| 3 | 3 | No | 3 |
| 4 | 4 | No | 4 |
| 5 | 5 or more | No | 5 or more |

---

### Typelist: OfficialIdRequiredType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\OfficialIdRequiredType.tti`
**Description:** Official Id Required Type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| optional | Optional | No | Optional |
| mandatoryissue | Mandatory at Issue | No | Mandatory at Issue |
| mandatoryaudit | Mandatory at Audit | No | Mandatory at Audit |

---

### Typelist: OfficialIDScope

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\OfficialIDScope.tti`
**Description:** Scope of an OfficialID.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| State | State | No | State |
| InsuredAndState | Insured and State | No | Insured and State |

---

### Typelist: OfficialIDType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\OfficialIDType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\OfficialIDType.ttx`
**Description:** Type of official id (i.e. SSN, FEIN, State Tax, State Unemployment, etc)
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| BureauID | Bureau ID | No | Bureau ID |
| DOLID | Dept of Labor ID | No | Dept of Labor ID |
| DUNS | Dun & Bradstreet Number | No | Dun & Bradstreet Number |
| FEIN | FEIN | No | Federal Employer Identification Number |
| NCCIID | NCCI Interstate ID | No | NCCI Interstate ID |
| SSN | SSN | No | Social Security Number |
| STAX | State Tax ID | No | State Tax Identification Number |
| STUN | State Unemployment ID | No | State Unemployment Identification Number |
| TUNS | Temporary Dun & Bradstreet Number | No | Temporary Dun & Bradstreet Number |
| NCCIintrastate | NCCI Intrastate ID | No | NCCI Intrastate ID |

---

### Typelist: OrganizationType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\OrganizationType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\OrganizationType.ttx`
**Description:** Type of organization for attorneys, doctors, and government authorities
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| individual | Individual/Sole Proprietorship | No | Individual/Sole Proprietorship |
| partnership | Partnership | No | Partnership |
| corporation | Corporation | No | Corporation |
| association | Association, Labor Union, Religious Organization | No | Association, Labor Union, Religious Organization |
| llc | LLC | No | LLC |
| jointventure | Joint Venture | No | Joint Venture |
| commonownership | Common Ownership | No | Common Ownership |
| limitedpartnership | Limited Partnership | No | Limited Partnership |
| trustestate | Trust or Estate | No | Trust or Estate |
| executortrustee | Executor or Trustee | No | Executor or Trustee |
| llp | LLP | No | LLP |
| government | Government Entity | No | Government Entity |
| nonprofit | NonProfit Corp. | No | NonProfit Corp |
| jointemployers | Joint Employers | No | Joint Employers |
| multiple | Multiple statuses | No | Multiple statuses |
| other | Other | No | Other |

---

### Typelist: OtherStates

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\OtherStates.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\OtherStates.ttx`
**Description:** Other States
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| None | None | No | No other states |
| AllOther | All other non-monopolistic states | No | All other non-monopolistic states |
| ListedOnly | Listed states only | No | Listed states only |
| AllExcept | All states except | No | All states except |

---

### Typelist: OutboundRecordStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\OutboundRecordStatus.tti`
**Description:** The status for an Outbound Record.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| pending | Pending | No | The outbound record is ready to be delivered. |
| processed | Processed | No | The Outbound Record has been processed and included in an Outbound File. |
| error | Error | No | The Outbound Record resulted in an error when processed. |
| skipped | Skipped | No | The Outbound Record has been skipped and is awaiting purge. |

---

### Typelist: OverrideSourceCategory

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\OverrideSourceCategory.tti`
**Description:** Category for override sources, e.g. user or automated process
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| user | User | No | User input |
| auto | Auto | No | Automatic process |

---

### Typelist: OverrideSourceType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\OverrideSourceType.tti`
**Description:** Source for the override value (for example, manual input, or automatic renewal cap)
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| manual | Manual | No | Manual input from Override dialog |
| renewalcap | Renewal cap | No | Computed by renewal capping algorithm |

---

### Typelist: PackageRisk

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\PackageRisk.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\PackageRisk.ttx`
**Description:** Package Risk Type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| office | Office | No | Office |
| mercantile | Mercantile | No | Mercantile |
| motelhotel | Motel/Hotel | No | Motel/Hotel |
| apartment | Apartment | No | Apartment |
| institutional | Institutional | No | Institutional |
| services | Services | No | Services |
| industrial | Industrial/Processing | No | Industrial/Processing |
| contractor | Contractor | No | Contractor |

---

### Typelist: PAMultiPolicyDiscount

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\PAMultiPolicyDiscount.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\PAMultiPolicyDiscount.ttx`
**Description:** Personal Auto multi-policy discounts
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| none | None | No | None |
| 2policy | 2 policy discount (10%) | No | Two policy discount (10%) |
| 3policy | 3 policy discount (15%) | No | Three policy discount (15%) |

---

### Typelist: PAPIPCovCostType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\PAPIPCovCostType.tti`
**Description:** The type of PIP coverage where the cost applies.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| basic | Basic | No | Basic |
| optional | Optional | No | Optional |
| income | Wage Loss | No | Wage Loss |
| medical | Medical | No | Medical |
| rehab | Rehab | No | Rehab |
| services | Services | No | Services |
| managedcare | Managed Care | No | Managed Care |
| death | Death | No | Death |
| funeral | Funeral | No | Funeral |
| guest | Guest | No | Guest |

---

### Typelist: ParameterType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ParameterType.tti`
**Description:** Value type of a system or component parameter
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| String | String | No | String (default) |
| Integer | Integer | No | Integer |
| Boolean | Boolean | No | Boolean |
| Datetime | Datetime | No | Date/Time |
| LongText | LongText | No | String (clob) |

---

### Typelist: Parentheses

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\Parentheses.tti`
**Description:** Parentheses
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| OneLeft | ( | No | ( |
| TwoLeft | (( | No | (( |
| ThreeLeft | ((( | No | ((( |
| FourLeft | (((( | No | (((( |
| OneRight | ) | No | ) |
| TwoRight | )) | No | )) |
| ThreeRight | ))) | No | ))) |
| FourRight | )))) | No | )))) |

---

### Typelist: PassiveRestraintType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\PassiveRestraintType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\PassiveRestraintType.ttx`
**Description:** Auto Passive restraint type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| no | No | No | No |
| driver | Driver Side | No | Driver Side Only |
| both | Both Sides | No | Both Sides |

---

### Typelist: PayableBasisType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\PayableBasisType.tti`
**Description:** Defines the types of payable basis for reinsurance agreement.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| AsWritten | As Written | No | The ceded premiums and commissions are reported and considered payable as the written premium is recognized. |
| AsEarned | As Earned | No | They are considered payable as the underlying premium is earned. |

---

### Typelist: PaymentMethod

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\PaymentMethod.tti`
**Description:** Payment Method
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Installments | Payment Plan | No | Payment Plan |
| ReportingPlan | Reporting Plan | No | Reporting plan |

---

### Typelist: PaymentTransactionType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\PaymentTransactionType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\PaymentTransactionType.ttx`
**Description:** Payment Gateway Transaction Type
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| AUTHORIZE | Authorization | No | Authorization |
| SALE | Sale | No | Sale |
| INQUIRY | Inquiry | No | Inquiry |
| DELAYED_PAYMENT | Delayed Payment | No | Delayed Payment |
| CREDIT | Credit | No | Credit |
| DATA_UPLOAD | Data Upload | No | Data Upload |

---

### Typelist: PaymentType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\PaymentType.tti`
**Description:** The payment type used for billing
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Installment | Installment | No | Installment payment type |
| PremiumReporting | Premium Reporting | No | Premium Reporting payment type |

---

### Typelist: PayPeriodType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\PayPeriodType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\PayPeriodType.ttx`
**Description:** Pay period type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| daily | Daily | No | Employee paid on a daily basis |
| weekly | Weekly | No | Employee paid on a weekly basis |
| everytwoweeks | Every two weeks | No | Employee paid every two weeks |
| twiceamonth | Twice a Month | No | Employee paid twice a month |
| monthly | Monthly | No | Employee paid on a monthly basis |

---

### Typelist: PercentByTens

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\PercentByTens.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\PercentByTens.ttx`
**Description:** Percentage values from 0 to 100 by tens
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 100 | 100% | No | 100% |
| 90 | 90% | No | 90% |
| 80 | 80% | No | 80% |
| 70 | 70% | No | 70% |
| 60 | 60% | No | 60% |
| 50 | 50% | No | 50% |
| 40 | 40% | No | 40% |
| 30 | 30% | No | 30% |
| 20 | 20% | No | 20% |
| 10 | 10% | No | 10% |
| 0 | 0% | No | 0% |

---

### Typelist: PercentDuplicated

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\PercentDuplicated.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\PercentDuplicated.ttx`
**Description:** PercentDuplicated
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 90plus | at least 90% | No | at least 90% |
| 51plus | at least 51% | No | at least 51% |
| 50minus | 50% or less | No | 50% or less |

---

### Typelist: PercentOccupied

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\PercentOccupied.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\PercentOccupied.ttx`
**Description:** Percentage of building occupied
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 100 | 100% | No | 100% |
| 90 | 90% | No | 90% |
| 80 | 80% | No | 80% |
| 70 | 70% | No | 70% |
| 60 | 60% | No | 60% |
| 50 | 50% | No | 50% |
| 40 | 40% | No | 40% |
| 30 | 30% | No | 30% |
| 20 | 20% | No | 20% |
| 10 | 10% | No | 10% |
| 0 | 0% | No | 0% |

---

### Typelist: PersonalDataTagValue

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\PersonalDataTagValue.tti`
**Description:** Valid tag values for a PersonalData tag
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| ObfuscateDefault | ObfuscateDefault | No | default obfuscation for personal data |
| ObfuscateUnique | ObfuscateUnique | No | unique obfuscation for personal data |

---

### Typelist: PersonOrg

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\PersonOrg.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\PersonOrg.ttx`
**Description:** Person or Organization?
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| per | Person | No | A person |
| org | Organization | No | An organization |

---

### Typelist: PhoneCountryCode

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\PhoneCountryCode.tti`
**Description:** List of regions and their regional phone codes
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| AC | Ascension Island (247) | No | 247 |
| AD | Andorra (376) | No | 376 |
| AE | United Arab Emirates (971) | No | 971 |
| AF | Afghanistan (93) | No | 93 |
| AG | Antigua and Barbuda (1) | No | 1 |
| AI | Anguilla (1) | No | 1 |
| AL | Albania (355) | No | 355 |
| AM | Armenia (374) | No | 374 |
| AN | Netherlands Antilles (599) | No | 599 |
| AO | Angola (244) | No | 244 |
| AR | Argentina (54) | No | 54 |
| AS | American Samoa (1) | No | 1 |
| AT | Austria (43) | No | 43 |
| AU | Australia (61) | No | 61 |
| AW | Aruba (297) | No | 297 |
| AX | Ã…land Islands (358) | No | 358 |
| AZ | Azerbaijan (994) | No | 994 |
| BA | Bosnia and Herzegovina (387) | No | 387 |
| BB | Barbados (1) | No | 1 |
| BD | Bangladesh (880) | No | 880 |
| BE | Belgium (32) | No | 32 |
| BF | Burkina Faso (226) | No | 226 |
| BG | Bulgaria (359) | No | 359 |
| BH | Bahrain (973) | No | 973 |
| BI | Burundi (257) | No | 257 |
| BJ | Benin (229) | No | 229 |
| BL | Saint Barthélemy (590) | No | 590 |
| BM | Bermuda (1) | No | 1 |
| BN | Brunei (673) | No | 673 |
| BO | Bolivia (591) | No | 591 |
| BQ | BQ (599) | No | 599 |
| BR | Brazil (55) | No | 55 |
| BS | Bahamas (1) | No | 1 |
| BT | Bhutan (975) | No | 975 |
| BW | Botswana (267) | No | 267 |
| BY | Belarus (375) | No | 375 |
| BZ | Belize (501) | No | 501 |
| CA | Canada (1) | No | 1 |
| CC | Cocos [Keeling] Islands (61) | No | 61 |
| CD | Congo - Kinshasa (243) | No | 243 |
| CF | Central African Republic (236) | No | 236 |
| CG | Congo - Brazzaville (242) | No | 242 |
| CH | Switzerland (41) | No | 41 |
| CI | Ivory Coast (225) | No | 225 |
| CK | Cook Islands (682) | No | 682 |
| CL | Chile (56) | No | 56 |
| CM | Cameroon (237) | No | 237 |
| CN | China (86) | No | 86 |
| CO | Colombia (57) | No | 57 |
| CR | Costa Rica (506) | No | 506 |
| CU | Cuba (53) | No | 53 |
| CV | Cape Verde (238) | No | 238 |
| CW | Curaçao (599) | No | 599 |
| CX | Christmas Island (61) | No | 61 |
| CY | Cyprus (357) | No | 357 |
| CZ | Czech Republic (420) | No | 420 |
| DE | Germany (49) | No | 49 |
| DJ | Djibouti (253) | No | 253 |
| DK | Denmark (45) | No | 45 |
| DM | Dominica (1) | No | 1 |
| DO | Dominican Republic (1) | No | 1 |
| DZ | Algeria (213) | No | 213 |
| EC | Ecuador (593) | No | 593 |
| EE | Estonia (372) | No | 372 |
| EG | Egypt (20) | No | 20 |
| ER | Eritrea (291) | No | 291 |
| ES | Spain (34) | No | 34 |
| ET | Ethiopia (251) | No | 251 |
| FI | Finland (358) | No | 358 |
| FJ | Fiji (679) | No | 679 |
| FK | Falkland Islands (500) | No | 500 |
| FM | Micronesia (691) | No | 691 |
| FO | Faroe Islands (298) | No | 298 |
| FR | France (33) | No | 33 |
| GA | Gabon (241) | No | 241 |
| GB | United Kingdom (44) | No | 44 |
| GD | Grenada (1) | No | 1 |
| GE | Georgia (995) | No | 995 |
| GF | French Guiana (594) | No | 594 |
| GG | Guernsey (44) | No | 44 |
| GH | Ghana (233) | No | 233 |
| GI | Gibraltar (350) | No | 350 |
| GL | Greenland (299) | No | 299 |
| GM | Gambia (220) | No | 220 |
| GN | Guinea (224) | No | 224 |
| GP | Guadeloupe (590) | No | 590 |
| GQ | Equatorial Guinea (240) | No | 240 |
| GR | Greece (30) | No | 30 |
| GT | Guatemala (502) | No | 502 |
| GU | Guam (1) | No | 1 |
| GW | Guinea-Bissau (245) | No | 245 |
| GY | Guyana (592) | No | 592 |
| HK | Hong Kong SAR China (852) | No | 852 |
| HN | Honduras (504) | No | 504 |
| HR | Croatia (385) | No | 385 |
| HT | Haiti (509) | No | 509 |
| HU | Hungary (36) | No | 36 |
| ID | Indonesia (62) | No | 62 |
| IE | Ireland (353) | No | 353 |
| IL | Israel (972) | No | 972 |
| IM | Isle of Man (44) | No | 44 |
| IN | India (91) | No | 91 |
| IO | British Indian Ocean Territory (246) | No | 246 |
| IQ | Iraq (964) | No | 964 |
| IR | Iran (98) | No | 98 |
| IS | Iceland (354) | No | 354 |
| IT | Italy (39) | No | 39 |
| JE | Jersey (44) | No | 44 |
| JM | Jamaica (1) | No | 1 |
| JO | Jordan (962) | No | 962 |
| JP | Japan (81) | No | 81 |
| KE | Kenya (254) | No | 254 |
| KG | Kyrgyzstan (996) | No | 996 |
| KH | Cambodia (855) | No | 855 |
| KI | Kiribati (686) | No | 686 |
| KM | Comoros (269) | No | 269 |
| KN | Saint Kitts and Nevis (1) | No | 1 |
| KP | North Korea (850) | No | 850 |
| KR | South Korea (82) | No | 82 |
| KW | Kuwait (965) | No | 965 |
| KY | Cayman Islands (1) | No | 1 |
| KZ | Kazakhstan (7) | No | 7 |
| LA | Laos (856) | No | 856 |
| LB | Lebanon (961) | No | 961 |
| LC | Saint Lucia (1) | No | 1 |
| LI | Liechtenstein (423) | No | 423 |
| LK | Sri Lanka (94) | No | 94 |
| LR | Liberia (231) | No | 231 |
| LS | Lesotho (266) | No | 266 |
| LT | Lithuania (370) | No | 370 |
| LU | Luxembourg (352) | No | 352 |
| LV | Latvia (371) | No | 371 |
| LY | Libya (218) | No | 218 |
| MA | Morocco (212) | No | 212 |
| MC | Monaco (377) | No | 377 |
| MD | Moldova (373) | No | 373 |
| ME | Montenegro (382) | No | 382 |
| MF | Saint Martin (590) | No | 590 |
| MG | Madagascar (261) | No | 261 |
| MH | Marshall Islands (692) | No | 692 |
| MK | Macedonia (389) | No | 389 |
| ML | Mali (223) | No | 223 |
| MM | Myanmar [Burma] (95) | No | 95 |
| MN | Mongolia (976) | No | 976 |
| MO | Macau SAR China (853) | No | 853 |
| MP | Northern Mariana Islands (1) | No | 1 |
| MQ | Martinique (596) | No | 596 |
| MR | Mauritania (222) | No | 222 |
| MS | Montserrat (1) | No | 1 |
| MT | Malta (356) | No | 356 |
| MU | Mauritius (230) | No | 230 |
| MV | Maldives (960) | No | 960 |
| MW | Malawi (265) | No | 265 |
| MX | Mexico (52) | No | 52 |
| MY | Malaysia (60) | No | 60 |
| MZ | Mozambique (258) | No | 258 |
| NA | Namibia (264) | No | 264 |
| NC | New Caledonia (687) | No | 687 |
| NE | Niger (227) | No | 227 |
| NF | Norfolk Island (672) | No | 672 |
| NG | Nigeria (234) | No | 234 |
| NI | Nicaragua (505) | No | 505 |
| NL | Netherlands (31) | No | 31 |
| NO | Norway (47) | No | 47 |
| NP | Nepal (977) | No | 977 |
| NR | Nauru (674) | No | 674 |
| NU | Niue (683) | No | 683 |
| NZ | New Zealand (64) | No | 64 |
| OM | Oman (968) | No | 968 |
| PA | Panama (507) | No | 507 |
| PE | Peru (51) | No | 51 |
| PF | French Polynesia (689) | No | 689 |
| PG | Papua New Guinea (675) | No | 675 |
| PH | Philippines (63) | No | 63 |
| PK | Pakistan (92) | No | 92 |
| PL | Poland (48) | No | 48 |
| PM | Saint Pierre and Miquelon (508) | No | 508 |
| PR | Puerto Rico (1) | No | 1 |
| PS | Palestinian Territories (970) | No | 970 |
| PT | Portugal (351) | No | 351 |
| PW | Palau (680) | No | 680 |
| PY | Paraguay (595) | No | 595 |
| QA | Qatar (974) | No | 974 |
| RE | Réunion (262) | No | 262 |
| RO | Romania (40) | No | 40 |
| RS | Serbia (381) | No | 381 |
| RU | Russia (7) | No | 7 |
| RW | Rwanda (250) | No | 250 |
| SA | Saudi Arabia (966) | No | 966 |
| SB | Solomon Islands (677) | No | 677 |
| SC | Seychelles (248) | No | 248 |
| SD | Sudan (249) | No | 249 |
| SE | Sweden (46) | No | 46 |
| SG | Singapore (65) | No | 65 |
| SH | Saint Helena (290) | No | 290 |
| SI | Slovenia (386) | No | 386 |
| SJ | Svalbard and Jan Mayen (47) | No | 47 |
| SK | Slovakia (421) | No | 421 |
| SL | Sierra Leone (232) | No | 232 |
| SM | San Marino (378) | No | 378 |
| SN | Senegal (221) | No | 221 |
| SO | Somalia (252) | No | 252 |
| SR | Suriname (597) | No | 597 |
| SS | SS (211) | No | 211 |
| ST | São Tomé and Príncipe (239) | No | 239 |
| SV | El Salvador (503) | No | 503 |
| SX | Sint Maarten (1) | No | 1 |
| SY | Syria (963) | No | 963 |
| SZ | Swaziland (268) | No | 268 |
| TC | Turks and Caicos Islands (1) | No | 1 |
| TD | Chad (235) | No | 235 |
| TG | Togo (228) | No | 228 |
| TH | Thailand (66) | No | 66 |
| TJ | Tajikistan (992) | No | 992 |
| TK | Tokelau (690) | No | 690 |
| TL | Timor-Leste (670) | No | 670 |
| TM | Turkmenistan (993) | No | 993 |
| TN | Tunisia (216) | No | 216 |
| TO | Tonga (676) | No | 676 |
| TR | Turkey (90) | No | 90 |
| TT | Trinidad and Tobago (1) | No | 1 |
| TV | Tuvalu (688) | No | 688 |
| TW | Taiwan (886) | No | 886 |
| TZ | Tanzania (255) | No | 255 |
| UA | Ukraine (380) | No | 380 |
| UG | Uganda (256) | No | 256 |
| US | United States (1) | No | 1 |
| UY | Uruguay (598) | No | 598 |
| UZ | Uzbekistan (998) | No | 998 |
| VA | Vatican City (379) | No | 379 |
| VC | Saint Vincent and the Grenadines (1) | No | 1 |
| VE | Venezuela (58) | No | 58 |
| VG | British Virgin Islands (1) | No | 1 |
| VI | U.S. Virgin Islands (1) | No | 1 |
| VN | Vietnam (84) | No | 84 |
| VU | Vanuatu (678) | No | 678 |
| WF | Wallis and Futuna (681) | No | 681 |
| WS | Samoa (685) | No | 685 |
| YE | Yemen (967) | No | 967 |
| YT | Mayotte (262) | No | 262 |
| ZA | South Africa (27) | No | 27 |
| ZM | Zambia (260) | No | 260 |
| ZW | Zimbabwe (263) | No | 263 |
| ZZ | Unknown | No | 0 |
| UNPARSEABLE | Unparseable | No | Unparseable Phone Numbers |

---

### Typelist: PhoneType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\PhoneType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\PhoneType.ttx`
**Description:** List of regions and their regional phone codes
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Work | Work | No | Work |
| Fax | Fax | No | Fax |
| Home | Home | No | Home |
| Cell | Mobile | No | Mobile |
| Generic | Phone | No | Generic Type for a Phone |

---

### Typelist: PipCovered

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\PipCovered.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\PipCovered.ttx`
**Description:** Indicate how PIP should be rated
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 0 | PP operated by employees | No | PP operated by employees |
| 1 | PP not principlly operated by employees | No | PP not principlly operated by employees |
| 2 | Truck where operator is covered by WC | No | Truck where operator is covered by WC |

---

### Typelist: PlumbingType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\PlumbingType.tti`
**Description:** Plumbing Type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| copper | Copper | No | Copper |
| galv | Galvanized | No | Galvanized |
| pvc | PVC | No | PVC |
| other | Other | No | Other |

---

### Typelist: PolicyPeriodCloneStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\PolicyPeriodCloneStatus.tti`
**Description:** TemporaryCloneStatus
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Unprocessed | Unprocessed | No | Policy Period is freshly cloned, and nothing has been done to it. |
| Purgeable | Purgeable | No | This cloned policy period has been processed and is now ready to be purged |

---

### Typelist: PolicyPeriodStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\PolicyPeriodStatus.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\PolicyPeriodStatus.ttx`
**Description:** All available types of policies
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| New | New | No | Policy is brand new. Submission, Issuance and Renewal jobs initially set this status |
| Draft | Draft | No | Policy is editable. Audit, Cancellation, PolicyChange, Reinstatement, Rewrite and RewriteNewAccount jobs initially set this status |
| Quoted | Quoted | No | Policy has been quoted. Quote process sets this status when complete |
| Quoting | Quoting | No | Policy is in the process of being quoted. Quote process initially sets this status |
| Bound | Bound | No | Policy has been bound. Cancellation, Issuance, Reinstatement, Rewrite, RewriteNewAccount, Submission and PolicyChange jobs set this status |
| Withdrawn | Withdrawn | No | Policy has been withdrawn by agent or insured |
| Declined | Declined | No | Policy has been declined by carrier |
| Expired | Expired | No | Policy has timed out. Job expiration work queue sets this status |
| NonRenewed | Non-renewed | No | Policy has been Non-Renewed |
| NotTaken | Not-taken | No | Policy was not-taken |
| Temporary | Temporary | No | Policy is in the process of being created |
| LegacyConversion | LegacyConversion | No | Policy is a Legacy SOR that is created for renewal conversion. |
| RateRequested | Rate Requested | No | Policy has been queued to rate asynchronously. Quote process sets this status when asynchronous rating is chosen |
| QuoteRequested | Quote Requested | No | Policy has been queued to quote asynchronously. Quote process sets this status when asynchronous quoting is chosen |
| Rated | Rated | No | Policy has been rated. Quote process sets this status when rating is complete |
| Binding | Binding | No | Policy binding is in progress |
| Renewing | Renewing | No | Renewal for policy is being scheduled |
| NonRenewing | Non-renewing | No | Non-renewal for policy is being scheduled |
| NotTaking | Not-taking | No | Policy is being processed for being not-taken |
| Canceling | Canceling | No | Policy is being scheduled for cancellation |
| Rescinding | Rescinding | No | Cancellation rescinding process started |
| Rescinded | Rescinded | No | Cancellation has been rescinded |
| Reinstating | Reinstating | No | Reinstatement process has started |
| AuditComplete | Completed | No | Audit is completed |
| Waived | Waived | No | Audit was waived |

---

### Typelist: PolicyTermArchiveState

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\PolicyTermArchiveState.tti`
**Description:** Combined archive state of the PolicyPeriods in the PolicyTerm.
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| NotArchived | NotArchived | No | No PolicyPeriods in the PolicyTerm are archived |
| PartiallyArchived | PartiallyArchived | No | Some but not all PolicyPeriods in the PolicyTerm are archived |
| FullyArchived | FullyArchived | No | All PolicyPeriods in the PolicyTerm are archived |

---

### Typelist: PreRenewalDirection

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\PreRenewalDirection.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\PreRenewalDirection.ttx`
**Description:** Pre-renewal direction
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| underwriter | Refer to Underwriter | No | Refer to Underwriter |
| assistant | Refer to Underwriter Assistant | No | Refer to Underwriter Assistant |
| custrep | Refer to Customer Service Representative | No | Refer to Customer Service Representative |
| nonrenewrefer | Non-Renew and Refer to Underwriter | No | Non-Renew and Refer to Underwriter |
| nonrenew | Non-Renew | No | Non-Renew |
| nottaken | Not-Taken | No | Not-Taken |

---

### Typelist: PrimaryColor

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\PrimaryColor.tti`
**Description:** Primary Colors
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| ff0000 | Red | No | Red |
| 00ff00 | Green | No | Green |
| 0000ff | Blue | No | Blue |

---

### Typelist: PrimaryCoverage

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\PrimaryCoverage.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\PrimaryCoverage.ttx`
**Description:** Whether coverage is primary or secondary
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Primary | Primary | No | Primary |
| Secondary | Secondary | No | Secondary |

---

### Typelist: PrimaryPhoneType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\PrimaryPhoneType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\PrimaryPhoneType.ttx`
**Description:** Types of phone numbers
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| home | Home | No | Home |
| work | Work | No | Work |
| mobile | Mobile | No | Mobile |

---

### Typelist: PrintFormat

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\PrintFormat.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\PrintFormat.ttx`
**Description:** Different print views; corresponds to the report or template used to create the printable document
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| policy-default | Default policy view | No | Default printable view of a policy |

---

### Typelist: Priority

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\Priority.tti`
**Description:** Basic priority typelist
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| urgent | Urgent | No | Highest priority - must be addressed immediately |
| high | High | No | High priority - should be addressed before normal activities |
| normal | Normal | No | Normal |
| low | Low | No | Low - needs to be addressed eventually but there is no urgency |

---

### Typelist: ProducerStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ProducerStatus.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\ProducerStatus.ttx`
**Description:** Status of external producer organization
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Active | Active | No | Normal privileges |
| Limited | Limited | No | Reduced permissions, can still renew. |
| Suspended | Suspended | No | Reduced permissions, can no longer renew. |
| Terminating | Terminating | No | The producer is going away. |
| Terminated | Terminated | No | The producer relationship is stopped and the producer is no longer granted access to the system. |

---

### Typelist: ProducerStatusUse

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ProducerStatusUse.tti`
**Description:** Defines how this ProducerStatus can be used.
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| submissionOkay | Submissions | No | This ProducerStatus can be used for Submissions. |
| renewalOkay | Renewals | No | This ProducerStatus can be used for Renewals. |
| okay | All usages | No | This ProducerStatus can be used for all Jobs. |

---

### Typelist: ProductAccountType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ProductAccountType.tti`
**Description:** Product is for Person, Company, or Any type of account
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Person | Person | No | Product is available for Person type account. |
| Company | Company | No | Product is available for Company type account. |
| Any | Any | No | Product is available for Any type account. |

---

### Typelist: ProductMode

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ProductMode.tti`
**Description:** The mode in which jobs run to support product development - Product Generator
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| hide | Hidden | No | Product design not available |
| use | User | No | The manual products run as close to "real" as possible |
| design | Designer | No | Product design data can be captured whilst running the system |
| develop | Developer | No | Develop and generate the products |

---

### Typelist: ProductSelectionReason

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ProductSelectionReason.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\ProductSelectionReason.ttx`
**Description:** Reason for making a product offer (filtered by ProductSelectionStatus)
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| NotOffered | NotOffered | No | Product not offered |
| LossHistory | Loss history | No | Loss history |
| PaymentHistory | Payment history | No | Payment history |

---

### Typelist: ProductSelectionStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ProductSelectionStatus.tti`
**Description:** Status of a product offered through the Submission Manager
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Available | Available | No | Product is available for submission. |
| Unavailable | Unavailable | No | Product is unavailable for unstated reason. |
| RiskReserved | Risk reserved | No | Product is reserved by someone else. |
| AutoDeclined | (Auto) Declined | No | Product is not available. |
| NotApplicable | Not Applicable | No | Product is not applicable to the Account. |

---

### Typelist: ProductType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ProductType.tti`
**Description:** The type of a Product: Can be either Commercial or Personal
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Commercial | Commercial | No | A commercial product |
| Personal | Personal | No | A personal product |

---

### Typelist: ProductWorkDateType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ProductWorkDateType.tti`
**Description:** ProductWorkDateType
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| sale | sale | No | sale |
| distribution | distribution | No | distribution |
| disposal | disposal | No | disposal |
| completion | completion | No | completion |
| manufacture | manufacture | No | manufacture |

---

### Typelist: ProfessionalDiscount

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ProfessionalDiscount.tti`
**Description:** Professional Discount
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Astronomers_Astrophysicists | Astronomers/Astrophysicists | No | Astronomers/Astrophysicists |
| Educators | Educators | No | Educators - Elementary through High School |
| FirstResponders | First Responders | No | First Responders |
| HealthCareProfessionals | Health Care Professionals | No | Health Care Professionals |
| Librarians | Librarians | No | Librarians |
| MaritimeCrew | Maritime Crew | No | Maritime Crew |
| RailRoadTrainCrew | RailRoad Train Crew | No | RailRoad Train Crew |
| SoftwareProfessionals | Software Professionals | No | Software Professionals |

---

### Typelist: ProrationMethod

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ProrationMethod.tti`
**Description:** The method used to compute a final amount from the term amount.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| ProRataByDays | Day-based pro rata amount | No | Pro-rata based on fraction of term |
| Flat | Flat | No | Flat amount (all of term amount) |

---

### Typelist: ProximitySearchStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ProximitySearchStatus.tti`
**Description:** Categorize the geocode status of an address
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| failed | Failed | No | This category includes the following geocode status: failure |
| notyetsearchable | Not Yet Searchable | No | This category includes the following geocode status: none |
| searchable | Searchable | No | This category includes the following geocode status: exact, street, city, postalcode |

---

### Typelist: PurgeStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\PurgeStatus.tti`
**Description:** PurgeStatus
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Unknown | Unknown | No | Either the job has not yet been evaluated, or the job has been evaluated and it does not satisfy the Pruned status nor the NoActionRequired status. |
| NoActionRequired | No Action Requried | No | The job will never need to be considered for purging again because the job's only PolicyPeriod is promoted. |
| Pruned | Pruned | No | The job is already in a pruned state, either because the unselected PolicyPeriods have been purged, or because there never were any unselected PolicyPeriods. |

---

### Typelist: PurgeType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\PurgeType.tti`
**Description:** Not specified in source
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Unknown | Unknown | No | Unknown |

---

### Typelist: QuestionFormat

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\QuestionFormat.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\QuestionFormat.ttx`
**Description:** How the question should be rendered in PCF
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| BooleanCheckbox | Boolean Checkbox | No | A boolean yes/no checkbox.  Default for Boolean questions. |
| DateField | Date Field | No | A Date picker.  Default for Date questions. |
| IntegerField | Integer Field | No | A simple integer field.  Default for Integer questions. |
| StringField | String Field | No | A simple 1-line text field.  Default for String questions. |
| ChoiceSelect | Choice Select | No | A combo box of choices.  Default for Choice questions. |
| ChoiceRadio | Choice Radio | No | A radio button of choices. An option for Choice questions with 2-3 choices |
| BooleanSelect | Boolean Select | No | A boolean combo box. |
| StringTextArea | String Text Box | No | A simple multiline text field. |
| BooleanRadio | Boolean Radio | No | A radio button for Yes and No. |

---

### Typelist: QuestionPostOnChange

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\QuestionPostOnChange.tti`
**Description:** Question postOnChange Behavior
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| always | Always | No | Question always posts on change |
| auto | Automatic | No | Question only posts on change if other questions depend on its answer |

---

### Typelist: QuestionSetType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\QuestionSetType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\QuestionSetType.ttx`
**Description:** A kind of question set
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| underwriting | Underwriting | No | Underwriting |
| productqualification | Product Qualification | No | Product Qualification |

---

### Typelist: QuestionType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\QuestionType.tti`
**Description:** A kind of question
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Boolean | Boolean | No | A question whose answer is Yes or No |
| Date | Date | No | A question whose answer is a Date |
| Integer | Integer | No | A question whose answer is an Integer |
| String | String | No | A question whose answer is a String |
| Choice | Choice | No | A multiple-choice question whose answer is an entry in the QuestionChoice table |

---

### Typelist: QuoteMaturityLevel

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\QuoteMaturityLevel.tti`
**Description:** The various states a policy period can be in with more mature states having higher priorities
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| unrated | Unrated | No | Period has no rating information |
| rated | Rated | No | Period is rated |
| quoted | Quoted | No | Period is quoted |

---

### Typelist: QuoteRoundingMode

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\QuoteRoundingMode.tti`
**Description:** QuoteRoundingMode
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| UP | Up | No | Up |
| DOWN | Down | No | Down |
| CEILING | Ceiling | No | Ceiling |
| FLOOR | Floor | No | Floor |
| HALF_UP | Half Up | No | Half Up |
| HALF_DOWN | Half Down | No | Half Down |
| HALF_EVEN | Half Even | No | Half Even |
| UNNECESSARY | Unnecessary | No | Unnecessary |

---

### Typelist: QuoteType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\QuoteType.tti`
**Description:** Kinds of quotes you can request
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Quick | Quick Quote | No | Quick Quote |
| Full | Full Application | No | Full Application |

---

### Typelist: RadioactiveCoverage

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RadioactiveCoverage.tti`
**Description:** Radioactive Contamination Coverage Applicable
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| limited | Limited | No | Limited |
| broad | Broad | No | Broad |

---

### Typelist: RadiusCode

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RadiusCode.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\RadiusCode.ttx`
**Description:** Radius Code
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 200PlusMiles | Long Haul | No | Long Haul |
| 0 | Not applicable | No | Not applicable |
| 15orLess | Local | No | Local |
| 15orMore | Intermediate | No | Intermediate |
| LessThan50Miles | Local | No | Local |
| 50-200Miles | Intermediate | No | Intermediate |

---

### Typelist: RateAmountType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RateAmountType.tti`
**Description:** The type of credit or debit that the cost represents.
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| StdPremium | Standard premium | No | A standard premium. |
| NonstdPremium | Non-standard Premium | No | A non-standard premium. |
| TaxSurcharge | Tax or surcharge | No | A tax or surcharge. |

---

### Typelist: RateBookExportType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RateBookExportType.tti`
**Description:** A typelist of rate book export formats 
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Excel | Excel | No | Excel File Format |
| XML | XML | No | Xml file format |

---

### Typelist: RateBookStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RateBookStatus.tti`
**Description:** Describes where a rate book is in the workflow, which in turn determines whether it can be edited (or be re-opened for editing), whether it needs approval, etc.
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Draft | Draft | No | The rate book may be freely edited |
| Stage | Stage | No | The rate book has been updated and needs approval to go into production |
| Approved | Approved | No | The rate book has been approved to go into production, but has not been moved into production yet |
| Active | Active | No | The rate book is in production and may not normally be changed |

---

### Typelist: RatedPeril

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RatedPeril.tti`
**Description:** Rated peril
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| fire | Fire | No | Fire |
| lightning | Lightning | No | lightning |
| windstormhail | Windstorm or Hail | No | Windstorm or hail |
| explosion | Explosion | No | Explosion |
| riotcommotion | Riot or Civil Commotion | No | Riot or civil commotion |
| aircraft | Aircraft | No | Damage caused by aircraft |
| vehicles | Vehicles | No | Damage cause by vehicles |
| smoke | Smoke | No | Smoke |
| vandalism | Vandalism | No | Vandalism |
| theft | Theft | No | Theft |
| volcanic | Volcanic Action | No | Volcanic action |
| fallingobject | Falling Object | No | Falling object |
| icesnow | Weight of Ice, Snow, or Sleet | No | Weight of ice, snow, or sleet |
| water | Non-Weather Water | No | Non-weather water |

---

### Typelist: RateEngineParameter

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RateEngineParameter.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\RateEngineParameter.ttx`
**Description:** Describes the type of parameters used in a rating engine
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| RateBookStatus | RateBookStatus | No | Uses a RateBookStatus typelist |

---

### Typelist: RateFactorType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RateFactorType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\RateFactorType.ttx`
**Description:** Types of rating inputs
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Building | Building features | No | Age, condition, and unusual structural features |
| Employees | Employees | No | Selection, training, supervision, and experience |
| EmpQual | Employee qualifications | No | Employee qualifications |
| ExtraSafetyPrograms | Extraordinary safety programs applicable to workplace | No | Extraordinary safety programs applicable to workplace |
| Location | Location | No | Accessibility, congestion, and exposures |
| Management | Management | No | Cooperation in matters of safeguarding and proper handling of the property covered |
| MedFacilities | Availability of medical facilities in or near workplace | No | Availability of medical facilities in or near workplace |
| MgmtCooperation | Cooperation with carrier by management | No | Cooperation with carrier by management |
| OtherRisk | Other risk characteristics not addressed above (specified) | No | Other risk characteristics not addressed above (specified) |
| PolicyExpense | Considerations related to policy expenses | No | Considerations related to policy expenses |
| Premises | Premises and equipment | No | Care, condition, and type |
| Protection | Protection | No | Not otherwise recognized |
| RiskNotInClassifPlan | Risk elements not addressed in the classification plan | No | Risk elements not addressed in the classification plan |
| SafetyEquipment | Safety equipment/devices present in/missing from workplace | No | Safety equipment/devices present in/missing from workplace |
| SafetyOrganization | Safety Organization | No | Safety literature, award, and penalty system |
| ValuesInsured | Dispersion or Concentration of Values Insured | No | Dispersion or Concentration of Values Insured |
| WorkplaceMaint | Workplace maintenance or operations | No | Workplace maintenance or operations |
| LocationInside | Location - Inside Premises | No | Exposure to loss inside the premises |
| LocationOutside | Location - Outside Premises | No | Exposure to loss outside the premises |
| Equipment | Equipment - Type, Condition, Care | No | Equipment - Type, Condition, Care |
| MgmtSafetyOrg | Management - Safety Organization | No | Management - Safety Organization |

---

### Typelist: RateMethod

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RateMethod.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\RateMethod.ttx`
**Description:** Describes the method of rating to be applied
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| SysTable | SysTable | No | Uses a system table based rating engine |
| RateFlow | RateFlow | No | Uses a rate flow based rating engine |

---

### Typelist: RateTableColumnDisplay

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RateTableColumnDisplay.tti`
**Description:** Rate table column display
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Normal | Normal | No | Normal display |
| Small | Small | No | Small display |
| Large | Large | No | Large display |

---

### Typelist: RateTableDataType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RateTableDataType.tti`
**Description:** Rate Table Data Type
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| String | String | No | String Data Type |
| Integer | Integer | No | Integer data type |
| Decimal | Decimal | No | Decimal data type |
| Boolean | Boolean | No | Boolean (bit) data type |
| Date | Date | No | Date data type |

---

### Typelist: RateTableErrorType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RateTableErrorType.tti`
**Description:** RateTableErrorType
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| DuplicateRow | Duplicate factor row | No | Duplicate factor row |
| MinNumFactor | Row requires at least 1 factor | No | Each row must define at least one factor |
| InvalidRange | Invalid range | No | Invalid range |
| RangeOverlap | Numeric range overlap | No | Numeric range overlap |
| InvalidValue | Invalid value | No | Invalid value |
| InvalidCodeValue | Invalid code value | No | Invalid code value |
| InvalidDateFormat | Invalid Date Format | No | Invalid Date Format |
| ValueAfterNull | Actual param value after null value | No | Actual param value after null value |
| ExceedsPrecisionOrScale | Scale or precision exceeds target column | No | Value exceeds scale or precision supported by targeted column(s).  Value(s) has/have been rounded. |
| ParameterRemoved | Highlighted rows use a parameter that has been removed from the rate table definition: you must cancel your changes | No | Parameter was removed from the rate table definition |

---

### Typelist: RateType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RateType.tti`
**Description:** Type of rating to use
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Class | Class | No | Lookup table rate for this type of building |
| Specific | Specific | No | Specific rate that applies only to a particular building as determined by physical inspection of the property |

---

### Typelist: RatingScale

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RatingScale.tti`
**Description:** The scale of the basis to which the rate is applied
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 1 | Per Unit | No | Rate applies to basis amount |
| 100 | Per 100 | No | Rate applies per 100 basis amount |
| 1000 | Per 1000 | No | Rate applies per 1000 basis amount |

---

### Typelist: RatingStyle

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RatingStyle.tti`
**Description:** Used to provide additional granularity for a rating engine to use
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| QuickQuote | Quick Quote | No | Quick quote rating style |
| Default | Default | No | Default rating style |

---

### Typelist: ReasonCode

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ReasonCode.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\ReasonCode.ttx`
**Description:** Reasons
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| nonpayment | Non-payment | No | Payment not received |
| fraud | Fraud | No | Fraud |
| flatrewrite | Policy rewritten or replaced (flat cancel) | No | Policy rewritten or replaced (flat cancel) |
| midtermrewrite | Policy rewritten (mid-term) | No | Policy rewritten (mid-term) |
| unresolvedcontingency | Unresolved Contingency | No | Unresolved Contingency |
| nottaken | Policy not-taken | No | Policy not-taken |
| sold | Out of business/sold | No | Out of business/sold |
| noemployee | No employees/operations | No | No employees/operations |
| noc | Insured's request - N.O.C | No | Insured's request - N.O.C |
| fincononpay | Insured's request - (finance co. nonpay) | No | Insured's request - (Finance co. nonpay) |
| violation | Violation of health, safety, fire, or codes | No | Violation of health, safety, fire, or codes |
| vacant | Vacant; below occupancy limit | No | Vacant; below occupancy limit |
| uwreasons | Underwriting reasons | No | Underwriting reasons |
| suspension | Suspension or revocation of license or permits | No | Suspension or revocation of license or permits |
| riskchange | Substantial change in risk or increase in hazard | No | Substantial change in risk or increase in hazard |
| wrapup | Participation in wrap-up complete | No | Participation in wrap-up complete |
| nonreport | Non-report of payroll or failure to cooperate | No | Non-report of payroll or failure to cooperate |
| nondisclose | Non disclosure of losses or underwriting information | No | Non disclosure of losses or underwriting information |
| eligibility | No longer eligible for group or program | No | No longer eligible for group or program |
| reinsurance | Loss of reinsurance | No | Loss of reinsurance |
| failcoop | Failure to cooperate | No | Failure to cooperate |
| failterm | Failure to comply with terms and conditions | No | Failure to comply with terms and conditions |
| failsafe | Failure to comply with safety recommendations | No | Failure to comply with safety recommendations |
| criminal | Criminal conduct by the insured | No | Criminal conduct by the insured |
| condemn | Condemned/unsafe | No | Condemned/unsafe |
| cancel | Cancellation of underlying insurance | No | Cancellation of underlying insurance |
| LossHistory | Loss history | No | Loss history |
| OpsChars | Operations characteristics | No | Operations characteristics |
| ProductsChars | Products characteristics | No | Products characteristics |
| PaymentHistory | Payment history | No | Payment history |
| ProdRequirements | Does not meet program/product requirements | No | Does not meet program/product requirements |
| CovsNotAvailable | Requested coverages/limits not available | No | Requested coverages/limits not available |
| InfoNotProvided | Required information not provided | No | Required information not provided |

---

### Typelist: ReceptacleType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ReceptacleType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\ReceptacleType.ttx`
**Description:** ReceptacleType
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| ULClassA | UL Class A | No | UL Class A |
| ULClassB | UL Class B | No | UL Class B |
| ULClassC | UL Class C | No | UL Class C |

---

### Typelist: ReferenceDateByType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ReferenceDateByType.tti`
**Description:** Types of reference dating
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| PolicyTerm | Policy Term | No | Reference dating is based on the policy term |
| ApplicableObject | Applicable Object | No | Reference dating is based on the applicable object |
| DefinedObject | Defined Object | No | Reference dating is based on the object the pattern defines |

---

### Typelist: ReferenceDateType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ReferenceDateType.tti`
**Description:** Types of reference dates
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| EffectiveDate | EffectiveDate | No | Policy Effective Date |
| WrittenDate | WrittenDate | No | Written date of policy |
| RatingPeriodDate | RatingPeriodDate | No | Rating Period Date |

---

### Typelist: RegionType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RegionType.tti`
**Description:** Types of region definitions
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| state | State | No | State |
| county | County | No | County |
| zip | Zip code | No | Zip code |

---

### Typelist: ReinstateCode

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ReinstateCode.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\ReinstateCode.ttx`
**Description:** Reinstate Reason Codes
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| payment | Payment received | No | Payment received |
| other | Other | No | Other |

---

### Typelist: Relationship

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\Relationship.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\Relationship.ttx`
**Description:** ACORD 1-6-0 Relationship
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| AmbEmp | Ambulance district employee | No | Ambulance district employee |
| ApptOff | Appointed official/officer | Yes | Appointed official/officer |
| AuxPD | Auxiliary police | No | Auxiliary police |
| BdTrMbr | Board of trustee member | Yes | Board of trustee Member |
| CEO | Chief executive officer | Yes | Chief executive officer |
| CFO | Chief financial officer | Yes | Chief financial officer |
| CH | Child | Yes | Child |
| ChmnBOD | Chairman of the board | Yes | Chairman of the board |
| Clergy | Clergy | No | Clergy |
| Cmndr | Commander | Yes | Commander |
| COO | Chief operating officer | Yes | Chief operating officer |
| CorpDir | Corporate director | Yes | Corporate director |
| CorpOffPartSoleProp | Corp. officer, partner, sole proprietor | No | Corporate officer, partner, sole proprietor |
| Ctrlr | Controller | Yes | Controller |
| Dir | Director | No | Director |
| DomAgg | Domestic or agricultural workers | No | Domestic or agricultural workers |
| ElecOfc | Elected/appointed official/officer | No | Elected/appointed official/officer |
| ElecOfr | Any elected official | Yes | Any elected official |
| EmpChtr | Employee on corp. charter | Yes | Employee on corp. charter |
| Empl | Empl-not spouse, partner, corp. officer | Yes | Employee - not spouse, partner or corporate officer |
| ExecDir | Executive director | No | Executive director |
| FamilyMember | Farm family member | No | Farm family member |
| FDEmp | Fire district employees | No | Fire district employees |
| FireChf | Fire chief | Yes | Fire chief |
| GenPtnr | General partner | No | General partner |
| Indv | Individual | No | Individual |
| LtdPtnr | Limited partner | No | Limited partner |
| Mayor | Mayor | Yes | Mayor |
| Member | Assn. member | No | Assn. member |
| Npers | Named person | No | Named person |
| Officer | Officer | No | Officer |
| OfcrBOD | Officer-board of directors | Yes | Officer-board of directors |
| Ot | Other | No | Other |
| PolChf | Police Chief | Yes | Police chief |
| PrefWrk | Preferred worker | Yes | Preferred Worker |
| Pres | President | No | President |
| Princpl | Principal | Yes | Principal |
| ProjEmp | Project employee | Yes | Project employee |
| PrpOwnr | Property owner | Yes | Property Owner |
| REMgt | Real estate management workers | No | Real estate management workers |
| Ptnr | Partner | No | Partner |
| Relative | Relative | No | Relative |
| ResEmp | Residence employee | No | Residence employee |
| Sec | Secretary | No | Secretary |
| SolePrp | Sole proprietor | No | Sole proprietor |
| SP | Spouse | No | Spouse |
| StatEmp | Statutory employee | No | Statutory employee |
| Supr | Superintendent | No | Superintendent |
| Treas | Treasurer | No | Treasurer |
| Trustee | Trustee | No | Trustee |
| ViceCmd | Vice commander | Yes | Vice commander |
| VP | Vice-president | No | Vice-president |
| Vol | Volunteer | No | Volunteer |
| Wstudy | Work study | No | Work study |

---

### Typelist: RenewalCode

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RenewalCode.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\RenewalCode.ttx`
**Description:** Renewal Reason Codes
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| goodrisk | Renew - good risk | No | Renew - good risk |
| assignedrisk | Renew - assigned risk | No | Renew - assigned risk |
| accountfavor | Renew - account consideration | No | Renew - account consideration |
| producerfavor | Renew - producer consideration | No | Renew - producer consideration |
| requiredbylaw | Renew - legal requirement | No | Renew - legal requirement |

---

### Typelist: ResidenceType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ResidenceType.tti`
**Description:** ResidenceType
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Fam1 | 1 Family Residence | No | Single Family |
| Fam2 | 2 Family Residence | No | Duplex |
| Fam3 | 3 Family Residence | No | Triplex |
| Fam4 | 4 Family Residence | No | Quadplex |
| Fam5 | 5+ Family Residence | No | More than 4 |
| Apartment | Apartment | No | Apartment |
| Condo | Condominium | No | Condominium |
| Mobile | Mobile Home | No | Mobile Home |

---

### Typelist: ResourceContext

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ResourceContext.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\ResourceContext.ttx`
**Description:** A context for packaging rule sets, libraries, script parameters, and other configurable resources
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| wc | Guidewire WC | No | Guidewire workers' compensation related resources |
| base | Guidewire base | No | Guidewire base configuration related resources |
| sample | Guidewire sample data | No | Guidewire Sample Data related resources |

---

### Typelist: ReviewCategory

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ReviewCategory.tti`
**Description:** Category for Service Provider Management Review questions and categories; generally, this will be extended by customers
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| general | General | No | A default category for general questions. |

---

### Typelist: ReviewServiceType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ReviewServiceType.tti`
**Description:** Service types list for Service Provider Management Reviews; generally, this will be extended by customers
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| other | Other | No | Indicates that no more specific service type is applicable. |

---

### Typelist: RevisionType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RevisionType.tti`
**Description:** Revision type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Revision | Revision | No | Revision of any kind of audit |
| Reversal | Reversal | No | Reversal of an audit or an audit revision |

---

### Typelist: RewriteType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RewriteType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\RewriteType.ttx`
**Description:** Type of rewrite
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| RewriteFullTerm | Rewrite Full Term | No | Rewrite Full Term |
| RewriteRemainderOfTerm | Rewrite Remainder of Term | No | Rewrite Remainder of Term |
| RewriteNewTerm | Rewrite New Term | No | Rewrite New Term |

---

### Typelist: RIAttachmentInclusionType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RIAttachmentInclusionType.tti`
**Description:** Reinsurance attachment inclusion typelist
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Included | Included | No | Included attachments |
| Excluded | Excluded | No | Excluded attachments |
| SpecialAcceptance | Special Acceptance | No | Attachments with special acceptance |

---

### Typelist: RICoverageGroupType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RICoverageGroupType.tti`
**Description:** The coverage group indicates the type of Reinsurance that applies to a given Reinsurance Risk 
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Property | Property | No | Includes all building-related property coverages from policies like CP, IM, BOP, and HO |
| Liability | Liability | No | Includes all liability coverages from policies like GL, BOP, HO, D&O, E&O, Pro Liab, and personal or comm Umbrella.  Excludes Auto Liability and Workers Comp liability. |
| AutoPD | Auto PD | No | Includes all property damage coverages for PA, BA, and other property coverages for mobile things like motorcycles, personal watercraft, snow mobiles, etc. |
| AutoLiability | Auto Liability | No | Includes all liability coverages for PA, BA, and other property coverages for mobile things like motorcycles, personal watercraft, snow mobiles, etc. |
| WorkersComp | Workers Comp | No | separate category for Workers Comp liability |

---

### Typelist: RIEffDatedStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RIEffDatedStatus.tti`
**Description:** The status of the current RIEffDated entity
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Draft | Draft | No | Draft status, the RIEffDated is associated with a unbound policy period. |
| Bound | Bound | No | Bound status, the RIEffDated is associated with a bound policy period. |

---

### Typelist: RIRecalcReason

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RIRecalcReason.tti`
**Description:** Reason code for a recalculation
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| PolicyBound | PolicyBound | No | A policy was put in force or changed |
| AuditComplete | AuditComplete | No | Premium transactions were created as a result of an audit. |
| AgreementChange | AgreementChange | No | An agreement reinsuring this Risk was changed |
| ProgramChange | ProgramChange | No | The program reinsuring this Risk was changed |
| PolicyFileEdit | PolicyFileEdit | No | The Reinsurance values for a bound policy were edited in the PolicyFile |

---

### Typelist: RiskAssessmentError

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RiskAssessmentError.tti`
**Description:** Risk Assessment Errors
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| HttpBadRequest | Http Bad Request | No | Risk assessment service reported bad http request |
| NoResponseEntityFromRiskAssessmentService | No Response Entity From Risk Assessment Service | No | No response entity received from risk assessment service |
| RiskAssessmentAuthenticationFailed | Risk Assessment Authentication Failed | No | Risk assessment service authentication failed |
| RiskAssessmentServiceConnectionRefused | Risk Assessment Service Connection Refused | No | Connection to risk assessment service is refused |
| LacksSingleLocationRiskAssessmentPermission | Lacks Single Location Risk Assessment Permission | No | Insufficient permissions to make single location risk assessment requests |
| LacksMultipleLocationRiskAssessmentPermission | Lacks Multiple Location Risk Assessment Permission | No | Insufficient permissions to make multiple location risk assessment requests |
| NoSelectedRiskProfile | Risk Profile Code Required | No | The risk assessment did not send a risk profile code |
| RiskProfileCodeInvalid | Invalid Risk Profile Code | No | Risk profile Code was not recognized by Risk Assessment |
| InvalidLocation-CoordinatesInvalid | Invalid Location Coordinates - Latitude or Longitude Invalid | No | Invalid location latitude |
| InvalidLocation-CoordinatesOrAddressRequired | Invalid Location - Coordinates Or Address Required | No | There was no address or lat long sent to Risk Assessment |
| InvalidLocationGeocodeableAddress-CouldNotGeocode | Invalid Location Geocodeable Address - Could Not Geocode | No | The address sent to Risk Assessment could not be parsed |
| InvalidJson | Invalid Json | No | Invalid Json |
| ErrorForUnexpectedLocation | Error for unexpected location | No | Error was returned for a location that was not requested |
| UnableToParseJSONErrors | Unable to parse JSON errors | No | Unable to parse JSON errors |
| UnknownErrorCategory | Unkown Error Category | No | Risk assessment Error found but not configured with a known category |
| UnknownErrorCode | Unknown Error Code | No | Unknown error code, code is not in this typelist |
| InvalidLocation-PolicySystemIdRequired | Invalid Location Policy System Id Required | No | A public ID was not sent to the risk assessment. |
| NoSelectedLocation | No Selected Location | No | Spotlight interactive there was no pin or selected location |
| TimeoutContactingParameterService | Timeout Contacting Parameter Service | No | Timeout contacting Spotlight Interactive parameter service |
| ErrorContactingParameterService | Error Contacting Parameter Service | No | Error contacting Spotlight Interactive parameter service |
| LocationRequired | Location Required | No |  |

---

### Typelist: RiskAssessmentErrorType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RiskAssessmentErrorType.tti`
**Description:** categories of risk assessment errors
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Request | Request | No | an error at the request level when sending single or multiple locations to be assessed |
| Location | Location | No | error associated with the risk assessment of a single location |

---

### Typelist: RoleType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RoleType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\RoleType.ttx`
**Description:** Defines the role types
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| user | User Role | No | Roles associated with Users |

---

### Typelist: RoofType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RoofType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\RoofType.ttx`
**Description:** Type of roof
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| A | A | No | A |
| B | B | No | B |
| C | C | No | C |

---

### Typelist: RoundingModeType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RoundingModeType.tti`
**Description:** Values corresponding to java.math.RoundingMode
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| UP | ROUND_UP | No | RoundingMode.UP -- Rounding mode to round away from zero. |
| DOWN | ROUND_DOWN | No | RoundingMode.DOWN -- Rounding mode to round towards zero. |
| CEILING | ROUND_CEILING | No | RoundingMode.CEILING -- Rounding mode to round towards positive infinity. |
| FLOOR | ROUND_FLOOR | No | RoundingMode.FLOOR -- Rounding mode to round towards negative infinity. |
| HALF_UP | ROUND_HALF_UP | No | RoundingMode.HALF_UP -- Rounding mode to round towards nearest neighbor, unless both neighbors are equidistant, in which case round up. |
| HALF_DOWN | ROUND_HALF_DOWN | No | RoundingMode.HALF_DOWN -- Rounding mode to round towards nearest neighbor, unless both neighbors are equidistant, in which case round down. |
| HALF_EVEN | ROUND_HALF_EVEN | No | RoundingMode.HALF_EVEN -- Rounding mode to round towards nearest neighbor, unless both neighbors are equidistant, in which case round towards the even neighbor. |
| UNNECESSARY | ROUND_UNNECESSARY | No | RoundingMode.UNNECESSARY -- Rounding mode to assert that the requested operation has an exact result, hence no rounding is necessary. |

---

### Typelist: RoundingScaleType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RoundingScaleType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\RoundingScaleType.ttx`
**Description:** Rounding scale applied to calculations in the Rate Routine.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 4 | .0001 | No | ten thousandths |
| 3 | .001 | No | thousandths |
| 2 | .01 | No | hundredths |
| 1 | .1 | No | tenths |
| 0 | 1 | No | ones |
| minus1 | 10 | No | tens |
| minus2 | 100 | No | hundreds |
| minus3 | 1000 | No | thousands |

---

### Typelist: RowUniformityStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RowUniformityStatus.tti`
**Description:** RowUniformityStatus
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| uniform | Uniform | No | Rows are uniform |
| nonuniform | Non-uniform | No | Non-uniform rows can be made uniform automatically |
| intractable | Intractable | No | Unable to make uniform |

---

### Typelist: RPSDType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RPSDType.tti`
**Description:** the type of Rating Period Start Date
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| anniversary | Anniversary | No | This RPSD is an anniversary date |
| forcedrerating | Forced Rerating | No | This RPSD is a forced rerating |
| latemod | Late Modifier | No | This RPSD is a late modifier change |
| audit | Audit | No | This RPSD is for splitting in an audit |

---

### Typelist: RuleActionKey

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RuleActionKey.tti`
**Description:** Key to a RuleAction
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| *(None defined)* | *Dynamic or database-driven* | No | Typelist populated dynamically at runtime or via database table |

---

### Typelist: RuleBooleanOperator

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RuleBooleanOperator.tti`
**Description:** RuleBooleanOperator
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| AND | AND | No | AND |
| OR | OR | No | OR |

---

### Typelist: RuleConditionType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RuleConditionType.tti`
**Description:** Type of rule condition
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| AlwaysTrue | None | No | AlwaysTrue |
| AllAnd | All of the following criteria must be true (AND) | No | AllAnd |
| AllOr | At least one of the following criteria must be true (OR) | No | AllOr |
| Advanced | The following combination of criteria must evaluate to true (AND/OR) | No | Advanced |

---

### Typelist: RuleContextDefinitionKey

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RuleContextDefinitionKey.tti`
**Description:** Key to a RuleContextDefinition
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| *(None defined)* | *Dynamic or database-driven* | No | Typelist populated dynamically at runtime or via database table |

---

### Typelist: RuleExecutionStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RuleExecutionStatus.tti`
**Description:** Business Rule Execution Status
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Enabled | Enabled | No | This rule is running in this environment |
| Invalid | Invalid | No | This rule is not running in this environment due to validation errors |
| Disabled | Disabled | No | This rule is not running in this environment as it is disabled |
| NotDeployed | Not Deployed | No | This rule is not running in this environment as it has not been deployed |
| PrevDisabled | Previous Version Disabled | No | This rule is not running in this environment as the previously deployed version of this rule is not enabled |
| PrevEnabled | Previous Version Enabled | No | The previous version of this rule is running in this environment |
| Unknown | Unknown | No | Validation in progress and run status unknown |

---

### Typelist: RuleImportSide

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RuleImportSide.tti`
**Description:** Existing or Importing rule version of a RuleImportEntry to use as a new head version
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Existing | Existing | No | An existing rule version |
| Importing | New | No | An importing rule version |

---

### Typelist: RuleImportStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RuleImportStatus.tti`
**Description:** Rule Import Status
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| New | New Rule | No | The rule is new |
| NoConflict | New Version | No | The rule was modified only on remote system |
| Conflict | Versions Conflict | No | The rule was modified on both systems |
| ResolvedConflict | Versions Conflict | No | The rule was modified on both systems and the conflict has been resolved |
| NoAction | Skipped | No | No action is required because the imported rule version already exists |
| Deployed | Rule Deployment | No | The rule was deployed on a different system |
| ImportedNew | Imported New Rule | No | The new rule was imported |
| Imported | Replaced with New Version | No | The new rule version was imported |
| ImportedConflict | Replaced with Importing Version | No | The rule was modified on both systems, the conflict was resolved and the rule was imported |
| ImportedDeployed | Existing Version Deployed | No | The rule was deployed on a different system and imported to this system |
| Discarded | Discarded | No | The import was discarded |
| ExistingConflict | Kept Existing Version | No | The rule was modified on both systems, the conflict was resolved and the rule was kept the same |
| ImportedEditedConflict | Applied Edited Version | No | The rule was modified on both systems, the conflict was resolved and a new draft was imported for resolution |
| EditedResolvedConflict | Edited Version | No | The rule was modified on both systems, and a new edited version was created |

---

### Typelist: RuleOperator

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RuleOperator.tti`
**Description:** Operators for biz rules
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| GreaterThan | > | No | Greater Than |
| GreaterThanOrEqual | >= | No | Greater Than Or Equal |
| LessThan | < | No | Less Than |
| LessThanOrEqual | <= | No | Less Than Or Equal |
| Equals | = | No | Equals |
| NotEquals | Is Not Equal To | No | NotEquals |
| IsTrue | Is True | No | Is True |
| IsFalse | Is False | No | Is False |
| IsIn | Is In | No | The right-hand-side operand must evaluate to an array, and the left-hand-side operand must evaluate to a type matching a single element in the array. Evaluates to true if at least one of the elements in the array matches the left-hand operand. |
| IsNotIn | Is Not In | No | The opposite of IsIn |
| Contains | Contains | No | When the left-hand-side operand evaluates to an array, this operator is the only one that is available. Evaluates to true if at least one of the elements in the array matches the right-hand operand. |
| DoesNotContain | Does Not Contain | No | The opposite of Contains |
| HasAValue | Has a Value | No | Has a Value |
| HasNoValue | Has No Value | No | Has No Value |

---

### Typelist: RuleSetType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RuleSetType.tti`
**Description:** Types of rule sets
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| V | Validation | No | Validation rules |
| A | Assignment | No | Assignment rules |
| AR | Archive | No | Archiving rules |
| E | Exception | No | Exception rules |
| WP | Workplan | No | Workplan rules |
| L | Loaded | No | Rules executed on a imported claim |
| PR | Pre-setup | No | Rules executed on a new claim before it has been set up |
| PO | Post-setup | No | Rules executed on a new claim after it has been set up |
| C | Closed | No | Actions to be taken after closing a claim or exposure |
| PU | Pre-update | No | Rules execute after validating, but before updating an editable entity |
| EM | Event Message | No | Rules for generating integration event messages |
| AP | Approval Routing | No | Used to find the user who must approve an approval batch |
| TAR | Transaction Approval | No | Used to determine whether or not a transaction needs approval |

---

### Typelist: RuleStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RuleStatus.tti`
**Description:** Business Rule Status
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| draft | Draft | No | The rule is being developed |
| staged | Staged | No | The rule is being tested |
| approved | Approved | No | The rule is approved for production |

---

### Typelist: RuntimePropertyGroup

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\RuntimePropertyGroup.tti`
**Description:** Grouping for RuntimeProperty entities
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| configuration | Configuration | No | General configuration properties. |
| integration | Integration | No | General integration properties. |

---

### Typelist: SafeDoorType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\SafeDoorType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\SafeDoorType.ttx`
**Description:** Safe door type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| RND | Round | No | Round |
| SQR | Square | No | Square |

---

### Typelist: Safeguards

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\Safeguards.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\Safeguards.ttx`
**Description:** Burglary And Robbery Protective Safeguards
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| br1 | BR-1 | No | Burglary Alarm - notifies outside station or police |
| br2 | BR-2 | No | Burglary Alarm - Siren or Gong |
| br3 | BR-3 | No | Security Service with hourly rounds and watch clock |
| br4 | BR-4 | No | Other |

---

### Typelist: SafeLabel

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\SafeLabel.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\SafeLabel.ttx`
**Description:** Safe label
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| U | UL | No | UL |
| S | SMNA | No | SMNA |

---

### Typelist: SafeType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\SafeType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\SafeType.ttx`
**Description:** Class of safe
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| TL15 | TL15 | No | TL15 |
| TL30 | TL30 | No | TL30 |
| TL60 | TL60 | No | TL60 |
| TRTL15 | TRTL15 | No | TRTL15 |
| TRTL30 | TRTL30 | No | TRTL30 |
| TRTL60 | TRTL60 | No | TRTL60 |
| TXTL15 | TXTL15 | No | TXTL15 |
| TXTL30 | TXTL30 | No | TXTL30 |
| TXTL60 | TXTL60 | No | TXTL60 |

---

### Typelist: SafetyPremiumCreditType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\SafetyPremiumCreditType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\SafetyPremiumCreditType.ttx`
**Description:** Safety Premium Credit
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 5 | 5% | No | 5% |

---

### Typelist: SampleColor

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\SampleColor.tti`
**Description:** Sample color type list
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| ffffff | White (retired) | Yes | White (retired) |
| 000000 | Black | No | Black |
| ff0000 | Red | No | Red |
| 00ff00 | Green | No | Green |
| 1589ff | Dodger Blue | No | Dodger Blue |
| ff00ff | Magenta | No | Magenta |
| ff8040 | Orange | No | Orange |

---

### Typelist: SampleDataSet

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\SampleDataSet.tti`
**Description:** A set of sample data for non-production use
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| tiny | Tiny | No | Just a few users like aapplegate, good for unit tests. |
| small | Small | No | A small community model and a few sample Accounts and Policies, useful for local development. |
| large | Large | No | A large, full data set useful for demonstrations and manual QA. |
| productxjobstatus | Product x Job Status | No | A data set containing policies for every product in every job status allowed by our builders. |
| search | Free-text Search | No | A standalone data set containing accounts and policies for exercising Free-text search |

---

### Typelist: SampleDataSetCategory

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\SampleDataSetCategory.tti`
**Description:** Categories of sample data (non-production)
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| additive | Additive | No | Sample data that builds on smaller data sets.  Typekey priority is used to determine what to load. |
| standalone | Standalone | No | Sample data that is not meant to build on other data sets.  Priority is ignored except for display purposes. |

---

### Typelist: SampleTheme

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\SampleTheme.tti`
**Description:** Sample color theme
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| cold | Cold | No | Cold color |
| warm | Warm | No | Warm color |

---

### Typelist: ScriptParameterType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ScriptParameterType.tti`
**Description:** Value type of a script parameter
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| varchar | varchar | No | varchar |
| integer | integer | No | integer |
| bit | bit | No | bit |
| datetime | datetime | No | datetime |
| decimal | decimal | No | decimal |
| money | money | No | money |
| nonnegativeinteger | nonnegativeinteger | No | nonnegativeinteger |
| nonnegativemoney | nonnegativemoney | No | nonnegativemoney |
| risk | risk | No | risk |
| postalcode | postalcode | No | postalcode |
| speed | speed | No | speed |
| phone | phone | No | phone |
| year | year | No | year |
| percentage | percentage | No | percentage |
| percentagedec | percentagedec | No | percentagedec |
| monthlyfrequency | monthlyfrequency | No | monthlyfrequency |
| weeklyfrequency | weeklyfrequency | No | weeklyfrequency |
| positivemoney | positivemoney | No | positivemoney |
| positiveinteger | positiveinteger | No | positiveinteger |
| user | user | No | User |
| group | group | No | Group |

---

### Typelist: SearchObjectType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\SearchObjectType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\SearchObjectType.ttx`
**Description:** The type of search
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| *(None defined)* | *Dynamic or database-driven* | No | Typelist populated dynamically at runtime or via database table |

---

### Typelist: Segment

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\Segment.tti`
**Description:** Market segment that a underwriting company is eligible to provide insurance for.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| low | Low Hazard | No | Low Hazard Market Segment |
| med | Medium Hazard | No | Medium Hazard Market Segment |
| high | High Hazard | No | High Hazard Market Segment |

---

### Typelist: SignConstruction

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\SignConstruction.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\SignConstruction.ttx`
**Description:** Sign Construction
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| entirelymetal | Entirely Metal | No | Entirely Metal |
| other | Other | No | Other |

---

### Typelist: SignType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\SignType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\SignType.ttx`
**Description:** Inland Marine Sign Type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| mechanical | Mechanical | No | Mechanical |
| neon | Neon | No | Neon |
| fluorescent | Fluorescent | No | Fluorescent |
| automatic | Automatic | No | Automatic |
| lamps | Lamps | No | Lamps |
| other | Other | No | Other |

---

### Typelist: SmallBusinessType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\SmallBusinessType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\SmallBusinessType.ttx`
**Description:** List of Small Business Types
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| convenience | Convenience Store | No | Convenience store |
| contractor | Contractor-artisan | No | Contractor-artisan |
| condominium | Condominium-residential | No | Condominium-residential |
| restaurant_fast | Restaurant-fast food | No | Restaurant-fast food |
| office | Office bldg-lro | No | Office bldg-lro |
| contractor_land | Contractor-landscape | No | Contractor-landscape |
| processor | Processing | No | Processing |
| selfstore | Self Storage | No | Self Storage |
| motel | Motel | No | Motel |
| service | Services-personal/professional | No | Services-personal/professional |
| notlisted | Not listed | Yes | Not listed |
| wholesale | Wholesaler | No | Wholesaler |
| retail | Store-Retail | No | Store-Retail |
| restaurant_limited | Restaurant-limited | No | Restaurant-limited |
| apartment | Apartment | No | Apartment |

---

### Typelist: SmartCommsTransactionType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\SmartCommsTransactionType.tti`
**Description:** SmartComms Bulk Job Transaction Types
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| TRANSACTION_FILE | Transaction File | No | Used when you want to process a single input XML data file. |
| TRANSACTION_FOLDER | Transaction Folder | No | Used when you want to submit more than one input XML data file as one job |

---

### Typelist: SmokeAlarms

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\SmokeAlarms.tti`
**Description:** 
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| none | None | No | None |
| allfloors | All Floors | No | Smoke Alarms on All Floors |
| partial | Partial | No | Smoke Alarms but not on All Floors |

---

### Typelist: SortByRange

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\SortByRange.tti`
**Description:** Possible values to sort notes by
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| author | Author | No | Sort by Author |
| date | Date | No | Sort by Date |
| subject | Subject | No | Sort by Subject |
| topic | Topic | No | Sort by Topic |

---

### Typelist: SpecialCov

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\SpecialCov.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\SpecialCov.ttx`
**Description:** What kind of special coverage does this group of employees have?
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| stat | State Act | No | WC 00 02 01 |
| voco | Voluntary Comp | No | WC 00 03 11A |
| uslh | U.S.L. & H. | No | WC 00 01 06A |
| ocsa | Outer Continental Shelf Act | No | WC 00 01 09A |
| fcmh | Fed Coal Mine Act | No | WC 00 01 02 |
| msaw | Migrant and Seasonal Agricultural Worker Act | No | WC 00 01 11 |
| deba | Defense Base Act | No | WC 00 01 01A |
| pxact | Non-appropriated Fund Instrumentality's Act | No | WC 00 01 08A |
| mari | Maritime Coverage | No | WC 00 02 01 |
| fela | Fed Empl Liab Act | No | WC 00 01 04a |
| ltdm | Limited Maritime | No | WC 00 02 04 |
| stop | Exposure Rated Stop Gap | No | WC 00 03 03 |

---

### Typelist: SpecialHandling

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\SpecialHandling.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\SpecialHandling.ttx`
**Description:** Special handling for a Policy Change.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| billimmediately | Bill Immediately | No | Bill Immediately |
| billonnext | Bill on Next Invoice | No | Bill on Next Invoice |
| holdforaudit | Hold for Final Audit | No | Holds all charges on this billing instruction for Final Audit |
| holdforauditall | Hold for Final Audit (All Unbilled Items) | No | Holds all unbilled items on the policy period for Final Audit |

---

### Typelist: SpecialtyType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\SpecialtyType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\SpecialtyType.ttx`
**Description:** Doctor specialties
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| allergy | Allergy | No | Allergy |
| anesthesiology | Anesthesiology | No | Anesthesiology |
| cardiology | Cardiology | No | Cardiology |
| dermatology | Dermatology | No | Dermatology |
| emergencymed | Emergency medicine | No | Emergency medicine |
| endocrinology | Endocrinology | No | Endocrinology |
| ent | ENT | No | ENT |
| familypractice | Family practice | No | Family Practice |
| gastroenterology | Gastroenterology | No | Gastroenterology |
| hematologyonc | Hematalogy/oncology | No | Hematalogy/oncology |
| hospitalist | Hospitalist | No | Hospitalist |
| infectiousdis | Infectious disease | No | Infectious disease |
| internalmed | Internal medicine | No | Internal medicine |
| medpeds | Med/peds | No | Med/peds |
| nephrology | Nephrology | No | Nephrology |
| neurology | Neurology | No | Neurology |
| obgyn | Obstetrics/gynecology | No | Obstetrics/gynecology |
| occupationalmed | Occupational medicine | No | Occupational medicine |
| opthalmology | Opthalmology | No | Opthalmology |
| pathology | Pathology | No | Pathology |
| physmedrehab | Physical medicine/rehabilitation | No | Physical medicine/rehabilitation |
| plasticsurgery | Plastic surgery | No | Plastic surgery |
| psychiatry | Psychiatry | No | Psychiatry |
| pulmcritcare | Pulmonary/Critical Care | No | Pulmonary/Critical Care |
| surgery | Surgery | No | Surgery |
| orthopedics | Orthopedics | No | Orthopedics |
| chiropractic | Chiropractic | No | Chiropractic |
| dental | Dental | No | Dental |

---

### Typelist: SpecificHazard

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\SpecificHazard.tti`
**Description:** Hazard Type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| fireplace | Fireplace | No | Fireplace |
| woodstove | Woodstove | No | Woodstove |
| floodzone | Flood Zone | No | Flood Zone |
| brushzone | Brush Zone | No | Brush Zone |
| forestfirezone | Forest Fire Zone | No | Forest Fire Zone |
| landslidezone | Landslide Zone | No | Landslide Zone |
| tidalwater | Tidal Water | No | Tidal Water |

---

### Typelist: SpecifiedCauseOfLoss

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\SpecifiedCauseOfLoss.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\SpecifiedCauseOfLoss.ttx`
**Description:** Cause of loss
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| fire | Fire | No | fire |
| firetheft | Fire and theft | No | Fire and theft |
| firetheftstorm | Fire, theft, and windstorm | No | Fire, theft, and windstorm |
| limited | Limited specified causes of loss | No | Limited specified causes of loss |

---

### Typelist: SpoilageType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\SpoilageType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\SpoilageType.ttx`
**Description:** Spoilage type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| BkdownContam | Breakdown/contamination | No | Breakdown/contamination |
| PowerOutage | Power outage | No | Power outage |
| All | Breakdown/contamination/power outage | No | Breakdown/contamination/power outage |

---

### Typelist: Sprinklered

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\Sprinklered.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\Sprinklered.ttx`
**Description:** Percentage of building covered by sprinklers
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 100 | 100% | No | 100% |
| 90 | 90% | No | 90% |
| 80 | 80% | No | 80% |
| 70 | 70% | No | 70% |
| 60 | 60% | No | 60% |
| 50 | 50% | No | 50% |
| 40 | 40% | No | 40% |
| 30 | 30% | No | 30% |
| 20 | 20% | No | 20% |
| 10 | 10% | No | 10% |
| 0 | N/A | No | N/A |

---

### Typelist: SprinklerSystemType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\SprinklerSystemType.tti`
**Description:** Sprinkler System Type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| none | None | No | None |
| full | Full | No | Full |
| partial | Partial | No | Partial |

---

### Typelist: SQLStatementType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\SQLStatementType.tti`
**Description:** Types of sql statements
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| select | Select | No | Select statement |
| update | Update | No | Update statement |
| insert | Insert | No | Insert statement |
| delete | Delete | No | Delete statement |
| createtable | Create table | No | Create table statement |
| dropsequence | Drop sequence | No | Drop sequence statement |
| droptable | Drop table | No | Drop table statement |
| renametable | Rename table | No | Rename table statement |
| truncatetable | Truncate table | No | Truncate table statement |
| createindex | Create index | No | Create index statement |
| dropindex | Drop index | No | Drop index statement |
| addcolumn | Add column | No | Add column statement |
| dropcolumn | Drop column | No | Drop column statement |
| renamecolumn | Rename column | No | Rename column statement |
| columnnullability | Change column nullability | No | Change column nullability statement |
| updatedbstats | Update db statistics | No | Update db statistics statement |
| createfk | Create foreign key | No | Create foreign key statement |
| dropfk | Drop foreign key | No | Drop foreign key statement |
| createpk | Create primary key | No | Create primary key statement |
| droppk | Drop primary key | No | Drop primary key statement |
| other | Other | No | Other statement type |
| deletedbstats | Delete db statistics | No | Delete db statistics statement |
| altertabledegree | Alter table degree | No | Alter table degree statement |
| altercolumn | Alter column | No | Alter table (column) statement |
| disableidentityinsert | Disable identity insert | No | Disable identity insert statement |
| enableidentityinsert | Enable identity insert | No | Enable identity insert statement |

---

### Typelist: StartPointType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\StartPointType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\StartPointType.ttx`
**Description:** The different fields on an activity or claim that could be used as the starting point for another date field
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| activitycreation | Activity creation date | No | Creation date of the activity |
| startdate | Activity start date | No | Start date on activity |
| policyeffdate | Policy Effective Date | No | Policy Effective Date |
| policyexpirdate | Policy Expiration Date | No | Policy Expiration Date |

---

### Typelist: StartupPage

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\StartupPage.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\StartupPage.ttx`
**Description:** The startup page for the user
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Desktop | Desktop | No | My Desktop |
| DesktopActivities | Desktop: Activities | No | My Activities in Desktop |
| DesktopSubmissions | Desktop: Submissions | No | My Submissions in Desktop |
| DesktopRenewals | Desktop: Renewals | No | My Renewals in Desktop |
| DesktopOtherWorkOrders | Desktop: OtherWorkOrders | No | My Other Work Orders in Desktop |
| DesktopQueues | Desktop: Queues | No | My Queues in Desktop |
| Search | Search | No | Search |
| Admin | Admin | No | Admin |

---

### Typelist: State

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\State.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\State.example.ttx`
**Description:** States such as in AU, CA, JP, US
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| AK | Alaska | No | Alaska |
| AL | Alabama | No | Alabama |
| AR | Arkansas | No | Arkansas |
| AZ | Arizona | No | Arizona |
| CA | California | No | California |
| CO | Colorado | No | Colorado |
| CT | Connecticut | No | Connecticut |
| DC | District of Columbia | No | District of Columbia |
| DE | Delaware | No | Delaware |
| FL | Florida | No | Florida |
| GA | Georgia | No | Georgia |
| HI | Hawaii | No | Hawaii |
| IA | Iowa | No | Iowa |
| ID | Idaho | No | Idaho |
| IL | Illinois | No | Illinois |
| IN | Indiana | No | Indiana |
| KS | Kansas | No | Kansas |
| KY | Kentucky | No | Kentucky |
| LA | Louisiana | No | Louisiana |
| MA | Massachusetts | No | Massachusetts |
| MD | Maryland | No | Maryland |
| ME | Maine | No | Maine |
| MI | Michigan | No | Michigan |
| MN | Minnesota | No | Minnesota |
| MO | Missouri | No | Missouri |
| MS | Mississippi | No | Mississippi |
| MT | Montana | No | Montana |
| NC | North Carolina | No | North Carolina |
| ND | North Dakota | No | North Dakota |
| NE | Nebraska | No | Nebraska |
| NH | New Hampshire | No | New Hampshire |
| NJ | New Jersey | No | New Jersey |
| NM | New Mexico | No | New Mexico |
| NV | Nevada | No | Nevada |
| NY | New York | No | New York |
| OH | Ohio | No | Ohio |
| OK | Oklahoma | No | Oklahoma |
| OR | Oregon | No | Oregon |
| PA | Pennsylvania | No | Pennsylvania |
| PR | Puerto Rico | No | Puerto Rico |
| RI | Rhode Island | No | Rhode Island |
| SC | South Carolina | No | South Carolina |
| SD | South Dakota | No | South Dakota |
| TN | Tennessee | No | Tennessee |
| TX | Texas | No | Texas |
| UT | Utah | No | Utah |
| VA | Virginia | No | Virginia |
| VT | Vermont | No | Vermont |
| WA | Washington | No | Washington |
| WI | Wisconsin | No | Wisconsin |
| WV | West Virginia | No | West Virginia |
| WY | Wyoming | No | Wyoming |
| AB | Alberta | No | Alberta |
| BC | British Columbia | No | British Columbia |
| MB | Manitoba | No | Manitoba |
| NB | New Brunswick | No | New Brunswick |
| NL | Newfoundland and Labrador | No | Newfoundland and Labrador |
| NT | Northwest Territories | No | Northwest Territories |
| NS | Nova Scotia | No | Nova Scotia |
| NU | Nunavut | No | Nunavut |
| ON | Ontario | No | Ontario |
| PE | Prince Edward Island | No | Prince Edward Island |
| QC | Quebec | No | Quebec |
| SK | Saskatchewan | No | Saskatchewan |
| YT | Yukon | No | Yukon |
| VI | Virgin Islands | No | Virgin Islands |
| MP | Northern Mariana Islands | No | Northern Mariana Islands |
| MH | Marshall Islands | No | Marshall Islands |
| GU | Guam | No | Guam |
| FM | Federated States of Micronesia | No | Federated States of Micronesia |
| AU_SA | South Australia | No | South Australia |
| AU_NT | Northern Territory | No | Northern Territory |
| AU_QLD | Queensland | No | Queensland |
| AU_NSW | New South Wales | No | New South Wales |
| AU_VIC | Victoria | No | Victoria |
| AU_WA | Western Australia | No | Western Australia |
| AU_TAS | Tasmania | No | Tasmania |
| AU_ACT | A.C.T. | No | Australian Capital Territory |
| AU_JBT | Jervis Bay Territory | No | Jervis Bay Territory |
| Aichi | Aichi | No | Aichi |
| Akita | Akita | No | Akita |
| Aomori | Aomori | No | Aomori |
| Chiba | Chiba | No | Chiba |
| Ehime | Ehime | No | Ehime |
| Fukui | Fukui | No | Fukui |
| Fukuoka | Fukuoka | No | Fukuoka |
| Fukushima | Fukushima | No | Fukushima |
| Gifu | Gifu | No | Gifu |
| Gumma | Gumma | No | Gumma |
| Hiroshima | Hiroshima | No | Hiroshima |
| Hokkaido | Hokkaido | No | Hokkaido |
| Hyogo | Hyogo | No | Hyogo |
| Ibaraki | Ibaraki | No | Ibaraki |
| Ishikawa | Ishikawa | No | Ishikawa |
| Iwate | Iwate | No | Iwate |
| Kagawa | Kagawa | No | Kagawa |
| Kagoshima | Kagoshima | No | Kagoshima |
| Kanagawa | Kanagawa | No | Kanagawa |
| Kochi | Kochi | No | Kochi |
| Kumamoto | Kumamoto | No | Kumamoto |
| Kyoto | Kyoto | No | Kyoto |
| Mie | Mie | No | Mie |
| Miyagi | Miyagi | No | Miyagi |
| Miyazaki | Miyazaki | No | Miyazaki |
| Nagano | Nagano | No | Nagano |
| Nagasaki | Nagasaki | No | Nagasaki |
| Nara | Nara | No | Nara |
| Niigata | Niigata | No | Niigata |
| Oita | Oita | No | Oita |
| Okayama | Okayama | No | Okayama |
| Okinawa | Okinawa | No | Okinawa |
| Osaka | Osaka | No | Osaka |
| Saga | Saga | No | Saga |
| Saitama | Saitama | No | Saitama |
| Shiga | Shiga | No | Shiga |
| Shimane | Shimane | No | Shimane |
| Shizuoka | Shizuoka | No | Shizuoka |
| Tochigi | Tochigi | No | Tochigi |
| Tokushima | Tokushima | No | Tokushima |
| Tokyo | Tokyo | No | Tokyo |
| Tottori | Tottori | No | Tottori |
| Toyama | Toyama | No | Toyama |
| Wakayama | Wakayama | No | Wakayama |
| Yamagata | Yamagata | No | Yamagata |
| Yamaguchi | Yamaguchi | No | Yamaguchi |
| Yamanashi | Yamanashi | No | Yamanashi |
| DE_BY | Bavaria | No | Bavaria |
| DE_BW | Baden-Wuerttemberg | No | Baden-Wuerttemberg |
| DE_BE | Berlin | No | Berlin |
| DE_BB | Brandenburg | No | Brandenburg |
| DE_HB | Bremen | No | Bremen |
| DE_HH | Hamburg | No | Hamburg |
| DE_HE | Hesse | No | Hesse |
| DE_MV | Mecklenburg-Vorpommern | No | Mecklenburg-Vorpommern |
| DE_NI | Lower Saxony | No | Lower Saxony |
| DE_NW | North Rhine-Westphalia | No | North Rhine-Westphalia |
| DE_RP | Rhineland-Palatinate | No | Rhineland-Palatinate |
| DE_ST | Saxony-Anhalt | No | Saxony-Anhalt |
| DE_SH | Schleswig-Holstein | No | Schleswig-Holstein |
| DE_SL | Saarland | No | Saarland |
| DE_SN | Saxony | No | Saxony |
| DE_TH | Thuringia | No | Thuringia |

---

### Typelist: StateAbbreviation

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\StateAbbreviation.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\StateAbbreviation.ttx`
**Description:** Abbreviations for states such as in AU, CA, JP, US
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| AK | AK | No | Alaska |
| AL | AL | No | Alabama |
| AR | AR | No | Arkansas |
| AZ | AZ | No | Arizona |
| CA | CA | No | California |
| CO | CO | No | Colorado |
| CT | CT | No | Connecticut |
| DC | DC | No | District of Columbia |
| DE | DE | No | Delaware |
| FL | FL | No | Florida |
| GA | GA | No | Georgia |
| HI | HI | No | Hawaii |
| IA | IA | No | Iowa |
| ID | ID | No | Idaho |
| IL | IL | No | Illinois |
| IN | IN | No | Indiana |
| KS | KS | No | Kansas |
| KY | KY | No | Kentucky |
| LA | LA | No | Louisiana |
| MA | MA | No | Massachusetts |
| MD | MD | No | Maryland |
| ME | ME | No | Maine |
| MI | MI | No | Michigan |
| MN | MN | No | Minnesota |
| MO | MO | No | Missouri |
| MS | MS | No | Mississippi |
| MT | MT | No | Montana |
| NC | NC | No | North Carolina |
| ND | ND | No | North Dakota |
| NE | NE | No | Nebraska |
| NH | NH | No | New Hampshire |
| NJ | NJ | No | New Jersey |
| NM | NM | No | New Mexico |
| NV | NV | No | Nevada |
| NY | NY | No | New York |
| OH | OH | No | Ohio |
| OK | OK | No | Oklahoma |
| OR | OR | No | Oregon |
| PA | PA | No | Pennsylvania |
| PR | PR | No | Puerto Rico |
| RI | RI | No | Rhode Island |
| SC | SC | No | South Carolina |
| SD | SD | No | South Dakota |
| TN | TN | No | Tennessee |
| TX | TX | No | Texas |
| UT | UT | No | Utah |
| VA | VA | No | Virginia |
| VT | VT | No | Vermont |
| WA | WA | No | Washington |
| WI | WI | No | Wisconsin |
| WV | WV | No | West Virginia |
| WY | WY | No | Wyoming |
| VI | VI | No | Virgin Islands |
| MP | MP | No | Northern Mariana Islands |
| MH | MH | No | Marshall Islands |
| GU | GU | No | Guam |
| FM | FMa | No | Federated States of Micronesia |
| AB | AB | No | Alberta |
| BC | BC | No | British Columbia |
| MB | MB | No | Manitoba |
| NB | NB | No | New Brunswick |
| NL | NL | No | Newfoundland and Labrador |
| NT | NT | No | Northwest Territories |
| NS | NS | No | Nova Scotia |
| NU | NU | No | Nunavut |
| ON | ON | No | Ontario |
| PE | PE | No | Prince Edward Island |
| QC | QC | No | Quebec |
| SK | SK | No | Saskatchewan |
| YT | YT | No | Yukon |
| AU_SA | SA | No | South Australia |
| AU_NT | NT | No | Northern Territory |
| AU_QLD | QLD | No | Queensland |
| AU_NSW | NSW | No | New South Wales |
| AU_VIC | VIC | No | Victoria |
| AU_WA | WA | No | Western Australia |
| AU_TAS | TAS | No | Tasmania |
| AU_ACT | ACT | No | Australian Capital Territory |
| DE_BY | BY | No | Bavaria |
| DE_BW | BW | No | Baden-Wuerttemberg |
| DE_BE | BE | No | Berlin |
| DE_BB | BBg | No | Brandenburg |
| DE_HB | HB | No | Bremen |
| DE_HH | HH | No | Hamburg |
| DE_HE | HE | No | Hesse |
| DE_MV | MV | No | Mecklenburg-Vorpommern |
| DE_NI | NI | No | Lower Saxony |
| DE_NW | NW | No | North Rhine-Westphalia |
| DE_RP | RP | No | Rhineland-Palatinate |
| DE_ST | ST | No | Saxony-Anhalt |
| DE_SH | SH | No | Schleswig-Holstein |
| DE_SL | SL | No | Saarland |
| DE_SN | SN | No | Saxony |
| DE_TH | TH | No | Thuringia |

---

### Typelist: StopGap

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\StopGap.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\StopGap.ttx`
**Description:** EL coverage for monopolistic states
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| None | None | No | None |
| AllMonopolyStates | All monopoly states | Yes | All monopoly states |
| AllMonopolisticStates | All monopolistic states | No | All monopolistic states |
| ListedStatesOnly | Listed states only | No | Listed states only |

---

### Typelist: StringCriterionMode

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\StringCriterionMode.tti`
**Description:** The mode of a String restriction
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Equals | Equals | No | Useful in flagging whether String restrictions should be implemented with compareEquals. This performs most quickly. |
| StartsWith | StartsWith | No | Useful in flagging whether String restrictions should be implemented with compareStartsWith. This performs moderately quickly. |
| Contains | Contains | No | Useful in flagging whether String restrictions should be implemented with compareContains. This performs most slowly. |

---

### Typelist: SwimmingPools

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\SwimmingPools.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\SwimmingPools.ttx`
**Description:** Number of swimming pools
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 1 | 1 | No | 1 |
| 2 | 2 | No | 2 |
| 3 | 3 | No | 3 |
| 4 | 4 | No | 4 |
| 5 | 5 | No | 5 |
| 6 | 6 | No | 6 |
| 7 | 7 | No | 7 |
| 8 | 8 | No | 8 |
| 9 | 9 | No | 9 |
| 10 | 10 | No | 10 |

---

### Typelist: SynchState

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\SynchState.tti`
**Description:** Sync states for claims and exposures
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| unsynched | unsynched | No | Object is unsynced |
| synch_sent | synch_sent | No | Object is sync_sent (first message has been generated) |

---

### Typelist: SystemPermissionType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\SystemPermissionType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\SystemPermissionType.ttx`
**Description:** Defines all permissions that can be granted to users via privileges and roles. The maximum number of supported SystemPermissionTypes is 7000.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| internaltools | All internal tools | No | Permission to access all Internal Tools |
| toolsInfoview | View Info tools page | No | Permission to access the Info Internal Tools page |
| toolsBatchProcessview | View BatchProcess tools page | No | Permission to access the BatchProcess Internal Tools page |
| toolsBatchProcessedit | Edit BatchProcess tools page | No | Permission to edit the BatchProcess Internal Tools page |
| toolsWorkQueueview | View WorkQueue tools page | No | Permission to access the WorkQueue Internal Tools page |
| toolsWorkQueueedit | Edit WorkQueue tools page | No | Permission to edit the WorkQueue Internal Tools page |
| toolsJMXBeansEdit | Edit ManagementBeans tools page | No | Permission to edit the ManagementBeans presented on Internal Tools page |
| toolsJMXBeansview | View ManagementBeans tools page | No | Permission to access the ManagementBeans Internal Tools page |
| toolsJProfileredit | Edit JProfiler tools page | No | Permission to edit the JProfiler Internal Tools page |
| toolsProfilerview | View Profiler tools page | No | Permission to access the Profiler Internal Tools page |
| toolsProfileredit | Edit Profiler tools page | No | Permission to edit the Profiler Internal Tools page |
| toolsCacheinfoview | View Cache Info page | No | Permission to view the CacheInfo Internal Tools page |
| toolsPluginview | View StartablePlugin tools page | No | Permission to access the StartablePlugin Internal Tools page |
| toolsPluginedit | Edit StartablePlugin tools page | No | Permission to edit the StartablePlugin Internal Tools page |
| toolsLogview | View Log tools page | No | Permission to access the Log Internal Tools page |
| toolsLogedit | Edit Log tools page | No | Permission to edit the Log Internal Tools page |
| toolsClusterview | View Cluster tools page | No | Permission to access the Cluster Internal Tools page |
| toolsClusteredit | Edit Cluster tools page | No | Permission to edit the Cluster Internal Tools page |
| ruleadmin | Administer rules | No | Permission to run Guidewire Studio or import rules |
| regionview | View regions | No | Permission to view the list of regions and region details |
| roleview | View roles | No | Permission to view the list of roles and role details |
| groupview | View groups | No | Permission to view details of a group |
| grouptreeview | View group tree | No | Permission to see the user/group tree on the Administration tab |
| actpatcreate | Create activity pattern | No | Permission to create new activity patterns |
| actpatedit | Edit activity pattern | No | Permission to edit activity patterns |
| actpatdelete | Delete activity pattern | No | Permission to delete activity patterns |
| actpatview | View activity pattern | No | Permission to view the list of activity patterns or activity pattern details |
| attrmanage | Manage attributes | No | Permission to create, edit, or delete user attributes |
| attrview | View attributes | No | Permission to view the list of user attributes or attribute details |
| alpview | View authority limit profiles | No | Permission to view authority limit profiles |
| soapadmin | SOAP administration | No | Permission to use the SOAP APIs |
| debugtools | Always access debug tools | No | Permission to access debug tools, even when they are disabled by a configuration parameter |
| userview | View user | No | Permission to view details of a user |
| scrprmview | View script parameters | No | Permission to view the list of script parameters or details of an individual script parameter |
| scrprmmanage | Manage script parameters | No | Permission to create, edit, or delete script parameters |
| manageldfctrs | Manage load factors | No | Permission to modify the load factors on all users and groups |
| usercreate | Create users | No | Permission to create a new user |
| useredit | Edit users | No | Permission to edit an existing user, except for roles, authority limits, or attributes |
| userdelete | Delete users | No | Permission to delete a user (Note: if a user has had any activity it's recommended to make them non-active rather than delete) |
| usereditattrs | Edit user attributes | No | Permission to edit attributes for a user |
| usereditlang | Edit user language | No | Permission to edit language |
| groupcreate | Create groups | No | Permission to create groups |
| groupdelete | Delete groups | No | Permission to delete groups |
| usergrantroles | Grant roles to users | No | Permission to grant or revoke roles |
| rolemanage | Manage roles | No | Permission to create, edit, or delete roles |
| zonemanage | Manage admin zones | No | Permission to create, edit, or delete admin zones |
| zoneview | View admin zones | No | Permission to view the list of admin zones |
| buswkmanage | Manage business week | No | Permission to create, edit, or delete business week |
| buswkview | View business week | No | Permission to view the list of business week |
| orgcreate | Create organization | No | Permission to create an organization. |
| orgdelete | Delete organization | No | Permission to delete an organization. |
| orgeditbasic | Edit organization basic info | No | Permission to edit an organization's basic info. |
| orgsearch | Search for organization | No | Permission to search for organizations. |
| orgviewbasic | View organization basic info | No | Permission to view an organization's basic info. |
| retrymessage | Retry message | No | Permission to try to resend the failed message |
| skipmessage | Skip message | No | Permission to skip the failed message |
| resyncmessage | Resync message | No | Permission to resync message |
| actmakemand | Make activities mandatory | No | Permission to set whether an activity is mandatory |
| viewteam | View team | No | Permission to view the Team tab |
| actown | Own activity | No | Permission to own an activity.  Note that the user must be able to see the account or job, to own a specific activity. |
| viewworkload | View global workload | No | Permission to view global workload statistics of other users |
| viewactcal | View activity calendar | No | Permission to view activity calendar of other users |
| seczonemanage | Manage security zones | No | Permission to create, edit, and delete security zones |
| regionmanage | Manage regions | No | Permission to create, edit, and delete regions |
| groupedit | Edit groups | No | Permission to edit groups |
| actraown | Reassign owned activities | No | Permission to reassign your own activities |
| actraunown | Reassign unowned activities | No | Permission to reassign activities owned by other users |
| actcreate | Create activities | No | Permission to create new activities |
| workflowview | View workflow | No | Permission to view the Workflow page |
| workflowmanage | Manage workflow | No | Permission to view the ManageWorkflow page |
| doccreate | Create documents | No | Permission to add documents |
| docview | View documents | No | Permission to view documents |
| docedit | Edit documents | No | Permission to edit documents |
| docdelete | Delete documents | No | Permission to remove documents |
| docviewall | View all documents | No | Permission to view all documents, regardless of the permissions set on the individual documents |
| docmodifyall | Modify all documents | No | Permission to edit or delete all documents, regardless of the permissions set on the individual documents |
| notecreate | Create notes | No | Permission to add notes |
| noteview | View notes | No | Permission to view notes |
| noteeditbody | Edit note body | No | Permission to edit the body of notes |
| noteedit | Edit note | No | Permission to edit the notes |
| notedelete | Delete notes | No | Permission to remove notes |
| actreviewassign | Review assignments | No | Permission to review and approve manually-approved assignables |
| abcreatepref | Create address book preferred vendors | No | Permission to add a preferred vendor to the address book |
| abeditpref | Edit address book preferred vendors | No | Permission to modify an existing preferred vendor address book entry |
| acteditunowned | Edit unowned activities | No | Permission to modify (edit/skip/close) activities owned by other users |
| userviewall | View all users | No | Permission to see users in all visible groups |
| usergrantauth | Grant authority limits | No | Permission to grant or change an authority limit for a user |
| actapproveany | Approve any approval activity | No | Permission to approve any approval activity even if the activity is assigned to someone else; the approver is still subject to authority limit restrictions |
| actview | View activities | No | Permission to view activities |
| integadmin | Administer integration | No | Permission to administer integration events |
| purge | Purge objects | No | Permission to purge objects from the database |
| archive | Archive objects | No | Permission to archive objects |
| lvprint | Print listviews | No | Permission to print listviews |
| viewdesktop | View Desktop | No | Permission to view the Desktop |
| viewsearch | View Search | No | Permission to view the Search tab |
| actviewallqueues | View all activity queues | No | Permission to view all activity queues, even those in other security zones |
| actqueuenext | Get next activity from queue | No | Permission to get the next activity off of a queue |
| actqueuepick | Pick activity from queue | No | Permission to pick an activity from a queue |
| actqueueassign | Assign activity from queue | No | Permission to assign an activity from a queue |
| reporting_view | View Report tab | No | Permission to view the Report tab, if the add-on reporting module is installed |
| abview | View address book contacts | No | Permission to view the details of contact entries in the address book |
| abcreate | Create address book contacts | No | Permission to create a new contact in the address book |
| abedit | Edit address book contacts | No | Permission to edit an existing contact in the address book |
| abviewsearch | View address book contact search pages | No | Permission to search contact entries in the address book |
| abdelete | Delete address book contacts | No | Permission to delete an existing contact in the address book |
| abdeletepref | Delete address book preferred vendors | No | Permission to delete an existing preferred vendor address book entry |
| ctcview | View local contacts | No | Permission to view and search local contact entries |
| ctccreate | Create local contacts | No | Permission to create a new local contact |
| ctcedit | Edit local contacts | No | Permission to edit an existing local contact |
| anytagcreate | Create contact with any tag | No | Permission to create a new contact regardless of which tag(s) it has |
| anytagview | View contact with any tag | No | Permission to view the details of a contact regardless of which tag(s) it has |
| anytagedit | Edit contact with any tag | No | Permission to edit the details of a contact regardless of which tag(s) it has |
| anytagdelete | Delete contact with any tag | No | Permission to delete a contact regardless of which tag(s) it has |
| holidayview | View holidays | No | Permission to view a list of holidays or holiday details |
| holidaymanage | Manage holidays | No | Permission to create, edit, and delete holidays |
| admindatachangeview | View Data Change | No | Permission to view the data change page. |
| wsdatachangeedit | Add Data Change | No | Permission to add a data change gosu program. |
| admindatachangeexec | Execute Data Change | No | Permission to execute the data change. |
| changecontactsubtype | Change Contact Subtype | No | Permission to change contact subtype |
| eventmessageview | View event messages | No | Permission to view the event messages page |
| editobfuscatedusercontact | Edit obfuscated user contact | No | Permission to edit obfuscated user contacts |
| requestcontactdestruction | Request Contact Destruction | No | Permission to call the PersonalDataDestructionAPI to destroy contacts |
| reviewcancellation | Review cancellation | Yes | Permission to review a cancellation |
| cancelreschedule | Cancellation reschedule | No | Permission to reschedule a cancellation |
| bindsubmission | Bind submission | No | Permission to bind a submission |
| viewsubmission | View submission | No | Permission to view a submission |
| reviewsubmission | Review submission | Yes | Permission to edit a submission that is in review state |
| reviewpolchange | Review policy change | Yes | Permission to review a policy change |
| reviewreinstate | Review reinstatement | Yes | Permission to review a reinstatement |
| reviewrenewal | Review renewal | Yes | Permission to review a renewal |
| reviewrewrite | Approve rewrite | Yes | Permission to approve rewrite |
| viewaccountholderinfo | Account Holder Info | No | Permission to navigate to and view Account Holder Info page under contacts |
| authprofilecreate | Create authority profile | No | Permission to create or clone an authority profile |
| authprofiledelete | Delete authority profile | No | Permission to delete an authority profile |
| declinesubmission | Decline submission | No | Permission to decline a submission |
| accountcreate | Create account | No | Permission to create an account |
| accountreopen | Reopen account | No | Permission to reopen a withdrawn account |
| accountwithdraw | Withdraw account | No | Permission to withdraw an unused account |
| accountsummary | View account file summary | No | Permission to view account file summary page |
| accountroles | View account file roles | No | Permission to view account file roles page |
| accountcontacts | View account file contacts | No | Permission to view account file contacts page |
| accountrelations | View account file related accounts | No | Permission to view account file related accounts page |
| accounthistory | View account file history | No | Permission to view account file history page |
| accountworkorders | View account file work orders | No | Permission to view account file work orders page |
| accountclaims | View account file claims | No | Permission to view account file claims page |
| accountbilling | View account file billing | No | Permission to view account file billing page |
| accountnotes | View account file notes | No | Permission to view account file notes page |
| accountdocs | View account file documents | No | Permission to view account file documents page |
| accountmovepolicies | Move policies | No | Permission to move policies between accounts |
| accountrewritepolicies | Rewrite policies to account | No | Permission to rewrite policies between accounts |
| contactclaims | View contact file claims | No | Permission to view contact file claims page |
| uwview | View underwriting companies | No | Permission to view the underwriting companies page |
| uwedit | Edit underwriting companies | No | Permission to edit the underwriting companies page |
| cancelovereffdate | Cancellation override effective date | No | Permission to set effective date of cancellation to less than calculated date |
| cancelcarriersource | Cancellation can choose carrier as source | No | Permission to be able to set the carrier as the source |
| canceloverrefund | Cancellation override refund method | No | Permission to override the default refund cancellation method |
| viewmyactivities | View my activities | No | Permission to view My Activities page |
| viewmysubmissions | View my submissions | No | Permission to view My Submissions page |
| viewmyrenewals | View my renewals | No | Permission to view My Renewals page |
| viewmypolicychanges | View my policy changes | No | Permission to view My Policy Changes page |
| viewmyqueues | View my queues | No | Permission to view My Queues page |
| viewsensdoc | View sensitive docs | No | Permission to view a sensitive doc |
| editsensdoc | Edit sensitive docs | No | Permission to edit a sensitive doc |
| delsensdoc | Delete sensitive docs | No | Permission to delete a sensitive doc |
| viewintdoc | View internal docs | No | Permission to view an internal doc |
| editintdoc | Edit internal docs | No | Permission to edit an internal doc |
| delintdoc | Delete internal docs | No | Permission to delete an internal doc |
| createsensnote | Create sensitive notes | No | Permission to create a sensitive note |
| viewsensnote | View sensitive notes | No | Permission to view a sensitive note |
| editsensnote | Edit sensitive notes | No | Permission to edit a sensitive note |
| delsensnote | Delete sensitive notes | No | Permission to delete a sensitive note |
| createintnote | Create internal notes | No | Permission to create an internal note |
| viewintnote | View internal notes | No | Permission to view an internal note |
| editintnote | Edit internal notes | No | Permission to edit an internal note |
| delintnote | Delete internal notes | No | Permission to delete an internal note |
| sendemail | Send Email | No | Permission to create and send email |
| editaccountroles | Edit account roles | No | Permission to edit account roles |
| editpolicyroles | Edit policy roles | No | Permission to edit policy roles |
| editjobroles | Edit job roles | No | Permission to edit job roles |
| viewhist | View History | No | Permission to view the history page |
| viewparticipants | View Participants | No | Permission to view participant page |
| viewmodifiers | View Modifiers | No | Permission to view modifiers page |
| viewworkplan | View Workplan | No | Permission to view workplan page |
| pfilesummary | View policy file summary | No | Permission to view the policy file summary page |
| pfilebilling | View policy file billing | No | Permission to view the policy file billing page |
| pfilecontacts | View policy file contacts | No | Permission to view the policy file contacts page |
| pfiledetails | View policy file details | No | Permission to view the policy file details page |
| pfilepayments | View policy file payments | No | Permission to view the policy file payments page |
| pfilepricing | View policy file pricing | No | Permission to view the policy file pricing page |
| pfileworkorders | View policy file work orders | No | Permission to view the policy file work orders page |
| jobcopy | Copy job | No | Permission to copy a job |
| nottakensubmission | Flag submission as not-taken | No | Permission to flag a submission as not-taken |
| searchaccounts | Search accounts | No | Permission to search accounts |
| searchactivities | Search activities | No | Permission to search activities |
| searchcontacts | Search related contacts | No | Permission to search contacts related to the user |
| searchpols | Search related policies | No | Permission to search active/in-force policies related to the user |
| searchprodcodes | Search producer codes | No | Permission to search producer codes |
| createmanualuwissue | Create manual uw issue | No | Permission to create manual uw issues |
| viewprerenewal | View pre-renewal | No | Permission to view pre-renewal |
| editprerenewal | Edit pre-renewal | No | Permission to edit pre-renewal |
| editnonrenewexp | Edit non-renew explanation | No | Permission to edit non-renew explanation |
| selectnonrenew | Select non-renew as a pre-renewal direction | No | Permission to select non-renew as a pre-renewal direction |
| editautosymbol | Edit covered auto symbols | No | Edit covered auto symbols |
| createreferralreason | Create referral reason | No | Create referral reason |
| reviseaudit | Revise audit | No | Revise audit |
| startaudit | Start audit job | No | Permission to start an audit |
| rescheduleaudit | Reschedule audit | No | Permission to change the dates of an audit |
| completeaudit | Complete audit | No | Permission to complete audits |
| advanceaudit | Advance audit | No | Permission to advance audits |
| editaudit | Edit audit | No | Permission to edit audits |
| waiveaudit | Waive audit | No | Permission to waive an audit |
| viewaudit | View audit | No | Permission to view an audit |
| reverseaudit | Reverse audit | No | Permission to manually reverse an audit |
| createaudit | Create audit | No | Permission to create an ad-hoc audit |
| viewclaimsystem | View claim system | No | Permission to see the hyperlink to claim system |
| viewrestrictedclaim | View restricted claim | No | Permission to see the hyperlink to restricted claim in claim system |
| overridebilling | Override Billing | No | Permission to override billing behaviors |
| viewriskrefreasons | View risk analysis referral reasons | No | Permission to view referral reasons |
| viewriskevalissues | View risk analysis UW issues | No | Permission to view UW issues |
| viewriskclaims | View risk analysis claims | No | Permission to view claims |
| viewriskpriorpolicies | View risk analysis prior policies | No | Permission to view prior policies |
| viewriskpriorlosses | View risk analysis prior losses | No | Permission to view prior losses |
| price | Manually price policy | Yes | Permission to manually price a policy |
| cancwizdocs | View cancellation wizard documents | Yes | Permission to view the cancellation wizard documents page |
| cancwizhist | View cancellation wizard history | Yes | Permission to view the cancellation history page |
| cancwizroles | View cancellation wizard job roles | Yes | Permission to view the cancellation wizard job roles page |
| cancwiznotes | View cancellation wizard notes | Yes | Permission to view the cancellation wizard notes page |
| cancwizpriorhist | View cancellation wizard prior history | Yes | Permission to view the cancellation wizard prior history page |
| cancwizrateinputs | View cancellation wizard rating inputs | Yes | Permission to view the cancellation wizard rating inputs page |
| cancwizrisk | View cancellation wizard risk analysis | Yes | Permission to view the cancellation wizard risk analysis page |
| cancwizriskhist | View cancellation wizard risk history | Yes | Permission to view the cancellation wizard risk history page |
| cancwizworkplan | View cancellation wizard workplan | Yes | Permission to view the cancellation wizard workplan page |
| pchgwizdocs | View policy change wizard documents | Yes | Permission to view the policy change wizard documents page |
| pchgwizhist | View policy change wizard history | Yes | Permission to view the policy change history page |
| pchgwizroles | View policy change wizard job roles | Yes | Permission to view the policy change wizard job roles page |
| pchgwiznotes | View policy change wizard notes | Yes | Permission to view the policy change wizard notes page |
| pchgwizpriorhist | View policy change wizard prior history | Yes | Permission to view the policy change wizard prior history page |
| pchgwizrateinputs | View policy change wizard rating inputs | Yes | Permission to view the policy change wizard rating inputs page |
| pchgwizrisk | View policy change wizard risk analysis | Yes | Permission to view the policy change wizard risk analysis page |
| pchgwizriskhist | View policy change wizard risk history | Yes | Permission to view the policy change wizard risk history page |
| pchgwizworkplan | View policy change wizard workplan | Yes | Permission to view the policy change wizard workplan page |
| reinwizdocs | View reinstatement wizard documents | Yes | Permission to view the reinstatement wizard documents page |
| reinwizhist | View reinstatement wizard history | Yes | Permission to view the reinstatement history page |
| reinwizroles | View reinstatement wizard job roles | Yes | Permission to view the reinstatement wizard job roles page |
| reinwiznotes | View reinstatement wizard notes | Yes | Permission to view the reinstatement wizard notes page |
| reinwizpriorhist | View reinstatement wizard prior history | Yes | Permission to view the reinstatement wizard prior history page |
| reinwizrateinputs | View reinstatement wizard rating inputs | Yes | Permission to view the reinstatement wizard rating inputs page |
| reinwizrisk | View reinstatement wizard risk analysis | Yes | Permission to view the reinstatement wizard risk analysis page |
| reinwizriskhist | View reinstatement wizard risk history | Yes | Permission to view the reinstatement wizard risk history page |
| reinwizworkplan | View reinstatement wizard workplan | Yes | Permission to view the reinstatement wizard workplan page |
| rnwlwizdocs | View renewal wizard documents | Yes | Permission to view the renewal wizard documents page |
| rnwlwizhist | View renewal wizard history | Yes | Permission to view the renewal history page |
| rnwlwizroles | View renewal wizard job roles | Yes | Permission to view the renewal wizard job roles page |
| rnwlwiznotes | View renewal wizard notes | Yes | Permission to view the renewal wizard notes page |
| rnwlwizpriorhist | View renewal wizard prior history | Yes | Permission to view the renewal wizard prior history page |
| rnwlwizrateinputs | View renewal wizard rating inputs | Yes | Permission to view the renewal wizard rating inputs page |
| rnwlwizrisk | View renewal wizard risk analysis | Yes | Permission to view the renewal wizard risk analysis page |
| rnwlwizriskhist | View renewal wizard risk history | Yes | Permission to view the renewal wizard risk history page |
| rnwlwizworkplan | View renewal wizard workplan | Yes | Permission to view the renewal wizard workplan page |
| rewrwizdocs | View rewrite wizard documents | Yes | Permission to view the rewrite wizard documents page |
| rewrwizhist | View rewrite wizard history | Yes | Permission to view the rewrite wizard history page |
| rewrwizroles | View rewrite wizard job roles | Yes | Permission to view the rewrite wizard job roles page |
| rewrwiznotes | View rewrite wizard notes | Yes | Permission to view the rewrite wizard notes page |
| rewrwizpriorhist | View rewrite wizard prior history | Yes | Permission to view the rewrite wizard prior history page |
| rewrwizrateinputs | View rewrite wizard rating inputs | Yes | Permission to view the rewrite wizard rating inputs page |
| rewrwizrisk | View rewrite wizard risk analysis | Yes | Permission to view the rewrite wizard risk analysis page |
| rewrwizriskhist | View rewrite wizard risk history | Yes | Permission to view the rewrite wizard risk history page |
| rewrwizworkplan | View rewrite wizard workplan | Yes | Permission to view the rewrite wizard workplan page |
| subwizdocs | View submission wizard documents | Yes | Permission to view the submission wizard documents page |
| subwizhist | View submission wizard history | Yes | Permission to view the submission wizard history page |
| subwizroles | View submission wizard job roles | Yes | Permission to view the submission wizard job roles page |
| subwiznotes | View submission wizard notes | Yes | Permission to view the submission wizard notes page |
| subwizpriorhist | View submission wizard prior history | Yes | Permission to view the submission wizard prior history page |
| subwizrateinputs | View submission wizard rating inputs | Yes | Permission to view the submission wizard rating inputs page |
| subwizrisk | View submission wizard risk analysis | Yes | Permission to view the submission wizard risk analysis page |
| subwizriskhist | View submission wizard risk history | Yes | Permission to view the submission wizard risk history page |
| subwizworkplan | View submission wizard workplan | Yes | Permission to view the submission wizard workplan page |
| accountpremloss | View account file premiums losses | Yes | Permission to view account file premiums losses page |
| pfileclaims | View policy file claims | Yes | Permission to view the policy file claims page |
| pfiledocs | View policy file documents | Yes | Permission to view the policy file documents page |
| pfilenotes | View policy file notes | Yes | Permission to view the policy file notes page |
| pfilerateinputs | View policy file rating inputs | Yes | Permission to view the policy file rating inputs page |
| pfileroles | View policy file participants | Yes | Permission to view the policy file partipants page page |
| pfilepriorhist | View policy file prior history | Yes | Permission to view the policy file prior history page |
| pfileriskeval | View policy file risk evaluation | Yes | Permission to view the policy file risk evaluation page |
| declinepolchange | Decline policy change | Yes | Permission to decline a policy change |
| splitpolicy | Split or Spin Policies | No | Permission to divide (split or spin) policies into other submissions |
| mergeaccounts | Merge Accounts | No | Permission to move all information from one account to another and delete the irrelevant one |
| viewbillingsystem | View billing system | No | Permission to see the hyperlink to billing system |
| userroleassignmentbulkassign | Reassign roles bulk | No | Permission to reassign bulk role assignments on jobs or policies. |
| restorefromarchive | Retrieve from archive | No | Permission to retrieve a policy period from the archive. |
| editrateasofdate | Edit Rate as of Date | No | Permission to view and edit the Rate as of Date |
| ratebookview | View rate books and tables | No | Permission to view rate books and tables. |
| ratebookedit | Edit rate books and tables | No | Permission to add and edit rate books and tables. |
| ratebookapprove | Approve rate books and tables | No | Permission to approve and activate rate books. |
| bulkpolicyratingtest | Rate policies in bulk for rating impact analysis | Yes | Permission to rate policies in bulk for rating impact analysis |
| rateimpacttesting | Rate policies for rate impact testing | No | Permission to rate policies for rate impact testing |
| ratingworksheetview | View rating worksheet | No | Permission to view rating worksheets. |
| exportmasksmanage | Manage export masks | No | Permission to create, edit, or delete export masks |
| affinitygroupadmin | Affinity Group Administration | No | Permission to administer Affinity Groups |
| updateprodcodes | Producer Code Update | No | Permission to update producer code |

---

### Typelist: SystemUserType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\SystemUserType.tti`
**Description:** Types of special system users
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| sysadmin | system administrator | No | The system administrator |
| defaultowner | default owner | No | A special user that accepts failed or unresolved assignments |
| sysservices | system services | No | A daemon user that executes system services like escalation |

---

### Typelist: TableUpdateStatsType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\TableUpdateStatsType.tti`
**Description:** Type of process running update statistics
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Table | Table | No | Table Update Statistics Statements |
| Index | Index | No | Index Update Statistics Statements |
| Histogram | Histogram | No | Histogram Update Statistics Statements |

---

### Typelist: TaxFilingStatusType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\TaxFilingStatusType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\TaxFilingStatusType.ttx`
**Description:** State-specific field
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| MarriedJoint | Married/filing jointly | No | Married/filing jointly |
| MarriedSep | Married/filing separately | No | Married/filing separately |
| Single | Single | No | Single |
| SingleHH | Single/Head of household | No | Single/Head of household |
| Widow | Qualifying widow(er) with dependent child | No | Qualifying widow(er) with dependent child |

---

### Typelist: TaxStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\TaxStatus.tti`
**Description:** The status of a vendor's tax ID
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| unknown | Unknown | No | Unknown |
| unconfirmed | Unconfirmed | No | Known, but not yet verified |
| confirmed | Confirmed | No | Known and verified |

---

### Typelist: TeamStatsRecordType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\TeamStatsRecordType.tti`
**Description:** TeamStatsRecordType
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| user | User | No | Record with statistical data for a user |
| group | Group | No | Record with aggregated statistical data for a group |
| misassigned | Misassigned | No | Record with aggregated statistical data for non-member, unknown, or system users |
| inqueue | InQueue | No | Record with aggregated statistical data for per-group queued activities |

---

### Typelist: TeamStatsType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\TeamStatsType.tti`
**Description:** TeamStatsType
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| ByActivity | By Activity | No | Statistics calculated by assigned activity |
| ByRole | By Role | No | Statistics calculated by user role |

---

### Typelist: TermType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\TermType.tti`
**Description:** Policy term types
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Annual | Annual | No | year term |
| HalfYear | 6 months | No | 6 month term |
| Other | Other | No | Other term |

---

### Typelist: TerritoryDefinition

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\TerritoryDefinition.tti`
**Description:** TerritoryDefinition
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| WorldExcludingNamed | World, Excluding Named | No | World, Excluding Named |
| Worldwide | Worldwide | No | Worldwide |
| AdditionalNamedCountries | AdditionalNamedCountries | No | Additional Named Countries |

---

### Typelist: TestOnlyType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\TestOnlyType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\TestOnlyType.ttx`
**Description:** Test-only typelist
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| code0 | Code 0 | Yes | Code 0 (red) |
| code1 | Code 1 | No | Code 1 (red) |
| code2 | Code 2 | No | Code 2 (red) |
| code3 | Code 3 | No | Code 3 (green-blue) |
| code4 | Code 4 | No | Code 4 |
| code5 | Code 5 | Yes | Code 5 (green) |
| code6 | Code 6 | No | Code 6 (green) |
| code7 | Code 7 | No | Code 7 (green) |
| code8 | Code 8 | No | Code 8 (red-blue) |
| code9 | Code 9 | No | Code 9 |
| code10 | Code 10 | Yes | Code 10 (blue) |
| code11 | Code 11 | No | Code 11 (blue) |
| code12 | Code 12 | No | Code 12 (blue) |
| code13 | Code 13 | No | Code 13 (red-green) |
| code14 | Code 14 | No | Code 14 |
| code15 | Code 15 | Yes | Code 15 (Color_retired) |
| code16 | Code 16 | No | Code 16 (Color_retired) |
| code17 | Code 17 | No | Code 17 (Color_retired) |
| code18 | Code 18 | No | Code 18 (red-green-blue) |
| code19 | Code 19 | No | Code 19 |

---

### Typelist: Tier

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\Tier.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\Tier.ttx`
**Description:** The tier of the organization
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| silver | Silver | No | Silver |
| gold | Gold | No | Gold |
| bronze | Bronze | No | Bronze |

---

### Typelist: TimeZoneType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\TimeZoneType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\TimeZoneType.ttx`
**Description:** Users' time zones
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| US.Eastern | Eastern Time (Eastern) | No | GMT -05:00 |
| US.East-Indiana | Eastern Time (East-Indiana) | No | GMT -05:00 |
| US.Central | Central Time (Central) | No | GMT -06:00 |
| US.Mountain | Mountain Time (Mountain) | No | GMT -07:00 |
| US.Arizona | Mountain Time (Arizona) | No | GMT -07:00 |
| US.Pacific | Pacific Time (Pacific) | No | GMT -08:00 |
| US.Alaska | Alaska Time (Alaska) | No | GMT -09:00 |
| US.Hawaii | Hawaii Time (Hawaii) | No | GMT -10:00 |
| US.Aleutian | Hawaii-Aleutian Time (Aleutian) | No | GMT -10:00 |

---

### Typelist: TrainingClassType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\TrainingClassType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\TrainingClassType.ttx`
**Description:** The type of training a driver has undergone.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| DriversTraining | Driver's Training | No | the driver has completed a Driver's Training course |
| MatureDriversTraining | Mature Driver's Training | No | the driver has completed a Mature Driver's Training course |

---

### Typelist: TriggeringPointKey

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\TriggeringPointKey.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\TriggeringPointKey.ttx`
**Description:** Unique key identifying a TriggeringPoint, used when invoking Business Rules
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Reinsurance | Reinsurance | No | Triggers at Reinsurance |
| UWHold | UWHold | No | Triggers at UWHold |
| RegulatoryHold | RegulatoryHold | No | Triggers at RegulatoryHold |
| MVR | MVR | No | Triggers at MVR |

---

### Typelist: TypeOfSupplementalRpting

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\TypeOfSupplementalRpting.tti`
**Description:** TypeOfSupplementalRpting
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Broad | Broad | No | Broad |
| Detail | Detail | No | Detail |

---

### Typelist: ULCovTermUseType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ULCovTermUseType.tti`
**Description:** UnderlyingCoverage Term Use Type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Direct | Direct | No | Direct user entered Value |
| Option | Option | No | Single selectable option |
| Package | Package | No | Selectable Package (set) of options |
| Reference | Reference | No | Reference to an existing CovTermPattern |

---

### Typelist: ULGradeType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ULGradeType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\ULGradeType.ttx`
**Description:** UL Grade type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Default | Default | No | Default |

---

### Typelist: UnitOfDistance

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\UnitOfDistance.tti`
**Description:** Units of distance
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Mile | Mile | No | International statute mile |
| Kilometer | Kilometer | No | Kilometer |
| Meter | Meter | No | Meter |
| Foot | Foot | No | Foot |

---

### Typelist: UpFrontPaymentMethod

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\UpFrontPaymentMethod.tti`
**Description:** UpFrontPaymentMethod
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| notcollected | Not Collected | No | Not Collected |
| check | Check | No | Check |
| cash | Cash | No | Cash |
| electronic | Electronic | No | Electronic |
| agent | Agent | No | The payment is collected by the Agent |

---

### Typelist: UpgradeDBStorageSetType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\UpgradeDBStorageSetType.tti`
**Description:** Types of database storage sets persited before and after an upgrade
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| sqlserverdatabase | SQL Server database | No | Storage info for a SQL Server database |
| sqlserverdataspace | SQL Server database dataspace | No | Storage info for a SQL Server database dataspace |
| sqlservertempdb | SQL Server database tempdb | No | Storage info for a SQL Server database tempdb |
| sqlservertablesindexes | SQL Server database tables and indexes | No | Storage info for a SQL Server database tables and indexes |
| oracletablespacedef | Oracle tablespace storage definition | No | Tablespace storage definitions for Oracle |
| oracletablesdef | Oracle tables storage definition | No | Table Storage definitions for Oracle |
| oracleindexesdef | Oracle indexes storage definition | No | Indexes storage definitions for Oracle |
| oraclelobsdef | Oracle LOB storage definition | No | LOB storage info for Oracle |
| oracletablespace | Oracle tablespaces | No | Storage info for Oracle tablespaces |
| oracletables | Oracle tables | No | Storage info for Oracle tables |
| oracleindexes | Oracle indexes | No | Storage info for Oracle indexes |
| oraclelobs | Oracle LOBs | No | Storage info for Oracle LOBs |

---

### Typelist: UpgradeExecutionTimeType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\UpgradeExecutionTimeType.tti`
**Description:** Types of upgrade execution times
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| bootstrap | Bootstrap | No | Bootstrap |
| syncindexes | Sync indexes | Yes | Sync indexes |
| checkdbstate | Check database state | No | Check database state for disabled constraints, etc. |
| prerowcounts | Capture row counts before upgrade | No | Capture row counts before upgrade |
| dbparameters | Persist database parameters | No | Persist database parameters |
| dbspacebefore | Capture database space before | No | Capture database space info before upgrade |
| customversionchecks | Customer Version Checks | No | Execute customer checks to determine whether to proceed with upgrade |
| custompreupgrade | Customer Pre-Upgrade version triggers | No | Execute customer pre-upgrade steps defined in IDatamodelUpgrade plugin |
| versionchecks | Version Checks | No | Execute checks to determine whether to proceed with upgrade |
| vtbeforeschemadiff | Execute VersionTriggers before schema diff | No | Execute VersionTriggers before schema diff |
| orphanedtypecodes | Verify no references to orphaned type codes | No | Verify no references to orphaned type codes |
| encryptdecrypt | Encrypt or decrypt existing data | No | Encrypt or decrypt existing data |
| gensteps | Generate steps | No | Generate steps |
| executesteps | Execute steps | No | Execute steps |
| vtafterschemadiff | VersionTriggers after schema diff | No | VersionTriggers after schema diff |
| custompostupgrade | Customer Post-Upgrade version triggers | No | Execute customer post-upgrade steps defined in IDatamodelUpgrade plugin |
| snapshotdatamodel | Capture snapshot of datamodel for archiving | No | Capture snapshot of datamodel for archiving |
| cleanup | Clean up | No | Clean up |
| copytoshadowtables | Copy contents to shadow tables | Yes | Copy contents of source tables to shadow tables |
| postrowcounts | Capture row counts after upgrade | No | Capture row counts after upgrade |
| dbspaceafter | Capture database space after | No | Capture database space info after upgrade |
| verifyschema | Verify schema | No | Verify schema |

---

### Typelist: UserAttributeType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\UserAttributeType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\UserAttributeType.ttx`
**Description:** Major categories of attributes
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| default | Default | No | Default |
| Language | Language | No | Language |
| Account | Named Account | No | Named Account |
| Expertise | Expertise | No | Expertise |
| LOB | Line of Business | No | Line of Business |

---

### Typelist: UserExperienceType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\UserExperienceType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\UserExperienceType.ttx`
**Description:** Experience levels for users
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| low | Low | No | Novice |
| mid | Mid | No | Average |
| high | High | No | Expert |

---

### Typelist: UserRole

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\UserRole.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\UserRole.ttx`
**Description:** Roles users can have on an assignable object
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Auditor | Auditor | No | The user who will audit a policy. |
| AuditExaminer | Audit Examiner | No | The user who will examin an audit. |
| Creator | Creator | No | The creator of this job |
| CustomerRep | Customer Service Representative | No | Customer Service representative |
| InitialReferrer | Initial Referrer | No | Initial Referrer |
| PreRenewalOwner | Pre-Renewal Owner | No | Pre-Renewal owner |
| Producer | Producer | No | The user who can act on behalf of the policyholder for purposes of gathering relevant information or providing authorization. |
| Requestor | Requestor | No | Person who initiated a submission or other work order |
| Underwriter | Underwriter | No | An internal user, typically an underwriter, who has to oversee the job to completion. |
| UnderwriterAssist | Underwriter Assistant | No | Underwriter assistant |
| defaultassignmentrole | Default Assignment Role | No | A special assignment role that accepts failed or unresolved assignments |
| processor | Processor | No | Clerical person who is responsible for processing the work order |
| tech | Underwriting Technician | No | An underwriting assistant who handles common underwriting tasks |
| loss_control | Loss Control | No | Person who inspects risks and advises underwriting of issues |
| relateduser | Related user | No | Miscellaneous related user |

---

### Typelist: UserRoleConstraint

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\UserRoleConstraint.tti`
**Description:** Constraints that can be applied to UserRoles
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| objectowner | ObjectOwner | No | Indicates that the user assigned to this role must have the same permissions that are required to be the owner of the assignable object. |

---

### Typelist: UserType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\UserType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\UserType.ttx`
**Description:** Types of normal system users
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| producer | Producer | No | An external producer. |
| assistant | Producer Assistant | No | Assistant for an external producer. |
| underwriter | Underwriter | No | An underwriter. |
| other | Other | No | Other. |
| auditor | Auditor | No | An auditor |

---

### Typelist: UserTypeCategory

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\UserTypeCategory.tti`
**Description:** The category that the user type belongs to.
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| internal | Internal | No | Internal category. |
| external | External | No | External category. |

---

### Typelist: UWApprovalDurationType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\UWApprovalDurationType.tti`
**Description:** The length the uw approval is valid.
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| NextChange | Next Change | No | Valid until next change. |
| EndOfTerm | End Of Term | No | Valid until end of term. |
| OneYear | One Year | No | Valid for one year from the effective date of the current job. |
| ThreeYears | Three Years | No | Valid for three years from the effective date of the current job |
| Rescinded | Rescinded | No | Valid until rescinded. |

---

### Typelist: UWCompanyCode

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\UWCompanyCode.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\UWCompanyCode.ttx`
**Description:** A code for an underwriting company
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| default | Default | No | Default underwriting company |
| 1111_11111 | Acme Low Hazard Insurance | No |  |
| 2111_11111 | Acme Medium Hazard Insurance | No |  |
| 3111_33333 | Acme High Hazard Insurance | No |  |
| 4111_44444 | Four Corners Low Hazard Casualty | No |  |
| 5666_55555 | Four Corners Medium Hazard Casualty | No |  |
| 6666_66666 | Four Corners High Hazard Casualty | No |  |
| 7777_12345 | FifthWheel Low Hazard Insurance | No |  |
| 7777_23211 | FifthWheel Medium Hazard Insurance | No |  |
| 9000_00001 | FifthWheel High Hazard Insurance | No |  |

---

### Typelist: UWCompanyStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\UWCompanyStatus.tti`
**Description:** Underwriting Company Status
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Active | Active | No | Active |
| Retired | Retired | No | Retired |
| Other | Other | No | Other |

---

### Typelist: UWIssueBlockingPoint

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\UWIssueBlockingPoint.tti`
**Description:** The points at which a UWIssue can block progress of a job.  When checking against a particular blocking point, any issues with a higher priority will be considered to also block, i.e. issues that block at quote will also block at bind.  NonBlocking must always remain at priority 0.
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Rejected | Rejected | No | Indicates that an issue has been rejected. |
| BlocksQuote | Blocks Quote | No | Indicates that an issue will prevent quoting the PolicyPeriod. |
| BlocksRateRelease | Blocks Rate Release | No | Indicates that an issue will prevent releasing a PolicyPeriod rate. |
| BlocksQuoteRelease | Blocks Quote Release | No | Indicates that an issue will prevent releasing a PolicyPeriod quote. |
| BlocksBind | Blocks Bind | No | Indicates that an issue will prevent binding the PolicyPeriod. |
| BlocksIssuance | Blocks Issuance | No | Indicates that an issue will prevent issuing the PolicyPeriod. |
| NonBlocking | Non-Blocking | No | Indicates that an issue will not block progress and is merely informational. |

---

### Typelist: UWIssueCheckingSet

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\UWIssueCheckingSet.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\UWIssueCheckingSet.ttx`
**Description:** Sets of UWIssues which are generated (or re-generated) at the same time. When rule sets are run for a checking set, an issue which is not regenerated is assumed to no longer apply.
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| PreQuote | Quote Issues | No | Created before quoting. |
| PreRateRelease | Rate Release Issues | No | Created before releasing a rate. |
| PreQuoteRelease | Quote Release Issues | No | Created before releasing a quote. |
| PreBind | Bind Issues | No | Created before binding. |
| PreIssuance | Issuance Issues | No | Created before issuance. |
| Referral | Referral | No | Created from an UW referral reason. |
| Question | Question | No | Created automatically from a Question. |
| Renewal | Renewal | No | Created as part of renewal processing. |
| Manual | Manual | No | Created manually. |
| Upgrade | Upgrade | No | Created during DB upgrade. |
| All | All | No | Checked at every blocking point. |
| PolicyRenewalAPI | PolicyRenewalAPI | No | Created during PolicyRenewalAPI execution |
| UWHold | Underwriting Hold | No | Created for underwriting holds |
| RegulatoryHold | Regulatory Hold | No | Created for regulatory holds |
| MVR | MVR Issues | No | Checks at PreQuote and PreBind for MVR issues |
| Reinsurance | Reinsurance | No | Checks for reinsurance issues, done at each stage after PreQuote |

---

### Typelist: UWIssueHistoryStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\UWIssueHistoryStatus.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\UWIssueHistoryStatus.ttx`
**Description:** The historical status of an UW issue after some action affecting its approval.
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Created | Created | No | The issue was created. |
| Approved | Approved | No | The issue was approved. |
| Rejected | Rejected | No | The issue was rejected. |
| Reopened | Reopened | No | The issue was reopened (without specifying an issue blocking point after). |
| Removed | Issue no longer applies | No | The issue was removed (e.g., by the issue evaluation rules). |
| Expired | Expired | No | The issue approval expired. |
| ChangeEffDate | Change Effective Date | No | The effective date of the issue was changed. |

---

### Typelist: UWReferralReasonStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\UWReferralReasonStatus.tti`
**Description:** Status of a UWReferralReason
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Open | Open | No | Referral reason is still open |
| Closed | Closed | No | Referral reason has been closed/resolved |

---

### Typelist: UWRuleAvailability

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\UWRuleAvailability.tti`
**Description:** Underwriting rule availability options
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| All | All | No | All |
| Available | Available | No | Available |
| Unavailable | Unavailable | No | Unavailable |
| Valid | Passing Validation | No | Rules passing validation |
| Invalid | Failing Validation | No | Rules that fail validation |

---

### Typelist: UWValueAssignmentType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\UWValueAssignmentType.tti`
**Description:** Specifies the way in which a default value is assigned to the "Reference Value"
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Fixed | Fixed | No | Indicates that the default value for the approval is copied directly from the issue |
| OffsetAmount | Offset Amount | No | A fixed amount is added to or subtracted from the issue's reference value to compute a default for the approval |
| OffsetPercent | Offset Percentage | No | The issue's reference value is increased or decreased by a percentage amount, depending on the direction of the comparator |

---

### Typelist: VacationStatusType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\VacationStatusType.tti`
**Description:** Possible vacation statuses for a user
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| atwork | At work | No | The user is at work |
| onvacation | On vacation | No | The user is on vacation |
| inactive | On vacation (Inactive) | No | The user is not available |

---

### Typelist: ValidationIssueType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ValidationIssueType.tti`
**Description:** Validation issues can be errors or warning
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| error | Error | No | A validation error |
| warning | Warning | No | A validation warning |

---

### Typelist: ValidationLevel

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ValidationLevel.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\ValidationLevel.ttx`
**Description:** Levels of validation errors and warnings
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| loadsave | Load and save | No | Minimum level that must be passed for a PolicyPeriod to be committed to the database |
| default | Default | No | Default validation level in the application UI and validate-on-commit |
| quotable | Quotable | No | Ready to be quoted |
| bindable | Bindable | No | Bind a Policy |
| readyforissue | Ready for issue | No | Ready for issue |
| quickquotable | Quick Quotable | No | Ready to be Quick Quoted |

---

### Typelist: ValuationMethod

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ValuationMethod.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\ValuationMethod.ttx`
**Description:** Types of valuation methods
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Appraisal | Appraisal | Yes | Appraisal |
| CompSale | Comparable sale | Yes | Comparable sale |
| SaleRec | Sales receipt | Yes | Sales receipt |
| ReplCost | Replacement cost | No | Replacement cost |
| ACV | Actual cash value | No | Actual cash value |
| FuncValue | Functional value | No | Functional value |
| AgreedAmt | Agreed amount | No | Agreed amount |
| ActCost | Actual cost | Yes | Actual cost |

---

### Typelist: ValueComparator

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ValueComparator.tti`
**Description:** Ways of comparing values of a common types
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| None | None | No | Value used to indicate that a given issue type has no associated value. |
| Any | Any | Yes | Value used to indicate that an authority grant is not contingent on a particular value. |
| Numeric_LE | At most | No | Value used to indicate that the issue value should be treated as a BigDecimal and must be less or equal to than the approval or grant value. |
| Numeric_GE | At least | No | Value used to indicate that the issue value should be treated as a BigDecimal and must be greater than or equal to the approval or grant value. |
| Monetary_LE | At most (monetary) | No | Value used to indicate that the issue value should be treated as a MonetaryAmount and must be less than or equal to the approval or grant value. |
| Monetary_GE | At least (monetary) | No | Value used to indicate that the issue value should be treated as a MonetaryAmount and must be greater than or equal to the approval or grant value. |
| State_Set | In set | No | Value used to indicate that the issue value should be treated as a (possibly-exclusive) set of States and the issue value must be contained (or not contained) within that set. |

---

### Typelist: ValueFormatterType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ValueFormatterType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\ValueFormatterType.ttx`
**Description:** Ways of formatting issue, approval, and grant value.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Unformatted | Unformatted | No | Formatter type where no formatting will be performed on the value. |
| Integer | Integer | No | Formatter type for integer values. |
| Units | Units | No | Formatter type for integer values of 'unit'. |
| Age | Age | No | Formatter type for ages. |
| Number | Number | No | Formatter type for BigDecimal values. |
| USD | USD | Yes | Formatter type for US dollar values (with cents). |
| USDBrief | USDBrief | Yes | Formatter type for US dollar values (without cents). |
| Currency | Currency | Yes | Formatter type the currency associated with the current locale. |
| StateSet | StateSet | No | Formatter type for sets of States. |
| MonetaryAmount | MonetaryAmount | No | Formatter used for MonetaryAmounts |
| TestFormatter | TestFormatter | Yes | Formatter used only for testing. |

---

### Typelist: ValueProvider

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ValueProvider.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\ValueProvider.ttx`
**Description:** ValueProvider
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| CoverageValueProvider | Coverage Value Provider | No | Provides Value for Coverage from a code |
| CovTermOptionValueProvider | Coverage Term Option Value Provider | No | Provides Value for Coverage Term Options from a code |
| CovTermValueProvider | Coverage Term Value Provider | No | Provides Value for Coverage Terms from a code |
| ReferenceFactorValueProvider | Reference Factor Value Provider | No | Provides Value for Reference Factors from a code |
| TermlessCoverageValueProvider | Termless Coverage Value Provider | No | Provides Value for Termless Coverages from a code |
| TypeListValueProvider | Typelist Value Provider | No | Provides Value from a typelist |

---

### Typelist: VehicleIndustry

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\VehicleIndustry.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\VehicleIndustry.ttx`
**Description:** Vehicle industry
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Truckers | Haulers | No | Haulers |
| Food | Comestibles | No | Comestibles |
| Special | Delivery - NOC | No | Delivery - NOC |
| Waste | Refuse/Recycling | No | Refuse/Recycling |
| Farmers | Agriculture | No | Agriculture |
| Dump | Aggregate & Dumping | No | Aggregate & Dumping |
| Contractors | Construction | No | Construction |
| NOC | N.O.C | No | N.O.C |

---

### Typelist: VehicleIndustryUse

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\VehicleIndustryUse.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\VehicleIndustryUse.ttx`
**Description:** Vehicle industry use
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| commoncarrier | Hauler - Common | No | Hauler - Common |
| contractother | Hauler - Contract | No | Hauler - Contract |
| contractchemical | Hauler - Contract, Hazmat | No | Hauler - Contract, Hazmat |
| contractiron | Hauler - Contract, Steel | No | Hauler - Contract, Steel |
| exemptother | Hauler - Exempt NOC | No | Hauler - Exempt NOC |
| exemptlivestock | Hauler - Exempt - Livestock | No | Hauler - Exempt - Livestock |
| transportcarrier | Hauler - For Hire | No | Hauler - For Hire |
| towtrucks | Tow Trucks - For Hire | No | Tow Trucks for Hire |
| carriersother | Hauler - NOC | No | Hauler - NOC |
| canneries | Food - Canning/Packing | No | Food - Canning/Packing |
| fishseafood | Food - Seafood | No | Food - Seafood |
| frozenfood | Food - Frozen | No | Food - Frozen |
| fruitvegetable | Food - Produce | No | Food - Produce |
| meatpoultry | Food - Meat/Poultry | No | Food - Meat/Poultry |
| foodother | Food - NOC | No | Food - NOC |
| armoredcars | Delivery - Armored Transport | No | Delivery - Armored Transport |
| filmdelivery | Delivery - Film | No | Delivery - Film |
| magazinesnewspapers | Delivery - Periodicals | No | Delivery - Periodicals |
| mailparcel | Delivery - Mail and Parcels | No | Delivery - Mail and Parcels |
| specialallother | Delivery - NOC | No | Delivery - NOC |
| autodismantlers | Auto Dismantlers | No | Auto Dismantlers |
| buildingwrecking | Hauler - Construction Debris | No | Hauler - Construction Debris |
| garbage | Hauler - Refuse/Recycling | No | Hauler - Refuse/Recycling |
| junkdealers | Junk Dealers | No | Junk Dealers |
| wasteother | Hauler - Waste NOC | No | Hauler - Waste NOC |
| livestock | Hauler - Livestock | No | Hauler - Livestock |
| farmersother | Agriculture - NOC | No | Agriculture - NOC |
| dumpexcavating | Excavating - NOC | No | Excavating - NOC |
| sandgravel | Aggregates - Not Quarry | No | Aggregates - Not Quarry |
| mining | Mining | No | Mining |
| quarrying | Quarrying | No | Quarrying |
| dumpother | Dump- NOC | No | Dump- NOC |
| buildingcommercial | Construction -  Commercial | No | Construction -  Commercial |
| buildingprivate | Construction - Residential | No | Construction - Residential |
| electricalplumbing | Construction - Artisan | No | Construction - Artisan |
| contractorexcavating | Construction - UG | No | Construction - UG |
| streetroad | Construction - Street and Road | No | Construction - Street and Road |
| contractorsother | Construction - NOC | No | Construction - NOC |
| notspeclogging | Logging - NOC | No | Logging - NOC |
| notspecother | NOC | No | NOC |
| individualfamily | Individually Owned or Family Corp. | No | Individually Owned or Family Corp.- Other than Livestock Hauling |

---

### Typelist: VehicleOwnership

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\VehicleOwnership.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\VehicleOwnership.ttx`
**Description:** Vehicle Ownership
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Owned | Owned | No | Owned vehicles |
| NonOwned | Non-owned | No | Non-owned vehicles |
| Leased | Leased | No | Leased vehicles |

---

### Typelist: VehiclePrimaryUse

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\VehiclePrimaryUse.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\VehiclePrimaryUse.ttx`
**Description:** Vehicle Primary Use
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| business | Business | No | Business |
| pleasure | Pleasure | No | Pleasure |
| commuting | Commuting/School | No | Commuting/School |
| mixed | Business+Pleasure | No | Business+Pleasure |
| Commercial | Business, NOC | No | Business, NOC |
| Retail | Customer Delivery | No | Customer Delivery |
| Service | Trades | No | Trades |
| OwnerDrivenTaxi | Livery-Owner Operated | No | Livery-Owner Operated |
| RentedLeasedTaxi | Livery-Driver Leased | No | Livery-Driver Leased |
| Taxicab | Taxi cab | No | Taxi cab |
| Limousine | Limousine | No | Limousine |
| CarService | Car service | No | Car service |
| UrbanBus | Bus - Metro Ops Only | No | Bus - Metro Ops Only |
| EmployerFurnishedVan | Vanpool - Employer | No | Vanpool - Employer |
| OtherVan | Van - NOC | No | Van - NOC |
| AirportBusLimo | Bus / Shuttle - Airport | No | Bus / Shuttle - Airport |
| InterCityBus | Bus - Intercit | No | Bus - Intercity |
| CharterBus | Bus - Charter | No | Bus - Charter |
| SightseeingBus | Bus - Sightseeing | No | Bus - Sightseeing |
| AthleteEntertainer | Bus - athletes and entertainers | No | Bus - athletes and entertainers |
| OtherBus | Bus - NOC | No | Bus - NOC |
| ChurchBus | Bus - Church | No | Bus - Church |
| DistrictOwnedSchoolBus | Bus - Public School | No | Bus - Public School |
| OtherSchoolBus | Bus - Other School | No | Bus - Other School |
| SSA_Emp | Soc. Service - employee | No | Soc. Service - employee |
| SSA_Other | Soc. Service, NOC | No | Soc. Service, NOC |
| FarmLaborIncPassHaz | Farm Labor - Incl Passengers | No | Farm Labor - Incl Passengers |
| FarmLaborExcPassHaz | Farm Labor - Excl Passengers | No | Farm Labor - Excl Passengers |
| RentalTruck | Rental - Truck | No | Rental - Truck |
| RentalTractor | Rental - Tractor | No | Rental - Tractor |
| RentalTrailer | Rental - Trailer | No | Rental - Trailer |
| RentalPPAuto | Rental - Passenger vehicle | No | Rental - Passenger vehicle |
| RentalMotorHome | Rental - RV | No | Rental - RV |
| RentalMisc | Rental - NOC | No | Rental - NOC |
| LeasingContingentCov | Leasing - Excess Cov | No | Leasing - Excess Cov |
| FireDepartmentPP | FD - Passenger vehicles | No | FD - Passenger vehicles |
| FireDepartmentOther | FD - NOC | No | FD - NOC |
| LawEnforcementPP | PD - Passenger vehicles | No | PD - Passenger vehicles |
| LawEnforcementOther | PD - NOC | No | PD - NOC |
| FuneralLimousine | Funeral - Limo | No | Funeral - Limo |
| FuneralHearse | Funeral - NOC | No | Funeral - NOC |
| RepossessedAutomobile | Repossessed vehicle | No | Repossessed vehicle |
| DriverTraining | School - Driver Training | No | School - Driver Training |
| CommDrivingSchool | Commercial driving school | No | Commercial driving school |
| LawEnforcementMCycle | PD - motorcycle | No | PD - motorcycle |
| MobileHomeTrailorLQ | Mobile home | No | Mobile home |
| MobileHomeCamperBody | RV - pick up body | No | RV - pick up body |
| MobileHomeLess22Ft | RV - 22'+ | No | RV - 22'+ |
| MobileHomeGreater22Ft | RV - Under 22' | No | RV - Under 22' |
| Snowmobiles | Snowmobile | No | Snowmobile |
| GolfMobiles | Golf mobiles | No | Golf mobiles |
| Antique | Antique Vehicle | No | Antique Vehicle |
| BobtailOperation | Tractor w/o Trlr | No | Tractor w/o Trlr |
| AutoDeliveryPickUp | AutoDelivery | No | AutoDelivery |
| AmbulanceService | EMT | No | EMT |

---

### Typelist: VehicleSizeClass

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\VehicleSizeClass.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\VehicleSizeClass.ttx`
**Description:** Vehicle Size Class
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| LightTruck | Light truck | No | Light truck (0-10000 lbs. GVW) |
| MediumTruck | Medium truck | No | Medium truck (10,001-20,000 lbs. GVW) |
| HeavyTruck | Heavy truck | No | Light truck (20001-45000 lbs. GVW) |
| HeavyTruckTractor | Heavy truck-tractor | No | Heavy truck-tractor (0-45000 lbs. GCW) |
| ExtraHeavyTruck | Extra heavy truck | No | Extra heavy truck (over 45000 lbs. GVW) |
| ExtraHeavyTruckTractor | Extra heavy truck-tractor | No | Extra heavy truck-tractor (over 45000 lbs. GCW) |
| Semitrailer | Semitrailer | No | Semitrailer |
| Trailer | Trailer | No | Trailer |
| ServiceUtilityTrailer | Service or utility trailer | No | Service or utility trailer |
| 1-8 | 1 to 8 passenger | No | 1 to 8 |
| 9-20 | 9 to 20 passenger | No | 9 to 20 |
| 21-60 | 21 to 60 passenger | No | 21 to 60 |
| over60 | over 60 passenger | No | over 60 |
| 0-70CC | 0-70 CC | No | 0-70 CC |
| 71-100CC | 71-100 CC | No | 71-100 CC |
| 101-125CC | 101-125 CC | No | 101-125 CC |
| 126-200CC | 126-200 CC | No | 126-200 CC |
| 201-275CC | 201-275 CC | No | 201-275 CC |
| 276-350CC | 276-350 CC | No | 276-350 CC |
| 351-500CC | 351-500 CC | No | 351-500 CC |
| 501-650CC | 501-650 CC | No | 501-650 CC |
| over650CC | over 650 CC | No | over 650 CC |
| PrivatePassenger | Private passenger | No | Private passenger |

---

### Typelist: VehicleType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\VehicleType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\VehicleType.ttx`
**Description:** Vehicle Type
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Commercial | Trucks,Tractors,Trailers | No | Commercial - Non-passenger |
| PP | Passenger Vehicles | No | Passenger Vehicles |
| PublicTransport | Livery Vehicles | No | Livery Vehicles |
| Special | Special | No | Special |
| auto | Passenger/Light Truck | No | Passenger/Light Truck |
| other | Other | No | Other |

---

### Typelist: VendorType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\VendorType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\VendorType.ttx`
**Description:** Types of vendors
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| indautoinspector | Independent auto inspector | No | Independent auto inspector |
| indpropinspector | Independent property inspector | No | Independent property inspector |
| autorepair | Auto repair shop | No | Auto repair shop |
| autoglass | Auto glass shop | No | Auto glass shop |
| towingservice | Towing service | No | Towing service |
| autorental | Auto rental service | No | Auto rental service |
| bldingcontractor | Building contractor | No | Building contractor |
| fireinspector | Fire inspector | No | Fire inspector |
| defenseatt | Defense attorney | No | Defense attorney |
| plaintiffatt | Plaintiff attorney | No | Plaintiff attorney |
| doctor | Doctor | No | Doctor |
| hospital | Hospital | No | Hospital |
| insuranceagent | Insurance agent | No | Insurance agent |
| externaladjuster | External adjuster | No | External adjuster |
| nurse | Nurse | No | Nurse - for medical management and rehab |
| government | Government authority | No | Government authority |

---

### Typelist: VenueType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\VenueType.tti`
**Description:** The types of legal venues.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| County | County | No | County |
| State | State | No | State |
| Fed | Federal | No | Federal |
| Muni | Municipal | No | Municipal |
| WcAppeals | Workers' Comp Appeals Board | No | Workers' Comp Appeals Board |
| Supreme | Supreme Court | No | Supreme Court |
| ADR | Alternative dispute resolution | No | Alternative dispute resolution |
| StateSup | State Supreme Court | No | State Supreme Court |

---

### Typelist: VoluntaryComp

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\VoluntaryComp.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\VoluntaryComp.ttx`
**Description:** Voluntary compensation type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| stat | State Act | No | State Act |
| uslh | U.S.L. & H. | No | U.S.L. & H. |

---

### Typelist: WaiverOfSubrogationType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\WaiverOfSubrogationType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\WaiverOfSubrogationType.ttx`
**Description:** The type of waiver of subro.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| blanket | Blanket | No | A blanket waiver of liability |
| specific | Specific | No | A specific waiver of liability |

---

### Typelist: WatchpersonSupervision

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\WatchpersonSupervision.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\WatchpersonSupervision.ttx`
**Description:** Type of supervision of the watchpersons
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| C2 | Central station signals every 2 hours | No | Central station signals every 2 hours |
| C3 | Central station signals every 3 hours | No | Central station signals every 3 hours |
| CH | Central station hourly registration | No | Central station hourly registration |
| CM | Central station signals more than every 3 hours | No | Central station signals more than every 3 hours |
| CS | Central station | No | Central station |
| H | Hourly clock registration | No | Hourly clock registration |
| N | Does not signal or register | No | Does not signal or register |
| OT | Other | No | Other |

---

### Typelist: WCClassCodeFederalDomains

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\WCClassCodeFederalDomains.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\WCClassCodeFederalDomains.ttx`
**Description:** A type of class code (FELA, Maritime, etc)
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Mari | WC Maritime | No | WC Maritime Act (Program I) codes |
| MariState | WC Maritime State | No | WC Maritime Act (Program II) codes |
| MariUSLH | WC Maritime USLH | No | WC Maritime Act (Program II) codes |
| FELA | WC FELA | No | WC FELA Act (Program I) codes |
| FELAState | WC FELA State | No | WC FELA Act (Program II) codes |
| FELAUSLH | WC FELA USLH | No | WC FELA Act (Program II) codes |

---

### Typelist: WCJurisdictionCostType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\WCJurisdictionCostType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\WCJurisdictionCostType.ttx`
**Description:** The type of a WC Jurisdiction Cost.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| MinPrem | Minimum Premium Adjustment | No | Additional premium charged so that standard premium for the policy or state meets a minimum amount |
| CancelShortRatePenalty | Cancellation short-rate penalty | No | Cancellation penalty determined by short-rate. |
| Tax | Tax | No | Tax |
| CIGA | CIGA surcharge | No | CA Insurance Guarantee Assoc surcharge |
| ExpenseConst | Expense constant | No | Expense constant |
| PremDis | Premium discount | No | Premium discount |
| TerrorPrem | Terrorism premium | No | Terrorism premium |
| SchedCredit | Schedule credit | No | Premium adjustment based on evaluation of the insured's risk relative to the average risk of others in the same class |
| Waiver | Waiver charge | No | Extra charge for waiver of subrogation |
| ExpMod | Experience modifier | No | Workers' comp experience modifier credit or debit |
| WCEL | Emp liab increased limits | No | Premium for workers' comp employers liability limits above the base (standard) amounts |

---

### Typelist: WCParticipatingPlanID

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\WCParticipatingPlanID.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\WCParticipatingPlanID.ttx`
**Description:** The type of WC participating plan.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 1ystd | 1Y-STD | No | One year standard |
| 2ystd | 2Y-STD | No | Two years standard |
| 3ystd | 3Y-STD | No | Three years standard |

---

### Typelist: Weekdays

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\Weekdays.tti`
**Description:** A list of weekdays
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Sunday | Sunday | No | Sunday |
| Monday | Monday | No | Monday |
| Tuesday | Tuesday | No | Tuesday |
| Wednesday | Wednesday | No | Wednesday |
| Thursday | Thursday | No | Thursday |
| Friday | Friday | No | Friday |
| Saturday | Saturday | No | Saturday |

---

### Typelist: WindRating

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\WindRating.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\WindRating.ttx`
**Description:** Wind rating
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| SC | Superior Construction | No | Superior Construction |
| WRC | Wind Resistive Construction | No | Wind Resistive Construction |
| SWRC | Semi Wind Resistive Construction | No | Semi Wind Resistive Construction |
| OC | Ordinary Construction | No | Ordinary Construction |

---

### Typelist: WindType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\WindType.tti`
**Description:** Wind type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| *(None defined)* | *Dynamic or database-driven* | No | Typelist populated dynamically at runtime or via database table |

---

### Typelist: WiringType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\WiringType.tti`
**Description:** Wiring Type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| copper | Copper | No | Copper Wiring |
| aluminum | Aluminum | No | Aluminum Wiring |
| KnobAndTube | Knob & Tube | No | Knob and Tube |

---

### Typelist: WorkerKind

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\WorkerKind.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\WorkerKind.ttx`
**Description:** What kind of worker?
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| farmag | Farm/agricultural | No | Farm or agricultural worker |
| domhos | Domestic/household | No | Domestic or household Worker |

---

### Typelist: WorkflowActionType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\WorkflowActionType.tti`
**Description:** What action is the Workflow currently trying to take?
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| assert | Assert | No | Executing Assertions |
| activity | Activity | No | Creating Activities |
| start | Start | No | Executing a Start block |
| finish | Finish | No | Executing a Finish block |
| enter | Enter | No | Executing an Enter block |
| exit | Exit | No | Executing an Exit block |
| branch | Branch | No | Executing a Branch (or Timeout, Trigger, etc.) |
| selectBranch | SelectBranch | No | Looking for one of the branches to be ready to execute |

---

### Typelist: WorkflowActiveState

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\WorkflowActiveState.tti`
**Description:** The possible states of an active workflow object
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| running | Running | No | The workflow is currently running. |
| waitmanual | Wait Timeout/Manual | No | The workflow is waiting for a trigger or timeout. |
| waitactivity | Wait Activity | No | The workflow is waiting for some activities to complete. |
| waitmessage | Wait Message | No | The workflow is waiting for a message to be acked. |

---

### Typelist: WorkflowHandler

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\WorkflowHandler.tti`
**Description:** What infrastructure handles this Workflow?
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| internal | Internal | No | Handled by Guidewire's internal Workflow engine |
| test | Test | No | Handled by testing infrastructure (not for production!) |

---

### Typelist: WorkflowState

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\WorkflowState.tti`
**Description:** The states a workflow object can be in
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| active | Active | No | Active -- the workflow is running. |
| error | Error | No | The workflow encountered an exception while running, so the it has been paused until the error is fixed. |
| suspended | Suspended | No | Suspended -- execution of the workflow was manually suspended.  It can be resumed later. |
| completed | Completed | No | Completed -- the workflow reached one of its Outcomes. |

---

### Typelist: WorkflowTriggerKey

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\WorkflowTriggerKey.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\WorkflowTriggerKey.ttx`
**Description:** What workflow Triggers are allowed
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| FinishRenewalDocs | FinishRenewalDocs | No | FinishRenewalDocs |
| FailRenewalDocs | FailRenewalDocs | No | FailRenewalDocs |
| FinishIssueRenewal | FinishIssueRenewal | No | FinishIssueRenewal |
| FailIssueRenewal | FailIssueRenewal | No | FailIssueRenewal |
| FinishNonRenewalDocs | FinishNonRenewalDocs | No | FinishNonRenewalDocs |
| FailNonRenewalDocs | FailNonRenewalDocs | No | FailNonRenewalDocs |
| FinishSendNonRenewal | FinishSendNonRenewal | No | FinishSendNonRenewal |
| FailSendNonRenewal | FailSendNonRenewal | No | FailSendNonRenewal |
| FinishNotTakenDocs | FinishNotTakenDocs | No | FinishNotTakenDocs |
| FailNotTakenDocs | FailNotTakenDocs | No | FailNotTakenDocs |
| FinishSendNotTaken | FinishSendNotTaken | No | FinishSendNotTaken |
| FailSendNotTaken | FailSendNotTaken | No | FailSendNotTaken |
| Cancel | Cancel | No | Cancel |
| Withdraw | Withdraw | No | Withdraw |
| EditPolicy | EditPolicy | No | EditPolicy |
| FinishSendNotices | FinishSendNotices | No | FinishSendNotices |
| FailSendNotices | FailSendNotices | No | FailSendNotices |
| FinishCancellation | FinishCancellation | No | FinishCancellation |
| FailCancellation | FailCancellation | No | FailCancellation |
| Rescind | Rescind | No | Rescind |
| FinishRescind | FinishRescind | No | FinishRescind |
| FailRescind | FailRescind | No | FailRescind |
| OrderMVRs | OrderMVRs | No | OrderMVRs |
| WaitForMVRs | WaitForMVRs | No | WaitForMVRs |

---

### Typelist: WorkItemSetState

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\WorkItemSetState.tti`
**Description:** State of a WorkItemSet
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Processing | Processing | No | the WorkItemSet is being worked on, i.e. there is at least one WorkItem that has not been completed yet |
| Completed | Completed | No | all WorkItems have been processed. Some WorkItems may have been successful and others may have failed |
| Canceling | Canceling | No | a WorkItemSet goes into this state when the user requests that we cease further processing. Workers will continue processing current WorkItems, but will not start new ones. |
| CurrentlyPaused | Paused | No | the WorkItemSet is currently paused |
| CurrentlyStarting | Starting | No | the WorkItemSet is currently starting up |
| CurrentlyStuck | Stuck | No | the WorkItemSet appears to be stuck. Please cancel. |

---

### Typelist: WorkItemStatusType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\WorkItemStatusType.tti`
**Description:** The status of a work-item
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| available | Available | No | Work item that is available to be processed. |
| checkedout | CheckedOut | No | Work item that is checked out. |
| failed | Failed | No | Work item that exceeded the maximum number of allowed retries. |

---

### Typelist: XCUHazardsAllowed

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\XCUHazardsAllowed.tti`
**Description:** XCUHazardsAllowed
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| XCULocationOperation | XCU Site | No | XCU Site |
| XCUHazard | Permitted Hazard Description | No | Permitted Hazard Description |

---

### Typelist: XCUSite

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\XCUSite.tti`
**Description:** XCUSite
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Operation | Operation | No | Operation |
| Location | Location | No | Location |

---

### Typelist: Y2KExclusionType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\Y2KExclusionType.tti`
**Description:** Y2KExclusionType
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| total-exceptpremisesBI | total-exceptpremisesBI | No | total-except premises BI |
| productscompops | productscompops | No | products/comp ops only |
| total | total | No | total |

---

### Typelist: Zone

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\Zone.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\Zone.ttx`
**Description:** Zones that vehicle travels in
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 01 | Atlanta Zone | No | Atlanta |
| 02 | Baltimore/Washington Zone | No | Baltimore/Washington |
| 03 | Boston Zone | No | Boston |
| 04 | Buffalo Zone | No | Buffalo |
| 05 | Charlotte Zone | No | Charlotte |
| 06 | Chicago Zone | No | Chicago |
| 07 | Cincinnati Zone | No | Cincinnati |
| 08 | Cleveland Zone | No | Cleveland |
| 09 | Dallas/Fort Worth Zone | No | Dallas/FortWorth |
| 10 | Denver Zone | No | Denver |
| 11 | Detroit Zone | No | Detroit |
| 12 | Hartford Zone | No | Hartford |
| 13 | Houston Zone | No | Houston |
| 14 | Indianapolis Zone | No | Indianapolis |
| 15 | Jacksonville Zone | No | Jacksonville |
| 16 | Kansas City Zone | No | Kansas |
| 17 | Little Rock Zone | No | LittleRock |
| 18 | Los Angeles Zone | No | LosAngeles |
| 19 | Louisville Zone | No | Louisville |
| 20 | Memphis Zone | No | Memphis |
| 21 | Miami Zone | No | Miami |
| 22 | Milwaukee Zone | No | Milwaukee |
| 23 | Minneapolis/St. Paul Zone | No | Minneapolis |
| 24 | Nashville Zone | No | Nashville |
| 25 | New Orleans Zone | No | New Orleans |
| 26 | New York City Zone | No | NewYork |
| 27 | Oaklahoma City Zone | No | Oaklahoma |
| 28 | Omaha Zone | No | Omaha |
| 29 | Phoenix Zone | No | Phoenix |
| 30 | Philadelphia Zone | No | Philadelphia |
| 31 | Pittsburgh Zone | No | Pittsburgh |
| 32 | Portland Zone | No | Portland |
| 33 | Richmond Zone | No | Richmond |
| 34 | St. Louis Zone | No | StLouis |
| 35 | Salt Lake City Zone | No | SaltLake |
| 36 | San Francisco Zone | No | SanFrancisco |
| 37 | Tulsa Zone | No | Tulsa |
| 40 | Pacific Coast Zone | No | PacificCoast |
| 41 | Mountain Zone | No | Mountain |
| 42 | Midwest Zone | No | Midwest |
| 43 | Soutwest Zone | No | Southwest |
| 44 | North Central Zone | No | NorthCentral |
| 45 | Mideast Zone | No | Mideast |
| 46 | Gulf Zone | No | Gulf |
| 47 | Southeast Zone | No | Southeast |
| 48 | Eastern Zone | No | Eastern |
| 49 | New England Zone | No | NewEngland |
| 50 | Alaska Zone | No | Alaska |

---

### Typelist: ZoneType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\metadata\typelist\ZoneType.tti`
**Extension Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\ZoneType.ttx`
**Description:** Possible types of zones
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| country | Country | No | Country |
| unknown | Unknown | Yes | Placeholder typecode for fields that should be populated with another ZoneType |
| city | City | No | City |
| citykanji | CityKanji | No | CityKanji |
| county | County | No | County |
| state | State | No | State |
| prefecture | Prefecture | No | Prefecture |
| province | Province | No | Province |
| postalcode | Postal Code | No | PostalCode |
| zip | Zip code | No | Zip code |
| fsa | FSA | No | FSA |
| postcodearea | Post Code Area | No | Post Code Area |
| postcoderegion | Post Code Region | No | Post Code Region |

---

### Typelist: AcceptDecline

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\AcceptDecline.tti`
**Description:** AcceptDecline
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| accept | Accept | No | Accept |
| decline | Decline | No | Decline |

---

### Typelist: AdditionalInformationType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\AdditionalInformationType.tti`
**Description:** 
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| School | School Name | No | School Name |

---

### Typelist: AggLimitLevel

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\AggLimitLevel.tti`
**Description:** Level where agg limit applies
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| policy | per policy | No | per policy |
| location | per location | No | per location |
| building | per building | No | per building |

---

### Typelist: BroadLimited

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\BroadLimited.tti`
**Description:** Broad or Limited Coverage
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| broad | Broadened | No | Broadened |
| limited | Limited | No | Limited |

---

### Typelist: CatastropheType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\CatastropheType.tti`
**Description:** the type of a given catastrophe
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| iso | ISO | No | ISO |
| internal | Internal | No | Internal |

---

### Typelist: CoordinateBenefits

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\CoordinateBenefits.tti`
**Description:** Hawaii PIP Coordinage benefits
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| decline | Decline | No | Decline |
| health | Coordinate Health Benefits | No | Coordinate Health Benefits |
| disability | Coordinate Disability Benefits | No | Coordinate Disability Benefits |
| coordinateboth | Coordinate Health and Disability Benefits | No | Coordinate Health and Disability Benefits |

---

### Typelist: DeductibleType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\DeductibleType.tti`
**Description:** Deductible Type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| PerClaim | Per Claim | No | Per Claim |
| PerOccurrence | Per Occurrence | No | Per Occurrence |

---

### Typelist: FullLimitedTort

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\FullLimitedTort.tti`
**Description:** FullLimitedTort
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| full | Full | No | No limit on Tort |
| limited | Limited | No | Limited Tort |

---

### Typelist: GLActType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\GLActType.tti`
**Description:** GLActType
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Completion | Completion | No | Completion |
| Disposal | Disposal | No | Disposal |
| Distribution | Distribution | No | Distribution |
| Manufacture | Manufacture | No | Manufacture |
| Sale | Sale | No | Sale |

---

### Typelist: GLProductWorkType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\GLProductWorkType.tti`
**Description:** GLProductWorkType
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Product | Product | No | Product |
| Work | Work | No | Work |

---

### Typelist: GLY2KCompSpecdCovExclType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\GLY2KCompSpecdCovExclType.tti`
**Description:** GLY2KCompSpecdCovExclType
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Product | Product | No | Product |
| CompletedOperation | Completed Operation | No | Completed Operation |

---

### Typelist: NumberOfStories

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\NumberOfStories.tti`
**Description:** NumberOfStories
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 1 | 1 | No | 1 Story |
| 2 | 2 | No | 2 Stories |
| 3 | 3 | No | 3 Stories |
| 4 | 4 | No | 4 Stories |
| 5Plus | 5+ | No | 5 Stories or more |

---

### Typelist: PIPHousehold

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\PIPHousehold.tti`
**Description:** PIP Household coverage or exclusion for NY, MA, DE, OR and others
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| decline | Decline | No | Decline |
| insured | Insured | No | Insured Only |
| family | Insured and Family/Household | No | Insured and Family/Household |

---

### Typelist: PIPNJAggLimit

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\PIPNJAggLimit.tti`
**Description:** NJ PIP Agg Wage Loss Limit
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 104 | 104 Weeks | No | 104 weeks |
| unlimited | Unlimited | No | Unlimited |

---

### Typelist: PIPWorkLossExclusion

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\PIPWorkLossExclusion.tti`
**Description:** MN PIP work loss exclusion for insured or insured and household
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| noexclusion | No Exclusion | No | No Exclusion |
| excludeinsured | Insured Only (if 65+) | No | Insured Only (if 65+) |
| excludefamily | Insured and familty (if all 65+) | No | Insured and familty (if all 65+) |

---

### Typelist: RateConversionType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\RateConversionType.tti`
**Description:** Explains how a rating factor or modifier rate should be converted for use by the rating engine.
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| as_is | Use as is | No | The rate already represents the correct amount to multiply by.  For example, 0.2000 should be used as is, so that basis * 0.2000 = amount. |
| diff_from_1 | Use rate-1 | No | The rate is commonly displayed as a factor relative to 1.00, such as 1.1 for a 10% increase or 0.85 for a 15% discount, but the actual amount to be added is the +10% or -15%.  For example, 0.9500 should be converted so that basis * (0.9500 - 1) = basis * -0.0500 = amount. |
| credit | Use as credit | No | The rate is commonly shown as a positive number but is intended to generate a credit (negative charge).  For example, 0.15 should be multiplied by -1 so that basis * (-1 * 0.15) = amount. |

---

### Typelist: RateSubtotalType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\RateSubtotalType.tti`
**Description:** Defines a set of rating subtotals used by the sample rating rules for storing and retrieving intermediate values.
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| total_premium | Total Premium | No | Amount which includes all premiums but excludes taxes and other non-premium fees. |
| wc_manual | Manual Premium | No | Amount determined by applying manual rates to each exposure unit. |
| wc_subject | Subject Premium | No | Amount that is subject to experience modification. |
| wc_modified | Modified Premium | No | Amount after application of experience modification. |
| wc_standard | Standard Premium | No | Amount which includes everything classified as standard premium (including min premium adjustments but prior to expense constants, premium discounts, etc.) |
| wc_eap | Estimated Annual Premium | No | Amount which includes all premiums but excludes non-premium taxes and surcharges. |
| bop_manual | Manual Premium | No | Amount determined by applying manual rates to each exposure unit. |
| bop_subject | Subject Premium | No | Amount that is subject to individual risk premium modification. |
| bop_modified | Modified Premium | No | Amount after application of individual risk premium modification. |
| bop_standard | Standard Premium | No | Amount which includes everything classified as standard premium (including min premium adjustments but prior to expense constants, premium discounts, etc.) |
| bop_eap | Estimated Annual Premium | No | Amount which includes all premiums but excludes non-premium taxes and surcharges. |

---

### Typelist: SampleA

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\SampleA.tti`
**Description:** Sample typelist A
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| codeOne | CodeOne | No | CodeOne |
| codeTwo | CodeTwo | No | CodeTwo |
| codeThree | CodeThree | No | CodeThree |

---

### Typelist: SampleB

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\SampleB.tti`
**Description:** Sample typelist B
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| red | Red | No | Red |
| blue | Blue | No | Blue |
| green | Green | No | Green |
| Color_retired | Color_retired | Yes | Color_retired |

---

### Typelist: SBCovPackages

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\SBCovPackages.tti`
**Description:** SB CoveragePacks
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| MerchantPack | Merchant's Risk Pack | No | Merchant's Risk Pack |
| LessorPack | Lessor's Risk Pack | No | Lessor's Risk Pack |
| TechPack | Technology Risk Pack | No | Technology Risk Pack |
| ResidentialPack | Residential Risk Pack | No | Residential Risk Pack |
| FoodPack | Food Risk Pack | No | Food Risk Pack |
| ContractorPack | Contractor Risk Pack | No | Contractor Risk Pack |

---

### Typelist: VehicleEmployeeUsage

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\VehicleEmployeeUsage.tti`
**Description:** MA PIP Work Comp Discount eligibility
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| employeesonly | Used for Employees Only | No | Used to Transport Employees only |
| multiuse | Multi-use | No | Multi-use |

---

### Typelist: WC7ClassCodeFedDomains

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\WC7ClassCodeFedDomains.tti`
**Description:** A type of class code (FELA, Maritime, etc)
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Mari | WC Maritime | No | WC Maritime Act (Program I) codes |
| MariState | WC Maritime State | No | WC Maritime Act (Program II) codes |
| MariUSLH | WC Maritime USLH | No | WC Maritime Act (Program II) codes |
| FELA | WC FELA | No | WC FELA Act (Program I) codes |
| FELAState | WC FELA State | No | WC FELA Act (Program II) codes |
| FELAUSLH | WC FELA USLH | No | WC FELA Act (Program II) codes |

---

### Typelist: WC7ClassCodeProgramType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\WC7ClassCodeProgramType.tti`
**Description:** Types of programs
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| ProgramI | Program I | No | Program I |
| ProgramIIStateAct | Program II State Act | No | Program II State Act |
| ProgramIIUSLH | Program II USLH | No | Program II USLH |

---

### Typelist: WC7ClassCodeType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\WC7ClassCodeType.tti`
**Description:** Types of class codes
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| FELA | FELA | No | FELA |
| USLH | USLH | No | USLH |
| Admiralty | Admiralty | No | Admiralty |
| Nonratable | Nonratable | No | Nonratable |
| AtomicEnergy | Atomic Energy | No | Atomic Energy |

---

### Typelist: WC7CovEmpCostType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\WC7CovEmpCostType.tti`
**Description:** The type of cost for a covered employees' cost: e.g. Manual Premium, USLH
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| ManualPremium | Manual Premium | No | Manual Premium |
| USLH | USLH | No | United States Longshoremans & Harbor Works Act |
| CoalMineDisCharge | Coal Mine Disease Charge | No | Coal Mine Disease Charge |
| CatastropheLoading | Catastrophe Loading | No | Catastrophe Loading |
| SupplementalDisease | Supplemental Disease | No | Supplemental Disease |

---

### Typelist: WC7CovProgramType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\WC7CovProgramType.tti`
**Description:** WC Coverage program type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| ProgramI | Program I | No | Program I |
| ProgramII | Program II | No | Program II |

---

### Typelist: WC7ELIncrLimitCostType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\WC7ELIncrLimitCostType.tti`
**Description:** The type of Employers liability increased limit cost: e.g. factor or charge
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| incrlimitfactor | Increased Limit Factor | No | Increased Limit Factor |
| incrlimitcharge | Increased Limit Charge | No | Increased Limit Charge |

---

### Typelist: WC7EmployeeLeasingPolicyType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\WC7EmployeeLeasingPolicyType.tti`
**Description:** The type of employee leasing policy.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Master | Master Policy | No | A policy written in the name of the PEO covering its direct workers, and the leased workers of multiple client companies. |
| MCP | Multiple Coordinated Policy (MCP) | No | Multiple coordinated policies where the PEO has a policy covering its direct workers and each client company has a policy covering its leased workers.  Endorsements are used to coordinate between the client companies and the PEO. |
| MultiplePEO | Multiple PEO Policies | No | Multiple policies where each client company has a policy covering its leased workers with the PEO as the primary named insured with reference to the name of the client company. |
| ClientDirect | Client Direct Policy | No | A policy obtained by the client for both the client's leased and direct workers. |

---

### Typelist: WC7ExpModStatus

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\WC7ExpModStatus.tti`
**Description:** WC7ExpModStatus
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Preliminary | Preliminary | No | Preliminary |
| Final | Final | No | Final |
| Contingent | Contingent | No | Contingent |

---

### Typelist: WC7FedEmpLiabAct

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\WC7FedEmpLiabAct.tti`
**Description:** Federal Employers Liability coverage Act type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| mari | Maritime Coverage | No | Maritime Coverage |
| fela | Fed Empl Liab Act | No | Fed Empl Liab Act |

---

### Typelist: WC7FELACovEmpCostType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\WC7FELACovEmpCostType.tti`
**Description:** The type of cost for a FELA covered employees' cost
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| FELACovEmp | FELA Covered Employee | No | FELA Covered Employee |
| IncreasedLimitsFactor | Increased Limit Factor(FELA) | No | Increased Limit Factor(FELA) |
| SupplementalDisease | Supplemental Disease(FELA) | No | Supplemental Disease(FELA) |

---

### Typelist: WC7GoverningLaw

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\WC7GoverningLaw.tti`
**Description:** What kind of special coverage does this group of employees have?
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| state | State Act | No |  |
| defenseBaseAct | Defense Base Act | No | WC 00 01 01 A 04 92 |
| fedCoalMine | Federal Coal Mine Health And Safety Act | No | WC 00 01 02 A 07 11 |
| longshoreAndHarbor | Longshore And Harbor Workers Compensation Act | No | WC 00 01 06 A 04 92 |
| migrantAndSeasonalAgricultural | Migrant And Seasonal Agricultural Worker Protection Act | No | WC 00 01 11 07 92 |
| nonappropriatedFundInstrumentalities | Nonappropriated Fund Instrumentalities Act | No | WC 00 01 08 A 04 92 |
| outerContinentalShelfLands | Outer Continental Shelf Lands Act | No | WC 00 01 09 B 07 11 |
| voluntaryComp | Voluntary Compensation and Employers Liability | No | WC 00 03 11 A 08 91 |
| voluntaryCompForResidenceEmp | Voluntary Compensation and Employers Liability For Residence Employees | No | WC 00 03 12 A 07 11 |
| limitedMaritime | Limited Maritime | No | WC 00 02 04 |
| stopGap | Exposure Rated Stop Gap | No | Exposure rated stop gap |

---

### Typelist: WC7JurisdictionCostType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\WC7JurisdictionCostType.tti`
**Description:** The type of a WC Jurisdiction Cost.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| MinPrem | Minimum Premium Adjustment | No | Additional premium charged so that standard premium for the policy or jurisdiction meets a minimum amount |
| MinPremFELAMaritime | Minimum Premium Adjustment (FELA, Maritime) | No | Additional premium charged so that standard premium for the policy or jurisdiction meets a minimum amount (FELA / Maritime) |
| CancelShortRatePenalty | Cancellation short-rate penalty | No | Cancellation penalty determined by short-rate. |
| Tax | Tax | No | Tax |
| CIGA | CIGA surcharge | No | CA Insurance Guarantee Assoc surcharge |
| ExpenseConst | Expense constant | No | Expense constant |
| PremDis | Premium discount | No | Premium discount |
| TerrorPrem | Terrorism premium | No | Terrorism premium |
| SchedCredit | Schedule credit | No | Premium adjustment based on evaluation of the insured's risk relative to the average risk of others in the same class |
| Waiver | Waiver charge | No | Extra charge for waiver of subrogation |
| WaiverBalance | Waiver Balance charge | No | Balance charge to bring Specific Waiver of Subrogation up to Minimum |
| ExpMod | Experience modifier | No | Workers' comp experience modifier credit or debit |
| WCEL | Emp liab increased limits | No | Premium for workers' comp employers liability limits above the base (standard) amounts |
| CPAP | CPAP Jurisdiction Modifier | No | CPAP Jurisidiction Modifier |
| ScheduleMod | Schedule Modifier | No | Schedule Modifier |
| AircraftSeatSurcharge | Aircraft Seat Surcharge | No | Aircraft Seat Surcharge |
| ELVoluntaryCompFlatCharge | Employers Liability Voluntary Compensation flat charge | No | Employers Liability Voluntary Compensation flat charge |
| SmallDeductible | Small Deductible Credit | No | Small Deductible Credit |
| ModifierAdjustment | Modifier Adjustment | No | Modifier Adjustment |
| CertifiedSafetyCredit | Certified Safety Credit | No | Certified Safety Credit |
| DrugFreeWorkplaceCredit | Drug Free Workplace Credit | No | Drug Free Workplace Credit |
| CatastrophePremium | Catastrophe (Other Than Certified Acts of Terrorism) | No | Catastrophe (Other Than Certified Acts of Terrorism) |
| ManagedCareCredit | Managed Care Credit | No | Managed Care Credit |
| CoinsuranceDeductCredit | Coinsurance &/or Deductible Credit | No | Coinsurance &/or Deductible Credit |
| MaritimeManualPremium | Maritime Manual Premium | No | Maritime Manual Premium |

---

### Typelist: WC7LiabilityAct

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\WC7LiabilityAct.tti`
**Description:** Liability acts
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| WorkersComp | Workers Comp Acts | No | Workers Comp Acts |
| Federal | Federal Acts | No | Federal Acts |

---

### Typelist: WC7MaritimeCovEmpCostType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\WC7MaritimeCovEmpCostType.tti`
**Description:** The type of cost for a maritime covered employees' cost
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| MaritimeCovEmp | Maritime Covered Employee | No | Maritime Covered Employee |
| IncreasedLimitsFactor | Increased Limit Factor(Maritime) | No | Increased Limit Factor(Maritime) |
| SupplementalDisease | SupplementalDisease(Maritime) | No | Supplemental Disease(Maritime) |

---

### Typelist: WC7ParticipatingPlanID

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\WC7ParticipatingPlanID.tti`
**Description:** The type of WC participating plan.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 1ystd | 1Y-STD | No | One year standard |
| 2ystd | 2Y-STD | No | Two years standard |
| 3ystd | 3Y-STD | No | Three years standard |

---

### Typelist: WC7PersonOrg

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\WC7PersonOrg.tti`
**Description:** Person or Organization?
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| per | Person | No | A person |
| org | Organization | No | An organization |

---

### Typelist: WC7PremiumLevelType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\WC7PremiumLevelType.tti`
**Description:** WC7PremiumLevelType
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| TotalManualPremium | Total Manual Premium | No | Total Manual Premium |
| SubjectPremium | Subject Premium | No | Subject Premium |
| TotalSubjectPremium | Total Subject Premium | No | Total Subject Premium |
| TotalModifiedPremium | Total Modified Premium | No | Total Modified Premium |
| TotalStandardPremium | Total Standard Premium | No | Total Standard Premium |
| EstimatedAnnualPremium | Estimated Annual Premium | No | Estimated Annual Premium |
| TotalAmountDue | Total Amount Due | No | Total Amount Due |

---

### Typelist: WC7ProfessionalEmployeeType

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\WC7ProfessionalEmployeeType.tti`
**Description:** The type of employee for the employee leasing plan.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| PEO | Professional Employer Organization (PEO) | No | A firm that provides a service under which client companies can outsource employee management tasks, like workers' compensation. |
| Client | Client Company | No | A company that hires a PEO to provide management tasks for its employee |

---

### Typelist: WC7VoluntaryComp

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\WC7VoluntaryComp.tti`
**Description:** Voluntary compensation type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Jurisdiction | Jurisdiction Act | No | Jurisdiction Act |
| USLH | U.S.L. & H. | No | U.S.L. & H. |

---

### Typelist: WC7WaiverOfSubrogation

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\WC7WaiverOfSubrogation.tti`
**Description:** The type of waiver of subro.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| blanket | Blanket | No | A blanket waiver of liability |
| specific | Specific | No | A specific waiver of liability |

---

### Typelist: WC7WorkerKind

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\WC7WorkerKind.tti`
**Description:** What kind of worker?
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| farmag | Farm or Agricultural Worker | No | Farm or agricultural worker |
| domhos | Domestic or Household Worker | No | Domestic or household Worker |

---

### Typelist: WCRateStepAction

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\WCRateStepAction.tti`
**Description:** Types of actions that can be taken at each step of the sample Worker Comp rating process.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| subtotal | Store subtotal | No | Calculates and stores a subtotal for later use in the rating algorithm.  Does not generate any new rating lines.  If chosen, the subtotal and granularity fields should be non-null. |
| modifier | Apply modifier | No | Calculates a new rating line to give a credit or debit based on a modifier.  If chosen, the modifierID and rateConversion fields should be non-null.  If the subtotal and granularity fields are non-null, then the subtotal will be looked up and used as the basis for the calculation.  Otherwise, the subtotal up to this point will be used. |
| fee | Apply rate-based adjustment, tax, or surcharge | No | Calculates a new rating line by looking up a rating factor (for a state), typically to add a tax or surcharge.  If chosen, the factorName and rateConversion fields should be non-null.  Similar to the modifier action, the subtotal and granularity fields are optional. |
| custom | Custom | No | No generic action is capable of processing this step so a custom action must be defined for it. |

---

### Typelist: WorkCapacity

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\WorkCapacity.tti`
**Description:** Capacity in which employee returned to work
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| fullduty | RTW - full duty | No | Full duty |
| modifiedduty | RTW - modified duty | No | Modified duty |
| estimatedrtw | Estimated RTW date | No | Estimated RTW date |
| stopped_work | Stopped work | No | Stopped work |

---

### Typelist: Job

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\Job.ttx`
**Description:** Subtype typelist for entity Job
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| *(None defined)* | *Dynamic or database-driven* | No | Typelist populated dynamically at runtime or via database table |

---

### Typelist: PolicyLine

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\PolicyLine.ttx`
**Description:** Subtype typelist for entity PolicyLine
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic policy/account generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| *(None defined)* | *Dynamic or database-driven* | No | Typelist populated dynamically at runtime or via database table |

---

### Typelist: RIAgreement

**Source:** `C:\GW10\PolicyCenter\modules\configuration\config\extensions\typelist\RIAgreement.ttx`
**Description:** Subtype typelist for entity RIAgreement
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| RIAgreement | Reinsurance Agreement | No | RIAgreement |
| ProportionalRIAgreement | Proportional Agreement | No | ProportionalRIAgreement |
| NonProportionalRIAgreement | Non-Proportional Agreement | No | NonProportionalRIAgreement |
| FacProportionalRIAgreement | Proportional Facultative Agreement | No | FacProportionalRIAgreement |
| NetExcessOfLossRITreaty | Net Excess of Loss Treaty | No | NetExcessOfLossRITreaty |
| QuotaShareRITreaty | Quota Share Treaty | No | QuotaShareRITreaty |
| FacNetExcessOfLossRIAgreement | Net Excess of Loss Facultative Agreement | No | FacNetExcessOfLossRIAgreement |
| AnnualAggregateRITreaty | Annual Aggregate Treaty | No | AnnualAggregateRITreaty |
| PerEventRITreaty | Per-Event Treaty | No | PerEventRITreaty |
| FacExcessOfLossRIAgreement | Excess of Loss Facultative Agreement | No | FacExcessOfLossRIAgreement |
| ExcessOfLossRITreaty | Excess of Loss Treaty | No | ExcessOfLossRITreaty |
| SurplusRITreaty | Surplus Treaty | No | SurplusRITreaty |

---

