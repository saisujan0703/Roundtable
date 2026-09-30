# ClaimCenter Typelist Catalog

**Guidewire ClaimCenter Version:** 10.2.1.1523 (Platform 10.201.1)
**Installation Location:** `C:\GW10\ClaimCenter`
**Extraction Date:** 2026-09-26
**Total Unique Typelists Discovered:** 443

---

## Overview & Methodology

This catalog documents every verified typelist extracted from the Guidewire ClaimCenter installation metadata (`.tti`) and extension (`.ttx`) definitions. In ClaimCenter, typelists govern claim lifecycles, exposure statuses, financial transaction types, cost categorization, injury severities, litigation stages, and service vendor roles.

Each typelist entry contains:
1. **Typelist Name**: Identifier used in Gosu, entity XML schemas, and PCF user interfaces.
2. **Source Path**: Exact file path on this VM verifying the definition.
3. **Description**: Verifiable documentation from the typelist XML metadata.
4. **Valid Codes Table**: Code, Display Name, Retired status, and synthetic generation relevance.

---

## Typelist Definitions

### Typelist: AccidentPremises

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\AccidentPremises.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\AccidentPremises.ttx`
**Description:** A code to indicate the premises where the accident occurred.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Employer | Employer | No | Employer |
| Lessee | Lessee | No | Lessee |
| Other | Other | No | Other |

---

### Typelist: AccidentType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\AccidentType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\AccidentType.ttx`
**Description:** Detailed accident type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 01 | Contact with chemicals | No | Contact with chemicals |
| 02 | Contact with hot objects or substances | No | Contact with hot objects or substances |
| 03 | Contact with temperature extremes | No | Contact with temperature extremes |
| 04 | Contact with fire or flame | No | Contact with fire or flame |
| 05 | Contact with steam or hot fluids | No | Contact with steam or hot fluids |
| 06 | Contact with dust, gases, fumes, or vapors | No | Contact with dust, gases, fumes, or vapors |
| 07 | Contact with welding operation | No | Contact with welding operation |
| 09 | Contact with radiation | No | Contact with radiation |
| 11 | Contact with miscellaneous | No | Contact with miscellaneous |
| 14 | Contact with abnormal air pressure | No | Contact with abnormal air pressure |
| 84 | Contact with electrical current | No | Contact with electrical current |
| 10 | Caught in, under, or between machine or machinery | No | Caught in, under, or between machine or machinery |
| 12 | Caught in, under, or between object handled | No | Caught in, under, or between object handled |
| 13 | Caught in, under, or between miscellaneous | No | Caught in, under, or between miscellaneous |
| 20 | Caught in, under, or between collapsing materials (slides of earth) | No | Caught in, under, or between collapsing materials (slides of earth) - either man made or natural |
| 15 | Cut, puncture, scrape, injured by broken glass | No | Cut, puncture, scrape, injured by broken glass |
| 16 | Cut, puncture, scrape, injured by hand tool, utensil; not powered | No | Cut, puncture, scrape, injured by hand tool, utensil; not powered |
| 17 | Cut, puncture, scrape, injured by object being lifted or handled | No | Cut, puncture, scrape, injured by object being lifted or handled |
| 18 | Cut, puncture, scrape, injured by powered hand tool, appliance | No | Cut, puncture, scrape, injured by powered hand tool, appliance |
| 19 | Cut, puncture, scrape, injured by miscellaneous | No | Cut, puncture, scrape, injured by miscellaneous |
| 25 | Fall, slip, or trip injury from different level (elevation) | No | Fall, slip or trip injury from different level (elevation) - off wall, catwalk, bridge, etc. |
| 26 | Fall, slip, or trip injury from ladder or scaffolding | No | Fall, slip, or trip injury from ladder or scaffolding |
| 27 | Fall, slip, or trip injury from liquid or grease spills | No | Fall, slip, or trip injury from liquid or grease spills |
| 28 | Fall, slip, or trip injury into openings | No | Fall, slip, or trip injury into openings (shafts, excavations, floor openings, etc.) |
| 29 | Fall, slip, or trip injury on same level | No | Fall, slip, or trip injury on same level |
| 30 | Slipped, do not fall | No | Fall, slip or trip injury from ladder or scaffolding |
| 31 | Fall, slip, or trip injury, miscellaneous | No | Fall, slip, or trip injury, miscellaneous |
| 32 | Fall, slip, or trip injury on ice or snow | No | Fall, slip, or trip injury on ice or snow |
| 33 | Fall, slip, or trip injury on stairs | No | Fall, slip, or trip injury on stairs |
| 40 | Crash of water vehicle | No | Crash of water vehicle |
| 41 | Crash of rail vehicle | No | Crash of rail vehicle |
| 45 | Collision or sideswipe with another vehicle | No | Collision or sideswipe with another vehicle (both vehicles in motion) |
| 46 | Collision with a fixed object | No | Collision with a fixed object (standing vehicle or stationary object) |
| 47 | Crash of airplane | No | Crash of airplane |
| 48 | Vehicle upset | No | Vehicle upset (overturned or jackknifed) |
| 50 | Motor vehicle, miscellaneous | No | Motor vehicle, miscellaneous |
| 52 | Strain or injury by continual noise | No | Strain or injury by continual noise |
| 53 | Strain or injury by twisting | No | Strain or injury by twisting |
| 54 | Strain or injury by jumping | No | Strain or injury by jumping |
| 55 | Strain or injury by holding or carrying | No | Strain or injury by holding or carrying |
| 56 | Strain or injury by lifting | No | Strain or injury by lifting |
| 57 | Strain or injury by pushing or pulling | No | Strain or injury by pushing or pulling |
| 58 | Strain or injury by reaching | No | Strain or injury by Reaching |
| 59 | Strain or injury by using tool or machinery | No | Strain or injury by using tool or machinery |
| 60 | Strain or injury by miscellaneous | No | Strain or injury by miscellaneous |
| 61 | Strain or injury by wielding or throwing | No | Strain or injury by wielding or throwing |
| 97 | Strain or injury by repetitive motion | No | Strain or injury by repetitive motion (carpal tunnel syndrome) |
| 65 | Striking against or stepping on moving part of machine | No | Striking against or stepping on moving part of machine |
| 66 | Striking against or stepping on object being lifted or handled | No | Striking against or stepping on object being lifted or handled |
| 67 | Striking against or stepping on sanding, scraping, cleaning operation | No | Striking against or stepping on sanding, scraping, cleaning operation |
| 68 | Striking against or stepping on stationary object | No | Striking against or stepping on stationary object |
| 69 | Stepping on sharp object | No | Stepping on sharp object |
| 70 | Striking against or stepping on miscellaneous | No | Striking against or stepping on miscellaneous |
| 74 | Struck or injured by fellow worker; patient | No | Struck or injured by fellow worker; patient (not in act of a crime) |
| 75 | Struck or injured by falling or flying object | No | Struck or injured by falling or flying object |
| 76 | Struck or injured by hand tool or machine in use | No | Struck or injured by hand tool or machine in use |
| 77 | Struck or injured by motor vehicle | No | Struck or injured by motor vehicle |
| 78 | Struck or injured by moving parts of machine | No | Struck or injured by moving parts of machine |
| 79 | Struck or injured by object being lifted or handled | No | Struck or injured by object being lifted or handled |
| 80 | Struck or injured by object handled by others | No | Struck or injured by object handled by others |
| 81 | Struck or injured, miscellaneous | No | Struck or injured, miscellaneous (includes kicked, stabbed, bit, etc.) |
| 85 | Struck or injured by animal or insect | No | Struck or injured by animal or insect |
| 86 | Struck or injured by explosion or flare back | No | Struck or injured by explosion or flare back |
| 94 | Rubbed or abraded by repetitive motion | No | Rubbed or abraded by repetitive motion (callous, blister, etc.) |
| 95 | Rubbed or abraded, miscellaneous | No | Rubbed or abraded, miscellaneous |
| 82 | Absorption, ingestion, or inhalation, miscellaneous | No | Absorption, ingestion, or inhalation, miscellaneous |
| 87 | Foreign matter (body) in eye(s) | No | Foreign matter (body) in eye(s) |
| 88 | Natural disasters | No | Natural disasters (earthquake, hurricane, tornado, etc.) |
| 89 | Person in act of a crime | No | Person in act of a crime (robbery or criminal assault) |
| 90 | Miscellaneous - other than physical cause of injury | No | Miscellaneous - other than physical cause of injury |
| 91 | Mold | No | Mold |
| 96 | Terrorism | No | Terrorism |
| 98 | Miscellaneous - cumulative, miscellaneous | No | Miscellaneous - cumulative, miscellaneous (all other) |
| 99 | Miscellaneous - other | No | Miscellaneous - other |

---

### Typelist: ActivityCategory

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ActivityCategory.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ActivityCategory.ttx`
**Description:** All available categories of activities
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| approval | Approval | No | Approval |
| correspondence | Correspondence | No | Correspondence |
| interview | Interview | No | Interview |
| newmail | New Mail | No | New mail |
| reminder | Reminder | No | Reminder |
| request | Request | No | Request |
| response | Response | No | Response |
| tool | Tool | No | Tool |
| fnol | FNOL | Yes | FNOL |
| assignmentreview | Assignment Review | No | Assignment review |
| approvaldenied | Approval Denied | No | Approval denied |
| general | General | No | General |
| warning | Warning | No | Warning |
| litigation | Litigation | No | Litigation |
| iso | ISO | No | ISO |
| investigation | Investigation | No | Investigation |
| filereview | File Review | No | File Review |
| handlinginstructions | Handling Instructions | No | Handling Instructions |
| servicerequestnotification | Service Notification | No | Service Notification |

---

### Typelist: ActivityClass

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ActivityClass.tti`
**Description:** The class of the activity
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| task | Task | No | Task |
| event | Event | No | Event |

---

### Typelist: ActivityStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ActivityStatus.tti`
**Description:** The status of the activity
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| open | Open | No | Open |
| skipped | Skipped | No | Skipped |
| complete | Complete | No | Complete |
| canceled | Canceled | No | Canceled activity that is still visible to the user |

---

### Typelist: ActivitySubjectSearchType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ActivitySubjectSearchType.tti`
**Description:** The types of subject searches for activity pattens
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| activitypattern | Activity Pattern | No | Search by activity pattern id |
| contains | Contains Search | No | Search by contains text |

---

### Typelist: ActivityType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ActivityType.tti`
**Description:** The type of activity
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| general | General | No | General |
| approval | Approval | No | Approval |
| assignmentreview | Assignment Review | No | Assignment Review |
| approvaldenied | Approval Denied | No | Approval Denied |

---

### Typelist: AddressType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\AddressType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\AddressType.ttx`
**Description:** Types of mailing addresses
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| home | Home | No | Home |
| business | Business | No | Business |
| other | Other | No | Other |
| billing | Billing | No | Billing |

---

### Typelist: AdversePartyDenialReason

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\AdversePartyDenialReason.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\AdversePartyDenialReason.ttx`
**Description:** Adverse Carriers reason for denying claim related to the Adverse Party
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| suspended | Licence Suspended | No | Licence Suspended |
| lapsed | Policy Lapsed | No | Policy Lapsed |

---

### Typelist: AggLimitCalcCriteria

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\AggLimitCalcCriteria.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\AggLimitCalcCriteria.ttx`
**Description:** AggLimitCalcCriteria defines the choices for limiting which costtypes and/or cost categories count towards aggregate limits.  Configured via aggregatelimitused-config.xml
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| all | All incurred costs | No | All incurred costs |
| costTypesExcludingExpenses | All incurred costs except expenses | No | All incurred costs except expenses |
| costTypesExcludingLegalExpenses | All incurred costs except legal expenses | No | All incurred costs except legal expenses |

---

### Typelist: AggregateLimitType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\AggregateLimitType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\AggregateLimitType.ttx`
**Description:** Aggregate limit types
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| lossdate | Loss date | No | Annual limit by loss date |
| reporteddate | Reported date | No | Annual limit by reported date |
| none | None | No | Annual limit without restrictions |

---

### Typelist: AggregateType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\AggregateType.tti`
**Description:** Aggregate types: limit, or deductible
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| limit | Limit | No | Annual Aggregate Limit |
| deductible | Deductible | No | Annual Aggregate Deductible |

---

### Typelist: ApprovalStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ApprovalStatus.tti`
**Description:** The approval status of an approvable entity
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| unapproved | Unapproved | No | Pending approval |
| approved | Approved | No | The entity has been approved |
| rejected | Rejected | No | The entity has been rejected |

---

### Typelist: ApprovedTreatment

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ApprovedTreatment.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ApprovedTreatment.ttx`
**Description:** Medical treatment outcome - for use on MedCaseMgr screen
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Drug | Drug prescription | No | Drug prescription |
| LabXrayPath | Lab, x-ray, or path work | No | Lab, x-ray or path work |
| SpecialistRef | Specialist referral | No | Specialist referral |
| PT | Physical therapy | No | Physical therapy |
| Chiro | Chiropractor | No | Chiropractor |
| CATscan | CAT scan | No | CAT scan |
| MRI | MRI | No | MRI |
| Surgery | Surgery | No | Surgery |
| Massage | Massage therapy | No | Massage therapy |
| HealthClub | Health club membership | No | Health club membership |

---

### Typelist: ArchiveFinalStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ArchiveFinalStatus.tti`
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

### Typelist: ArchiveSourceStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ArchiveSourceStatus.tti`
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

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ArchiveState.tti`
**Description:** state of the data in archive process
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| archived | Archived | No | Graph has been archived |
| retrieving | Retrieving | No | Graph is marked for retrieving |

---

### Typelist: AssessmentAction

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\AssessmentAction.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\AssessmentAction.ttx`
**Description:** Type of assessment
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Review | Reviewing | No | Reviewing |
| Deny | Denied | No | Denied |
| approve | Approved | No | Approved |

---

### Typelist: AssessmentContentAction

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\AssessmentContentAction.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\AssessmentContentAction.ttx`
**Description:** Type of assessment
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Review | Review | No | Review |
| Deny | Deny | No | Deny |
| depreciate | To be Depreciated | No | Approved, yet to be Depreciated |
| approve | Approve | No | Approve |

---

### Typelist: AssessmentEvent

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\AssessmentEvent.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\AssessmentEvent.ttx`
**Description:** Type of assessment
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| assignaccept | Assignment Accepted | No | Assignment Accepted |
| assigncanceled | Assignment Canceled | No | Assignment Canceled |
| estdate | Estimate Date Set | No | Estimate Date Set |
| estcomplete | Estimate Complete | No | Estimate Complete |
| estaccepted | Estimate Accepted | No | Estimate Accepted |
| reinspect | Re-inspection Requested | No | Re-inspection Requested |
| reinspectcomplete | Re-inspection Complete | No | Re-inspection Complete |
| repairdate | Repair Date Set | No | Repair Date Set |
| newrepairdate | Repair Date Re-Set | No | Repair Date Re-Set |
| repair | Repair In-Progress | No | Repair In-Progress |
| repaircomplete | Repair Complete | No | Repair Complete |

---

### Typelist: AssessmentSource

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\AssessmentSource.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\AssessmentSource.ttx`
**Description:** Type of negotiation.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Insured | Insured's Vendor | No | Insured |
| ApprovedVendor | Approved Vendor | No | Approved Vendor |
| InternalAppraiser | Internal Appraiser | No | Internal Appraiser |
| DeskReview | Desk Review | No | Desk Review |
| Claimant | Third Party's Vendor | No | Claimant (Third Party) |

---

### Typelist: AssessmentStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\AssessmentStatus.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\AssessmentStatus.ttx`
**Description:** Assessment Status
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Open | Open | No | Open |
| Closed | Closed | No | Closed |

---

### Typelist: AssessmentType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\AssessmentType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\AssessmentType.ttx`
**Description:** Assessment Status
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Property | Property | No | Property |
| Contents | Contents | No | Contents |
| Auto | Auto | No | Auto |

---

### Typelist: AssignmentSearchType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\AssignmentSearchType.tti`
**Description:** Possible search types for assignment
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| User | User | No | User |
| Group | Group | No | Group |
| Queue | Queue | No | Queue |

---

### Typelist: AssignmentSelectionType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\AssignmentSelectionType.tti`
**Description:** Possible selection types for the assignment pop-up
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| FromList | FromList | No | FromList |
| FromSearch | FromSearch | No | FromSearch |

---

### Typelist: AssignmentStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\AssignmentStatus.tti`
**Description:** Assignment status of an assignable entity
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| assigned | Assigned | No | Entity is assigned; AssignedUserID and AssignedGroupID are both non-null |
| pendingassignment | Pending assignment | No | Assignable is waiting for its containing entity to be assigned or reviewed; AssignedUserID and AssignedGroupID may be null or non-null |
| manual | Manual | No | Entity is waiting to be manually assigned or reviewed; a non-null AssignedUserID means pending review |
| unassigned | Unassigned | No | Entity is unassigned; AssignedUserID and AssignedGroupID are both null |

---

### Typelist: AuthorityLimitType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\AuthorityLimitType.tti`
**Description:** Types of authority limits
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| ctr | Claim total reserves | No | The total reserves for all exposures on a claim |
| etr | Exposure total reserves | No | The total reserves for a single exposure |
| car | Claim available reserves | No | The available reserves for all exposures on a claim |
| ear | Exposure available reserves | No | The available reserves for a single exposure |
| rcs | Reserve change size | No | The size of a single reserve change |
| cptd | Claim payments to date | No | The total amount of payments to date for the claim |
| eptd | Exposure payments to date | No | The total amount of payments to date for a single exposure |
| pa | Payment amount | No | The amount of a single payment |
| per | Payments exceed reserves | No | The amount by which payments are allowed to exceed reserves on a claim |

---

### Typelist: AutoSync

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\AutoSync.tti`
**Description:** The status code for auto-sync
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Disallow | Disallow | No | Disallow |
| Allow | Allow | No | Allow |
| Suspended | Suspended | No | Suspended |

---

### Typelist: BaggageType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\BaggageType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\BaggageType.ttx`
**Description:** Baggage type categorization
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| trunk | Trunk | No | A wooden box larger than other kinds of luggage |
| suitcase | Suitcase | No | A general term that may refer to wheeled or non-wheeled luggage, as well as soft or hard side luggage |
| tote | Tote | No | A small shoulder bag |
| duffel | Duffel bag | No | A barrel-shaped bag |
| laptopbag | Laptop bag | No | A laptop bag or backpack |
| backpack | Backpack | No | A small shoulderbag |
| wallet_purse | Wallet or Purse | No | A wallet or purse for personal belongings |
| documents | Travel Documents | No | Passport, visa, ticket, drivers License etc |
| other | Other | No | Other |

---

### Typelist: BankAccount

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\BankAccount.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\BankAccount.ttx`
**Description:** Bank account
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| default | Default | No | Default bank account |

---

### Typelist: BatchProcessType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\BatchProcessType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\BatchProcessType.ttx`
**Description:** Types of batch processes
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| ActivityEsc | Activity Escalation | No | Activity escalation monitor |
| Archive | Archiving Item Writer | No | Archiving item writer |
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
| GroupException | Group Exception | No | Group exception monitor |
| UserException | User Exception | No | User exception monitor |
| Workflow | Workflow | No | Workflows work queue writer. |
| ContactAutoSync | ContactAutoSync | No | Automatically synchronize the local contacts that are out of sync and marked 'allow' auto-sync. |
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
| Statistics | Statistics | No | Statistics calculator |
| ClaimException | Claim Exception | No | Claim exception monitor |
| IdleClaim | Idle Claim Exception | No | Idle claim exception monitor |
| IdleClosedClaim | Idle Closed Claim Exception | No | Idle closed claim exception monitor |
| EncryptionUpgrade | Encryption Upgrade | No | Upgrades encryption for entity fields |
| ExchangeRate | Exchange Rate | No | Creates a new ExchangeRateSet using ExchangeRateSetPlugin |
| FinancialsEsc | Financials Escalation | No | Financials escalation monitor - escalates checks from Awaiting-submission status to Requesting status so that the downstream system will be alerted |
| FinancialsCalc | Financials Calculations | No | Financials calculations |
| BulkInvoiceEsc | Bulk Invoice Escalation | No | Escalate Bulk Invoices from Awaiting-submission status to Requesting status |
| BulkInvoiceWF | Bulk Invoice Workflow Monitor | No | Transitions invoices from 'CreatingChecks' status to 'AwaitingSubmission' or 'InvalidInvoiceItems' status once the invoice is ready |
| TAccountEsc | TAccounts Escalation | No | TAccounts escalation monitor to transition payments and reserves from FutureDated state to Awaiting-submission state |
| AggLimitCalc | Aggregate Limit Calculations | No | Aggregate limit calculations |
| ClaimContactsCalc | Claim Contacts Calculations | No | Claim contacts calculations |
| DashboardStatistics | Dashboard Statistics | No | Statistics for the executive dashboard |
| ReviewSync | ClaimCenter (SPM) Completed Review Sync | No | Transmits completed reviews to ContactManager. |
| ClaimHealthCalc | Claim Health Calculations | No | Calculates health indictators and metrics for all claims that do not have any metrics calculated |
| RetiredPolicyGraphDisconnector | Retired Policy Graph Disconnector | No | Disconnects claim graph objects from retired policy objects so that those claims can be archived |
| ClaimValidation | Bulk claim validation | No | Bulk claim validation work queue writer.  Creates workitems to schedule loaded claims for validation. See ClaimAPI.bulkValidate() |
| CatastropheClaimFinder | Catastrophe Claim Finder | No | Finds possible claims related to a catastrophe and creates a 'Review for Catastrophe' activity on the claim. |
| RecalculateMetrics | Recalculate Claim Metrics | No | Recalculates claim metrics for claims whose metric update time has passed. |
| InvoiceItemProcessing | Invoice Item Processing | No | Processes bulk invoice items across lifecycle |
| InvoiceProcessing | Invoice Processing | No | Processes invoices for parallel processing of bulk invoice items |
| ContactRetire | Contact Retire | No | Attempt to retire a Contacts marked as possibly retireable. |
| PurgeMessageHistory | Purge Message History | No | Purges old messages from the message history table |
| CatastrophePolicyLocationDownload | Catastrophe Policy Location Download | No | Downloads PolicyLocationSummary data for catastrophes from the policy system |
| UserWorkloadUpdate | User Workload Update | No | Updates user weighted workload |
| ServiceRequestMetricEscalation | Service Metric Escalation | No | Escalates service metrics when they have exceeded an upper limit |
| SolrDataImport | Solr Data Import | No | Performs a full data import of the app database into the Solr/Lucene index |

---

### Typelist: BatchProcessTypeUsage

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\BatchProcessTypeUsage.tti`
**Description:** This defines the usages of this typelist
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Schedulable | Schedulable | No | This indicates that this BatchProcessType is schedulable |
| UIRunnable | UI Runnable | No | This indicates that this BatchProcessType is runnable from the UI |
| APIRunnable | API Runnable | No | This indicates that this BatchProcessType is runnable from the API |
| MaintenanceOnly | Maintenance Only | No | This indicates that this BatchProcessType is only runnable while the server is at maintenance run level |

---

### Typelist: BIValidationAlertType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\BIValidationAlertType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\BIValidationAlertType.ttx`
**Description:** Types of validation failures for a BulkInvoice.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| unspecified | Unspecified | No | Unspecified |
| itemwitharchivedclaim | Item claim is archived | No | One of the Bulk Invoice Items has been configured with an archived claim. The claim must be retrieved before it can be used. |

---

### Typelist: BoatType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\BoatType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\BoatType.ttx`
**Description:** Type of boat, if vehicle style is boat
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| AI | Airboat | No | Airboat |
| CO | Commercial | No | Commercial |
| CR | Cruiser | No | Cruiser |
| HS | Houseboat | No | Houseboat |
| HO | Hovercraft | No | Hovercraft |
| HY | Hydrofoil | No | Hydrofoil |
| HR | Hydroplane | No | Hydroplane |
| RU | Runabout | No | Runabout |
| SA | Sailboat | No | Sailboat |
| UT | Utility | No | Utility |
| YA | Yacht | No | Yacht |
| YY | Other | No | Other (jetski, canoe, kayak, johnboat, rowboat, etc.) |

---

### Typelist: BodyPartType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\BodyPartType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\BodyPartType.ttx`
**Description:** The primary body part affected
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| head | Head | No | Head |
| lower | Lower extremities | No | Lower extremities |
| multiple | Multiple body parts | No | Multiple body parts |
| neck | Neck | No | Neck |
| trunk | Trunk | No | Trunk |
| upper | Upper extremities | No | Upper extremities |

---

### Typelist: BulkInvoiceItemStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\BulkInvoiceItemStatus.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\BulkInvoiceItemStatus.ttx`
**Description:** Possible statuses for BulkInvoiceItem entities
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| approved | Item approved | No | Bulk invoice item has passed the bulk invoice approval process |
| awaitingsubmission | Awaiting submission | No | Bulk invoice item and its check have passed approval and is ready to be escalated once the bulk invoice is ready to be escalated |
| checkpendingapproval | Check pending approval | No | Bulk invoice item has passed the bulk invoice approval process and is waiting for its check to be approved |
| draft | Draft | No | Bulk invoice item is possibly committed to the database, but is not yet ready for validation |
| inreview | In review | No | Bulk invoice item requires action before it can be paid.  This value can be set when approving a bulk invoice. |
| notvalid | Not valid | No | Payment/check associated with the bulk invoice item failed validation |
| pendingstop | Pending stop | No | Bulk invoice item was stopped, and confirmation of stop is pending |
| pendingtransfer | Pending transfer | No | Check associated with bulk invoice item was transferred, and acknowledgement of the transfer event message is pending |
| pendingvoid | Pending void | No | Bulk invoice item was voided, and confirmation of void is pending |
| errorduringprocessing | Error during processing | No | The invoice encountered a problem during processing |
| rejected | Rejected | No | Bulk invoice item was rejected by the bulk invoice approver |
| stopped | Stopped | No | Bulk invoice item was stopped |
| submitted | Submitted | No | Bulk invoice item was submitted to the downstream system |
| submitting | Submitting | No | Bulk invoice item is being submitted to downsteam system |
| transferred | Transferred | No | Check associated with bulk invoice item was transferred |
| voided | Voided | No | Bulk invoice item was voided |

---

### Typelist: BulkInvoiceJobType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\BulkInvoiceJobType.tti`
**Description:** Job type describing the process for which a bulk invoice work item is created
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| submission | Submission | No | Bulk invoice is being submitted |

---

### Typelist: BulkInvoiceStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\BulkInvoiceStatus.tti`
**Description:** Possible statuses for BulkInvoice entities
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| awaitingsubmission | Awaiting submission | No | Awaiting submission to the downstream system |
| cleared | Cleared | No | Bulk invoice's associated bulk check has been cleared |
| creatingchecks | Creating checks | No | Checks are being created for the invoice |
| draft | Draft | No | Bulk invoice is possibly committed to DB, but not yet ready for validation |
| initiatingcheckcreation | Initiating check creation | No | The invoice is ready for the check creation process to begin |
| initiatingdelete | Initiating delete | No | The invoice is ready for the delete process to begin |
| initiatingescalation | Initiating escalation | No | The invoice is ready for the escalation process to begin |
| initiatingstop | Initiating stop | No | The invoice is ready for the stop process to begin |
| initiatingvoid | Initiating void | No | The invoice is ready for the void process to begin |
| inreview | In review | No | Bulk invoice is under review |
| invaliditems | Invalid bulk invoice items | No | One or more approved items on the bulk invoice failed validation or had some problem with the associated check |
| issued | Issued | No | Bulk invoice's associated bulk check has been issued |
| onhold | On hold | No | Bulk invoice was put on hold by downstream system |
| pendingstop | Pending stop | No | Bulk invoice was stopped, and confirmation of stop is pending |
| pendingvoid | Pending void | No | Bulk invoice was voided, and confirmation of void is pending |
| processingdelete | Processing delete | No | The invoice is being deleted |
| errorduringprocessing | Error during processing | No | The invoice encountered a problem during processing |
| processingescalation | Processing escalation | No | The invoice is being escalated |
| processingstop | Processing stop | No | The invoice is being stopped |
| processingvoid | Processing void | No | The invoice is being voided |
| rejected | Rejected | No | Bulk invoice rejected by assigned approver |
| requested | Requested | No | Sent to downstream system and acknowledged |
| requesting | Requesting | No | Queued for submission to the downstream system |
| retired | Retired | No | The invoice has been retired |
| stopped | Stopped | No | Bulk invoice was stopped |
| voided | Voided | No | Bulk invoice was voided |

---

### Typelist: BusinessType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\BusinessType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\BusinessType.ttx`
**Description:** Types of external organizations
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| broker | Broker | No | Broker |
| agency | Agency | No | Agency |

---

### Typelist: CalendarContext

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\CalendarContext.tti`
**Description:** The context for a calendar
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| supervisor | Supervisor | No | A calendar that displays activities assigned to the logged in supervisor's subordinates |
| desktop | Desktop | No | A calendar that displays assigned activities across all claims |
| claim | Claim | No | A calendar that displays assigned activities for a single claim |
| matter | Matter | No | A calendar that displays assigned activities for a single matter |

---

### Typelist: CatastropheType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\CatastropheType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\CatastropheType.ttx`
**Description:** Type of a given catastrophe
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| iso | ISO | No | ISO |
| internal | Internal | No | Internal |

---

### Typelist: CharacterSet

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\CharacterSet.tti`
**Description:** Character sets available for print/export
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| *(None defined)* | *Dynamic or database-driven* | No | Typelist populated dynamically at runtime or via database table |

---

### Typelist: CheckBatching

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\CheckBatching.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\CheckBatching.ttx`
**Description:** How a check should be batched for sending
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| apdefault | A/P default | No | A/P default |
| bulkcheck | Bulk check | No | Check is a record keeping entity for a bulk check |

---

### Typelist: CheckHandlingInstructions

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\CheckHandlingInstructions.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\CheckHandlingInstructions.ttx`
**Description:** Special handling instructions for a check
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| default | Default | No | Default check handling procedures |
| hold | Hold for supporting documentation | No | Hold for supporting documentation |

---

### Typelist: CheckType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\CheckType.tti`
**Description:** Describes the relationship between a check and a primary check
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| primary | Primary | No | The primary check in a check group |
| secondary | Secondary | No | A non-primary check in a check group |

---

### Typelist: CitationType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\CitationType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\CitationType.ttx`
**Description:** 
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| yeildfailure | Failure to yield | No | Failure to yield |
| controlfailure | Failure to maintain control of lane | No | Failure to maintain control of lane |
| tooclose | Following too closely | No | Following too closely |
| recklessdriving | Reckless driving | No | Reckless driving |
| speeding | Speeding | No | Speeding |
| dui_dwi | DUI/DWI | No | DUI/DWI |
| other | Other | No | Other |

---

### Typelist: ClaimAccessType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ClaimAccessType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ClaimAccessType.ttx`
**Description:** The type of access granted on a claim
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| edit | Edit | No | Edit permissions |
| view | View | No | View permissions |

---

### Typelist: ClaimantIDType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ClaimantIDType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ClaimantIDType.ttx`
**Description:** Claimant ID Type
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| A | Assigned by Jurisdiction | No | Employee ID Assigned by Jurisdiction |
| E | Employment Visa | No | Employee Employment Visa |
| G | Green Card | No | Employee Green Card |
| P | Passport Number | No | Employee Passport Number |
| S | Social Security Number | No | Employee Social Security Number |

---

### Typelist: ClaimantType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ClaimantType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ClaimantType.ttx`
**Description:** Categorizes claimant relative to the policyholder
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| insured | Insured | No | Insured |
| householdmember | Member of the insured's household | No | Member of the insured's household |
| veh_ins_driver | Driver of insured's vehicle (not insured or household member) | No | Driver of insured's vehicle (not insured or household member) |
| veh_other_owner | Owner of other vehicle | No | Owner of other vehicle |
| veh_other_driver | Driver of other vehicle | No | Driver of other vehicle |
| veh_ins_occupant | Occupant of insured's vehicle | No | Occupant of insured's vehicle |
| veh_other_occ | Occupant of other vehicle | No | Occupant of other vehicle |
| bystander | Pedestrian or bystander | No | Pedestrian or bystander |
| propertyowner | Owner of the lost/damaged property | No | Owner of the lost/damaged property |
| customer | Customer | No | Customer |
| employee | Employee | No | Employee |
| contractor | Contractor | No | Contractor |
| subcontractor | Subcontractor | No | Subcontractor |
| other | Other third party | No | Other third party |

---

### Typelist: ClaimAssocType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ClaimAssocType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ClaimAssocType.ttx`
**Description:** Types of Claim Associations
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| general | General | No | General claim association |
| parentchild | Parent/child | No | Where primary claim is the parent |
| eventrelated | Event-related | No | Claims related to one event, including environmental claims |
| priorclaims | Prior claims | No | Prior claims related to the primary claim |
| reinsurancerelated | Reinsurance-related | No | Claims related by reinsurance |

---

### Typelist: ClaimClosedOutcomeType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ClaimClosedOutcomeType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ClaimClosedOutcomeType.ttx`
**Description:** The possible outcomes of a claim when it is closed
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| paymentscomplete | Payments Complete | No | Payments complete |
| completed | Completed | No | Completed |
| duplicate | Duplicate | No | Duplicate |
| mistake | Mistake | No | Mistake |
| fraud | Fraud | No | Fraud |

---

### Typelist: ClaimLifeCycleState

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ClaimLifeCycleState.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ClaimLifeCycleState.ttx`
**Description:** Provides a way to store a state value for extended lifecycle processing; for example, for SIU processing over time
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| step1 | Step 1 | No | First step in the lifecycle |
| step2 | Step 2 | No | Second step in the lifecycle |
| step3 | Step 3 | No | Third step in the lifecycle |

---

### Typelist: ClaimMetricCategory

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ClaimMetricCategory.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ClaimMetricCategory.ttx`
**Description:** Category of the metric on a claim
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| OverallClaimMetrics | Overall Claim Metrics | No |  |
| ClaimActivityMetrics | Claim Activity | No |  |
| ClaimFinancialsMetrics | Claim Financials | No |  |

---

### Typelist: ClaimProgressType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ClaimProgressType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ClaimProgressType.ttx`
**Description:** Description of the progress on an open claim
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| new | New | No | New |
| investigation | Investigation | No | Investigation |
| evaluation | Evaluation | No | Evaluation |
| settlement | Settlement | No | Settlement |
| litigation | Litigation | No | Litigation |
| pendingrecovery | Pending recovery | No | Pending recovery |

---

### Typelist: ClaimReopenedReason

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ClaimReopenedReason.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ClaimReopenedReason.ttx`
**Description:** The possible reasons for a claim to be reopened
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| paymentdenied | Payment Denied | No | Final Payment causing this claim to close has been denied |
| mistake | Mistake | No | Mistake |
| newinfo | New information | No | New information |

---

### Typelist: ClaimSearchNameSearchType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ClaimSearchNameSearchType.tti`
**Description:** The search options for the name searches in claim search
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| insured | Insured | No | Find by insured claim contact role |
| claimant | Claimant | No | Find by claimant claim contact role |
| addinsured | Additional Insured | No | Find by additional insured |
| any | Any Party Involved | No | Find by any claim contact |

---

### Typelist: ClaimSearchType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ClaimSearchType.tti`
**Description:** Type of claim searches available
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| active | Active Database | No | Claims stored on active database |
| archived | Archive | No | Claims stored in archive |
| all | All Sources | No | Claims stored in both live and archive |

---

### Typelist: ClaimSecurityType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ClaimSecurityType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ClaimSecurityType.ttx`
**Description:** Permissions to restrict access to claims
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| unsecuredclaim | UnsecuredClaim | No | Permission to view claims with no additional security specified |
| employeeclaim | Employee claim | No | Permission to see a claim involving an employee |
| fraudriskclaim | Fraud risk | No | Permission to see a claim with a high fraud risk |
| sensitiveclaim | Sensitive | No | Permission to see a sensitive claim |
| underlitclaim | Under litigation | No | Permission to see a claim that is currently under litigation |

---

### Typelist: ClaimSegment

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ClaimSegment.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ClaimSegment.ttx`
**Description:** Types of segments a claim can have
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| unknown | Unknown | No | Unknown segment, or segment not automatically set by rules |
| auto_low | Auto - low complexity | No | Auto - low complexity |
| auto_mid | Auto - mid complexity | No | Auto - mid complexity |
| auto_high | Auto - high complexity | No | Auto - high complexity |
| prop_low | Property - low complexity | No | Property - low complexity |
| prop_mid | Property - mid complexity | No | Property - mid complexity |
| prop_high | Property - high complexity | No | Property - high complexity |
| liab_low | Liability - low complexity | No | Liability - low complexity |
| liab_mid | Liability - mid complexity | No | Liability - mid complexity |
| liab_high | Liability - high complexity | No | Liability - high complexity |
| wc_med_only | Workers' Comp - med only | No | Workers' Comp - med only |
| wc_lost_time | Workers' Comp - indemnity | No | Workers' Comp - indemnity |
| auto_glass | Auto - glass | No | Auto - glass |
| injury_low | Injury - low complexity | No | Injury - low complexity |
| injury_mid | Injury - mid complexity | No | Injury - mid complexity |
| injury_high | Injury - high complexity | No | Injury - high complexity |
| contents_low | Contents - low complexity | No | Contents - low complexity |
| contents_high | Contents - high complexity | No | Contents - high complexity |
| wc_liability | Workers' Comp - employer's liability | No | Workers' Comp - employer's liability |
| travel_low | Travel - low complexity | No | Travel - low complexity |
| travel_mid | Travel - mid complexity | No | Travel - mid complexity |
| travel_high | Travel - high complexity | No | Travel - high complexity |

---

### Typelist: ClaimSource

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ClaimSource.tti`
**Description:** Information about how Claim was entered into the System
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| ordinary | Ordinary | No | Ordinary Claim |
| autofirstandfinal | Auto First and Final | No | Claim entered as auto first and final |

---

### Typelist: ClaimState

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ClaimState.tti`
**Description:** Standard states for a claim, such as open or closed
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| draft | Draft | No | Draft |
| open | Open | No | Open |
| closed | Closed | No | Closed |
| archived | Archived | No | Archived |

---

### Typelist: ClaimStrategy

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ClaimStrategy.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ClaimStrategy.ttx`
**Description:** list of the different strategies available
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| unknown | Unknown | No | Unknown strategy, or strategy not assigned by rules |
| auto_fast | Auto - Fast Track | No | Auto - Fast Track |
| auto_normal | Auto - Investigate | No | Auto - Investigate |
| prop_fast | Property - Fast Track | No | Property - Fast Track |
| prop_normal | Property - Investigate | No | Property - Investigate |
| liab_fast | Liability - Fast Track | No | Liability - Fast Track |
| liab_normal | Liability - Investigate | No | Liability - Investigate |
| wc_fast | Workers' Comp - Fast Track | No | Workers' Comp - Fast Track |
| wc_normal | Workers' Comp - Manage Loss | No | Workers' Comp - Manage Loss |
| injury_fast | Injury - Fast Track | No | Injury - Fast Track |
| injury_normal | Injury - Investigate | No | Injury - Investigate |
| contents_fast | Contents - Fast Track | No | Contents - Fast Track |
| contents_normal | Contents - Investigate | No | Contents - Investigate |
| wc_investigate | Workers' Comp - Investigate | No | Workers' Comp - Investigate |

---

### Typelist: ClaimTextType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ClaimTextType.tti`
**Description:** Text fields on claim, stored in the ClaimText array
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| BenefitsDecisionReason | BenefitsDecisionReason | No | Explanation of benefits decision |
| MedicalDiagnosis | MedicalDiagnosis | No | Medical Diagnosis for workers' comp claim |
| SubjComplaints | SubjComplaints | No | Subjective description of complaint for workers' comp claim |
| ObjFindings | ObjFindings | No | Objective description of condition for workers' comp claim |
| TreatmentRend | TreatmentRend | No | Description of treatment rendered for workers' comp claim |
| MMInote | MMInote | No | Maximum medical improvement notes for workers' comp claim |
| PreexDisbltyInfo | PreexDisbltyInfo | No | Description of preexisting disability for workers' comp claim |
| StorageNotes | StorageNotes | No | Claim storage notes |
| SIEscalateSIUNote | SIEscalateSIUNote | No | Description of reason for decision on SIU escalation |
| ISOErrorMessage | ISOErrorMessage | No | Error message if most recent ISO ClaimSearch request failed |
| ReinsuranceReason | ReinsuranceReason | No | Description of reason for marking or unmarking a claim for reinsurance |
| InjuryDescription | InjuryDescription | Yes | Description of injury for workers' comp claim |

---

### Typelist: ClaimTier

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ClaimTier.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ClaimTier.ttx`
**Description:** Claim tier, used to decide which claim metric limits apply to the claim's metrics
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| incidentreport | Incident Only | No | A reported incident; a claim is not anticipated |
| medicalonly | Medical Only | No | A claim with a medical component with no indemnity |
| indemnity | Indemnity | No | A claim with an indemnity component; may have medical as well |
| el | Employer's Liability | No | A claim with Employer's Liability |
| low | Low Severity | No | Low Severity |
| medium | Medium Severity | No | Medium Severity |
| high | High Severity | No | High Severity |

---

### Typelist: CollisionPoint

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\CollisionPoint.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\CollisionPoint.ttx`
**Description:** The point of first impact
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 03 | Front bumper, grille, hood & radiator | No | Front bumper, grille, hood & radiator |
| 04 | Left fender - front (headlamp area) | No | Left fender - front (headlamp area) |
| 05 | Left fender - side & wheel area | No | Left fender - side & wheel area |
| 06 | Left front door | No | Left front door |
| 08 | Left quarter panel | No | Left Quarter panel |
| 07 | Left rear door | No | Left rear door |
| 09 | Rear bumper, rear body panel, trunk lid/ liftgate | No | Rear bumper, rear body panel, trunk lid/liftgate |
| 02 | Right fender - front (headlamp area) | No | Right fender - front (headlamp area) |
| 01 | Right fender - side & wheel area | No | Right fender - side & wheel area |
| 12 | Right front door | No | Right front door |
| 10 | Right quarter panel | No | Right quarter panel |
| 11 | Right rear door | No | Right rear door |
| 13 | Roof panel | No | Roof panel |
| 17 | Undercarriage | No | Undercarriage |
| 14 | Point of impact unknown (collision loss) | No | Point of impact unknown (collision loss) |
| 15 | Total loss | No | Total loss |
| 16 | Non-collision (comprehensive loss) | No | Non-collision (comprehensive loss) |
| front | Front | Yes | Front |
| leftfront | Left front | Yes | Left front |
| rightfront | Right front | Yes | Right front |
| leftside | Left side | Yes | Left side |
| rightside | Right side | Yes | Right side |
| rear | Rear | Yes | Rear |
| leftrear | Left rear | Yes | Left rear |
| rightrear | Right rear | Yes | Right rear |
| top | Top / roof | Yes | Top / roof |

---

### Typelist: CompensabilityDecision

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\CompensabilityDecision.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\CompensabilityDecision.ttx`
**Description:** 
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| accepted | Accepted | No | Accepted |
| partialdenial | Accepted - with partial denial | No | Accepted - with partial denial |
| denied | Denied | No | Denied |
| pending | Pending | No | Pending |
| disputed | Disputed | No | Disputed |

---

### Typelist: ComponentType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ComponentType.tti`
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

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ConsistencyCheckType.tti`
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

### Typelist: ContactBidiRel

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ContactBidiRel.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ContactBidiRel.ttx`
**Description:** Bi-directional representations of contact relationships. This list is used in the presentation of a contact's relationships. Entries in this list come in pairs. One half of the pair corresponds to an entry in the ContactRel typelist. The other half represents the inverse of the first half of the relationship. Pairs are defined in the ab/contact-relationship-config.xml files.
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

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

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ContactChangeResolution.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ContactChangeResolution.ttx`
**Description:** Resolution status of a PendingContactChange
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| approved | Approved | No | Approved |
| rejected | Rejected | No | Rejected |
| more_info_req | More Information Required | No | More Information Required |
| already_applied | Already Applied | No | Already Applied |

---

### Typelist: ContactClass

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ContactClass.tti`
**Description:** The classification of a contact
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| general | Basic | No | Basic contact with no specific classification |
| user | User | No | User |
| vendor | Vendor | No | Vendor |
| venue | Legal Venue | No | Authority that handles legal matters (for example, a court house) |

---

### Typelist: ContactCreationApprovalStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ContactCreationApprovalStatus.tti`
**Description:** Approval status of contact for creation
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| pending_approval | Pending Approval | No | Pending Approval |
| approved | Approved | No | Approved |
| rejected | Rejected | No | Rejected |

---

### Typelist: ContactDestructionStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ContactDestructionStatus.tti`
**Description:** Status in the Contact Purge Process
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

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

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ContactDestructionStatusCategory.tti`
**Description:** The categories if the Contact DestructionStatus is in a final state to nofity external systems
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| DestructionStatusFinished | Destruction Status Finished | No | The contact destruction request has been finished |
| DestructionStatusNotProcessed | Destruction Status Not Processed | No | The contact destruction request has not been processed |
| ReadyToBeNotified | Ready To Be Notified | No | The Contact Destruction Request is ready to be notified |
| ReadyToAttemptDestruction | Ready To Attempt Destruction | No | This contact purge request is ready to be sent to the destroyer |

---

### Typelist: ContactLinkStatusType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ContactLinkStatusType.tti`
**Description:** Represents the link status of a Contact with its associated Address Book Contact.
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| NOT_FOUND | Not found | No | No associated Address Book Contact found. |
| OUT_OF_SYNC | Out of sync | No | The Contact is out of sync with the associated Address Book Contact. |
| IN_SYNC | In sync | No | The Contact is in sync with the associated Address Book Contact. |

---

### Typelist: ContactMatchResultType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ContactMatchResultType.tti`
**Description:** Represents the result of definitive match search.
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

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

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ContactRel.tti`
**Description:** Types of relationships a contact can have with another contact
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| guardian | Parent / Guardian | No | Parent of a child or Guardian of a ward. |
| employer | Employer | No | Employer |
| primarycontact | Primary Contact | No | Primary contact |
| thirdpartyinsurer | Third-Party Insurer | No | Third-Party Insurer |
| collectionagency | Collection Agency | No | Collection Agency |

---

### Typelist: ContactRelCons

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ContactRelCons.tti`
**Description:** This typelist is obsolete and should not be used
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| exclusive | Exclusive | No | Exclusive |

---

### Typelist: ContactRole

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ContactRole.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ContactRole.ttx`
**Description:** The relationship a contact has with the claim
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| checkpayee | Check Payee | No | The payee on a check |
| negcontact | Negotiation Contact | No | Negotiation contact |
| claimant | Claimant | No | Claimant |
| other | Other | No | Other |
| recoverypayer | Recovery Payer | No | The payer on a recovery |
| recoveryonbehalfof | Recovery On Behalf Of | No | The responsible party on a recovery |
| vendor | Vendor | No | Vendor |
| activityowner | Activity Owner | No | The external owner of an activity |
| agent | Agent | No | Agent |
| coveredparty | Covered Party | No | Covered party |
| doingbusinessas | Doing Business As | No | Doing business as |
| excludedparty | Excluded Party | No | Excluded party |
| insured | Insured | No | Insured |
| policyholder | Policy holder | No | Policy Holder |
| underwriter | Underwriter | No | Underwriter |
| formeragent | Former Agent | No | Former agent |
| formercoveredparty | Former Covered Party | No | Former covered party |
| formerdoingbusinessas | Former Doing Business As | No | Former doing business As |
| formerexcludedparty | Former Excluded Party | No | Former excluded party |
| formerinsured | Former Insured | No | Former insured |
| formerpolicyholder | Former Policy Holder | No | Former policy holder |
| formerunderwriter | Former Underwriter | No | Former underwriter |
| filedby | Filed By | No | Filed by |
| venue | Venue | No | Authority which handles legal matters e.g., a court house. |
| defenseattorney | Primary Defense Attorney | No | Primary Defense Attorney |
| plaintiffatt | Primary Plaintiff's Attorney | No | Primary Plaintiff's Attorney |
| formercheckpayee | Former Check Payee | No | Former Check Payee |
| passenger | Passenger | No | Passenger |
| witness | Witness | No | Witness |
| attorney | Attorney | No | Attorney |
| judges | Judges | No | Belongs to the pool of judges at a particular venue. |
| mattermanager | Legal Case Manager | No | Legal Case Manager |
| codefendant | Co-defendant | No | Co-defendant |
| defendant | Defendant | No | Defendant |
| secdefattorney | Secondary Defense Attorney | No | Secondary Defense Attorney |
| defensefirm | Primary Defense Law Firm | No | Primary Defense Law Firm |
| secdefensefirm | Secondary Defense Law Firm | No | Secondary Defense Law Firm |
| judge | Judge | No | Judge |
| leadparalegal | Lead Paralegal | No | Lead Paralegal |
| lienholder | Lienholder | No | Lienholder |
| plaintiff | Plaintiff | No | Plaintiff |
| plaintifffirm | Primary Plaintiff Law Firm | No | Primary Plaintiff Law Firm |
| secplaintifffirm | Secondary Plaintiff Law Firm | No | Secondary Plaintiff Law Firm |
| secplaintiffatt | Secondary Plaintiff's Attorney | No | Secondary Plaintiff's Attorney |
| injured | Injured Party | No | Injured Party |
| supervisor | Supervisor | No | Supervisor |
| claimantdep | Claimant Dependent | No | Claimant Dependent |
| altcontact | Alternate Contact | No | Alternate Contact |
| casemgmtco | Case Management Company | No | Case Management Company |
| casemgr | Case Manager | No | Case Manager |
| doctor | Doctor | No | Doctor |
| PrimaryDoctor | Primary Doctor | No | Primary Doctor |
| FirstIntakeDoctor | First Intake Doctor | No | First Intake Physician |
| OccTherapist | Occupational Therapist | No | Occupational Therapist |
| PhysTherapist | Physical Therapist | No | Physical Therapist |
| driver | Driver | No | Driver |
| disbenprovider | Disability Benefits Provider | No | Disability Benefits Provider |
| employer | Employer | No | Employer |
| hospital | Hospital - Medical Center | No | Hospital - Medical Center |
| maincontact | Main Contact | No | Main Contact |
| nursecasemgr | Nurse Case Manager | No | Nurse Case Manager |
| reporter | Reporter | No | Reporter |
| rsbenprovider | Replacement Services Benefits Provider | No | Replacement Services Benefits Provider |
| wccarrier | WC Carrier | No | WC Carrier |
| repairshop | Repair Shop | No | Repair Shop |
| recoveryagent | Recovery Agent | No | The agent of a recovery |
| plaintiffs | Plaintiff's Attorney | No | Plaintiff's Attorney |
| TowingAgcy | Towing Agency | No | Towing Agency |
| InsuredRep | Insured Representative | No | Insured Representative |
| LawEnfcAgcy | Law Enforcement Agency | No | Law Enforcement Agency |
| salvageservice | Salvage Service | No | Salvage service |
| salvagebuyer | Salvage Buyer | No | Salvage buyer |
| assessor | Assessor | No | Assessor |
| AppraisalSource | Assessment Source | No | Assessor utilized at notice of claim |
| fnolassessor | Primary Assessor | No | Assessor utilized at notice of claim |
| adverseparty | Responsible Party | No | Responsible Party related to Subrogation |
| collection | Collection Agency | No | Collection Agency |
| subrogator | External Subrogation Firm | No | External Subrogation Firm |
| pedestrian | Pedestrian | No | Pedestrian |
| arbitrator | Arbitrator | No | Arbitrator |
| mediator | Mediator | No | Mediator |
| arbitrationvenue | Arbitration Venue | No | Authority which handles arbitration legal matters e.g., a hearing office. |
| mediationvenue | Mediation Venue | No | Authority which handles mediation legal matters e.g., a conference office. |
| hearingjudge | Hearing Judge | No | Hearing Adjudicator |
| hearingvenue | Hearing Venue | No | Authority which handles hearing legal matters e.g., a hearing office. |
| incidentowner | Owner | No | Owner of the Vehicle or Property.  Used for 3rd party incidents |
| ems | Emergency Management Service | No | Emergency Management Service |
| debrisremoval | Debris Removal | No | Debris removal service |
| lodgingprovider | Lodging Provider | No | Lodging Provider |
| servicerequestparticipant | Service Participant | No | Participant in a Service, such as the customer contact |
| servicerequestspecialist | Service Vendor | No | Vendor selected to perform the work for a Service |

---

### Typelist: ContactRoleCategory

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ContactRoleCategory.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ContactRoleCategory.ttx`
**Description:** Used for grouping related ContactRoles
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| primary | Primary roles | No | Primary roles |
| secondary | Secondary roles | No | Secondary roles |
| vendor | Vendors | No | Vendors |
| litigation | Litigation roles | No | Litigation roles |
| former | "Former" roles | No | "Former" roles |

---

### Typelist: ContactSearchResultType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ContactSearchResultType.tti`
**Description:** Represents the result of definitive match search.
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| SUCCESS | Success | No | Address book search succeeded |
| TOO_LOOSE_SEARCH | Too Loose Search Criteria | No | Search criteria is too loose and executing may require too much of the DB resources. Search not executed. |

---

### Typelist: ContactSearchType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ContactSearchType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ContactSearchType.ttx`
**Description:** The type of contact search
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| internal | Address Book | No | Address Book |

---

### Typelist: ContactTagType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ContactTagType.tti`
**Description:** Types of contact tags
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| client | Client | No | Client |
| claimparty | Claim Party | No | Claim Party |
| vendor | Vendor | No | Vendor |

---

### Typelist: ContentLineItemCategory

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ContentLineItemCategory.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ContentLineItemCategory.ttx`
**Description:** ContentItemCategory
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| bookcases | Bookcases | No | Bookcases |
| books | Books | No | Books |
| chairs | Chairs | No | Chairs |
| desks | Desks | No | Desks |
| filecabinet | File Cabinets | No | File Cabinets |
| lamps | Lamps | No | Lamps |
| partitions | Partitions | No | Partitions |
| sofas | Sofas | No | Sofas |
| tables | Tables | No | Tables |
| computers | Computers | No | Computers |
| fax | Fax Machine | No | Fax Machine |
| keyboard | Keyboards | No | keyboard |
| monitors | Monitors | No | Monitors |
| mouse | Mouse | No | Mouse |
| printers | Printers | No | Printers |
| servers | Servers | No | Servers |
| calendars | Calendars | No | Calendars |
| correctionfluid | Correction Fluid | No | Correction Fluid |
| envelopes | Envelopes | No | Envelopes |
| folders | Folders | No | Folders |
| glue | Glue | No | glue |
| paper | Paper | No | Paper |
| pencilpen | Pencils and Pens | No | Pencils and Pens |
| scissors | Scissors | No | Scissors |
| stapler | Stapler | No | Stapler |
| staples | Staples | No | Staplers |
| calculator | Calculator | No | Calculator |
| clocks | Clocks | No | Clocks |
| copiers | Copiers | No | Copiers |
| dvd | DVD Player | No | DVD Player |
| microwave | Microwave | No | Microwave |
| shredder | Paper Shredders | No | Paper Shredders |
| radio | Radio | No | Radio |
| safe | Safe | No | Safe |
| telephone | Telephone | No | Telephone |
| television | Television | No | Television |
| bedding | Bedding/Drapes/Linens | No | Bedding/Drapes/Linens |
| cameras | Cameras | No | Cameras |
| clothing | Clothing | No | Clothing |
| collectibles | Collectibles | No | Collectibles |
| cooking | Cooking | No | Cooking |
| dvds | DVD's/Tapes | No | DVD's/Tapes |
| decorations | Decorations | No | Decorations |
| electronics | Electronics | No | Electronics |
| arts | Fine Arts | No | Fine Arts |
| china | Fine China/Dishes | No | Fine China/Dishes |
| furniture | Furniture | No | Furniture |
| gardening | Gardening | No | Gardening |
| glass | Glass/Crystal | No | Glass/Crystal |
| jewelry | Jewelry | No | Jewelry |
| appliances | Major Appliances | No | Major Appliances |
| instruments | Musical Instruments | No | Musical Instruments |
| rugs | Rugs | No | Rugs |
| silverware | Silverware | No | Silverware |
| sports | Sports Equipment | No | Sports Equipment |
| other | Other | No | other |
| cash | Cash | No | Cash |
| personal_effects | Personal Effects | No | Personal Effects |

---

### Typelist: ContentLineItemSchedule

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ContentLineItemSchedule.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ContentLineItemSchedule.ttx`
**Description:** ContentItemSchedule
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| officefix | Office Furniture and Fixtures | No | Furniture and Fixtures |
| infosys | Information Systems | No | Information Systems |
| officesup | Office Supplies | No | Office Supplies |
| equip | Equipment | No | Equipment |
| homeowners | Homeowners | No | Household items |
| other | Other | No | Other |
| travel | Travel | No | Items schedule for Travel line |

---

### Typelist: CostCategory

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\CostCategory.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\CostCategory.ttx`
**Description:** Categories of costs
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| unspecified | Unspecified Cost Category | No | Unspecified Cost Category |
| indemnity | Indemnity | No | Indemnity |
| legal | Legal | No | Legal |
| other | Other | No | Other |
| towing | Towing | No | Towing |
| rental | Rental | No | Rental |
| autoglass | Glass | No | Glass |
| body | Auto body | No | Auto body repair |
| labor | Labor | No | Labor |
| autoparts | Auto parts | No | Auto parts |
| inspection | Vehicle inspection | No | Vehicle inspection |
| lostwages | Lost wages | No | Lost wages |
| medical | Medical | No | Medical care |
| mileage | Mileage reimbursement | No | Mileage reimbursement |
| casemgmt | Case management | No | Case management |
| ttd | Temporary total disability | No | Temporary total disability |
| tpd | Temporary partial disability | No | Temporary partial disability |
| ptd | Permanent total disability | No | Permanent total disability |
| ppd | Permanent partial disability | No | Permanent partial disability |
| vocational | Vocational | No | Vocational |
| death | Death benefits | No | Death benefits |
| lifetime | Lifetime benefits | No | Lifetime benefits |
| supplemental | Supplemental earnings | No | Supplemental earnings |
| settlement | Settlement | No | Settlement |
| reimbursement | Reimbursement | No | Reimbursement |
| burial | Burial expenses | No | Burial expenses |
| wcmileage | Mileage reimbursement-WC | No | Mileage reimbursement-WC |
| salvage | Salvage | No | Salvage |
| trip_cancel_delay | Trip | No | Trip cancellation or delay |
| baggage | Baggage | No | Baggage loss or delay |
| ems | Emergency Services | No | Emergency Management Services |
| property_inspection | Property Inspection | No | Property Inspection |
| contents | Contents | No | Contents |
| property_repair | Property Repair | No | Property Repair |
| addnl_living_expenses | Additional Living Expenses | No | Additional Living Expenses |
| autoappraisal | Vehicle appraisal | No | Vehicle appraisal |

---

### Typelist: CostType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\CostType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\CostType.ttx`
**Description:** Types of transaction costs
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| claimcost | Claim Cost | No | Loss payments to claimants or repairers |
| unspecified | Unspecified Cost Type | No | Unspecified Cost Type |
| aoexpense | Expense - A&O | No | Adjusting and other expenses |
| dccexpense | Expense - D&CC | No | Defense and cost containment |

---

### Typelist: Country

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\Country.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\Country.ttx`
**Description:** List of regions, or countries
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

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

### Typelist: CoverageBasis

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\CoverageBasis.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\CoverageBasis.ttx`
**Description:** Basis of the coverage
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Replacement | Replacement cost | No | Replacement cost |
| ACV | Actual cash value | No | Actual cash value |

---

### Typelist: CoverageForm

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\CoverageForm.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\CoverageForm.ttx`
**Description:** Coverage form
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Occurrence | Occurrence coverage (default) | No | Occurrence coverage (default) |
| PriorActs | Occurrence coverage (prior acts) | No | Occurrence coverage (prior acts) |
| ClmsMdRtr | Claims-made cov-basic with retroactive cov | No | Claims-made coverage - basic with retroactive coverage |
| ClmsMdRtrExt | Claims-made cov-extended rptg period (w/ retro cov) | No | Claims-made coverage - extended reporting period (with retroactive coverage) |
| ClmsMdNoRtr | Claims-made cov-basic no retro cov | No | Claims-made coverage - basic no retroactive coverage |
| ClmsMdNoRtrExt | Claims-made cov-extended rptg period (no retro cov) | No | Claims-made coverage - extended reporting period (no retroactive coverage) |

---

### Typelist: CoveragePartType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\CoveragePartType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\CoveragePartType.ttx`
**Description:** CoveragePartType
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| hoprental | Rental | No | Rental |
| hopcondo | Condominium | No | Condominium |
| hopdwelling | Dwelling | No | Dwelling |

---

### Typelist: CoverageSubtype

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\CoverageSubtype.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\CoverageSubtype.ttx`
**Description:** Subtype of coverage, filtered by CoverageType
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| GLCGLCov_ops_bi | GL Premise/Ops - Bodily Injury | No | General Liability Premises/Operations - Bodily Injury |
| GLCGLCov_ops_pd | GL Premise/Ops - Property Damage | No | General Liability Premises/Operations - Property Damage |
| GLCGLCov_ops_mp | GL Premise/Ops - Med Pay | No | General Liability Premises/Operations - Med Pay |
| GLCGLCov_ops_gd | GL Premise/Ops - General Damage | No | General Liability Premises/Operations - General Damage |
| GLCGLCov_prod_bi | GL Prod/Comp Ops - Bodily Injury | No | General Liability Products/Completed Operations - Bodily Injury |
| GLCGLCov_prod_pd | GL Prod/Comp Ops - Property Damage | No | General Liability Products/Completed Operations - Property Damage |
| GLCGLCov_prod_mp | GL Prod/Comp Ops - Med Pay | No | General Liability Products/Completed Operations - Med Pay |
| GLCGLCov_prod_gd | GL Prod/Comp Ops - General Damage | No | General Liability Products/Completed Operations - General Damage |
| GLCGLCov_adv_gd | GL Personal/Advertising Injury | No | General Liability Personal/Advertising Injury |
| GLDeductible-BI | Optional GL Deductible - BI | No | Optional GL Deductible - BI |
| GLDeductible-PD | Optional GL Deductible - PD | No | Optional GL Deductible - PD |
| GLDeductible-GEN | Optional GL Deductible - Gen. Damage | No | Optional GL Deductible - Gen. Damage |
| GLPollutionDesignatedCovBI | Designated Pollutant Cov - BI | No | Designated Pollutant Cov - BI |
| GLPollutionDesignatedCovPD | Designated Pollutant Cov - PD | No | Designated Pollutant Cov - PD |
| GLPollutionDesignatedCovGEN | Designated Pollutant Cov - Gen. Damages | No | Designated Pollutant Cov - General Damages |
| GLPollutionShortTermCovBI | Short Term Pollution - BI | No | Short Term Pollution - BI |
| GLPollutionShortTermCovPD | Short Term Pollution - PD | No | Short Term Pollution - PD |
| GLPollutionShortTermCovGEN | Short Term Pollution - Gen. Damages | No | Short Term Pollution - Gen. Damages |
| GLPollutionBI | Pollution Coverage - BI | No | Pollution Coverage - BI |
| GLPollutionPD | Pollution Coverage - PD | No | Pollution Coverage - PD |
| GLPollutionGEN | Pollution Coverage - Gen. Damage | No | Pollution Coverage - Gen. Damage |
| GLLiquorLiabilityCovBI | Liquor Liability Cov - BI | No | Liquor Liability Cov - BI |
| GLLiquorLiabilityCovPD | Liquor Liability Cov - PD | No | Liquor Liability Cov - PD |
| GLLiquorLiabilityCovGEN | Liquor Liability Cov - Gen. Damages | No | Liquor Liability Cov - Gen. Damages |
| GLContractLiabRRBI | Contract Liability - RR  -BI | No | Contract Liability - RR -BI |
| GLContracdtLiabRRPD | Contract Liability - RR -PD | No | Contract Liability - RR -PD |
| ContractLiabRRGEN | Contract Liability - RR -Gen Damage | No | Contract Liability - RR -Gen Damage |
| GLLimitedPAandInjuryCov | Ltd Contractual Liab for Personal Advertising and Injury | No | Ltd Contractual Liab for Personal Advertising and Injury: CG 22 74 |
| GLAddCondoCovBI | Condominium - BI | No | Condominium - B |
| GLAddCondoCovPD | Condominium PD | No | Condominium PD |
| GLAddCondoCovGEN | Condominium - Gen Damages | No | Condominium - Gen Damage |
| GLElectronicDataLiability | Electronic Data Liability | No | Electronic Data Liability: CG 04 37 |
| GLGovSubdivisionsBI | Gov't. Subdivisions - BI | No | Gov't. Subdivisions - BI |
| GLGovSubdivisionsPD | Gov't. Subdivisions - PD | No | Gov't. Subdivisions - PD |
| GLGovSubdivisionsGEN | Gov't. Subdivisions Gen. Damage | No | Gov't. Subdivisions Gen. Damage |
| GLLawnCareBI | Lawn Care - BI | No | Lawn Care - BI |
| GLLawnCarePD | Lawn Care - PD | No | Lawn Care - PD |
| GLLawnCareGEN | Lawn Care - Gen. Damages | No | Lawn Care - Gen. Damages |
| GLLtdFungiCovBI | Limited Fungi Cov - BI | No | Limited Fungi Cov - BI |
| GLLtdFungiCovPD | Limited Fungi Cov - PD | No | Limited Fungi Cov - PD |
| GLLtdFungiCovGEN | Limited Fungi Cov - Gen. Damages | No | Limited Fungi Cov - Gen. Damages |
| GLPestHerbicideApplicatorSchedule | Pesticide Or Herbicide Applicator Coverage | No | Pesticide Or Herbicide Applicator Coverage |
| GLUGResourcesCovBI | Underground Resources Cov - BI | No | Underground Resources Cov - BI |
| GLUGResourcesCovPD | Underground Resources Cov - PD | No | Underground Resources Cov - PD |
| GLUGResourcesCovGEN | Underground Resources Cov - Gen. Damages | No | Underground Resources Cov - Gen. Damages |
| ProductWithdrawalLtd | Product Withdrawal - Limited | No | Limited Coverage for Product Withdrawal: CG 04 36 |
| GLAddInjuryLeasedWorkers | Coverage for Injury to Leased Workers | No | Coverage for Injury to Leased Workers: CG 04 24 |
| GLEmpBenefitsLiabilityCov | Employee Benefits Liability | No | Employee Benefits Liability: CG 04 35 |
| Y2KLimitedCov | Y2K/Computer - Limited | No | Y2K / Computer Limited Cov: CG 04 31 |
| XCUSpecifiedBI | XCU - Specified - BI | No | XCU - Specified - BI |
| XCUSpecifiedPD | XCU - Specified - PD | No | XCU - Specified - PD |
| XCUSpecifiedGEN | XCU - Specified - Gen. Damages | No | XCU - Specified - Gen. Damages |
| CPBldgCov | Building Coverage | No | Building Coverage |
| CPBPPCov | Business Personal Property Coverage | No | Business Personal Property Coverage |
| CPBldgBusIncomeCov | Business Income Coverage | No | Business Income Coverage |
| CPBldgExtraExpenseCov | Extra Expense Coverage | No | Extra Expense Coverage |
| CPBldgStockCov | Business Personal Property - Separation of Coverage (Stock) | No | Business Personal Property - Separation of Coverage (Stock) |
| CPBlanketCov | CPBlanket Coverage | No | CPBlanket Coverage |
| PAExcessElectronicsCov | Electronic Equipment | No | Electronic Equipment |
| PALossOfUseCov | Rental Car Loss of Use | No | Rental Car Loss of Use |
| PATapeDiscMediaCov | Tape / Disc Media | No | Tape / Disc Media |
| PALiabilityCov_vd | Liability - Vehicle Damage | No | Liability - Vehicle Damage |
| PALiabilityCov_pd | Liability - Property Damage | No | Liability - Property Damage |
| PALiabilityCov_bi | Liability - Bodily Injury | No | Liability - Bodily Injury |
| PAMexicoCovBI | Mexico Cov - BI | No | Mexico Cov - BI |
| PAMexicoCovPD | Mexico Cov - PD | No | Mexico Cov - PD |
| PAMexicoCovVEH | Mexico Cov - Vehicle Damage | No | Mexico Cov - Vehicle Damage |
| PAMexicoCovGEN | Mexico Cov - Gen. Damages | No | Mexico Coverage - Gen. Damages |
| PAMedPayCov | Medical Payments | No | Medical Payments |
| PAPropProtectionCov | Property Protection Insurance | No | Property Protection Insurance |
| PAUIMBICov | Underinsured Motorist - Bodily Injury | No | Underinsured Motorist - Bodily Injury |
| PAUIMPDCov | Underinsured Motorist - Property Damage | No | Underinsured Motorist - Property Damage |
| PAUMBICov | Uninsured Motorist - Bodily Injury | No | Uninsured Motorist - Bodily Injury |
| PAUMPDCov | Uninsured Motorist - Property Damage | No | Uninsured Motorist - Property Damage |
| PACollisionCov | Collision | No | Collision |
| PACollision_MA_MI_Limited | Collision - Limited Coverage | No | Collision - Limited Coverage |
| PAComprehensiveCov | Comprehensive | No | Comprehensive |
| PARentalCov | Rental Reimbursement | No | Rental Reimbursement |
| PATowingLaborCov | Towing and Labor | No | Towing and Labor |
| PADeathDisabilityCov | Death and Disability Benefit | No | Auto Death and Disability Benefit |
| PAPIP_AR | PIP - Arkansas | No | PIP - Arkansas |
| PAPIP_DC | PIP - District of Columbia | No | PIP - District of Columbia |
| PAPIP_DE | PIP - Delaware | No | PIP - Delaware |
| PAPIP_FL | PIP - Florida | No | PIP - Florida |
| PAPIP_HI | PIP - Hawaii | No | PIP - Hawaii |
| PAPIP_KS | PIP - Kansas | No | PIP - Kansas |
| PAPIP_KY | PIP - Kentucky | No | PIP - Kentucky |
| PAPIP_MA | PIP - Massachusetts | No | PIP - Massachusetts |
| PAPIP_MD | PIP - Maryland | No | PIP - Maryland |
| PAPIP_MI | PIP - Michigan | No | PIP - Michigan |
| PAPIP_MN | PIP - Minnesota | No | PIP - Minnesota |
| PAPIP_ND | PIP - North Dakota | No | PIP - North Dakota |
| PAPIP_NJ | PIP - New Jersey | No | PIP - New Jersey |
| PAPIP_NY | PIP - New York | No | PIP - New York |
| PAPIP_OR | PIP - Oregon | No | PIP - Oregon |
| PAPIP_PA | PIP - Pennsylvania | No | PIP - Pennsylvania |
| PAPIP_TX | PIP - Texas | No | PIP - Texas |
| PAPIP_UT | PIP - Utah | No | PIP - Utah |
| PAPIP_WA | PIP - Washington | No | PIP - Washington |
| IMSignCov | Sign | No | Inland Marine Sign |
| ContractorsEquipSchedCov | Scheduled Equipment | No | Scheduled Equipment |
| ContractorsEquipAdditionallyAcquiredProperty | Additionally Acquired Property | No | Additionally Acquired Property |
| ContractorsEquipDebrisRemoval | Debris Removal | No | Debris Removal |
| ContractorsEquipPollutionCleanup | Pollution Cleanup | No | Pollution Cleanup |
| ContractorsEquipPreservationOfProperty | Preservation Of Property | No | Preservation Of Property |
| ContractorsEquipRentalReibursement | Rental Reimbursement | No | Rental Reimbursement |
| ContractorsEquipRentedEquipment | Rented Equipment | No | Rented Equipment - per occurrence |
| ContractorsEquipEmployeesTools | Employees Tools | No | Employees Tools - per occurrence |
| ContractorsEquipMiscUnscheduledCov | Misc Unscheduled Items | No | Misc Unscheduled Items - per occurrence |
| AccountsRecOffPremisesProperty | Off Premises Property | No | Off Premises Property |
| IMAccountReceivableCov | Accounts Receivable | No | Accounts Receivable |
| WCFedEmpLiabCov | Federal Employer's Liability | No | Federal Employer's Liability |
| WCEmpLiabCov | Workers' Comp Employer's Liability | No | Workers' Comp Employer's Liability |
| WCOtherStatesMED | Other States Insurance - Med Only | No | Other States Insurance - Med Only |
| WCOtherStatesWAGES | Other States Insurance - Other than Med | No | Other States Insurance - Other than Med |
| WCWorkersCompMED | WC Coverage -Med Only | No | WC Coverage -Med Only |
| WCWorkersCompWAGES | WC Coverage - Other than Med | No | WC Coverage - Other than Med |
| WCWorkCompDeductMED | State Specific Deductible - Med Only | No | State Specific Deductible - Med Only |
| WCWorkCompDeductNOTMED | State Specific Deductible - Other than Med | No | State Specific Deductible - Other than Med |
| BOPBuildingCov | Building | No | Building |
| BOPOrdinanceCov | Ordinance or Law | No | Ordinance or Law |
| BOPPersonalPropCov | Business Personal Property | No | Business Personal Property |
| BOPReceivablesCov | Accounts Receivable | No | Accounts Receivable |
| BOPValuablePapersCov | Valuable Papers | No | Valuable Papers |
| BOPCondoUnitOwnCov | Condo Unit Owner | No | Condo Unit Owner |
| BOPElectricalSchedCov | Electrical Equipment - Scheduled | No | Electrical Equipment - Scheduled |
| BOPFuncPerPropCov | Functional Business Personal Property | No | Functional Business Personal Property |
| BOPTenantsLiabilityCovPD | Tenant's Liability - PD | No | Tenant's Liability - PD |
| BOPTenantsLiabilityCovGEN | Tenant's Liability - Gen. Damages | No | Tenant's Liability - Gen. Damages |
| BOPVacancyChangeCov | Vacancy Change Coverage | No | Vacancy Changes/Conditions |
| BOPVacancyCov | Vacancy Permit | No | Vacancy Permit |
| BOPMechBreakdownCov | Mechanical Breakdown | No | Mechanical Breakdown |
| BOPUtilDirectCovPD | Utilities Direct Damage - Building | No | Utilities Direct Damage - Building |
| BOPUtilDirectCovCON | Utilities Direct Damage - Contents | No | Utilities Direct Damage - Contents |
| BOPUtilTimeCov | Utilities - Time Element | No | Utilities - Time Element |
| BOPAggLimitProjCov | Aggregate Limits of Insurance - Projects | No | Aggregate Limits of Insurance - Projects |
| BOPDesigPremProj | Designated Premises or Project Limitation | No | Designated Premises or Project Limitation |
| BOPPesticideApplicaorCovBI | Pesticide Applicator Cov - BI | No | Pesticide Applicator Cov - BI |
| BOPPesticideApplicatorCovGEN | Pesticide Applicator Cov - Gen. Damages | No | Pesticide Applicator Cov - Gen. Damages |
| BOPToolsSchedCov | Contractors Tools - Scheduled | No | Contractors Tools - Scheduled |
| BOPBurgRobCov | Burglary and Robbery | No | Burglary and Robbery |
| BOPComputerFraudCov | Computer/Funds Transfer Fraud | No | Computer/Funds Transfer Fraud |
| BOPForgeAltCov | Forgery and Alteration | No | Forgery and Alteration |
| BOPMoneySecCov | Money and Securities | No | Money and Securities |
| BOPBusIncDepPrpCov | Business Income - Dependent Property | No | Business Income - Dependent Prop |
| BOPBusIncExtCov | Business Income - Extended Period | No | Business Income - Extended Period |
| BOPBusIncPayrollCov | Business Income - Ordinary Payroll | No | BOP Business Income - Ordinary Payroll |
| BOPY2KIncomeExpenseCov | Income/Expense - Electronic Equip. | No | Income/Expense - Electronic Equip. |
| BOPAdditionalCov | Special Coverage Packages | No | Special Coverage Packages |
| BOPLiabilityBI | Liability - BI | No | Liability - BI |
| BOPLiabilityPD | Liability - PD | No | Liability - PD |
| BOPLiabilityGEN | Liability - Gen. Damages | No | Liability - Gen. Damages |
| BOPMedExpCov | Premises Medical Expense | No | Premises Medical Expense |
| BOPPersAdvertInj | Personal and Advertising Injury | No | Personal and Advertising Injury |
| BOPTenantFireCov | Tenants Fire Liability | No | Tenants Fire Liability |
| BOPEmpBenefits | Employee Benefits Liability | No | Employee Benefits Liability |
| BOPEmpBenExtRpting | Employee Benefits Extended Reporting | No | Employee Benefits Extended Reporting |
| BOPLeasedWorkerInjBI | Leased Workers Injury - BI | No | Leased Workers Injury - BI |
| BOPLeasedWorkerInjCovGEN | Leased Workers Injury - Gen. Damages | No | Leased Workers Injury - Gen. Damages |
| BOPPollutionCov | Pollution - Limited Liability Extension | No | Limited Pollution Liability Extension |
| BOPY2KLimitedCov | Computer Limited Liability Coverage | No | Computer Limited Liability Coverage |
| BOPY2KPremOnlyCov | Computer Liability-Premises Only | No | Computer Liability-Premises Only |
| BOPFDService | FD Service Contract | No | FD Service Contract |
| BOPFoodContamCovINCOME | Food Contamination Cov - Bus. Income | No | Food Contamination Cov - Bus. Income |
| BOPFoodContamCovGEN | Food Contamination Cov - Gen. Damages | No | Food Contamination Cov - Gen. Damages |
| BOPFungiPropCov | Limited Fungi Coverage (Property) | No | Limited Fungi Coverage (Property) |
| BOPNewAcquiredOrgCov | Newly Acquired Organization Coverage | No | Newly Acquired Organization Coverage |
| BusIncChangeCov | Bus. Inc. Waiting Period Change | No | Bus. Inc. Waiting Period Change |
| BOPLiquorCovBI | Liquor Liability Cov - BI | No | Liquor Liability Cov - BI |
| BOPLiquorCovGEN | Liquor Liability Cov - Gen. Damages | No | Liquor Liability Cov - Gen. Damages |
| BOPLiquorEventsBI | Liquor Liability - Events - BI | No | Liquor Liability - Events - BI |
| BOPLiquorEventsGEN | Liquor Liability - Events - Gen. Damages | No | Liquor Liability - Events - Gen. Damages |
| BOPLiquorRemoveExc | Liquor Liability - Remove Exclusion | No | Liquor Liability - Remove Exclusion |
| BOPLocWindHailCov | Windstorm/Hail | No | Windstorm/Hail |
| BOPOutdoorProp | Outdoor Property | No | Outdoor Property |
| BOPOutSignCov | Outdoor Signs | No | Outdoor Signs |
| BOPOverflowCovPD | Water Backup/Sump Overflow - Building | No | Water Backup/Sump Overflow - Building |
| BOPOverflowCovCON | Water Backup/Sump Overflow - Contents | No | Water Backup/Sump Overflow - Contents |
| BOPPersonalEffects | Personal Effects | No | Personal Effects |
| BOPPersPropOffPrem | Personal Property Off Premises | No | Personal Property Off Premises |
| BOPSpoilageCov | Spoilage | No | Spoilage |
| BOPBarberCovBI | Barber/Beautician Liability - BI | No | Barber/Beautician Liability - BI |
| BOPBarberCovGEN | Barber/Beautician Liability - Gen. Damages | No | Barber/Beautician Liability - Gen. Damages |
| BOPFuneralDirCov | Funeral Director Liability | No | Funeral Director Liability |
| BOPHearingAidCov | Hearing Aid / Optician Liability | No | Hearing Aid / Optician Liability |
| BOPPharmacistCov | Pharmacist Limited Liability Coverage | No | Pharmacist Limited Liability Coverage |
| BOPPrinterCov | Printers Errors and Omissions | No | Printers Errors and Omissions |
| BOPVetCov | Veterinarian Liability | No | Veterinarian Liability |
| BOPCondoAssnCov | Condo Association Coverage | No | Condo Association Coverage |
| BOPMotelCov | Motel Coverage | No | BOP Motel Coverage |
| BOPSelfStorCov | Self Storage Coverage | No | Self Storage Coverage |
| BOPToolsInstallUnschedCov | Contractors Tools/Installation | No | Contractors Tools/Installation |
| BOPAlaskaAFGLCov | AK - Attorney Fees - GL | No | Alaska Attorney Fees - GL |
| BOPCAEqBldgRecCov | CA - EQ Reconstruction | No | CA - EQ Reconstruction |
| BOPCAEqBldgSubCov | CA EQ - Building Sublimits | No | CA Earthquake - Building Sublimits |
| BOPMALeadPoisonCov | MA - Lead Poisoning | No | MA -  Lead Poisoning |
| BOPMATenantReloCov | MA - Apartment Coverage | No | MA - Apartment Coverage |
| BOPCertTerrorCap | Terror - Cap on Cert. Acts | No | Terror - Cap on Cert. Acts |
| BOPPropertyCov | Policywide Property Deductible | No | Policywide Property Deductible |
| BOPEqBldgCov | Earthquake | No | Earthquake |
| BOPEQSpLeakBuilding | EQ Sprinkler Leakage - Building | No | EQ Sprinkler Leakage - Building |
| BOPEQSpLeakBPP | EQ Sprinkler Leakage - Contents | No | EQ Sprinkler Leakage - Contents |
| BOPMineSubCov | Mine Subsidence | No | Mine Subsidence |
| BOPEmpDisCov | Employee Dishonesty | No | Employee Dishonesty |
| BOPHiredAutoBI | Hired Auto - BI | No | Hired Auto - BI |
| BOPHiredAutoVEH | Hired Auto - Vehicle Damage | No | Hired Auto - Vehicle Damage |
| BOPHiredAutoGEN | Hired Auto - Gen. Damages | No | Hired Auto - Gen. Damages |
| BOPNonOwnedAutoCovBI | Non owned auto - BI | No | Non owned auto - BI |
| BOPNonOwnedAutoVEH | Non owned auto - Vehicle Damage | No | Non owned auto - Vehicle Damage |
| BOPNonOwnedAutoCovGEN | Non owned auto - Gen. Damages | No | Non owned auto - Gen. Damages |
| BOPGuestPropCov | Guest's Property | No | Guest's Property Liability |
| BOPGuestSafeDepCov | Guests Property In Safe Deposit | No | Guests Property In Safe Deposit |
| zd7gujr17mccs3puv5jreeu1e59GD | Coverage E - Personal Liability General | No | Personal Liability General |
| zd7gujr17mccs3puv5jreeu1e59BI | Coverage E - Personal Liability Bodily Injury | No | Personal Liability Bodily Injury |
| zd7gujr17mccs3puv5jreeu1e59PD | Coverage E - Personal Liability Property | No | Personal Liability Property |
| z8tjsluucfmoh3nho364cli3uv8 | Coverage F - Medical Payments To Others | No | Medical Payments To Others |
| zl4i2neakg3g4ecg0t01bj445va | Coverage A - Dwelling | No | Dwelling |
| z26h4fbq18l81e5n478v5v07mj8 | Coverage B - Other Structures | No | Other Structures |
| zbtjua8nrhpvncl90406b37g2l9 | Coverage C - Personal Property | No | Personal Property |
| zpsii9qu58bma5eju8f5pgi0brb | Coverage D - Loss of Use | No | Loss of Use |
| zjjh6939q3g4n4k900psm1l21o9 | Fungus & Mold Remediation | No | Fungus & Mold Remediation |
| z2tgk324p0qk1fq75ei5be8g5gb | Identity Theft Protection | No | Identity Theft Protection |
| zlghejgaimjih96iplkcios7bs9 | Scheduled Personal Property | No | Scheduled Personal Property |
| BADOCCollisionCov | Collision - DOC | No | Collision for Drive Other Car |
| BADOCCompCov | Comprehensive - DOC | No | Comprehensive for Drive Other Car |
| BADOCLiabilityCovBI | Liability DOC - Bodily Injury | No | Liability (Drive Other Car) - Bodily Injury |
| BADOCLiabilityCovPD | Liability DOC - Property Damage | No | Liability DOC - Property Damage |
| BADOCLiabilityCovVEH | Liability DOC - Vehicle Damage | No | Liability DOC - Vehicle Damage |
| BADOCMedPayCov | Medical Payments - DOC | No | Medical Payments |
| BADOCUnderinsCov | Underinsured Motorist - DOC | No | Underinsured Motorist for Drive Other Car |
| BADOCUninsuredBI | Uninsured Motorist - DOC - BI | No | Uninsured Motorist - DOC - BI |
| BADOCUninsuredPD | Uninsured Motorist - DOC - PD | No | Uninsured Motorist - DOC - PD |
| BADOCUninsuredVEH | Uninsured Motorist - DOC - Vehicle Damage | No | Uninsured Motorist - DOC - Vehicle Damage |
| BAAudVisDataEqip2Cov | Audio, Visual, Data Electronic Equipment- Stated Amt. | No | Audio Visual Data Equipment |
| BAFellowEmployeesCov | Fellow Employees | No | Fellow Employees |
| BAHiredCollisionCov | Hired Auto Collision | No | Hired Auto Collision |
| BAHiredCompCov | Hired Auto Comprehensive | No | Hired Auto Comprehensive |
| BAHiredLiabilityCovBI | Hired Auto Liability - BI | No | Hired Auto Liability - BI |
| BAHiredLiabilityCovVEH | Hired Auto Liability - Vehicle Damage | No | Hired Auto Liability - Vehicle Damage |
| BAHiredLiabilityCovPD | Hired Auto Liability - PD | No | Hired Auto Liability - PD |
| BAHiredSpecPerilCov | Hired Auto Specified Causes of Loss | No | Hired Auto Specified Causes of Loss |
| BAHiredUIMBI | Hired Auto Underinsured Motorist - BI | No | Hired Auto Underinsured Motorist - BI |
| BAHiredUIMPD | Hired Auto Underinsured Motorist -PD | No | Hired Auto Underinsured Motorist - PD |
| BAHiredUIMVEH | Hired Auto Underinsured Motorist - Vehicle Damage | No | Hired Auto Underinsured Motorist - Vehicle Damage |
| BAHiredUMCovBI | Hired Auto Uninsured Motorist - BI | No | Hired Auto Uninsured Motorist - BI |
| BAHiredUMCovPD | Hired Auto Uninsured Motorist -PD | No | Hired Auto Uninsured Motorist - PD |
| BAHiredUMCovVEH | Hired Auto Uninsured Motorist - Vehicle Damage | No | Hired Auto Uninsured Motorist - Vehicle Damage |
| BALoanLeaseGapCov | Loan Lease Gap | No | Loan Lease Gap |
| BALossOfUseCov | Loss of Use | No | Loss of Use |
| BANonownedLiabCov_bi | Non-Owned Auto Liability - Bodily Injury | No | Non-Owned Auto Liability - Bodily Injury |
| BANonownedLiabCov_pd | Non-Owned Auto Liability - Property Damage | No | Non-Owned Auto Liability - Property Damage |
| BANonownedLiabCov_vd | Non-Owned Auto Liability - Vehicle Damage | No | Non-Owned Auto Liability - Vehicle Damage |
| BANonOwndSSExtendedBI | Non-owned Social Srv Extended - BI | No | Non-owned Social Srv Extended - BI |
| BANonOwndSSExtendedPD | Non-owned Social Srv Extended - PD | No | Non-owned Social Srv Extended - PD |
| BANonOwnSSExtendCovVEH | Non-owned Social Srv Extended - Vehicle Damage | No | Non-owned Social Srv Extended - Vehicle Damage |
| BABobtailLiabCov_bi | Bobtail Liability - Bodily Injury | No | Bobtail Liability - Bodily Injury |
| BABobtailLiabCov_pd | Bobtail Liability - Property Damage | No | Bobtail Liability - Property Damage |
| BABobtailLiabCov_vd | Bobtail Liability - Vehicle Damage | No | Bobtail Liability - Vehicle Damage |
| BADealerLimitLiabCov_bi | Auto Dealer Limited Liability - Bodily Injury | No | Auto Dealer Limited Liability - Bodily Injury |
| BADealerLimitLiabCov_pd | Auto Dealer Limited Liability - Property Damage | No | Auto Dealer Limited Liability - Property Damage |
| BADealerLimitLiabCov_vd | Auto Dealer Limited Liability - Vehicle Damage | No | Auto Dealer Limited Liability - Vehicle Damage |
| BAOwnedLiabilityCov_bi | Liability - Bodily Injury | No | Liability - Bodily Injury |
| BAOwnedLiabilityCov_vd | Liability - Vehicle Damage | No | Liability - Vehicle Damage |
| BAOwnedLiabilityCov_pd | Liability - PD | No | Liability - PD |
| BAOwnedMedPayCov | Medical Payments | No | Medical Payments |
| BASeasonTrailerLiabCov_bi | Seasonal Trailer Liability - Bodily Injury | No | Seasonal Trailer Liability - Bodily Injury |
| BASeasonTrailerLiabCov_pd | Seasonal Trailer Liability - Property Damage | No | Seasonal Trailer Liability - Property Damage |
| BASeasonTrailerLiabCov_vd | Seasonal Trailer Liability - Vehicle Damage | No | Seasonal Trailer Liability - Vehicle Damage |
| BACollisionCov | Collision | No | Collision |
| BACollisionLimited_MAMI | Collision - Limited Coverage | No | Collision - Limited Coverage |
| BAComprehensiveCov | Comprehensive | No | Comprehensive |
| BASpecCausesLossCov | Specified Causes of Loss | No | Specified Causes of Loss |
| BATowingLaborCov | Towing and Labor | No | Towing and Labor |
| BAPollutLiabBasicBI | Pollution Liability Basic- BI | No | Pollution Liability Basic- BI |
| BAPollutLiabBasicPD | Pollution Liability Basic - PD | No | Pollution Liability Basic - PD |
| BAPollutLiabBasicGEN | Pollution Liability Basic - Gen. Damages | No | Pollution Liability Basic - Gen. Damages |
| BAPollutLiabBoardBI | Pollution Liability Broad - BI | No | Pollution Liability Broad - BI |
| BAPollutLiabBoardGEN | Pollution Liability Broad - General Damage | No | Pollution Liability Broad - General Damage |
| BAPollutLiabBoardPD | Pollution Liability Broad - PD | No | Pollution Liability Broad - PD |
| BARentalCov | Rental Reimbursement | No | Rental Reimbursement |
| BATapeDiscRecordCov | Tape Disc Record | No | Tape Disc Record |
| BALimitedPropDamCov | Limited Property Damage | No | Limited Property Damage |
| BAOwnedUIMBICov | Underinsured Motorist - Bodily Injury | No | Underinsured Motorist - Bodily Injury |
| BAOwnedUIMPDCov | Underinsured Motorist - Property Damage | No | Underinsured Motorist - Property Damage |
| BAOwnedUMBICov | Uninsured Motorist - Bodily Injury | No | Uninsured Motorist - Bodily Injury |
| BAOwnedUMBISuppCov | Uninsured Motorist - Supplemental BI | No | Uninsured Motorist - Supplemental BI |
| BAOwnedUMPDCovPD | Uninsured Motorist -PD | No | Uninsured Motorist -PD |
| BAOwnedUMPDCovVEH | Uninsured Motorist - Vehicle Damage | No | Uninsured Motorist - Vehicle Damage |
| BAPropProtectionCov | Property Protection Insurance | No | Property Protection Insurance |
| CADeathDisabilityCov | Auto Death and Disability Benefit | No | Auto Death and Disability Benefit |
| CAPIP_DE | PIP - Delaware | No | PIP - Delaware |
| CAPIP_FL | PIP - Florida | No | PIP - Florida |
| CAPIP_HI | PIP - Hawaii | No | PIP - Hawaii |
| CAPIP_KS | PIP - Kansas | No | PIP - Kansas |
| CAPIP_KY | PIP - Kentucky | No | PIP - Kentucky |
| CAPIP_MA | PIP - Massachusetts | No | PIP - Massachusetts |
| CAPIP_MD | PIP - Maryland | No | PIP - Maryland |
| CAPIP_MI | PIP - Michigan | No | PIP - Michigan |
| CAPIP_MN | PIP - Minnesota | No | PIP - Minnesota |
| CAPIP_ND | PIP - North Dakota | No | PIP - North Dakota |
| CAPIP_NJ | PIP - New Jersey | No | PIP - New Jersey |
| CAPIP_NY | PIP - New York | No | PIP - New York |
| CAPIP_OR | PIP - Oregon | No | PIP - Oregon |
| CAPIP_PA | PIP - Pennsylvania | No | PIP - Pennsylvania |
| CAPIP_TX | PIP - Texas | No | PIP - Texas |
| CAPIP_UT | PIP - Utah | No | PIP - Utah |
| CAPIP_WA | PIP - Washington | No | PIP - Washington |
| CA_PIP_AR | PIP - Arkansas | No | PIP - Arkansas |
| CA_PIP_DC | PIP - District Of Columbia | No | PIP - District Of Columbia |
| PUPLiabilityBI | Personal Umbrella - BI | No | Personal Umbrella - BI |
| PUPLiabilityPD | Personal Umbrella - PD | No | Personal Umbrella - PD |
| PUPLiabilityGEN | Personal Umbrella - Gen. Damages | No | Personal Umbrella - Gen. Damages |
| PUPWorldWide | Personal Umbrella - Worldwide Cov | No | Personal Umbrella - Worldwide Cov |
| gl_gd2 | General Liability - General Damage 2 | No | General Liability - General Damage 2 |
| eando_gd | E and O - General Damage | No | E and O - General Damage |
| dando_gd | Directors and Officers - General Damage | No | Directors and Officers - General Damage |
| malp_bid | General liability - Bodily Injury | No | General liability - Bodily Injury |
| farm_pd | Farmowners - Property Damage | No | Farmowners - Property Damage |
| farm_bid | Farmowners - Bodily Injury | No | Farmowners - Bodily Injury |
| bag_loss_damg_dly | Baggage - Loss, Damage or Delay | No | Loss, damage or delay of baggage |
| mpay_travel | Travel - Medical Expenses | No | Medical expenses for the travel line |
| hiredauto_dmg_travel | Hired Auto Damages | No | Hired or rented auto damages |
| liab_trav_ad | Liability - Auto Damages | No | Auto damage liability |
| liab_trav_bi | Liability - Bodily Injury Damage | No | Bodily injury damage liability |
| liab_trav_gd | Liability - General Damage | No | General damage liability |
| liab_trav_pr | Liability - Property Damage | No | Property damage liability |
| TripCancelDelay | Trip - Cancellation or Delay | No | Trip - Cancellation or Delay |

---

### Typelist: CoverageType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\CoverageType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\CoverageType.ttx`
**Description:** Type of coverage
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| GLCGLCov | General Liability | No | Comprehensive General Liability |
| GLDeductible | GL Deductible | No | GL Deductible |
| GLPollutionDesignatedCov | Designated Pollutants | No | Coverage for Designated Pollutants |
| GLPollutionShortTermCov | Short Term Pollution Coverage | No | Short Term Pollution Coverage |
| PollutionBroadLimited | Pollution Coverage | No | Pollution Coverage |
| GLLiquorEndorsement | Liquor Liability Endorsement | No | Liquor Liability Endorsement |
| GLContractualLiabRR | Contractual Liability - Railroads | No | Contractual Liability - Railroads |
| GLLimitedPAandInjuryCov | Ltd Contractual Liab for Personal and Advertising | No | Ltd Contractual Liab for Personal and Advertising |
| GLAddCondoCov | Condominiums | No | Condominiums |
| GLElectronicDataLiability | Electronic Data Liability | No | Electronic Data Liability |
| GLGovSubdivisions | Governmental Subdivisions | No | Governmental Subdivisions |
| GLLawnCare | Lawn Care Services | No | Lawn Care Services |
| GLLtdFungiBacteriaCov | Limited Fungi or Bacteria Coverage | No | Limited Fungi or Bacteria Coverage |
| GLPestHerbicideApplicatorSchedule | Pesticide Or Herbicide Applicator Coverage | No | Pesticide Or Herbicide Applicator Coverage |
| GLUndergroundResourceCov | Underground Resources And Equip Coverage | No | Underground Resources And Equip Coverage |
| ProductWithdrawalLtd | Product Withdrawal - Limited | No | Limited Coverage for Product Withdrawal |
| GLAddInjuryLeasedWorkers | Coverage for Injury to Leased Workers | No | Coverage for Injury to Leased Workers |
| GLEmpBenefitsLiabilityCov | Employee Benefits Liability | No | Employee Benefits Liability |
| Y2KLimitedCov | Y2K/Computer - Limited | No | Y2K / Computer Limited Coverage |
| XCUSpecified | XCU - Specified | No | XCU - Specified Locations, Operation, Hazard |
| CPBldgCov | Building Coverage | No | Building Coverage |
| CPBPPCov | Business Personal Property Coverage | No | Business Personal Property Coverage |
| CPBldgBusIncomeCov | Business Income Coverage | No | Business Income Coverage |
| CPBldgExtraExpenseCov | Extra Expense Coverage | No | Extra Expense Coverage |
| CPBldgStockCov | Business Personal Property - Separation of Coverage (Stock) | No | Business Personal Property - Separation of Coverage (Stock) |
| CPBlanketCov | CPBlanket Coverage | No | CPBlanket Coverage |
| PAExcessElectronicsCov | Electronic Equipment | No | Excess Electronic Equipment |
| PALossOfUseCov | Rental Car Loss of Use | No | Rental Car Loss of Use |
| PATapeDiscMediaCov | Tape / Disc Media | No | Tape / Disc Media |
| PALiabilityCov | Liability - Bodily Injury and Property Damage | No | Liability - Bodily Injury and Property Damage |
| PALimitedMexicoCov | Mexico Coverage - Limited | No | Mexico Coverage - Limited |
| PAMedPayCov | Medical Payments | No | Medical Payments |
| PAPropProtectionCov | Property Protection Insurance | No | Property Protection Insurance |
| PAUIMBICov | Underinsured Motorist - Bodily Injury | No | Underinsured Motorist - Bodily Injury |
| PAUIMPDCov | Underinsured Motorist - Property Damage | No | Underinsured Motorist - Property Damage |
| PAUMBICov | Uninsured Motorist - Bodily Injury | No | Uninsured Motorist - Bodily Injury |
| PAUMPDCov | Uninsured Motorist - Property Damage | No | Uninsured Motorist - Property Damage |
| PACollisionCov | Collision | No | Collision |
| PACollision_MA_MI_Limited | Collision - Limited Coverage | No | Collision - Limited Coverage |
| PAComprehensiveCov | Comprehensive | No | Comprehensive |
| PARentalCov | Rental Reimbursement | No | Rental Reimbursement |
| PATowingLaborCov | Towing and Labor | No | Towing and Labor |
| PADeathDisabilityCov | Death & Disability Benefit | No | Death & Disability Benefit |
| PAPIP_AR | PIP - Arkansas | No | PIP - Arkansas |
| PAPIP_DC | PIP - District of Columbia | No | PIP - District of Columbia |
| PAPIP_DE | PIP - Delaware | No | PIP - Delaware |
| PAPIP_FL | PIP - Florida | No | PIP - Florida |
| PAPIP_HI | PIP - Hawaii | No | PIP - Hawaii |
| PAPIP_KS | PIP - Kansas | No | PIP - Kansas |
| PAPIP_KY | PIP - Kentucky | No | PIP - Kentucky |
| PAPIP_MA | PIP - Massachusetts | No | PIP - Massachusetts |
| PAPIP_MD | PIP - Maryland | No | PIP - Maryland |
| PAPIP_MI | PIP - Michigan | No | PIP - Michigan |
| PAPIP_MN | PIP - Minnesota | No | PIP - Minnesota |
| PAPIP_ND | PIP - North Dakota | No | PIP - North Dakota |
| PAPIP_NJ | PIP - New Jersey | No | PIP - New Jersey |
| PAPIP_NY | PIP - New York | No | PIP - New York |
| PAPIP_OR | PIP - Oregon | No | PIP - Oregon |
| PAPIP_PA | PIP - Pennsylvania | No | PIP - Pennsylvania |
| PAPIP_TX | PIP - Texas | No | PIP - Texas |
| PAPIP_UT | PIP - Utah | No | PIP - Utah |
| PAPIP_WA | PIP - Washington | No | PIP - Washington |
| IMSignCov | Inland Marine Sign | No | Inland Marine Sign |
| ContractorsEquipSchedCov | Contractors Scheduled Equipment | No | Contractors Scheduled Equipment |
| ContractorsEquipAdditionallyAcquiredProperty | Contractors Equipment - Additional Acquired Property | No | Contractors Equipment - Additional Acquired Property |
| ContractorsEquipDebrisRemoval | Contractors Equipment - Debris Removal | No | Contractors Equipment - Debris Removal |
| ContractorsEquipPollutionCleanup | Contractors Equipment - Pollution Cleanup | No | Contractors Equipment - Pollution Cleanup |
| ContractorsEquipPreservationOfProperty | Contractors Equipment - Preservation of Property | No | Contractors Equipment - Preservation of Property |
| ContractorsEquipRentalReibursement | Contractors Rental Reimbursement | No | Contractors Rental Reimbursement |
| ContractorsEquipRentedEquipment | Contractors Rented Equipment | No | Contractors Rented Equipment |
| ContractorsEquipEmployeesTools | Contractors Equipment - Employees Tools | No | Employees Tools - per occurrence |
| ContractorsEquipMiscUnscheduledCov | Contractors Equipment - Misc. Items | No | Misc Unscheduled Items - per occurrence |
| AccountsRecOffPremisesProperty | Accts Receivable - Off Premises Property | No | Accts Receivable - Off Premises Property |
| IMAccountReceivableCov | Accounts Receivable | No | Accounts Receivable |
| WCFedEmpLiabCov | Federal Employer's Liability | No | Federal Employer's Liability |
| WCEmpLiabCov | Workers' Comp Employer's Liability | No | Workers' Comp Employer's Liability |
| WCOtherStatesInsurance | Other States Insurance | No | Other States Insurance |
| WCWorkersCompCov | Statutory Workers' Comp | No | Statutory Workers' Comp |
| WCWorkCompDeductCov | Workers' Comp State-Specific Deductible | No | Workers' Comp State-Specific Deductible |
| BOPBuildingCov | Building | No | Building |
| BOPOrdinanceCov | Ordinance or Law | No | Ordinance or Law |
| BOPPersonalPropCov | Business Personal Property | No | Business Personal Property |
| BOPReceivablesCov | Accounts Receivable | No | Accounts Receivable |
| BOPValuablePapersCov | Valuable Papers | No | Valuable Papers |
| BOPCondoUnitOwnCov | Condo Unit Owner | No | Condo Unit Owner |
| BOPElectricalSchedCov | Electrical Equipment - Scheduled | No | Electrical Equipment - Scheduled |
| BOPFuncPerPropCov | Functional Business Personal Property | No | Functional Business Personal Property |
| BOPTenantsLiabilityCov | Tenants Liability | No | Tenants Liability |
| BOPVacancyChangeCov | Vacancy Change Coverage | No | Vacancy Changes/Conditions |
| BOPVacancyCov | Vacancy Permit | No | Vacancy Permit |
| BOPMechBreakdownCov | Mechanical Breakdown | No | Mechanical Breakdown |
| BOPUtilDirectCov | Utilities - Direct Damage | No | Utilities - Direct Damage |
| BOPUtilTimeCov | Utilities - Time Element | No | Utilities - Time Element |
| BOPAggLimitProjCov | Aggregate Limits of Insurance - Projects | No | Aggregate Limits of Insurance - Projects |
| BOPDesigPremProj | Designated Premises or Project Limitation | No | Designated Premises or Project Limitation |
| BOPPesticideApplicatorCov | Pesticide Applicator Coverage | No | Pesticide Applicator Coverage |
| BOPToolsSchedCov | Contractors Tools - Scheduled | No | Contractors Tools - Scheduled |
| BOPBurgRobCov | Burglary and Robbery | No | Burglary and Robbery |
| BOPComputerFraudCov | Computer/Funds Transfer Fraud | No | Computer/Funds Transfer Fraud |
| BOPForgeAltCov | Forgery and Alteration | No | Forgery and Alteration |
| BOPMoneySecCov | Money and Securities | No | Money and Securities |
| BOPBusIncDepPrpCov | Business Income - Dependent Property | No | Business Income - Dependent Prop |
| BOPBusIncExtCov | Business Income - Extended Period | No | Business Income - Extended Period |
| BOPBusIncPayrollCov | Business Income - Ordinary Payroll | No | BOP Business Income - Ordinary Payroll |
| BOPY2KIncomeExpenseCov | Income/Expense - Electronic Equip. | No | Income/Expense - Electronic Equip. |
| BOPAdditionalCov | Special Coverage Packages | No | Special Coverage Packages |
| BOPLiabilityCov | Liability | No | Liability |
| BOPMedExpCov | Premises Medical Expense | No | Premises Medical Expense |
| BOPPersAdvertInj | Personal and Advertising Injury | No | Personal and Advertising Injury |
| BOPTenantFireCov | Tenants Fire Liability | No | Tenants Fire Liability |
| BOPEmpBenefits | Employee Benefits Liability | No | Employee Benefits Liability |
| BOPEmpBenExtRpting | Employee Benefits Extended Reporting | No | Employee Benefits Extended Reporting |
| BOPLeasedWorkerInjCov | Leased Workers - Injury Coverage | No | Leased Workers - Injury Coverage |
| BOPPollutionCov | Pollution - Limited Liability Extension | No | Limited Pollution Liability Extension |
| BOPY2KLimitedCov | Computer Limited Liability Coverage | No | Computer Limited Liability Coverage |
| BOPY2KPremOnlyCov | Computer Liability-Premises Only | No | Computer Liability-Premises Only |
| BOPFDService | FD Service Contract | No | FD Service Contract |
| BOPFoodContamCov | Food Contamination Coverage | No | Food Contamination Coverage |
| BOPFungiPropCov | Limited Fungi Coverage (Property) | No | Limited Fungi Coverage (Property) |
| BOPNewAcquiredOrgCov | Newly Acquired Organization Coverage | No | Newly Acquired Organization Coverage |
| BusIncChangeCov | Bus. Inc. Waiting Period Change | No | Bus. Inc. Waiting Period Change |
| BOPLiquorCov | Liquor Liability Coverage | No | Liquor Liability Coverage |
| BOPLiquorEvents | Liquor Liability - Event Only | No | Liquor Liability - Event Only |
| BOPLiquorRemoveExc | Liquor Liability - Remove Exclusion | No | Liquor Liability - Remove Exclusion |
| BOPLocWindHailCov | Windstorm/Hail | No | Windstorm/Hail |
| BOPOutdoorProp | Outdoor Property | No | Outdoor Property |
| BOPOutSignCov | Outdoor Signs | No | Outdoor Signs |
| BOPOverflowCov | Water Backup and Sump Overflow | No | Water Backup and Sump Overflow |
| BOPPersonalEffects | Personal Effects | No | Personal Effects |
| BOPPersPropOffPrem | Personal Property Off Premises | No | Personal Property Off Premises |
| BOPSpoilageCov | Spoilage | No | Spoilage |
| BOPBarberCov | Barber/Beautician Liability | No | Barber/Beautician Liability |
| BOPFuneralDirCov | Funeral Director Liability | No | Funeral Director Liability |
| BOPHearingAidCov | Hearing Aid / Optician Liability | No | Hearing Aid / Optician Liability |
| BOPPharmacistCov | Pharmacist Limited Liability Coverage | No | Pharmacist Limited Liability Coverage |
| BOPPrinterCov | Printers Errors and Omissions | No | Printers Errors and Omissions |
| BOPVetCov | Veterinarian Liability | No | Veterinarian Liability |
| BOPCondoAssnCov | Condo Association Coverage | No | Condo Association Coverage |
| BOPMotelCov | Motel Coverage | No | BOP Motel Coverage |
| BOPSelfStorCov | Self Storage Coverage | No | Self Storage Coverage |
| BOPToolsInstallUnschedCov | Contractors Tools/Installation | No | Contractors Tools/Installation |
| BOPAlaskaAFGLCov | AK - Attorney Fees - GL | No | Alaska Attorney Fees - GL |
| BOPCAEqBldgRecCov | CA - EQ Reconstruction | No | CA - EQ Reconstruction |
| BOPCAEqBldgSubCov | CA EQ - Building Sublimits | No | CA Earthquake - Building Sublimits |
| BOPMALeadPoisonCov | MA - Lead Poisoning | No | MA -  Lead Poisoning |
| BOPMATenantReloCov | MA - Apartment Coverage | No | MA - Apartment Coverage |
| BOPCertTerrorCap | Terror - Cap on Cert. Acts | No | Terror - Cap on Cert. Acts |
| BOPPropertyCov | Policywide Property Deductible | No | Policywide Property Deductible |
| BOPEqBldgCov | Earthquake | No | Earthquake |
| BOPEqSpBldgCov | Earthquake - Sprinkler Leakage | No | Earthquake - Sprinkler Leakage |
| BOPMineSubCov | Mine Subsidence | No | Mine Subsidence |
| BOPEmpDisCov | Employee Dishonesty | No | Employee Dishonesty |
| BOPHiredAuto | Hired Auto | No | Hired Auto |
| BOPNonOwnedAutoCov | Non-owned Auto Liability | No | Non-owned Auto Liability |
| BOPGuestPropCov | Guest's Property | No | Guest's Property Liability |
| BOPGuestSafeDepCov | Guests Property In Safe Deposit | No | Guests Property In Safe Deposit |
| zd7gujr17mccs3puv5jreeu1e59 | Coverage E - Personal Liability | No | Personal Liability |
| z8tjsluucfmoh3nho364cli3uv8 | Coverage F - Medical Payments To Others | No | Medical Payments To Others |
| zl4i2neakg3g4ecg0t01bj445va | Coverage A - Dwelling | No | Dwelling |
| z26h4fbq18l81e5n478v5v07mj8 | Coverage B - Other Structures | No | Other Structures |
| zbtjua8nrhpvncl90406b37g2l9 | Coverage C - Personal Property | No | Personal Property |
| zpsii9qu58bma5eju8f5pgi0brb | Coverage D - Loss of Use | No | Loss of Use |
| zocji60oon5qu43lr22k8q4o15a | Section I Deductibles | No | Section I Deductibles |
| zu7jmsu26rk141vkaijeq6golm9 | Building Additions and Alterations | No | Building Additions and Alterations |
| zdtga636fmshibrnrfu1h5s7cvb | Collapse | No | Collapse |
| z7ui0o2ttovs76h6rtk6q9gbeh8 | Construction Permit Increase Costs | No | Construction Permit Increase Costs |
| zu4gq88v6fqir3hpdsamf12gu2a | Credit/Debit Card, Forgery and Counterfeit Money | No | Credit/Debit Card, Forgery and Counterfeit Money |
| zmpji3fssm9h5emk8uqv9nl6sb8 | Damage to Property of Others | No | Damage to Property of Others |
| ztihci8muqm61c3a6vmaeb28a2b | Data and Records | No | Data and Records |
| z2cjsu8d7ldr23ojbnc6es16ti9 | Debris Removal | No | Debris Removal |
| zo4iu93mmrrl90ise6f67gqif98 | Debris Removal of Trees | No | Debris Removal of Trees |
| zrjhog8dpqkb00hc4dtc7ljrukb | Dwelling Under Construction - Extension of Coverages | No | Dwelling Under Construction - Extension of Coverages |
| zvoiu1bhk3vs48lq0i2ef8fogfa | Emergency Living Expense - Power Interruption Off Premises | No | Emergency Living Expense - Power Interruption Off Premises |
| z6vgil0u20qn9a8b8h9c24sc6eb | Emergency Removal of Property | No | Emergency Removal of Property |
| zk9jol4tjcvk422ctjoib6nm5s9 | Fire Department Service Charge | No | Fire Department Service Charge |
| z7lhomv5qqndfdnsr9680bb1hq9 | Fire Extinguisher Recharge | No | Fire Extinguisher Recharge |
| zeliiv44ls0fd7s7cdln05s05qa | First Aid | No | First Aid |
| zjjh6939q3g4n4k900psm1l21o9 | Fungus & Mold Remediation | No | Fungus & Mold Remediation |
| zu6i6rdl89rc2cu7inkfbe38b6b | Glass | No | Glass |
| ze3gohh5o7209812gfah4cs0ed8 | Grave Markers | No | Grave Markers |
| z2tgk324p0qk1fq75ei5be8g5gb | Identity Theft Protection | No | Identity Theft Protection |
| zk9i4qe1i9ncn6lptuvt85f0439 | Inflation Protection | No | Inflation Protection |
| z0ui0qal30ijg7f24ndprcj356b | Landlord's Furnishings | No | Landlord's Furnishings |
| z78h4sr6nki8ha99hku55rd4uaa | Lock Replacement | No | Lock Replacement |
| zp2g4atrihccn086l4vpbreit28 | Loss Assessment | No | Loss Assessment |
| zilgk228c95qt3ob6v9s6na08ab | Mortgage Closing Cost Expense | No | Mortgage Closing Cost Expense |
| zi8gq0ddmt92f4efi0tqik4hgv8 | Ordinance Or Law | No | Ordinance Or Law |
| z8oh0o5asbk8g9v4bspvmgpq3k9 | Personal Property Off Premises - Earthquake and Flood | No | Personal Property Off Premises - Earthquake and Flood |
| zbags5ei5vefn92sf55g2tielv8 | Reasonable Repairs | No | Reasonable Repairs |
| zuhiksn15sd0g53anl8v0pu45db | Reward | No | Reward |
| z19ia8ibe31cierblikntvppe68 | Trees, Shrubs, Plants & Lawns | No | Trees, Shrubs, Plants & Lawns |
| z1bg07ii0pfa4cj02al1n88sgeb | Volcanic Action | No | Volcanic Action |
| z4lhib5av546s2ko4naf3s8crf8 | Assisted Living Care | No |  |
| z50ikk44122467ads0qitrdqqi8 | Backup of Sewers, Drains and Sump Pump | No | Backup of Sewers, Drains and Sump Pump |
| zr4gsjbrvihdr6ktd06s5kc87n9 | Earthquake | No | Earthquake |
| zb4iiqcl6a21b0grb6aamorc4ca | Escaped Liquid Fuel | No | Escaped Liquid Fuel |
| zc9i82cntebm2a97javsujkqk7b | Extended Residence Theft | No | Extended Theft for Residence Rented to Others |
| zr3jqmau1bned1g0oe6pqhu7ct8 | Foundation Water Damage from Seepage | No | Foundation Water Damage from Seepage |
| z39i08pn1407l7i6bv5j2jk2jhb | Golf Cart | No |  |
| z4bjaqp9ugpiqe79vlsr61jkfb9 | Increased Limit - Other Structures | No |  |
| zbkhgt4jvb1i76oglrok2qsnq09 | Increased Limits - Personal Property At Other Residences | No | Increased Limits - Personal Property At Other Residences |
| z6phevqrmj0r38hvvhtbk7pimv8 | Limited Fungus And Mold Liability | No | Limited Fungus And Mold Liability |
| zntgc6mmauu3hagr0g8ura77549 | Permitted Incidental Occupancies | No |  |
| zqai6drb846ga0qkobutjcleb2a | Refrigerated Contents | No | Refrigerated Contents |
| zs8hqfgnkr1v9396ccjbc8pbki8 | Scheduled Landlord's Furnishings | No | Scheduled Landlord's Furnishings |
| zlghejgaimjih96iplkcios7bs9 | Scheduled Personal Property | No | Scheduled Personal Property |
| zdmj42u34b70e98oe73a1ab3u48 | Sinkhole Collapse | No | Sinkhole Collapse |
| z74i2o900p9aner9khi3ucsf1pb | Special Computer Coverage | No | Special Computer Coverage |
| zo8jgu75d357q794cno84vh0338 | Specific Structures Away From Residence | No | Specific Structures Away From Residence |
| zpajido164efucetokjge4q45e9 | Structures Rented To Others - Residence Premises | No | Structures Rented To Others - Residence Premises |
| zc1jk38ardj581cfmn0e395i758 | Valuable Personal Property | No | Valuable Personal Property |
| zrcjqe5k1gu1ic8sbend4tpb1gb | Workers' Compensation | No | Workers' Compensation |
| z1gguiuovtplr3j4rucqdv0stra | Assisted Living Care Item | No |  |
| zdogeskkpv01dc9p8upk23dne09 | Golf Cart Item | No | Golf Cart Coverage - Schedule Detail |
| z1fhulh3d21qr4o5ktk2e54ndpb | Increased Limit - Other Structures Item | No | Increased Limit - Other Structures Item |
| zm8igrhpt3bfg2lvdnl5lf0iat9 | Increased Limits - Personal Property At Other Residences Item | No | Increased Limits - Personal Property At Other Residences Item |
| zrrhqcqhj768sfnjh0uoas3n5d9 | Permitted Incidental Occupancies Item | No |  |
| zo5h0mvsjli2d8gp47cpa3appfb | Scheduled Landlord's Furnishings Item | No |  |
| zd5joencat3ep2cm32h3e5cdmj9 | Scheduled Personal Property Item | No | Scheduled Personal Property Item |
| zh5j85vgpge8n6saji15tsonl8b | Specific Structures Away From Residence Item | No |  |
| zcgjavp5vcr21558v9bucnfqj0b | Structures Rented To Others - Residence Premises Item | No | Structures Rented To Others - Residence Premises Item |
| zc9iqhupesj0fbpvo8ltn4526b8 | Valuable Personal Property Item | No | Valuable Personal Property Item |
| BADOCCollisionCov | Collision -DOC | No | Collision for Drive Other Car |
| BADOCCompCov | Comprehensive - DOC | No | Comprehensive for Drive Other Car |
| BADOCLiabilityCov | Liability - Bodily Injury and Property Damage - DOC | No | Liability - Bodily Injury and Property Damage - DOC |
| BADOCMedPayCov | Medical Payments - DOC | No | Medical Payments  for Drive Other Car |
| BADOCUnderinsCov | Underinsured Motorist - DOC | No | Underinsured Motorist for Drive Other Car |
| BADOCUninsuredCov | Uninsured Motorist - DOC | No | Uninsured Motorist for Drive Other Car |
| BAAudVisDataEqip2Cov | Audio, Visual, Data Electronic Equipment- Stated Amt. | No | Audio Visual Data Equipment |
| BAFellowEmployeesCov | Fellow Employees | No | Fellow Employees |
| BAHiredCollisionCov | Hired Auto Collision | No | Hired Auto Collision |
| BAHiredCompCov | Hired Auto Comprehensive | No | Hired Auto Comprehensive |
| BAHiredLiabilityCov | Hired Auto Liability | No | Hired Auto Liability |
| BAHiredSpecPerilCov | Hired Auto Specified Causes of Loss | No | Hired Auto Specified Causes of Loss |
| BAHiredUIMCov | Hired Auto Underinsured Motorist | No | Hired Auto Underinsured Motorist |
| BAHiredUMCov | Hired Auto Uninsured Motorist | No | Hired Auto Uninsured Motorist |
| BALoanLeaseGapCov | Loan Lease Gap | No | Loan Lease Gap |
| BALossOfUseCov | Loss of Use | No | Loss of Use |
| BANonownedLiabCov | Non-Owned Auto Liability | No | Non-Owned Auto Liability |
| BANonOwndSSExtendCov | Non-Owned Social Services Extended | No | Non-Owned Social Services Extended |
| BABobtailLiabCov | Bobtail Liability | No | Bobtail Liability |
| BADealerLimitLiabCov | Auto Dealer Limited Liability | No | Auto Dealer Limited Liability |
| BAOwnedLiabilityCov | Liability | No | Liability - Bodily Injury and Property Damage |
| BAOwnedMedPayCov | Medical Payments | No | Medical Payments |
| BASeasonTrailerLiabCov | Seasonal Trailer Liability | No | Seasonal Trailer Liability |
| BACollisionCov | Collision | No | Collision |
| BACollisionLimited_MAMI | Collision - Limited Coverage | No | Collision - Limited Coverage |
| BAComprehensiveCov | Comprehensive | No | Comprehensive |
| BASpecCausesLossCov | Specified Causes of Loss | No | Specified Causes of Loss |
| BATowingLaborCov | Towing and Labor | No | Towing and Labor |
| BAPollutLiabBasicCov | Pollution Liability Basic | No | Pollution Liability Basic |
| BAPollutLiabBoardCov | Pollution Liability Broad | No | Pollution Liability Broad |
| BARentalCov | Rental Reimbursement | No | Rental Reimbursement |
| BATapeDiscRecordCov | Tape Disc Record | No | Tape Disc Record |
| BALimitedPropDamCov | Limited Property Damage | No | Limited Property Damage |
| BAOwnedUIMBICov | Underinsured Motorist - Bodily Injury | No | Underinsured Motorist - Bodily Injury |
| BAOwnedUIMPDCov | Underinsured Motorist - Property Damage | No | Underinsured Motorist - Property Damage |
| BAOwnedUMBICov | Uninsured Motorist - Bodily Injury | No | Uninsured Motorist - Bodily Injury |
| BAOwnedUMBISuppCov | Uninsured Motorist - Supplemental BI | No | Uninsured Motorist - Supplemental BI |
| BAOwnedUMPDCov | Uninsured Motorist - Property Damage | No | Uninsured Motorist - Property Damage |
| BAPropProtectionCov | Property Protection Insurance | No | Property Protection Insurance |
| CADeathDisabilityCov | Death and Disability | No | Death and Disability |
| CAPIP_DE | PIP - Delaware | No | PIP - Delaware |
| CAPIP_FL | PIP - Florida | No | PIP - Florida |
| CAPIP_HI | PIP - Hawaii | No | PIP - Hawaii |
| CAPIP_KS | PIP - Kansas | No | PIP - Kansas |
| CAPIP_KY | PIP - Kentucky | No | PIP - Kentucky |
| CAPIP_MA | PIP - Massachusetts | No | PIP - Massachusetts |
| CAPIP_MD | PIP - Maryland | No | PIP - Maryland |
| CAPIP_MI | PIP - Michigan | No | PIP - Michigan |
| CAPIP_MN | PIP - Minnesota | No | PIP - Minnesota |
| CAPIP_ND | PIP - North Dakota | No | PIP - North Dakota |
| CAPIP_NJ | PIP - New Jersey | No | PIP - New Jersey |
| CAPIP_NY | PIP - New York | No | PIP - New York |
| CAPIP_OR | PIP - Oregon | No | PIP - Oregon |
| CAPIP_PA | PIP - Pennsylvania | No | PIP - Pennsylvania |
| CAPIP_TX | PIP - Texas | No | PIP - Texas |
| CAPIP_UT | PIP - Utah | No | PIP - Utah |
| CAPIP_WA | PIP - Washington | No | PIP - Washington |
| CA_PIP_AR | PIP - Arkansas | No | PIP - Arkansas |
| CA_PIP_DC | PIP - District Of Columbia | No | PIP - District Of Columbia |
| PUP_Primary_LiabilityCov_PUE | Primary Personal Liability Coverage | No | Primary Personal Liability Coverage |
| PUP_WorldWideCov_PUE | World Wide | No | World Wide |
| EANDO | Errors and omissions | No | Errors and omissions |
| MALP | Malpractice | No | Malpractice |
| DandO | Directors and Officers | No | Directors and Officers |
| FARM | Farmowners | No | Farmowners |
| baggage | Baggage | No | General coverage for baggage including suitcases and contents like personal items, electronics, wallet, passports, etc. |
| health_travel | Health | No | Heath coverage |
| hiredauto_travel | Hired Auto | No | Excesses for hired/rented auto |
| liab_travel | Liability | No | 3rd party liability |
| trip | Trip | No | Trip coverage for travel and accommodations |

---

### Typelist: CoveredPartyType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\CoveredPartyType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\CoveredPartyType.ttx`
**Description:** Types of covered parties
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| addinsured | Additional insured | No | Additional insured |
| addnamedinsured | Additional named insured | No | Additional named insured |

---

### Typelist: CovTermModelAgg

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\CovTermModelAgg.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\CovTermModelAgg.ttx`
**Description:** Coverage Term Model Aggregation
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| ag | Annual aggregate | No | Annual aggregate |
| ei | Each incident | Yes | Each incident |
| pi | Per item | No | Per item |
| pc | Per claim | No | Per claim |
| pp | Per person | No | Per person |
| ea | Each accident | No | Each accident |
| po | Per occurence | No | Per occurence |
| cc | Each common cause | No | Each common cause |

---

### Typelist: CovTermModelRest

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\CovTermModelRest.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\CovTermModelRest.ttx`
**Description:** Coverage Term Model Scope
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

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

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\CovTermModelType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\CovTermModelType.ttx`
**Description:** Coverage term model type
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

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

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\CovTermModelVal.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\CovTermModelVal.ttx`
**Description:** Coverage Term Model Value Type
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| money | Money | No | Money |
| percent | Percent | No | Percent |
| days | Days | No | Days |
| hours | Hours | No | Hours |
| count | Count | No | Integer number of things (e.g., people, etc.) |

---

### Typelist: CovTermPattern

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\CovTermPattern.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\CovTermPattern.ttx`
**Description:** The types of coverage terms for each coverage type
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| GLCGLAggLimit | Aggregate Limit | No | Aggregate Limit |
| GLCGLBIAggLimit | Bodily Injury Aggregate Limit | No | Bodily Injury Aggregate Limit |
| GLCGLBILimit | Bodily Injury Occurrence Limit | No | Bodily Injury Occurrence Limit |
| GLCGLMedPayLimit | Medical Payments per person | No | Medical Payments per person |
| GLCGLOccLimit | Occurrence Limit | No | Occurrence Limit |
| GLCGLPDAggLimit | Property Damage Aggregate Limit | No | Property Damage Aggregate Limit |
| GLCGLPDLimit | Property Damage Occurrence Limit | No | Property Damage Occurrence Limit |
| GLCGLPersAdLimit | Personal & Advertising Injury | No | Personal & Advertising Injury Limit |
| GLCGLRentedPropLimit | Damage to Rented Premises | No | Damage to Rented Premises Limit |
| CGLProductsAggLim | Products/Comp.Ops Aggregate | No | Products/Comp.Ops Aggregate |
| CGLProdCompOpBIAgg | Products/Comp. Ops BI Agg | No | Products/Comp. Ops BI Agg |
| CGLProdCompOpsPDAgg | Products/Comp. Ops PD Agg | No | Products/Comp. Ops PD Agg |
| GLCSLDeductible | Deductible - CSD | No | Optional Deductible - not for split limit policies |
| GLBIDeductible | Deductible - BI | No | BI Deductible when policy uses split limits |
| GLPDDeductible | Deductible - PD | No | PD deductible used when policy has split limits |
| ClaimBasis | Deductible Basis | No | Deductible Basis |
| DesignatedPollutants | Designated Pollutants | No | Designated Pollutants |
| NamedPerilsOnly | Named Perils Only | No |  |
| PollutionLimitType | Pollution Limit | No | Pollution Limit |
| PollutionSubLimit | Pollution Sub Limit | No | Pollution Sub Limit |
| GLLiquorEvent | Event Coverage Only | No | Boolean restricts coverage to specified events |
| GLLiquorEventDesc | Event Description | No | Event Description |
| GLContractualLiabRRDescription | Description | No | Description of Contracted Work |
| GLLimitedPAandInjuryCovDescription | Description | No | Description of Contracts |
| GLElectronicDataLimit | Electronic Data Limit | No | Electronic Data Limit |
| GLLitdFungiBacteriaLimit | Fungi or Bacteria Limit | No | Fungi or Bacteria Limit |
| GLUndergroundResourceLimit | Underground Resource Aggregate Limit | No | Underground Resource Aggregate Limit |
| ProdWithdrawAgg | Aggregate Limit | No | Aggregate Limit |
| ProductWithdrawDeduct | Deductible | No | Deductible |
| ProductWithdrawPercent | Participating Percent | No | Participating Percent |
| ProductWithdrawCutOffDate | Cut Off Date | No | Cut Off Date |
| GLEmpBenefitsAggLimit | Aggregate Limit | No | Aggregate Limit |
| GLEmpBenefitsLiabDeduct | Deductible | No | Deductible |
| GLEmpBenefitsLiabilityCovRetroactiveDate | Retroactive Date | No | Retroactive date of employee benefits liability coverage |
| GLEmpBenefitsPerEmpLimit | Per Employee Limit | No | Per Employee Limit |
| Y2KBILimit | BI Limit | No | BI Limit |
| Y2KPDLimit | PD Limit | No | PD Limit |
| Y2KPersAdvrtInjuryLimit | Personal & Advertising Injury Limit | No | Personal & Advertising Injury Limit |
| Y2KDescription | Description of Operations | No |  |
| XCULocOpsHazBasis | XCU Locations/Ops/Hazard/Basis | No | XCU Locations/Ops/Hazard/Basis |
| CPBldgCovLimit | Limit | No | Limit |
| CPBldgCovDeductible | Deductible | No | Deductible |
| CPBldgCovWindDeductible | Wind % Deductible | No | Wind % Deductible |
| CPBldgCovCoinsurance | Coinsurance | No | Coinsurance |
| CPBldgCovCauseOfLoss | Cause Of Loss | No | Cause Of Loss |
| CPBldgCovValuationMethod | Valuation Method | No | Valuation Method |
| CPBldgCovAutoIncrease | Auto Increase % | No | Auto Increase % |
| CPBldgCovExcludeVandalism | Exclude Vandalism | No | Exclude Vandalism |
| CPBldgCovExcludeSprinkler | Exclude Sprinkler | No | Exclude Sprinkler |
| CPBldgCovExcludeTheft | Exclude Theft | No | Exclude Theft |
| CPBPPCovLimit | Limit | No | Limit |
| CPBPPCovCauseOfLoss | Cause Of Loss | No | Cause Of Loss |
| CPBPPCovDeductible | Deductible | No | Deductible |
| CPBPPCovWindDeductible | Wind Deductible % | No | Wind Deductible % |
| CPBPPCovCoinsurance | Coinsurance % | No | Coinsurance % |
| CPBPPValuationMethod | Valuation Method | No | Valuation Method |
| CPBPPCovReportingForm | Reporting Form | No | Reporting Form |
| CPBPPCovExcludeVandalism | Exclude Vandalism | No | Exclude Vandalism |
| CPBPPCovExcludeSprinkler | Exclude Sprinkler | No | Exclude Sprinkler |
| CPBPPCovExcludeTheft | Exclude Theft | No | Exclude Theft |
| CPBldgBusIncomeCovCoinsurance | Coinsurance % | No | Coinsurance % |
| CPBldgBusIncomeCovCauseOfLoss | Cause Of Loss | No | Cause Of Loss |
| CPBldgBusIncomeCovPeriod | Period of Coverage (in days) | No | Period of Coverage (in days) |
| CPBldgBusIncomeCovWaiting | Waiting Period (in hours) | No | Waiting Period (in hours) |
| BusIncomeOtherLimit | Income Limit - Not Mfg or Rental | No | Money limit for Business Income - other than mfg or rental |
| BusIncomeMfgLimit | Income Limit - Mfg Only | No | Money Limit for Business Income - Mfg Income only |
| BusIncomeRentalLimit | Income Limit - Rental Only | No | Money Limit for Business Income - Rental Income only |
| CPBldgExtraExpenseCovLimit | Limit | No | Limit |
| CPBldgExtraExpenseCovMonthLimit | Monthly Limit | No | Monthly Limit |
| CPBldgStockCovLimit | Limit | No | Limit |
| CPBldgStockCovCauseOfLoss | Cause Of Loss | No | Cause Of Loss |
| CPBldgStockCovDeductible | Deductible | No | Deductible |
| CPBldgStockCovWindDeductible | Wind Deductible % | No | Wind Deductible% |
| CPBldgStockCovValuationMethod | Valuation Method | No | Valuation Method |
| CPBldgStockCovCoinsurance | Coinsurance % | No | Coinsurance % |
| CPBldgStockCovReportingForm | Reporting Form | No |  |
| CPBldgStockCovExcludeVandalism | Exclude Vandalism | No | Exclude Vandalism |
| CPBldgStockCovExcludeSprinkler | Exclude Sprinkler | No | Exclude Sprinkler |
| CPBldgStockCovExcludeTheft | Exclude Theft | No | Exclude Theft |
| CPBlanketDeductible | Deductible | No | Deductible |
| CPBlanketCoinsurance | Coinsurance | No | Coinsurance |
| CPBlanketLimit | Limit | No | Blanket Limit |
| PAExcessElectronicsLimit | Increased Limit | No | Electronic Equipment Increased Limit |
| PARentalLossOfUseLimit | Rental Car Loss of Use Limit | No | Rental Car Loss of Use Limit |
| PATapeDiscMediaLimit | Tape / Disc Media Limit | No | Tape / Disc Media Limit |
| PALiability | Auto Liability Package | No | Auto Liability Package |
| PAFullLimitedTort | Full / Limited Tort | No | Full / Limited Tort |
| PAMedLimit | Medical Limit | No | Medical Limit |
| PAMedPayCoordinateBene | Coordinate Benefits | No | Coordinate Medical Benefits |
| PAPropProtectLimit | Property protection limits | No | Property protection limits |
| PAUIMBI | Underinsured Motorist BI Limits | No | Underinsured Motorist Bodily Injury Package |
| PAUIMBIstacked | Stacked Limits | No | Stacked Limits |
| PAUIMPDlimit | Underinsured Motorist - Property Damage Limit | No | Underinsured Motorist - Property Damage Limit |
| PAUIMPDstack | Stacked Limits | No | Stacked Limits |
| PAUMBI | Uninsured Motorist - BI Limits | No | Uninsured Motorist - BI Limits |
| PAUMBIIncludeUIM | Include Underinsured | No |  |
| PAUMBIstacked | Stacked Limits | No | Stacked Limits |
| PAUMPDLimit | Uninsured Motorist - Property Damage Limit | No | Uninsured Motorist - Property Damage Limit |
| PAUMPDstacked | Stacked Limits | No | Stacked Limits |
| PACollDeductible | Collision Deductible | No | Collision Deductible |
| PACollisionBroad | Broadened Collision | No | Broadened Collision |
| PACompDeductible | Comprehensive Deductible | No | Comprehensive Deductible |
| PACompZeroGlass | No deductible for glass | No | No deductible for glass |
| PARental | Rental Package | No | Rental Package |
| TowingAndLaborLimit | Towing and Labor Limit | No | Towing and Labor Limit |
| DeathBenefit | Death Benefit | No | Death Benefit |
| DisabilityBenefit | Disability Benefit - weekly | No | Disability Benefit - weekly |
| DismembermentBenefitLimit | Dismemberment and Fracture Benefit | No | Dismemberment and Fracture Benefit |
| PAPIP_AR_Med | Medical | No | Medical |
| PAPIP_AR_WorkLoss | Income | No | Income |
| PAPIP_AR_Death | Death | No | Death |
| PAPIP_DC_Medical | Medical | No | Medical |
| PAPIP_DC_Funeral | Funeral | No | Funeral |
| PAPIP_DC_WorkLoss | Income | No | Income |
| PAPIP_DE_Deductible | PIP Deductible | No | PIP Deductible |
| PAPIP_DE_Deduct_WhoApplies | Apply PIP Deductible to | No | Apply PIP Deductible to |
| PAPIP_DE_LIM | PIP Limit | No | PIP  Limit |
| PAPIP_FL_LIMIT | PIP Limit | No | PIP Limit |
| PAPIP_FL_Deductible | PIP Deductible | No | PIP Deductible |
| PAPIP_FL_WorkWaiver | Waive Income | No | Waive Income |
| PAPIP_FL_ApplyDeductible | Apply PIP Deductible to | No | Apply PIP Deductible to |
| PAPIP_HI_MedRehab | Medical | No | Medical |
| PAPIP_HI_WageLoss | Income | No | Income |
| PAPIP_HI_Death | Death | No | Death |
| PAPIP_HI_Funeral | Funeral | No | Funeral |
| PAPIP_HI_AltTreatment | Alternative Expenses | No | Alternative Expenses |
| PAPIP_HI_MANAGED_CARE | Managed Care | No | Managed Care |
| PAPIP_HI_MGDCARE_COPAY_DEDUCT | Managed Care Copays / Deductibles | No | Managed Care Copays / Deductibles |
| PAPIP_HI_DEDUCTIBLE | PIP Deductible | No | PIP Deductible |
| PAPIPKS_MED | Medical | No | Medical |
| PAPIPKS_REHAB | Rehabilitation | No | Rehabilitation |
| PAPIPKS_SERVICES | Services | No | Services |
| PAPIPKS_FUNERAL | Funeral | No | Funeral |
| PAPIPKS_WORK | Income | No | Income |
| PAPIPKS_SURVIVOR | Survivor | No | Survivor |
| PAPIPKY_Motorcycle | Motorcycle Coverage | No | Motorcycle Coverage |
| PAPIPKY_GuestONLY | Guest Coverage Only | No | Guest Coverage Only |
| PAPIPKY_AggLimit | PIP Aggregate Limit | No | PIP Aggregate Limit |
| PAPIPKY_Funeral | Funeral | No | Funeral |
| PAPIPKYWEEKLY | Income | No | Income |
| PAPIPMA_LIMIT | PIP Limit | No | PIP Limit |
| PAPIPMA_DEDUCTIBLE | PIP Deductible | No | PIP Deductible |
| PAPIPMA_WC | WC Discount | No | WC Discount |
| PAPIPMA_AIRBAG | Passive Restraint Discount | No | Passive Restraint Discount |
| PAPIPMD_LIMIT | PIP Limit | No | PIP Limit |
| PAPIPMD_WAIVER | Waived Individuals | No | Waived Individuals |
| PAPIPMD_GUEST | Guest PIP Only | No | Guest PIP Only |
| PAPIPMI_DEDUCTIBLE | PIP Deductible | No | PIP Deductible |
| PAPIPMI_MED | PIP Medical | No | PIP Medical - Unlimited |
| PAPIPMI_FUNERAL | PIP Funeral | No | PIP Funeral |
| PAPIPMI_INCOME | PIP Income | No | PIP Income |
| PAPIPMI_SURVIVOR | PIP Survivor | No | PIP Survivor |
| PAPIPMI_SERVICES | PIP Services | No | PIP Services |
| PAPIPMI_OtherProvider | COORDINATE PIP | No | COORDINATE PIP |
| PAPIPMN_MEDICAL | Medical | No | Medical |
| PAPIPMN_OTHER | Other Than Med | No | Other Than Med PIP Benefits |
| PAPIPMN_MED_DEDUCT | Medical Deductible | No | Medical Deductible |
| PAPIPMN_OTH_DEDUCT | Other Than Med Deductible | No | Deductible for all PIP coverages other than Medical |
| PAPIPMN_STACK | Stack Pip Limits | No | Stack Pip Limits - requires 2+ vehicles |
| PAPIPMN_EXC_WORK | Exclude Income | No | Exclude Income |
| PAPIPMN_CYCLE | Motorcycles | No | Extend PIP coverage to Motorcycles |
| PAPIPMN_WORK | Income | No | Income |
| PAPIPMN_SERVICES | Services | No | Services |
| PAPIPMN_SURVIVOR | Survivor | No | Survivor |
| PAPIP_ND_INCOME | PIP Income | No | PIP Income |
| PAPIPND_SERVICE | Services | No | Services |
| PAPIPND_FUNERAL | Funeral | No | Funeral |
| PAPIP_ND_MEDICAL | PIP Medical | No | PIP Medical |
| PAPIPND_AGG | ND PIP AGGREGATE Limit | No |  |
| PAPIPND_SURVIVOR | ND PIP Survivor Benefit | No | NORTH DAKOTA ; |
| PAPIPNJ_MEDLIMIT | Medical | No | Medical |
| PAPIPNJ_MEDDEDUCT | Medical Deductible | No | Medical Deductible |
| PAPIPNJ_MEDDEDUCTappliesto | Medical Deductible applies to | No | Medical Deductible applies to |
| PAPIPNJ_MEDONLY | Med Only option | No | Med Only option |
| PAPIPNJ_MEDsecondary | PIP Med is secondary | No | PIP Med is secondary |
| PAPIPNJ_MED_COPAY | Medical Copay Option | No | Medical Copay Option |
| PAPIPNJ_OTHER_LIMS | NON-Medical Benefits | No | NON-Medical Benefits (weekly income/max income /daily services/max services / funeral / death) |
| PAPIPNY_DEDUCTIBLE | Deductible | No | Deductible |
| PAPIPNY_MOTORCYCLE | Motorcycle | No | Motorcycle |
| PAPIPNY_EXMED | Exclude Medical | No | Exclude Medical |
| PAPIPNY_DEATH | Death | No | Death |
| PAPIPNY_OBEL | Opt. Basic Econ. Loss | No | Opt. Basic Econ. Loss |
| PAPIP_NY_AGGREGATE | PIP Aggregate  | No | PIP Aggregate  |
| PAPIPNY_INCOME | PIP Income | No | PIP Income |
| PAPIPNY_EXPENSE | PIP Expense | No | PIP Expense |
| PAPIPOR_DEDUCT | Deductible | No | Deductible |
| PAPIPOR_DEDUCTIBLEappliesto | Deductible Applies To | No | Deductible Applies To |
| PAPIPOR_MED | PIP Medical | No | PIP Medical |
| PAPIPOR_INCOME | PIP Income | No | PIP Income |
| PAPIPOR_SERVICES | PIP Services | No | PIP Services |
| PAPIPOR_CHILDCARE | PIP Childcare | No | PIP Childcare |
| PAPIPOR_FUNERAL | PIP Funeral | No | PIP Funeral |
| PAPIPPA_MEDICAL | Medical | No | Medical |
| PAPIPPA_INCOME | Income | No | Income |
| PAPIPPA_DEATH | Death | No | Death |
| PAPIPPA_FUNERAL | Funeral | No | Funeral |
| PAPIPPA_COMBINED | COMBINED Limit | No | COMBINED Limit |
| PAPIPPA_EXTRAMED | Extraordinary Medical | No | Extraordinary Medical |
| PAPIPTX_LIMIT | PIP Limit | No | PIP Limit |
| PAPIPUT_MEDICAL | Medical | No | Medical |
| PAPIPUT_WORK | Income | No | Income |
| PAPIPUT_FUNERAL | Funeral | No | Funeral |
| PAPIPUT_SURVIVOR | Survivor | No | Survivor |
| PAPIPWA_MED | PIP Medical | No | PIP Medical |
| PAPIPWA_INCOME | PIP Income | No | PIP Income |
| PAPIPWA_SERVICES | PIP Services | No | PIP Services |
| PAPIPWA_FUNERAL | PIP Funeral | No | PIP Funeral |
| IMSignLimit | Limit | No | Inland Marine Sign Limit |
| IMSignDeductible | Deductible | No | Inland Marine Sign Deductible |
| ContractorsEquipSchedCovLimit | Limit | No | Contractors Scheduled Equipment Limit |
| ContractorsEquipSchedCovDeductible | Deductible | No | Contractors Scheduled Equipment Deductible |
| ContractorsEquipSchedCovValuation | Valuation | No | Contractors Scheduled Equipment Valuation |
| ContractorsEquipRentalReibursementOccurrenceLimit | Occurrence Limit | No | Contractors Rental Reimbursemet - Per Occurrence |
| ContractorsEquipRentalReibursementDeductible | Deductible | No |  |
| ContractorsEquipRentalPolicyLimit | Aggregate Limit | No | Per Policy Aggregate |
| ContractorsEquipRentedEquipmentLimit | Limit | No |  |
| ContractorsEquipRentedEquipmentDeductible | Deductible | No |  |
| ContractorsEquipRentedEquipmentMaxIndivItemVal | Max Individual Item Value | No | Rented Equipment, maximum item value |
| ContractorsEquipEmployeesToolsLimit | Limit | No | Employees' Tools Limit |
| ContractorsEquipEmployeesToolsDeductible | Deductible | No | Employees' Tools Deductible |
| ContractorsEquipEmployeesToolsMaxIndivItemVal | Max Individual Item Value | No | Max Individual Item Value |
| ContractorsEquipMiscUnscheduledLimit | Limit | No |  |
| ContractorsEquipMiscUnscheduledDeductible | Deductible | No | Unscheduled Items Deductible |
| ContractorsEquipMiscUnschItemMaxItemVal | Max Individual Item Value | No | Maximum limit per unscheduled item |
| AccountsRecOffPremisesPropertyLimit | Limit | No | Limit |
| AccountsRecOffPremisesPropertyDescription | Description | No | Description of Off Premises Account Receivables Records |
| IMAccountsReceivableLimit | Limit | No | Accounts Receivable Limit |
| WCFedEmpLiabCovProgram | Program I / II | No | WC Fed Liability Program Type I / II |
| WCFedEmpLiabLimit | Limit per Accident | No | Per Accident Limit |
| FedEmpLiabAct | WC Fed Liab Act | No | WC Federal Liability Act |
| WCFedEmpLiabilityLaw | WC Fed Liab Law | No | WC Fed Liab Law |
| FELADisease | Disease Aggregate Limit | No | Disease Aggregate Limit |
| WCEmpLiabLimit | Employer's Liability Limit | No | Employer's Liability Limit |
| WCStopGapOpt | Stop Gap | No | Stop Gap |
| WCIncludedMonopolisticStates | Included Monopolistic States | No | Included Monopolistic States |
| WCOtherStatesOpt | Covered States | No | Covered States |
| WCIncludedStates | Included States | No | Included States |
| WCExcludedStates | Excluded States | No | Excluded States |
| WCDeductible | Deductible | No | Deductible |
| BOPBldgLim | Building Limit | No | Building Limit |
| BOPBldgValuation | Valuation Method | No | Valuation Method |
| BOPBuildingCoin | Coinsurance | No | Coinsurance |
| BOPBldgAnnualIncrease | Building Annual Increase % | No |  |
| BOPOrdLawCov23Lim | BOP Ordinance or Law Combined 2,3 Limit | No | BOP Ordinance or Law Combined 2,3 Limit |
| BOPOrdLawCov2Lim | Ordinance or Law Coverage 2 Limit | No | Ordinance or Law Coverage 2 Limit |
| BOPOrdLawCov3Lim | BOP Ordinance or Law Coverage 3 Limit | No | BOP Ordinance or Law Coverage 3 Limit |
| BOPOrdLawIncomeExpense | Ordinance or Law - Income/Expense | No | Ordinance or Law - Income/Expense |
| BOPOrdLawIncomeExpenseDeduct | BOP Ordinance or Law - Income/Expense Deductible | No | BOP Ordinance or Law - Income/Expense Deductible |
| BOPOrdLawCov1yesno | BOP Ordinance or Law Coverage 1 Election | No | BOP Ordinance or Law Coverage 1 Election |
| BOPBPPBldgLim | Business Personal Property Limit | No | Business Personal Property Limit |
| BOPBPPValuation | Valuation Method | No | Valuation Method |
| BOPPersonalPropCoin | Coinsurance | No | Coinsurance |
| BOPARonPremLim | AR On Premises Limit | No | AR On Premises Limit |
| BOPReceivablesOffPremLim | AR Off Premises Limit | No | AR Off Premises Limi |
| BOPValPaperOnPremLim | Papers On Premises Limit | No | Papers On Premises Limit |
| BOPValPapersOffPremLimit | Papers Off Premises Limit | No | Papers Off Premises Limit |
| CondoMiscProp | Condo Miscellaneous Property Limit | No | Condo Unit owner |
| CondoLossAssessment | Condo Loss Assessment | No | Condo Loss Assessment |
| CondoOwnerLimit | Condo Owner Limit | No | Condo Owner Limit |
| CondoMiscPropDed | Condo Miscellaneous Property Deductible | No | Condo Miscellaneous Property Deductible |
| BOPElectricalSchedLimit | Electrical Equipment - Scheduled Limit | No | Electrical Equipment - Scheduled Limit |
| BOPFuncPerPropLim | Functional Business Personal Property Limit | No | Functional Business Personal Property Limit |
| BOPTenantsLiabLim | Tenants Liability Limit | No | Tenants Liability Limit |
| BOPVacancyChange | Vacancy Change - Pct Occupied | No | Vacancy Change - Pct Occupied |
| BOPSprinklerLeak | Sprinkler Leakage | No | Sprinkler Leakage |
| BOPVacancyCovFromDate | From Date | No | From |
| BOPVacancyCovToDate | To Date | No | To Date |
| BOPVandalism | Vandalism | No | Vandalism |
| BOPMechBreakdownLim | Breakdown Limit | No | Breakdown Limit |
| BOPMechBreakdownDeduct | Breakdown Deductible | No | Breakdown Deductible |
| BOPMechBreakdownIncomeDeduct | Business Income Deductible | No | Business Income Deductible |
| BOPUtilDirectLim | Direct Loss Limit | No | Direct Loss Limit |
| BOPUtilDirectComm | Communications (not O/H lines) | No | Communications (not O/H lines) |
| BOPUtilDirectPower | Power (not O/H lines) | No | Power (not O/H lines) |
| BOPUtilDirectPowerOH | Power (inc O/H lines) | No | Power (inc O/H lines) |
| BOPUtilDirectWater | Water Supply | No | Water Supply |
| BOPUtilDirectCommOH | Communications (inc O/H lines) | No | Communications (inc O/H lines) |
| BOPUtilTimeLim | Utilities Time Element Limit | No | Utilities Time Element Limit |
| BOPUtilTimePowerOH | Power (inc O/H lines) | No | Power (inc O/H lines) |
| BOPUtilTimeWater | Water Supply | No | Water Supply |
| BOPUtilTimeCommOH | Communications (inc O/H lines) | No | Communications (inc O/H lines) |
| BOPUtilTimePower | Power (not O/H lines) | No | Power (not O/H lines) |
| BOPUtilTimeComm | Communications (not O/H lines) | No | Communications (not O/H lines) |
| BOPToolsSchedLim | Contractors Tools - Scheduled Limit | No | Contractors Tools - Scheduled Limit |
| BOPBurgRobLim | Burglary and Robbery Limit | No | Burglary and Robbery Limit |
| BOPComputerFraudLim | Computer Fraud Limit | No | Computer & Funds Transfer Fraud Limit |
| BOPForgeAltLimit | Forgery and Alteration Limit | No | Forgery and Alteration Limit |
| BOPMoneyOnPremLim | Money & Securities On Premise Limit | No | Money & Securities On Premise Limit |
| BOPMoneyOffPremLim | Money & Securities Off Premise Limit | No | Money & Securities Off Premise Limit |
| BOPBIDepPropLim | Bus. Income-Dependent Prop. Limit | No | Dependent Prop. Limit |
| BusIncomeExtended | Business Income - Extended Period | No | Business Income - Extended Period |
| BusIncomeOrdPayroll | Business Income - Ordinary Payroll | No | Business Income - Ordinary Payroll |
| BOPY2KIncomeExpenseLim | Location Aggregate Limit | No | Location Aggregate Limit |
| SBSpecialPacks | Special Coverages Packages | No | Special Coverages Packages |
| BOPLiability | Limits: Occurrence / Prod Agg / Gen Agg | No | Limits: Occurrence / Prod Agg / Gen Agg |
| BOPLiabPDDeductible | PD Deductible | No | PD Deductible |
| BOPLiabDeductType | PD Deductible Type | No | PD Deductible Type |
| BOPMedExpenseLimit | Premises Medical Expense Limit | No | Premises Medical Expense Limit |
| BOPTenantsFireLiabBaseLimit | Tenants Fire Liability Limit | No | Tenants Fire Liability Limit |
| BOPEmpBenAggLim | Employees Benefits Agg Limit | No | Employees Benefits Agg Limit |
| BOPEmpBenEachEmpDed | Employees Benefits Each Employee Deductible | No | Employees Benefits Each Employee Deductible |
| BOPEmpBenEachEmpLim | Employees Benefits Each Employee Limit | No | Employees Benefits Each Employee Limit |
| BOPEmpBenRetroDate | Retroactive Date | No | Retroactive Date |
| BOPPollutionLim | Limited Pollution Liability Agg Limit | No | Limited Pollution Liability Agg Limit |
| BOPFoodContamAdvLim | Food Contamination Adv. Limit | No | Food Contamination Adv. Limit |
| BOPFoodContamLim | Food Contamination Limit | No | Food Contamination Limit |
| BOPFungiPropLim | Fungi Aggregate Limit | No | Fungi Aggregate Limit |
| BOPFungiAggLevel | Agg Limit Level | No | Agg Limit Level |
| BOPFungiTimeCov | Time Element Limit | No | Time Element Limit |
| BusIncWaitingPeriod | Waiting Period | No | Waiting Period |
| BOPLiquorAggLim | Liquor Liability Aggregate Limit | No | Liquor Liability Aggregate Limit |
| BOPLiquorCauseBILim | Liquor Liability Each Common Cause BI Limit | No | Liquor Liability Each Common Cause BI Limit |
| BOPLiquorCauseLim | Liquor Liability Common Cause Limit | No | Liquor Liability Common Cause Limit |
| BOPLiquorCauseMSLim | Liquor Liability Each Comon Cause Loss of Means of Support Limit | No | Liquor Liability Each Comon Cause Loss of Means of Support Limit |
| BOPLiquorMSLim | Liquor Liability Loss Of Means Of Support Or Loss Of Society Limit | No | Liquor Liability Loss Of Means Of Support Or Loss Of Society Limit |
| BOPLiquorPersonBILim | Liquor Liability Each Person BI Limit | No | Liquor Liability Each Person BI Limit |
| BOPLiquorPersonLim | Liquor Liability Each Person Limit | No | Liquor Liability Each Person Limit |
| BOPLiquorPersonMSLim | Liquor Liability Each Person Loss of Means of Support Limit | No | Liquor Liability Each Person Loss of Means of Support Limit |
| BOPLiquorPersonPDLim | Liquor Liability Each Person PD Limit | No | Liquor Liability Each Person PD Limit |
| LiqLiabEventsDescription | Event Description | No | Event Description |
| LiqLiabEventDate | Event Date | No |  |
| BOPWindHailDed | Windstorm/Hail  % Deductible | No | Windstorm/Hail  % Deductible |
| BOPWindHailMoneyDed | Windstorm/Hail $ Deductible | No | Windstorm/Hail $ Deductible |
| BOPOutdoorPropLim | Outdoor Property Limit(Per Item/Agg) | No | Outdoor Property Limit(Per Item/Agg) |
| BOPOutdoorSignLim | Outdoor Sign Limit | No | Outdoor Sign Limit |
| BOPOverflowLim | Backup/Overflow Limit | No | Backup/Overflow Limit |
| BOPPersEffectsLim | Personal Effects Limit | No | Personal Effects Limit |
| BOPPerPropOffPremLim | Off Premises Personal Property | No | Off Premises Personal Property |
| BOPSpoilageCovDescription | Description | No | Description of Coverage or Schedule of Covered items |
| BOPPowerOutage | BOPPowerOutage | No | Power Outage |
| BOPFridgeMaintenance | Refridgeration Maintenance | No | Refrigeration Maintenance Agreement |
| BOPBreakContam | Breakdown or Contamination | No | Breakdown or Contamination |
| BOPSpoilageDed | Deductible | No | Deductible |
| BOPSpoilageLim | Limit | No | Limit |
| BOPBarberBeautNum | Licensed Individuals - Count | No | Licensed Individuals - Count |
| BOPFuneralDirNum | Licensed Individuals - Count | No | Licensed Individuals - Count |
| BOPHearingAidSales | Gross Sales | No | Gross Sales |
| BOPPhamacistSales | Gross Sales | No | Gross Sales |
| BOPPrinterSales | Gross Sales | No | Gross Sales |
| BOPVetNum | Licensed Individuals - Count | No | Licensed Individuals - Count |
| BOPInstallationLim | PerJob/All Jobs Limit | No | PerJob/All Jobs Limit |
| BOPToolsBlanketLim | Contractors Tools Blanket | No | Contractors Tools Blanket |
| BOPToolsEmployees | Contractors Employees Tools | No | Contractors Employees Tools |
| BOPToolsNonOwnedLim | Contractors NonOwned Tools | No | Contractors NonOwned Tools |
| BOPAlaskaAFGLLim | Alaska Attorney Fees Limit | No | Alaska Attorney Fees Limit |
| BOPCAEqBldgRecLimit | CA Earthquake Reconstruction Cost  Limit | No | CA Earthquake Reconstruction Cost  Limit |
| BOPCAEqBldgSubDed | CA Earthquake - Building Sublimits Deductible | No | CA Earthquake - Building Sublimits Deductible |
| BOPCAEqBldgSubLim | CA Earthquake - Building Sublimits | No | CA Earthquake - Building Sublimits |
| BOPCertTerrorCapLimit | Aggregate Limit | No | Aggregate Limit |
| BOPBaseDed | Property Base Deductible | No | Property Base Deductible |
| BOPGlassDed | Glass Deductible | No | Glass Deductible |
| BOPOptCovDed | Optional Coverages Deductible | No | Optional Coverages Deductible |
| BOPPropBuildDed | Property Optional Deductible | No | Property Optional Deductible |
| BOPPropertyCovCauseOfLoss | Cause Of Loss | No | Building Coverage Form |
| EQDeductible | EQ % Deductible | No | EQ % Deductible |
| BOPMineSubLim | Mine Subsidence Limit | No | Mine Subsidence Limit |
| BOPEmpDisLimit | Employee Dishonesty Limit | No | Employee Dishonesty Limit |
| BOPEmpDisNumEmp | Number of Covered Employees | No | Number of Covered Employees |
| BOPEmpDisNumLoc | Number of Covered Locations | No | Number of Covered Locations |
| GuestPropClaimLim | Guest Property - limit per Guest | No | Guest Property - limit per Guest |
| GuestPropOccLim | Guests Property Occurrence Limit | No | Guests Property Occurrence Limit |
| BOPGuestSafeDepLimit | Guest Property - Safe Deposit Limit | No | Guest Property - Safe Deposit Limit |
| zjihof5u6p0ob195orrdcmauhpa | CovE Limit | No | Personal Liability Limit |
| zh4g6se5d9cc545f97tn498tsm8 | Personal Injury | No | Personal Injury |
| zr6hcc8odmd006c8d9biad684da | CovF Limit | No | Medical Payments Limit |
| zuhhq4ac7p78j6bt9u6gapf92o9 | CovA Limit | No | Dwelling Limit |
| zqlg02is5fdfeekq2kuu8vnem79 | Coinsurance | No | Coinsurance |
| z8ugc5n3dv8bu7pbhkkbeiv23s9 | Valuation Method | No | Valuation Method |
| zc2j8chomjs3adiai3m74vl50ra | Cause of Loss | No | Cause of Loss |
| zhtie7v97j1864502v6pu6ru5u8 | CovB Limit Pct | No | Other Structures Limit Pct |
| z4ogou9jlvl0q1jjv8fa4jf2b18 | CovB Limit | No | Other Structures Limit  |
| zc1ia45ph8a7i5plpkbr35mp2c9 | CovC Limit Pct | No | Personal Property Limit Pct |
| zalgosqi0n5nbbdpe0l7nep5l5b | Property at Other Residence | No | Property at Other Residence |
| z0jjmb897bn960lvevaiagk4j38 | CovC Limit  | No | Personal Property Limit |
| zq0juckbo7cpvcgjed6459aic49 | Self Storage Units | No | Self Storage Units |
| z6vgm3qsh6cll9aur7b7jl9vr19 | Cause of Loss | No | Cause of Loss |
| zmmic6abinst0brv5j5p4fg2uca | Valuation Method | No | Valuation Method |
| zccjq08o5p47o1msqlbef57be2b | CovD Limit Pct | No | Loss of Use Limit Pct |
| zmjhmpiqq348g1i0gqgsdhhh9q9 | Loss of Rental Income | No | Loss of Rental Income |
| zdbiq4n6t22tqdq906jh6k5sbb9 | Prohibited Use - Civil Authority | No | Prohibited Use - Civil Authority |
| zgghesfp77k231ct483vgs9f7ub | CovD Limit | No | Loss of Use Limit |
| zm7g2sosoafsv74h974bld972ta | All Other Perils | No | All Other Perils |
| zfvimq6hie4hr27sr3r4gfu8pnb | All Perils | No | All Perils |
| zj8ik0gtjuev47mdmkj29th5jt9 | Hurricane Windstorm | No | Hurricane Windstorm |
| HOPSectionIDeductiblesEarthquake | Earthquake | No | Earthquake |
| zpbhoiumut2dk7dsff5ao5nro59 | Windstorm or Hail | No | Windstorm or Hail |
| zmcg09it95nsa2cc4va1ia5b118 | Limit | No | Limit |
| zpiisldptve6k4m41uo29bjk6ta | Permits Limit | No | Permits Increased Cost Limit |
| z11jolhuvvubg9sscbpd6mcs4i8 | Limit | No | Limit |
| ztnh6llp5fe5j2m58qnu7nc5fab | Property of Others Limit | No | Property of Others Limit |
| zonisjg5e30c114s32p2shpo5na | Personal Only | No | Personal Only |
| zj5iembc591apahqggk4cgvcft8 | Data & Records Limit | No | Data & Records Limit |
| zidhqs5kvipod72ar5le6k5higa | Limit | No | Limit |
| z2chk05cobia54qdqjoubspaqg9 | Power Failure Expense Limit | No | Power Failure Expense Limit |
| zm7hstt7p1obq7ovms6a6aok3o8 | Property Removal Limit | No | Property Removal Limit |
| zipjiqfv4ng8acrdf0uuddc3g38 | FD Service Limit | No | Fire Department Service Charge Limit |
| zsnjkur9omblc1n30gaj2ak50f9 | Recharge Limit | No | Fire Extinguisher Recaharge Limit |
| zn3h08rtlfpde43obiudbq09ja9 | Fungi Remediation Limit | No | Fungi Remediation Limit |
| zochcqdagct1lcav18gldrn6kqb | Monument Limit | No | Monument Limit |
| z09g6cvnpu8ka694pj71dsv9s78 | ID Theft Limit | No | ID Theft Expense Limit |
| zcphighm142918rg39gspdqqln9 | Deductible | No | Deductible |
| zucikjgff28ikd57vgo0v17hel8 | Annual Increase | No | Annual Increase |
| z6ki2rhsse7lf631h8n130pj0d8 | Limit | No | Limit |
| zhlge07d7quku5kk35hk3ksuum9 | Loss Assessment Limit | No | Loss Assessment Limit |
| z4ti6io51subg14r1j2vdh6if89 | Mortgage Exp Limit | No | Mortgage Closing Cost Limit |
| zecge7q4j80a91gemca3j496na8 | Limit | No | Limit |
| zb7ju1l6o4fggbmkbf8dmq3qps9 | EQ/Flood Off PremisesLimit | No | Earthquake or Flood Off Premises Limit |
| zneh8p1jbds7ud09i345kbu50sa | Limit for Arson or Recovered Property | No | Limit for Arson or Recovered Property |
| zfigedt82ie1129tk1tql0j49e8 | Limit for Theft Conviction | No | Limit for Theft Conviction |
| zhdic49albr924jec7klvulhoa8 | Landscape Limit | No | Tree, Shrub, Plants and Lawn Limit |
| zteg0fguld0sccqafgenav4ff79 | Backup Limit | No | Sewer, Drain or Sump Backup Limit |
| zpni4ecv2jd3de9ekhpl7gn19j9 | Deductible | No |  |
| zhvha9tspf14tdtoms11pena158 | Masonry Veneer Exclusion | No | Masonry Veneer Exclusion |
| z4phqb5m98p7o8f4f64bindbge8 | EQ Deductible | No | Earthquake Deductible |
| zv3g6aos8sp4iarh5nbmo5cfer8 | Fungi and Mold Liability Limit | No | Limited Fungi and Mold Liability Limit |
| z3ijkag98i052btcjqef390hkg9 | In Residence | No |  |
| znsi8h8pr0d28a6gb8e3psodidb | Description of Business | No |  |
| z88g4jt7ovvl6eqbn243fl6kttb | Limit | No | Limit |
| zbugmd8apaqcl5oc5knc0rd62eb | Deductible | No | Deductible |
| zsfiibsn5vfk95pvjsfnnvdf6h8 | Limit Cov C | No |  |
| zloh23v5tvo9h22u9s6ujgdqg5a | Assisted Living Liability Limit | No | Assisted Living Liability Limit |
| zetg68o4lcajf1nt9frdn77ogmb | Include Collision | No |  |
| z0pjsih9gkurgbh648e992svj88 | Limit | No |  |
| zagjum6b0mkagbks5gmb3gc58vb | Limit | No |  |
| zbnhu6nt78onmd8kecdg4st4vi8 | Limit | No |  |
| zsnh23eboma1o5drue4vhdhhkl9 | Limit | No |  |
| ziej03pfje7079tt5ug6uag6468 | Unit Limit | No | Unit Limit |
| zk4i8n347nmmtd6ve4j3b8utcj8 | Limit | No | Limit |
| z90golpur3a4feu7fgtkg60in98 | Deductible | No | Deductible |
| z6ii69kdt74egdr5lbkdus1ck8a | Valuation Method | No | Valuation Method |
| z0dgc55rc23ho41up1t30049hqb | Type | No |  |
| z0rj2ab9ajr9n0c821onqkj7209 | Appraised Value | No | Appraised Value |
| zaagmovelvmh03d5ur750svk1fb | Limit | No |  |
| zfui0ffmtkk791n0hi96k2njjr9 | Limit | No |  |
| zpoh0pntlgeci4n6otmb0n7rc59 | Per Item | No | Per Item |
| zrfje8tkfiolp0tu76rl0uhun6b | Aggregate Limit | No | Aggregate Limit |
| z8fiamifodmqv8ve4nn3u87cdf8 | Type | No |  |
| BADOCCollisionDeduct | Collision Deductible | No | Collision Deductible |
| BADOCCompDeduct | Comprehensive Deductible | No | Comprehensive Deductible |
| BADOCLiabilityLiab | Auto Liability Package | No | Auto Liability Package |
| BADOCMedPayLimit | Medical Limit | No | Medical Limit |
| BADOCUnderinsBI | Underinsured Motorist Bodily Injury Package | No | Underinsured Motorist Bodily Injury Package |
| BADOCUninsuredBI | Uninsured Motorist Bodily Injury Package | No | Uninsured Motorist Bodily Injury Package |
| BAAudVisDataEquipDed | Audio Visual Data Equipment Deductible | No | Audio Visual Data Equipment Deductible |
| BAAudVisDataEquipLim | Audio, Visual, Electronic Equipment | No | Audio, Visual, Electronic Equipment |
| BAHiredCollDeduct | Hired Auto Collision Deductible | No | Hired Auto Collision Deductible |
| BAHiredCompDeduct | Hired Auto Comprehensive Deductible | No | Hired Auto Comprehensive Deductible |
| BAHiredLiabilityBI | Liability BI | No | Liability BI |
| BAHiredSpecPerilCovHiredCauseOfLoss | Cause of Loss | No | Cause of loss |
| BAHiredSpecPerilDdct | Deductible | No | Deductible |
| BANonownedLiabBI | Liability Bodily Injury | No | Liability Bodily Injury |
| BADealerLimitLiabClass1 | Class 1 Employees | No | Class 1 Employees |
| BADealerLimitLiabClass2 | Class 2 Employees | No |  |
| BADealerLimitLiabTotalEmp | Total Employees - Class 1 | No |  |
| BADealerLimitLiabCustomer | Unlimited Customer Liability | No |  |
| BADealerLimitLiabLimit | Limit | No |  |
| BAOwnedLiabilityLimit | Liability Limit | No | Liability Limit - BI and PD |
| BALiabilityTort | Full or Limited Tort | No |  |
| BAOwnedMedPayLimit | Limit | No | Medical Payment Limit |
| BAOwnedMedPayCoordinate | Coordinate Benefilts | No | Coordinate Benefilts |
| BASeasonalTrailerLiabDesc | Description of Trailers | No | Description of Trailers |
| BASeasonTrailerLiabProdTransp | Produce Transported | No | Produce Transported |
| BASeasonTrailerLiabCount | Trailer Count | No | Trailer Count |
| BASeasonTrailerLiabStartDate | Start Coverage | No | Start Coverage |
| BASeasonTrailerLiabEndDate | End Coverage | No | End Coverage |
| BASeasonTrailerLiabLimit | Limit | No | Limit |
| BACollisionDeduct | Collision Deductible | No | Collision Deductible |
| BACollisionBroad | Collision Broadened | No | Collision Broadened |
| BAComprehensiveDdct | Comprehensive Deductible | No | Comprehensive Deductible |
| BAZeroGlass | No Deductible for Glass | No | No Deductible for Glass |
| BASpecCausesLossCovSpecifiedCauseOfLoss | Specified Cause of Loss | No | Specified Cause of Loss |
| BASpecCausesLossDdct | Deductible | No | Deductible |
| BATow | Towing Limit | No |  |
| BARental | Rental Package | No | Rental Package |
| BATapeDiscLimit | Tape Disc Record Limit | No | Tape Disc Record Limit |
| BALimitedPropDamLmt | Limited Property Damage Limit | No | Limited Property Damage Limit |
| BAOwnedUIMBI | Underinsured Motorist Bodily Injury Package | No | Underinsured Motorist Bodily Injury Package |
| BAUIMPDLimit | Underinsured Motorist - Property Damage Limit | No | Underinsured Motorist - Property Damage Limit |
| BAOwnedUMBI | Uninsured Motorist Bodily Injury Package | No | Uninsured Motorist Bodily Injury Package |
| BAUMEconomicOnly | Economic Only | No | Economic Only |
| BAOwnedUMStack | Stack UM Coverage | No | Stack UM Coverage |
| BAOwnedUMStackUIM | Stack UM / UIM Coveages | No | Stack UM / UIM Coveages |
| BAOwnedUMConversion | UIM Conversion | No | UIM Conversion |
| BAOwnedUMBISuppBI | Liability BI | No | Liability BI |
| BAUMPDLimit | Uninsured Motorist - Property Damage Limit | No | Uninsured Motorist - Property Damage Limit |
| BAPropProtectLimit | Property protection limits | No | Property protection limits |
| DeathBenefitLimit | Death Benefit | No | Death Benefit |
| DisabilityBenefitLimit | Disability Benefit / weekly | No | Disability Benefit / weekly |
| PIP_DE_Deductible | PIP Deductible | No | PIP Deductible |
| PIP_DE_Deduct_WhoApplies | Apply PIP Deductible to | No | Apply PIP Deductible to |
| BAPIP_DE_LIM | PIP Limit | No | PIP  Limit |
| CAPIP_FL_LIMIT | PIP Limit | No | PIP Limit |
| CAPIP_FL_Deductible | PIP Deductible | No | PIP Deductible |
| CAPIP_FL_WorkWaiver | Waive Income | No | Waive Income |
| CAPIP_FL_ApplyDeductible | Apply PIP Deductible to | No | Apply PIP Deductible to |
| PIP_HI_MedRehab | Medical | No | Medical |
| WageLoss | Income | No | Income |
| HI_Death | Death | No | Death |
| PIP_HI_Funeral | Funeral | No | Funeral |
| PIPAltTreatment | Alternative Expenses | No | Alternative Expenses |
| PIPHI_MANAGED_CARE | Managed Care | No | Managed Care |
| PIPHI_MGDCARE_COPAY_DEDUCT | Managed Care Copays / Deductibles | No | Managed Care Copays / Deductibles |
| PIPHI_DEDUCTIBLE | PIP Deductible | No | PIP Deductible |
| PIPKS_MED | Medical | No | Medical |
| PIPKS_REHAB | Rehabilitation | No | Rehabilitation |
| PIPKS_SERVICES | Services | No | Services |
| PIPKS_FUNERAL | Funeral | No | Funeral |
| PIPKS_WORK | Income | No | Income |
| PIPKS_SURVIVOR | Survivor | No | Survivor |
| KYPIP_Motorcylce | Motorcycle Coverage | No | Motorcycle Coverage |
| PIPKY_GuestONLY | Guest Coverage Only | No | Guest Coverage Only |
| PIPKY_AggLimit | PIP Aggregate | No | PIP Aggregate Limit |
| PIPKY_Funeral | Funeral | No | Funeral |
| PIPKYWEEKLY | Income | No | Income |
| PIPMA_PIP | PIP Limit | No | PIP Limit |
| PIPMA_DEDUCTIBLE | PIP Deductible | No | PIP Deductible |
| PIPMA_WC | WC Discount | No | WC Discount |
| PIPMA_AIRBAG | Passive Restraint Discount | No | Passive Restraint Discount |
| PIPMD_PIP | PIP Limit | No | PIP Limit |
| PIPMD_WAIVER | Waived Individuals | No | Waived Individuals |
| PIPMD_GUEST | Guest Pip Only | No | Guest Pip Only |
| PIPMI_DEDUCTIBLE | PIP Deductible | No | PIP Deductible |
| PIPMI_MED | PIP Medical | No | PIP Medical - Unlimited |
| PIPMI_FUNERAL | PIP Funeral | No | PIP Funeral |
| PIPMI_INCOME | PIP Income | No | PIP Income |
| PIPMI_SURVIVOR | PIP Survivor | No | PIP Survivor |
| PIPMI_SERVICES | PIP Services | No | PIP Services |
| PIPMI_OtherProvider | Coordinate PIP | No | Coordinate PIP |
| PIPMN_MEDICAL | Medical | No | Medical |
| PIPMN_OTHER | Other Than Med | No | Other Than Med PIP Benefits |
| PIPMN_MED_DEDUCT | Medical Deductible | No | Medical Deductible |
| PIPMN_OTH_DEDUCT | Other Than Med Deductible | No | Deductible for all PIP coverages other than Medical |
| PIPMN_STACK | Stack PIP Limits | No | Stack PIP Limits - requires 2+ vehicles |
| PIPMN_EXC_WORK | Exclude Income | No | Exclude Income |
| PIPMN_CYCLE | Motorcycles | No | Extend PIP coverage to Motorcycles |
| PIPMN_WORK | Income | No | Income |
| PIPMN_SERVICES | Services | No | Services |
| PIPMN_SURVIVOR | Survivor | No | Survivor |
| CAPIP_ND_INCOME | PIP Income | No | PIP Income |
| PIPND_SERVICE | Services | No |  |
| PIPND_FUNERAL | Funeral | No |  |
| CAPIP_ND_MEDICAL | PIP Medical | No | PIP Medical |
| PIPND_AGG | ND PIP Aggregate Limit | No |  |
| PIPND_SURVIVOR | ND PIP Survivor Benefit | No | North Dakota ; |
| PIPNJ_MEDLIMIT | Medical | No | Medical |
| PIPNJ_MEDDEDUCT | Medical Deductible | No | Medical Deductible |
| PIPNJ_MEDDEDUCTappliesto | Medical Deductible applies to | No | Medical Deductible applies to |
| PIPNJ_MEDONLY | Med Only Option | No | Med Only Option |
| PIPNJ_MEDsecondary | PIP Med is secondary | No | PIP Med is secondary |
| PIPNJ_MED_COPAY | Medical Copay Option | No | Medical Copay Option |
| PIPNJ_OTHER_LIMS | Non-Medical Benefits | No | Non-Medical Benefits (weekly income/max income /daily services/max services / funeral / death) |
| PIPNY_DEDUCTIBLE | Deductible | No |  |
| PIPNY_MOTORCYCLE | Motorcycle | No | Motorcycle |
| PIPNY_EXMED | Exclude Medical | No | Exclude Medical |
| PIPNY_DEATH | Death | No | Death |
| PIPNY_OBEL | Opt. Basic Econ. Loss | No | Opt. Basic Econ. Loss |
| CAPIP_NY_AGGREGATE | PIP Aggregate  | No |  |
| PIPNY_INCOME | PIP Income | No | PIP Income |
| NYPIP_EXPENSE | PIP EXPENSE | No |  |
| PIPOR_DEDUCT | Deductible | No | Deductible |
| PIPOR_DEDUCTIBLEappliesto | Deductible Applies To | No | Deductible Applies To |
| PIPOR_MED | PIP Medical | No | PIP Medical |
| PIPOR_INCOME | PIP Income | No |  |
| PIPOR_SERVICES | PIP Services | No | PIP Services |
| PIPOR_CHILDCARE | PIP Childcare | No | PIP Childcare |
| PIPOR_FUNERAL | PIP Funeral | No | PIP Funeral |
| PIPPA_MEDICAL | Medical | No | Medical |
| PIPPA_INCOME | Income | No | Income |
| PIPPA_DEATH | Death | No | Death |
| PIPPA_FUNERAL | Funeral | No |  |
| PIPPA_COMBINED | Combined Limit | No |  |
| PIPPA_EXTRAMED | Extraordinary Medical | No |  |
| PIPTX_PIP | PIP Limit | No |  |
| PIPUT_MEDICAL | Medical | No | Medical |
| PIPUT_WORK | Income | No | Income |
| PIPUT_FUNERAL | Funeral | No |  |
| PIPUT_SURVIVOR | Survivor | No |  |
| PIPWA_MED | PIP Medical | No | PIP Medical |
| PIPWA_INCOME | PIP Income | No |  |
| PIPWA_SERVICES | PIP Services | No | PIP Services |
| PIPWA_FUNERAL | PIP Funeral | No |  |
| BAPIP_AR_Med | Medical | No | Medical |
| BAPIP_AR_WorkLoss | Income | No | Income |
| PIP_AR_Death | Death | No | Death |
| BAPIP_DC_Medical | Medical | No | Medical |
| BAPIP_DC_Funeral | Funeral | No | Funeral |
| BAPIP_DC_WorkLoss | Income | No | Income |
| pc_custom_blanket | Blanket Coverage | No | Blanket Coverage |
| pc_custom_occurLimit | Occurrence Limit | No | Occurrence Limit |
| pc_custom_coinsurance | Coinsurance | No | Coinsurance |

---

### Typelist: CreatedVia

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\CreatedVia.tti`
**Description:** type of automation or user created the implementing object
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| manual | User Entry | No | Created by user |
| bizrule | Business Rule | No | Created by Business Rule framework |
| ui_automatic | Automatic | No | Created by code automatically in UI |
| ruleset | Rule Set | No | Created by gosu rule set |
| web_service | Web Service | No | Created by web service call |
| system | System generated | No | Generated by Guidewire ClaimCenter system |

---

### Typelist: CriterionOperator

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\CriterionOperator.tti`
**Description:** List of available operators for criterion
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| gt | Greater Than Operator | No | Greater Than |
| gte | Greater Than or Equality Operator | No | Greater Than Or Equal To |
| lt | Less Than Operator | No | Less Than |
| lte | Less Than or Equality Operator | No | Less Than or Equal To |
| eq | Equality Operator | No | Equal To |
| neq | InEquality Operator | No | Not Equal To |
| inlist | In List Operator | No | Is One Of |
| between | Range Operator | No | Is Between |
| nil | Null or Empty Operator | No | Has No Value |

---

### Typelist: Currency

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\Currency.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\Currency.example.ttx`
**Description:** Types of Currencies.
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

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

### Typelist: CustomConditionParamType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\CustomConditionParamType.tti`
**Description:** The parameter of custom conditions
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Claim | Claim | No | Parameter type for Claim |
| Exposure | Exposure | No | Parameter type for Exposure |
| Activity | Activity | No | Parameter type for Activity |
| TransactionSet | TransactionSet | No | Parameter type for TransactionSet |

---

### Typelist: CustomConditionReturnType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\CustomConditionReturnType.tti`
**Description:** Return type of custom conditions
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| boolean | boolean | No | Return type for boolean |
| int | int | No | Return type for int |
| String | String | No | Return type for String |

---

### Typelist: CustomConditionType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\CustomConditionType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\CustomConditionType.ttx`
**Description:** Custom conditions
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| *(None defined)* | *Dynamic or database-driven* | No | Typelist populated dynamically at runtime or via database table |

---

### Typelist: CustomerServiceTier

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\CustomerServiceTier.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\CustomerServiceTier.ttx`
**Description:** Represents the customer service tier
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| silver | Silver Customer | No | The service tier for Silver customers |
| gold | Gold Customer | No | The service tier for Gold customers |
| platinum | Platinum Customer | No | The service tier for Platinum customers |

---

### Typelist: CustomHistoryType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\CustomHistoryType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\CustomHistoryType.ttx`
**Description:** Custom history event types, used to support once-only execution of rules
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| a_n_f_r | Auto: No fault rating | No | Claim exception: Fault rating not set on auto claim |
| e_w_n_r | Exposure with no reserves | No | Claim exception: No reserve set for exposure |
| Export | Exported to mainframe | No | Integration: New claim exported to mainframe |
| DataChange | Data change | No | Data change |
| create_recovery_bill | Create recovery bill | No | Create recovery bill |
| catastrophe | Guidewire catastrophe rules | No | Change to catastrophe values |
| email | Email sent | No | Email sent |
| warning | Warning | No | Warning |

---

### Typelist: DashboardStatType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\DashboardStatType.tti`
**Description:** The type of object to which the dashboard statistic applies
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| group | Group | No | Statistic for a group |
| lob | LOB | No | Statistic for a line of business |
| losstype | LossType | No | Statistic for a loss type |
| coveragetype | CoverageType | No | Statistic for a coveragetype |

---

### Typelist: DataChangeStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\DataChangeStatus.tti`
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

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\DataDistributionType.tti`
**Description:** Type of data distributions
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| app_specific | App specific | No | Data distribution provided by the application |
| assignable | Assignable_by_date | No | Distribution of assignable by date |
| adhoc | Ad hoc | No | Ad hoc distribution supplied as input |

---

### Typelist: DataGenActionType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\DataGenActionType.tti`
**Description:** Action type performed by data-gen
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| restore | Restore | No | Restore DB from pcb. |
| advanceDate | AdvanceDate | No | Advancing all dates field in DB. |
| initialize | Initialize | No | Initialize DB. |

---

### Typelist: DataGenStatusType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\DataGenStatusType.tti`
**Description:** Data-gen action status.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| succeed | Succeed | No | Action succeeded. |
| failed | Failed | No | Action failed. |
| inProgress | InProgress | No | Action in progress. |

---

### Typelist: DateBinDataType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\DateBinDataType.tti`
**Description:** The type of data to be stored in a date binned distribution,   determining which column of a DateBinnedDDValue to display
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Typekey | Typekey | No | A GW Typekey column |
| Boolean | Boolean | No | A Boolean column |

---

### Typelist: DateFieldsToSearchType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\DateFieldsToSearchType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\DateFieldsToSearchType.ttx`
**Description:** The search options for the date searches in search
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| loss | Loss date | No | Find by Loss Date |
| reported | Reported date | No | Find by reported date |
| closed | Closed date | No | Find by closed date |
| target | Due date | No | Find by target date |
| create | Creation date | No | Find by creation date |
| approved | Approved date | No | Find by approved date |
| issue | Issue date | No | Find by issue date |
| service | Date of service | No | Find by service date |
| periodstart | Service period start | No | Find by service period start |
| periodend | Service period end | No | Find by service period end |
| schedsend | Scheduled send date | No | The date the check is supposed to go out |

---

### Typelist: DateRangeChoiceType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\DateRangeChoiceType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\DateRangeChoiceType.ttx`
**Description:** The predetermined list of date ranges we can search for
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| n0 | Today | No | Today |
| n7 | Last 7 days | No | 7 days before today |
| n14 | Last 14 days | No | 14 days before today |
| n30 | Last 30 days | No | 30 days before today |
| n90 | Last 90 days | No | 90 days before today |
| n180 | Last 180 days | No | 180 days before today |
| n365 | Last 365 days | No | 365 days before today |
| 7 | Next 7 days | No | 7 days from today |
| 30 | Next 30 days | No | 30 days from today |
| 90 | Next 90 days | No | 90 days from today |
| 180 | Next 180 days | No | 180 days from today |
| 365 | Next 365 days | No | 365 days from today |

---

### Typelist: DateSearchType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\DateSearchType.tti`
**Description:** What kind of date search we are doing
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| fromlist | List | No | Selected from a list |
| enteredrange | Enter Dates | No | An entered range |

---

### Typelist: DaysInWeekType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\DaysInWeekType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\DaysInWeekType.ttx`
**Description:** Days in week used for benefit calculation
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| five | Five | No | Five |
| seven | Seven | No | Seven |

---

### Typelist: DBUpdateStatsRunnerType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\DBUpdateStatsRunnerType.tti`
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

### Typelist: DeductibleStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\DeductibleStatus.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\DeductibleStatus.ttx`
**Description:** Indicates whether the deductible has been paid
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| paid | Paid | No | Paid |
| unpaid | Unpaid | No | Unpaid |

---

### Typelist: DeductionType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\DeductionType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\DeductionType.ttx`
**Description:** Types of deductions listed on a check
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| irs | Backup withholding | No | Backup withholding for the IRS |
| lawyer | Lawyer | No | Lawyer |
| child_support | Child support | No | Child support |
| dependent | Dependent | No | Dependent |
| other_lien | Other lien | No | Other lien |
| retirement_plan | Retirement plan | No | Retirement plan |
| health_insurer | Health benefits insurer | No | Health benefits insurer |
| union_dues | Union dues | No | Union dues |

---

### Typelist: DeliveryMethod

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\DeliveryMethod.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\DeliveryMethod.ttx`
**Description:** Delivery method for a check
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| send | Send | No | Send |
| hold | Hold for adjuster | No | Hold for adjuster |
| no_check_needed | No check needed | No | No check needed |

---

### Typelist: DestructionRequestStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\DestructionRequestStatus.tti`
**Description:** Status in the Contact Purge Process
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| DoesNotExist | Does Not Exist | No | Request for destruction does not exist |
| Unprocessed | Unprocessed | No | New Request that has not been processed yet |
| InProgress | In Progress | No | The destruction request is in progress |
| Finished | Finished | No | Request has been processed and the contact should have been destroyed if possible. |

---

### Typelist: DetailedBodyPartDesc

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\DetailedBodyPartDesc.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\DetailedBodyPartDesc.ttx`
**Description:** DetailedBodyPartDesc
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 13A | Total deafness of both ears | No | Total deafness of both ears |
| 13B | Total deafness of one ear | No | Total deafness of one ear |
| 13C | Prior hearing loss one ear - loss in remaining ear | No | Where worker prior to injury has suffered a total loss of hearing in one ear, and as a result of the accident loses total hearing in remaining ear |
| 14A | Eye loss - enucleation | No | The loss of eye by enucleation (including disfigurement resulting there from) |
| 14B | Total blindness of one eye | No | Total blindness of one eye |
| 14C | Blindness in both eyes | No | Blindness in both eyes |
| 36A | Loss of an index finger metacarpal bone | No | The loss of an index finger and metacarpal bone thereof |
| 36B | Loss of an index finger at proximal joint | No | The loss of an index finger at the proximal joint |
| 36C | Loss of an index finger at second joint | No | The loss of an index finger at the second joint |
| 36D | Loss of an index finger at distal joint | No | The loss of an index finger at the distal joint |
| 36E | Loss of a second finger and metacarpal bone | No | The loss of a second finger and the metacarpal bone thereof |
| 36F | Loss of middle finger at proximal joint | No | The loss of a middle finger at the proximal joint |
| 36G | Loss of middle finger at second joint | No | The loss of a middle finger at the second joint |
| 36H | Loss of middle finger at distal joint | No | The loss of a middle finger at the distal joint |
| 36I | Loss of a third or ring finger and metacarpal | No | The loss of a third or ring finger and the metacarpal thereof |
| 36J | Loss of ring finger at proximal joint | No | The loss of a ring finger at the proximal joint |
| 36K | Loss of a ring finger at second joint | No | The loss of a ring finger at the second joint |
| 36L | Loss of a ring finger at distal joint | No | The loss of a ring finger at the distal joint |
| 36M | Loss of a little finger and the metacarpal bone | No | The loss of a little finger and the metacarpal bone thereof |
| 36N | Loss of a little finger at proximal joint | No | The loss of a little finger at the proximal joint |
| 36O | Loss of a little finger at second joint | No | The loss of a little finger at the second joint |
| 36P | Loss of a little finger at distal joint | No | The loss of a little finger at the distal joint |
| 37A | Loss of a thumb and metacarpal bone | No | The loss of a thumb and metacarpal bone thereof |
| 37B | Loss of a thumb at proximal joint | No | The loss of a thumb at the proximal joint |
| 37C | Loss of a thumb at second or distal joint | No | The loss of a thumb at the second or distal joint |
| 57A | Little toe metatarsal bone | No | Little toe metatarsal bone |
| 57B | Little toe - distal joint | No | Little toe at distal joint |
| 57C | Loss of any other toe with the metatarsal bone | No | The loss of any other toe with the metatarsal bone thereof |
| 57D | Loss of any other toe at proximal joint | No | The loss of any other toe at the proximal joint |
| 57E | Other toe at middle joint | No | Other toe at middle joint |
| 57F | Loss of any other toe at second or distal joint | No | The loss of any other toe at the second or distal joint |
| 57G | Other toe at distal joint | No | Other toe at distal joint |
| 58A | Loss of a great toe with metatarsal bone | No | The loss of a great toe with the metatarsal bone thereof |
| 58B | Loss of great toe at proximal joint | No | The loss of a great toe at the proximal joint |
| 58C | Loss of a great toe at second or distal joint | No | The loss of a great toe at the second or distal joint |

---

### Typelist: DetailedBodyPartType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\DetailedBodyPartType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\DetailedBodyPartType.ttx`
**Description:** The detailed body parts that correspond to (and are filtered by) BodyPartType
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 10 | Multiple head injuries | No | Multiple head injuries - Any combination of head injuries |
| 11 | Skull | No | Skull |
| 12 | Brain | No | Brain |
| 13 | Ear(s) | No | Ear(s) - includes: hearing, inside eardrum |
| 14 | Eye(s) | No | Eye(s) - includes: optic nerves, vision, eye lids |
| 15 | Nose | No | Nose - includes: nasal passage, sinus, sense of smell |
| 16 | Teeth | No | Teeth |
| 17 | Mouth | No | Mouth - includes: lips, tongue, throat, taste |
| 18 | Soft tissue (head) | No | Soft tissue (head) |
| 19 | Facial bones | No | Facial bones - includes: jaw |
| 20 | Multiple neck injuries | No | Multiple neck injuries - any combination of neck injuries |
| 21 | Vertebrae | No | Vertebrae - includes: spinal column bone, cervical segment |
| 22 | Disc (neck) | No | Disc (neck) - includes: spinal column cartilage, cervical segment |
| 23 | Spinal cord (neck) | No | Spinal cord (neck) - includes: nerve tissue, cervical segment |
| 24 | Larynx | No | Larynx - includes: cartilage, vocal cords |
| 25 | Soft tissue (neck) | No | Soft tissue (neck) - Other than larynx or trachea |
| 26 | Trachea | No | Trachea |
| 30 | Multiple upper extremities | No | Multiple upper extremities - any combination of arm and hand injuries |
| 31 | Upper arm | No | Upper arm - humerus and corresponding muscles, excluding clavicle and scapula |
| 32 | Elbow | No | Elbow - radial head |
| 33 | Lower arm | No | Lower arm - forearm: radius, ulna, and corresponding muscle |
| 34 | Wrist | No | Wrist - carpals and corresponding muscles |
| 35 | Hand | No | Hand - metacarpals and corresponding muscles, excluding wrists and fingers |
| 36 | Finger(s) | No | Finger(s) - other than thumb and corresponding muscles |
| 37 | Thumb | No | Thumb |
| 38 | Shoulder(s) | No | Shoulder(s) - armpit, rotator cuff, trapezius, clavicle, scapula |
| 39 | Wrist(s) and Hand(s) | No | Wrist(s) and hand(s) |
| 40 | Multiple trunk injuries | No | Multiple trunk injuries - any combination of trunk injuries |
| 41 | Upper back area | No | Upper back area - (thoracic area) upper back muscles, excluding vertebrae, disc, spinal cord |
| 42 | Lower back area | No | Lower back area - (lumbar area) lower back muscles, excluding sacrum, coccyx, pelvis, vertebrae, disc, spinal cord |
| 43 | Disc (back) | No | Disc (back) - spinal column cartilage other than cervical segment |
| 44 | Chest | No | Chest - including: ribs, sternum, soft tissue |
| 45 | Sacrum and coccyx | No | Sacrum and coccyx - first nine vertebrae |
| 46 | Pelvis | No | Pelvis |
| 47 | Spinal cord (back) | No | Spinal cord (back) - nerve tissue other than cervical segment |
| 48 | Internal organs | No | Internal organs - other than heart and lungs |
| 49 | Heart | No | Heart |
| 50 | Multiple lower appendages | No | Multiple lower appendages - any combination of leg and foot injuries |
| 51 | Hip | No | Hip |
| 52 | Upper leg | No | Upper leg - femur and corresponding muscles |
| 53 | Knee | No | Knee - Patella |
| 54 | Lower leg | No | Lower leg - tibia, fibula and corresponding muscles |
| 55 | Ankle | No | Ankle - tarsals |
| 56 | Foot | No | Foot - metatarsals, heel, Achilles tendon and corresponding muscles, excluding ankle or toes |
| 57 | Toes | No | Toes |
| 58 | Great toe | No | Great toe |
| 60 | Lungs | No | Lungs |
| 61 | Abdomen including groin | No | Abdomen including groin - excluding injury to internal organs |
| 62 | Buttocks | No | Buttocks - soft tissue |
| 63 | Lumbar or sacral vertebrae | No | Lumbar or sacral vertebrae - bone portion of the spinal column |
| 64 | Artificial appliance | No | Artificial appliance - braces, etc. |
| 65 | Unclassified - insufficient info to properly identify | No | Unclassified - insufficient info to properly identify |
| 66 | No physical injury | No | No physical injury - mental disorder |
| 67 | Ribs | No | Ribs |
| 68 | Stomach | No | Stomach |
| 90 | Multiple body parts | No | Multiple body parts - applies when more than one major body part has been affect (such as an arm and a leg) |
| 91 | Body systems (with no external injury) | No | Body systems (with no external injury) - applies to the functioning of an entire body system without external injury (e.g. poisoning, inflammation) |
| 99 | Whole Body | No | A code referencing the anatomic classification of the injury |

---

### Typelist: DetailedInjuryType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\DetailedInjuryType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\DetailedInjuryType.ttx`
**Description:** More detail on the primary injury
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 01 | No Physical Injury | No | No Physical Injury - Glasses, contacts, artificial appliance |
| 02 | Amputation | No | Amputation |
| 03 | Angina pectoris | No | Angina pectoris (chest pain) |
| 04 | Burn | No | Burn - heat (burn or scald) or chemical (corrosive damage) |
| 07 | Concussion | No | Concussion - brain, cerebral |
| 10 | Contusion | No | Contusion - bruise with intact skin surface, hematoma |
| 13 | Crushing | No | Crushing |
| 16 | Dislocation | No | Dislocation - pinched nerve, slipped or ruptured disc, herniated disc, complete tear, MD dislocation |
| 19 | Electric shock | No | Electric shock |
| 22 | Enucleation | No | Enucleation - removal of organ or tumor |
| 25 | Foreign body | No | Foreign body |
| 28 | Fracture | No | Fracture - breaking of a bone or a cartilage |
| 30 | Freezing | No | Freezing - frostbite |
| 31 | Hearing loss or impairment | No | Hearing loss or impairment |
| 32 | Heat prostration | No | Heat prostration - heat stroke, sun stroke, excluding sun burn |
| 34 | Hernia | No | Hernia - abnormal protrusion of an organ through its containing wall |
| 36 | Infection | No | Infection |
| 37 | Inflammation | No | Inflammation |
| 40 | Laceration | No | Laceration - cuts, scratches, abrasions, superficial wounds |
| 41 | Myocardial infarction | No | Myocardial infarction - heart attack, heart conditions, hypertension |
| 42 | Poisoning (not overdose or cumulative injury) | No | Poisoning (not overdose or cumulative injury) |
| 43 | Puncture | No | Puncture |
| 46 | Rupture | No | Rupture |
| 47 | Severance | No | Severance |
| 49 | Sprain | No | Sprain |
| 52 | Strain | No | Strain |
| 53 | Syncope | No | Syncope - fainting, passing out |
| 54 | Asphyxiation | No | Asphyxiation - strangulation, drowning |
| 55 | Vascular | No | Vascular - strokes, varicose veins, other circulatory injuries |
| 58 | Vision Loss | No | Vision Loss |
| 59 | Other specific injury | No | Other specific injury |
| 60 | Dust disease | No | Dust disease - all other lung disease |
| 61 | Asbestosis | No | Asbestosis - lung disease from asbestos |
| 62 | Black lung | No | Black lung - lung disease from coal mining |
| 63 | Byssinosis | No | Byssinosis - lung disease from cotton, flax, hemp |
| 64 | Silicosis | No | Silicosis - lung disease from inhalation of silica (quartz) dust |
| 65 | Respiratory disorders (gases, fumes, chemicals) | No | Respiratory disorders (gases, fumes, chemicals) |
| 66 | Poisoning (chemical) | No | Poisoning (chemical) |
| 67 | Poisoning (metal) | No | Poisoning (metal) |
| 68 | Dermatitis | No | Dermatitis - from repeated contact with irritants |
| 69 | Mental disorder | No | Mental disorder |
| 70 | Radiation | No | Radiation |
| 71 | All other occupational disease injuries | No | All other occupational disease injuries |
| 72 | Loss of hearing | No | Loss of hearing |
| 73 | Contagious disease | No | Contagious disease |
| 74 | Cancer | No | Cancer |
| 75 | AIDS | No | AIDS |
| 76 | Video display terminal diseases | No | Video display terminal diseases - excluding carpal tunnel syndrome |
| 77 | Mental stress | No | Mental stress |
| 78 | Carpal Tunnel Syndrome | No | Carpal Tunnel Syndrome |
| 79 | Hepatitis C | No | Hepatitis C |
| 80 | All other cumulative injuries | No | All other cumulative injuries |
| 90 | Multiple physical injuries only | No | Multiple physical injuries only |
| 91 | Multiple injuries including both physical and psychological | No | Multiple injuries including both physical and psychological |

---

### Typelist: DisabledDueToAccident

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\DisabledDueToAccident.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\DisabledDueToAccident.ttx`
**Description:** For non-WC, to characterize the disability
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| partdisabled | Partially Disabled | No | Partially Disabled |
| totaldisabled | Totally Disabled | No | Totally Disabled |
| notdisabled | Not Disabled | No | Not Disabled |

---

### Typelist: DocumentSection

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\DocumentSection.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\DocumentSection.ttx`
**Description:** Section for the document
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| bills | Bills | No | Bills |
| medical | Medical | No | Medical |
| indemnity | Indemnity | No | Indemnity |
| rehab | Rehab | No | Rehab |
| legal | Legal | No | Legal |
| correspondence | Correspondence | No | Correspondence |
| misc | Misc | No | Misc |
| subrogation | Subrogation | No | Subrogation |

---

### Typelist: DocumentSecurityType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\DocumentSecurityType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\DocumentSecurityType.ttx`
**Description:** Type of the document for access-restriction purposes
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| unrestricted | Unrestricted document | No | Document that does not require access restriction |
| sensitive | Sensitive document | No | Document that is sensitive in nature |

---

### Typelist: DocumentStatusType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\DocumentStatusType.tti`
**Description:** Status of the document
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| draft | Draft | No | Draft |
| approving | Approving | No | Approving |
| approved | Approved | No | Approved |
| final | Final | No | Final |
| filed | Filed | Yes | Filed |

---

### Typelist: DocumentType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\DocumentType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\DocumentType.ttx`
**Description:** Type of document
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| diagram | Diagram | No | Diagram |
| email | Email | No | Email |
| policereport | Police report | No | Police report |
| repairestimate | Repair estimate | No | Repair estimate |
| fnol | First notice of loss | No | First notice of loss (original report) |
| statement | Statement | No | Statement |
| letter_received | Letter received | No | Letter received |
| letter_sent | Letter sent | No | Letter sent |
| email_sent | Email Sent | No | Email Sent by CreateEmail |
| sla | Service Level Agreement | No | Service Level Agreement |
| w9 | W-9 | No | W-9 |
| other | Other | No | Other |

---

### Typelist: DynamicActionCategory

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\DynamicActionCategory.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\DynamicActionCategory.ttx`
**Description:** The category of the DynamicAction
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| General | GeneralRules | No | General business rules |

---

### Typelist: EffDatedChangeType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\EffDatedChangeType.tti`
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

### Typelist: EmploymentStatusType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\EmploymentStatusType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\EmploymentStatusType.ttx`
**Description:** Status of employment
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| fulltime | Full-time employee | No | Full-time employee |
| parttime | Part-time employee | No | Part-time employee |
| unemployed | Unemployed | No | Unemployed |
| onstrike | On strike | No | On strike |
| disabled | Disabled | No | Disabled |
| retired | Retired | No | Retired |
| other | Other | No | Other |
| seasonal | Seasonal | No | Seasonal |
| volunteer | Volunteer | No | Volunteer |
| ft_apprentice | Full-time apprentice | No | Full-time apprentice |
| pt_apprentice | Part-time apprentice | No | Part-time apprentice |
| pieceworker | Pieceworker | No | Pieceworker |
| temporary | Temporary | No | Temporary |
| student | Student | No | Student |
| minor | Minor child | No | Minor child |

---

### Typelist: EntitySourceType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\EntitySourceType.tti`
**Description:** Identifies whether entity search/fetch operations should be performed against the internal system or some remote system
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| internal | Internal | No | Search/fetch should be performed internally against the local database |
| external | External | No | Search/fetch should be performed against some remote system via a plugin |

---

### Typelist: ErrorCategory

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ErrorCategory.tti`
**Description:** The type of error for messages that are in error
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| *(None defined)* | *Dynamic or database-driven* | No | Typelist populated dynamically at runtime or via database table |

---

### Typelist: ETLStrings

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ETLStrings.tti`
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

### Typelist: ExposureClosedOutcomeType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ExposureClosedOutcomeType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ExposureClosedOutcomeType.ttx`
**Description:** The possible outcomes of an exposure when it is closed
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| completed | Completed | No | Completed |
| duplicate | Duplicate | No | Duplicate |
| paymentscomplete | Payments complete | No | Payments complete |
| mistake | Mistake | No | Mistake |
| fraud | Fraud | No | Fraud |
| unnecessary | Unnecessary | No | Unnecessary |

---

### Typelist: ExposureProgressType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ExposureProgressType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ExposureProgressType.ttx`
**Description:** Description of the progress on an open exposure
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| new | New | No | New |
| investigation | Investigation | No | Investigation |
| evaluation | Evaluation | No | Evaluation |
| settlement | Settlement | No | Settlement |
| litigation | Litigation | No | Litigation |
| pendingrecovery | Pending recovery | No | Pending recovery |

---

### Typelist: ExposureReopenedReason

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ExposureReopenedReason.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ExposureReopenedReason.ttx`
**Description:** The possible reasons for an exposure to be reopened
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| paymentdenied | Payment Denied | No | Final Payment causing this exposure to close has been denied |
| mistake | Mistake | No | Mistake |
| newinfo | New information | No | New information |

---

### Typelist: ExposureSecurityType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ExposureSecurityType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ExposureSecurityType.ttx`
**Description:** Exposure security types
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| *(None defined)* | *Dynamic or database-driven* | No | Typelist populated dynamically at runtime or via database table |

---

### Typelist: ExposureState

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ExposureState.tti`
**Description:** Standard states for a exposure, such as open or closed
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| draft | Draft | No | Draft |
| open | Open | No | Open |
| closed | Closed | No | Closed |
| exception | Exception | No | None of the above |

---

### Typelist: ExposureTextType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ExposureTextType.tti`
**Description:** Text fields on exposure, stored in ExposureText array
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| TreatmentRendered | TreatmentRendered | No | Treatment rendered |
| SubjectiveComplaints | SubjectiveComplaints | No | Patient's subjective complaints |
| ObjectiveFindings | ObjectiveFindings | No | Treatment provider's findings |
| ISOErrorMessage | ISOErrorMessage | No | Error message if most recent ISO ClaimSearch request failed |

---

### Typelist: ExposureTier

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ExposureTier.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ExposureTier.ttx`
**Description:** ExposureTier
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| medical | Medical | No | Medical Exposure |
| indemnity | Indemnity | No | Indemnity |
| el | Employer's Liability | No | Employer's Liability |
| 1p_pd_low | 1st Party Physical Damage - Low Complexity | No | 1st Party Physical Damage - Low Complexity |
| 1p_pd_high | 1st Party Physical Damage - High Complexity | No | 1st Party Physical Damage - High Complexity |
| 1p_med_low | 1st Party Medical - Low Complexity | No | 1st Party Medical - Low Complexity |
| 1p_med_high | 1st Party Medical - High Complexity | No | 1st Party Medical - High Complexity |
| lossofuse | Loss of Use | No | Loss of Use |
| rental | Rental | No | Rental |
| towing | Towing | No | Towing |
| 1p_sd_low | 1st Party Structural Damage - Low Complexity | No | 1st Party Structural Damage - Low Complexity |
| 1p_sd_high | 1st Party Structural Damage - High Complexity | No | 1st Party Structural Damage - High Complexity |
| 1p_content_low | 1st Party Contents - Low Complexity | No | 1st Party Contents - Low Complexity |
| 1p_content_high | 1st Party Contents - High Complexity | No | 1st Party Contents - High Complexity |
| low | Low Complexity | No | Low Complexity |
| medium | Medium Complexity | No | Medium Complexity |
| high | High Complexity | No | High Complexity |
| 3p_med_low | 3rd Party Medical - Low Complexity | No | 3rd Party Medical - Low Complexity |
| 3p_med_high | 3rd Party Medical - High Complexity | No | 3rd Party Medical - High Complexity |
| 3p_pd_low | 3rd Party Physical Damage - Low Complexity | No | 3rd Party Physical Damage - Low Complexity |
| 3p_pd_high | 3rd Party Physical Damage - High Complexity | No | 3rd Party Physical Damagel - High Complexity |

---

### Typelist: ExposureType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ExposureType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ExposureType.ttx`
**Description:** The different types of available exposure screens, filtered by coverage type and coverage subtype
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| BodilyInjuryDamage | Bodily Injury | No | Bodily Injury |
| LostWages | Indemnity | No | Indemnity |
| WCInjuryDamage | Medical Details | No | Medical Details |
| PIPDamages | PIP | No | PIP |
| LossOfUseDamage | Loss of Use | No | Loss Of Use |
| PersonalPropertyDamage | Personal Property | No | Personal Property |
| PropertyDamage | Property | No | Property |
| VehicleDamage | Vehicle | No | Vehicle |
| EmployerLiability | Employer Liability | No | Employer Liability |
| GeneralDamage | General | No | General |
| MedPay | Med Pay | No | Med Pay |
| TowOnly | Towing and Labor | No | Towing and Labor |
| Theft | Theft | Yes | Theft |
| Baggage | Baggage | No | Baggage |
| TripCancellationDelay | Trip Cancellation or Delay | No | Trip cancellation or delay |
| Content | Content | No | Content |
| OtherStructure | Other Structure | No | Other Structure |
| LivingExpenses | Living Expenses | No | Living Expenses |
| Dwelling | Dwelling | No | Dwelling |

---

### Typelist: ExternalToolType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ExternalToolType.tti`
**Description:** The different external tools available
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| word | Microsoft Word | No | Microsoft Word |
| adobe | Adobe Acrobat | No | Adobe Acrobat |
| ie | Microsoft Internet Explorer | No | Microsoft Internet Explorer |

---

### Typelist: FailoverState

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\FailoverState.tti`
**Description:** FailoverState
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| NotStarted | Not Started | No | Automatic failover not started |
| InProgress | In Progress | No | Automatic failover is in progress |
| Postponed | Postponed | No | Automatic failover is postponed |
| Failed | Failed | No | Automatic failover failed (requires manual intervention) |

---

### Typelist: FaultRating

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\FaultRating.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\FaultRating.ttx`
**Description:** Who is at fault, for example insured, third party
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 2 | Insured not at fault | Yes | Insured not at fault |
| thirdparty | Other party at fault | No | Insured not at fault |
| nofault | No fault | No | No fault - Insured not at fault |
| 0 | Fault unknown | No | Fault unknown |
| 1 | Insured at fault | No | Insured at fault |
| 3 | Physical Damage only | Yes | Physical Damage only |

---

### Typelist: FinancialsCalculationType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\FinancialsCalculationType.tti`
**Description:** Types of pre-defined financials calculations.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| availablereserves | AvailableReserves | No | Financials calculation for available reserves. |
| futurepayments | FuturePayments | No | Financials calculation for future payments. |
| grosstotalincurred | GrossTotalIncurred | No | Financials calculation for gross total incurred. |
| openrecoveryreserves | OpenRecoveryReserves | No | Financials calculation for open recover reserves. |
| openreserves | OpenReserves | No | Financials calculation for open reserves. |
| pendapperodpaymnts | PendingApprovalErodingPayments | No | Financials calculation for pending approval eroding payments. |
| pendappnonerodpaymnts | PendingApprovalNonErodingPayments | No | Financials calculation for pending approval noneroding payments. |
| pendapppayments | PendingApprovalPayments | No | Financials calculation for pending approval payments. |
| pendappreserves | PendingApprovalReserves | No | Financials calculation for pending approval reserves. |
| remainingreserves | RemainingReserves | No | Financials calculation for remaining reserves. |
| totalincurrednet | TotalIncurredNet | No | Financials calculation for total incurred net. |
| totincnetminopnrecres | TotalIncurredNetMinusOpenRecoveryReserves | No | Financials calculation for total incurred net minus open recovery reserves. |
| totalpayments | TotalPayments | No | Financials calculation for total payments. |
| totpaymntwithpending | TotalPaymentsWithPending | No | Financials calculation for total payments with pending. |
| totalrecoveries | TotalRecoveries | No | Financials calculation for total recoveries. |
| totalrecoveryreserves | TotalRecoveryReserves | No | Financials calculation for total recovery reserves. |
| totalreserves | TotalReserves | No | Financials calculation for total reserves. |
| totreswithpending | TotalReservesWithPending | No | Financials calculation for total reserves with pending |

---

### Typelist: FinancialSearchField

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\FinancialSearchField.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\FinancialSearchField.ttx`
**Description:** The search field for financial searches
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| remainingReserve | Remaining Reserve | No | Remaining reserve |
| totalIncurredNet | Net Total Incurred | No | Net total incurred |
| totalPaid | Total Paid | No | Total paid |
| futurePaid | Future Paid | No | Future paid |
| grossCheckAmount | Gross Amount | No | Gross amount |
| Amount | Amount | No | Amount |

---

### Typelist: FinancialThreshold

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\FinancialThreshold.tti`
**Description:** Types of financial thresholds for which special handling can be triggered
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| NetTotalPaid | Net Total Paid | No | Net Total Paid |
| TotalPaid | Total Paid | No | Total Paid |
| NetTotalIncurred | Net Total Incurred | No | Net Total Incurred |

---

### Typelist: FinancialTriggerCause

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\FinancialTriggerCause.tti`
**Description:** Types of events that can trigger a financial threshold event
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| reached | Reached | No | Amount has reached or exceeded threshold |

---

### Typelist: FirstFinalReportedAgency

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\FirstFinalReportedAgency.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\FirstFinalReportedAgency.ttx`
**Description:** Party/Agency that reported Glass claim.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| INSURED | Insured | No | Insured |
| VENDOR | Auto Body Vendor | No | Auto Body Vendor |

---

### Typelist: FlaggedType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\FlaggedType.tti`
**Description:** The type of flagged states a claim can be in
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| isflagged | Is flagged | No | Currently flagged |
| wasflagged | Was flagged | No | Previously flagged |
| neverflagged | Never flagged | No | Never flagged |

---

### Typelist: FreeTextClaimSearchType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\FreeTextClaimSearchType.tti`
**Description:** Type of claim searches available
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| byContactInfoActive | Active Database | No | Claims stored on active database |
| byContactInfoArchive | Archive | No | Claims stored in archive |

---

### Typelist: FreTxtClmSrchNameSrchTyp

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\FreTxtClmSrchNameSrchTyp.tti`
**Description:** The search options for the name searches in claim search
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| insured | Insured | No | Find by insured claim contact role |
| claimant | Claimant | No | Find by claimant claim contact role |
| addinsured | Additional Insured | No | Find by additional insured |
| any | Any Party Involved | No | Find by any claim contact |

---

### Typelist: FullDenialReason

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\FullDenialReason.tti`
**Description:** Full Denial Reason Codes
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 1A | No Compensable Accident - Coming and going | No | No Compensable Accident - Coming and going |
| 1B | No Compensable Accident - Horseplay | No | No Compensable Accident - Horseplay |
| 1C | No Compensable Accident - Willful intent to injure oneself | No | No Compensable Accident - Willful intent to injure oneself |
| 1D | No Compensable Accident - Does not meet statutory definition of accident | No | No Compensable Accident - Does not meet statutory definition of accident |
| 1E | No Compensable Accident - Deviation from employment | No | No Compensable Accident - Deviation from employment |
| 1F | No Compensable Accident - Recreational/social activity | No | No Compensable Accident - Recreational/social activity |
| 1G | No Compensable Accident - Traveling employee | No | No Compensable Accident - Traveling employee |
| 1H | No Compensable Accident - Subsequent intervening accident | No | No Compensable Accident - Subsequent intervening accident |
| 1I | No Compensable Accident - Presumption of compensability, as defined by the jurisdiction, does not apply | No | No Compensable Accident - Presumption of compensability, as defined by the jurisdiction, does not apply |
| 2A | No Causal Relationship - Idiopathic condition | No | No Causal Relationship - Idiopathic condition |
| 2B | No Causal Relationship - Pre-existing condition | No | No Causal Relationship - Pre-existing condition |
| 2C | No Causal Relationship - Stress non-work related | No | No Causal Relationship - Stress non-work related |
| 2D | No Causal Relationship - No medical evidence of injury | No | No Causal Relationship - No medical evidence of injury |
| 2E | No Causal Relationship - No injury per statutory definition | No | No Causal Relationship - No injury per statutory definition |
| 2F | No Causal Relationship - Accident not major contributing cause of injury | No | No Causal Relationship - Accident not major contributing cause of injury |
| 3A | No Coverage - No employer/employee relationship | No | No Coverage - No employer/employee relationship |
| 3B | No Coverage - Independent contractor | No | No Coverage - Independent contractor |
| 3C | No Coverage - Does not meet statutory definition of employee | No | No Coverage - Does not meet statutory definition of employee |
| 3D | No Coverage - No jurisdiction | No | No Coverage - No jurisdiction |
| 3E | No Coverage - No policy in effect on the date of accident | No | No Coverage - No policy in effect on the date of accident |
| 3F | No Coverage - Statute of limitation expired | No | No Coverage - Statute of limitation expired |
| 3G | No Coverage - Statutory exemptions (sole proprietor, corporate officer etc) | No | No Coverage - Statutory exemptions (sole proprietor, corporate officer etc) |
| 3H | No Coverage - Elected other coverage (24 hour, collective bargaining, opted out) | No | No Coverage - Elected other coverage (24 hour, collective bargaining, opted out) |
| 3I | No Coverage - Employee not reported to PEO | No | No Coverage - Employee not reported to PEO |
| 4A | Substance Use/Abuse - Injury primarily occasioned by intoxication or use of any drug | No | Substance Use/Abuse - Injury primarily occasioned by intoxication or use of any drug |
| 4B | Substance Use/Abuse - Violation of drug-free work place policy in effect | No | Substance Use/Abuse - Violation of drug-free work place policy in effect |
| 5A | Other - Failure to report accident timely | No | Other - Failure to report accident timely |
| 5B | Other - Right to reserve | No | Other - Right to reserve |
| 5C | Other - Misrepresentation | No | Other - Misrepresentation |

---

### Typelist: FutureMedicalActionType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\FutureMedicalActionType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\FutureMedicalActionType.ttx`
**Description:** Type of medical action required in the future.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| continuing | Continuing | No | Continuing medical treatment required |
| released | Released | No | Released from care no further treatment |
| referred | Referred | No | Referring to different provider for opinion/treatment |
| investigating | Investigating | No | Ordered tests/x-rays other medical investigations |
| ps_mmi | P&S/MMI | No | Reached P&S/MMI status (Permanent & Stationary / Maximum Medical Improvement) |
| surgery | Surgery | No | Requires surgery |

---

### Typelist: FXRateMarket

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\FXRateMarket.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\FXRateMarket.ttx`
**Description:** Types of foreign exchange rate markets.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| static_table | StaticTable | No | A static table of one-way rates. |

---

### Typelist: GenderType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\GenderType.tti`
**Description:** Gender
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| M | Male | No | Male |
| F | Female | No | Female |

---

### Typelist: GeocodeStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\GeocodeStatus.tti`
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

### Typelist: GeographicalRegion

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\GeographicalRegion.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\GeographicalRegion.ttx`
**Description:** Geographical region classification
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| europe | Europe | No | Europe |
| australia_nz | Australia/NZ | No | Australia/New Zealand |
| worldwide_ex_us_ca | Worldwide ex. USA/Canada | No | Worldwide except USA & Canada |
| worldwide | Worldwide | No | Worldwide |

---

### Typelist: GroupType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\GroupType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\GroupType.ttx`
**Description:** Types of groups
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| root | Root Group | No | This is the root group of an organization |
| autofasttrack | Auto - fast track | No | Fast track auto team |
| autonormal | Auto | No | Auto team |
| autocomplex | Auto - complex | No | Complex auto team |
| propfasttrack | Property - fast track | No | Fast track property team |
| propnormal | Property | No | Property team |
| propcomplex | Property - complex | No | Complex property team |
| lbltyfasttrack | Liability - fast track | No | Fast track liability team |
| lbltynormal | Liability | No | Liability team |
| lbltycomplex | Liability - complex | No | Complex liability team |
| lbltyspecs | Liability specialists | No | Specialists for highly complex liability claims |
| wc_med_only | Workers' comp - med only | No | Workers' comp med only team |
| wc_lost_time | Workers' comp - indemnity | No | Workers' comp indemnity team |
| wc_normal | Workers' comp | No | Workers' comp team |
| general | General | No | General |
| regional | Regional service center | No | Regional service center |
| local | Local office | No | Local office |
| auto_inspectors | Auto damage appraisers | No | Auto damage appraisers |
| attorneys | Defense attorneys | No | Defense attorneys |
| cleanup | Clean-up services | No | Clean-up services |
| clerical | Clerical support | No | Clerical support |
| drive_in | Drive-in centers | No | Drive-in centers |
| hq | Corporate headquarters | No | Corporate headquarters |
| independent | Independent adjusters | No | Independent adjusters |
| injury_specs | Injury liability specialists | No | Injury liability specialists |
| intake | New claim processing | No | New claim processing |
| litigation | Litigation unit | No | Litigation unit |
| medical_mgmt | Medical management | No | Medical management |
| policy | Policy processing | No | Policy processing |
| preferred | Preferred repair shops | No | Preferred repair shops |
| prop_inspectors | Property damage appraisers | No | Property damage appraisers |
| rehab | Rehab/nursing | No | Rehab/nursing |
| salvage | Salvage unit | No | Salvage unit |
| siu | Special investigation unit | No | Special investigative unit |
| systemadmin | System administrators | No | System administrators |
| underwriting | Underwriting | No | Underwriting |
| police | Police | No | Police |
| travel | Travel | No | Travel |
| reinsurance | Reinsurance Unit | No | Reinsurance Unit |
| theftsimple | Simple Theft | No | Auto - Simple Theft |
| theftcomplex | Complex Theft | No | Auto - Complex Theft |

---

### Typelist: HistoryType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\HistoryType.tti`
**Description:** The type of claim/exposure history
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| custom | Custom | No | A custom history event happened; see CustomType for details |
| policyedited | Policy edited | No | The policy was edited, and thus marked unverified |
| approval | Approval or Rejection | No | A referral was approved/rejected |

---

### Typelist: HolidayTagCode

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\HolidayTagCode.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\HolidayTagCode.ttx`
**Description:** The holiday tag code
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| general | General | No | General |
| FederalHolidays | Federal Holidays | No | Federal Holidays |
| CompanyHolidays | Company Holidays | No | Company Holidays |

---

### Typelist: HOPCoverageForm

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\HOPCoverageForm.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\HOPCoverageForm.ttx`
**Description:** HOP Coverage Form
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| ho2 | HO2 | No | Homeowners (Good) |
| ho3 | HO3 | No | Homeowners (Better) |
| ho5 | HO5 | No | Homeowners (Best) |
| ho8 | HO8 | Yes | Homeowners (Older Homes) |
| ho4 | HO4 | No | Renters |
| ho6 | HO6 | No | Condo |

---

### Typelist: HowReportedType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\HowReportedType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\HowReportedType.ttx`
**Description:** How the claim was reported
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| phone | Phone | No | Phone |
| internet | Internet | No | Internet |
| fax | Fax | No | Fax |
| mail | Mail | No | Mail |
| walkin | Walk-in | No | Walk-in |

---

### Typelist: ICDBodySystem

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ICDBodySystem.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ICDBodySystem.ttx`
**Description:** Represents broad classifications of ICD codes used for categorization
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 1 | Infectious And Parasitic Diseases (001-139) | Yes | Infectious And Parasitic Diseases (001-139) |
| 2 | Neoplasms (140-239) | Yes | Neoplasms (140-239) |
| 3 | Endocrine, Nutritional And Metabolic Diseases, And Immunity Disorders (240-279) | Yes | Endocrine, Nutritional And Metabolic Diseases, And Immunity Disorders (240-279) |
| 4 | Diseases Of The Blood And Blood-Forming Organs (280-289) | Yes | Diseases Of The Blood And Blood-Forming Organs (280-289) |
| 5 | Mental Disorders (290-319) | Yes | Mental Disorders (290-319) |
| 6 | Diseases Of The Nervous System And Sense Organs (320-389) | Yes | Diseases Of The Nervous System And Sense Organs (320-389) |
| 7 | Diseases Of The Circulatory System (390-459) | Yes | Diseases Of The Circulatory System (390-459) |
| 8 | Diseases Of The Respiratory System (460-519) | Yes | Diseases Of The Respiratory System (460-519) |
| 9 | Diseases Of The Digestive System (520-579) | Yes | Diseases Of The Digestive System (520-579) |
| 10 | Diseases Of The Genitourinary System (580-629) | Yes | Diseases Of The Genitourinary System (580-629) |
| 11 | Complications Of Pregnancy, Childbirth, And The Puerperium (630-676) | Yes | Complications Of Pregnancy, Childbirth, And The Puerperium (630-676) |
| 12 | Diseases Of The Skin And Subcutaneous Tissue (680-709) | Yes | Diseases Of The Skin And Subcutaneous Tissue (680-709) |
| 13 | Diseases Of The Musculoskeletal System And Connective Tissue (710-739) | Yes | Diseases Of The Musculoskeletal System And Connective Tissue (710-739) |
| 14 | Congenital Anomalies (740-759) | Yes | Congenital Anomalies (740-759) |
| 15 | Certain Conditions Originating In The Perinatal Period (760-779) | Yes | Certain Conditions Originating In The Perinatal Period (760-779) |
| 16 | Symptoms, Signs, And Ill-Defined Conditions (780-799) | Yes | Symptoms, Signs, And Ill-Defined Conditions (780-799) |
| 17 | Injury And Poisoning (800-999) | Yes | Injury And Poisoning (800-999) |
| 18 | External Causes Of Injury (E800-E999) | Yes | External Causes Of Injury (E800-E999) |
| 19 | Plementary Classification Of Factors Influencing Health Status And Contact With Health Services (V01-V82) | Yes | Plementary Classification Of Factors Influencing Health Status And Contact With Health Services (V01-V82) |
| icd10_1 | Certain infectious and parasitic diseases (ICD10 A00-B99) | No | Certain infectious and parasitic diseases (ICD10 A00-B99) |
| icd10_2 | Neoplasms (ICD10 C00-D49) | No | Neoplasms (ICD10 C00-D49) |
| icd10_3 | Diseases of the blood and blood-forming organs and certain disorders involving the immune mechanism (ICD10 D50-D89) | No | Diseases of the blood and blood-forming organs and certain disorders involving the immune mechanism (ICD10 D50-D89) |
| icd10_4 | Endocrine, nutritional and metabolic diseases (ICD10 E00-E89) | No | Endocrine, nutritional and metabolic diseases (ICD10 E00-E89) |
| icd10_5 | Mental, Behavioral and Neurodevelopmental disorders (ICD10 F01-F99) | No | Mental, Behavioral and Neurodevelopmental disorders (ICD10 F01-F99) |
| icd10_6 | Diseases of the nervous system (ICD10 G00-G99) | No | Diseases of the nervous system (ICD10 G00-G99) |
| icd10_7 | Diseases of the eye and adnexa (ICD10 H00-H59) | No | Diseases of the eye and adnexa (ICD10 H00-H59) |
| icd10_8 | Diseases of the ear and mastoid process (ICD10 H60-H95) | No | Diseases of the ear and mastoid process (ICD10 H60-H95) |
| icd10_9 | Diseases of the circulatory system (ICD10 I00-I99) | No | Diseases of the circulatory system (ICD10 I00-I99) |
| icd10_10 | Diseases of the respiratory system (ICD10 J00-J99) | No | Diseases of the respiratory system (ICD10 J00-J99) |
| icd10_11 | Diseases of the digestive system (ICD10 K00-K95) | No | Diseases of the digestive system (ICD10 K00-K95) |
| icd10_12 | Diseases of the skin and subcutaneous tissue (ICD10 L00-L99) | No | Diseases of the skin and subcutaneous tissue (ICD10 L00-L99) |
| icd10_13 | Diseases of the musculoskeletal system and connective tissue (ICD10 M00-M99) | No | Diseases of the musculoskeletal system and connective tissue (ICD10 M00-M99) |
| icd10_14 | Diseases of the genitourinary system (ICD10 N00-N99) | No | Diseases of the genitourinary system (ICD10 N00-N99) |
| icd10_15 | Pregnancy, childbirth and the puerperium (ICD10 O00-O9A) | No | Pregnancy, childbirth and the puerperium (ICD10 O00-O9A) |
| icd10_16 | Certain conditions originating in the perinatal period (ICD10 P00-P96) | No | Certain conditions originating in the perinatal period (ICD10 P00-P96) |
| icd10_17 | Congenital malformations, deformations and chromosomal abnormalities (ICD10 Q00-Q99) | No | Congenital malformations, deformations and chromosomal abnormalities (ICD10 Q00-Q99) |
| icd10_18 | Symptoms, signs and abnormal clinical and laboratory findings, not elsewhere classified (ICD10 R00-R99) | No | Symptoms, signs and abnormal clinical and laboratory findings, not elsewhere classified (ICD10 R00-R99) |
| icd10_19 | Injury, poisoning and certain other consequences of external causes (ICD10 S00-T88) | No | Injury, poisoning and certain other consequences of external causes (ICD10 S00-T88) |
| icd10_20 | External causes of morbidity (ICD10 V00-Y99) | No | External causes of morbidity (ICD10 V00-Y99) |
| icd10_21 | Factors influencing health status and contact with health services (ICD10 Z00-Z99) | No | Factors influencing health status and contact with health services (ICD10 Z00-Z99) |

---

### Typelist: ILElementType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ILElementType.tti`
**Description:** The type describing how the logging element is handled (e.g. Profiler-based, manual)
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| profilertag | Profiler Tag | No | The logging element handled by Profiler-based solution. |
| manual | Manual | No | The logging element handled by manual logging instruction put somewhere in the code. |
| workqueue | Work Queue | No | The logging element associated with a work queue |
| job | Job | No | The logging element associated with a job |

---

### Typelist: IMEType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\IMEType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\IMEType.ttx`
**Description:** 
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Orthopedic | Orthopedic | No | Orthopedic independent medical examiner report |
| Chiropractic | Chiropractic | No | Chiropractic independent medical examiner report |
| Neurological | Neurological | No | Neurological independent medical examiner report |
| Other | Other | No | Other independent medical examiner report |

---

### Typelist: ImportanceLevel

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ImportanceLevel.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ImportanceLevel.ttx`
**Description:** A relative level of importance assigned to an entity
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| notOnCalendar | Not On Calendar | No | Not Showing on Calendar |
| top | Top | No | Top importance level |
| high | High | No | High importance level |
| medium | Medium | No | Medium importance level |
| low | Low | No | Low importance level |

---

### Typelist: InboundChunkStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\InboundChunkStatus.tti`
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

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\InboundFileStatus.tti`
**Description:** The status of an inbound file.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| loaded | Loaded | No | The file has been successfully loaded. |
| duplicate | Duplicate | No | The file was detected as a duplicate. |
| error | Error | No | An error occurred while loading the file. |

---

### Typelist: InboundRecordStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\InboundRecordStatus.tti`
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

### Typelist: IncludeDaysType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\IncludeDaysType.tti`
**Description:** Which days to include in the day count
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| elapsed | Calendar days | No | The number of calendar days elapsed since the starting point; includes all weekends and holidays |
| businessdays | Business days | No | The number of business days since the starting point; does not include weekends and holidays |

---

### Typelist: InfoSource

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\InfoSource.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\InfoSource.ttx`
**Description:** Medical info source - for use on MedCaseMgr Screen
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| MedCertificate | Medical certificate | No | Medical certificate |
| MedReport | Medical report | No | Medical report |
| HospitalReport | Hospital report | No | Hospital report |
| CallFromEmployer | Call from employer | No | Call from Employer |
| CallFromClaimant | Call from claimant | No | Call from claimant |
| CallFromDoctor | Call from doctor | No | Call from doctor |
| CallFromOccTherapist | Call from occupational therapist | No | Call from occupational Therapist |
| CallFromPhysTherapist | Call from physical therapist | No | Call from physical therapist |
| CallFromCaseWrkr | Call from case worker | No | Call from case worker |
| CallFromGuardian | Call from parent or guardian | No | Call from parent or guardian |
| CallFromHospital | Call from hospital | No | Call from hospital |
| CallFromAttorney | Call from attorney | No | Call from attorney |
| CallToEmployer | Call to employer | No | Call to employer |
| CallToClaimant | Call to claimant | No | Call to claimant |
| CallToDoctor | Call to doctor | No | Call to doctor |
| CallToOccTherapist | Call to occupational therapist | No | Call to occupational therapist |
| CallToPhysTherapist | Call to physical therapist | No | Call to physical therapist |
| CallToCaseWrkr | Call to case worker | No | Call to case worker |
| CallToGuardian | Call to parent or guardian | No | Call to parent or guardian |
| CallToHospital | Call to hospital | No | Call to hospital |
| CallToAttorney | Call to attorney | No | Call to attorney |
| Other | Other | No | Contact with party not listed |

---

### Typelist: InitialTreatment

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\InitialTreatment.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\InitialTreatment.ttx`
**Description:** Initial Treatment Code
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 0 | No medical treatment | No | No medical treatment |
| 1 | Minor on-site remedies by employer medical staff | No | Minor on-site remedies by employer medical staff |
| 2 | Minor clinic/hospital medical remedies and diagnostic testing | No | Minor clinic/hospital medical remedies and diagnostic testing |
| 3 | Emergency evaluation, diagnostic testing, and medical procedures | No | Emergency evaluation, diagnostic testing, and medical procedures |
| 4 | Hospitalization greater than 24 hours | No | Hospitalization greater than 24 hours |
| 5 | Future major medical/Lost time anticipated (i.e. hernia case) | No | Future major medical/Lost time anticipated (i.e. hernia case) |

---

### Typelist: InjuryType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\InjuryType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\InjuryType.ttx`
**Description:** The primary injury
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| multiple | Multiple injuries | No | Multiple injuries |
| occupational | Occupational disease or cumulative injury | No | Occupational disease or cumulative injury |
| specific | Specific injury | No | Specific injury |

---

### Typelist: InstructionCategory

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\InstructionCategory.tti`
**Description:** InstructionCategory
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| newclaim | New Claim | No | Instructions related to new claims |
| denial | Denial | No | Instructions related to claim denials |
| sla | SLA | No | Service Level agreements for this account |
| other | Other | No | Other instructions |
| settlement | Settlement | No | Instructions related to claims settlement |
| litigation | Litigation | No | Instructions related to litigation |
| assignment | Assignment | No | Instructions related to assignment |

---

### Typelist: InstructionType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\InstructionType.tti`
**Description:** InstructionType
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| instructionsforsetup | Instructions for Setup | No | New claim setup instructions |
| other | Other | No | Other new claim instructions |
| authorization | Authorization | No | Authorization |
| internal | Internal | No | Assignment instructions |
| vendors | Vendors | No | Vendors instructions |
| lawfirms | Law Firms | No | Law Firms instructions |
| timefirstpayment | Time for first payment | No | Time for first payment |
| timeclose | Time to close | No | Time to close |

---

### Typelist: InsuranceLine

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\InsuranceLine.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\InsuranceLine.ttx`
**Description:** Insurance line (for statistical purposes)
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| comm_auto_liab | Commercial auto liability | No | Commercial auto liability |
| comm_auto_phys | Commercial auto physical damage | No | Commercial auto physical damage |
| comm_auto_noflt | Commercial auto no-fault | No | Commercial auto no-fault |
| businessowners | Businessowners | No | Businessowners |
| comm_property | Commercial property | No | Commercial property |
| farmowners | Farmowners | No | Farmowners |
| general_liab | General Liability | No | General Liability |
| glass | Glass | No | Glass |
| pers_liab | Personal liability | No | Personal liability |
| pers_auto_liab | Personal auto liability | No | Personal auto liability |
| pers_auto_phys | Personal auto physical damage | No | Personal auto physical damage |
| pers_auto_noflt | Personal auto no-fault | No | Personal auto no-fault |
| inland_marine | Inland marine | No | Inland marine |
| wc | Workers' compensation | No | Workers' compensation |
| hopHomeowners | Homeowners | No | Homeowners |
| mobile_hopHomeowners | Mobile Homeowners | No | Mobile Homeowners |

---

### Typelist: InsuranceSubLine

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\InsuranceSubLine.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\InsuranceSubLine.ttx`
**Description:** Insurance sub-line (for statistical purposes)
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| med_pay | Medical payments | No | Medical payments |
| uninsured | Uninsured motorists | No | Uninsured motorists |
| underinsured | Underinsured motorists | No | Underinsured motorists |
| auto_std | Auto standard | No | Auto standard |
| auto_non_std | Auto non-standard | No | Auto non-standard |
| assigned_risk | Assigned risk | No | Assigned risk |
| pers_auto_liab | Personal auto liability | No | Personal auto liability |
| pers_auto_noflt | Personal auto no-fault | No | Personal auto no-fault |
| pers_auto_phys | Personal auto physical damage | No | Personal auto physical damage |
| bo_simplified | Businessowners - simplified | No | Businessowners - simplified |
| bo_nonsimplified | Businessowners - non simplified | No | Businessowners - non simplified |
| basic_1 | Basic group 1 causes of loss | No | Basic group 1 causes of loss |
| basic_2 | Basic group 2 causes of loss | No | Basic group 2 causes of loss |
| farmowners | Farmowners | No | Farmowners |
| premises | Premises/operations liability | No | Premises/operations liability |
| owners_contracts | Owners and contractors | No | Owners and contractors |
| prof_liability | Professional liability | No | Professional liability |
| gl_other | All other general liability | No | All other general liability |
| glass | Glass | No | Glass |
| pers_liability | Personal liability | No | Personal liability |
| wc_std | Workers' compensation | No | Workers' compensation |
| fela | Federal Employers' Liability Act | No | Federal Employers' Liability Act |
| jones | Jones Act/Maritime | No | Jones Act/Maritime |
| inland_marine | Inland marine | No | Inland marine |
| hopHomeowners | Homeowners | No | Homeowners |
| hopHomeowners_rc | Homeowners with replacement cost | No | Homeowners with replacement cost |
| mobile_hopHomeowners | Mobile homeowners | No | Mobile homeowners |

---

### Typelist: InternalPolicyType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\InternalPolicyType.tti`
**Description:** Internal policy types
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| personal | personal | No | Personal |
| commercial | commercial | No | Commercial |

---

### Typelist: ISOMessageType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ISOMessageType.tti`
**Description:** ISOMessageType
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| claimsearch | Claim Search | No | Message to search for a claim |
| keyfieldupdate | KeyFieldUpdate | No | Message to indicate update of field |

---

### Typelist: ISOStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ISOStatus.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ISOStatus.ttx`
**Description:** Status of exposure with ISO - checked, not of interest
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| None | None | No | Not checked by ISO |
| Sent | Sent | No | Sent to ISO database |
| NotOfInterest | Not of Interest | No | Not of interest to ISO |
| ResendPending | Resend pending | No | Request has been made to resend to ISO |

---

### Typelist: Jurisdiction

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\Jurisdiction.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\Jurisdiction.ttx`
**Description:** The list of jurisdictions regulating insurance and other licensing within this deployment. This is similar to the State typelist, which is used for addresses and locations. Each code in the Jurisdiction typelist has an additional category set that is based on State typelist. In many deployments, the State and Jurisdiction typelists will be equal
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

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

### Typelist: JurisdictionalFormula

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\JurisdictionalFormula.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\JurisdictionalFormula.ttx`
**Description:** Formulas specifying which days to include in calculating the TargetDate of a denial period
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| AfterLossDate | x days after Loss Date | No | x days after Loss Date |
| AfterNoticeDate | y days after Notice Date | No | y days after Notice Date |
| AfterLossAndNotice | Greater of x days after Loss Date or y days after Notice Date | No | Greater of x days after Loss Date or y days after Notice Date |

---

### Typelist: JurisdictionType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\JurisdictionType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\JurisdictionType.ttx`
**Description:** Used to categorize Jurisdications.  Each Jurisdiction can be associated with one or more JurisdictionTypes
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| insurance | Insurance | No | Insurance |
| driving_lic | Driver's license | No | Driver's license |
| vehicle_reg | Vehicle registration | No | Vehicle registration |
| ins_tax | Insurance Tax | No | Insurance Tax |
| cons_tax | Consumption tax | No | Consumption tax such as sales tax or VAT |

---

### Typelist: LanguageType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\LanguageType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\LanguageType.ttx`
**Description:** Users' preferred languages
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| de | Deutsch | No | Deutsch |
| en_US | English (US) | No | English (US) |
| es | EspaÃ±ol | No | EspaÃ±ol |
| fr | FranÃ§ais | No | FranÃ§ais |
| it | Italiano | No | Italiano |
| ja | æ—¥æœ¬èªž | No | æ—¥æœ¬èªž |

---

### Typelist: LargeLossNotificationStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\LargeLossNotificationStatus.tti`
**Description:** The status of large loss notification messages.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| None | None | No | No notification sent |
| InQueue | InQueue | No | Notification message created and waiting to be sent |
| Sent | Sent | No | Notification successfully sent |

---

### Typelist: LargeLossNotificationType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\LargeLossNotificationType.tti`
**Description:** Indicates whether notification should go to Policy System or CC
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| PS | PS | No | Policy System |
| CC | CC | No | ClaimCenter |

---

### Typelist: LeaseTerminationReason

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\LeaseTerminationReason.tti`
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

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\LedgerSide.tti`
**Description:** Defines the accounting classification of an account and the sign of a line item
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| debit | Debit | No | Debit |
| credit | Credit | No | Credit |

---

### Typelist: LegalSpecialty

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\LegalSpecialty.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\LegalSpecialty.ttx`
**Description:** specialty types for attornies
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| personalinjury | Personal injury | No | Personal injury |
| motorvehliability | Motor vehicle liability | No | Motor vehicle liability |
| generalliability | General liability | No | General liability |
| workerscomp | Workers' compensation | No | Workers' compensation |

---

### Typelist: LimitsIndicator

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\LimitsIndicator.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\LimitsIndicator.ttx`
**Description:** Combined single limits indicator
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Yes | Yes | No | Yes |
| No | No | No | No |
| Unknown | Unknown | No | Unknown |

---

### Typelist: LineCategory

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\LineCategory.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\LineCategory.ttx`
**Description:** Categories for transaction line items
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| deductible | Deductible | No | Deductible |
| formerdeductible | Former Deductible | No | Former Deductible |
| other | Other | No | Other |
| doctor | Doctor | No | Doctor's care |
| nurse | Nurse | No | Nursing care |
| hospital | Hospital | No | Hospital |
| drugs | Prescription drugs | No | Prescription drugs |
| chiro | Chiropractor | No | Chiropractor |
| pt | Physical therapy | No | Physical therapy |
| diagnostic | X-ray/diagnostic | No | X-ray/diagnostic |
| mileage | Mileage reimbursement | No | Mileage reimbursement |
| DraftAppeal | Draft Appeal | No | Draft Appeal |
| Discovery | Discovery/Research | No | Discovery/Research |
| Deposition | Deposition | No | Deposition |
| Hearing | Hearing | No | Hearing |
| FileReview | File review | No | File review |
| ReviewCorrespond | Review correspondence | No | Review correspondence |
| CourtCosts | Court costs | No | Court costs |
| Experts | Experts (Private, CPA, Reconstruction) | No | Experts (Private, CPA, Reconstruction) |
| Investigation | Investigation | No | Investigation |
| Meeting | Meeting | No | Meeting |
| PhoneCall | Phone call | No | Phone call |
| inspection | Inspection | No | Inspection |
| parts | Parts | No | Parts |
| labor | Labor | No | Labor |
| towing | Towing | No | Towing |
| reimburseddeductible | Reimbursed Deductible | No | Reimbursed Deductible |

---

### Typelist: LitigationStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\LitigationStatus.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\LitigationStatus.ttx`
**Description:** Status of litigations
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| not_litigated | Not In litigation | No | Not In litigation |
| litigated | In litigation | No | In litigation |
| complete | Litigation complete | No | Litigation complete |
| rep | Claimant represented by lawyer | Yes | Claimant represented by lawyer |
| suit_filed | Suit filed | Yes | Suit filed |
| judge | Venue set, judge selected | Yes | Venue set, judge selected |
| discovery | Discovery complete | Yes | Discovery complete |
| trial_begun | Trial begun | Yes | Trial begun |
| trial_complete | Trial complete | Yes | Trial complete |
| verdict_returned | Verdict returned | Yes | Verdict returned |
| pending_appeal | Pending appeal | Yes | Pending appeal |
| in_appeal | In appeal | Yes | In appeal |
| closed | Closed | Yes | Closed |

---

### Typelist: LoadCommandType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\LoadCommandType.tti`
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

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\LoaderCallbackTimeType.tti`
**Description:** Types of LoaderCallback execution times
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| beforeidgeneration | Before ID generation | No | Before ID generation |
| beforeinsertselects | Before insert/selects into source tables | No | Before insert/selects into source tables |
| afterinsertselects | After insert/selects into source tables | No | After insert/selects into source tables |

---

### Typelist: LoadErrorType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\LoadErrorType.tti`
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

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\LoadFactorType.tti`
**Description:** Type of load factor privileges a user has
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| loadfactorview | View | No | User can view the load factor levels of other users in the group |
| loadfactoradmin | Admin | No | User can view and modify the load factor levels of other users in the group |

---

### Typelist: LoadStepType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\LoadStepType.tti`
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

### Typelist: LOBCode

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\LOBCode.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\LOBCode.ttx`
**Description:** Line of business
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| GLLine | General Liability Line | No | General Liability |
| CPLine | Commercial Property Line | No | Commercial Property |
| PersonalAutoLine | Personal Auto Line | No | Personal Auto |
| IMLine | Inland Marine Line | No | Inland Marine Line |
| WorkersCompLine | Workers' Comp Line | No | Workers' Comp |
| BOPLine | Businessowners Line | No | BusinessOwners |
| HOPLine | Homeowners Line | No | Homeowners Line |
| BusinessAutoLine | Commercial Auto Line | No | Commercial Auto Line |
| PersonalUmbrellaLine_PUE | Personal Umbrella Line | No | Personal Umbrella Line |
| other_liab | Other Liability | No | Other Liability |
| travel | Travel | No | Travel line |

---

### Typelist: LocaleType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\LocaleType.tti`
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

### Typelist: LocationOfTheft

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\LocationOfTheft.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\LocationOfTheft.ttx`
**Description:** To describe the Location where the property was stolen
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| residential | Residential | No | Residential |
| commercial | Commercial | No | Commercial |
| offPremises | Off Premises | No | Off Premises |

---

### Typelist: LookupColumnDataType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\LookupColumnDataType.tti`
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

### Typelist: LossCategory

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\LossCategory.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\LossCategory.ttx`
**Description:** Detailed category of the exposure
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| default | default | No | default |

---

### Typelist: LossCause

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\LossCause.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\LossCause.ttx`
**Description:** Specific loss subtypes
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| animalcollision | Collision with animal | Yes | Collision with animal |
| animal | Animal | No | Animal |
| bikecollision | Collision with bicycle | No | Collision with bicycle |
| fixedobjcoll | Collision with fixed object | No | Collision with fixed object |
| vehcollision | Collision with motor vehicle | No | Collision with motor vehicle |
| otherobjcoll | Collision with other object | No | Collision with other object |
| pedcollision | Collision with pedestrian | No | Collision with pedestrian |
| trainbuscoll | Collision with train or bus | No | Collision with train or bus |
| loadingdamage | Damage in loading or unloading | No | Damage in loading or unloading |
| FallingObject | Falling or moving object | No | Falling or moving object |
| earthquake | Earthquake | No | Earthquake |
| explosion | Explosion | No | Explosion |
| firedamage | Fire damage to vehicle | Yes | Fire damage to vehicle |
| waterdamage | Water damage | No | Water Damage |
| glassbreakage | Glass breakage | No | Glass breakage |
| vandalism | Malicious mischief and vandalism | No | Malicious mischief and vandalism |
| rearend | Rear-end collision | No | Rear-end collision |
| riotandcivil | Riot and civil commotion | No | Riot and civil commotion |
| theftentire | Theft of entire vehicle | No | Theft of entire vehicle |
| theftparts | Theft Audio or other parts | No | Theft Audio or other parts |
| fire | Fire | No | Fire |
| wind | Wind | No | Wind |
| hail | Hail | No | Hail |
| mold | Mold | No | Mold |
| structfailure | Structural failure | No | Structural failure |
| snowice | Snow/ice | No | Snow/ice |
| burglary | Burglary | No | Burglary |
| animal_bite | Animal/insect bite/scratch/sting | No | Animal/insect bite/scratch/sting |
| broken_glass | Broken glass | No | Broken glass |
| electrical_curr | Contact with electric current | No | Contact with electric current |
| air_crash | Crash of airplane | No | Crash of airplane |
| rail_crash | Crash of rail vehicle | No | Crash of rail vehicle |
| water_veh_crash | Crash of water vehicle | No | Crash of water vehicle |
| construction | Faulty construction | No | Faulty construction |
| errors | Errors and omissions | No | Errors and omissions |
| breach | Breach of contract | No | Breach of contract |
| burn_scald | Burn or scald - heat or cold exposures - contact with | No | Burn or scald - heat or cold exposures - contact with |
| caught_in | Caught in, under, or between | No | Caught in, under, or between |
| cut | Cut, puncture, scrape, injured by | No | Cut, puncture, scrape, injured by |
| fall | Fall, slip, or trip injury | No | Fall, slip, or trip injury |
| motorvehicle | Motor vehicle | No | Motor vehicle |
| strain | Strain or injury by | No | Strain or injury by |
| striking | Striking against or stepping on | No | Striking against or stepping on |
| struck | Struck or injured by | No | Struck or injured by |
| rubbed | Rubbed or abraded by | No | Rubbed or abraded by |
| miscellaneous | Miscellaneous causes | No | Miscellaneous causes |
| leftcollision | Collision while turning left | No | Collision while turning left |
| assault | Assault or battery | No | Assault or battery |
| med_error | Medical error | No | Medical error |
| product | Product failure | No | Product failure |
| excess | Excess liability | No | Excess liability |
| rollover | Rollover | No | Rollover |
| personal_misconduct | Personal misconduct | No | Personal Misconduct |
| professional_sports | Professional or organized sports | No | Professional or Organized Sports |
| official_duty | Mandatory official duty (military, jury etc) | No | Mandatory official duty (military, jury etc) |
| death | Death | No | Death |
| preex_med_condition | Pre existing medical condition | No | Pre existing medical condition |
| abandonment | Abandonment | No | Abandonment |
| delay | Delay | No | Delay |
| cancellation | Cancellation | No | Cancellation |
| terrorism_hijack | Terrorism or Hijack | No | Terrorism or Hijack |
| missed_departure | Missed departure | No | Missed departure |
| documents | Documents | No | Loss of documents like passport, tickets, driver's license |
| hurricane | Hurricane | No | Hurricane |

---

### Typelist: LossPartyType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\LossPartyType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\LossPartyType.ttx`
**Description:** Generally either first- or third-party loss
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| insured | Insured's loss | No | Insured's loss |
| third_party | Third-party liability | No | Third-party liability |

---

### Typelist: LossType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\LossType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\LossType.ttx`
**Description:** All available types of claims
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| AUTO | Auto | No | Auto |
| PR | Property | No | Property |
| GL | Liability | No | Liability |
| WC | Workers' Comp | No | Workers' Comp |
| TRAV | Travel | No | General loss during travel |

---

### Typelist: LostPropertyType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\LostPropertyType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\LostPropertyType.ttx`
**Description:** ISO category of lost property, for theft losses
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Art | Art/antique | No | Art/antique |
| AudioVisual | Audio/visual | No | Audio/visual |
| Cash | Cash | No | Cash |
| Clothing | Clothing | No | Clothing |
| ComputerEquip | Computer equipment | No | Computer equipment |
| Furs | Furs | No | Furs |
| Guns | Guns | No | Guns |
| Jewelry | Jewelry | No | Jewelry |
| Silverware | Silverware | No | Silverware |
| SportsEquip | Sports equipment | No | Sports equipment |
| Tools | Tools | No | Tools |
| OfficeEquip | Office equipment | No | Office equipment |
| Other | Other or multiple | No | Other or multiple |
| MoblEquip | Mobile equipment | No | Mobile equipment |
| Engine | Engine | No | Engine |
| Outdrive | Outdrive | No | Outdrive |

---

### Typelist: LostWagesBenefitType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\LostWagesBenefitType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\LostWagesBenefitType.ttx`
**Description:** Types of lost wages benefits
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| ppd | PPD | No | Permanent Partial Disability |
| ptd | PTD | No | Permanent Total Disability |
| tpd | TPD | No | Temporary Partial Disability |
| ttd | TTD | No | Temporary Total Disability |
| death | Death | No | Death benefits |
| voc | Vocational | No | Vocational benefits |

---

### Typelist: MajorPerils

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\MajorPerils.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\MajorPerils.ttx`
**Description:** Major perils (for statistical purposes)
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| bodily_injury | Auto bodily injury | No | Auto bodily injury |
| prop_damage | Property damage | No | Property damage |
| med_pay | Medical payments | No | Medical payments |
| uninsured_bi | Uninsured motorist BI | No | Uninsured motorist BI |
| under_insured_bi | Under-insured motorist BI | No | Under-insured motorist BI |
| pip | Personal injury protection | No | Personal injury protection |
| pers_nofault | Auto no-fault | No | Auto no-fault |
| comprehensive | Comprehensive | No | Comprehensive |
| collision | Collision | No | Collision |
| rental | Rental reimbursement | No | Rental reimbursement |
| businessowners | Businessowners | No | Businessowners |
| bldg_1 | Building basic group 1 | No | Building basic group 1 |
| bldg_2 | Building Basic Group 2 | No | Building Basic Group 2 |
| contents_1 | Contents basic group 1 | No | Contents basic group 1 |
| contents_2 | Contents basic group 2 | No | Contents basic group 2 |
| farmowners | Farmowners | No | Farmowners |
| gl_std | General liability - CPP  and GL | No | General liability - CPP  and GL |
| glass | Glass | No | Glass |
| earthquake_bldg | Earthquake building | No | Earthquake building |
| earthquake_cont | Earthquake contents | No | Earthquake contents |
| gl_pers | General liability (personal umbrella) | No | General liability (personal umbrella) |
| watercraft_liab | Watercraft liability | No | Watercraft liability |
| wc | Workers' compensation | No | Workers' compensation |
| im_watercraft | Inland marine watercraft | No | Inland marine watercraft |
| im_other | Inland marine all other | No | Inland marine watercraft |
| mobile_hopHomeowners | Mobile homeowners | No | Mobile homeowners |
| hopHomeowners | Homeowners | No | Homeowners |

---

### Typelist: ManageWorkflowActionType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ManageWorkflowActionType.tti`
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

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\MaritalStatus.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\MaritalStatus.ttx`
**Description:** Types of marital status
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| single | Single | No | Single |
| married | Married | No | Married |
| divorced | Divorced | No | Divorced |
| widowed | Spouse deceased | No | Spouse deceased |
| common | Common law spouse | No | Common law spouse |
| separated | Separated | No | Separated |
| unknown | Unknown | No | Unknown |

---

### Typelist: MatterCourtDistrict

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\MatterCourtDistrict.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\MatterCourtDistrict.ttx`
**Description:** Court jurisdictional area
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

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

---

### Typelist: MatterCourtType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\MatterCourtType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\MatterCourtType.ttx`
**Description:** Court jurisdiction
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| state | State | No | State court. |
| federal | Federal | No | Federal court. |
| county | County | No | County court. |

---

### Typelist: MatterMethodServed

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\MatterMethodServed.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\MatterMethodServed.ttx`
**Description:** Method served.
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| CertifiedMail | Certified mail | No | Mailed |
| Sheriff | Sheriff | No | Sheriff |

---

### Typelist: MatterReopenedReason

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\MatterReopenedReason.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\MatterReopenedReason.ttx`
**Description:** Reason for reopening matter.
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| mistake | Mistake | No | Mistake |
| newinfo | New information | No | New information |
| retrial | Retrial | No | Retrial |

---

### Typelist: MatterRiskType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\MatterRiskType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\MatterRiskType.ttx`
**Description:** Describes the overall risk on a matter.
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| low | Low | No | Low |
| medium | Medium | No | Medium |
| high | High | No | High |

---

### Typelist: MatterStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\MatterStatus.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\MatterStatus.ttx`
**Description:** Litigation status type.
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Filed | Matter filed | No | Lawsuit filed |
| Closed | Closed | Yes | Closed |
| LegalRep | Legal representation | No | Legal representation |
| Judge | Judge selected | No | Judge selected |
| Discovery | Discovery completed | No | Discovery completed |
| TrialBegun | Trial begun | No | Trial begun |
| TrialComplete | Trial complete | No | Trial complete |
| Verdict | Verdict returned | No | Verdict returned |
| PendingAppeal | Pending appeal | No | Pending appeal |
| Appeal | In appeal | No | In appeal |

---

### Typelist: MatterTextType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\MatterTextType.tti`
**Description:** The type of matter text.
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| SettlementPlan | Settlement plan | No | The current settlement plan. |
| AltToSettlement | Alternative to settlement | No | Describes the current alternative to settling; e.g., what is the cost of settling and the likelihood that the defense can win? |
| DefenseArgument | Defense argument | No | The basics of the current defense argument. Allows busy adjusters to quickly see negotiating points while disrupted by outside plaintiff's counsel. |
| PlaintiffArgument | Plaintiff argument | No | The corollary to the defense argument. |
| RecommendedActions | Recommended actions | No | Actions currently recommended by ClaimCenter or by third-party decision support systems. |

---

### Typelist: MatterType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\MatterType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\MatterType.ttx`
**Description:** Litigation status type
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| General | General | No | General |
| Lawsuit | Lawsuit | No | Lawsuit |
| Arbitration | Arbitration | No | Arbitration |
| Hearing | Hearing | No | Hearing |
| Mediation | Mediation | No | Mediation |

---

### Typelist: MatterVenueRating

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\MatterVenueRating.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\MatterVenueRating.ttx`
**Description:** Venue type desc
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Favorable | Favorable | No | Favorable |
| Unfavorable | Unfavorable | No | Unfavorable |
| Unknown | Unknown | No | Unknown |

---

### Typelist: MedicalActionType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\MedicalActionType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\MedicalActionType.ttx`
**Description:** Types of medical-related actions
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| intlvisit | Initial visit | No | Initial visit |
| imevisit | IME visit | No | IME visit |
| stateimevisit | State-designated IME visit | No | State-designated IME visit |
| mmi | MMI visit | No | MMI visit |

---

### Typelist: MedicalTreatmentStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\MedicalTreatmentStatus.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\MedicalTreatmentStatus.ttx`
**Description:** Medical treatment status - for use on MedCaseMgr screen
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| InitialReview | Initial review | No | Initial review |
| MedicalExam | Medical exam | No | Medical exam |
| FollowUpVisit | Follow-up visit | No | Follow-up visit |
| ContinuingTreatment | Continuing treatment | No | Continuing treatment |
| RestMedication | Rest and medication | No | Rest and medication |
| PhysicalTherapy | Physical therapy | No | Physical therapy |
| ActiveTreatment | Active treatment | No | Active treatment |
| LabXray | Laboratory or X-ray | No | Laboratory or X-ray |
| SpecialistReferral | Specialist referral | No | Specialist referral |
| SpecialistTest | Specialist test | No | Specialist Test such as MRI or CAT Scan |
| Hospital | Hospital | No | Hospital |
| PendingSurgery | Pending surgery | No | Pending surgery |
| Surgery | Surgery | No | Surgery |
| PostSurgeryRecovery | Post surgical recovery period | No | Post surgical recovery period |
| Released | Released | No | Released |
| Other | Other treatment | No | Other Treatment not listed here |

---

### Typelist: MedicalTreatmentType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\MedicalTreatmentType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\MedicalTreatmentType.ttx`
**Description:** Type of treatment received
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| acup | Acupuncture | No | Acupuncture |
| chir | Chiropractor | No | Chiropractor |
| counsel | Psych counseling | No | Psych counseling |
| emer_care | Emergency care | No | Emergency care |
| er | ER treated & released | No | ER treated & released |
| hospital | Hospitalized | No | Hospitalized |
| inject | Injections | No | Injections |
| major_surgery | Major surgery | No | Major surgery |
| minor_surgery | Minor surgery | No | Minor surgery |
| mri | MRI | No | MRI |
| mult_doctors | Multiple doctors | Yes | Multiple doctors |
| mult_treatments | Multiple treatments | No | Multiple treatments |
| neuro | Neurologic | No | Neurologic |
| none | No treatment | Yes | No treatment |
| one_doctor | Only one doctor | Yes | Only one doctor |
| ortho | Orthopedic | No | Orthopedic |
| oth | Other | No | Other |
| pcp | Primary care physician | No | Primary care physician |
| pt | Physical therapy | No | Physical therapy |
| rehab | Rehab | No | Rehab |
| xray | X-ray | No | X-ray |

---

### Typelist: MergeConflictResolution

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\MergeConflictResolution.tti`
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

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\MergeConflictStrategy.tti`
**Description:** Identifies a strategy for resolving merge conflicts.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| retain_old | Retain old future-dated value | No | Strategy that retains the previously existing value with a later effective date. |
| merge_new_forward | Merge new back-dated value forward | No | Strategy that merges the new value with an earlier effective date forward. |

---

### Typelist: MessageDestinationStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\MessageDestinationStatus.tti`
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

### Typelist: MetricUnit

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\MetricUnit.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\MetricUnit.ttx`
**Description:** Units for claim metrics, such as days, currency, percent etc.
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| numeric | Numeric | No |  |
| percent | Percent | No |  |
| currency | Currency | No |  |
| hours | Hours | No |  |
| days | Days | No |  |

---

### Typelist: MetroAgencyType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\MetroAgencyType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\MetroAgencyType.ttx`
**Description:** Type of Investigating Agency for metro report
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| PD | Police Department | No | Police Department |
| CO_PD | County Police | No | County Police |
| FD | Fire Dept | No | Fire Department |
| CO_FD | County Fire | No | County Fire Department |
| CO_SO | County Sheriff | No | County Sheriff |
| SEC | Private Security | No | Private Security |
| DMV | Dept of Motor Veh. | No | Dept of Motor Veh. |
| HP | Highway Patrol/State Police | No | Highway Patrol/State Police |
| TWP_FD | Township Fire Dept | No | Township Fire Department |
| TWP_PD | Township Police | No | Township Police |
| BVS | Bureau of Vital Stats | No | Bureau of Vital Stats |
| MP | Military Police | No | Military Police |
| CORON | Coroner | No | Coroner |
| EMS | Emergency Med Serv | No | Emergency Med Serv |
| DPS | Dept of Public Safety | No | Dept of Public Safety |

---

### Typelist: MetroReportStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\MetroReportStatus.tti`
**Description:** 
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| new | New | No | The initial status of the report request |
| insufficientdata | InsufficientData | No | Some of the required fields are missing |
| validated | Validated | No | The request is validated and ready to be sent out |
| sendingorder | SendingOrder | No | The request is sent and waiting for the response from Metro |
| orderfailed | OrderFailed | No | The order request is failed based on the result sent back from Metro |
| accepted | Accepted | No | The Report Order File is sent and accepted by Metro |
| pending | Pending | No | The order was received and in process |
| hold | Hold | No | The order is awaiting additional information from the customer |
| deferred | Deferred | No | An image was returned with a notice that the data source will take some additional time to provide the requested information |
| sendinginquiry | SendingInquiry | No | The Report Inquiry File is sent and waiting for the response from Metro |
| hasreport | HasReport | No | The Report is ready on the external server |
| downloadingreport | DownloadingReport | No | The system is in the process of downloading the report |
| received | Received | No | The Report is received (download) to our server |
| inquiryfailed | InquiryFailed | No | The inquiry request is failed based on the result sent back from Metro |
| closed | Closed | No | The Report is Closed |
| error | Error | No | The Report request has errors |
| duplicate | Duplicate | No | The Report request failed due to a duplicate request |

---

### Typelist: MetroReportType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\MetroReportType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\MetroReportType.ttx`
**Description:** Type of metro reports
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| A | Auto Accident | No | Auto Accident |
| B | Auto Theft | No | Auto Theft |
| C | Auto Theft Recovery | No | Auto Theft Recovery |
| D | Driving History | No | Driving History |
| E | Coroner Reports | No | Coroner Reports |
| F | Fire Home | No | Fire Home |
| G | Burglary | No | Burglary |
| H | Death Certificate | No | Death Certificate |
| I | Incident | No | Incident |
| J | Locate Defendant/Witness | No | Locate Defendant/Witness |
| K | EMS/Rescue Squad | No | EMS/Rescue Squad |
| L | Supplemental/Addendum | No | Supplemental/Addendum |
| M | MV-104 (NY Only) | No | MV-104 (NY Only) |
| N | OSHA | No | OSHA |
| O | Other | No | Other |
| P | Activities Fixed Rate | No | Activities Fixed Rate |
| Q | Property and Judgments | No | Property and Judgments |
| R | Registration Check/DMV | No | Registration Check/DMV |
| S | Insurance Check | No | Insurance Check |
| T | Title History | No | Title History |
| U | Subrogation Financial/Assets | No | Subrogation Financial/Assets |
| V | Vandalism/Auto | No | Vandalism/Auto |
| W | Weather Report | No | Weather Report |
| X | Fire-Auto | No | Fire-Auto |
| Y | Photo | No | Photo |
| Z | Disposition of Charges | No | Disposition of Charges |

---

### Typelist: NamePrefix

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\NamePrefix.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\NamePrefix.ttx`
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

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\NameSuffix.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\NameSuffix.ttx`
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
| esq | Esq. | No | Esquire |

---

### Typelist: NegotiationType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\NegotiationType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\NegotiationType.ttx`
**Description:** Type of negotiation.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Offer | Offer | No | Offer |
| Demand | Demand | No | Demand |
| Counter | Counteroffer | No | Counteroffer |
| Rejection | Rejection | No | Rejection (going to trial) |
| AcceptedSettlement | Accepted Settlement | No | Accepted Settlement |

---

### Typelist: NoteSecurityType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\NoteSecurityType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\NoteSecurityType.ttx`
**Description:** Type of the note for access-restriction purposes
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| public | Public | No | Note viewable by any user in the system |
| private | Private | No | Note viewable by internal users only |
| sensitive | Sensitive | No | Confidential note, viewable by select internal users only |
| medical | Medical | No | Medical note, viewable by internal users with medical note view/edit permissions |

---

### Typelist: NoteTopicType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\NoteTopicType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\NoteTopicType.ttx`
**Description:** Topic to which this note belongs
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| general | General | No | General |
| fnol | First notice of loss | No | First notice of loss |
| coverage | Coverage | No | Coverage |
| investigation | Investigation | No | Investigation |
| medical | Medical issues | No | Medical issues |
| evaluation | Evaluation | No | Evaluation |
| settlement | Settlement | No | Settlement |
| subrogation | Subrogation | No | Subrogation |
| salvage | Salvage | No | Salvage |
| litigation | Litigation | No | Litigation |
| denial | Denial | No | Denial |
| reinsurance | Reinsurance | No | Reinsurance |

---

### Typelist: NoteType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\NoteType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\NoteType.ttx`
**Description:** Type of note
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| diagram | Diagram | No | Diagram |
| interviewreport | Interview report | No | Interview report |
| actionplan | Action plan | No | Action plan |
| statusreport | Status report | No | Status report |
| reviewactivity | Supervisor review activity | No | Action plan |

---

### Typelist: NotificationType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\NotificationType.tti`
**Description:** Special Handling Notification Type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| email | Single email recipient | No | Notify a single email recipient |
| multi_email | Multiple email recipients | No | Notify multiple email recipients |
| contactrole | Contact based on claim role | No | Notify a contact based on his/her role |

---

### Typelist: NumberOfClaims

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\NumberOfClaims.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\NumberOfClaims.ttx`
**Description:** Number of claims for question set
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 0 | Under 3 in past year | No | Under 3 in past year |
| 5 | Between 3 and 6 in past year | No | Between 3 and 6 in past year |
| 10 | Over 6 in the past year | No | Over 6 in the past year |

---

### Typelist: OccupancyType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\OccupancyType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\OccupancyType.ttx`
**Description:** To describe where the property in question is occupied
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| vacant | Vacant | No | Vacant |
| underConst | Under Construction | No | Under Construction |
| occupied | Occupied | No | Occupied |

---

### Typelist: OfficialIDType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\OfficialIDType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\OfficialIDType.ttx`
**Description:** Type of official id (i.e. SSN, FEIN, State Tax, State Unemployment, etc)
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| BureauID | Bureau ID | No | Bureau ID |
| DOLID | Dept of Labor ID | No | Dept of Labor ID |
| DUNS | Dun & Bradstreet Number | No | Dun & Bradstreet Number |
| FEIN | FEIN | No | Federal Employer Identification Number |
| NCCIID | Bureau ID | No | Bureau ID |
| SSN | SSN | No | Social Security Number |
| STAX | State Tax ID | No | State Tax Identification Number |
| STUN | State Unemployment ID | No | State Unemployment Identification Number |
| TUNS | Temporary Dun & Bradstreet Number | No | Temporary Dun & Bradstreet Number |
| NCCIintrastate | NCCI Intrastate ID | No | NCCI Intrastate ID |

---

### Typelist: OfficialType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\OfficialType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\OfficialType.ttx`
**Description:** Type of official - police, fire etc
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| police | Police | No | Police |
| seriff | Sheriff | No | Sheriff |
| trooper | State trooper | No | State trooper |
| security | Security officer | No | Security officer |
| coroner | Coroner | No | Coroner |
| fire | Fire | No | Fire |
| ambulance | Ambulance | No | Ambulance |
| depttrans | Dept. of Transportation | No | Dept. of Transportation |
| regagency | Regulatory agency | No | Regulatory agency |
| healthdept | Health department | No | Health department |
| civilagen | Civil agency | No | Civil agency |
| utilservprov | Utility service provider | No | Utility service provider |
| fema | FEMA | No | FEMA |
| other | Other | No | Other |

---

### Typelist: OffRoadVehicleStyle

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\OffRoadVehicleStyle.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\OffRoadVehicleStyle.ttx`
**Description:** Style of snowmobile or ATV (wheels, tracks etc.)
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| CYL | Cycle only | No | Cycle only |
| SKT | Skis and tracks | No | Skis and tracks |
| SKW | Skis and wheels | No | Skis and wheels |
| TRA | Tracks only | No | Tracks only |
| TRW | Tracks and wheels | No | Tracks and wheels |
| WHE | Wheels only | No | Wheels only |

---

### Typelist: OnPremisesType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\OnPremisesType.tti`
**Description:** Whether the incident occurred on the employer's premises
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| yes | Yes | No | Yes |
| no | No | No | No |

---

### Typelist: OrganizationType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\OrganizationType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\OrganizationType.ttx`
**Description:** Type of organization for attorneys, doctors, and government authorities
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| solepropship | Sole Proprietorship | No | Sole Proprietorship |
| partnership | Partnership | No | Partnership |
| corporation | Corporation | No | Corporation |
| federal | Federal | No | Federal |
| state | State | No | State |
| county | County | No | County |
| city | City | No | City |

---

### Typelist: OtherRecoverableStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\OtherRecoverableStatus.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\OtherRecoverableStatus.ttx`
**Description:** Other recoverable status
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| in_review | In review | No | Salvage is in review |
| open | Open | No | Salvage is open |
| closed | Closed | No | Salvage is closed |

---

### Typelist: OtherRiskType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\OtherRiskType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\OtherRiskType.ttx`
**Description:** Type of location based miscellaneous risk unit
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| acctrecvblonpremise | Accounts Receivable On Premise | No | Accounts Receivable On Premise |
| acctrecvbloffpremise | Accounts Receivable Off Premise | No | Accounts Receivable Off Premise |
| schequipment | Scheduled Equipment | No | Scheduled Equipment |
| signs | Signs | No | Signs |
| other | Other | No | Other |

---

### Typelist: OutboundRecordStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\OutboundRecordStatus.tti`
**Description:** The status for an Outbound Record.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| pending | Pending | No | The outbound record is ready to be delivered. |
| processed | Processed | No | The Outbound Record has been processed and included in an Outbound File. |
| error | Error | No | The Outbound Record resulted in an error when processed. |
| skipped | Skipped | No | The Outbound Record has been skipped and is awaiting purge. |

---

### Typelist: Outcome

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\Outcome.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\Outcome.ttx`
**Description:** The outcome of the exposure
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| denied | Denied - no payment | No | Denied - no payment |
| closednopayment | Closed - no payment | No | Closed - no payment |
| settled | Settled with payment | No | Settled with payment |
| lit_settled | Litigation: settled | No | Litigation: settled |
| litigation_won | Litigation: won a judgment | No | Litigation: won a judgment |
| litigation_lost | Litigation: lost a judgment | No | Litigation: lost a judgment |
| dropped | Claimant stopped pursuing claim | No | Claimant stopped pursuing claim |

---

### Typelist: OwnerType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\OwnerType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\OwnerType.ttx`
**Description:** Types of ownership
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| sole_owner | Sole owner | No | Sole owner / lienholder |
| partial_owner | Partial owner | No | Partial owner |

---

### Typelist: PaidOnTime

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\PaidOnTime.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\PaidOnTime.ttx`
**Description:** 
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| notapplicable | Not applicable | No | Not applicable |
| ontime | First TTD payment on time | No | First TTD payment on time |
| payafterdelay | First payment after claim in delay/deny status | No | First payment after claim in delay/deny status |
| moconvert | First payment after claim converting from MO to Indemnity | No | First payment after claim converting from MO to Indemnity |
| payaward | Payment for award | No | Payment for award |
| payedd | Payment to EDD | No | Payment to EDD |
| attendexam | Payment to attend exam | No | Payment to attend exam |
| latenotice | Late because of late notice | No | Late because of late notice |
| latetechnical | Late because of technical processing | No | Late because of technical processing |

---

### Typelist: ParameterType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ParameterType.tti`
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

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\Parentheses.tti`
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

### Typelist: PartialDenialReason

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\PartialDenialReason.tti`
**Description:** Partial Denial Reason Codes
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| A | Denying Indemnity in whole, but not Medical | No | Denying Indemnity in whole, but not Medical |
| B | Denying Indemnity in part, but not Medical | No | Denying Indemnity in part, but not Medical |
| C | Denying Medical in whole, but not Indemnity | No | Denying Medical in whole, but not Indemnity |
| D | Denying Medical in part, but not Indemnity | No | Denying Medical in part, but not Indemnity |
| E | Denying Indemnity in whole and Medical in part | No | Denying Indemnity in whole and Medical in part |
| F | Denying Medical in whole and Indemnity in part | No | Denying Medical in whole and Indemnity in part |
| G | Denying both Indemnity and Medical in part | No | Denying both Indemnity and Medical in part |

---

### Typelist: PaymentFrequencyType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\PaymentFrequencyType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\PaymentFrequencyType.ttx`
**Description:** Per-state definition of possible payment periods
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| daily | Daily | No | Employee to be paid on a daily basis |
| weekly | Weekly | No | Employee to be paid on a weekly basis |
| everytwoweeks | Every two weeks | No | Employee to be paid every two weeks |
| twiceamonth | Twice a month | No | Employee to be paid twice a month |
| monthly | Monthly | No | Employee to be paid on a monthly basis |

---

### Typelist: PaymentMethod

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\PaymentMethod.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\PaymentMethod.instant.ttx`
**Description:** Method of payment
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| manual | Manual check | No | Manual check |
| check | Check | No | Check |
| eft | Electronic funds transfer | No | Electronic funds transfer |
| instant | Instant | No | Instant payment |

---

### Typelist: PaymentType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\PaymentType.tti`
**Description:** Type of payment
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| partial | Partial | No | Partial |
| final | Final | No | Final |
| supplement | Supplement | No | Supplement |

---

### Typelist: PayPeriodType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\PayPeriodType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\PayPeriodType.ttx`
**Description:** Pay period type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| daily | Daily | No | Employee paid on a daily basis |
| weekly | Weekly | No | Employee paid on a weekly basis |
| everytwoweeks | Every two weeks | No | Employee paid every two weeks |
| twiceamonth | Twice a month | No | Employee paid twice a month |
| monthly | Monthly | No | Employee paid on a monthly basis |

---

### Typelist: PersonalDataTagValue

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\PersonalDataTagValue.tti`
**Description:** Valid tag values for a PersonalData tag
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| ObfuscateDefault | ObfuscateDefault | No | default obfuscation for personal data |
| ObfuscateUnique | ObfuscateUnique | No | unique obfuscation for personal data |

---

### Typelist: PersonRelationType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\PersonRelationType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\PersonRelationType.ttx`
**Description:** The relationship of the person to the claimant
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| self | Self/Insured | No | Self |
| relative | Relative | No | Relative |
| friend | Friend | No | Friend |
| agent | Agent | No | Agent |
| attorney | Attorney | No | Attorney |
| employee | Employee | No | Employee |
| other | Other | No | Other |
| spouse | Spouse | No | Spouse |
| child | Child | No | Child |
| parent | Parent | No | Parent |
| grandparent | Grandparent | No | Grandparent |
| domesticpartner | Domestic partner | No | Domestic partner |
| claimant | Claimant | No | Claimant |
| claimantatty | Claimant's attorney | No | Claimant's attorney |
| claimantinsco | Claimant's insurance co. | No | Claimant's insurance co. |
| rentalrep | Rental representative | No | Rental representative |
| repairshop | Repair shop | No | Repair shop |
| insco | Insurance company | Yes | Insurance co (typically would be third-party insurer) |
| injuredworker | Injured Worker | No | Injured Worker |
| supervisor | Supervisor | No | Supervisor |
| riskmanager | Risk Manager | No | Risk Manager |
| medicalprovider | Medical Provider | No | Medical Provider |
| hrrep | HR Representative | No | HR Representative |

---

### Typelist: PhoneCountryCode

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\PhoneCountryCode.tti`
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

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\PhoneType.tti`
**Description:** List of regions and their regional phone codes
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Work | Work | No | Work |
| Fax | Fax | No | Fax |
| Home | Home | No | Home |
| Cell | Mobile | No | Mobile |
| Generic | Generic | No | Generic |

---

### Typelist: PolicyPeriodType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\PolicyPeriodType.tti`
**Description:** Policy grouping types
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| account | Account | No | Policy grouping by account. |
| policy | Policy | No | Policy grouping by policy snapshot. |

---

### Typelist: PolicyRatingPlan

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\PolicyRatingPlan.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\PolicyRatingPlan.ttx`
**Description:** Policy rating plans
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| GuaranteedCost | Guaranteed cost | No | Guaranteed cost |
| SlidingScaleDiv | Sliding scale dividend | No | Sliding scale dividend |
| IncurredLossRat | Incurred loss ratio | No | Incurred loss ratio |
| PaidLossRetro | Paid loss retroactive | No | Paid loss retroactive |
| Deductible | Deductible | No | Deductible |
| Par | Par (CA only) | No | Par (CA only) |
| NonPar | Non-par (CA only) | No | Non-par (CA only) |

---

### Typelist: PolicySource

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\PolicySource.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\PolicySource.ttx`
**Description:** Sources for policies
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Manual | Manual entry | No | Manual entry |
| Automated | Automated entry | No | Automated entry |

---

### Typelist: PolicyStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\PolicyStatus.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\PolicyStatus.ttx`
**Description:** Status of the claim
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| inforce | In force | No | The policy is in force as of the requested effective date. |
| expired | Expired | No | The policy term is expired as of the current date. |
| paymentpastdue | Payment past due | Yes | Payment past due |
| archived | Archived | No | The policy has been archived by the policy system, so no details are available. |
| canceled | Canceled | No | The policy is canceled as of the requested effective date. |
| pending_cancellation | Pending Cancellation | No | The policy is pending cancellation because of non-payment or some other underwriting reason. |
| pending_confirmation | Pending Confirmation | No | The policy term has been created in the policy system but is not yet considered binding, usually pending payment. |

---

### Typelist: PolicyTab

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\PolicyTab.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\PolicyTab.ttx`
**Description:** Available policy tabs
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| endorsements | Endorsements | No | Endorsements |
| statcodes | Stat Codes | No | Statistical codes |
| aggregatelimits | Aggregate Limits | No | Aggregate limits |
| classcodes | Class Codes | No | Property locations with associated class codes |
| vehicles | Vehicles | No | Vehicles |
| properties | Properties | No | Property locations |
| boats | Boats | No | Boats |
| misc | Misc | No | Misc |
| trips | Trips | No | Trips for travel |

---

### Typelist: PolicyType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\PolicyType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\PolicyType.ttx`
**Description:** Types of policies
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| PersonalAuto | Personal Auto | No | Personal Auto |
| BusinessAuto | Commercial Auto | No | Commercial Auto |
| CommercialPackage | Commercial Package | No | Commercial Package |
| GeneralLiability | General Liability | No | General Liability |
| HOPHomeowners | Homeowners | No | Homeowners |
| CommercialProperty | Commercial Property | No | Commercial Property |
| InlandMarine | Inland Marine | No | Inland Marine |
| WorkersComp | Workers' Compensation | No | Workers' Compensation |
| BusinessOwners | Businessowners | No | Business Owners |
| PersonalUmbrella | Personal Umbrella | No | Personal Umbrella |
| prof_liability | Professional Liability | No | Professional liability |
| farmowners | Farmowners | No | Farmowners |
| D_and_O | Directors and Officers | Yes | Directors and officers |
| travel_per | Personal Travel | No | Personal travel includes a single person and families, not group travel |

---

### Typelist: PriContributingFactors

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\PriContributingFactors.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\PriContributingFactors.ttx`
**Description:** First column of contributing factors array
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Environment | Environmental conditions | No | Environmental conditions |
| DriverFactors | Driver factors | No | Driver factors |
| ProtectFactors | Protection factors | No | Protection factors |
| Enviro | Environment | No | Environment |
| HumanInvolve | Human involvement | No | Human involvement |
| Defect | Defect | No | Defect |
| Commun | Communication | No | Communication |
| HumanInvolveGL | Human involvement | No | Human involvement |
| EnviroGL | Environment | No | Environment |
| notapplic | Not applicable | No | Not applicable |
| contacts | Contracts | No | Contracts |

---

### Typelist: PrimaryCauseType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\PrimaryCauseType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\PrimaryCauseType.ttx`
**Description:** Legal suit primary cause type.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Delay | Delay or insufficient claimant contact | No | Delay or insufficient claimant contact |
| Predetermined | Predetermined | No | Claimant always intended to file |
| LowSettlement | Low settlement offer | No | Low settlement offer |
| BS | Blind Suit/First Notice | No | Blind Suit/First Notice |
| UD | Unreasonable Demand | No | Unreasonable Demand |
| NI | Negotiations at Impasse | No | Negotiations at Impasse |
| VD | Valuation Dispute (1st party) | No | Valuation Dispute (1st party) |
| CA | Court Approval | No | Court Approval |
| SL | Statute of Limitations | No | Statute of Limitations |

---

### Typelist: PrimaryColor

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\PrimaryColor.tti`
**Description:** Primary Colors
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| ff0000 | Red | No | Red |
| 00ff00 | Green | No | Green |
| 0000ff | Blue | No | Blue |

---

### Typelist: PrimaryPhoneType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\PrimaryPhoneType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\PrimaryPhoneType.ttx`
**Description:** Types of phone numbers
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| home | Home | No | Home |
| work | Work | No | Work |
| mobile | Mobile | No | Mobile |

---

### Typelist: PrintFormat

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\PrintFormat.tti`
**Description:** Different print views; corresponds to the report or template used to create the printable document
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| *(None defined)* | *Dynamic or database-driven* | No | Typelist populated dynamically at runtime or via database table |

---

### Typelist: Priority

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\Priority.tti`
**Description:** Basic priority typelist
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| urgent | Urgent | No | Highest priority - must be addressed immediately |
| high | High | No | High priority - should be addressed before normal activities |
| normal | Normal | No | Normal |
| low | Low | No | Low - needs to be addressed eventually but there is no urgency |

---

### Typelist: PropertyLineItemCategory

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\PropertyLineItemCategory.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\PropertyLineItemCategory.ttx`
**Description:** AssessmentItemCategory
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| acu | Air Conditioning | No | Air Conditioning |
| building | Building | No | building |
| Fence | Fence | No | Fence |
| generator | Generators | No | Generators |
| heating | Heating System | No | Heating System |
| lighting | Lighting System | No | Lighting Systems |
| plumbing | Plumbing System | No | Plumbing System |
| roof | Roof | No | Roof |

---

### Typelist: ProviderType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ProviderType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ProviderType.ttx`
**Description:** Types of services providers
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| familymember | Family member | No | Family member |
| thirdparty | Third party | No | Third party |

---

### Typelist: ProximitySearchStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ProximitySearchStatus.tti`
**Description:** Categorize the geocode status of an address
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| failed | Failed | No | This category includes the following geocode status: failure |
| notyetsearchable | Not Yet Searchable | No | This category includes the following geocode status: none |
| searchable | Searchable | No | This category includes the following geocode status: exact, street, city, postalcode |

---

### Typelist: PurgeType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\PurgeType.tti`
**Description:** Not specified in source
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Unknown | Unknown | No | Unknown |

---

### Typelist: QuestionFormat

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\QuestionFormat.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\QuestionFormat.ttx`
**Description:** How the question should be rendered in PCF
**Synthetic Data Relevance:** Operational / Reference

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

---

### Typelist: QuestionSetType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\QuestionSetType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\QuestionSetType.ttx`
**Description:** A kind of question set
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| newclaim | NewClaim | No | New Claim Wizard Questionaire |
| siucar | SIUCar | No | Auto SIU questions - applicable for auto claims |
| siugen | SIUGen | No | General SIU questions - applicable to all. |
| siuwork | SIUwork | No | Workers comp SIU questions - applicable for workers compensation claims. |
| spmreview | SPMReview | No | Review for Service Provider Management |

---

### Typelist: QuestionType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\QuestionType.tti`
**Description:** A kind of question
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Boolean | Boolean | No | A question whose answer is Yes or No |
| Date | Date | No | A question whose answer is a Date |
| Integer | Integer | No | A question whose answer is an Integer |
| String | String | No | A question whose answer is a String |
| Choice | Choice | No | A multiple-choice question whose answer is an entry in the QuestionChoice table |

---

### Typelist: RadiusChoice

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\RadiusChoice.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\RadiusChoice.ttx`
**Description:** Choices for the radius of a proximity search
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 5 | 4 | No | 10 |
| 10 | 10 | No | 10 |
| 20 | 20 | No | 20 |
| 50 | 50 | No | 50 |
| 100 | 100 | No | 100 |
| 200 | 200 | No | 200 |
| 500 | 500 | No | 500 |
| 1000 | 1000 | No | 1000 |

---

### Typelist: ReasonForUse

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ReasonForUse.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ReasonForUse.ttx`
**Description:** Business or pleasure
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| business | Business | No | Business |
| pleasure | Pleasure | No | Pleasure |

---

### Typelist: RecoveryCategory

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\RecoveryCategory.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\RecoveryCategory.ttx`
**Description:** Categories of recovery
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| unspecified | Unspecified Recovery Category | No | Unspecified Recovery Category |
| salvage | Salvage | No | Salvage |
| subro | Subrogation | No | Subrogation |
| credit_loss | Credit to loss | No | Credit to loss |
| credit_exp | Credit to expense | No | Credit to expense |
| deductible | Deductible | No | Deductible |

---

### Typelist: RecurrenceDay

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\RecurrenceDay.tti`
**Description:** Days of the week that payments can be made
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| mon | Monday | No | Monday |
| tue | Tuesday | No | Tuesday |
| weds | Wednesday | No | Wednesday |
| thurs | Thursday | No | Thursday |
| fri | Friday | No | Friday |
| sat | Saturday | No | Saturday |
| sun | Sunday | No | Sunday |

---

### Typelist: RecurrenceWeek

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\RecurrenceWeek.tti`
**Description:** Week in the month that a payment can be made; used as a modifier for the values in the RecurrenceDay typelist
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| first | first | No | first |
| second | second | No | second |
| third | third | No | third |
| fourth | fourth | No | fourth |
| last | last | No | last |

---

### Typelist: RegionType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\RegionType.tti`
**Description:** Types of region definitions
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| state | State | No | State |
| county | County | No | County |
| zip | Zip code | No | Zip code |

---

### Typelist: ReinsuranceFlaggedStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ReinsuranceFlaggedStatus.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ReinsuranceFlaggedStatus.ttx`
**Description:** Flagged status of reinsurance, or does not apply
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| SystemFlagged | System Flagged | No | Reinsurance reportable set by the system |
| UserFlagged | User Flagged | No | Reinsurance reportable set by the user |
| UserUnflagged | User Unflagged | No | Reinsurance reportable unset by the user |
| SystemUnflagged | System Unflagged | No | Reinsurance reportable set by the system |

---

### Typelist: ReinsuranceTreatyType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ReinsuranceTreatyType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ReinsuranceTreatyType.ttx`
**Description:** Type of reinsurance treaty
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| liab | Liability | No | Liability Treaty |
| prop | Property | No | Property Treaty |
| wc | Workers' comp | No | Workers' Compensation Treaty |

---

### Typelist: ReportabilityType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ReportabilityType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ReportabilityType.ttx`
**Description:** Whether a payment should be reported to the IRS as income
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| notreportable | Not reportable | No | Not reportable |
| reportable | Reportable | No | Reportable |

---

### Typelist: ReportingDate

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ReportingDate.tti`
**Description:** Applicable reporting dates
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| extreportdate | extreportdate | No | Extended reporting date |
| retroactivedate | retroactivedate | No | Retroactive date |

---

### Typelist: ResContributingFactors

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ResContributingFactors.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ResContributingFactors.ttx`
**Description:** Third column of Contributing factors array
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Rain | Rain | No | Rain |
| Snow | Snow | No | Snow |
| Sleet | Sleet | No | Sleet |
| Hail | Hail | No | Hail |
| HighWind | High Wind/Wind Gust | No | High Wind/Wind Gust |
| WthOther | Other Weather | No | Other |
| Dry | Dry | No | Dry |
| Wet | Wet | No | Wet |
| Ice | Ice | No | Ice |
| SnowSlush | Snow or Slush | No | Snow or Slush |
| SandMudDirt | Sand / Mud / Dirt | No | Sand / Mud / Dirt |
| Oil | Oil | No | Oil |
| Gravel | Gravel | No | Gravel |
| RDOther | Other Road Surface | No | Other |
| Daylight | Daylight | No | Daylight |
| Dusk | Dusk | No | Dusk |
| Dawn | Dawn | No | Dawn |
| NightLight | Night lighted | No | Night lighted |
| nghtnolght | Night not lighted | No | Night not lighted |
| lgtOther | Other Light Condition | No | Other Light Condition |
| solarglare | Solar glare | No | Solar glare |
| blowdebris | Blowing debris | No | Blowing debris |
| Smoke | Smoke | No | Smoke |
| Fog | Fog | No | Fog |
| Othervis | Other Visibility | No | Other Visibility |
| notphysdiv | Not physically divided | No | Not physically divided |
| divwobarrier | Divided without barrier | No | Divided without barrier |
| divwbarrier | Divided with barrier | No | Divided with barrier |
| oneway | One way | No | One way |
| uncontinter | uncontrolled intersection | No | uncontrolled intersection |
| onramp | on ramp | No | on ramp |
| offramp | off ramp | No | off ramp |
| otherhwy | Other Highway Type | No | Other Highway Type |
| lessthan1 | < 1 hr | No | Less Than One Hour |
| 1to4hours | 1hr - 04:59hrs | No | One hour to 4 hours and 59 minutes |
| 5to9hours | 5hrs - 09:59hrs | No | Five hours to 9 hours and 59 minutes |
| tenhours | 10 hours or more | No | Ten hours or more |
| lessoneday | < 1 day | No | less than one day |
| onetothree | 1-3 days | No | 1-3 days |
| fourtoseven | 4-7 days | No | 4-7 days |
| lessseven | > 7days | No | greater than 7 days |
| zerotonine | 0 - 9 | No | 0 - 9 |
| tentwentyfive | 10 to 25 | No | 10 to 25 |
| twentyfivefourty | 25 to 40 | No | 25 to 40 |
| fourtyonesixty | 41 to 60 | No | 41 to 60 |
| sixtyoneplus | 61 or greater | No | 61 or greater |
| OrdinaryComb | Ordinary Combustibles | No | Ordinary Combustibles |
| GreaseFlameLiq | Grease/Flammable Liquid | No | Grease/Flammable Liquid |
| LintDust | Lint/Dust | No | Lint/Dust |
| Otherhouse | Other Housekeeping | No | Other |
| SolidPiles | Solid Piles | No | Solid Piles |
| Racks | Racks | No | Racks |
| Otherstore | Other Storage | No | Other Storage |
| IneffFireWalls | Ineffective Fire Walls/Doors | No | Ineffective Fire Walls/Doors |
| UnprotVertOpen | Unprotected Verticle Openings | No | Unprotected Verticle Openings |
| ImproperDucts | Improperly Spaced Ducts | No | Improperly Spaced Ducts |
| OtherPhs | Other Physical Features | No | Other Physical Features |
| Delayed | Delayed | No | Delayed |
| Inappropriate | Inappropriate | No | Inappropriate |
| otherdiscov | Other Discovery | No | Other Discovery |
| defectinstr | Defective instructions | No | Defective instructions |
| insuffinstr | Insufficient instructions | No | Insufficient instructions |
| inapproplang | Language inappropriate for foreign speaking market | No | anguage inappropriate for foreign speaking market |
| misleadinstr | Misleading instructions | No | Misleading instructions |
| noinstr | No instructions | No | No instructions |
| encourage | Encouraged misuse | No | Encouraged misuse |
| failnotify | Failure to notify of defect/recall/retrofit | No | Failure to notify of defect/recall/retrofit |
| misrep | Misrepresentation | No | Misrepresentation |
| failwarn | Failure to warn | No | Failure to warn |
| inadequate | Inadequate warnings | No | Inadequate warnings |
| misleading | Misleading warnings | No | Misleading warnings |
| design | Design | No | Design |
| manufacture | Manufacture | No | Manufacture |
| warranty | Warranty/Performance | No | Warranty/Performance |
| repairs | Repairs/Maintanence | No | Repairs/Maintanence |
| installation | Installation | No | Installation |
| othernon | Other | No | Other |
| foreign | Foreign substance | No | Foreign substance |
| spoiled | Spoiled | No | Spoiled |
| bacterial | Bacterial | No | Bacterial |
| bornchem | Foodborne chemical toxin | No | foodborne chemical toxin |
| otherfood | Other Food | No | Other |
| curb | Curb | No | Curb |
| elevcha | Elevation Change | No | Elevation Change |
| floor | Floor Defect | No | Floor Defect |
| grmusa | Grass / Mud / Sand | No | Grass / Mud / Sand |
| incline | Incline | No | Incline |
| protrud | Protruding object | No | Protruding object |
| surdef | Surface Defect | No | Surface Defect |
| othersurf | Other Surface | No | Other Surface |
| display | Display | No | Display |
| furnfix | Furniture / Fixture | No | Furniture / Fixture |
| icesnow | Ice/Snow | No | Ice/Snow |
| water | Water | No | Water |
| othersub | Other Substance | No | Other |
| unguarded | Unguarded | No | Unguarded |
| inadguard | Inadequate guarding/protection | No | Inadequate guarding/protection |
| guardtamp | Guarding was tampered with/ removed/bypassed | No | Guarding was tampered with/ removed/bypassed |
| uservio | User violated instructions | No | User violated instructions |
| warnig | Warnings were ignored | No | Warnings were ignored |
| bothinst | Both instructions and warnings were ignored | No | Both instructions and warnings were ignored |
| warntrue | No instructions or warnings against this use | No | No instructions or warnings against this use |
| notapplic | Not Applicable | No | Not Applicable |
| holdharmless | Hold Harmless/Indemnity | No | Hold Harmless/Indemnity |
| addinsured | Additional Insured | No | Additional Insured |
| other | Other | No | Other |

---

### Typelist: ResolutionType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ResolutionType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ResolutionType.ttx`
**Description:** Legal matter resolution type.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| AD | Appeal dismissed | No | Appeal dismissed |
| AL | Appeal lost | No | Appeal lost |
| AM | Appeal moot | No | Appeal moot |
| AR | Appeal remanded | No | Appeal remanded |
| AW | Appeal withdrawn | No | Appeal withdrawn |
| AWO | Appeal won | No | Appeal won |
| AP | Appealed | No | Appealed |
| AA | Award | No | Award |
| CV | Change of venue | No | Change of venue |
| CN | Conflict | No | Conflict |
| CO | Consolidation | No | Consolidation |
| CA | Coverage acknowledged | No | Coverage acknowledged |
| CD | Coverage denied | No | Coverage denied |
| DJ | Default judgment | No | Default judgment |
| DT | Defense tendered | No | Defense tendered |
| DVD | Directed verdict-defendant | No | Directed verdict-defendant |
| DVP | Directed verdict-plaintiff | No | Directed verdict-plaintiff |
| DS | Discontinued | No | Discontinued |
| DM | Dismissed | No | Dismissed |
| PMD | Petition/motion denied | No | Petition/motion denied |
| PMG | Petition/motion granted | No | Petition/motion granted |
| PMW | Petition/motion withdrawn | No | Petition/motion withdrawn |
| SA | Settled-ADR | No | Settled-ADR |
| SAA | Settled-appraisal award | No | Settled-appraisal award |
| SR | Settled-regular | No | Settled-regular |
| SO | Settled-other | No | Settled-other |
| SS | Settled-structured | No | Settled-structured |
| SJ | Summary judgment | No | Summary judgment |
| VD | Verdict for defendant | No | Verdict for defendant |
| VP | Verdict for plaintiff | No | Verdict for plaintiff |
| VO | Voided defense/matter | No | Voided defense/matter |
| Settlement | Settlement | Yes | Settlement |
| Judgment | Judgment | Yes | Judgment |
| Appeal | Appeal | Yes | Appeal |

---

### Typelist: ResourceContext

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ResourceContext.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ResourceContext.ttx`
**Description:** A context for packaging rule sets, libraries, script parameters, and other configurable resources
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| wc | Guidewire workers' comp | No | Guidewire workers' compensation related resources |
| base | Guidewire base | No | Guidewire base configuration related resources |
| sample | Guidewire sample data | No | Guidewire sample data related resources |
| iso | Guidewire ISO configuration | No | Guidewire ISO ClaimSearch messaging resources |
| si | Guidewire Special Investigations Detection | No | Guidewire Special Investigations Detection resources |
| limitsded | Guidewire limits and deductibles | No | Guidewire limits and deductibles |
| assignrules | Guidewire assignment rules | No | Guidewire assignment rules |
| segmentrules | Guidewire segmentation rules | No | Guidewire segmentation rules |
| pip | Guidewire PIP rules | No | Guidewire PIP rules |
| totalloss | Guidewire total loss calculator rules | No | Guidewire total loss calculator rules |
| deductibles | Guidewire payment deductible rules | No | Guidewire payment deductible rules |
| workplan | Guidewire workplan rules | No | Guidewire workplan rules |
| claimshistory | Guidewire claims history rules | No | Guidewire claims history rules |
| salvage | Guidewire salvage rules | No | Guidewire salvage rules |
| subro | Guidewire subrogation rules | No | Guidewire subrogation rules |

---

### Typelist: ResultingAction

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ResultingAction.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ResultingAction.ttx`
**Description:** List of available actions for dynamic action configuration
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| NewActivity | Create Activity | No | Creates a new activity |

---

### Typelist: RetroPeriodType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\RetroPeriodType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\RetroPeriodType.ttx`
**Description:** Per-state definition of possible retroactive periods
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| seven | Seven calendar days | No | Seven calendar days |
| ten | Ten calendar days | No | Ten calendar days |

---

### Typelist: ReviewCategory

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ReviewCategory.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ReviewCategory.ttx`
**Description:** Category for Service Provider Management Review questions and categories; generally, this will be extended by customers
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| general | General | No | A default category for general questions. |
| timeliness | Timeliness | No | Timeliness |
| communication | Communication | No | Communication |
| officestaff | Office Personnel | No | Office Personnel. |
| technicians | Technicians | No | Technicians |
| quality | Quality of Work | No | Quality of Work |
| accuracy | Accuracy of Quote | No | Accuracy of Quote |
| adjuster | Adjuster | No | Section for adjusters to add comments |

---

### Typelist: ReviewServiceType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ReviewServiceType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ReviewServiceType.ttx`
**Description:** Service types list for Service Provider Management Reviews; generally, this will be extended by customers
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| other | Other | No | Indicates that no more specific service type is applicable. |
| body | Body | No | Body |
| paint | Paint | No | Paint |
| drivetrain | Transmission and Engine | No | Transmission and Engine |
| brakes | Brakes | No | Brakes |
| suspension | Suspension | No | Suspension |

---

### Typelist: RIAgreementCoverageType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\RIAgreementCoverageType.tti`
**Description:** The coverage type of the reinsurance agreement
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Aggregate | Aggregate | No | Aggregate reinsurance coverage |
| PerRisk | PerRisk | No | Per risk reinsurance coverage |

---

### Typelist: RIAgreementStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\RIAgreementStatus.tti`
**Description:** Status of reinsurance agreement, used in RIAgreement.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| draft | Draft | No | Draft |
| active | Active | No | Active |

---

### Typelist: RIArrangementType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\RIArrangementType.tti`
**Description:** Type of arrangement of a reinsurance agreement (Treaty or Facultative).
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| treaty | Treaty | No | Agreement between the insurer and the reinsurer which provides for automatic reinsurance. |
| facultative | Facultative | No | Reinsurance placed on an individual case basis. |

---

### Typelist: RoleType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\RoleType.tti`
**Description:** Defines the role types
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| user | User Role | No | Roles associated with Users |

---

### Typelist: RoomType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\RoomType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\RoomType.ttx`
**Description:** Types of rooms in a property
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| kitchen | Kitchen | No | Kitchen |
| livingroom | Living Room | No | Living Room |
| bedroom | Bedroom | No | Bedroom |
| bathroom | Bathroom | No | Bathroom |
| garage | Garage | No | Garage |
| other | Other | No | Other |

---

### Typelist: RuleActionKey

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\RuleActionKey.tti`
**Description:** Key to a RuleAction
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| *(None defined)* | *Dynamic or database-driven* | No | Typelist populated dynamically at runtime or via database table |

---

### Typelist: RuleBooleanOperator

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\RuleBooleanOperator.tti`
**Description:** RuleBooleanOperator
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| AND | AND | No | AND |
| OR | OR | No | OR |

---

### Typelist: RuleConditionType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\RuleConditionType.tti`
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

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\RuleContextDefinitionKey.tti`
**Description:** Key to a RuleContextDefinition
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| *(None defined)* | *Dynamic or database-driven* | No | Typelist populated dynamically at runtime or via database table |

---

### Typelist: RuleExecutionStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\RuleExecutionStatus.tti`
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

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\RuleImportSide.tti`
**Description:** Existing or Importing rule version of a RuleImportEntry to use as a new head version
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Existing | Existing | No | An existing rule version |
| Importing | New | No | An importing rule version |

---

### Typelist: RuleImportStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\RuleImportStatus.tti`
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

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\RuleOperator.tti`
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

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\RuleSetType.tti`
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

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\RuleStatus.tti`
**Description:** Business Rule Status
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| draft | Draft | No | The rule is being developed |
| staged | Staged | No | The rule is being tested |
| approved | Approved | No | The rule is approved for production |

---

### Typelist: RuntimePropertyGroup

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\RuntimePropertyGroup.tti`
**Description:** Grouping for RuntimeProperty entities
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| configuration | Configuration | No | General configuration properties. |
| integration | Integration | No | General integration properties. |

---

### Typelist: SalvageStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\SalvageStatus.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\SalvageStatus.ttx`
**Description:** Salvage status - for example in review, open or closed
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| in_review | In review | No | Salvage is in review |
| open | Open | No | Salvage is open |
| closed | Closed | No | Salvage is closed |

---

### Typelist: SampleColor

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\SampleColor.tti`
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

### Typelist: SampleTheme

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\SampleTheme.tti`
**Description:** Sample color theme
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| cold | Cold | No | Cold color |
| warm | Warm | No | Warm color |

---

### Typelist: ScriptParameterType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ScriptParameterType.tti`
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

### Typelist: SearchContactType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\SearchContactType.tti`
**Description:** Mirrors the contact subtypes
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| person | Person | No | Person |
| company | Company | No | Company |

---

### Typelist: SearchObjectType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\SearchObjectType.tti`
**Description:** The type of search
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| *(None defined)* | *Dynamic or database-driven* | No | Typelist populated dynamically at runtime or via database table |

---

### Typelist: SecContributingFactors

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\SecContributingFactors.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\SecContributingFactors.ttx`
**Description:** Second column of Contributing factors array
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Weather | Weather conditions | No | Weather conditions |
| RoadSurface | Road surface condition | No | Road surface condition |
| LightCond | Light conditions | No | Light conditions |
| Visibility | Visibility | No | Visibility |
| HwyType | Highway type | No | Highway type |
| HoursOnDuty | Hours on duty | No | Hours on duty |
| DaysOnDuty | Days on duty | No | Days on duty |
| Milesph | MPH over limit | No | MPH over limit |
| Housekeeping | Housekeeping | No | Housekeeping |
| Storage | Storage | No | Storage |
| PhysFeatures | Physical features | No | Physical features |
| Discovery | Discovery | No | Discovery |
| Instructions | Instructions | No | Instructions |
| MarketingSales | Marketing/sales | No | Marketing/sales |
| Warnings | Warnings | No | Warnings |
| NonFood | Non-food | No | Non-food |
| Food | Food | No | Food |
| SurfaceArea | Surface area | No | Surface area |
| ObjectSub | Object Substance | No | Object Substance |
| ProtectFact | Protection factors | No | Protection factors |
| UseApp | Use/application | No | Use/application |
| NotApplic | Not applicable | No | Not applicable |
| LegalOblig | Legal obligations | No | Legal obligations |

---

### Typelist: ServiceRequestInvoiceStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ServiceRequestInvoiceStatus.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ServiceRequestInvoiceStatus.ttx`
**Description:** Status of a service invoice
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| waitingforapproval | Waiting for Approval | No | Invoice received, waiting for approval |
| approved | Approved | No | Invoice has been approved but not yet paid |
| rejected | Rejected | No | Invoice was rejected |
| checkcreated | Check Created | No | Check was created and associated with the invoice |
| withdrawn | Withdrawn | No | Invoice was withdrawn |

---

### Typelist: ServiceRequestKind

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ServiceRequestKind.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ServiceRequestKind.ttx`
**Description:** Kind of service
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| quoteandservice | Quote and Perform Service | No | Request Type for a Service that manages a quote, service performed, and invoices received. |
| quoteonly | Quote Only | No | Request Type for a Service that manages only a quote. |
| serviceonly | Perform Service | No | Request Type for a Service that manages the service performed and invoices received. |
| unmanaged | Unmanaged Service | No | Request Type for a Service that manages only the invoices received. |

---

### Typelist: ServiceRequestMessageType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ServiceRequestMessageType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ServiceRequestMessageType.ttx`
**Description:** Service message type
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| info | Information | No | Message that is informational |
| question | Question | No | Message that requires a response answer |

---

### Typelist: ServiceRequestOperation

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ServiceRequestOperation.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ServiceRequestOperation.ttx`
**Description:** State transitions for all kinds of service requests
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| submitinstruction | Submit Instruction | No | Submit Instruction |
| specialistacceptedwork | Vendor Accepted Work | No | Vendor Accepted Work |
| addquote | Add Quote | No | Add Quote |
| approvequote | Approve Quote | No | Approve Quote |
| specialistcompletedwork | Vendor Completed Work | No | Vendor Completed Work |
| addinvoice | Add Invoice | No | Add Invoice |
| requestrequote | Request Requote | No | Request Requote |
| specialistwaiting | Vendor Waiting | No | Vendor Waiting |
| specialistresumedwork | Vendor Resumed Work | No | Vendor Resumed Work |
| updatequoteecd | Update Quote ECD | No | Update Quote ECD |
| updateserviceecd | Update Service ECD | No | Update Service ECD |
| specialistdeclined | Vendor Declined | No | Vendor Declined |
| cancelservicerequest | Cancel Service | No | Cancel Service |
| specialistcanceled | Vendor Canceled Service | No | Vendor Canceled Service |
| approveinvoice | Approve Invoice | No | Approve Invoice |
| payinvoice | Pay Invoice | No | Pay Invoice |
| rejectinvoice | Reject Invoice | No | Reject Invoice |
| withdrawinvoice | Withdraw Invoice | No | Withdraw Invoice |
| unpayinvoice | Unpay Invoice | No | Unpay Invoice |

---

### Typelist: ServiceRequestProgress

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ServiceRequestProgress.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ServiceRequestProgress.ttx`
**Description:** Progress of a service
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| requested | Requested | No | Service request has been sent to the selected vendor, and has been acknowledged |
| declined | Declined | No | The vendor has declined to accept the service request |
| specialistwaiting | Vendor Waiting | No | Vendor is blocked |
| inprogress | In Progress | No | The vendor is authorized to perform the work |
| workcomplete | Work Complete | No | The work has been completed |
| canceled | Canceled | No | The service request has been canceled |
| draft | Draft | No | The service is still being edited and has not yet been sent to the vendor |
| expired | Expired | No | The service has expired |

---

### Typelist: ServiceRequestQuoteStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ServiceRequestQuoteStatus.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ServiceRequestQuoteStatus.ttx`
**Description:** Status of a service quote
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| waitingforapproval | Waiting for Approval | No | Quote received and waiting for approval |
| waitingforquote | Waiting for Quote | No | Service is waiting to be quoted |
| approved | Approved | No | Quote has been approved |
| noquote | No Quote | No | Service does not have a quote |
| quoted | Quoted | No | Quote has been received |

---

### Typelist: ServiceRequestStatementLineItemCategory

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ServiceRequestStatementLineItemCategory.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ServiceRequestStatementLineItemCategory.ttx`
**Description:** Category of the ServiceRequestStatementLineItem
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| inspection | Inspection | No | Inspection |
| parts | Parts | No | Parts |
| labor | Labor | No | Labor |
| towing | Towing | No | Towing |
| CourtCosts | Court costs | No | Court costs |
| Deposition | Deposition | No | Deposition |
| Hearing | Hearing | No | Hearing |
| Investigation | Investigation | No | Investigation |
| chiro | Chiropractor | No | Chiropractor |
| diagnostic | X-ray/diagnostic | No | X-ray/diagnostic |
| doctor | Doctor | No | Doctor's care |
| pt | Physical therapy | No | Physical therapy |
| hospital | Hospital | No | Hospital |
| other | Other | No | Other |

---

### Typelist: ServiceRequestTier

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ServiceRequestTier.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ServiceRequestTier.ttx`
**Description:** ServiceRequestTier
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| high | High | No | High |
| medium | Medium | No | Medium |
| low | Low | No | Low |

---

### Typelist: SettlementSpeed

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\SettlementSpeed.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\SettlementSpeed.ttx`
**Description:** Speed of settlement desired for question sets
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 0 | Over one week? | No | Over one week? |
| 5 | Four to seven days? | No | Four to seven days? |
| 10 | Less than four days? | No | Less than four days? |

---

### Typelist: SettleMethod

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\SettleMethod.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\SettleMethod.ttx`
**Description:** Method of settling medical payment
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| lumpsum | Lump sum | No | Lump sum |
| lumpsumother | Other than lump sum | No | Other than lump sum |
| stipaward | Stipulated award | No | Stipulated award (carrier/claimant settlement) |
| dismissal | Dismissal | No | Dismissal or take nothing |
| cacompromise | CA compromise | No | CA Compromise and release |
| other | Other | No | Other |

---

### Typelist: SeverityType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\SeverityType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\SeverityType.ttx`
**Description:** The severity of the exposure
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| minor | Minor | No | Minor |
| moderate-gen | Moderate | No | Moderate |
| moderate-auto | Moderate (drivable) | No | Moderate (drivable) |
| moderate-prop | Moderate (usable) | No | Moderate (usable) |
| major-gen | Major | No | Major |
| major-auto | Major (not drivable) | No | Major (not drivable) |
| major-prop | Major (not usable) | No | Major (not usable) |
| major-injury | Major (hospitalization) | No | Major (hospitalization) |
| severe-gen | Severe | No | Severe |
| severe-auto | Possible total loss | No | Possible total loss |
| severe-injury | Life-threatening | No | Life-threatening |
| td | Temporary disability | No | Temporary disability |
| pd | Permanent disability | No | Permanent disability |
| fatal | Death | No | Fatal |
| medical_only | Became medical only | No | Became medical only |
| perm-total | Permanent total | No | Permanent total |
| temporary | Temporary | No | Temporary |
| contract-medical | Contract medical | No | Contract medical |
| wc-ell | Employer liability | No | Employer liability |

---

### Typelist: ShapeType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ShapeType.tti`
**Description:** type of a geographic shape
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| bbox | bbox | No | Bounding Box |
| polygon | polygon | No | Polygon |
| region | region | No | Region, a set of multiple sub-shapes |

---

### Typelist: SideOfBody

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\SideOfBody.tti`
**Description:** Side Of Body
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| left | Left | No | Left side of Body |
| right | Right | No | Right side of body |
| both | Both | No | Both sides of body |

---

### Typelist: SIUStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\SIUStatus.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\SIUStatus.ttx`
**Description:** Special Investigation Unit status - used if claim is under investigation
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| No_Referral | No referral | No | No SIU referral |
| Under_Investigation | Under investigation | No | Under investigation with SIU |
| Investigation_Closed | Investigation closed | No | SIU closed investigation |

---

### Typelist: SortByRange

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\SortByRange.tti`
**Description:** Possible values to sort notes by
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| author | Author | No | Sort by Author |
| date | Date | No | Sort by Date |
| subject | Subject | No | Sort by Subject |
| topic | Topic | No | Sort by Topic |

---

### Typelist: SpecialistCommMethod

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\SpecialistCommMethod.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\SpecialistCommMethod.ttx`
**Description:** A channel through which specialists can communicate with the carrier
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| gwportal | Guidewire Portal | No | Guidewire Portal |
| otherportal | Third-party Portal | No | Third-party Portal |
| fax | Fax | No | Fax |
| phone | Phone | No | Phone |

---

### Typelist: SpecialtyType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\SpecialtyType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\SpecialtyType.ttx`
**Description:** Doctor specialties
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| allergy | Allergy | No | Allergy |
| anesthesiology | Anesthesiology | No | Anesthesiology |
| cardiology | Cardiology | No | Cardiology |
| dermatology | Dermatology | No | Dermatology |
| emergencymed | Emergency Medicine | No | Emergency Medicine |
| endocrinology | Endocrinology | No | Endocrinology |
| ent | ENT | No | ENT |
| familypractice | Family Practice | No | Family Practice |
| gastroenterology | Gastroenterology | No | Gastroenterology |
| hematologyonc | Hematalogy/Oncology | No | Hematalogy/Oncology |
| hospitalist | Hospitalist | No | Hospitalist |
| infectiousdis | Infectious Disease | No | Infectious Disease |
| internalmed | Internal Medicine | No | Internal Medicine |
| medpeds | Med/Peds | No | Med/Peds |
| nephrology | Nephrology | No | Nephrology |
| neurology | Neurology | No | Neurology |
| obgyn | Obstetrics/Gynecology | No | Obstetrics/Gynecology |
| occupationalmed | Occupational Medicine | No | Occupational Medicine |
| opthalmology | Opthalmology | No | Opthalmology |
| pathology | Pathology | No | Pathology |
| physmedrehab | Physical Medicine/Rehabilitation | No | Physical Medicine/Rehabilitation |
| plasticsurgery | Plastic Surgery | No | Plastic Surgery |
| psychiatry | Psychiatry | No | Psychiatry |
| pulmcritcare | Pulmonary/Critical Care | No | Pulmonary/Critical Care |
| surgery | Surgery | No | Surgery |
| chiropractic | Chiropractic | No | Chiropractic |
| orthopedics | Orthopedics | No | Orthopedics |
| dental | Dental | No | Dental |

---

### Typelist: SQLStatementType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\SQLStatementType.tti`
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

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\StartPointType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\StartPointType.ttx`
**Description:** The different fields on an activity or claim that could be used as the starting point for another date field
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| activitycreation | Activity creation date | No | Creation date of the activity |
| startdate | Activity start date | No | Start date on activity |
| claimnotice | Claim notice date | No | Notice date on the claim |
| lossdate | Claim loss date | No | Loss date on the claim |

---

### Typelist: StartupPage

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\StartupPage.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\StartupPage.ttx`
**Description:** The startup page for the user
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| DesktopActivities | Desktop: Activities | No | My Activities in Desktop |
| DesktopClaims | Desktop: Claims | No | My Claims in Desktop |
| DesktopExposures | Desktop: Exposures | No | My Exposures in Desktop |
| AwaitingAssignment | Desktop: Pending Assignments | No | My Pending Assignments in Desktop |
| Team | Team | No | Team |
| ClaimSearch | Search Claims | No | Search Claims |
| NewClaim | New Claim Wizard | No | New Claim Wizard |
| Admin | Administration | No | Administration |
| Dashboard | Dashboard | No | Dashboard |

---

### Typelist: State

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\State.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\State.ttx`
**Description:** States such as in AU, CA, JP, US
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

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
| VI | Virgin Islands | No | Virgin Islands |
| MP | Northern Mariana Islands | No | Northern Mariana Islands |
| MH | Marshall Islands | No | Marshall Islands |
| GU | Guam | No | Guam |
| FM | Federated States of Micronesia | No | Federated States of Micronesia |
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
| AU_SA | South Australia | No | South Australia |
| AU_NT | Northern Territory | No | Northern Territory |
| AU_QLD | Queensland | No | Queensland |
| AU_NSW | New South Wales | No | New South Wales |
| AU_VIC | Victoria | No | Victoria |
| AU_WA | Western Australia | No | Western Australia |
| AU_TAS | Tasmania | No | Tasmania |
| AU_ACT | A.C.T. | No | Australian Capital Territory |
| AU_JBT | Jervis Bay Territory | No | Jervis Bay Territory |
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

---

### Typelist: StateAbbreviation

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\StateAbbreviation.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\StateAbbreviation.ttx`
**Description:** Abbreviations for states such as in AU, CA, JP, US
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

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

### Typelist: StatementSource

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\StatementSource.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\StatementSource.ttx`
**Description:** StatementSource
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| manual | Manual Entry | No | Manual Entry |
| gwportal | Guidewire Portal | No | Guidewire Portal |

---

### Typelist: StatuteLimitationsType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\StatuteLimitationsType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\StatuteLimitationsType.ttx`
**Description:** 
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| federal | Federal Involved | No | Federal statute |
| state | State Involved | No | State statute |
| City | City Involved | No | City statute |
| medical | Medical | No | Medical |
| damage | Damage | No | Damage |
| other | Other | No | Other |

---

### Typelist: StorageCategory

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\StorageCategory.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\StorageCategory.ttx`
**Description:** Storage category
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| prop_cas | Property/casualty | No | Property/casualty |
| work_comp | Workers' Compensation | No | Workers' Compensation |
| health_acc | Health & accident | No | Health & accident |
| tpa | Third-party administrator | No | Third-party administrator |
| other | Other | No | Other |

---

### Typelist: StorageType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\StorageType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\StorageType.ttx`
**Description:** Storage type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| inhouse | In house | No | In house |
| destroyed | Destroyed | No | Destroyed |
| storage | Storage facility | No | Storage facility |

---

### Typelist: StringCriterionMode

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\StringCriterionMode.tti`
**Description:** The mode of a String restriction
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Equals | Equals | No | Useful in flagging whether String restrictions should be implemented with compareEquals. This performs most quickly. |
| StartsWith | StartsWith | No | Useful in flagging whether String restrictions should be implemented with compareStartsWith. This performs moderately quickly. |
| Contains | Contains | No | Useful in flagging whether String restrictions should be implemented with compareContains. This performs most slowly. |

---

### Typelist: SubroClassification

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\SubroClassification.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\SubroClassification.ttx`
**Description:** 
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| uninsured | Uninsured | No | Uninsured |
| insured | Insured | No | Insured |

---

### Typelist: SubroClosedOutcome

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\SubroClosedOutcome.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\SubroClosedOutcome.ttx`
**Description:** SubroCloseOutcome
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| full | Full Recovery | No | Full Recovery |
| compromised | Compromised | No | Compromised |
| uncollectable | Uncollectable | No | Uncollectable |
| discontinued | Discontinued | No | Discontinued |
| notpursued | Not Pursued | No | Not Pursued |

---

### Typelist: SubrogationStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\SubrogationStatus.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\SubrogationStatus.ttx`
**Description:** Status of subrogations
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| closed | Closed | No | Closed |
| review | In Review | No | Evaluation recovery opportunity |
| open | Open | No | Pursuing recovery |

---

### Typelist: SubroGovernmentInvolved

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\SubroGovernmentInvolved.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\SubroGovernmentInvolved.ttx`
**Description:** Used to track if governental entities are Subro Adverse Targets
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| nongov | No | No | Not applicable to governental entities |
| gov | Yes | No | Applicable to Governental entities |

---

### Typelist: SubroSchedRecoveryType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\SubroSchedRecoveryType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\SubroSchedRecoveryType.ttx`
**Description:** Type of scheduled but yet to be paid Recovery
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| promissory | Promissory Note | No | Promissory Note |
| arbsettlement | Arbitration Settlement | No | Arbitration Settlement |

---

### Typelist: SubroStrategy

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\SubroStrategy.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\SubroStrategy.ttx`
**Description:** 
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| pursueins | Pursue against Insurer | No | Pursue against Insurer |
| negotiate | Negotiate against Insurer | No | Negotiate against Insurer |
| arbitrate | Arbitration | No | Arbitration |
| pursue | Pursue | No | Pursue |
| collection | Utilize Collection Agency | No | Collection Agency |
| lawsuit | Lawsuit | No | Lawsuit |
| drop | Drop Pursuit | No | Drop Pursuit |

---

### Typelist: SuitType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\SuitType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\SuitType.ttx`
**Description:** Legal suit type.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Insured | Insured | No | Insured |
| ThirdParty | Third-party | No | Third-party |
| FirstParty | First-party | No | First-party |

---

### Typelist: SynchState

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\SynchState.tti`
**Description:** Sync states for claims and exposures
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| unsynched | unsynched | No | Object is unsynced |
| synch_sent | synch_sent | No | Object is sync_sent (first message has been generated) |

---

### Typelist: SystemPermissionType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\SystemPermissionType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\SystemPermissionType.ttx`
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
| actown | Own activity | No | Permission to own an activity and to see the Desktop Activities page |
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
| ownsensclaim | Own sensitive claims | No | Permission to own sensitive claims |
| ownsensclaimsub | Own sensitive claim subobjects | No | Permission to own subobjects on sensitive claims |
| viewsensdoc | View sensitive documents | No | Permission to view a sensitive document |
| editsensdoc | Edit sensitive documents | No | Permission to edit a sensitive document |
| delsensdoc | Delete sensitive documents | No | Permission to delete a sensitive document |
| viewprivnote | View private note | No | Permission to view a private note |
| editprivnote | Edit private note | No | Permission to edit a private note |
| delprivnote | Delete private note | No | Permission to delete a private note |
| viewsensnote | View sensitive note | No | Permission to view a sensitive note |
| editsensnote | Edit sensitive note | No | Permission to edit a sensitive note |
| delsensnote | Delete sensitive note | No | Permission to delete a sensitive note |
| viewmednote | View medical note | No | Permission to view a medical note |
| editmednote | Edit medical note | No | Permission to edit a medical note |
| delmednote | Delete medical note | No | Permission to delete a medical note |
| viewSensSIUdetails | View sensitive SIU details | No | Permission to view sensitive SIU details |
| editSensSIUdetails | Edit sensitive SIU details | No | Permission to edit sensitive SIU details |
| viewSensMCMdetails | View sensitive Med Case Mgmt details | No | Permission to view sensitive Medical Case Management details |
| editSensMCMdetails | Edit sensitive Med Case Mgmt details | No | Permission to edit sensitive Medical Case Management details |
| StorageUpdate | Edit claim storage information | No | Permission to edit claim storage information |
| viewsubrodetails | View Subrogation details | No | Permission to view Subrogation-related information |
| editsubrodetails | Edit Subrogation details | No | Permission to edit Subrogation-related information |
| report_user | Show reports | No | Permission to view reports in report server |
| report_manager | Show reports and dashboard | No | Permission to view reports and dashboard in report server |
| viewrefdata | View reference data | No | Permission to view administration reference data |
| editrefdata | Edit reference data | No | Permission to edit administration reference data |
| viewpolicysystem | View policy system | No | Permission to view policy in policy system |
| riedit | Edit RI transactions & agreements | No | Permission to edit RI transactions & agreements |
| riview | View RI transactions & agreements | No | Permission to view RI transactions & agreements |
| verifyFNOL | Verify FNOLs (Obsolete) | Yes | (Obsolete) |

---

### Typelist: SystemUserType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\SystemUserType.tti`
**Description:** Types of special system users
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| sysadmin | system administrator | No | The system administrator |
| defaultowner | default owner | No | A special user that accepts failed or unresolved assignments |
| sysservices | system services | No | A daemon user that executes system services like escalation |

---

### Typelist: TableUpdateStatsType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\TableUpdateStatsType.tti`
**Description:** Type of process running update statistics
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Table | Table | No | Table Update Statistics Statements |
| Index | Index | No | Index Update Statistics Statements |
| Histogram | Histogram | No | Histogram Update Statistics Statements |

---

### Typelist: TAccountType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\TAccountType.tti`
**Description:** The type of a specific TAccount for a ReserveLine
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| stagingcashin | Staging cash in | No | Staging cash in T-account |
| stagingcashout | Staging cash out | No | Staging cash out T-account |
| stagingexpenses | Staging expenses | No | Staging expenses T-account |
| draftpayments | Draft payments | No | Draft payments T-account |
| pendappnonerodingpmts | Pending approval non-eroding payments | No | Pending approval non-eroding payments T-account |
| pendapperodingpmts | Pending approval eroding payments | No | Pending approval eroding payments T-account |
| pendingappreserves | Pending approval reserves | No | Pending approval reserves T-account |
| pendingapprecreserves | Pending approval recovery reserves | No | Pending approval recovery reserves T-account |
| pendingapprecoveries | Pending approval recoveries | No | Pending approval recoveries T-account |
| futureerodingpmts | Future eroding payments | No | Future eroding payment T-account |
| futurenonerodingpmts | Future non-eroding payments | No | Reserves auto-created to offset future non-eroding payments |
| awserodingpmts | Awaiting submission eroding payments | No | Awaiting submission eroding payments T-account |
| awsnonerodingpmts | Awaiting submission non-eroding payments | No | Non-eroding awaiting submission payments T-account |
| committednonerodepmts | Committed non-eroding payments | No | Committed non-eroding payments T-account |
| committederodepmts | Committed eroding payments | No | Committed eroding payments T-account |
| pendingcashout | Pending cash out | No | Pending cash out T-account |
| pendingexpense | Pending expense | No | Pending expense T-account |
| pendingreserves | Pending reserves | No | Pending reserves T-account |
| claimexpenses | Claim expenses | No | Claim expenses T-account |
| reserves | Reserves | No | Submitted reserves T-account |
| recoveryreserves | Recovery reserves | No | Submitted recovery reserves T-account |
| recoveries | Recoveries | No | Submitted recoveries T-account |
| cashout | Cash Out | No | Cash out T-account |
| cashin | Cash In | No | Cash in T-account |
| erodingforexchange | Eroding Payments Foreign Exchange | No | T-account to hold foreign exchange adjustments for eroding payments |
| nonerodingforexchange | Non-Eroding Payments Foreign Exchange | No | T-account to hold foreign exchange adjustments for non-eroding payments |
| cmtdnonadjcededres | Committed non-adjustment RI Ceded Reserves | No | Non-adjustment RICededReserve transactions sent downstream. |
| cmtdadjcededres | Committed adjustment RI Ceded Reserves | No | Adjustment RICededReserve transactions sent downstream. |
| cededreservesout | Committed RI Ceded Reserves | No | Total RICededReserve transactions sent downstream. |
| cmtdnonadjrecoverable | Committed non-adjustment RI Recoverables | No | Non-adjustment RIRecoverable transactions sent downstream. |
| cmtdadjrecoverable | Committed adjustment RI Recoverable | No | Adjustment RIRecoverable transactions sent downstream. |
| recoverablesout | Committed RI Recoverable | No | Total RIRecoverable transactions sent downstream. |

---

### Typelist: TaxFilingStatusType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\TaxFilingStatusType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\TaxFilingStatusType.ttx`
**Description:** State-specific field
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| single | Single | No | Single |
| married-joint | Married filing jointly | No | Married filing jointly |
| married-separate | Married filing separately | No | Married filing separately |
| headofhousehold | Head of household | No | Head of household |
| widow | Qualifying widow(er) with dependent child | No | Qualifying widow(er) with dependent child |

---

### Typelist: TaxStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\TaxStatus.tti`
**Description:** The status of a vendor's tax ID
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| unknown | Unknown | No | Unknown |
| unconfirmed | Unconfirmed | No | Known, but not yet verified |
| confirmed | Confirmed | No | Known and verified |

---

### Typelist: TimeZoneType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\TimeZoneType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\TimeZoneType.ttx`
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

### Typelist: TransactionLifeCycleState

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\TransactionLifeCycleState.tti`
**Description:** Internal status of a TAccountTransaction, as opposed to the business status of a transaction represented by the values in the TransactionStatus typelist
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| new | New | No | Transactions in this state are brand new, often with no lineitems yet, and not yet in DRAFT state |
| draft | Draft | No | Transactions in this state have not yet been completed and submitted for approval |
| pendingapproval | Pending approval | No | Transaction is moving through the approval process |
| rejected | Rejected | No | Transaction has been rejected |
| denied | Denied | No | Transaction has been denied |
| futuredated | Future dated | No | Valid only for future dated payments |
| awaitingsubmission | Awaiting submission | No | Transaction is waiting to be submitted to the downstream system |
| committed | Committed | No | Transaction has been committed and is no longer editable |
| retired | Retired | No | Transaction has been retired |

---

### Typelist: TransactionStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\TransactionStatus.tti`
**Description:** The status of a transaction, from draft through approval to submission
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| draft | Draft | No | Draft; not yet submitted to a back-end accounting system |
| pendingapproval | Pending approval | No | Pending approval |
| awaitingsubmission | Awaiting submission | No | Awaiting for the send date to arrive, at which point the status will change to Submitting (applicable only to payments) |
| submitting | Submitting | No | In the process of being submitted to the accounting system |
| requesting | Requesting | No | In the process of being requested from the accounting system (applicable only to checks) |
| submitted | Submitted | No | Submitted to the accounting system |
| requested | Requested | No | Requested of the accounting system (applicable only to checks) |
| rejected | Rejected | No | Rejected by the user assigned to approve the transaction |
| denied | Denied | No | Denied by the downstream system |
| pendingvoid | Pending void | No | A void transaction request is pending (applicable only to payments and recoveries) |
| voided | Voided | No | The transaction is voided (applicable only to payments and recoveries) |
| pendingstop | Pending stop | No | A stop payment request is pending (applicable only to payments) |
| stopped | Stopped | No | A stop payment has been issued for this payment's check (applicable only to payments) |
| issued | Issued | No | Check has been issued |
| cleared | Cleared | No | Check has cleared |
| pendingrecode | Pending recode | No | Transaction that is pending recode |
| recoded | Recoded | No | Transaction that is recoded |
| pendingtransfer | Pending transfer | No | Transaction that is pending transfer from one claim to another claim |
| transferred | Transferred | No | Transaction that is transferred from one claim to another claim |
| notifying | Notifying | No | In the process of notifying the accounting system of a new manual check |

---

### Typelist: TransportType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\TransportType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\TransportType.ttx`
**Description:** Types of transport
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| other | Other | No | Other |
| airline | Airline | No | Airline |
| bus | Bus | No | Bus |
| cruise_ship | Cruise ship | No | Cruise ship |
| taxi | Taxi | No | Taxi |
| rental_car | Rental car | No | Rental car |

---

### Typelist: TreatmentOutcome

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\TreatmentOutcome.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\TreatmentOutcome.ttx`
**Description:** Medical Treatment Outcome - for use on MedCaseMgr screen
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| RTW-FT-PIO | RTW FT pre-injury occupation | No | Return-to-work full-time pre-injury ccupation |
| RTW-FT-MD | RTW FT modified duties | No | Return-to-work full-time modified duties |
| RTW-PT-PIO | RTW PT pre-injury occupation | No | Return-to-work part-time pre-injury occupation |
| RTW-PT-MD | RTW PT modified duties | No | Return-to-work part-time modified duties |
| UnfitForWork | Still unfit for work | No | Still unfit for work |
| AW-RT | At work, but receiving treatment | No | At work, but receiving treatment |

---

### Typelist: TriggeringPointKey

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\TriggeringPointKey.tti`
**Description:** Unique key identifying a TriggeringPoint, used when invoking Business Rules
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| *(None defined)* | *Dynamic or database-driven* | No | Typelist populated dynamically at runtime or via database table |

---

### Typelist: TypeofProperty

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\TypeofProperty.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\TypeofProperty.ttx`
**Description:** Type of Property
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Building | Building | No | Building |
| Contents | Contents | No | Contents |
| Equipment | Equipment | No | Equipment |
| Cargo | Cargo | No | Cargo |
| Other | Other | No | Other |

---

### Typelist: UnderwritingCompanyType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\UnderwritingCompanyType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\UnderwritingCompanyType.ttx`
**Description:** Lists different legal entities (subsidiaries) that underwrite different types of policies
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| parent | Succeed Insurance Parent Co. | No | The main parent company |
| child1 | Succeed Fire Insurance Co. | No | A separately branded book of business |
| child2 | Southern Mutual Insurance | No | An acquired subsidiary company |

---

### Typelist: UnderwritingGroupType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\UnderwritingGroupType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\UnderwritingGroupType.ttx`
**Description:** Lists different underwriting groups
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| acme_auto | Acme Auto | Yes | Acme Auto |
| succeed_auto | Succeed Auto | No | Succeed Auto |
| acme_prop | Acme Property | Yes | Acme Property |
| succeed_prop | Succeed Property | No | Succeed Property |
| acme_wc | Acme Workers' Comp | Yes | Acme Workers' Comp |
| succeed_wc | Succeed Workers' Comp | No | Succeed Workers' Comp |
| succeed_fire | Succeed Fire | No | Succeed Fire |
| acme_fire | Acme Fire | Yes | Acme Fire |
| southwestern | Southwestern | No | Southwestern |

---

### Typelist: UnitOfDistance

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\UnitOfDistance.tti`
**Description:** Units of distance
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Mile | Mile | No | International statute mile |
| Kilometer | Kilometer | No | Kilometer |
| Meter | Meter | No | Meter |
| Foot | Foot | No | Foot |

---

### Typelist: UpgradeDBStorageSetType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\UpgradeDBStorageSetType.tti`
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

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\UpgradeExecutionTimeType.tti`
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

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\UserAttributeType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\UserAttributeType.ttx`
**Description:** Major categories of attributes
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| default | Default | No | Default |
| Language | Language | No | Language |
| Account | Named account | No | Named account |
| Expertise | Expertise | No | Expertise |

---

### Typelist: UserExperienceType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\UserExperienceType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\UserExperienceType.ttx`
**Description:** Experience levels for users
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| low | Low | No | Novice |
| mid | Mid | No | Average |
| high | High | No | Expert |

---

### Typelist: UserRole

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\UserRole.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\UserRole.ttx`
**Description:** Roles users can have on an assignable object
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| primaryadjuster | Primary Adjuster | Yes | Primary adjuster for the claim |
| relateduser | Related User | No | Other user associated with the claim |
| siuinvestigator | SIU Investigator | No | SIU Investigator associated with the claim |
| supervisor | Supervisor | No | Supervisor associated with the claim |
| attorney | Attorney | No | Attorney associated with the claim |
| vhcleinsp | Vehicle Inspector | No | Vehicle Inspector associated with the claim |
| propinsp | Property Inspector | No | Property Inspector associated with the claim |
| salvgowner | Salvage Owner | No | Salvage Owner associated with the claim |
| doctor | Doctor | No | Doctor associated with the claim |
| vendor | Vendor | No | Vendor associated with the claim |
| reporter | Reporter | No | Reporter associated with the claim |
| repairshop | Repair Shop | No | Repair Shop associated with the claim |
| nursecasemgr | Nurse Case Manager | No | Nurse Case Manager associated with the claim |
| indepappr | Independent Appraiser | No | Independent Appraiser associated with the claim |
| siu | SIU | No | SIU associated with the claim |
| police | Police | No | Police |
| reinsmgr | Reinsurance Manager | No | Reinsurance Manager associated with the claim |

---

### Typelist: UserRoleConstraint

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\UserRoleConstraint.tti`
**Description:** Constraints that can be applied to UserRoles
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| objectowner | ObjectOwner | No | Indicates that the user assigned to this role must have the same permissions that are required to be the owner of the assignable object. |

---

### Typelist: VacationStatusType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\VacationStatusType.tti`
**Description:** Possible vacation statuses for a user
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| atwork | At work | No | The user is at work |
| onvacation | On vacation | No | The user is on vacation |
| inactive | On vacation (Inactive) | No | The user is not available |

---

### Typelist: ValidationIssueType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ValidationIssueType.tti`
**Description:** Validation issues can be errors or warning
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| error | Error | No | A validation error |
| warning | Warning | No | A validation warning |

---

### Typelist: ValidationLevel

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ValidationLevel.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ValidationLevel.ttx`
**Description:** Levels of validation errors and warnings
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| loadsave | Load and save | No | Load and save |
| iso | Valid for ISO | No | Valid for ISO ClaimSearch |
| external | Send to external system | No | Send to external system |

---

### Typelist: VehicleDirection

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\VehicleDirection.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\VehicleDirection.ttx`
**Description:** The direction the vehicle was going at the time of the accident
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| reverse | Backing up | No | Backing up |
| turningleft | Turning left | No | Turning left |
| turningright | Turning right | No | Turning right |
| merge | Merging/changing lanes | No | Merging/changing lanes |
| pass | Passing other vehicle(s) | No | Passing other vehicle(s) |
| oth | Other maneuver | No | Other maneuver |
| straight | Going straight | No | Going straight |
| stop_traffic | Stopped in traffic lane | No | Stopped in traffic lane |
| curve | Negotiating curve | No | Negotiating curve |
| passed | Being passed by other vehicle(s) | No | Being passed by other vehicle(s) |
| start | Starting in traffic lane | No | Starting in traffic lane |
| leave | Leaving parking space | No | Leaving parking space |
| uturn | Making U-turn | No | Making U-turn |
| park | Entering parking space | No | Entering parking space |
| disabled | Disabled in traffic lane | No | Disabled in traffic lane |
| stop_shoulder | Stopped on shoulder of road | No | Stopped on shoulder of road |
| forward | Forward | Yes | Forward |

---

### Typelist: VehicleLineItemCategory

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\VehicleLineItemCategory.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\VehicleLineItemCategory.ttx`
**Description:** Vehicle Incident Assessment Line Item Category
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| body | Body | No | Body |
| brakes | Brakes | No | Brakes |
| electrical | Electrical | No | Electrical |
| engine | Engine | No | Engine |
| fuel | Fuel System | No | Fuel |
| interior | Interior | No | Interior |
| suspension | Suspension | No | Suspension |
| roof | Roof | No | Roof |
| wheels | Wheels | No | Wheels |
| other | Other | No | Other |

---

### Typelist: VehicleManufacturer

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\VehicleManufacturer.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\VehicleManufacturer.ttx`
**Description:** Manufacturer, for example GMC/Ford/Chrysler.
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| ACUR | Acura | No | Acura |
| ALFA | Alfa Romeo | No | Alfa Romeo |
| ALIE | Allied | No | Allied |
| ALIS | Allis-Chalmers | No | Allis-Chalmers |
| ALKO | Alois Kober (AL-KO) | No | Alois Kober (AL-KO) |
| ALUE | Alouette Recreational Products, Ltd. | No | Alouette Recreational Products, Ltd. |
| AMGN | AM General Corp (Hummer) | No | AM General Corp (Hummer) |
| ARCA | Arctic Cat | No | Arctic Cat |
| ARCC | Arctic Enterprises | No | Arctic Enterprises |
| ARLB | Arlberg | No | Arlberg |
| ASTO | Aston Martin | No | Aston Martin |
| ATV | Other ATV | No | Other ATV |
| AUDI | Audi | No | Audi |
| AUTS | Auto Ski, Inc. | No | Auto Ski, Inc. |
| BENT | Bentley | No | Bentley |
| BMBR | Bombardier, Inc. | No | Bombardier, Inc. |
| BMW | BMW | No | BMW |
| BOAS | Boa-Ski Airport, Ltd. | No | Boa-Ski Airport, Ltd. |
| BOAT | Boatel Ski | No | Boatel Ski |
| BOMB | Bombardier | No | Bombardier |
| BRUZ | Brutanza Engineering, Inc. | No | Brutanza Engineering, Inc. |
| BUIC | Buick | No | Buick |
| CADI | Cadillac | No | Cadillac |
| CHEV | Chevrolet | No | Chevrolet |
| CHOC | Chrysler Outboard Corp. | No | Chrysler Outboard Corp. |
| CHPR | Chaparral Inds., Inc. | No | Chaparral Inds., Inc. |
| CHRY | Chrysler | No | Chrysler |
| CITR | Citroen | No | Citroen |
| CSHM | Cushman | No | Cushman |
| DAEW | Daewoo | No | Daewoo |
| DAIH | Daihatsu | No | Daihatsu |
| DATS | Datsun | No | Datsun |
| DAUP | Dauphin | No | Dauphin |
| DODG | Dodge | No | Dodge |
| FEMC | Feldman Engineering & Mfg., Co. | No | Feldman Engineering & Mfg., Co. |
| FERR | Ferrari | No | Ferrari |
| FIAT | Fiat | No | Fiat |
| FORD | Ford | No | Ford |
| FRED | Frederick-Willys | No | Frederick-Willys |
| GBCO | Gilson Brothers Co. | No | Gilson Brothers Co. |
| GEO | GEO | No | GEO |
| GM | General Motors | No | General Motors |
| GMC | General Motors Corp. | No | General Motors Corp. |
| HDMC | Harley-Davidson Motor Co., Inc. | No | Harley-Davidson Motor Co., Inc. |
| HOND | Honda | No | Honda |
| HRTI | Herters, Inc. | No | Herters, Inc. |
| HURU | Hustler-Rustler | No | Hustler-Rustler |
| HYUN | Hyundai | No | Hyundai |
| INFI | Infiniti | No | Infiniti |
| ISU | Isuzu | No | Isuzu |
| JACC | Jac-Trac, Inc. | No | Jac-Trac, Inc. |
| JAGU | Jaguar | No | Jaguar |
| JDER | Deere & Co. | No | Deere & Co. |
| KAWK | Kawasaki | No | Kawasaki |
| KIA | Kia Motors Corp. | No | Kia Motors Corp. |
| KMCU | Kawasaki Motors Corp., USA | No | Kawasaki Motors Corp., USA |
| KOME | Moto Kometik, Inc. | No | Moto Kometik, Inc. |
| LAMO | Lamborghini | No | Lamborghini |
| LARV | Larvin | No | Larvin |
| LEXS | Lexus | No | Lexus |
| LINC | Lincoln-Continental | No | Lincoln-Continental |
| LIOL | Lional Enterprises, Inc. | No | Lional Enterprises, Inc. |
| LNDR | Land Rover | No | Land Rover |
| LOTU | Lotus | No | Lotus |
| LSKP | Lori Engineering Corp. | No | Lori Engineering Corp. |
| MALR | Mallard | No | Mallard |
| MASE | Maserati | No | Maserati |
| MAYB | Maybach | No | Maybach |
| MAZD | Mazda | No | Mazda |
| MERC | Mercury | No | Mercury |
| MERZ | Mercedes-Benz | No | Mercedes-Benz |
| MG | MG | No | MG |
| MITS | Mitsubishi | No | Mitsubishi |
| MNTA | Three R Inds., Inc. | No | Three R Inds., Inc. |
| MOWA | Montgomery Ward | No | Montgomery Ward |
| MRCU | Mercury Marine | No | Mercury Marine |
| MSFI | Massey-Ferguson, Inc. | No | Massey-Ferguson, Inc. |
| NISS | Nissan | No | Nissan |
| NRTS | Northway Snowmobiles | No | Northway Snowmobiles |
| OCKE | Ockelbo Ind. AB | No | Ockelbo Ind. AB |
| ODGL | Ontario Drive & Gear, Ltd. | No | Ontario Drive & Gear, Ltd. |
| OLDS | Oldsmobile | No | Oldsmobile |
| ORIG | Original Equipment Mfg., Ltd. | No | Original Equipment Mfg., Ltd. |
| OTPE | Outdoor Power Equipment | No | Outdoor Power Equipment |
| OUTM | Outboard Marine Corp. | No | Outboard Marine Corp. |
| PANH | Panhard | No | Panhard |
| PEUG | Peugeot | No | Peugeot |
| PLRN | Poloron | No | Poloron |
| PLYC | Playcat Inds., Inc. | No | Playcat Inds., Inc. |
| PLYM | Plymouth | No | Plymouth |
| POLB | Raybon Mfg. Co. | No | Raybon Mfg. Co. |
| POLS | Polaris Inds., Inc. | No | Polaris Inds., Inc. |
| PONT | Pontiac | No | Pontiac |
| PORS | Porsche | No | Porsche |
| RAID | Leisure Vehicles, Inc. | No | Leisure Vehicles, Inc. |
| RENA | Renault | No | Renault |
| ROL | Rolls-Royce | No | Rolls-Royce |
| ROLF | Roll-O-Flex, Ltd. | No | Roll-O-Flex, Ltd. |
| RPII | H & H Snowmobiles | No | H & H Snowmobiles |
| SAA | Saab | No | Saab |
| SCRP | Scorpion, Inc. | No | Scorpion, Inc. |
| SKIR | Skiroule, Ltd. | No | Skiroule, Ltd. |
| SNOJ | Sno*Jet, Inc. | No | Sno*Jet, Inc. |
| SNOW | Snowmobile | No | Snowmobile |
| SPPI | Speedway Products, Inc. | No | Speedway Products, Inc. |
| SRCO | Sears | No | Sears |
| STCO | Starcraft Corp. | No | Starcraft Corp. |
| STRN | Saturn | No | Saturn |
| SUBA | Subaru | No | Subaru |
| SUZI | Suzuki | No | Suzuki |
| SUZU | Suzulight Su | No | Suzulight Su |
| TOYT | Toyota | No | Toyota |
| TRIU | Triumph | No | Triumph |
| TSCC | Tucker Sno-Cat Corp. | No | Tucker Sno-Cat Corp. |
| TTII | T & T Inds., Inc. | No | T & T Inds., Inc. |
| USSM | U.S. Suzuki Motor Corp., Ltd. | No | U.S. Suzuki Motor Corp., Ltd. |
| VKNG | Viking Snowmobiles, Inc. | No | Viking Snowmobiles, Inc. |
| VOLK | Volkswagen | No | Volkswagen |
| VOLV | Volvo | No | Volvo |
| YAMA | Yamaha | No | Yamaha |
| YMCL | Yamaha Motor Co., Ltd. | No | Yamaha Motor Co., Ltd. |
| ZCZY | Zastavia (ZCZ-Yugoslavia) | No | Zastavia (ZCZ-Yugoslavia) |

---

### Typelist: VehiclePolicyStatus

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\VehiclePolicyStatus.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\VehiclePolicyStatus.ttx`
**Description:** Is policy up to date, behind payment etc.
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| inforce | In force | No | In force |
| expired | Expired | No | Expired |
| paymentpastdue | Payment past due | No | Payment past due |

---

### Typelist: VehicleStyle

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\VehicleStyle.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\VehicleStyle.ttx`
**Description:** Car, bus, truck etc.
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| passengercar | Passenger car | No | Passenger car |
| motorcycle | Motorcycle | No | Motorcycle |
| pick_up | Pickup | No | Pickup |
| van | Van | No | Van |
| straight_truck | Straight truck | No | Straight truck |
| tractor_trailer | Tractor trailer | No | Tractor trailer |
| tractor_only | Tractor only | No | Tractor only |
| trailer | Trailer | No | Trailer |
| bus | Bus | No | Bus |
| construction_vehicle | Construction vehicle | No | Construction vehicle |
| mobile_home | Mobile home | No | Mobile home |
| dump_truck | Dump truck | No | Dump truck |
| garbage_truck | Garbage truck | No | Garbage truck |
| cement_mixer | Cement mixer | No | Cement mixer |
| crane | Crane | No | Crane |
| car_transporter | Car transporter | No | Car transporter |
| boat | Boat | No | Boat |
| snowmobile | Snowmobile | No | Snowmobile |
| ATV | ATV | No | ATV |
| rv | RV | No | RV |
| other | Other | No | Other |

---

### Typelist: VehicleType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\VehicleType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\VehicleType.ttx`
**Description:** Types of vehicle on a policy
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| listed | Listed on policy | No | Listed on policy |
| new | Newly acquired | No | Newly acquired |
| rental | Rented / hired | No | Rented / hired |
| temp | Temporary substitute vehicle | No | Temporary substitute vehicle |
| other_owned | Other owned | No | Other owned |
| other_non_owned | Other non-owned | No | Other non-owned |
| leased | Leased | No | Leased |
| tow | Vehicle in tow | No | Vehicle in tow |
| owned | Owned | No | Owned |

---

### Typelist: VendorType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\VendorType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\VendorType.ttx`
**Description:** Types of vendors
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

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

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\VenueType.tti`
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

### Typelist: WaitingPeriodType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\WaitingPeriodType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\WaitingPeriodType.ttx`
**Description:** Per-state definition of possible waiting periods
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| three_calendar | 3 calendar days | No | 3 calendar days |
| three_business | 3 business days | No | 3 business days |
| unknown | Unknown | No | Unknown |

---

### Typelist: WaterSource

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\WaterSource.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\WaterSource.ttx`
**Description:** Source of water
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| plumbing_appliances | Plumbing Or Appliances | No | Plumbing Or Appliances |
| roof | Roof | No | Roof |
| other | Other | No | Other |

---

### Typelist: WCBenefitFactorCategory

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\WCBenefitFactorCategory.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\WCBenefitFactorCategory.ttx`
**Description:** Category of factor documenting details of workers comp benefit
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| MaxDuration | Maximum duration | No | Maximum duration of benefit |
| Offset | Offset | No | Allowable offsets such as SSI |
| WorkerFactor | EE's Attribute | No | Attributes of the worker such as age |
| WeeklyWage | Weekly Wage | No | How is weekly wage calculated |
| Other | Other | No | Other |
| DateRelated | Date Related | No | How the various dates factor into the calulation.  e.g day of injuy counts as day of disability |
| Override | Override | No | Typical benefit calculation formula is not utilized |
| WaitingPeriod | Waiting Period | No | Additional information about the waiting period |

---

### Typelist: WCBenefitFactorType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\WCBenefitFactorType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\WCBenefitFactorType.ttx`
**Description:** Types of factor documenting details of workers comp benefit
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| countdayofinjury | Day of Injury does count as one day of disability | No | Day of Injury does count as one day of disability |
| other | Other | No | Used to track misc issues |
| weeksofbenefit | (Max Weeks of Benefit) x (% impairment rating) | No | Max Weeks of Benefit x % impairment rating |
| duration | Duration of Disability | No | Duration of Disability |
| maxnumweeks | # of weeks | No | Maximum Period: # of weeks: (which should be in value field |
| aftertaxearnings | EEs spendable / after-tax earnings | No | Weekly Wage should be EE's spendable/after-tax earnings |
| offsets_ss_ui | Social Security and UI benefits | No | Subject to Social Security and Unemployment (UI)  benefit offsets |
| offsets_many | SS, UI, severance pay and employer funded pension plan | No | Social Security, Unemployment Insurance, severance pay and employer funded pension plan |
| age | Special rules beginning at age | No | Please review state rules if EE has reached age of 70 |
| lifetime | Maximum Period Exception: Lifetime if paraplegic, quadriplegic, or brain damaged | No | Maximum Period Exception: Lifetime if paraplegic, quadriplegic, or brain damaged |

---

### Typelist: WCBodyPartType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\WCBodyPartType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\WCBodyPartType.ttx`
**Description:** The primary body part affected in a Workers' Comp claim
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| head | Head | No | Head |
| lower | Lower extremities | No | Lower extremities |
| multiple | Multiple body parts | No | Multiple body parts |
| neck | Neck | No | Neck |
| trunk | Trunk | No | Trunk |
| upper | Upper extremities | No | Upper extremities |

---

### Typelist: WCDetailedBodyPartType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\WCDetailedBodyPartType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\WCDetailedBodyPartType.ttx`
**Description:** The detailed body parts that correspond to (and are filtered by) by WCBodyPartType
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 10 | Multiple head injuries | No | Multiple head injuries - Any combination of head injuries |
| 11 | Skull | No | Skull |
| 12 | Brain | No | Brain |
| 13 | Ear(s) | No | Ear(s) - includes: hearing, inside eardrum |
| 14 | Eye(s) | No | Eye(s) - includes: optic nerves, vision, eye lids |
| 15 | Nose | No | Nose - includes: nasal passage, sinus, sense of smell |
| 16 | Teeth | No | Teeth |
| 17 | Mouth | No | Mouth - includes: lips, tongue, throat, taste |
| 18 | Soft tissue (head) | No | Soft tissue (head) |
| 19 | Facial bones | No | Facial bones - includes: jaw |
| 20 | Multiple neck injuries | No | Multiple neck injuries - any combination of neck injuries |
| 21 | Vertebrae | No | Vertebrae - includes: spinal column bone, cervical segment |
| 22 | Disc (neck) | No | Disc (neck) - includes: spinal column cartilage, cervical segment |
| 23 | Spinal cord (neck) | No | Spinal cord (neck) - includes: nerve tissue, cervical segment |
| 24 | Larynx | No | Larynx - includes: cartilage, vocal cords |
| 25 | Soft tissue (neck) | No | Soft tissue (neck) - Other than larynx or trachea |
| 26 | Trachea | No | Trachea |
| 30 | Multiple upper extremities | No | Multiple upper extremities - any combination of arm and hand injuries |
| 31 | Upper arm | No | Upper arm - humorous and corresponding muscles, excluding clavicle and scapula |
| 32 | Elbow | No | Elbow - radial head |
| 33 | Lower arm | No | Lower arm - forearm: radius, ulna, and corresponding muscle |
| 34 | Wrist | No | Wrist - carpals and corresponding muscles |
| 35 | Hand | No | Hand - metacarpals and corresponding muscles, excluding wrists and fingers |
| 36 | Finger(s) | No | Finger(s) - other than thumb and corresponding muscles |
| 37 | Thumb | No | Thumb |
| 38 | Shoulder(s) | No | Shoulder(s) - armpit, rotator cuff, trapezius, clavicle, scapula |
| 39 | Wrist(s) and Hand(s) | No | Wrist(s) and hand(s) |
| 40 | Multiple trunk injuries | No | Multiple trunk injuries - any combination of trunk injuries |
| 41 | Upper back area | No | Upper back area - (thoracic area) upper back muscles, excluding vertebrae, disc, spinal cord |
| 42 | Lower back area | No | Lower back area - (lumbar area) lower back muscles, excluding sacrum, coccyx, pelvis, vertebrae, disc, spinal cord |
| 43 | Disc (back) | No | Disc (back) - spinal column cartilage other than cervical segment |
| 44 | Chest | No | Chest - including: ribs, sternum, soft tissue |
| 45 | Sacrum and coccyx | No | Sacrum and coccyx - first nine vertebrae |
| 46 | Pelvis | No | Pelvis |
| 47 | Spinal cord (back) | No | Spinal cord (back) - nerve tissue other than cervical segment |
| 48 | Internal organs | No | Internal organs - other than heart and lungs |
| 49 | Heart | No | Heart |
| 50 | Multiple lower appendages | No | Multiple lower appendages - any combination of leg and foot injuries |
| 51 | Hip | No | Hip |
| 52 | Upper leg | No | Upper leg - femur and corresponding muscles |
| 53 | Knee | No | Knee - Patella |
| 54 | Lower leg | No | Lower leg - tibia, fibula and corresponding muscles |
| 55 | Ankle | No | Ankle - tarsals |
| 56 | Foot | No | Foot - metatarsals, heel, Achilles tendon and corresponding muscles, excluding ankle or toes |
| 57 | Toes | No | Toes |
| 58 | Great toe | No | Great toe |
| 60 | Lungs | No | Lungs |
| 61 | Abdomen including groin | No | Abdomen including groin - excluding injury to internal organs |
| 62 | Buttocks | No | Buttocks - Soft tissue |
| 63 | Lumbar or sacral vertebrae | No | Lumbar or sacral vertebrae - bone portion of the spinal column |
| 64 | Artificial appliance | No | Artificial appliance - braces, etc. |
| 65 | Unclassified - insufficient info to properly identify | No | Unclassified - insufficient info to properly identify |
| 66 | No physical injury | No | No physical injury - mental disorder |
| 90 | Multiple body parts | No | Multiple body parts - applies when more than one major body part has been affect (such as an arm and a leg) |
| 91 | Body systems (with no external injury) | No | Body systems (with no external injury) - applies to the functioning of an entire body system without external injury (e.g. poisoning, inflammation) |

---

### Typelist: WCDetailedInjuryType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\WCDetailedInjuryType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\WCDetailedInjuryType.ttx`
**Description:** More detail on the primary injury
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 01 | No Physical Injury | No | No Physical Injury - Glasses, contacts, artificial appliance |
| 02 | Amputation | No | Amputation |
| 03 | Angina pectoris | No | Angina pectoris (chest pain) |
| 04 | Burn | No | Burn - heat (burn or scald) or chemical (corrosive damage) |
| 07 | Concussion | No | Concussion - brain, cerebral |
| 10 | Contusion | No | Contusion - bruise with intact skin surface, hematoma |
| 13 | Crushing | No | Crushing |
| 16 | Dislocation | No | Dislocation - pinched nerve, slipped or ruptured disc, herniated disc, complete tear, MD dislocation |
| 19 | Electric shock | No | Electric shock |
| 22 | Enucleation | No | Enucleation - removal of organ or tumor |
| 25 | Foreign body | No | Foreign body |
| 28 | Fracture | No | Fracture - breaking of a bone or a cartilage |
| 30 | Freezing | No | Freezing - frostbite |
| 31 | Hearing loss or impairment | No | Hearing loss or impairment |
| 32 | Heat prostration | No | Heat prostration - heat stroke, sun stroke, excluding sun burn |
| 34 | Hernia | No | Hernia - abnormal protrusion of an organ through its containing wall |
| 36 | Infection | No | Infection |
| 37 | Inflammation | No | Inflammation |
| 40 | Laceration | No | Laceration - cuts, scratches, abrasions, superficial wounds |
| 41 | Myocardial infarction | No | Myocardial infarction - heart attack, heart conditions, hypertension |
| 42 | Poisoning (not overdose or cumulative injury) | No | Poisoning (not overdose or cumulative injury) |
| 43 | Puncture | No | Puncture |
| 46 | Rupture | No | Rupture |
| 47 | Severance | No | Severance |
| 49 | Sprain | No | Sprain |
| 52 | Strain | No | Strain |
| 53 | Syncope | No | Syncope - fainting, passing out |
| 54 | Asphyxiation | No | Asphyxiation - strangulation, drowning |
| 55 | Vascular | No | Vascular - strokes, varicose veins, other circulatory injuries |
| 58 | Vision Loss | No | Vision Loss |
| 59 | Other specific injury | No | Other specific injury |
| 60 | Dust disease | No | Dust disease - all other lung disease |
| 61 | Asbestosis | No | Asbestosis - lung disease from asbestos |
| 62 | Black lung | No | Black lung - lung disease from coal mining |
| 63 | Byssinosis | No | Byssinosis - lung disease from cotton, flax, hemp |
| 64 | Silicosis | No | Silicosis - lung disease from inhalation of silica (quartz) dust |
| 65 | Respiratory disorders (gases, fumes, chemicals) | No | Respiratory disorders (gases, fumes, chemicals) |
| 66 | Poisoning (chemical) | No | Poisoning (chemical) |
| 67 | Poisoning (metal) | No | Poisoning (metal) |
| 68 | Dermatitis | No | Dermatitis - from repeated contact with irritants |
| 69 | Mental disorder | No | Mental disorder |
| 70 | Radiation | No | Radiation |
| 71 | All other occupational disease injuries | No | All other occupational disease injuries |
| 72 | Loss of hearing | No | Loss of hearing |
| 73 | Contagious disease | No | Contagious disease |
| 74 | Cancer | No | Cancer |
| 75 | AIDS | No | AIDS |
| 76 | Video display terminal diseases | No | Video display terminal diseases - excluding carpal tunnel syndrome |
| 77 | Mental stress | No | Mental stress |
| 78 | Carpal Tunnel Syndrome | No | Carpal Tunnel Syndrome |
| 79 | Hepatitis C | No | Hepatitis C |
| 80 | All other cumulative injuries | No | All other cumulative injuries |
| 90 | Multiple physical injuries only | No | Multiple physical injuries only |
| 91 | Multiple injuries including both physical and psychological | No | Multiple injuries including both physical and psychological |

---

### Typelist: WCInjuryType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\WCInjuryType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\WCInjuryType.ttx`
**Description:** The primary injury in a Workers' Comp claim
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| multiple | Multiple injuries | No | Multiple injuries |
| occupational | Occupational disease or cumulative injury | No | Occupational disease or cumulative injury |
| specific | Specific injury | No | Specific injury |

---

### Typelist: WCMedicalTreatmentType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\WCMedicalTreatmentType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\WCMedicalTreatmentType.ttx`
**Description:** The type of treatment received in a Workers' Comp claim
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| hospital | Hospitalized | No | Hospitalized |
| major_surgery | Major surgery | No | Major surgery |
| minor_surgery | Minor surgery | No | Minor surgery |
| mult_doctors | Multiple doctors | No | Multiple doctors |
| mult_treatments | Multiple treatments | No | Multiple treatments |
| none | No treatment | No | No treatment |
| one_doctor | Only one doctor | No | Only one doctor |
| rehab | Rehab | No | Rehab |

---

### Typelist: WeatherType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\WeatherType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\WeatherType.ttx`
**Description:** Weather conditions at time of accident
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| CL | Clear | No | Clear |
| RA | Rain | No | Rain |
| SN | Snow | No | Snow |
| FG | Fog | No | Fog |
| IC | Ice | No | Ice |
| WI | Wind | No | Wind |

---

### Typelist: Weekdays

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\Weekdays.tti`
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

### Typelist: WitnessPosition

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\WitnessPosition.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\WitnessPosition.ttx`
**Description:** 
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 0 | Inside vehicle | No | Inside vehicle |
| 1 | In the other vehicle | No | In the other vehicle |
| 2 | Pedestrian | No | Pedestrian |
| 3 | Unknown | No | Unknown |

---

### Typelist: WorkCapacity

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\WorkCapacity.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\WorkCapacity.ttx`
**Description:** Capacity in which employee returned to work
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| lastdateworked | Last date worked prior to injury | Yes | Last date worked prior to injury |
| fullduty | Working - No Restrictions | No | Working - No Restrictions |
| modifiedduty | RTW - modified duty | Yes | Modified duty |
| estimatedrtw | Estimated RTW date | Yes | Estimated return to work date |
| stopped_work | Off work | No | Stopped work |
| restricted_work | Restricted work | No | Working with restrictions |

---

### Typelist: WorkflowActionType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\WorkflowActionType.tti`
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

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\WorkflowActiveState.tti`
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

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\WorkflowHandler.tti`
**Description:** What infrastructure handles this Workflow?
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| internal | Internal | No | Handled by Guidewire's internal Workflow engine |
| test | Test | No | Handled by testing infrastructure (not for production!) |

---

### Typelist: WorkflowState

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\WorkflowState.tti`
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

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\WorkflowTriggerKey.tti`
**Description:** What workflow Triggers are allowed
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| *(None defined)* | *Dynamic or database-driven* | No | Typelist populated dynamically at runtime or via database table |

---

### Typelist: WorkItemSetState

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\WorkItemSetState.tti`
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

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\WorkItemStatusType.tti`
**Description:** The status of a work-item
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| available | Available | No | Work item that is available to be processed. |
| checkedout | CheckedOut | No | Work item that is checked out. |
| failed | Failed | No | Work item that exceeded the maximum number of allowed retries. |

---

### Typelist: YesNo

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\YesNo.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\YesNo.ttx`
**Description:** Yes, no or unknown
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Yes | Yes | No | Yes |
| No | No | No | No |
| Unknown | Unknown | No | Unknown |

---

### Typelist: ZoneType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\typelist\ZoneType.tti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ZoneType.ttx`
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

### Typelist: AdjudicativeDomain

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\AdjudicativeDomain.tti`
**Description:** specialty types for adjudicators
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Disputes | Alternative Dispute Resolutions (ADR) | No | Alternative Dispute Resolutions (ADR) |
| Appeals | Appeals | No | Appeals |
| Municipal | Municipal | No | Municipal |
| County | County | No | County |
| Federal | Federal | No | Federal |
| Supreme | Supreme | No | Supreme |

---

### Typelist: AlarmType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\AlarmType.tti`
**Description:** Type of alarms: Automatic, Manual, None, or Unknown
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Automatic | Automatic | No | Automatic |
| Manual | Manual | No | Manual |
| None | None | No | None |
| Unknown | Unknown | No | Unknown |

---

### Typelist: BankAccountType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\BankAccountType.tti`
**Description:** The type of bank accout e.g. checking, savings etc
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| checking | Checking | No | Checking |
| savings | Savings | No | Savings |
| other | Other | No | Other |

---

### Typelist: BenefitEndReasonType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\BenefitEndReasonType.tti`
**Description:** Benefit end reason - for use on EditableClaimantDependents LV
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Remarried | Remarried | No | Remarried |
| BenefitLimitExpired | Benefit limit expired | No | Benefit limit expired |
| NoLongerDependent | No longer dependent | No | No longer dependent |

---

### Typelist: ClassType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ClassType.tti`
**Description:** class type
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| allwoodframed | All wood or wood framed | No | All wood and wood framed |
| masonwall | Masonry walls, wood roof | No | Masonry walls, wood roof |
| allmetal | All metal | No | All metal |
| maswallmetal | Masonry walls, metal roof | No | Masonry walls, metal roof |
| protmetal | Protected metal to 2hrs | No | Protected metal to 2hrs |
| reinconcrete | Reinforced concrete greater than 2hrs | No | Reinforced concrete greater than 2hrs |

---

### Typelist: DependentType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\DependentType.tti`
**Description:** Type of dependent - spouse, child etc.
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| spouse | Spouse | No | Spouse |
| childunder18 | Child under 18 | No | Child under 18 |
| fulltimestudent | Full-time student | No | Full-time student |
| other | Other | No | Other |

---

### Typelist: EssentialServiceType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\EssentialServiceType.tti`
**Description:** 
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| insidehome | Inside home | No | Inside home |
| outsidehome | Outside home | No | Outside home |
| transportation | Transportation | No | Transportation |

---

### Typelist: EstDamageType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\EstDamageType.tti`
**Description:** Estimate of damage from Iexprs
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 1 | $ 0 - 5,000 | No | $ 0 - 5,000 |
| 2 | $ 5,001 - 15,000 | No | $ 5,001 - 15,000 |
| 3 | $ 15,001 - 25,000 | No | $ 15,001 - 25,000 |
| 4 | $ 25,001 - 50,000 | No | $ 25,001 - 50,000 |
| 5 | $ 50,001 - 100,000 | No | $ 50,001 - 100,000 |
| 6 | > $ 100,000 | No | > $ 100,000 |
| Unknown | Unknown | No | Unknown |
| 7 | € 0 - 5000 | No | € 0 - 5000 |
| 8 | € 5001 - 15 000 | No | € 5001 - 15 000 |
| 9 | € 15 001 - 25 000 | No | € 15 001 - 25 000 |
| 10 | € 25 001 - 50 000 | No | € 25 001 - 50 000 |
| 11 | € 50 001 - 100 000 | No | € 50 001 - 100 000 |
| 12 | > € 100 000 | No | > € 100 000 |

---

### Typelist: ExtWallMat

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ExtWallMat.tti`
**Description:** Exterior wall covering material of property
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Wood | Wood | No | Wood |
| Metal | Metal | No | Metal |
| Stucco | Stucco | No | Stucco |
| BrickVeneer | Brick veneer | No | Brick veneer |
| Vinyl | Vinyl | No | Vinyl |
| Other | Other | No | Other |
| EIFS | Exterior insulating fastening system | No | Exterior insulating fastening system |
| Masonry | Masonry | No | Masonry |

---

### Typelist: LossArea

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\LossArea.tti`
**Description:** Loss area of property
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| office | Office | No | Office |
| warehouse | Warehouse | No | Warehouse |
| manufArea | Manufacturing area | No | Manufacturing area |
| other | Other | No | Other |

---

### Typelist: LossOccured

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\LossOccured.tti`
**Description:** 
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| AtPremisses | At premises | No | Loss occurred at premises |
| InTransit | In transit | No | Loss occurred in transit |
| other | Other | No | Other |

---

### Typelist: PercentageDriven

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\PercentageDriven.tti`
**Description:** % of time vehicle driven by the minor
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| 0 | 0 - 20% | No | 0 - 20% |
| 1 | 20 - 40% | No | 20 - 40% |
| 2 | 40-60% | No | 40-60% |
| 3 | > 60% | No | > 60% |
| 4 | Unsure | No | Unsure |

---

### Typelist: QuickClaimDefault

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\QuickClaimDefault.tti`
**Description:** Default values for quick claims
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Glass | GL Incident Only | No | General liability incidents only |
| QuickClaimAuto | Quick Claim Auto | No | Quick claim auto |
| AutoFirstAndFinal | Auto First and Final | No | Auto first and final |
| QuickClaimProperty | Quick Claim Property | No | Quick claim property |

---

### Typelist: RecovClassType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\RecovClassType.tti`
**Description:** Recovery Classification
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| nodam | No Apparent Damage | No | Found |
| str_eng | Stripped of major parts - engine | No | Stripped of major parts - engine |
| str_trans | Stripped of major parts - transmission | No | Stripped of major parts - transmission |
| str_oth | Stripped of major parts - other | No | Stripped of major parts - other |
| str_engtrans | Stripped of major parts - engine & transmission | No | Stripped of major parts - engine & transmission |
| str_engoth | Stripped of major parts - engine & other | No | Stripped of major parts - engine& other |
| str_transoth | Stripped of major parts - transmission & other | No | Stripped of major parts - transmission, & other |
| str_engtransoth | Stripped of major parts - engine, transmission & other | No | Stripped of major parts - engine, transmission, & other |
| dam | No major parts missing, but damaged | No | No major parts missing, but damaged |

---

### Typelist: RecovCondType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\RecovCondType.tti`
**Description:** Vehicle condition (at recovery from theft)
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| not_recov | Not recovered/condition unknown | No | Not recovered/condition unknown |
| no_dam | No apparent damage | No | No apparent damage |
| str | Stripped | No | Stripped |
| wreck | Wrecked | No | Wrecked |
| burn | Burned | No | Burned |
| flood | Flood | No | Flood |
| vandal | Vandalized | No | Vandalized |
| str_wrk | Stripped and wrecked | No | Stripped and wrecked |
| str_brn | Stripped and burned | No | Stripped and burned |
| str_fl | Stripped and flood | No | Stripped and flood |
| str_vand | Stripped and vandalized | No | Stripped and vandalized |
| wrk_brn | Wrecked and burned | No | Wrecked and burned |
| wrk_vand | Wrecked and vandalized | No | Wrecked and vandalized |
| brn_vand | Burned and vandalized | No | Burned and vandalized |
| fld_vand | Flood and vandalized | No | Flood and vandalized |

---

### Typelist: RoofMaterial

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\RoofMaterial.tti`
**Description:** Roof covering material of property
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Builtup | Built up | No | Built up |
| Shingles | Shingles | No | Shingles |
| Membrane | Membrane | No | Membrane |
| None | None | No | None |

---

### Typelist: ServiceRequestMetricLimitType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ServiceRequestMetricLimitType.tti`
**Description:** Calculation method for a service metric limit
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| nooffset | No Offset | No | Standard limit comparison, no computation |
| absoluteoffset | Absolute Offset | No | Offsets must be computed before comparison |
| percentageoffset | Percentage Offset | No | Offsets must be computed before comparison |

---

### Typelist: SourceSystem

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\SourceSystem.tti`
**Description:** Policy system from which line of business, coverage, etc. codes are sourced
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| PC | PolicyCenter | No | PolicyCenter product model codes |
| PC-PEL | PolicyCenter PELs | No | Product model codes for PolicyCenter product extension library products |
| PC-Custom | PolicyCenter Custom | No | Codes related to PolicyCenter but not generated automatically from the product model |
| Ext | External | No | Non-specific external policy system other than PolicyCenter |

---

### Typelist: SprinklerType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\SprinklerType.tti`
**Description:** Loss Area of property
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Wet | Wet | No | Wet |
| Dry | Dry | No | Dry |
| Open | Open | No | Open |
| Unknown | Unknown | No | Unknown |
| None | None | No | None |

---

### Typelist: SprinkRetServ

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\SprinkRetServ.tti`
**Description:** Sprinklers returned to service
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| Fully | Fully | No | Fully |
| Partially | Partially | No | Partially |
| Notatall | Not at all | No | None |

---

### Typelist: UserDetailAssignable

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\UserDetailAssignable.tti`
**Description:** Set of assignable object choices available for viewing in the user administration
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| claim | Claims | No | claims |
| exposure | Exposures | No | exposures |
| matter | Matters | No | matters |
| activity | Activities | No | activities |

---

### Typelist: VehCondType

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\VehCondType.tti`
**Description:** Vehicle condition
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| dr | Drivable (not total loss) | No | Drivable (not total loss) |
| dr_tl | Drivable (total loss) | No | Drivable (total loss) |
| nd | Not drivable (not total loss) | No | Not Drivable (not total loss) |
| nd_tl | Not drivable (total loss) | No | Not Drivable (total loss) |

---

### Typelist: ClaimIndicator

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ClaimIndicator.ttx`
**Description:** 
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| LitigationClaimIndicator | Litigation | No | Litigation Claim Indicator |
| FatalityClaimIndicator | Fatalities | No | Fatality Claim Indicator |
| LargeLossClaimIndicator | Large Loss | No | Large Loss Claim Indicator |
| CoverageInQuestionClaimIndicator | Coverage in Question | No | Coverage in Question Claim Indicator |
| SIUClaimIndicator | SIU | No | SIU Claim Indicator |
| FlagClaimIndicator | Flag Details | No | Flag Claim Indicator |
| SubrogationClaimIndicator | Subrogation | No | Subrogation Claim Indicator |

---

### Typelist: ClaimMetric

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ClaimMetric.ttx`
**Description:** 
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| DaysOpenClaimMetric | Days Open | No | Days Open Claim Metric |
| DaysInitialContactWithInsuredClaimMetric | Initial Contact with Insured (Days) | No | Days Insured was Contacted |
| DaysLastViewedByAdjusterClaimMetric | Days Since Last View - Adjuster | No | Days since Adjuster last viewed the claim |
| DaysLastViewedBySupervisorClaimMetric | Days Since Last View - Supervisor | No | Days since Supervisor last viewed the claim |
| OverdueActivitiesClaimMetric | Activities Past Due Date | No | Activities Past Due Date Claim Metric |
| OpenEscalatedActivitiesClaimMetric | Open Escalated Activities | No | Number of Open Escalated Activities Claim Metric |
| AllEscalatedActivitiesClaimMetric | Number of Escalated Activities | No | Number of Escalated Activities Claim Metric |
| PercentEscalatedActivitiesClaimMetric | % of Escalated Activities | No | Percentage of Escalated Activities Claim Metric |
| NetTotalIncurredClaimMetric | Net Total Incurred | No | Net Total Incurred Claim Metric |
| TotalPaidClaimMetric | Total Paid | No | Total Paid Claim Metric |
| PercentIncurredLossCostsClaimMetric | Incurred Loss Costs as % of Net Total Incurred | No | Incurred Loss Costs as % of Net Total Incurred Claim Metric |
| PercentPaidLossCostsClaimMetric | Paid Loss Costs as % of Total Paid | No | Paid Loss Costs as % of Total Paid Claim Metric |
| TimeToFirstPaymentClaimMetric | Time to First Loss Payment (Days) | No | Time to First Loss Payment Claim Metric |
| ReserveChangeCountClaimMetric | Number of Reserve Changes | No | Number of Reserve Changes Claim Metric |
| PercentReserveChangeClaimMetric | % Reserve Change from Initial Reserve | No | Percent Reserve Change from Initial Reserve Claim Metric |

---

### Typelist: ClassificationCondition

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ClassificationCondition.ttx`
**Description:** 
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| SegmentCondition | Segment Classification Condition | No | Classification condition filter by Segment |
| LossCauseCondition | Loss Cause Classification Condition | No | Classification condition filter by Loss Cause |
| ExposureCondition | Exposure Classification Condition | No | Classification condition filter by Exposure |
| IncidentSeverityCondition | Incident Severity Classification Condition | No | Classification condition filter by Incident Severity |
| JurisdictionCondition | Jurisdiction Classification Condition | No | Classification condition filter by Jurisdiction |
| CustomerServiceTierCondition | Service Tier Classification Condition | No | Classification condition filter by Service Tier |

---

### Typelist: ExposureMetric

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ExposureMetric.ttx`
**Description:** 
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| DaysOpenExposureMetric | Days Open | No | Days Open Exposure Metric |
| DaysInitialContactWithClaimantExposureMetric | Initial Contact with Claimant (Days) | No | Initial Contact with Claimant Exposure Metric |
| NetTotalIncurredExposureMetric | Net Total Incurred | No | Net Total Incurred Exposure Metric |
| TotalPaidExposureMetric | Total Paid | No | Total Paid Exposure Metric |
| PercentEscalatedActivitiesExposureMetric | % of Escalated Activities | No | Percent of Escalated Activities |
| PercentPaidLossCostsExposureMetric | Paid Loss Costs as % of Total Paid | No | Paid Loss Costs as % of Total Paid Exposure Metric |
| TimeToFirstPaymentExposureMetric | Time to First Loss Payment (Days) | No | Time To First Payment Exposure Metric |

---

### Typelist: RIAgreement

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\RIAgreement.ttx`
**Description:** 
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| RIAgreement | RIAgreement | No | RIAgreement |
| NonProportionalRIAgreement | Non Proportional RI Agreement | No | Non Proportional Reinsurance Agreement |
| ProportionalRIAgreement | Proportional RI Agreement | No | Proportional Reinsurance Agreement |
| ExcessOfLossRITreaty | Excess Of Loss RI Treaty Agreement | No | Excess Of Loss Reinsurance Treaty Agreement |
| NetExcessOfLossRITreaty | Net Excess Of Loss RI Treaty Agreement | No | Net Excess Of Loss Reinsurance Treaty Agreement |
| FacNetExcessOfLossRIAgreement | Net Excess Of Loss Fac Agreement | No | Net Excess Of Loss Facultative Agreement |
| QuotaShareRITreaty | Quota Share RI Treaty Agreement | No | Quota Share Reinsurance Treaty Agreement |
| FacProportionalRIAgreement | Fac Proportional RI Agreement | No | Fac Proportional Reinsurance Agreement |
| SurplusRITreaty | Surplus RI Treaty Agreement | No | Surplus Reinsurance Treaty Agreement |
| FacExcessOfLossRIAgreement | Excess Of Loss Fac Agreement | No | Excess Of Loss Facultative Agreement |
| PerEventRITreaty | Per Event RI Treaty Agreement | No | Per Event Reinsurance Treaty Agreement |
| AnnualAggregateRITreaty | Annual Aggregate RI Treaty Agreement | No | Annual Aggregate Reinsurance Treaty Agreement |

---

### Typelist: RiskUnit

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\RiskUnit.ttx`
**Description:** Subtype typelist for entity RiskUnit
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| RiskUnit | Risk Unit | No | RiskUnit |
| TripRU | Trip Risk | No | TripRU |
| VehicleRU | Vehicle Risk | No | VehicleRU |
| LocationBasedRU | Location Risk | No | LocationBasedRU |
| InlandMarineRU | Inland Marine Risk | No | InlandMarineRU |
| LocationMiscRU | Other Risk | No | LocationMiscRU |
| WCCovEmpRU | Workers Comp Risk | No | WCCovEmpRU |
| GeneralLiabilityRU | General Liability Risk | No | GeneralLiabilityRU |
| PropertyRU | Property Risk | No | PropertyRU |
| BuildingRU | Building Risk | No | BuildingRU |

---

### Typelist: ServiceRequestMetric

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\ServiceRequestMetric.ttx`
**Description:** Subtype typelist for entity ServiceRequestMetric
**Synthetic Data Relevance:** High (Primary business enumerator for synthetic claim/financial generation)

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| ServiceTimelinessServiceRequestMetric | Service Timeliness | No | Service Timeliness Service Metric |
| SpecialistInitialResponseTimeServiceRequestMetric | Response Time | No | Vendor Initial Response Time Service Metric |
| InvoiceVarianceVsQuoteServiceRequestMetric | Invoice Variance vs. Quote | No | Invoice Variance vs. Quote Service Metric |
| QuoteTimelinessServiceRequestMetric | Quote Timeliness | No | Quote Timeliness Service Metric |
| NumberOfDelaysServiceRequestMetric | Number Of Delays | No | NumberOfDelaysServiceRequestMetric |
| ServiceCycleTimeServiceRequestMetric | Cycle Time | No | Service Cycle Time Service Metric |

---

### Typelist: WorkloadClassification

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\typelist\WorkloadClassification.ttx`
**Description:** Workload Classification
**Synthetic Data Relevance:** Operational / Reference

| Code | Display Name | Retired | Description |
|------|--------------|---------|-------------|
| ClaimWorkloadClassification | Claim Workload Classification | No | Claim Workload Classification |
| ExposureWorkloadClassification | Exposure Workload Classification | No | Exposure Workload Classification |

---

