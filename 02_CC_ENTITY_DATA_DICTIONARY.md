# ClaimCenter Entity Data Dictionary

**Guidewire ClaimCenter Version:** 10.2.1.1523 (Platform 10.201.1)
**Installation Location:** `C:\GW10\ClaimCenter`
**Extraction Date:** 2026-09-26
**Total Insurance Entities Cataloged:** 192

---

## Overview & Extraction Methodology

This data dictionary provides a complete, source-grounded specification of the ClaimCenter data model. Every entity, attribute, data type, foreign key reference, typelist code, array collection, and validation rule is verified directly against the installed `.eti`, `.etx`, and `.eix` XML metadata files.

### Standard Platform Infrastructure Fields
In Guidewire ClaimCenter, entities inherit standard infrastructure attributes:
- **KeyableBean**: `ID` (Primary key, Long/Key, System-generated unique), `PublicID` (Varchar(64), External business identifier).
- **Versionable / Editable**: `BeanVersion` (Optimistic locking integer), `CreateTime` (DateTime), `CreateUser` (FK -> User), `UpdateTime` (DateTime), `UpdateUser` (FK -> User).
- **Retireable**: `Retired` (Long, 0 = Active, non-zero = timestamp of retirement / soft deletion).

---

## Entity Specifications

### Entity: Claim

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Claim.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\Claim.etx`
**Entity Type:** `retireable`
**Database Table:** `claim`
**Supertype:** None
**Description:** Insurance claim

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| ClaimNumber | claimnumber | Yes | - | - | The external identifier of the claim. |
| ClaimantRprtdDate | datetime | No | - | - | Workers' Comp only. Date when the claimant reported incident to insured (employer). |
| CoverageInQuestion | bit | No | - | - | Whether the claim is covered by the claimant's policies. |
| Description | mediumtext | No | - | - | Description of the accident or loss. |
| EmploymentInjury | bit | No | - | - | Workers' Comp only. Whether the injury occurred in course of employment. |
| ExposureBegan | datetime | No | - | - | Workers' Comp only. Date when the exposure began. |
| ExposureEnded | datetime | No | - | - | Workers' Comp only. Date when the exposure ended. |
| Fault | percentagedec | No | - | - | Insured's probable percentage of fault. |
| FireDeptInfo | shorttext | No | - | - | Reports, incident number, and other information from the fire department. |
| FlaggedDate | datetime | No | - | - | The date and time the claim was initially flagged.  When the flag is unset, this date is set to null and will be set to a new date if a new reason for flagging the claim is found later. |
| FlaggedReason | mediumtext | No | - | - | The reason this claim is flagged. |
| IncidentReport | bit | No | - | - | True if this is an incident report only and the claim will not be processed. |
| LossDate | datetime | No | - | - | The date on which the loss occurred. |
| PoliceDeptInfo | shorttext | No | - | - | Reports, incident number, and other information from the police deptartment. |
| PurgeDate | datetime | No | - | - | Date at which the claim should be purged. Configurations can use this field to decide when to mark the claim for purge, and there are sample Claim Closed and Claim Reopened rules to set it. It is not used by the internal purge logic. |
| ReOpenDate | datetime | No | - | - | Date claim was reopened. |
| ReportedDate | datetime | No | - | - | Date on which the loss was reported. |
| StateAckNumber | varchar | No | - | - | Acknowledgment number of the state file for this claim. |
| StateFileNumber | varchar | No | - | - | Number of the state file for this claim. |
| StatuteDate | datetime | No | - | - | Date at which the statute of limitations expires for this claim. |
| Mold | bit | No | - | - | Boolean field to mark a claim as involving mold. |
| HazardousWaste | bit | No | - | - | Boolean field to mark a claim as involving hazardous waste. |
| FirstNoticeSuit | bit | No | - | - | Boolean field to indicate suit at the time of the first notice. |
| DateRptdToAgent | datetime | No | - | - | The date the agent was notified about the claim. |
| DateRptdToInsured | datetime | No | - | - | The date the insured was notified about the claim. |
| ManifestationDate | datetime | No | - | - | The manifestation date. |
| LossLocationCode | varchar | No | - | - | Location Code for the Loss Location. |
| DateRptdToEmployer | datetime | No | - | - | The date the claim was reported to the employer. |
| ISOEnabled | bit | No | - | - | Default: true Is this field enabled for ISO. |
| AgencyId | varchar | No | - | - | An ID assigned to indicate company and office a claim is being submitted by, this data is used by ISO integration |
| ReinsuranceReportable | bit | No | - | - | True if this claim has exceeded the Reinsurance Reporting Threshold |
| DateCompDcsnDue | datetime | No | - | - | The date the compensability Decision (for entire claim) was Due. |
| DateCompDcsnMade | datetime | No | - | - | The date the compensability Decision (for entire claim) was Made. |
| BenefitsStatusDcsn | bit | No | - | - | Indicates if the benefits decision has been made yet. |
| DateFormGivenToEmp | datetime | No | - | - | The date the work comp form was given to an employee. |
| DateFormRetByEmp | datetime | No | - | - | The date the work comp form was returned by an employee. |
| ModifiedDutyAvail | bit | No | - | - | Is Modified Duty Available at Work. |
| InjuredOnPremises | bit | No | - | - | Was the employee injured on the premesis. |
| InjuredRegularJob | bit | No | - | - | Was the employee injured while doing his or her regular job. |
| SafetyEquipProv | bit | No | - | - | Was safety equipment provided. |
| SafetyEquipUsed | bit | No | - | - | Was safety equipment used. |
| ComputerSecurity | bit | No | - | - | Whether computer security issues were involved. |
| DeathDate | datetime | No | - | - | Date of death (if injury type is death). |
| DateEligibleForArchive | datetime | No | - | - | The date and time that this claim will become eligible for archiving. While this field is null or set to a date in the future, this claim is not selected by the archive batch process. (Note that being passed over by the archive batch process is different from being 'skipped' or 'excluded'.) |
| WeatherRelated | bit | No | - | - | Is related to weather |
| EmployerValidityReason | varchar | No | - | - | The reason the employer questions the validity of the claim. |
| SIScore | integer | No | - | - | Default: 0 Special Investigations Score. |
| SIEscalateSIUdate | datetime | No | - | - | Date escalated to SIU team. |
| ExaminationDate | datetime | No | - | - | Date of the Examination. |
| TreatedPatientBfr | bit | No | - | - | Has the patient been treated before. |
| DiagnosticCnsistnt | bit | No | - | - | Is the diagnostic consistent. |
| CurrentConditions | bit | No | - | - | Current conditions |
| FurtherTreatment | bit | No | - | - | Is further treatment required. |
| HospitalDate | datetime | No | - | - | Date admitted to the hospital. |
| HospitalDays | integer | No | - | - | Estimated Days in hospital. |
| PreexDisblty | bit | No | - | - | Default: false Whether the injured person had a pre-existing disability. |
| PTPinMPN | bit | No | - | - | Is Primary Treating Physician in MPN? |
| InsurerSentMPNNotice | datetime | No | - | - | Date that Insurer sent out the MPN Notification. |
| EmpSentMPNNotice | datetime | No | - | - | Date that the Employer sent out the MPN Notification. |
| InjWkrInMPN | datetime | No | - | - | Date that the injured Worker moved to MPN. |
| MMIdate | datetime | No | - | - | Date Maximum Medical Improvement was reached. |
| StorageDate | datetime | No | - | - | Date file shipped to storage facility. |
| StorageBoxNum | varchar | No | - | - | Storage Box Number. |
| StorageBarCodeNum | varchar | No | - | - | Storage Bar Code Number. |
| StorageVolumes | varchar | No | - | - | Storage Volumes. |
| ClaimWorkComp | ForeignKey | No | ClaimWorkComp | - | Claim's worker's compensation data |
| Catastrophe | ForeignKey | No | Catastrophe | - | Associated catastrophe. |
| EmploymentData | ForeignKey | No | EmploymentData | - | Workers' Comp only. Details about the claimant's employment. |
| LocationCode | ForeignKey | No | PolicyLocation | - | Workers' Comp only. Location at the employer's facilities where the accident occurred. |
| LossLocation | ForeignKey | No | Address | - | Location of the loss. |
| Policy | ForeignKey | Yes | Policy | - | The policy associated with this claim. |
| ClaimantDenorm | ForeignKey | No | Contact | - | Claimant FK denorm. |
| InsuredDenorm | ForeignKey | No | Contact | - | Insured FK denorm. |
| AccidentType | TypeKey | No | - | AccidentType | Detailed accident type; augments LossCause. Codes (74 total): [01, 02, 03, 04, 05, ...] |
| ClaimSource | TypeKey | No | - | ClaimSource | Information about how Claim was entered into the System. Codes: [ordinary, autofirstandfinal] |
| ClosedOutcome | TypeKey | No | - | ClaimClosedOutcomeType | The outcome reached when closing the claim. Codes: [paymentscomplete, completed, duplicate, mistake, fraud] |
| Currency | TypeKey | Yes | - | Currency | The currency for the claim, copied from the policy. Codes (7 total): [usd, eur, gbp, cad, aud, ...] |
| ReopenedReason | TypeKey | No | - | ClaimReopenedReason | The reason for reopening the claim. Codes: [paymentdenied, mistake, newinfo] |
| Flagged | TypeKey | Yes | - | FlaggedType | Default: neverflagged This claim's status as a flagged claim. Codes: [isflagged, wasflagged, neverflagged] |
| HowReported | TypeKey | No | - | HowReportedType | How the claim was reported. Codes: [phone, internet, fax, mail, walkin] |
| JurisdictionState | TypeKey | No | - | Jurisdiction | The state of jurisdiction. This indicates jurisdiction that covers the loss, which may differ from the state in which the loss occurred. The Jurisdiction must be associated with JurisdictionType.TC_INSURANCE. Codes (97 total): [AK, AL, AR, AZ, CA, ...] |
| LitigationStatus | TypeKey | No | - | LitigationStatus | The status of the litigation. Codes (13 total): [not_litigated, litigated, complete, rep, suit_filed, ...] |
| LOBCode | TypeKey | No | - | LobCode | Line of Business code; typically related to the policy. Codes (11 total): [GLLine, CPLine, PersonalAutoLine, IMLine, WorkersCompLine, ...] |
| LossCause | TypeKey | No | - | LossCause | General cause of loss; dependent on loss type. Codes (64 total): [animalcollision, animal, bikecollision, fixedobjcoll, vehcollision, ...] |
| LossType | TypeKey | Yes | - | LossType | High level claim type (for example, Auto or Property). Codes: [AUTO, PR, GL, WC, TRAV] |
| MainContactType | TypeKey | No | - | PersonRelationType | Relationship of the main contact to the insured. Codes (23 total): [self, relative, friend, agent, attorney, ...] |
| PermissionRequired | TypeKey | No | - | ClaimSecurityType | If non-null, this is an additional permission that users are required to have to view or work on this claim. This field is used to restrict access to sensitive or private claims; for example, those involving an employee or that are under litigation. Codes: [unsecuredclaim, employeeclaim, fraudriskclaim, sensitiveclaim, underlitclaim] |
| Progress | TypeKey | No | - | ClaimProgressType | Description of the progress of an open claim. Codes: [new, investigation, evaluation, settlement, litigation, pendingrecovery] |
| ReportedByType | TypeKey | No | - | PersonRelationType | Relationship of the person who reported the claim to the insured. Codes (23 total): [self, relative, friend, agent, attorney, ...] |
| Segment | TypeKey | No | - | ClaimSegment | Segmentation type of the claim. Both the claim and the exposure may be segmented. Codes (22 total): [unknown, auto_low, auto_mid, auto_high, prop_low, ...] |
| State | TypeKey | Yes | - | ClaimState | Default: draft Internal state of the claim. Codes: [draft, open, closed, archived] |
| Strategy | TypeKey | No | - | ClaimStrategy | Segmentation type of the claim. Both the claim and the exposure may be segmented. Codes (14 total): [unknown, auto_fast, auto_normal, prop_fast, prop_normal, ...] |
| ValidationLevel | TypeKey | No | - | ValidationLevel | Validation level that this object passed (if any) before it was stored. Codes: [loadsave, iso, external] |
| Weather | TypeKey | No | - | WeatherType | Weather conditions at the time of accident. Codes: [CL, RA, SN, FG, IC, WI] |
| SalvageStatus | TypeKey | No | - | SalvageStatus | The salvage status for a claim. Codes: [in_review, open, closed] |
| SIUStatus | TypeKey | No | - | SIUStatus | The SIU status for a claim Codes: [No_Referral, Under_Investigation, Investigation_Closed] |
| OtherRecovStatus | TypeKey | No | - | OtherRecoverableStatus | The Other Recoverable status for a claim. Codes: [in_review, open, closed] |
| ReinsuranceFlaggedStatus | TypeKey | No | - | ReinsuranceFlaggedStatus | The reinsurance flagged status for a claim. Codes: [SystemFlagged, UserFlagged, UserUnflagged, SystemUnflagged] |
| ConcurrentEmp | TypeKey | No | - | YesNo | Did the employee have concurrent employment. Codes: [Yes, No, Unknown] |
| EmpQusValidity | TypeKey | No | - | YesNo | Does the employer question the validity of the claim. Codes: [Yes, No, Unknown] |
| DrugsInvolved | TypeKey | No | - | YesNo | Does the employer question the validity of the claim. Codes: [Yes, No, Unknown] |
| FaultRating | TypeKey | No | - | FaultRating | Indicates in the insured is at fault. Codes: [2, thirdparty, nofault, 0, 1, 3] |
| SIULifeCycleState | TypeKey | No | - | ClaimLifeCycleState | Current state of SIU trigger rule processing for this Claim. Codes: [step1, step2, step3] |
| LargeLossNotificationStatus | TypeKey | No | - | LargeLossNotificationStatus | The status of large loss notices. Codes: [None, InQueue, Sent] |
| ClaimTier | TypeKey | No | - | ClaimTier | The tier of this claim, used to decide how to rate the claim metrics. Codes (7 total): [incidentreport, medicalonly, indemnity, el, low, ...] |
| LocationOfTheft | TypeKey | No | - | LocationOfTheft | the Location where the property was stolen. Codes: [residential, commercial, offPremises] |
| SIEscalateSIU | TypeKey | No | - | YesNo | Default: No Escalate to SIU team. Codes: [Yes, No, Unknown] |
| ShowMedicalFirstInfo | TypeKey | No | - | YesNo | Default: Yes Show Medical First info section. Codes: [Yes, No, Unknown] |
| StorageLocationState | TypeKey | No | - | State | Storage Location State. Codes (142 total): [AK, AL, AR, AZ, CA, ...] |
| StorageCategory | TypeKey | No | - | StorageCategory | Storage Category. Codes: [prop_cas, work_comp, health_acc, tpa, other] |
| StorageType | TypeKey | No | - | StorageType | Storage Type. Codes: [inhouse, destroyed, storage] |
| AllocatedClaimNumber | OneToOne | No | AllocatedClaimNumber | - | If this claim is draft, and an attempt to save it has failed, contains the claim number that was allocated before the failure. Otherwise null. |
| SubrogationSummary | OneToOne | No | SubrogationSummary | - | Claim's subrogation-related data |
| PolicyLocationSummaryJoin | OneToOne | No | PolicyLocationSummaryJoin | - | Link to get the associated policy location summary (from policy system for catastrophe). |
| ClaimRpt | OneToOne | No | ClaimRpt | - | The calculated financials data for this claim. |
| ClaimInfo | OneToOne | No | ClaimInfo | - | The claim info is used to cache information for when this claim is archived. |
| ClaimMetricRecalculationTime | OneToOne | No | ClaimMetricRecalculationTime | - | Tracks when Claim metrics and indicators need to be recalculated |
| SpecialHandlingFinancialState | OneToOne | No | SpecialHandlingFinancialState | - | Tracks previously calculated financial values used by AutomatedHandlerTriggers that trigger on financial thresholds |
| PropertyFireDamage | OneToOne | No | PropertyFireDamage | - | Details of fire damage to property |
| PropertyWaterDamage | OneToOne | No | PropertyWaterDamage | - | Details of water damage to property |
| InsuredPremises_Ext | bit | No | - | - | [Extension] True if the incident occurred on the employer's premises. |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Access | ClaimAccess | The access control objects for this claim. |
| Activities | Activity | The activities for this claim. |
| RoleAssignments | UserRoleAssignment | The user role assignments for this claim. |
| ClaimISOMatchReports | ClaimISOMatchReport | ISO match reports for this claim. |
| ClaimSynchStates | ClaimSynchState | The sync states related to this claim. |
| ConcurrentEmpl | ConcurrentEmployment | Details of concurrent employment for workers' comp claims. |
| Contacts | ClaimContact | The contacts involved with this claim. Including indirectly involved, like Exposures contacts. |
| Documents | Document | The documents associated with this claim; for example, FNOL accord form or police report. Warning: do not rely on the contents of this array when the IDocumentMetadataSource plugin is enabled; use DocumentsUtil.getAllDocumentsForClaim instead. |
| Exposures | Exposure | The exposures related to this claim. Note: if triggersValidation is false, exposure metrics will not be run automatically. |
| History | History | The history events related to this claim. |
| Incidents | Incident | Descriptions of incidents related to this claim. Note: In Gosu, it's preferred to use Claim.VehicleIncidentsOnly and similar properties for each Incident subtype. See the Application Guide. |
| Matters | Matter | The legal matters related to this claim. |
| Notes | Note | The notes particular to this claim. Notes can also be associated with a particular exposure. |
| Officials | Official | Details of officials associated with claim. |
| MetroReports | MetroReport | Details of reports associated with claim. |
| OtherBenefits | OtherBenefit | Details of other benefits for workers comp claim. |
| ReserveLines | ReserveLine | ReserveLines relating to this claim. |
| RICodings | RICoding | RICodings relating to this claim. |
| Text | ClaimText | Large text fields associated with claim. |
| Transactions | Transaction | Transactions relating to this claim.  For rules, it is much better to use one of the getXXXIterator() methods and for the UI it is much better to use one of the getXXXQuery() methods to retrieve all transactions or a specific subtype of Transactions for the claim. |
| Negotiations | Negotiation | The negotiations related to this claim. |
| Evaluations | Evaluation | The original cost estimate followed by any modifications to that estimate. |
| Workflows | ClaimWorkflow | Set of workflows associated with this Claim. |
| Deductibles | Deductible | Deductibles associated with this claim. |
| ServiceRequests | ServiceRequest | Service requests associated with this claim. Note: if triggersValidation is false, service request metrics will not be run automatically. |
| ClaimMetrics | ClaimMetric | Metrics related to this claim. |
| ClaimIndicators | ClaimIndicator | Indicators related to this claim. |
| RIAgreementGroups | RIAgreementGroup | The reinsurance agreement groups for this claim. |
| SITriggers | SITrigger | The triggers for Special Investigations linked to this Claim |
| ContribFactors | ContribFactor | Child collection |
| MedicalContactStatus | MedicalContactStatus | Child collection |
| MedicalTreatments | MedicalTreatment | Child collection |
| DrugsPrescribed | DrugPrescribed | Child collection |
| SIAnswerSet | SIUAnswerSet | Link to Answer set for SIU |

---

### Entity: ClaimInfo

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimInfo.eti`
**Entity Type:** `retireable`
**Database Table:** `claiminfo`
**Supertype:** None
**Description:** Claim Information

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| RootPublicID | publicid | Yes | - | - | The public ID of the root. |
| ClaimNumber | claimnumber | Yes | - | - | The external identifier of the claim. |
| PolicyNumber | policynumber | No | - | - | Number of the policy (generally a string). |
| LossDate | datetime | No | - | - | Cached LossDate on Claim |
| NoticeDate | datetime | No | - | - | Cached ReportedDate on Claim |
| PurgeDate | datetime | No | - | - | Date at which the claim should be purged. Configurations can use this field to decide when to mark the claim for purge, and there are sample Claim Closed and Claim Reopened rules to set it. It is not used by the internal purge logic. |
| LossLocationCode | varchar | No | - | - | Location Code denormed from claim.LossLocationCode |
| CoverageLineMatchDataInfoValid | bit | Yes | - | - | Default: false True for archived claims which have an accurate CoverageLineMatchDataInfo array, false otherwise |
| Claim | ForeignKey | No | Claim | - | Claim |
| AssignedGroup | ForeignKey | No | Group | - | Assigned group on Claim |
| Adjuster | ForeignKey | No | User | - | Assigned user on Claim |
| JurisdictionState | TypeKey | No | - | Jurisdiction | The state of jurisdiction. Denormed from claim.JurisdictionState Codes (97 total): [AK, AL, AR, AZ, CA, ...] |
| Currency | TypeKey | No | - | Currency | The currency for the claim, copied from the claim when the claim is archived. Always null for active claims. May also be null for pre 8.0 archived claims Codes (7 total): [usd, eur, gbp, cad, aud, ...] |
| LossLocation | OneToOne | No | LocationInfo | - | The loss location information for the archived claim. |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Contacts | ContactInfo | all the cached contacts (insured and claimant) for the archived claim |
| ClaimInAssociations | ClaimInAssociation | All the ClaimInAssociation entities for the Claim. |
| PeriodPolicies | PeriodPolicy | Array of PeriodPolicy beans associated with this ClaimInfo - only used internally for getting the PolicyPeriods off a Claim/Policy |
| ClaimAggregateLimitRpts | ClaimAggregateLimitRpt | Denormalized data for this claim per policyperiod. |
| Access | ClaimInfoAccess | The access control objects for this claim info. |
| CoverageLineMatchData | CoverageLineMatchDataInfo | Contains the coverage specifications for which at least one transaction exists on the archived claim. This is used to prevent future aggregate limits from being applied to coverage specifications where an archived claim's transaction would contribute, since it would no longer be possible to calculate the contribution of the archived claim. |

---

### Entity: ClaimContact

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimContact.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\ClaimContact.etx`
**Entity Type:** `retireable`
**Database Table:** `claimcontact`
**Supertype:** None
**Description:** Table linking contacts to claims and exposures.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| ContactProhibited | bit | No | - | - | Default: false Indicates whether contact is prohibited with this contact. |
| ClaimantFlag | bit | No | - | - | Denorm field indicating whether or not this ClaimContact has the role of claimant. |
| Claim | ForeignKey | Yes | Claim | - | Claim with which the contact is associated. |
| Contact | ForeignKey | Yes | Contact | - | Contact associated with the claim or exposure. |
| Policy | ForeignKey | No | Policy | - | Policy with which the contact is associated. |
| ContactValidFrom_Ext | datetime | No | - | - | [Extension] Start Date when this Contact is valid on this claim  |
| ContactValidTo_Ext | datetime | No | - | - | [Extension] Date when this Contact is no longer valid on this claim |
| BenefitEndDate_Ext | datetime | No | - | - | [Extension] Benefit end date |
| BenefitEndReason_Ext | shorttext | No | - | - | [Extension] Reason benefits ended (deprecated in favor of BenefitEndReasonType) |
| Service_Ext | mediumtext | No | - | - | [Extension] The service provided by contact |
| BenefitEndReasonType_Ext | TypeKey | No | - | BenefitEndReasonType | [Extension] Reason benefits ended - typelist |
| DependentType_Ext | TypeKey | No | - | DependentType | [Extension] Type of dependent - spouse, child etc. |
| EssentialServiceType_Ext | TypeKey | No | - | EssentialServiceType | [Extension] Type essential service provided by contact |
| ProviderType_Ext | TypeKey | No | - | ProviderType | [Extension] Provider type |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Roles | ClaimContactRole | The roles that this claimcontact has. |

---

### Entity: ClaimContactRole

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimContactRole.eti`
**Entity Type:** `retireable`
**Database Table:** `claimcontactrole`
**Supertype:** None
**Description:** Join table linking claimcontacts with their roles.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Active | bit | Yes | - | - | Default: true True if this contact is still active in its role for this claim or exposure. |
| Comments | shorttext | No | - | - | Comments about this role on the claimcontact. |
| PartyNumber | integer | No | - | - | Number of the party in the list of parties. |
| WitnessPerspective | varchar | No | - | - | WitnessPerspective |
| ClaimContact | ForeignKey | Yes | ClaimContact | - | The claimcontact with the given role. |
| Evaluation | ForeignKey | No | Evaluation | - | The evaluation with which the contact is associated, if any. |
| Exposure | ForeignKey | No | Exposure | - | The exposure with which the contact is associated, if any. |
| Matter | ForeignKey | No | Matter | - | The legal matter with which the contact is associated, if any. |
| Negotiation | ForeignKey | No | Negotiation | - | The negotiation with which the contact is associated, if any. |
| Policy | ForeignKey | No | Policy | - | The policy with which the contact is associated, if any. |
| Incident | ForeignKey | No | Incident | - | The incident with which the contact is associated, if any. |
| Role | TypeKey | Yes | - | contactrole | The role of the contact in relation to the claim, exposure, or matter. Codes (91 total): [checkpayee, negcontact, claimant, other, recoverypayer, ...] |
| CoveredPartyType | TypeKey | No | - | CoveredPartyType | The type of covered party. Codes: [addinsured, addnamedinsured] |
| WitnessStatementInd | TypeKey | No | - | YesNo | Indicator for whether witness gave statement or not Codes: [Yes, No, Unknown] |
| WitnessPosition | TypeKey | No | - | WitnessPosition | Where was the witness when the accident happened? Codes: [0, 1, 2, 3] |

---

### Entity: ClaimAccess

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimAccess.eti`
**Entity Type:** `versionable`
**Database Table:** `claimaccess`
**Supertype:** None
**Description:** Records information about users and groups that are allowed to access a claim.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Claim | ForeignKey | Yes | Claim | - | A foreign key to the claim. |

---

### Entity: Policy

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Policy.eti`
**Entity Type:** `retireable`
**Database Table:** `policy`
**Supertype:** None
**Description:** Insurance policy.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| AssignedRisk | bit | No | - | - | The policy is an Assigned risk from the state or not. |
| CancellationDate | datetime | No | - | - | Date on which the policy was canceled. |
| OrigEffectiveDate | datetime | No | - | - | First effective date on which the policyholder had coverage. |
| EffectiveDate | datetime | No | - | - | Date on which the policy is effective. |
| ExpirationDate | datetime | No | - | - | Date on which the policy expires. |
| FinancialInterests | shorttext | No | - | - | Other financial interests of note. |
| ForeignCoverage | bit | No | - | - | Whether the insured has foreign coverage. |
| Notes | shorttext | No | - | - | Other notes on the policy. |
| OtherInsInfo | shorttext | No | - | - | Notes about the insured's other insurance. |
| OtherInsurance | bit | No | - | - | Default: false Whether the insured has other insurance. |
| PolicyNumber | policynumber | Yes | - | - | Number of the policy (generally a string). |
| ProducerCode | shorttext | No | - | - | Agency that sold the policy. |
| Verified | bit | Yes | - | - | Default: false True if no non-internal fields have been changed since this policy was retrieved from external system. |
| TotalVehicles | integer | No | - | - | Default: 0 Total number of vehicles on the master version of the policy. |
| TotalProperties | integer | No | - | - | Default: 0 Total number of properties on the master version of the policy. |
| PolicySuffix | shorttext | No | - | - | Indicates each unique period that a policy has been in effect.  (Sometimes called 'Mod' or 'Module.') |
| AccountNumber | account | No | - | - | Account number that this Policy belongs to. |
| PolicySystemPeriodID | longint | No | - | - | The id of an associated external policy system period. |
| InsuredSICCode | varchar | No | - | - | The insured's SIC code (for workers' comp policies only). |
| WCStates | shorttext | No | - | - | States in which coverage applies (for workers' comp policies only). |
| WCOtherStates | shorttext | No | - | - | Other states in which coverage applies (for workers' comp policies only). |
| ReturnToWorkPrgm | bit | No | - | - | Default: false Return to work program (for workers' comp policies only). |
| Participation | percentagedec | No | - | - | Participation percentage (for commercial policies only). |
| ReportingDate | datetime | No | - | - | Extended reporting date for policies with extended coverage (for commercial policies only). |
| RetroactiveDate | datetime | No | - | - | Retroactive date for policies with retroactive coverage (for commercial policies only). |
| CustomerServiceTier | TypeKey | No | - | CustomerServiceTier | Service tier behind this policy Codes: [silver, gold, platinum] |
| PolicySource | TypeKey | No | - | PolicySource | Source of the policy information. Codes: [Manual, Automated] |
| Status | TypeKey | No | - | PolicyStatus | Status of the policy. Codes (7 total): [inforce, expired, paymentpastdue, archived, canceled, ...] |
| Currency | TypeKey | Yes | - | Currency | The Currency of the policy. When set, the new value is also propagated to Claim.Currency. Codes (7 total): [usd, eur, gbp, cad, aud, ...] |
| PolicyType | TypeKey | Yes | - | PolicyType | Type of policy. Codes (14 total): [PersonalAuto, BusinessAuto, CommercialPackage, GeneralLiability, HOPHomeowners, ...] |
| ValidationLevel | TypeKey | No | - | ValidationLevel | Validation level that this object passed (if any) before it was stored. Codes: [loadsave, iso, external] |
| UnderwritingCo | TypeKey | No | - | UnderwritingCompanyType | Underwriting company. Codes: [parent, child1, child2] |
| UnderwritingGroup | TypeKey | No | - | UnderwritingGroupType | Underwriting group. Codes (9 total): [acme_auto, succeed_auto, acme_prop, succeed_prop, acme_wc, ...] |
| PolicyRatingPlan | TypeKey | No | - | PolicyRatingPlan | Policy's rating plan (for workers' comp policies only). Codes (7 total): [GuaranteedCost, SlidingScaleDiv, IncurredLossRat, PaidLossRetro, Deductible, ...] |
| CoverageForm | TypeKey | No | - | CoverageForm | Policy's coverage form. Codes: [Occurrence, PriorActs, ClmsMdRtr, ClmsMdRtrExt, ClmsMdNoRtr, ClmsMdNoRtrExt] |
| Claim | OneToOne | No | Claim | - | The claim that references this policy. |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Contacts | ClaimContact | List of contacts associated with this policy. |
| Coverages | PolicyCoverage | List of coverages directly related to the policy. |
| Endorsements | Endorsement | List of endorsements for the policy. |
| StatCodes | StatCode | List of stat lines associated with the policy. |
| RiskUnits | RiskUnit | List of risk units covered by the policy. |
| Roles | ClaimContactRole | The roles that this claimcontact has. |
| ClassCodes | ClassCode | List of class codes covered by the Policy. |
| PolicyLocations | PolicyLocation | The list of all Locations available for use on this Policy. |

---

### Entity: PolicyCoverage

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\PolicyCoverage.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** Coverage
**Description:** Coverage associated directly with a policy.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: VehicleCoverage

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\VehicleCoverage.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** RUCoverage
**Description:** Coverage associated with a vehicle.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| NonmedAggLimit | nonnegativecurrencyamount | No | - | - | The dollar limit for all PIP Non-Medical coverage. |
| ReplaceAggLimit | nonnegativecurrencyamount | No | - | - | The dollar limit for all PIP Lost Wage and Replacement Services coverage. |
| PersonAggLimit | nonnegativecurrencyamount | No | - | - | The per person dollar limit for all PIP coverage. |
| ClaimAggLimit | nonnegativecurrencyamount | No | - | - | The per incident dollar limit for all PIP coverage. |

---

### Entity: PropertyCoverage

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\PropertyCoverage.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** RUCoverage
**Description:** Coverage associated with a property.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Coinsurance | percentagedec | No | - | - | Co-insurance percentage. |
| CoverageBasis | TypeKey | No | - | CoverageBasis | Coverage basis. Codes: [Replacement, ACV] |

---

### Entity: PolicyLocation

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\PolicyLocation.eti`
**Entity Type:** `retireable`
**Database Table:** `policylocation`
**Supertype:** None
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| PrimaryLocation | bit | Yes | - | - | Default: false Indicates whether this PolicyLocation should be considered the primary one on the owning Policy. |
| LocationNumber | shorttext | No | - | - | The alphanumeric "number" associated with this location. |
| Notes | shorttext | No | - | - | Any notes associated with this location. |
| PolicySystemId | policysystemid | No | - | - | Identifier for the policy location in an external policy system |
| Address | ForeignKey | No | Address | - | The address where this PolicyLocation exists. |
| Policy | ForeignKey | No | Policy | - | This PolicyLocation's owning Policy. |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Buildings | Building | Buildings associated with this location. |
| HighValueItems | PropertyItem | List of additional high value items. |
| Lienholders | PropertyOwner | List of lienholders for the property. |
| LocationBasedRisks | LocationBasedRU | List of location based risk units for the property. |

---

### Entity: Endorsement

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Endorsement.eti`
**Entity Type:** `retireable`
**Database Table:** `endorsement`
**Supertype:** None
**Description:** Endorsement.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Comments | shorttext | No | - | - | Other notes on the endorsement. |
| Description | shorttext | No | - | - | Description of the endorsement. |
| EffectiveDate | datetime | No | - | - | Date on which the endorsement is effective. |
| ExpirationDate | datetime | No | - | - | Date on which the endorsement expires. |
| FormNumber | varchar | No | - | - | Date and version of the legal document. |
| PolicySystemId | policysystemid | No | - | - | Identifier for the endorsement in an external policy system |
| Policy | ForeignKey | Yes | Policy | - | Policy with which the endorsement is associated. |

---

### Entity: StatCode

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\StatCode.eti`
**Entity Type:** `retireable`
**Database Table:** `statcode`
**Supertype:** None
**Description:** Statistical code (also known as a statistical line).

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| LineNumber | integer | Yes | - | - | Statistical data line number. |
| LocationNumber | varchar | No | - | - | Location number with which this stat line is associated. |
| BuildingNumber | varchar | No | - | - | Building number with which this stat line is associated. |
| VehicleNumber | varchar | No | - | - | Vehicle number with which this stat line is associated. |
| ClassCode | varchar | No | - | - | Workers comp class code with which this stat line is associated. |
| Notes | shorttext | No | - | - | Description of the endorsement. |
| Policy | ForeignKey | Yes | Policy | - | Policy with which the statistical code is associated. |
| InsuranceLine | TypeKey | No | - | InsuranceLine | Insurance line (also known as major line or bureau). Codes (16 total): [comm_auto_liab, comm_auto_phys, comm_auto_noflt, businessowners, comm_property, ...] |
| InsuranceSubLine | TypeKey | No | - | InsuranceSubLine | Insurance sub-line (also known as risk group or risk unit). Codes (27 total): [med_pay, uninsured, underinsured, auto_std, auto_non_std, ...] |
| State | TypeKey | No | - | State | State in which the statistical code applies. Codes (142 total): [AK, AL, AR, AZ, CA, ...] |
| MajorPeril | TypeKey | No | - | MajorPerils | Major peril. Codes (27 total): [bodily_injury, prop_damage, med_pay, uninsured_bi, under_insured_bi, ...] |

---

### Entity: ClassCode

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClassCode.eti`
**Entity Type:** `retireable`
**Database Table:** `classcode`
**Supertype:** None
**Description:** Employment class code (for workers' comp only).

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Code | employmentclassification | Yes | - | - | Class code. |
| Comments | shorttext | No | - | - | Other notes on the class code. |
| Description | shorttext | No | - | - | Description of the class code. |
| Policy | ForeignKey | Yes | Policy | - | Policy with which the class code is associated. |

---

### Entity: Contact

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Contact.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\Contact.etx`
**Entity Type:** `retireable`
**Database Table:** `contact`
**Supertype:** None
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
| PrimaryLanguage | TypeKey | No | - | LanguageType | The account's preferred language Codes: [de, en_US, es, fr, it, ja] |
| PrimaryLocale | TypeKey | No | - | LocaleType | The account's preferred locale Codes (8 total): [en_US, en_GB, en_CA, en_AU, fr_CA, ...] |
| ValidationLevel | TypeKey | No | - | ValidationLevel | Validation level that this object passed (if any) before it was stored. Codes: [loadsave, iso, external] |
| PreferredCurrency | TypeKey | No | - | Currency | The contact's preferred currency. Codes (7 total): [usd, eur, gbp, cad, aud, ...] |
| AutoSync | TypeKey | No | - | AutoSync | A status code to indicate whether this entity allows auto-sync or not. Null means disallow. Codes: [Disallow, Allow, Suspended] |
| Fingerprint | OneToOne | No | ContactFingerprint | - | One-to-one link |
| W9Received_Ext | bit | No | - | - | [Extension] Has W-9 form been received |
| W9ReceivedDate_Ext | datetime | No | - | - | [Extension] W-9 form received date |
| W9ValidFrom_Ext | datetime | No | - | - | [Extension] W-9 valid start date |
| W9ValidTo_Ext | datetime | No | - | - | [Extension] W-9 valid to date |
| OrganizationType_Ext | TypeKey | No | - | OrganizationType | [Extension] Type of organization |
| SpecialtyType_Ext | TypeKey | No | - | SpecialtyType | [Extension] Specialty of the doctor |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| ContactAddresses | ContactAddress | Secondary addresses associated with the contact. |
| SourceRelatedContacts | ContactContact | Contacts that point to this contact. |
| TargetRelatedContacts | ContactContact | Contacts that this Contact points to. |
| OfficialIDs | OfficialID | TaxIDs associated with this contact |
| CategoryScores | ContactCategoryScore | List of categories and their average scores, associated with this Contact. |
| Tags | ContactTag | List of ContactTags. |
| Reviews_Ext | Review | [Extension] Reviews for Service Provider Management |
| EFTRecords_Ext | EFTData | [Extension] Electronic Funds Transfer data for the contact |

---

### Entity: Person

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Person.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\Person.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** Contact
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
| LicenseState | TypeKey | No | - | Jurisdiction | Driver's license jurisdiction. Codes (97 total): [AK, AL, AR, AZ, CA, ...] |
| MaritalStatus | TypeKey | No | - | MaritalStatus | Marital status. Codes (7 total): [single, married, divorced, widowed, common, ...] |
| Prefix | TypeKey | No | - | NamePrefix | Prefix for the person's name. Codes: [mr, mrs, ms, dr] |
| Suffix | TypeKey | No | - | NameSuffix | Suffix for the person's name. Codes (10 total): [jr, sr, c_Ir, c_II, c_III, ...] |
| TaxFilingStatus | TypeKey | No | - | TaxFilingStatusType | State-specific field. Codes: [single, married-joint, married-separate, headofhousehold, widow] |
| VisaNumber_Ext | varchar | No | - | - | [Extension] Workers' Comp only. Employee Employment Visa Number |
| GreenCardNumber_Ext | varchar | No | - | - | [Extension] Workers' Comp only. Employee Green Card Number |
| PassportNumber_Ext | varchar | No | - | - | [Extension] Workers' Comp only. Employee Passport Number |
| JurisdictionAssignedID_Ext | varchar | No | - | - | [Extension] Workers' Comp only. Employee ID Assigned by Jurisdiction |
| SSNReleaseAuthorized_Ext | bit | No | - | - | [Extension] Workers' Comp only. SSN Release Authorized |
| TaxExemptionsEntitled_Ext | decimal | No | - | - | [Extension] Workers' Comp only. Tax Exemptions Entitled. |
| EmployeeSecurityID_Ext | varchar | No | - | - | [Extension]  A unique number designated by the jurisdiction to be used in conjunction with or in the place of the Employee ID. If the jurisdiction requires the Employee Security ID, the jurisdiction must return the Employee Security ID in the acknowledgment to promote future reporting of the designated value. |
| EducationLevel_Ext | varchar | No | - | - | [Extension] Workers' Comp only. The highest number of years or equivalency level of formal education completed. |
| ClaimantIDType_Ext | TypeKey | No | - | ClaimantIDType | [Extension] Workers' Comp only. Claimant ID Type |

---

### Entity: Company

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Company.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** Contact
**Description:** Represents an company/business as a primary subtype of Contact.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: Address

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Address.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\Address.etx`
**Entity Type:** `retireable`
**Database Table:** `address`
**Supertype:** None
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

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ContactAddress.eti`
**Entity Type:** `joinarray`
**Database Table:** `contactaddress`
**Supertype:** None
**Description:** Table linking contacts to addresses.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Address | ForeignKey | Yes | Address | - | Associated address. |
| Contact | ForeignKey | Yes | Contact | - | Associated contact. |

---

### Entity: PersonVendor

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\PersonVendor.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** Person
**Description:** Contact type representing vendors that are individual persons.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: CompanyVendor

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\CompanyVendor.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** Company
**Description:** Contact type representing vendors that are companies.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: AutoRepairShop

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\AutoRepairShop.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** CompanyVendor
**Description:** Represents an automobile repair shop (most typically, an autobody shop) as a CompanyVendor.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| AutoRepairLicense | varchar | No | - | - | Auto repair shop business license number |

---

### Entity: AutoTowingAgcy

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\AutoTowingAgcy.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** CompanyVendor
**Description:** Represents an automobile towing service as a CompanyVendor.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| AutoTowingLicense | varchar | No | - | - | Auto towing agency business license number |

---

### Entity: MedicalCareOrg

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\MedicalCareOrg.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** CompanyVendor
**Description:** Represents a medical care organization (hospital, clinic, or similar) as a CompanyVendor.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| MedicalOrgSpecialty | TypeKey | No | - | SpecialtyType | Medical specialty Codes (28 total): [allergy, anesthesiology, cardiology, dermatology, emergencymed, ...] |

---

### Entity: Doctor

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\Doctor.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PersonVendor
**Description:** Represents a doctor as a type of PersonVendor.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| MedicalLicense | varchar | No | - | - | Doctor's medical license number. |
| DoctorSpecialty | TypeKey | No | - | SpecialtyType | Doctor's medical specialty Codes (28 total): [allergy, anesthesiology, cardiology, dermatology, emergencymed, ...] |

---

### Entity: Attorney

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\Attorney.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PersonVendor
**Description:** Represents an attorney as a type of PersonVendor.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| AttorneyLicense | varchar | No | - | - | Attorney's business license number. |
| AttorneySpecialty | TypeKey | No | - | LegalSpecialty | Attorney's specialty Codes: [personalinjury, motorvehliability, generalliability, workerscomp] |

---

### Entity: LawFirm

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\LawFirm.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** CompanyVendor
**Description:** Represents a law firm as a type of CompanyVendor.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| LawFirmSpecialty | TypeKey | No | - | LegalSpecialty | Law firm specialty Codes: [personalinjury, motorvehliability, generalliability, workerscomp] |

---

### Entity: Incident

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Incident.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\Incident.etx`
**Entity Type:** `retireable`
**Database Table:** `incident`
**Supertype:** None
**Description:** Report of an incident related to a claim.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Description | mediumtext | No | - | - | General description of the incident. |
| AssessmentName | varchar | No | - | - | The name or subject of this negotiation. |
| AssessmentComment | shorttext | No | - | - | Assessment Comment |
| AssessmentTargetCloseDate | datetime | No | - | - | Date when this Assessment is expected to be complete |
| AssessmentCloseDate | datetime | No | - | - | Date when this Assessment is complete |
| IncludeLineItems | bit | No | - | - | Boolean field to indicate if assessmentitems are utilized |
| IncludeContentLineItems | bit | No | - | - | Boolean field to indicate if assessmentcontentitems are utilized |
| Claim | ForeignKey | Yes | Claim | - | Claim to which this incident is related. |
| InternalUser | ForeignKey | No | User | - | Internal User |
| AssessmentStatus | TypeKey | No | - | AssessmentStatus | AssessmentStatus Codes: [Open, Closed] |
| AssessmentType | TypeKey | No | - | AssessmentType | AssessmentType Codes: [Property, Contents, Auto] |
| Severity | TypeKey | No | - | SeverityType | Severity of the loss. Codes (19 total): [minor, moderate-gen, moderate-auto, moderate-prop, major-gen, ...] |
| LossParty | TypeKey | No | - | LossPartyType | The loss party; generally either first- or third-party loss. Codes: [insured, third_party] |
| LossEstimate_Ext | nonnegativecurrencyamount | No | - | - | [Extension] Estimated cost of the loss. |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Roles | ClaimContactRole | The contacts and their roles associated with this incident. |
| SourceLine | AssessmentSource | A source for this assessment. |
| ItemLine | AssessmentItem | A list of line items for this assessment. |
| ContentItemLine | AssessmentContentItem | A list of line items for this assessment. |
| Exposures | Exposure | A list of exposures for this incident |
| ServiceRequests_Ext | ServiceRequest | [Extension] Service requests associated with this incident. |

---

### Entity: VehicleIncident

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\VehicleIncident.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\VehicleIncident.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** MobilePropertyIncident
**Description:** Report of an incident involving a vehicle.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| HitAndRun | bit | No | - | - | Boolean field to indicate if a claim involves hit and run |
| OwnerRetainingSalvage | bit | No | - | - | Boolean field to indicate if Owner will retain the salvaged car or not |
| PhantomVehicle | bit | No | - | - | Unknown 3rd party vehicle involved or not(e.g. Hit and Run). |
| RecoveryLocation | ForeignKey | No | Address | - | The Address at which the recovery was made. |
| Vehicle | ForeignKey | No | Vehicle | - | Vehicle associated with the incident. |
| OwnersPermission_Ext | bit | No | - | - | [Extension] Whether the vehicle was driven with the owner's permission. |
| RentalAgency_Ext | varchar | No | - | - | [Extension] Vehicle Rental Agency. Deprecated: No longer used in the base configuration.  The equivalent of this field in 8.0 is the Specialist of a ServiceRequest with the 'Auto - Other - Car rental' service. |
| RentalBeginDate_Ext | datetime | No | - | - | [Extension] Date the vehical rental begins |
| RentalDailyRate_Ext | nonnegativecurrencyamount | No | - | - | [Extension] Vehicle Rental Daily Rate |
| RentalEndDate_Ext | datetime | No | - | - | [Extension] date the vehicle rental ends |
| RentalRequired_Ext | bit | No | - | - | [Extension] Indicator for vehicle rental requirement.  Deprecated: No longer used in the base configuration.  The equivalent of a true value for this field in 8.0 is the presence of a ServiceRequest with the 'Auto - Other - Car rental' service. |
| RentalReserveNo_Ext | varchar | No | - | - | [Extension] Vehicle rental Reservation Number |
| Speed_Ext | speed | No | - | - | [Extension] Speed of vehicle at impact, in MPH. |
| VehicleLocation_Ext | shorttext | No | - | - | [Extension] Current location of the vehicle. |
| VehicleOperable_Ext | bit | No | - | - | [Extension] Indicator to state if a vehicle is operable or not |
| VehicleParked_Ext | bit | No | - | - | [Extension] Was the vehicle parked at the time of the loss? |
| Appraisal_Ext | bit | No | - | - | [Extension] Indicator for Appraisal |
| BodyShopSelected_Ext | bit | No | - | - | [Extension] Indicator for Body Shop information |
| EquipmentFailure_Ext | bit | No | - | - | [Extension] Whether or not equipment failure was involved in the accident |
| MovePermission_Ext | bit | No | - | - | [Extension] Whether permission to move the vehicle has been received |
| VehicleDriveable_Ext | bit | No | - | - | [Extension] VehicleDriveable is deprecated. Use VehicleOperable instead |
| AirbagsDeployed_Ext | bit | No | - | - | [Extension] Whether or not airbags deployed |
| VehicleAge5Years_Ext | bit | No | - | - | [Extension] Vehicle Five Years Old? |
| VehicleAge10Years_Ext | bit | No | - | - | [Extension] Vehicle Ten Years Old? |
| Mileage100K_Ext | bit | No | - | - | [Extension] Mileage over 100K? |
| Extrication_Ext | bit | No | - | - | [Extension] Extrication Required? |
| VehicleRollOver_Ext | bit | No | - | - | [Extension] Vehicle Roll Over? |
| FireBurnDash_Ext | bit | No | - | - | [Extension] Fire Burn the Dash? |
| FireBurnEngine_Ext | bit | No | - | - | [Extension] Fire Burn the Engine? |
| FireBurnWindshield_Ext | bit | No | - | - | [Extension] Fire Burn the Windshield? |
| VehicleSubmerged_Ext | bit | No | - | - | [Extension] Vehicle Fully Submerged? |
| WaterLevelDash_Ext | bit | No | - | - | [Extension] Water Level Reach Dash? |
| FloodSaltWater_Ext | bit | No | - | - | [Extension] Flood Occur Salt Water? |
| WaterLevelSeats_Ext | bit | No | - | - | [Extension] Water Level Reach Seats? |
| ComponentsMissing_Ext | bit | No | - | - | [Extension] Major Components Missing? |
| InteriorMissing_Ext | bit | No | - | - | [Extension] Any Of The Interior Missing? |
| AirbagsMissing_Ext | bit | No | - | - | [Extension] Airbags Missing? |
| TotalLossPoints_Ext | integer | No | - | - | [Extension] Total Loss Calculated Points |
| TotalLoss_Ext | bit | No | - | - | [Extension] Whether the the vehicle is a total loss. |
| VehTowedInd_Ext | bit | No | - | - | [Extension] Deprecated: No longer used in the base configuration.  The equivalent of a true value for this field in 8.0 is the presence of a ServiceRequest with the 'Auto - Other - Towing service'. |
| RepWhereDisInd_Ext | bit | No | - | - | [Extension] Repaired where disabled indicator.  Deprecated: No longer used in the base configuration.  The equivalent of a true value for this field in 8.0 is the presence of a ServiceRequest with the 'Auto - Inspect / Repair - Auto body' service. |
| Collision_Ext | bit | No | - | - | [Extension] Whether vehicle was involved in a collision? |
| LocationInd_Ext | bit | No | - | - | [Extension] Whether vehicle location is different from insured's address?  Deprecated: No longer used in the base configuration.  The equivalent of this field in 8.0 is the ServiceAddress of a ServiceRequestInstruction with the 'Auto - Inspect / Repair - Auto body' service. |
| StorageFeeAmt_Ext | nonnegativecurrencyamount | No | - | - | [Extension]  |
| StorageFclty_Ext | varchar | No | - | - | [Extension]  |
| VehicleACV_Ext | nonnegativecurrencyamount | No | - | - | [Extension] Vehicle's actual cash value |
| SalvageCompany_Ext | varchar | No | - | - | [Extension]  |
| LotNumber_Ext | varchar | No | - | - | [Extension]  |
| DateSalvageAssigned_Ext | datetime | No | - | - | [Extension] Date assignment made to salvage team |
| DateVehicleRecovered_Ext | datetime | No | - | - | [Extension] Whether vehicle has been recovered |
| DateVehicleSold_Ext | datetime | No | - | - | [Extension] Whether vehicle has been sold |
| SalvageProceeds_Ext | currencyamount | No | - | - | [Extension] Amount vehicle was sold for |
| SalvageTow_Ext | currencyamount | No | - | - | [Extension] Towing fee |
| SalvageStorage_Ext | currencyamount | No | - | - | [Extension] Salvage storage |
| SalvageNet_Ext | currencyamount | No | - | - | [Extension] Net salvage recovery |
| SalvagePrep_Ext | currencyamount | No | - | - | [Extension] Vehicle prep fees |
| SalvageTitle_Ext | currencyamount | No | - | - | [Extension] Title fees |
| VehStolenInd_Ext | bit | No | - | - | [Extension] Vehicle stolen Indicator |
| VehLockInd_Ext | bit | No | - | - | [Extension] Vehicle locked Indicator |
| AntiThftInd_Ext | bit | No | - | - | [Extension] Vehicle equipped with anti-theft device Indicator |
| OdomRead_Ext | nonnegativeinteger | No | - | - | [Extension] Odometer reading |
| RecovDate_Ext | datetime | No | - | - | [Extension] Date the vehicle was recovered |
| CollisionPoint_Ext | TypeKey | No | - | CollisionPoint | [Extension] Point of first impact. |
| DriverRelation_Ext | TypeKey | No | - | PersonRelationType | [Extension] Relationship of the driver to the insured. This is redundant for a first-party loss. |
| DriverRelToOwner_Ext | TypeKey | No | - | PersonRelationType | [Extension] Relationship of the driver to the vehicle's owner. This is redundant for a first-party loss. |
| VehicleDirection_Ext | TypeKey | No | - | VehicleDirection | [Extension] Direction the vehicle was traveling at impact. |
| VehicleUseReason_Ext | TypeKey | No | - | ReasonForUse | [Extension] Reason for vehicle use |
| VehiclePolStatus_Ext | TypeKey | No | - | VehiclePolicyStatus | [Extension] Policy Status of Vehicle |
| VehicleType_Ext | TypeKey | No | - | VehicleType | [Extension] How the vehicle is related to the insured |
| TrafficViolation_Ext | TypeKey | No | - | YesNo | [Extension] Did the vehicle involved in the accident violate traffic? |
| CitationIssued_Ext | TypeKey | No | - | YesNo | [Extension] An indicator if there are citations. |
| VehicleTitleReqd_Ext | TypeKey | No | - | YesNo | [Extension]  |
| VehicleTitleRecvd_Ext | TypeKey | No | - | YesNo | [Extension]  |
| MinorOnPolicy_Ext | TypeKey | No | - | YesNo | [Extension] If the driver involved in accident is a minor, is he/she listed in the policy? |
| PercentageDrivenByMinor_Ext | TypeKey | No | - | PercentageDriven | [Extension] % of time vehicle used by the minor |
| VehCondType_Ext | TypeKey | No | - | VehCondType | [Extension]  |
| StorageAccrInd_Ext | TypeKey | No | - | YesNo | [Extension]  |
| AffdvCmplInd_Ext | TypeKey | No | - | YesNo | [Extension] Affidavit completed Indicator |
| RecovInd_Ext | TypeKey | No | - | YesNo | [Extension] Recovery Indicator |
| RecovState_Ext | TypeKey | No | - | State | [Extension] State (aka Territory) where the vehicle upon recovery |
| RecovCondType_Ext | TypeKey | No | - | RecovCondType | [Extension] Describes which general condition of vehicle upon recovery |
| RecovClassType_Ext | TypeKey | No | - | RecovClassType | [Extension] Describes which parts or recovered vehicle were stripped |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Citations_Ext | Citation | [Extension] Extension child collection |

---

### Entity: FixedPropertyIncident

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\FixedPropertyIncident.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\FixedPropertyIncident.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PropertyIncident
**Description:** Report of an incident involving a fixed property - usually a building

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Property | ForeignKey | No | PolicyLocation | - | The property involved in the incident. |
| OccupancyType | TypeKey | No | - | OccupancyType | Where the property in question is occupied. Codes: [vacant, underConst, occupied] |
| NumStories_Ext | nonnegativeinteger | No | - | - | [Extension] Number of Stories in the building/property |
| FireProtDetails_Ext | varchar | No | - | - | [Extension] dummy field for fire details |
| NumSprinkler_Ext | nonnegativeinteger | No | - | - | [Extension] Number of Sprinklers at Scene |
| NumSprinkOper_Ext | nonnegativeinteger | No | - | - | [Extension] Number of sprinklers that were operated |
| ClassType_Ext | TypeKey | No | - | ClassType | [Extension] Property attribute class type for Building details |
| RoofMaterial_Ext | TypeKey | No | - | RoofMaterial | [Extension] Roof Deck Materials for property |
| ExtWallMat_Ext | TypeKey | No | - | ExtWallMat | [Extension] External Wall material at scene. |
| LossArea_Ext | TypeKey | No | - | LossArea | [Extension] Loss Area of Property |
| AlarmType_Ext | TypeKey | No | - | AlarmType | [Extension] Alarm Type for property |
| SprinklerType_Ext | TypeKey | No | - | SprinklerType | [Extension] Sprinkler type for property |
| SprinkRetServ_Ext | TypeKey | No | - | SprinkRetServ | [Extension] Sprinklers returned to service. |
| MoldInvolved_Ext | TypeKey | No | - | YesNo | [Extension] Was Mold Involved? |
| HazardInvolved_Ext | TypeKey | No | - | YesNo | [Extension] Was Hazardous Waste Involved? |

---

### Entity: InjuryIncident

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\InjuryIncident.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\InjuryIncident.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** Incident
**Description:** Report of an incident involving a bodily injury.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| ClaimIncident | bit | No | - | - | True for the one InjuryIncident per claim that holds injury fields formerly on Claim, for Workers Comp. |
| AmbulanceUsed | bit | No | - | - | Ambulance arrived during the loss or not. |
| LostWages | bit | No | - | - | True if the injured person lost wages as a result of the injury. |
| Impairment | percentagedec | No | - | - | Percentage impairment. |
| GeneralInjuryType | TypeKey | No | - | InjuryType | High-level categorization of the injury. Codes: [multiple, occupational, specific] |
| DetailedInjuryType | TypeKey | No | - | DetailedInjuryType | Detailed Injury category. Codes (54 total): [01, 02, 03, 04, 07, ...] |
| MedicalTreatmentType | TypeKey | No | - | MedicalTreatmentType | Type of treatment received. Codes (21 total): [acup, chir, counsel, emer_care, er, ...] |
| DisabledDueToAccident | TypeKey | No | - | DisabledDueToAccident | For non-WC, to characterize the disability. Codes: [partdisabled, totaldisabled, notdisabled] |
| ReturnToModWorkValid_Ext | bit | No | - | - | [Extension] True indicates that Modified Duty is applicable for this injured person and will be tracked |
| ReturnToModWorkDate_Ext | datetime | No | - | - | [Extension] the Return to Modified Work date for this claim, if ReturnToModWorkActual is true, this date is actual, otherwise it is projected  |
| ReturnToModWorkActual_Ext | bit | No | - | - | [Extension] If true, the field, ReturnToModWorkDate, is actual; if false, then date is projected  |
| ReturnToWorkValid_Ext | bit | No | - | - | [Extension] True indicates that Return to Work will be tracked for this person |
| ReturnToWorkDate_Ext | datetime | No | - | - | [Extension] the Return to Work date for this claim, if ReturnToWorkActual is true, this date is actual, otherwise it is projected  |
| ReturnToWorkActual_Ext | bit | No | - | - | [Extension] If true, the field, ReturnToWorkDate, is actual; if false, then date is projected  |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| BodyParts | BodyPartDetails | Details of body parts injured. |
| InjuryDiagnoses | InjuryDiagnosis | All ICD codes associated with this incident |

---

### Entity: PropertyContentsIncident

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\PropertyContentsIncident.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\PropertyContentsIncident.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** MobilePropertyIncident
**Description:** Report of an incident involving property contents. For example contents of a home, outbuilding etc

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| PropertyLocation | ForeignKey | No | PolicyLocation | - | The property location for the incident. |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| PropertyContentsScheduledItems | PropertyContentsScheduledItem | Affected scheduled items, selected from the high value property items listed on the policy |

---

### Entity: DwellingIncident

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\DwellingIncident.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\DwellingIncident.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** FixedPropertyIncident
**Description:** Report of an incident involving a dwelling

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| MaterialsDamaged | varchar | No | - | - | Materials damaged as a result of the incident, for instance, floor, walls etc. |
| DamagedAreaSize | positiveinteger | No | - | - | Size of the damaged area in sq. feet, sq. meters or other units of measurement |
| PropertySize | positiveinteger | No | - | - | Size of the property in sq. feet, sq. meters or other units of measurement |
| YearsInHome | nonnegativeinteger | No | - | - | Number of years the insured has owned the home |
| NumberOfPeopleOnPolicy | nonnegativeinteger | No | - | - | Number of people on the policy |
| YearBuilt | datetime | No | - | - | Year the property was built |
| FireProtectionAvailable | bit | No | - | - | Is fire protection available |
| EMSInd | bit | No | - | - | Emergency Management Service requested.  Deprecated: No longer used in the base configuration.  The equivalent of a true value for this field in 8.0 is the presence of a ServiceRequest with the 'Home services - Emergency services - Make safe' service. |
| DebrisRemovalInd | bit | No | - | - | Debris Removal Service requested.  Deprecated: No longer used in the base configuration.  The equivalent of a true value for this field in 8.0 is the presence of a ServiceRequest with the 'Property - Emergency services - Debris removal' service. |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| DwellingRoomDamages | DwellingRoomDamage | Information about rooms damaged as a result of the incident. |

---

### Entity: OtherStructureIncident

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\OtherStructureIncident.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\OtherStructureIncident.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** FixedPropertyIncident
**Description:** Report of an incident involving a secondary structure

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| FencesDamaged | bit | No | - | - | Whether fences were damaged |

---

### Entity: LivingExpensesIncident

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\LivingExpensesIncident.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\LivingExpensesIncident.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PropertyIncident
**Description:** Report of an incident involving the loss of use of propery.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| StartDate | datetime | No | - | - | The date for which the insured started staying at the lodging provider. |

---

### Entity: MobilePropertyIncident

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\MobilePropertyIncident.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\MobilePropertyIncident.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PropertyIncident
**Description:** Report of an incident involving some kind of mobile property - vehicle, personal property but not a building.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| LossDesc_Ext | varchar | No | - | - | [Extension] Loss occurred if Other is selected Description needed. |
| LocationAddress_Ext | ForeignKey | No | Address | - | [Extension] Location address of the incident. Previous fields that made up this address described as 'Location of the Exposed Vehicle'. |
| LossOccured_Ext | TypeKey | No | - | LossOccured | [Extension] Where Loss occurred |

---

### Entity: BaggageIncident

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\BaggageIncident.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\BaggageIncident.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** MobilePropertyIncident
**Description:** Report of an incident involving some kind of baggage 

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| DelayOnly | bit | No | - | - | Indicates if this is a delay only loss |
| BaggageMissingFrom | datetime | No | - | - | The date/time the baggage was discovered to be missing |
| BaggageRecoveredOn | datetime | No | - | - | The date/time the baggage was recovered |
| CarrierCompensated | bit | No | - | - | Indicates if the carrier compensated the claimant for the baggage loss or delay |
| CarrierCompensatedAmount | nonnegativecurrencyamount | No | - | - | Amount the carrier compensated for the baggage loss or delay |
| RelatedTripRU | ForeignKey | No | TripRU | - | Related trip |
| BaggageType | TypeKey | No | - | BaggageType | Type of baggage Codes (9 total): [trunk, suitcase, tote, duffel, laptopbag, ...] |

---

### Entity: TripIncident

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\TripIncident.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\TripIncident.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** Incident
**Description:** Report of an incident involving a trip or travel

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| TripRU | ForeignKey | No | TripRU | - | Related risk unit for this incident |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| TripSegments | TripSegment | All trip segments associated with this policy |
| TripAccommodations | TripAccommodation | All trip accommodations associated with this policy |

---

### Entity: Exposure

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Exposure.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\Exposure.etx`
**Entity Type:** `retireable`
**Database Table:** `exposure`
**Supertype:** None
**Description:** An exposure is a discrete piece of a claim that involves a single type of loss (for example, vehicle damage or bodily injury) to a specific claimant.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| ClaimOrder | integer | Yes | - | - | Order of the exposure on the claim. |
| OtherCoverage | bit | No | - | - | True if the claimant has additional coverage. |
| OtherCoverageInfo | varchar | No | - | - | Information regarding additional coverage. |
| SettleDate | datetime | No | - | - | Date of settlement. |
| ReOpenDate | datetime | No | - | - | The last time an exposure was reopened. |
| MetricLimitGeneration | integer | No | - | - | Generation number, used to identify the limits for this exposure's metrics |
| BreakIn | bit | No | - | - | Whether there is evidence of a break-in. |
| DepreciatedValue | nonnegativecurrencyamount | No | - | - | Depreciated value of property or vehicle. |
| Locked | bit | No | - | - | Whether the property or vehicle was properly locked. |
| ReplacementValue | nonnegativecurrencyamount | No | - | - | Replacement value of the property or vehicle. |
| AverageWeeklyWages | positivecurrencyamount | No | - | - | Average weekly wages; this calculation differs by state. |
| WageStmtSent | datetime | No | - | - | Wage Statement sent date. |
| WageStmtRecd | datetime | No | - | - | Wage Statement received date. |
| LastDayWorked | datetime | No | - | - | Last day worked. |
| ExaminationDate | datetime | No | - | - | Date of the Examination. |
| TreatedPatientBfr | bit | No | - | - | Whether the the patient has been treated before. |
| DiagnosticCnsistnt | bit | No | - | - | Whether the diagnostic is consistent. |
| CurrentConditions | bit | No | - | - | Current conditions. |
| FurtherTreatment | bit | No | - | - | Whether further treatment is required. |
| HospitalDate | datetime | No | - | - | Date admitted to the hospital. |
| HospitalDays | integer | No | - | - | Estimated days in hospital. |
| WCPreexDisblty | bit | No | - | - | Default: false Whether the injured person had a pre-existing disability. |
| WCPreexDisbltyInfo | varchar | No | - | - | Information about the pre-existing disability. |
| SSDIEligible | bit | No | - | - | Whether the exposure is eligible for SSDI. |
| WCBenefit | bit | No | - | - | Whether Workers Compensation benefits are being collected. |
| SSBenefit | bit | No | - | - | Whether Social Security benefits are being collected. |
| WageBenefit | bit | No | - | - | Whether wage benefites are being collected. |
| ContactPermitted | bit | No | - | - | Default: true Whether contact is permitted with the claimant. |
| ExposureLimitReached | bit | No | - | - | Whether the exposure's exposure limit has been exceeded. |
| IncidentLimitReached | bit | No | - | - | Whether the exposure's incident limit has been exceeded. |
| PIPNonMedAggLimitReached | bit | No | - | - | Whether the exposure's PIP Non Medical Aggregate limit has been exceeded. |
| PIPESSLimitReached | bit | No | - | - | Whether the exposure's PIP Replacement Services Aggregate limit has been exceeded. |
| PIPPersonAggLimitReached | bit | No | - | - | Whether the exposure's PIP Per Person Aggregate limit has been exceeded. |
| PIPClaimAggLimitReached | bit | No | - | - | Whether the exposure's PIP Claim Aggregate limit has been exceeded. |
| RIGroupSetExternally | bit | Yes | - | - | Default: false Whether the reinsurance association was determined by an external system. |
| Coverage | ForeignKey | No | Coverage | - | The specific coverage for this exposure. |
| Claim | ForeignKey | Yes | Claim | - | The Claim for this Exposure. |
| Incident | ForeignKey | No | Incident | - | Incident that caused this exposure. |
| StatLine | ForeignKey | No | StatCode | - | Statistical line associated with this exposure. |
| ClaimantDenorm | ForeignKey | No | Contact | - | The claimant for the exposure, denormalized from the claim's contact array. |
| RIAgreementGroup | ForeignKey | No | RIAgreementGroup | - | Reinsurance group associated with this exposure. |
| TempLocation | ForeignKey | No | Address | - | Temporary location of policy holder. This is for a homeowners claim. |
| DeathBenefits | ForeignKey | No | Benefits | - | Death benefits details. |
| LifePensionBenefits | ForeignKey | No | Benefits | - | Life Pension benefits details. |
| PPDBenefits | ForeignKey | No | Benefits | - | PPD benefits details. |
| PTDBenefits | ForeignKey | No | Benefits | - | PTD benefits details. |
| TPDBenefits | ForeignKey | No | Benefits | - | TPD benefits details. |
| TTDBenefits | ForeignKey | No | Benefits | - | TTD benefits details. |
| VocBenefits | ForeignKey | No | Benefits | - | Vocational benefits details. |
| CompBenefits | ForeignKey | No | Benefits | - | Compensation benefits details. |
| DisBenefits | ForeignKey | No | Benefits | - | Disability benefits details. |
| NewEmpData | ForeignKey | No | EmploymentData | - | Information about a new job that the claimant has taken. |
| PIPDeathBenefits | ForeignKey | No | Benefits | - | Death benefits details. |
| PIPVocBenefits | ForeignKey | No | Benefits | - | Vocational rehab benefits details. |
| PriorEmpData | ForeignKey | No | EmploymentData | - | Information about the job the claimant had at the time of injury. |
| RSBenefits | ForeignKey | No | Benefits | - | Replacement services benefits details. |
| SSDIBenefits | ForeignKey | No | Benefits | - | Social security disability benefits details. |
| WCBenefits | ForeignKey | No | Benefits | - | Workers' comp benefits details. |
| ExposureType | TypeKey | Yes | - | ExposureType | Types of exposure. Codes (19 total): [BodilyInjuryDamage, LostWages, WCInjuryDamage, PIPDamages, LossOfUseDamage, ...] |
| ClaimantType | TypeKey | No | - | ClaimantType | Categorizes the claimant relative to policyholder. Codes (14 total): [insured, householdmember, veh_ins_driver, veh_other_owner, veh_other_driver, ...] |
| ClosedOutcome | TypeKey | No | - | ExposureClosedOutcomeType | Outcome reached when closing the exposure. Codes: [completed, duplicate, paymentscomplete, mistake, fraud, unnecessary] |
| ReopenedReason | TypeKey | No | - | ExposureReopenedReason | The reason for reopening the exposure. Codes: [paymentdenied, mistake, newinfo] |
| CoverageSubType | TypeKey | No | - | CoverageSubtype | The coverage subtype. Codes (327 total): [GLCGLCov_ops_bi, GLCGLCov_ops_pd, GLCGLCov_ops_mp, GLCGLCov_ops_gd, GLCGLCov_prod_bi, ...] |
| JurisdictionState | TypeKey | No | - | Jurisdiction | State of jurisdiction, if different than location of loss. The Jurisdiction must be associated with JurisdictionType.TC_INSURANCE. Codes (97 total): [AK, AL, AR, AZ, CA, ...] |
| LossCategory | TypeKey | No | - | LossCategory | Detailed category of the exposure. Codes: [default] |
| LossParty | TypeKey | No | - | LossPartyType | The loss party; generally either first- or third-party loss. Codes: [insured, third_party] |
| LostPropertyType | TypeKey | No | - | LostPropertyType | ISO category of lost property, for theft losses. Codes (16 total): [Art, AudioVisual, Cash, Clothing, ComputerEquip, ...] |
| PrimaryCoverage | TypeKey | Yes | - | CoverageType | Coverage Type of the coverage on this exposure. Codes (292 total): [GLCGLCov, GLDeductible, GLPollutionDesignatedCov, GLPollutionShortTermCov, PollutionBroadLimited, ...] |
| Progress | TypeKey | No | - | ExposureProgressType | Description of the progress of an open exposure. Codes: [new, investigation, evaluation, settlement, litigation, pendingrecovery] |
| Segment | TypeKey | No | - | ClaimSegment | Segmentation type of the exposure. Both the claim and exposure may be segmented. Codes (22 total): [unknown, auto_low, auto_mid, auto_high, prop_low, ...] |
| SettleMethod | TypeKey | No | - | SettleMethod | Method of settlement. Codes: [lumpsum, lumpsumother, stipaward, dismissal, cacompromise, other] |
| State | TypeKey | Yes | - | ExposureState | Default: draft Internal state of the exposure. Codes: [draft, open, closed, exception] |
| Strategy | TypeKey | No | - | ClaimStrategy | Strategy type of the exposure. Both the claim and exposure may define a strategy. Codes (14 total): [unknown, auto_fast, auto_normal, prop_fast, prop_normal, ...] |
| OtherCovgChoice | TypeKey | No | - | YesNo | Whether there is other coverage. Codes: [Yes, No, Unknown] |
| ValidationLevel | TypeKey | No | - | ValidationLevel | Validation level the exposure has passed (if any). Codes: [loadsave, iso, external] |
| SecurityLevel | TypeKey | No | - | ExposureSecurityType | The security level of this exposure. |
| ExposureTier | TypeKey | No | - | ExposureTier | The tier of this exposure, used to decide how to rate the exposure metrics. Codes (21 total): [medical, indemnity, el, 1p_pd_low, 1p_pd_high, ...] |
| DaysInWeek | TypeKey | No | - | DaysInWeekType | Days in week used for benefit calculation. Codes: [five, seven] |
| ExposureRpt | OneToOne | No | ExposureRpt | - | The calculated financials data for this exposure. |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| RoleAssignments | UserRoleAssignment | The user role assignments for this exposure. |
| Documents | Document | The documents associated with this exposure; for example, FNOL accord form or police report. |
| ExposureSynchStates | ExposureSynchState | Sync states related to this exposure. |
| ExposureISOMatchReports | ExposureISOMatchReport | ISO match reports for this exposure. |
| Notes | Note | Notes particular to this exposure. Notes can also be associated with the claim in general. |
| OtherCoverageDet | OtherCoverageDetail | Details of other coverage. |
| ReserveLines | ReserveLine | ReserveLines relating to this exposure. |
| Transactions | Transaction | All financial transactions relating to this exposure.  For rules, it is much better to use one of the getXXXIterator() methods and for the UI it is much better to use one of the getXXXQuery() methods to retrieve all transactions or a specific subtype of Transactions for the exposure. |
| Text | ExposureText | Large text fields associated with exposure. |
| Roles | ClaimContactRole | The contacts and their roles associated with this exposure. |
| ExposureMetrics | ExposureMetric | Metrics related to this exposure. |
| BenefitPeriods | BenefitPeriod | Periods of time when employee received benefits. |
| Settlements | Settlement | Settlements with the employee. |
| MedicalActions | MedicalAction | Key medical-related dates. |
| IMEPerformed | IMEPerformed | Independent medical examinations performed. |
| Activities | Activity | Child collection |
| ServiceRequests_Ext | ServiceRequest | [Extension] Service requests associated with this exposure. |

---

### Entity: ReserveLine

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ReserveLine.eti`
**Entity Type:** `retireable`
**Database Table:** `reserveline`
**Supertype:** None
**Description:** A unique combination of Claim, Exposure, CostType and CostCategory against which reserves can be set and payments made.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Claim | ForeignKey | Yes | Claim | - | The related claim. |
| Exposure | ForeignKey | No | Exposure | - | The related exposure. |
| CostType | TypeKey | Yes | - | costtype | Type of cost (for example, LAE or claim cost). Codes: [claimcost, unspecified, aoexpense, dccexpense] |
| CostCategory | TypeKey | Yes | - | costcategory | The costcategory for this transaction. Codes (36 total): [unspecified, indemnity, legal, other, towing, ...] |
| ReservingCurrency | TypeKey | Yes | - | Currency | Reserving Currency of this ReserveLine. Indicates the currency in which reserves are to be set aside and eroded. Codes (7 total): [usd, eur, gbp, cad, aud, ...] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| TAccounts | TAccount | Child collection |
| Transactions | Transaction | Set of transactions that contribute to this ReserveLine. |
| RICodings | RICoding | Set of RICodings that reference this ReserveLine. |
| RecoveryCodings | RecoveryCoding | Set of RecoveryCodings that reference this ReserveLine. |

---

### Entity: TransactionSet

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\TransactionSet.eti`
**Entity Type:** `retireable`
**Database Table:** `transactionset`
**Supertype:** None
**Description:** A group of items submitted at once for approval.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Claim | ForeignKey | Yes | Claim | - | The claim entity to which this TransactionSet belongs. |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Documents | TransactionSetDocument | Set of documents linked to this transaction set. |
| Activities | Activity | Set of approval / approval denial activities linked to this transaction set. |

---

### Entity: ReserveSet

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ReserveSet.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** TransactionSet
**Description:** Subtype of TransactionSet that contains one or more reserve transactions submitted together for approval.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Reserves | Reserve | Reserves in the set. |

---

### Entity: CheckSet

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\CheckSet.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** TransactionSet
**Description:** A check submitted for approval.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Recurrence | ForeignKey | No | CheckRecurrence | - | The recurrence schedule for the check set, if it has one. |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Checks | Check | All checks contained in the check set. |
| CheckGroups | CheckGroup | The check groups of multi-payee checks contained in the check set, if any. |
| RecurringChecks | RecurringCheck | Recurring checks (if any) that make up this check set. |
| Reserves | CheckSetReserve | Reserves that should be approved or rejected along with the set. |

---

### Entity: RecoverySet

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\RecoverySet.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** TransactionSet
**Description:** A TransactionSet of one or more Recoveries created and submitted together for approval.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Recoveries | Recovery | The recoveries in the set. |

---

### Entity: RecoveryReserveSet

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\RecoveryReserveSet.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** TransactionSet
**Description:** A TransactionSet of one or more RecoveryReserves created and submitted together for approval.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| RecoveryReserves | RecoveryReserve | Recovery reserves in the set. |

---

### Entity: Transaction

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Transaction.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\Transaction.etx`
**Entity Type:** `retireable`
**Database Table:** `transaction`
**Supertype:** None
**Description:** Transaction (either reserve, payment, recovery, or recovery reserve) for a particular claim or exposure.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Comments | shorttext | No | - | - | Comments about the transaction, such as a reason. |
| BookingDate | datetime | No | - | - | Normally the Date and time when Transaction status was updated to Submitted. See Docs for other cases, such as when imported via Web Service or Staging Tables. |
| ReserveLine | ForeignKey | Yes | ReserveLine | - | The ReserveLine associated with this transaction.  For all transaction subtypes this ReserveLine will have matching Claim, Exposure, CostType and CostCategory. |
| Claim | ForeignKey | Yes | Claim | - | The related claim.<p>Setting the claim also sets this transaction's currency to the claim's currency if it is null. |
| Exposure | ForeignKey | No | Exposure | - | The related exposure. |
| TransactionSet | ForeignKey | Yes | TransactionSet | - | Set that groups together one or more transactions for approval. |
| TransToReservingExchangeRate | ForeignKey | No | ExchangeRate | - | ExchangeRate to use when converting TransactionAmount to ReservingAmount. Setting this value updates the reserving amounts. Also sets the same ExchangeRate as TransToClaimExchangeRate if ClaimCurrency and ReservingCurrency are equal. |
| TransToClaimExchangeRate | ForeignKey | No | ExchangeRate | - | ExchangeRate to use when converting TransactionAmount to ClaimAmount. Setting this value updates the claim and reporting amounts. Also sets the same ExchangeRate as TransToReservingExchangeRate if ClaimCurrency and ReservingCurrency are equal. |
| ClaimToReportingExchangeRate | ForeignKey | No | ExchangeRate | - | ExchangeRate to use when converting ClaimAmount to ReportingAmount. Setting this value updates the reporting amounts. |
| RecoveryCoding | ForeignKey | No | RecoveryCoding | - | The RecoveryCoding to which this transaction is coded. |
| Currency | TypeKey | Yes | - | Currency | The Currency of the transaction amount. Codes (7 total): [usd, eur, gbp, cad, aud, ...] |
| CostType | TypeKey | Yes | - | costtype | Type of cost (for example, claim cost or adjusting overhead). Codes: [claimcost, unspecified, aoexpense, dccexpense] |
| CostCategory | TypeKey | Yes | - | costcategory | The CostCategory for this transaction. Codes (36 total): [unspecified, indemnity, legal, other, towing, ...] |
| ReservingCurrency | TypeKey | Yes | - | Currency | Reserving Currency of this transaction's ReserveLine. Indicates the currency in which reserves are to be set aside and eroded. Codes (7 total): [usd, eur, gbp, cad, aud, ...] |
| OriginTransactionOnset | OneToOne | No | TransactionOnset | - | TransactionOnset join entity pointing to this Transaction as an Onset. |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| LineItems | TransactionLineItem | Set of line items that further categorize the transaction amount. |
| Offsets | TransactionOffset | Transactions that offset this transaction. A transaction should have at most one item in this array. This array is applicable only to a payment or recovery. |
| Onsets | TransactionOnset | Transactions that onset this transaction. This array is applicable only to a payment or recovery. |
| TAccountTransactions | TAccountTransaction | Set of T-account transactions that make up the lifecycle of this Transaction. |
| RecTAccountTransactions | RecTAccountTransaction | Set of T-account transactions that make up the lifecycle of this Transaction. Only applicable to Recoveries and RecoveryReserves. |

---

### Entity: Reserve

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Reserve.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** Transaction
**Description:** A reserve transaction (any transaction that designates money for payments).

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| OffsetPayments | PaymentReserve | The payments for which this reserve is the offset.  Should only be one. |

---

### Entity: Payment

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Payment.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\Payment.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** Transaction
**Description:** A payment transaction.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| CloseExposure | bit | No | - | - | Default: false If this transaction is a final payment, this indicates whether it should or did close its associated exposure. |
| CloseClaim | bit | No | - | - | Default: false If this transaction is a final payment, this indicates whether it should or did close its associated claim. |
| DoesNotErodeReserves | bit | Yes | - | - | Default: false Indicates whether this payment should not erode reserves for its ReserveLine.  This field can only be set in the CheckWizard UI.  Otherwise, one of the setAsEroding() or setAsNonEroding() methods must be called from a rule to change whether a payment erodes reserves. |
| Check | ForeignKey | Yes | Check | - | Check that paid this payment. |
| Matter | ForeignKey | No | Matter | - | Foreign key to Matter |
| PaymentType | TypeKey | Yes | - | paymenttype | Type of the payment. Codes: [partial, final, supplement] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| OffsettingReserves | PaymentReserve | The reserve created to offset this payment, whether to zero reserves or keep reserves from becoming negative.  Should only be one. |

---

### Entity: Recovery

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Recovery.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** Transaction
**Description:** A recovery transaction.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| ClaimContact | ForeignKey | No | ClaimContact | - | Person or company from whom the recovery was obtained. |
| PayerDenorm | ForeignKey | No | Contact | - | Payer FK denorm. |
| OBOClaimContact | ForeignKey | No | ClaimContact | - | Person or company responsible for paying. |
| OffsettingRecoveryReserve | ForeignKey | No | RecoveryReserve | - | The RecoveryReserve, if any, that exists as a direct offset for this Recovery. |
| RecoveryCategory | TypeKey | Yes | - | RecoveryCategory | The RecoveryCategory to which this transaction is coded. Codes: [unspecified, salvage, subro, credit_loss, credit_exp, deductible] |

---

### Entity: RecoveryReserve

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\RecoveryReserve.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** Transaction
**Description:** A recovery reserve transaction; indicates an expected recovery.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| RecoveryCategory | TypeKey | Yes | - | RecoveryCategory | The RecoveryCategory to which this transaction is coded. Codes: [unspecified, salvage, subro, credit_loss, credit_exp, deductible] |

---

### Entity: Check

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Check.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\Check.etx`
**Entity Type:** `retireable`
**Database Table:** `check`
**Supertype:** None
**Description:** Groups one or more payments together for payment by a single check.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| CheckNumber | shorttext | No | - | - | The check or EFT identifier. |
| Comments | shorttext | No | - | - | Comments about the check, such as a reason it was voided. |
| DateOfService | datetime | No | - | - | Date that the service was performed (if this check is for a service). |
| EnteredTime | datetime | No | - | - | The time the check was created. This is different from CreateTime, which is the time it was stored in the system. |
| InvoiceNumber | shorttext | No | - | - | Invoice number associated with the check. |
| IssueDate | datetime | No | - | - | Date the check was issued. |
| MailTo | shorttext | No | - | - | Name of the person/company to whom the check should be mailed. |
| Memo | shorttext | No | - | - | Memo to include on the check. |
| PayTo | shorttext | No | - | - | Pay to the order of. |
| ReportableAmount | currencyamount | No | - | - | Reportable amount of the check in the transaction currency. Used by the BackupWithholdingCalculator as the amount of the check reportable to the IRS, from which it calculates backup withholding Deductions. It is editable in the UI. |
| ScheduledSendDate | dateonly | No | - | - | Date that the check is scheduled to be sent.  Also used to determine if the check amount is included in Future Payments (tomorrow or later).  Should only be modified in the UI or PreSetup rules. |
| ServicePdEnd | datetime | No | - | - | End date of the service period for the check. |
| ServicePdStart | datetime | No | - | - | Start date of the service period for the check. |
| PendEscalationForBulk | bit | No | - | - | Only escalate as part of a BulkInvoice. |
| Portion | ForeignKey | No | CheckPortion | - | The amount of a multi-payee check applicable to this check. |
| Group | ForeignKey | No | CheckGroup | - | CheckGroup this check belongs to, if it's part of a multi-payee check. |
| CheckSet | ForeignKey | Yes | CheckSet | - | CheckSet this Check belongs to. |
| ClaimContact | ForeignKey | No | ClaimContact | - | Claimant the check is being written for, as a ClaimContact. |
| Claim | ForeignKey | Yes | Claim | - | The related claim. |
| RecurringCheck | ForeignKey | No | RecurringCheck | - | The recurring check entity, if any, associated with this check. |
| BulkInvoiceItemInfo | ForeignKey | No | BulkInvoiceItemInfo | - | If this check was created to act as a record-keeper for a bulk invoice item, this is the item it references. |
| MailingAddress | ForeignKey | No | Address | - | Address of the person/company to whom the check should be mailed. This represents an Address entity. |
| VoidStopUser | ForeignKey | No | User | - | User that requested void or stop of the check |
| BankAccount | TypeKey | No | - | bankaccount | Source bank account. Codes: [default] |
| CheckBatching | TypeKey | No | - | checkbatching | How the check should be batched for sending. Codes: [apdefault, bulkcheck] |
| CheckInstructions | TypeKey | No | - | checkhandlinginstructions | Special handling instructions for the check. Codes: [default, hold] |
| CheckType | TypeKey | Yes | - | CheckType | Role of the check in the check group (primary or secondary). Codes: [primary, secondary] |
| DeductionType | TypeKey | No | - | DeductionType | Deduction type for secondary checks.  Always NULL for primary checks. Codes (8 total): [irs, lawyer, child_support, dependent, other_lien, ...] |
| DeliveryMethod | TypeKey | No | - | deliverymethod | Requested delivery method. Codes: [send, hold, no_check_needed] |
| PaymentMethod | TypeKey | No | - | paymentmethod | Requested payment method for all payments in the check. Codes: [manual, check, eft, instant] |
| Reportability | TypeKey | No | - | ReportabilityType | Whether the payment should be reported to the IRS as income. Codes: [notreportable, reportable] |
| Status | TypeKey | Yes | - | TransactionStatus | Status of the check (issued, voided, cleared, and so on). Do not update directly. Use methods to initiate operations, or use updateCheckStatus() method. Codes (20 total): [draft, pendingapproval, awaitingsubmission, submitting, requesting, ...] |
| CheckRpt | OneToOne | No | CheckRpt | - | The calculated data for this check. |
| MailToAddress_Ext | shorttext | No | - | - | [Extension] Address of the person/company to whom the check should be mailed. |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Deductions | Deduction | Any deductions related to the check. |
| Payees | CheckPayee | Recipients of the payment; there must be at least one. If there are multiple, each is a 'joint' payee. |
| Payments | Payment | Payments on the check. |
| ServiceRequestInvoices | ServiceRequestInvoice | ServiceRequestInvoices related to this check. All linked invoices are expected to have the same service request specialist and currency. |

---

### Entity: CheckPayee

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\CheckPayee.eti`
**Entity Type:** `joinarray`
**Database Table:** `checkpayee`
**Supertype:** None
**Description:** Links a Check to a Contact that is a Payee of the check.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Check | ForeignKey | Yes | Check | - | The check. |
| ClaimContact | ForeignKey | Yes | ClaimContact | - | The payee as a ClaimContact. |
| PayeeDenorm | ForeignKey | No | Contact | - | Payee FK denorm |
| PayeeType | TypeKey | Yes | - | contactrole | The payee type. This is used for tax reporting purposes. Codes (91 total): [checkpayee, negcontact, claimant, other, recoverypayer, ...] |

---

### Entity: CheckPortion

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\CheckPortion.eti`
**Entity Type:** `retireable`
**Database Table:** `checkportion`
**Supertype:** None
**Description:** Indicates the amount of a multi-payee check that applies to a particular check.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Percentage | percentagedec | No | - | - | The percentage to allocate towards the check. Setting this clears the fixed amount properties |
| FixedTransactionAmount | currencyamount | No | - | - | The fixed amount (in the transaction currency) to allocate towards the check. Setting this clears Percentage and updates FixedClaimAmount and FixedReportingAmount. At least one check must be added to this CheckPortion before setting this. |
| FixedClaimAmount | currencyamount | No | - | - | The fixed amount (in the claim currency) to allocate towards the check. |
| FixedReservingAmount | currencyamount | No | - | - | The fixed amount (in the reserving currency) to allocate towards the check. |
| FixedReportingAmount | currencyamount | No | - | - | The fixed amount (in the reporting currency) to allocate towards the check. |
| Reissued | bit | Yes | - | - | Default: false Flag indicating whether this portion was created for a reissued check. |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Checks | Check | Checks whose amounts are defined by this CheckPortion. If there are multiple checks in this array, all of them must belong to the same CheckRecurrence. |

---

### Entity: Deductible

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Deductible.eti`
**Entity Type:** `retireable`
**Database Table:** `deductible`
**Supertype:** None
**Description:** Amount to deduct from payments.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Amount | nonnegativecurrencyamount | Yes | - | - | Default: 0 Deductible amount to be applied to a payment. |
| Waived | bit | Yes | - | - | Default: false Specifies whether this deductible has been waived. |
| Overridden | bit | Yes | - | - | Default: false Specifies whether this deductible has been overriden. |
| EditReason | shorttext | No | - | - | Reason for editing (override or waive) the deductible. |
| Coverage | ForeignKey | No | coverage | - | The coverage, if any, whose deductible this entity represents. |
| Claim | ForeignKey | Yes | claim | - | The claim on which this deductible was created. |
| Currency | TypeKey | Yes | - | Currency | Codes (7 total): [usd, eur, gbp, cad, aud, ...] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| TransactionLineItems | TransactionLineItem | The TransactionLineItems applied to this deductible. |

---

### Entity: Activity

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Activity.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\Activity.etx`
**Entity Type:** `retireable`
**Database Table:** `activity`
**Supertype:** None
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
| ValidationLevel | TypeKey | No | - | ValidationLevel | Validation level that this object passed (if any) before it was stored. Codes: [loadsave, iso, external] |

---

### Entity: ActivityPattern

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ActivityPattern.eti`
**Entity Type:** `retireable`
**Database Table:** `activitypattern`
**Supertype:** None
**Description:** An activity pattern is a template for an activity. An activity pattern is not assigned to a user, nor does it belong to a claim; it is used only to create new activity instances. To create a new activity, an activity pattern is first chosen, and the values in the activity pattern are used to seed the values of the new activity instance.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| AutomatedOnly | bit | Yes | - | - | Default: false True if the activity pattern is used only by automated additions to the workplan. If true, the pattern won't be shown as an option for users to choose in the application's interface. |
| Description | mediumtext | No | - | - | Description of the activity pattern. |
| EscalationDays | integer | No | - | - | Used in conjunction with EscalationStartPoint and EscalationIncludedDays to calculate the EscalationDate of the activity. |
| EscalationHours | integer | No | - | - | Used in conjunction with EscalationStartPoint and EscalationIncludedDays to calculate the EscalationDate of the activity. |
| Command | mediumtext | No | - | - | A Gosu command to execute for this activity. |
| DocumentTemplate | shorttext | No | - | - | The id of an associated document template. The id gets passed to IDocumentTemplateSource to retrieve the DocumentTemplateDescriptor. |
| EmailTemplate | shorttext | No | - | - | The id of an associated email template. The id gets passed to IEmailTemplateSource to retrieve the EmailTemplateDescriptor. |
| Mandatory | bit | Yes | - | - | Default: false Whether completion of the activity is mandatory. |
| Code | varchar | No | - | - | The concise name of the activity pattern, used to identify the pattern within rules. |
| Recurring | bit | Yes | - | - | Default: false Whether this activity is recurring. |
| Subject | shorttext | No | - | - | Subject field of the activity. |
| ShortSubject | varchar | No | - | - | Short subject field of the activity. For use in small areas e.g., a calendar event entry. |
| TargetDays | integer | No | - | - | Used in conjunction with TargetStartPoint and TargetIncludedDays to calculate the ActionDate of the activity. |
| TargetHours | integer | No | - | - | Used in conjunction with TargetStartPoint and TargetIncludedDays to calculate the ActionDate of the activity. |
| EscBusCalLocPath | shorttext | No | - | - | Location bean path to use for business calendar in calculating EscalationDate, if applicable. |
| TargetBusCalLocPath | shorttext | No | - | - | Location bean path to use for business calendar in calculating TargetDate, if applicable. |
| Category | TypeKey | No | - | ActivityCategory | Category used to organize the activity pattern. Codes (19 total): [approval, correspondence, interview, newmail, reminder, ...] |
| ActivityClass | TypeKey | Yes | - | ActivityClass | Default: task The class of the activity. Codes: [task, event] |
| EscalationStartPt | TypeKey | No | - | StartPointType | Which existing date on the activity or associated claim to use as the starting date for the EscalationDate. Codes: [activitycreation, startdate, claimnotice, lossdate] |
| TargetStartPoint | TypeKey | No | - | StartPointType | Which existing date on the activity or associated claim to use as the starting date for the TargetDate. Codes: [activitycreation, startdate, claimnotice, lossdate] |
| EscalationInclDays | TypeKey | No | - | IncludeDaysType | Which days to include in calculating the EscalationDate. Codes: [elapsed, businessdays] |
| EscalationBusCalTag | TypeKey | No | - | HolidayTagCode | Holiday tag code to use for business calendar in calculating EscalationDate, if applicable. Codes: [general, FederalHolidays, CompanyHolidays] |
| TargetIncludeDays | TypeKey | No | - | IncludeDaysType | Which days to include in calculating the TargetDate. Codes: [elapsed, businessdays] |
| TargetBusCalTag | TypeKey | No | - | HolidayTagCode | Holiday tag code to use for business calendar in calculating TargetDate, if applicable. Codes: [general, FederalHolidays, CompanyHolidays] |
| Priority | TypeKey | No | - | Priority | Priority of the activity with respect to other activities. Codes: [urgent, high, normal, low] |
| Type | TypeKey | Yes | - | ActivityType | Default: general Type of the activity. Codes: [general, approval, assignmentreview, approvaldenied] |

---

### Entity: Note

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Note.eti`
**Entity Type:** `retireable`
**Database Table:** `note`
**Supertype:** None
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
| Topic | TypeKey | No | - | notetopictype | Default: general Topic to which the note belongs. Codes (12 total): [general, fnol, coverage, investigation, medical, ...] |
| SecurityType | TypeKey | No | - | NoteSecurityType | Type of note; used for access-restriction purposes Codes: [public, private, sensitive, medical] |
| Language | TypeKey | No | - | LanguageType | The language in which this note is created. Codes: [de, en_US, es, fr, it, ja] |

---

### Entity: Document

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Document.eti`
**Entity Type:** `retireable`
**Database Table:** `document`
**Supertype:** None
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
| Section | TypeKey | No | - | documentsection | The section to which this document belongs, if any. Codes (8 total): [bills, medical, indemnity, rehab, legal, ...] |
| SecurityType | TypeKey | No | - | documentsecuritytype | Type of document used for access-restriction purposes, in conjunction with the information in security-config.xml. Codes: [unrestricted, sensitive] |
| Type | TypeKey | No | - | documenttype | The specific type of the document, if any. Codes (12 total): [diagram, email, policereport, repairestimate, fnol, ...] |
| Language | TypeKey | No | - | LanguageType | The language in which this document is created. Codes: [de, en_US, es, fr, it, ja] |

---

### Entity: UserRoleAssignment

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\UserRoleAssignment.eti`
**Entity Type:** `retireable`
**Database Table:** `userroleassign`
**Supertype:** None
**Description:** Claim-level user role assignment.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Claim | ForeignKey | Yes | Claim | - | The claim. |
| Exposure | ForeignKey | No | Exposure | - | The associated exposure, if any. |

---

### Entity: User

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\User.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\User.etx`
**Entity Type:** `retireable`
**Database Table:** `user`
**Supertype:** None
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
| Language | TypeKey | No | - | LanguageType | User's preferred language. Codes: [de, en_US, es, fr, it, ja] |
| Locale | TypeKey | No | - | LocaleType | User's preferred locale. Codes (8 total): [en_US, en_GB, en_CA, en_AU, fr_CA, ...] |
| DefaultCountry | TypeKey | No | - | Country | User's default country Codes (243 total): [unknown, AF, AL, DZ, AS, ...] |
| DefaultPhoneCountry | TypeKey | No | - | PhoneCountryCode | User's default phone country Codes (245 total): [AC, AD, AE, AF, AG, ...] |
| TimeZone | TypeKey | No | - | TimeZoneType | User's time zone. Codes (9 total): [US.Eastern, US.East-Indiana, US.Central, US.Mountain, US.Arizona, ...] |
| ExperienceLevel | TypeKey | No | - | UserExperienceType | Experience level of the user. Codes: [low, mid, high] |
| SystemUserType | TypeKey | No | - | SystemUserType | Indicates the type of special system users (for example, default claim owner). This is null for regular users. Codes: [sysadmin, defaultowner, sysservices] |
| VacationStatus | TypeKey | Yes | - | VacationStatusType | Default: atwork The vacation status of this user. Codes: [atwork, onvacation, inactive] |
| ValidationLevel | TypeKey | No | - | ValidationLevel | Validation level that this object passed (if any) before it was stored. Codes: [loadsave, iso, external] |
| UserUIPreferences | OneToOne | No | UserUIPreferences | - | One-to-one link |
| OffsetStatsUpdateTime_Ext | datetime | No | - | - | [Extension] Extension field |
| NewlyAssignedActivities_Ext | integer | No | - | - | [Extension] Extension field |
| LossType_Ext | TypeKey | No | - | LossType | [Extension] High level claim type (for example, Auto or Property). |
| PolicyType_Ext | TypeKey | No | - | PolicyType | [Extension] High level policy type (for example, Auto or Property). |
| QuickClaim_Ext | TypeKey | No | - | QuickClaimDefault | [Extension] Default quick claim values categorized by LossType. |

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

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Group.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\Group.etx`
**Entity Type:** `retireable`
**Database Table:** `group`
**Supertype:** None
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
| GroupType | TypeKey | Yes | - | GroupType | Type of group (describes its function). Codes (41 total): [root, autofasttrack, autonormal, autocomplex, propfasttrack, ...] |
| ValidationLevel | TypeKey | No | - | ValidationLevel | Validation level that this object passed (if any) before it was stored. Codes: [loadsave, iso, external] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Users | GroupUser | Users belonging to this group. |
| Regions | GroupRegion | Regions associated with this group. |
| AssignableQueues | AssignableQueue | Assignment queues associated with this group. |

---

### Entity: Matter

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Matter.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\Matter.etx`
**Entity Type:** `retireable`
**Database Table:** `matter`
**Supertype:** None
**Description:** The set of data organized around a single lawsuit or potential lawsuit.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Name | varchar | Yes | - | - | Then name for this matter. Typically of the form 'X vs. Y' once the matter goes to trial. |
| CaseNumber | varchar | No | - | - | Official reference number for the lawsuit |
| Room | varchar | No | - | - | Room number in the venue. |
| DeclaratoryJgmt | bit | No | - | - | Whether the court has been asked to make a declaratory judgment. |
| Arbitration | bit | No | - | - | Whether a suit has gone into arbitration. |
| StructuredSettle | bit | No | - | - | Whether this matter is a good candidate for structured settlement. |
| MotionSummaryJgmt | bit | No | - | - | Whether this matter has a motion for summary judgment. |
| MediationDate | datetime | No | - | - | Date this matter entered mediation. |
| TrialDate | datetime | No | - | - | Current schedule trial date. |
| FileDate | datetime | No | - | - | Date the trial was filed in court. |
| FinalLegalCost | nonnegativecurrencyamount | No | - | - | The final legal cost. |
| FinalSettleCost | nonnegativecurrencyamount | No | - | - | The final settlement cost. |
| FinalSettleDate | datetime | No | - | - | The actual date of the final settlement (as opposed to the date of the payment). |
| DefenseApptDate | datetime | No | - | - | Date the defense counsel was appointed to this matter. |
| SentToDefenseDate | datetime | No | - | - | Date this matter was sent to the defense attorney. |
| FirstNotice | bit | No | - | - | Whether the lawsuit was the first notice of the claim. |
| SubroRelated | bit | No | - | - | Boolean field to mark if Matter related to Subrogation |
| MatterCaseNumber | varchar | No | - | - | Case number |
| ArbitrationDate | datetime | No | - | - | Current schedule trial date. |
| HearingDate | datetime | No | - | - | Current scheduled matter hearing date |
| ArbitrationRoom | varchar | No | - | - | Room number in the arbitration venue. |
| HearingRoom | varchar | No | - | - | Room number in the hearing venue. |
| MediationRoom | varchar | No | - | - | Room number in the mediation venue. |
| DocketNumber | varchar | No | - | - | Court docket number |
| FilingDate | dateonly | No | - | - | Filing date |
| ServiceDate | dateonly | No | - | - | Service date |
| ResponseDue | dateonly | No | - | - | Response Due |
| ResponseFiled | dateonly | No | - | - | Response filed |
| AdDamnumSpecified | bit | No | - | - | Was Ad Damnum specified? |
| AdDamnumAmount | currencyamount | No | - | - | Ad Damnum Amount |
| PunitiveDamages | bit | No | - | - | Punitive damages? |
| PunitiveAmount | currencyamount | No | - | - | Punitive damages amount |
| Claim | ForeignKey | Yes | Claim | - | The claim associated with this legal matter. |
| SubrogationSummary | ForeignKey | No | SubrogationSummary | - | Subrogation information related to this matter. |
| SuitType | TypeKey | No | - | SuitType | The type of suit. Codes: [Insured, ThirdParty, FirstParty] |
| Resolution | TypeKey | No | - | ResolutionType | The type of resolution. Codes (34 total): [AD, AL, AM, AR, AW, ...] |
| ReopenedReason | TypeKey | No | - | MatterReopenedReason | The reason for reopening the matter. Codes: [mistake, newinfo, retrial] |
| PrimaryCause | TypeKey | No | - | PrimaryCauseType | Why the lawsuit was brought in the first place. Codes (9 total): [Delay, Predetermined, LowSettlement, BS, UD, ...] |
| RiskType | TypeKey | No | - | MatterRiskType | Describes the overall risk on this matter. Codes: [low, medium, high] |
| ValidationLevel | TypeKey | No | - | ValidationLevel | Validation level the matter passed (if any) the last time it was checked. Codes: [loadsave, iso, external] |
| MatterType | TypeKey | No | - | MatterType | Type of Matter such as General, Lawsuit, Arbitration, Hearing or Mediation Codes: [General, Lawsuit, Arbitration, Hearing, Mediation] |
| CourtType | TypeKey | No | - | MatterCourtType | Court type Codes: [state, federal, county] |
| CourtDistrict | TypeKey | No | - | MatterCourtDistrict | Court jurisdictional district Codes (52 total): [AK, AL, AR, AZ, CA, ...] |
| LegalSpecialty | TypeKey | No | - | LegalSpecialty | Legal specialty needed for this matter Codes: [personalinjury, motorvehliability, generalliability, workerscomp] |
| VenueRating | TypeKey | No | - | MatterVenueRating | Rating of venue for this matter Codes: [Favorable, Unfavorable, Unknown] |
| MethodServed | TypeKey | No | - | MatterMethodServed | Method served Codes: [CertifiedMail, Sheriff] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Exposures | MatterExposure | The list of exposures to which this matter relates. |
| StatusTypeLines | LitStatusTypeLine | The progression of status type lines on this matter. |
| Roles | ClaimContactRole | The roles that this claimcontact has. |
| BudgetLines | BudgetLine | An array of budget line records |

---

### Entity: MatterExposure

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\MatterExposure.eti`
**Entity Type:** `joinarray`
**Database Table:** `matterexposure`
**Supertype:** None
**Description:** Links an exposure to a legal matter.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Matter | ForeignKey | Yes | Matter | - | Related matter. |
| Exposure | ForeignKey | Yes | Exposure | - | Related exposure. |

---

### Entity: ServiceRequest

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ServiceRequest.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\ServiceRequest.etx`
**Entity Type:** `editable`
**Database Table:** `servicerequest`
**Supertype:** None
**Description:** A unit of work requested of a specialist or vendor

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| ServiceRequestNumber | shorttext | Yes | - | - | A globally-unique, user-readable identifier for this service request. This number is normally generated within ClaimCenter. |
| LatestChangeTimestampDenorm | datetime | Yes | - | - | The timestamp of the latest ServiceRequestChange in the History. This value is denormalized here for ease of ordering ServiceRequests in queries. This is non-nullable because History cannot be empty. |
| Claim | ForeignKey | Yes | Claim | - | The related claim. |
| Specialist | ForeignKey | Yes | Contact | - | The vendor or internal entity selected to do the work requested by this service request. |
| Instruction | ForeignKey | Yes | ServiceRequestInstruction | - | The active instruction associated with this service request. |
| OriginatingServiceRequest | ForeignKey | No | ServiceRequest | - | The originating quote-only service request for this service request. Note: This will be non-null only when a quote-only service request is promoted to a quote and service service request. |
| LatestQuote | ForeignKey | No | ServiceRequestQuote | - | The latest quote associated with this service request. It is null if no quote has been added to the service request |
| Currency | TypeKey | Yes | - | Currency | The currency of this service request, which is used for its quotes, invoices, and checks. Codes (7 total): [usd, eur, gbp, cad, aud, ...] |
| Progress | TypeKey | Yes | - | ServiceRequestProgress | This service request's current place in its life cycle. Codes (8 total): [requested, declined, specialistwaiting, inprogress, workcomplete, ...] |
| QuoteStatus | TypeKey | Yes | - | ServiceRequestQuoteStatus | The current quote status for this service request. Codes: [waitingforapproval, waitingforquote, approved, noquote, quoted] |
| Kind | TypeKey | Yes | - | ServiceRequestKind | The kind for this service request. Codes: [quoteandservice, quoteonly, serviceonly, unmanaged] |
| Tier | TypeKey | No | - | ServiceRequestTier | The tier of this service request. Codes: [high, medium, low] |
| ServiceRequestReferenceNumber_Ext | shorttext | No | - | - | [Extension] A string identifier assigned to this ServiceRequest by the specialist. The value of this field may only be meaningful to the specialist. |
| RequestedServiceCompletionDate_Ext | datetime | No | - | - | [Extension] Desired date by which the specialist will have completed the work, or null if the specialist has not indicated such a date. |
| RequestedQuoteCompletionDate_Ext | datetime | No | - | - | [Extension] Desired date by which the specialist will have submitted the quote, or null if the specialist has not indicated such a date. |
| CanceledReason_Ext | longtext | No | - | - | [Extension] The reason the service request was canceled |
| ExpectedQuoteCompletionDate_Ext | datetime | No | - | - | [Extension] Date by which the specialist expects to submit the quote, or null if the specialist has not indicated such a date. |
| ExpectedServiceCompletionDate_Ext | datetime | No | - | - | [Extension] Date by which the specialist expects to complete the work, or null if the specialist has not indicated such a date. |
| Incident_Ext | ForeignKey | No | Incident | - | [Extension] The incident that led to the work requested by this service request. |
| Exposure_Ext | ForeignKey | No | Exposure | - | [Extension] The exposure that led to the work requested by this service request. |
| SpecialistCommMethod_Ext | TypeKey | No | - | SpecialistCommMethod | [Extension] The channel through which the carrier will communicate with the specialist. |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| History | ServiceRequestChange | The changes that have been applied to this service request, which together comprise its history. |
| InstructionHistory | ServiceRequestInstruction | All instructions that have been created for this service request, including instructions that are no longer active. |
| ServiceRequestPromotions | ServiceRequestPromotion | Array of ServiceRequestPromotions linking this ServiceRequest to other ServiceRequests to which this was promoted. |
| DocumentLinks | ServiceRequestDocumentLink | The link information for documents associated with this service request |
| Quotes | ServiceRequestQuote | The Quotes associated with this service request |
| Invoices | ServiceRequestInvoice | The Invoices associated with this service request |
| Notes | Note | The notes associated with this service request |
| Activities | Activity | The activities associated with this service request |
| ServiceRequestMetrics | ServiceRequestMetric | Metrics related to this service request |
| Messages | ServiceRequestMessage | Messages related to this service request |

---

### Entity: ServiceRequestInstruction

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ServiceRequestInstruction.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\ServiceRequestInstruction.etx`
**Entity Type:** `editable`
**Database Table:** `servicerequestinstruction`
**Supertype:** None
**Description:** A set of instructions to be transmitted to the specialist who will work on a service request

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| ServiceRequest | ForeignKey | Yes | ServiceRequest | - | The service request for which the specialist is being instructed. |
| InstructionText_Ext | longtext | No | - | - | [Extension] Text instructions to be provided to the specialist. |
| CustomerContact_Ext | ForeignKey | Yes | Contact | - | [Extension] The contact with whom the specialist should coordinate to perform the work. In many cases, this will be the claimant. |
| ServiceAddress_Ext | ForeignKey | No | Address | - | [Extension] The location at which the service is to be performed; may be null if the location is implied by the specialist, such as if it will be performed at the specialist's place of business. |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Services | ServiceRequestInstructionService | The services to be performed for this set of instructions. |

---

### Entity: ServiceRequestQuote

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ServiceRequestQuote.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** ServiceRequestStatement
**Description:** A quote received from a specialist for a Service Request.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| ExpectedDaysToPerformService | integer | Yes | - | - | Number of business days the specialist expects it will take to perform the service. |

---

### Entity: ServiceRequestInvoice

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ServiceRequestInvoice.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\ServiceRequestInvoice.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** ServiceRequestStatement
**Description:** An invoice received from a specialist for a Service Request.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| PaymentDate | datetime | No | - | - | The time at which this invoice was paid. |
| PaidBy | ForeignKey | No | User | - | The user who paid this invoice. |
| Check | ForeignKey | No | Check | - | The check that paid this invoice. |
| Status | TypeKey | Yes | - | ServiceRequestInvoiceStatus | The current invoice status Codes: [waitingforapproval, approved, rejected, checkcreated, withdrawn] |

---

### Entity: ServiceRequestMessage

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ServiceRequestMessage.eti`
**Entity Type:** `editable`
**Database Table:** `servreqmsg`
**Supertype:** None
**Description:** Messages for Service Requests

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Title | shorttext | Yes | - | - | The title of the service request message |
| Body | longtext | Yes | - | - | The body of the service request message |
| SendDate | datetime | Yes | - | - | The date the message was sent |
| SentFromPortal | bit | Yes | - | - | If the message is sent from an external portal |
| ServiceRequest | ForeignKey | Yes | ServiceRequest | - | The Service Request related to this message |
| Author | ForeignKey | Yes | Contact | - | The author of the message |
| Type | TypeKey | Yes | - | ServiceRequestMessageType | The message type Codes: [info, question] |

---

### Entity: Catastrophe

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Catastrophe.eti`
**Entity Type:** `retireable`
**Database Table:** `catastrophe`
**Supertype:** None
**Description:** Catastrophe

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Active | bit | Yes | - | - | Default: true True if a catastrophe can be assigned to a new claim. |
| CatastropheNumber | varchar | No | - | - | Catastrophe number. |
| Description | shorttext | No | - | - | Description of the catastrophe. |
| Name | varchar | No | - | - | Name of the catastrophe. |
| ScheduleBatch | bit | No | - | - | Default: false Boolean field to mark a catastrophe to be run in the CatastropheClaimFinder batch process. |
| CatastropheValidFrom | datetime | No | - | - | Start date when this catastrophe is valid |
| CatastropheValidTo | datetime | No | - | - | Date when this catastrophe is no longer valid |
| Comments | shorttext | No | - | - | Comments regarding the Catastrophe |
| PCSCatastropheNumber | varchar | No | - | - | PCS catastrophe number from ISO data feed. |
| TopLeftLongitude | decimal | No | - | - | Longitude for the top left point of the area of interest, in degrees. |
| TopLeftLatitude | decimal | No | - | - | Latitude for the top left  point of the area of interest, in degrees. |
| BottomRightLongitude | decimal | No | - | - | Longitude for the bottom right point of the area of interest, in degrees. |
| BottomRightLatitude | decimal | No | - | - | Latitude for the bottom right point of the area of interest, in degrees. |
| PolicyEffectiveDate | datetime | No | - | - | Effective date for retrieving policy locations from the policy system. |
| PolicyRetrievalSetTime | datetime | No | - | - | Time when policy location retrieval parameters were last set. |
| PolicyRetrievalCompletionTime | datetime | No | - | - | Time when last policy retrieval location was completed. |
| Type | TypeKey | No | - | CatastropheType | Type of the catastrophe (for example, ISO or internal). Codes: [iso, internal] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Perils | CatastrophePeril | Details of perils associated with a catastrophe. |
| CatastropheZones | CatastropheZone | The zones that define this catastrophe. |
| ClaimsHistory | CatastropheClaimsHistory | History of the matched claims. |

---

### Entity: SubrogationSummary

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\SubrogationSummary.eti`
**Entity Type:** `retireable`
**Database Table:** `subrogationsummary`
**Supertype:** None
**Description:** Subrogation information related to a claim

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| ExtOwned | bit | No | - | - | Default: false To indicate Subro for a claim as owned by an external owner |
| EscalateSubro | bit | No | - | - | Default: false Escalate toSubro |
| SubroReferralDate | datetime | No | - | - | Date when when referral made to Subrogation |
| SubroReferralComment | shorttext | No | - | - | A Comment from the referer to the referee |
| ProrateDeductible | bit | Yes | - | - | Default: false Indicates whether deductible should be prorated |
| CalculateOSRecReserve | bit | No | - | - | Default: false Whether to automatically calculate OS Recovery Reserves |
| Claim | ForeignKey | Yes | Claim | - | Related Claim |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| StatuteLine | StatuteLimitationsLine | A list of applicable Statute of Limitations for this claim. |
| SubroAdverseParties | SubroAdverseParty | A list of applicable Adverse Parties related to for this claim. |
| Subrogations | Subrogation | The subrogations associated with this summary |

---

### Entity: SIUAnswerSet

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\SIUAnswerSet.eti`
**Entity Type:** `retireable`
**Database Table:** `siuanswerset`
**Supertype:** None
**Description:** Join table between the answer set and the claim, to allow for multiple SIU answer sets on the same claim

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| AnswerSet | ForeignKey | Yes | AnswerSet | - | Fk to the AnswerSet |
| Claim | ForeignKey | Yes | Claim | - | Fk to the Claim |

---

### Entity: SIUClaimIndicator

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\SIUClaimIndicator.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** ClaimIndicator
**Description:** SIU Claim Indicator

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: Evaluation

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Evaluation.eti`
**Entity Type:** `retireable`
**Database Table:** `evaluation`
**Supertype:** None
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Name | varchar | No | - | - | Then name or subject of this evaluation. |
| Amount | nonnegativecurrencyamount | No | - | - | Total evaluation amount. |
| InsuredLiability | percentagedec | No | - | - | Insured's liability percentage. |
| ClaimantLiability | percentagedec | No | - | - | Claimant's liability percentage. |
| OtherLiability | percentagedec | No | - | - | Other party's liability percentage. |
| HospitalER | nonnegativecurrencyamount | No | - | - | Hospital/Emergency Room cost. |
| TreatingPhysician | nonnegativecurrencyamount | No | - | - | Treating physician cost. |
| PhysicalTherapy | nonnegativecurrencyamount | No | - | - | Physical therapy cost. |
| Diagnostic | nonnegativecurrencyamount | No | - | - | Diagnostic cost - for example, x-ray. |
| MedicalEquipment | nonnegativecurrencyamount | No | - | - | Medical equipment cost. |
| FutureMedical | nonnegativecurrencyamount | No | - | - | Future medical cost. |
| ClmtOutOfPocket | nonnegativecurrencyamount | No | - | - | Claimant out of pocket cost. |
| Other | nonnegativecurrencyamount | No | - | - | Other damages cost. |
| Low | nonnegativecurrencyamount | No | - | - | Low non-economic cost estimate. |
| High | nonnegativecurrencyamount | No | - | - | High non-economic cost estimate. |
| Likely | nonnegativecurrencyamount | No | - | - | Likely non-economic cost estimate. |
| Claim | ForeignKey | Yes | Claim | - | Related claim. |
| Exposure | ForeignKey | No | Exposure | - | Related exposure. |
| ClaimContact | ForeignKey | No | ClaimContact | - | Related claimant (either a person or a company). |
| Matter | ForeignKey | No | Matter | - | Related matter. |
| ServiceRequest | ForeignKey | No | ServiceRequest | - | Associated service request |

---

### Entity: Negotiation

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Negotiation.eti`
**Entity Type:** `retireable`
**Database Table:** `negotiation`
**Supertype:** None
**Description:** A negotiation for a claim or a part of a claim.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Name | varchar | No | - | - | The name or subject of this negotiation. |
| TargetOffer | nonnegativecurrencyamount | No | - | - | The target amount of negotiated settlement. |
| Rationale | longtext | No | - | - | The rationale for the proposed target offer. |
| MaxOffer | nonnegativecurrencyamount | No | - | - | The maximum offer the owner is willing to settle for before rethinking the strategy. |
| LiabilityEval | nonnegativecurrencyamount | No | - | - | An assessment of the total liability for this negotiation. |
| Claim | ForeignKey | Yes | Claim | - | Related claim. |
| Exposure | ForeignKey | No | Exposure | - | Related exposure. |
| ClaimContact | ForeignKey | No | ClaimContact | - | Related claimant (either a person or a company). |
| Matter | ForeignKey | No | Matter | - | Related matter. |
| ServiceRequest | ForeignKey | No | ServiceRequest | - | Associated service request |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| SettleNegotiation | NegotiationLine | A list of demands, offers, and couteroffers related to this negotiation. |
| Text | NegotiationText | The list of texts related to this negotiation; for example arguments, settlemnet plan, etc. |

---

### Entity: MetroReport

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\MetroReport.eti`
**Entity Type:** `retireable`
**Database Table:** `metroreport`
**Supertype:** None
**Description:** Details of metro reports associated with claim.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Name | varchar | No | - | - | Name of the metro report |
| LossDescription | varchar | No | - | - | Loss Description |
| MetroControlNumber | varchar | No | - | - | Metro Control number assigned by Metro Reporting |
| MetroTransactionID | varchar | No | - | - | Metro transaction ID - Unique number assigned to this order |
| MetroProcessID | varchar | No | - | - | Metro process ID - Identifying information for MetroReporting XML Support |
| DocumentURL | varchar | No | - | - | The URL link to the document provided by Metro |
| InformationURL | varchar | No | - | - | The URL link to the additional information needed from the customer |
| DelayMemoURL | varchar | No | - | - | The URL link to the delay memo when the status is deferred |
| ForceDuplicate | bit | No | - | - | Default: false Flag to indicate if a metro report should be requested regardless of a duplicate request. |
| CreateHoldActivity | bit | No | - | - | Flag to indicate if Hold Activity should be created or not. |
| CreateDeferredActivity | bit | No | - | - | Flag to indicate if Deferred Activity should be created or not. |
| DateOfDeath | datetime | No | - | - | Date of death for the deceased |
| SentDate | datetime | No | - | - | The date sent out the order file |
| ReceivedDate | datetime | No | - | - | The date received the report |
| ErrorMessage | varchar | No | - | - | Error message return from Metro if failed |
| AgentName | varchar | No | - | - | Name of Investigating Agency that issued the report |
| Precinct | varchar | No | - | - | Precinct, troop number or name/badge # of officer |
| ReportNumber | varchar | No | - | - | Report Number assigned by issuing Police-Fire Agency |
| OfficerName | varchar | No | - | - | The name of officer |
| DateReported | datetime | No | - | - | Date Reported |
| AgentCity | varchar | No | - | - | City of investigating agency |
| Claim | ForeignKey | Yes | Claim | - | The claim associated with this MetroReport. |
| Doc | ForeignKey | No | Document | - | The report document associated with this MetroReport, if it is stored in our database. Most users should use the Document property instead of this one, as this DocID will usually be null if the IDocumentMetadataSource plugin is in use |
| VehicleIncident | ForeignKey | No | VehicleIncident | - | The vehicle associated with this MetroReport, for auto report types. |
| DeceasedContact | ForeignKey | No | Contact | - | Contact for the deceased |
| ThirdPartyVehicle | ForeignKey | No | VehicleIncident | - | The third party vehicle associated with this MetroReport, for auto report types. |
| MetroReportType | TypeKey | No | - | MetroReportType | Type of metro reports (Auto Accident, Fire-Home etc) Codes (26 total): [A, B, C, D, E, ...] |
| LossType | TypeKey | No | - | LossType | The type of the Loss (Auto, Property, .. etc) Codes: [AUTO, PR, GL, WC, TRAV] |
| Status | TypeKey | No | - | MetroReportStatus | Default: new Status of the Official Report Codes (17 total): [new, insufficientdata, validated, sendingorder, orderfailed, ...] |
| MetroAgency | TypeKey | No | - | MetroAgencyType | Investigating Agency Type Codes (15 total): [PD, CO_PD, FD, CO_FD, CO_SO, ...] |
| AgentState | TypeKey | No | - | State | State of investigating Agency. Codes (142 total): [AK, AL, AR, AZ, CA, ...] |

---

### Entity: ClaimIndicator

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimIndicator.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\ClaimIndicator.etx`
**Entity Type:** `retireable`
**Database Table:** `claimindicator`
**Supertype:** None
**Description:** Claim 

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| IsOn | bit | No | - | - | Default: false Is this indicator on? |
| WhenOn | datetime | No | - | - | Time at which this indicator was set to on, or null if indicator off |
| Claim | ForeignKey | Yes | Claim | - | Claim to which this indicator is related. |

---

### Entity: CatastropheClaimsHistory

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\CatastropheClaimsHistory.eti`
**Entity Type:** `versionable`
**Database Table:** `catastropheclaimshistory`
**Supertype:** None
**Description:** The history of catastrophe finder batch process runs.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Description | mediumtext | No | - | - | Description of the history event. |
| EventTimestamp | datetime | No | - | - | Timestamp when the event occurred. |
| Catastrophe | ForeignKey | Yes | Catastrophe | - | The catastrophe. |

---

### Entity: CatastrophePeril

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\CatastrophePeril.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\CatastrophePeril.etx`
**Entity Type:** `joinarray`
**Database Table:** `catastropheperil`
**Supertype:** None
**Description:** Details of perils associated to a catastrophe.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Comments | shorttext | No | - | - | Comments regarding the peril |
| Catastrophe | ForeignKey | Yes | Catastrophe | - | Foreign key target: Catastrophe |
| LossCause | TypeKey | No | - | LossCause | The loss cause associated to the peril Codes (64 total): [animalcollision, animal, bikecollision, fixedobjcoll, vehcollision, ...] |
| LossType | TypeKey | No | - | LossType | High level claim type (for example, Auto or Property). Codes: [AUTO, PR, GL, WC, TRAV] |

---

### Entity: CatastropheZone

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\CatastropheZone.eti`
**Entity Type:** `versionable`
**Database Table:** `catastrophezone`
**Supertype:** None
**Description:** A zone of a catastrophe.  It contains the zone code, the zone type and the country to which the region belongs.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Code | shorttext | Yes | - | - | The code for this zone, this is the value that should be used for lookups. |
| Catastrophe | ForeignKey | Yes | Catastrophe | - | The catastrophe. |
| ZoneType | TypeKey | Yes | - | ZoneType | Type of zone. Codes (13 total): [country, unknown, city, citykanji, county, ...] |
| Country | TypeKey | Yes | - | Country | The country to which the zone belongs. Codes (243 total): [unknown, AF, AL, DZ, AS, ...] |

---

### Entity: CheckGroup

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\CheckGroup.eti`
**Entity Type:** `retireable`
**Database Table:** `checkgroup`
**Supertype:** None
**Description:** Groups the checks that are part of a multi-payee check.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| CheckSet | ForeignKey | Yes | CheckSet | - | The TransactionSet that this check group belongs to. |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Checks | Check | Check objects in the group, including the primary check. Together, these checks form a multi-payee check. |

---

### Entity: CheckRecurrence

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\CheckRecurrence.eti`
**Entity Type:** `retireable`
**Database Table:** `checkrecurrence`
**Supertype:** None
**Description:** Describes the recurrence schedule for a check.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| IssuanceDateOffset | integer | Yes | - | - | Default: 0 Number of days before a check is due that it should be issued. |
| FirstDueDate | datetime | Yes | - | - | Due date of the first check in the recurrence. |
| NumChecks | positiveinteger | Yes | - | - | Default: 1 Number of checks in the recurrence. |
| RecurrenceDay | TypeKey | No | - | RecurrenceDay | Day of the week the check is due. Codes (7 total): [mon, tue, weds, thurs, fri, ...] |
| CheckSet | OneToOne | No | CheckSet | - | The CheckSet for which this CheckRecurrence defines the recurrence schedule |

---

### Entity: CheckRpt

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\CheckRpt.eti`
**Entity Type:** `retireable`
**Database Table:** `checkrpt`
**Supertype:** None
**Description:** Calculated amounts for a check.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| GrossAmount | money | Yes | - | - | The gross amount of the check in the transaction currency. |
| GrossClaimAmount | money | Yes | - | - | The gross amount of the check in the claim currency. |
| GrossReservingAmount | money | Yes | - | - | The gross amount of the check in the reserving currency. |
| Check | ForeignKey | Yes | Check | - | The check that the calculations are on. |
| Currency | TypeKey | Yes | - | Currency | The transaction currency of the Check. Codes (7 total): [usd, eur, gbp, cad, aud, ...] |
| ReservingCurrency | TypeKey | Yes | - | Currency | The reserving currency of the Check. Codes (7 total): [usd, eur, gbp, cad, aud, ...] |

---

### Entity: CheckSearchView

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\CheckSearchView.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Aggregates the information needed to display one Check on the Payment/Check search page.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: CheckSetReserve

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\CheckSetReserve.eti`
**Entity Type:** `joinarray`
**Database Table:** `checksetreserve`
**Supertype:** None
**Description:** Links a check set with any reserves that were automatically created as part of processing its payments.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| CheckSet | ForeignKey | Yes | CheckSet | - | The check set. |
| Reserve | ForeignKey | Yes | Reserve | - | The automatically-generated reserve. |

---

### Entity: CheckView

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\CheckView.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Aggregates the information needed to display one Check on the Financials Checks page.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: ClaimAbstractView

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimAbstractView.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Abstract base view entity for efficiently displaying Claims in list views.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: ClaimAccessData

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimAccessData.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Anyone | bit | No | - | - | Default: false Whether this permission should be granted to everyone.  If true then GroupID, UserID, and SecurityZoneID should be null. |
| Group | ForeignKey | No | Group | - | The permitted group.  Exactly one of GroupID, UserID, and SecurityZoneID should be non-null. |
| User | ForeignKey | No | User | - | The permitted user.  Exactly one of GroupID, UserID, and SecurityZoneID should be non-null. |
| SecurityZone | ForeignKey | No | SecurityZone | - | The permitted security zone.  Exactly one of GroupID, UserID, and SecurityZoneID should be non-null. |
| Permission | TypeKey | Yes | - | claimaccesstype | The type of permission being granted. Codes: [edit, view] |

---

### Entity: ClaimAggregateLimitRpt

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimAggregateLimitRpt.eti`
**Entity Type:** `editable`
**Database Table:** `claimagglimitrpt`
**Supertype:** None
**Description:** The entity used to track the amount used per  claim against an aggregate limit.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| ReserveTotal | currencyamount | No | - | - | The total amount of reserve transactions from this claim that apply to the aggregate limit. |
| NonErodingPaymentTotal | currencyamount | No | - | - | The total amount of non-eroding payment transactions from this claim that apply to the aggregate limit. |
| ErodingPaymentTotal | currencyamount | No | - | - | The total amount of eroding payment transactions from this claim that apply to the aggregate limit. |
| RecoveryTotal | currencyamount | No | - | - | The total amount of recovery transactions from this claim that apply to the aggregate limit. |
| RecoveryReserveTotal | currencyamount | No | - | - | The total amount of recovery reserve transactions from this claim that apply to the aggregate limit. |
| FutureErodingPaymentTotal | currencyamount | No | - | - | The total amount of future eroding payment transactions from this claim that apply to the aggregate limit. |
| FutureNonErodingPaymentTotal | currencyamount | No | - | - | The total amount of future non-eroding payment transactions transactions from this claim that apply to the aggregate limit. |
| ClaimInfo | ForeignKey | Yes | ClaimInfo | - | ClaimInfo with which the aggregate limit is associated. |

---

### Entity: ClaimAssignmentView

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimAssignmentView.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: ClaimAssociation

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimAssociation.eti`
**Entity Type:** `retireable`
**Database Table:** `claimassoc`
**Supertype:** None
**Description:** Represents a grouping of a set of claims.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Title | shorttext | No | - | - | A brief title for the association. |
| Description | mediumtext | No | - | - | Description of the association. |
| ClaimAssocType | TypeKey | No | - | ClaimAssocType | Type of the association among the claims. Codes: [general, parentchild, eventrelated, priorclaims, reinsurancerelated] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| ClaimsInAssoc | ClaimInAssociation | The claims belonging to this association. |

---

### Entity: ClaimAssociationSearchCriteria

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimAssociationSearchCriteria.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\ClaimAssociationSearchCriteria.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Non-persistent set of criteria to use in searching for a specific claim association.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Title | shorttext | No | - | - | Desired ClaimAssociation title. |
| ClaimNumber | claimnumber | No | - | - | Number of a Claim included in the ClaimAssociation. |
| LossDate | datetime | No | - | - | Loss date of a Claim included in the ClaimAssociation. |
| LastName | lastname | No | - | - | Last name of an insured of a Claim included in the ClaimAssociation. |
| FirstName | firstname | No | - | - | First name of an insured of a Claim included in the ClaimAssociation. |
| CompanyName | companyname | No | - | - | Company name of an insured of a Claim included in the ClaimAssociation. |
| NameKanji_Ext | companyname | No | - | - | [Extension] This contact's name in kanji.  Used only for Japanese names and will be null otherwise. |
| FirstNameKanji_Ext | firstname | No | - | - | [Extension] First name in kanji.  Used only for Japanese names and will be null otherwise. |
| LastNameKanji_Ext | lastname | No | - | - | [Extension] Last name in kanji.  Used only for Japanese names and will be null otherwise. |

---

### Entity: ClaimCloseReopenInfo

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimCloseReopenInfo.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** CloseReopenInfo
**Description:** Temporary entity that holds transitional internal state information during all claim close or reopen operations.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Claim | ForeignKey | No | Claim | - | Claim that the action was applied. |

---

### Entity: ClaimContactRoleOwner

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimContactRoleOwner.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: ClaimDesktopView

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimDesktopView.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** View entity for efficiently displaying Claims on the Desktop page.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: ClaimException

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimException.eti`
**Entity Type:** `versionable`
**Database Table:** `claimexception`
**Supertype:** None
**Description:** Records the action of the claim exception monitor. This table will have at most one row for each claim in the system, indicating the last time it had claim exception rules run on it.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| ExCheckTime | datetime | Yes | - | - | The last time at which claim exception rules were run on the claim. |
| Claim | ForeignKey | Yes | Claim | - | A foreign key to the claim. |

---

### Entity: ClaimInAssociation

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimInAssociation.eti`
**Entity Type:** `joinarray`
**Database Table:** `claiminassoc`
**Supertype:** None
**Description:** Links a Claim with a ClaimAssociation.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| PrimaryClaim | bit | Yes | - | - | Default: false True if the given Claim is the primary Claim of the ClaimAssociation. |
| ClaimInfo | ForeignKey | Yes | ClaimInfo | - | ClaimInfo that belongs to the ClaimAssociation. |
| ClaimAssociation | ForeignKey | Yes | ClaimAssociation | - | ClaimAssociation which contains the Claim. |

---

### Entity: ClaimIndicatorAutomatedActivityHandler

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimIndicatorAutomatedActivityHandler.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** AutomatedActivityHandler
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| ClaimIndicatorTrigger | OneToOne | No | ClaimIndicatorTrigger | - | The associated ClaimIndicatorTrigger whose execution would result in an activity being generated according to the specifications of this handler |

---

### Entity: ClaimIndicatorAutomatedNotificationHandler

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimIndicatorAutomatedNotificationHandler.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** AutomatedNotificationHandler
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| ClaimIndicatorTrigger | OneToOne | No | ClaimIndicatorTrigger | - | The associated ClaimIndicatorTrigger whose execution would result in an email being generated according to the specifications of this handler |

---

### Entity: ClaimIndicatorCriterion

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimIndicatorCriterion.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| ClaimSearchCriteria | ForeignKey | Yes | ClaimSearchCriteria | - | Claim Search Criteria ID for this Claim Indicator Criterion. |
| ClaimIndicatorType | TypeKey | Yes | - | ClaimIndicator | Type of claim indicator this search will use to check if turned on. Codes (7 total): [LitigationClaimIndicator, FatalityClaimIndicator, LargeLossClaimIndicator, CoverageInQuestionClaimIndicator, SIUClaimIndicator, ...] |

---

### Entity: ClaimIndicatorTrigger

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimIndicatorTrigger.eti`
**Entity Type:** `retireable`
**Database Table:** `claimindicatortrigger`
**Supertype:** None
**Description:** An automated handler trigger whose execution is dependent on the change of a specific Claim Indicator on a Claim

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| TriggeringValue | bit | Yes | - | - | The value on which to execute this trigger.  If the specified ClaimIndicator changes to this value for a given Claim then this trigger should execute |
| AutomatedHandler | ForeignKey | Yes | AutomatedHandler | - | Foreign key target: AutomatedHandler |
| ClaimIndicator | TypeKey | Yes | - | ClaimIndicator | The Claim Indicator that can cause this trigger to execute Codes (7 total): [LitigationClaimIndicator, FatalityClaimIndicator, LargeLossClaimIndicator, CoverageInQuestionClaimIndicator, SIUClaimIndicator, ...] |

---

### Entity: ClaimInfoAccess

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimInfoAccess.eti`
**Entity Type:** `versionable`
**Database Table:** `claiminfoaccess`
**Supertype:** None
**Description:** Records information about users and groups that are allowed to access an archived claim.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| ClaimInfo | ForeignKey | Yes | ClaimInfo | - | A foreign key to the claim info. |

---

### Entity: ClaimInfoCriteria

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimInfoCriteria.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Non-persistent set of criteria to use in searching for a specific claim Info.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| ClaimNumber | claimnumber | No | - | - | Match by claim number. |
| PolicyNumber | policynumber | No | - | - | Match by policy number. |
| NameCriteria | ForeignKey | Yes | CCNameCriteria | - | Set of criteria to match by name. |
| AddressCriteria | ForeignKey | Yes | Address | - | Set of criteria to match by address. |
| ClaimSearchType | TypeKey | No | - | ClaimSearchType | The type of claim search to perform. Codes: [active, archived, all] |
| NameSearchType | TypeKey | No | - | ClaimSearchNameSearchType | Type of name search for claim search. Codes: [insured, claimant, addinsured, any] |
| FreeTextClaimSearchType | TypeKey | No | - | FreeTextClaimSearchType | The type of claim search to perform. Codes: [byContactInfoActive, byContactInfoArchive] |
| FreeTextNameSearchType | TypeKey | No | - | FreTxtClmSrchNameSrchTyp | Type of name search for claim search. Codes: [insured, claimant, addinsured, any] |

---

### Entity: ClaimInfoSearchView

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimInfoSearchView.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** View entity for efficiently displaying ClaimInfo on the Simple Claim search page.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: ClaimISOMatchReport

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimISOMatchReport.eti`
**Entity Type:** `retireable`
**Database Table:** `claimisomatchreport`
**Supertype:** None
**Description:** Details of a match for a Claim returned by the ISO ClaimSearch service.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Claim | ForeignKey | Yes | Claim | - | The related claim. |

---

### Entity: ClaimMetric

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimMetric.eti`
**Entity Type:** `editable`
**Database Table:** `claimmetric`
**Supertype:** None
**Description:** Metrics related to a claim

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Claim | ForeignKey | Yes | Claim | - | Claim to which this metric is related. |
| MetricLimitDenorm | ForeignKey | No | ClaimMetricLimit | - | The metric limit for the metric, denormalized from the claim's inital claim metric limits array. |
| ClaimMetricCategory | TypeKey | Yes | - | ClaimMetricCategory | Category of Claim Metric. Codes: [OverallClaimMetrics, ClaimActivityMetrics, ClaimFinancialsMetrics] |

---

### Entity: ClaimMetricLimit

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimMetricLimit.eti`
**Entity Type:** `retireable`
**Database Table:** `claimmetriclimit`
**Supertype:** None
**Description:** Limits for metrics related to a claim

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| AscendingLimitOrder | bit | Yes | - | - | Default: true Boolean field to indicate the direction of comparison for value validation |
| PolicyTypeMetricLimits | ForeignKey | Yes | PolicyTypeMetricLimits | - | Back pointer to policy type metric limits object that owns this limit. |
| ClaimMetricType | TypeKey | Yes | - | ClaimMetric | Type of claim metric to which this limit applies. Codes (15 total): [DaysOpenClaimMetric, DaysInitialContactWithInsuredClaimMetric, DaysLastViewedByAdjusterClaimMetric, DaysLastViewedBySupervisorClaimMetric, OverdueActivitiesClaimMetric, ...] |
| ClaimTier | TypeKey | No | - | ClaimTier | Claim tier to which this limit applies, or null if this is a default limit Codes (7 total): [incidentreport, medicalonly, indemnity, el, low, ...] |
| Currency | TypeKey | Yes | - | Currency | Currency for this limit, for non money based limits this is always the default currency. Codes (7 total): [usd, eur, gbp, cad, aud, ...] |
| ClaimMetricCategory | TypeKey | Yes | - | ClaimMetricCategory | Category of this claim metric limit, corresponds to category of metric. Codes: [OverallClaimMetrics, ClaimActivityMetrics, ClaimFinancialsMetrics] |
| MetricUnit | TypeKey | Yes | - | MetricUnit | Units for this type of metric. Codes: [numeric, percent, currency, hours, days] |

---

### Entity: ClaimMetricRecalculationTime

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimMetricRecalculationTime.eti`
**Entity Type:** `editable`
**Database Table:** `claimmetricrecalctime`
**Supertype:** None
**Description:** Tracks when a claim's metrics should be recalculated

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| NextRecalculationTime | datetime | No | - | - | The time when the claim metrics should next be recalculated. |
| MetricLimitGeneration | integer | Yes | - | - | Generation number, used to identify the limits for this claim's metrics |
| Claim | ForeignKey | Yes | Claim | - | Claim that owns this ClaimMetricRecalculationTime object. |

---

### Entity: ClaimRecentView

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimRecentView.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\ClaimRecentView.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** View entity for efficiently displaying Claims in the Recently Viewed Claims tab.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: ClaimRpt

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimRpt.eti`
**Entity Type:** `retireable`
**Database Table:** `claimrpt`
**Supertype:** None
**Description:** Calculated financial values for claims.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| OpenReserves | currencyamount | Yes | - | - | Default: 0 The open reserves. |
| OpenReservesReporting | currencyamount | Yes | - | - | Default: 0 The open reserves on a claim, in Reporting/Default Currency. |
| RemainingReserves | currencyamount | Yes | - | - | Default: 0 The remaining reserves on a claim. |
| RemainingReservesReporting | currencyamount | Yes | - | - | Default: 0 The remaining reserves on a claim, in Reporting/Default Currency. |
| AvailableReserves | currencyamount | Yes | - | - | Default: 0 The available reserves on a claim. |
| AvailableReservesReporting | currencyamount | Yes | - | - | Default: 0 The available reserves on a claim, in Reporting/Default Currency. |
| TotalPayments | currencyamount | Yes | - | - | Default: 0 The total payments. |
| TotalPaymentsReporting | currencyamount | Yes | - | - | Default: 0 The total payments on a claim, in Reporting/Default Currency. |
| FuturePayments | currencyamount | Yes | - | - | Default: 0 The future payments total. |
| FuturePaymentsReporting | currencyamount | Yes | - | - | Default: 0 The future payments total on a claim, in Reporting/Default Currency. |
| TotalRecoveries | currencyamount | Yes | - | - | Default: 0 The total recoveries on a claim. |
| TotalRecoveriesReporting | currencyamount | Yes | - | - | Default: 0 The total recoveries on a claim, in Reporting/Default Currency. |
| OpenRecoveryReserves | currencyamount | Yes | - | - | Default: 0 The open recovery reserves on the claim. |
| OpenRecoveryReservesReporting | currencyamount | Yes | - | - | Default: 0 The open recovery reserves on a claim, in Reporting/Default Currency. |
| Claim | ForeignKey | Yes | Claim | - | The claim that the calculations are on. |

---

### Entity: ClaimSearchCriteria

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimSearchCriteria.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\ClaimSearchCriteria.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** ClaimInfoCriteria
**Description:** Non-persistent set of criteria to use in searching for a specific claim.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| vinNumber | vin | No | - | - | Match by car VIN number. |
| licensePlate | text | No | - | - | Match by car license plate. |
| pendingAssignment | bit | No | - | - | Match claims that are pending assignment. |
| ReinsuranceReportable | bit | No | - | - | Match claims that are resinsurance reportable. |
| IncidentReport | bit | No | - | - | Match by incident report. |
| CoverageInQuestion | bit | No | - | - | Match by coverage in question status. |
| AssignedToGroup | ForeignKey | No | GroupSearchCriterion | - | Match by claim group assignment. |
| AssignedToUser | ForeignKey | No | User | - | Match by claim user assignment. |
| CreatedByUser | ForeignKey | No | User | - | Match by claim creator. |
| Catastrophe | ForeignKey | No | Catastrophe | - | Match by catastrophe. |
| DateCriterionChoice | ForeignKey | Yes | DateCriterionChoice | - | Match claim by specific date criteria. |
| ArchiveDateCriterionChoice | ForeignKey | Yes | DateCriterionChoice | - | Match claim by specific date criteria for archived claim. |
| FinancialCriterion | ForeignKey | Yes | FinancialCriterionMC | - | Match claim by specific financials criteria. |
| JurisdictionState | TypeKey | No | - | Jurisdiction | Match by jurisdiction. The Jurisdiction must be associated with JurisdictionType.TC_INSURANCE. Codes (97 total): [AK, AL, AR, AZ, CA, ...] |
| LOBCode | TypeKey | No | - | LOBCode | Match by line of business. Codes (11 total): [GLLine, CPLine, PersonalAutoLine, IMLine, WorkersCompLine, ...] |
| ClaimState | TypeKey | No | - | ClaimState | Match by state of claim. Codes: [draft, open, closed, archived] |
| LossType | TypeKey | No | - | LossType | Match by loss type. Codes: [AUTO, PR, GL, WC, TRAV] |
| LitigationStatus | TypeKey | No | - | LitigationStatus | Match by litigation status. Codes (13 total): [not_litigated, litigated, complete, rep, suit_filed, ...] |
| FlaggedType | TypeKey | No | - | FlaggedType | Match by flagged status. Codes: [isflagged, wasflagged, neverflagged] |
| Fault_Ext | percentagedec | No | - | - | [Extension] Insured's probable percentage of fault. |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| ClaimIndicatorCriterion | ClaimIndicatorCriterion | Match claim by specific claim indicator criteria |

---

### Entity: ClaimSearchView

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimSearchView.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** View entity for efficiently displaying Claims on the Claim search page.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: ClaimSnapshot

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimSnapshot.eti`
**Entity Type:** `retireable`
**Database Table:** `claimsnapshot`
**Supertype:** None
**Description:** Stores XML snapshots of claim data.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| ClaimData | text | No | - | - | The ClaimData object, stored as XML. |
| SnapshotDate | datetime | No | - | - | Date on which this snapshot was created. |
| EncryptionVersion | integer | Yes | - | - | Default: 0 The version of encryption |
| Compressed | bit | No | - | - | Default: false Indicates whether or not the claim data is compressed. |
| Claim | ForeignKey | Yes | Claim | - | Main Claim object whose snapshot is being stored. |

---

### Entity: ClaimSynchState

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimSynchState.eti`
**Entity Type:** `versionable`
**Database Table:** `claimsynchst`
**Supertype:** None
**Description:** Represents the current state of synchronization between a Claim and a MessageSink.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| MessageSink | integer | Yes | - | - | Identifies the message sink to which the synchronization state applies. |
| Claim | ForeignKey | Yes | Claim | - | The Claim to which the synchronization state applies. |
| SynchState | TypeKey | No | - | SynchState | The synchronization state of the given Claim with respect to the given message sink. Codes: [unsynched, synch_sent] |

---

### Entity: ClaimTeamView

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimTeamView.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** View entity for efficiently displaying Claims on the Team page.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: ClaimText

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimText.eti`
**Entity Type:** `versionable`
**Database Table:** `claimtext`
**Supertype:** None
**Description:** Text fields related to claims

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Text | mediumtext | No | - | - | Text field contents |
| Claim | ForeignKey | Yes | Claim | - | Related claim. |
| TextType | TypeKey | No | - | ClaimTextType | Meaning of the text field. Codes (12 total): [BenefitsDecisionReason, MedicalDiagnosis, SubjComplaints, ObjFindings, TreatmentRend, ...] |

---

### Entity: ClaimUserModel

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimUserModel.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Defines a User/Group pair that is assigned to something on a Claim

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| ClaimUserModelSet | ForeignKey | No | ClaimUserModelSet | - | Foreign key target: ClaimUserModelSet |
| User | ForeignKey | No | User | - | The user. |
| Group | ForeignKey | No | Group | - | The group. |

---

### Entity: ClaimUserModelSet

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimUserModelSet.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Defines a set of ClaimUserModels

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Claim | ForeignKey | No | Claim | - | Foreign key target: Claim |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| ClaimUserModels | ClaimUserModel | Child collection |

---

### Entity: ClaimVacationView

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimVacationView.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** View entity for efficiently displaying Claims on the Desktop page.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: ClaimValidationWorkItem

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimValidationWorkItem.eti`
**Entity Type:** `keyable`
**Database Table:** `validationworkitem`
**Supertype:** None
**Description:** Workitems for claims to be bulk-validated using distributed work queue.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Claim | ForeignKey | Yes | Claim | - | The claim to be validated. |

---

### Entity: ClaimWorkComp

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimWorkComp.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\ClaimWorkComp.etx`
**Entity Type:** `retireable`
**Database Table:** `workcomp`
**Supertype:** None
**Description:** Worker's compensation information related to a claim

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| TimeLossReport | bit | No | - | - | True if this is claim has a report that the injured worker will lose time from work. |
| MedicalReport | bit | No | - | - | True if this is claim has a report that the injured worker requires Medical treatment. |
| DeathReport | bit | No | - | - | True if this claim has a report of death of the injured worker. |
| EmployerLiability | bit | No | - | - | True if this claim has a possible Employer's Liability aspect. |
| EquipmentUsed | mediumtext | No | - | - | Field to describe the equipment, materials or chemicals the employee was using when event or exposure occurred. |
| ActivityPerformed | mediumtext | No | - | - | Field to describe the specific activity the injured worker was performing. |
| IllnessRelatedToExposure | bit | No | - | - | Is claim being made for illness related to chemical or material exposure? |
| ClassCodeByLocation | bit | No | - | - | Default: true Is Class Code filtered by Location |
| WaitingPeriodApplied | bit | No | - | - | Should the Waiting Period be applied? |
| Compensable | TypeKey | No | - | CompensabilityDecision | Indicates status of the compensability decision Codes: [accepted, partialdenial, denied, pending, disputed] |
| Claim | OneToOne | No | Claim | - | One-to-one link |
| JurisdictionClaimNumber_Ext | varchar | No | - | - | [Extension] Jurisdiction Claim Number will be filled once received by the Jurisdiction. |
| DateOfEmployeeRepresentation_Ext | dateonly | No | - | - | [Extension] Date Claim Administrator Notified of Employee Representation |
| InsuredReportNumber_Ext | varchar | No | - | - | [Extension] A number assigned by the insured to identify a specific claim. If this data is included on any FROI/SROI transaction, it should be returned on the transaction’s acknowledgment regardless of whether it is a data element collected by the jurisdiction. |
| DiscontinuedFringeBenefits_Ext | currencyamount | No | - | - | [Extension] The amount of non-salary remuneration which the employer has discontinued as applicable to the calculation of benefits per the jurisdiction. |
| MedRecReleaseAuth_Ext | bit | No | - | - | [Extension] An indicator that the employee's written authorization to release medical records related to the injury is on file. |
| FullDenialEffectiveDate_Ext | datetime | No | - | - | [Extension] The date the compensability Decision (for entire claim) was set to Denied. |
| InitialTreatment_Ext | TypeKey | No | - | InitialTreatment | [Extension] Initial Treatment |
| AccidentPremises_Ext | TypeKey | No | - | AccidentPremises | [Extension] A code to indicate the premises where the accident occurred. |
| PartialDenialReason_Ext | TypeKey | No | - | PartialDenialReason | [Extension] Indicates reason for partial denial |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| WaitingPeriodDetails | WCWaitingPeriod | Used to track the specific days indicated as the Waiting Period on a WC Claim |
| FullDenialReasons_Ext | FullDenialReason | [Extension] Compensability full denial reasons when the claim compensibility was set to denied. |

---

### Entity: ClaimWorkflow

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimWorkflow.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** Workflow
**Description:** Base workflow subtype for all workflows that are linked to a claim

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Claim | ForeignKey | Yes | Claim | - | The Claim with which this workflow is associated. |

---

### Entity: ExposureAbstractView

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ExposureAbstractView.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Abstract base view entity for efficiently displaying Exposures in list views.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: ExposureAssignmentView

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ExposureAssignmentView.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Exposure view entity with assignment detail attributes.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: ExposureClaimantView

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ExposureClaimantView.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** View for efficiently getting the claimants associated with an exposure.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: ExposureDesktopView

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ExposureDesktopView.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Desktop Exposure view entity.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: ExposureISOMatchReport

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ExposureISOMatchReport.eti`
**Entity Type:** `retireable`
**Database Table:** `exposureisomatchreport`
**Supertype:** None
**Description:** Details of a match for an Exposure returned by the ISO ClaimSearch service.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| Exposure | ForeignKey | Yes | Exposure | - | The related exposure. |

---

### Entity: ExposureMetric

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ExposureMetric.eti`
**Entity Type:** `editable`
**Database Table:** `exposuremetric`
**Supertype:** None
**Description:** Metrics related to a exposure

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Exposure | ForeignKey | Yes | Exposure | - | Exposure to which this metric is related. |
| MetricLimitDenorm | ForeignKey | No | ExposureMetricLimit | - | The metric limit for the exposure metric, denormalized from the claim's inital exposure metric limits array. |

---

### Entity: ExposureMetricLimit

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ExposureMetricLimit.eti`
**Entity Type:** `retireable`
**Database Table:** `expmetriclimit`
**Supertype:** None
**Description:** Limits for metrics related to an exposure

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| AscendingLimitOrder | bit | Yes | - | - | Default: true Boolean field to indicate the direction of comparison for value validation |
| PolicyTypeMetricLimits | ForeignKey | Yes | PolicyTypeMetricLimits | - | Back pointer to policy type metric limits object that owns this limit. |
| ExposureMetricType | TypeKey | Yes | - | ExposureMetric | Type of exposure metric to which this limit applies. Codes (7 total): [DaysOpenExposureMetric, DaysInitialContactWithClaimantExposureMetric, NetTotalIncurredExposureMetric, TotalPaidExposureMetric, PercentEscalatedActivitiesExposureMetric, ...] |
| ExposureTier | TypeKey | No | - | ExposureTier | Exposure tier to which this limit applies, or null if this is a default limit Codes (21 total): [medical, indemnity, el, 1p_pd_low, 1p_pd_high, ...] |
| Currency | TypeKey | Yes | - | Currency | Currency for this limit, for non money based limits this is always the default currency. Codes (7 total): [usd, eur, gbp, cad, aud, ...] |
| MetricUnit | TypeKey | Yes | - | MetricUnit | Units for this type of metric. Codes: [numeric, percent, currency, hours, days] |

---

### Entity: ExposureRpt

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ExposureRpt.eti`
**Entity Type:** `retireable`
**Database Table:** `exposurerpt`
**Supertype:** None
**Description:** Denormalized financial calculations for exposures.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| OpenReserves | currencyamount | Yes | - | - | Default: 0 The open reserves. |
| OpenReservesReporting | currencyamount | Yes | - | - | Default: 0 The open reserves on an exposure, in Reporting/Default Currency. |
| AvailableReserves | currencyamount | Yes | - | - | Default: 0 The available reserves on an exposure. |
| AvailableReservesReporting | currencyamount | Yes | - | - | Default: 0 The available reserves on an exposure, in Reporting/Default Currency. |
| RemainingReserves | currencyamount | Yes | - | - | Default: 0 The remaining reserves on an exposure. |
| RemainingReservesReporting | currencyamount | Yes | - | - | Default: 0 The remaining reserves on an exposure, in Reporting/Default Currency. |
| TotalPayments | currencyamount | Yes | - | - | Default: 0 The total payments. |
| TotalPaymentsReporting | currencyamount | Yes | - | - | Default: 0 The total payments on an exposure, in Reporting/Default Currency. |
| FuturePayments | currencyamount | Yes | - | - | Default: 0 The total of awaiting submission payments scheduled to be sent after today. |
| FuturePaymentsReporting | currencyamount | Yes | - | - | Default: 0 The total of awaiting submission payments scheduled to be sent after today, in Reporting/Default Currency. |
| TotalRecoveries | currencyamount | Yes | - | - | Default: 0 The total recoveries on an exposure. |
| TotalRecoveriesReporting | currencyamount | Yes | - | - | Default: 0 The total recoveries on a claim, in Reporting/Default Currency. |
| OpenRecoveryReserves | currencyamount | Yes | - | - | Default: 0 The open recovery reserves on an exposure. |
| OpenRecoveryReservesReporting | currencyamount | Yes | - | - | Default: 0 The open recovery reserves on a claim, in Reporting/Default Currency. |
| Exposure | ForeignKey | Yes | Exposure | - | The exposure that the calculations are on. |
| Claim | ForeignKey | Yes | Claim | - | The exposure's claim. |

---

### Entity: ExposureRule

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ExposureRule.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** CCRule
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| LossCauses | AppCritLossCause | Child collection |
| CoverageTypes | AppCritCoverageType | Child collection |
| IncidentTypes | AppCritIncidentType | Child collection |
| LossPartyTypes | AppCritLossPartyType | Child collection |

---

### Entity: ExposureSynchState

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ExposureSynchState.eti`
**Entity Type:** `versionable`
**Database Table:** `exposuresynchst`
**Supertype:** None
**Description:** Represents the current state of synchronization between an Exposure and a MessageSink.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| MessageSink | integer | Yes | - | - | Identifies the message sink to which the synchronization state applies. |
| Exposure | ForeignKey | Yes | Exposure | - | The Exposure to which the synchronization state applies. |
| SynchState | TypeKey | No | - | SynchState | The synchronization state of the given Exposure with respect to the given message sink. Codes: [unsynched, synch_sent] |

---

### Entity: ExposureTeamView

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ExposureTeamView.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Team Exposure view entity.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: ExposureText

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ExposureText.eti`
**Entity Type:** `versionable`
**Database Table:** `exposuretext`
**Supertype:** None
**Description:** A text field related to an exposure.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Text | mediumtext | No | - | - | The text associated with the exposure. |
| Exposure | ForeignKey | Yes | Exposure | - | Related exposure. |
| TextType | TypeKey | No | - | ExposureTextType | Meaning of the text field. Codes: [TreatmentRendered, SubjectiveComplaints, ObjectiveFindings, ISOErrorMessage] |

---

### Entity: ExposureVacationView

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ExposureVacationView.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Vacation Exposure view entity.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: MatterCloseReopenInfo

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\MatterCloseReopenInfo.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** CloseReopenInfo
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Matter | ForeignKey | No | Matter | - | Related matter. |

---

### Entity: MatterTeamView

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\MatterTeamView.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Displays matters efficiently in the team pages.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: MatterUserView

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\MatterUserView.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Displays matters efficiently in the admin user pages.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: MatterView

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\MatterView.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: PaymentReserve

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\PaymentReserve.eti`
**Entity Type:** `versionable`
**Database Table:** `paymentreserve`
**Supertype:** None
**Description:** Links a Payment to an offset Reserve.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Payment | ForeignKey | Yes | Payment | - | The payment. |
| Reserve | ForeignKey | Yes | Reserve | - | The reserve. |

---

### Entity: PaymentSearchCriteria

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\PaymentSearchCriteria.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Non-persistent set of criteria to use in searching for a specific Payment.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| ClaimNumber | claimnumber | No | - | - | Claim number to search for. |
| CheckNumber | shorttext | No | - | - | - |
| InvoiceNumber | shorttext | No | - | - | - |
| PayTo | shorttext | No | - | - | - |
| ApprovedByGroup | ForeignKey | No | GroupSearchCriterion | - | Foreign key target: GroupSearchCriterion |
| ApprovedByUser | ForeignKey | No | User | - | Foreign key target: User |
| CreatedByUser | ForeignKey | No | User | - | Foreign key target: User |
| NameCriteria | ForeignKey | Yes | CCNameCriteria | - | Foreign key target: CCNameCriteria |
| DateCriterionChoice | ForeignKey | Yes | DateCriterionChoice | - | Foreign key target: DateCriterionChoice |
| FinancialCriterion | ForeignKey | Yes | FinancialCriterionMC | - | Foreign key target: FinancialCriterionMC |
| CheckStatus | TypeKey | No | - | TransactionStatus | Codes (20 total): [draft, pendingapproval, awaitingsubmission, submitting, requesting, ...] |

---

### Entity: PaymentView

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\PaymentView.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Aggregates the information needed to display a Payment using the Payment filter of the Financials Transactions page. Subtype of TransactionView.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: PolicyLocationSummary

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\PolicyLocationSummary.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\PolicyLocationSummary.etx`
**Entity Type:** `editable`
**Database Table:** `policylocationsummary`
**Supertype:** None
**Description:** PolicyLocationSummary

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| PolicySystemId | policysystemid | Yes | - | - | Identifier for the policy location in an external policy system |
| PolicyNumber | policynumber | Yes | - | - | Number of the policy (generally a string). |
| Latitude | decimal | No | - | - | Latitude expressed in degrees.  Positive = North; Negative = South: -90 <= x <= 90 |
| Longitude | decimal | No | - | - | Longitude expressed in degrees relative to the prime meridian.  Positive = East; Negative = West: -180 <= x < 180 |
| InsuredName | companyname | No | - | - | Name of the primary insured. |
| InsuredAddressLine1 | addressline | No | - | - | First line of primary insured address. |
| InsuredAddressLine2 | addressline | No | - | - | Second line of primary insured address. |
| InsuredAddressLine3 | addressline | No | - | - | Third line of primary insured address. |
| InsuredCity | varchar | No | - | - | City of the primary insured. |
| InsuredCounty | varchar | No | - | - | County of the primary insured. |
| InsuredPostalCode | postalcode | No | - | - | Postal code of the primary insured; string to handle Zip+4 and international codes. |
| Phone | phone | No | - | - | Phone number of the primary insured. |
| PhoneExtension | varchar | No | - | - | The phone extension of the primary insured |
| EmailAddress | varchar | No | - | - | Email address of the primary insured. |
| TotalInsured | currencyamount | No | - | - | Default: 0 The total insured value for the policy location, in Reporting/Default Currency. |
| Catastrophe | ForeignKey | No | Catastrophe | - | Associated catastrophe. |
| PolicyType | TypeKey | Yes | - | PolicyType | Type of policy. Codes (14 total): [PersonalAuto, BusinessAuto, CommercialPackage, GeneralLiability, HOPHomeowners, ...] |
| GeocodeStatus | TypeKey | No | - | GeocodeStatus | Default: None Enum giving the status of the latitude and longitude data. Codes: [none, failure, city, postalcode, street, exact] |
| InsuredState | TypeKey | No | - | State | State of the primary insured. Codes (142 total): [AK, AL, AR, AZ, CA, ...] |
| InsuredCountry | TypeKey | No | - | Country | Country of the primary insured. Codes (243 total): [unknown, AF, AL, DZ, AS, ...] |
| PhoneCountry | TypeKey | No | - | PhoneCountryCode | The phone country of the primary insured Codes (245 total): [AC, AD, AE, AF, AG, ...] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| ClaimJoin | PolicyLocationSummaryJoin | Link to get to associated claims. |

---

### Entity: PolicyLocationSummaryJoin

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\PolicyLocationSummaryJoin.eti`
**Entity Type:** `editable`
**Database Table:** `policylocationsummaryjoin`
**Supertype:** None
**Description:** PolicyLocationSummaryJoin

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| PolicyLocationSummary | ForeignKey | Yes | PolicyLocationSummary | - | Associated PolicyLocationSummary |
| Claim | ForeignKey | Yes | Claim | - | Associated claim. |

---

### Entity: PolicyPeriod

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\PolicyPeriod.eti`
**Entity Type:** `retireable`
**Database Table:** `policyperiod`
**Supertype:** None
**Description:** Represents the period during which an insurance policy provides coverage.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| PolicyNumber | policynumber | No | - | - | Number of the policy (generally a string). |
| EffectiveDate | datetime | No | - | - | Date on which the policy is effective. |
| ExpirationDate | datetime | No | - | - | Date on which the policy expires. |
| PolicySuffix | shorttext | No | - | - | Indicates each unique period that a policy has been in effect.  (Sometimes called 'Mod' or 'Module.') |
| AccountNumber | account | No | - | - | Account number that the policies of this PolicyPeriod belong to. |
| PolicyType | TypeKey | Yes | - | PolicyType | Type of policy to which this period applies. Codes (14 total): [PersonalAuto, BusinessAuto, CommercialPackage, GeneralLiability, HOPHomeowners, ...] |
| PolicyPeriodType | TypeKey | Yes | - | PolicyPeriodType | Default: policy Type of policy period: account or policy. Codes: [account, policy] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| AggregateLimits | AggregateLimit | Aggregate limits for the policies in this period. |
| AggregateLimitRpts | AggregateLimitRpt | Denormalized data for this period. |
| ClaimAggregateLimitRpts | ClaimAggregateLimitRpt | Denormalized data for this period per claim. |
| CoverageLines | CoverageLine | Coverage lines associated with this period. |
| Policies | PeriodPolicy | Policies that belong to this period. |

---

### Entity: PolicyRetrievalResultSet

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\PolicyRetrievalResultSet.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Results of a policy retrieval.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| NotUnique | bit | Yes | - | - | True if the retrieval parameters map to multiple policies; false otherwise. |
| Result | ForeignKey | No | Policy | - | Detailed information about the policy. This is valid only if exactly one policy is retrieved. If zero or multiple policies match the retrieval parameters, then this is null. |

---

### Entity: PolicySearchCriteria

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\PolicySearchCriteria.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\PolicySearchCriteria.etx`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Search criteria for Policy searches.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| PolicyNumber | policynumber | No | - | - | - |
| LossDate | datetime | No | - | - | - |
| TaxIdString | ssn | No | - | - | - |
| Vin | vin | No | - | - | - |
| LastName | lastname | No | - | - | - |
| FirstName | firstname | No | - | - | - |
| CompanyName | companyname | No | - | - | - |
| IncludeArchived | bit | No | - | - | Default: false Include archived olicies in results |
| InsuredAddress | ForeignKey | No | Address | - | The address of the insured.  Supercedes the separate fields of City, State, and PostalCode. |
| PropertyAddress | ForeignKey | No | Address | - | The address of the property.  Generalizes and supercedes the existing PropertyCity field. |
| LossType | TypeKey | Yes | - | LossType | Type of loss. Codes: [AUTO, PR, GL, WC, TRAV] |
| PolicyType | TypeKey | No | - | PolicyType | Type of policy. Codes (14 total): [PersonalAuto, BusinessAuto, CommercialPackage, GeneralLiability, HOPHomeowners, ...] |
| ContactType | TypeKey | No | - | SearchContactType | Type of contact to search for Codes: [person, company] |
| NameKanji_Ext | companyname | No | - | - | [Extension] This contact's name in kanji (used only for Japanese names and will be null otherwise) |
| FirstNameKanji_Ext | firstname | No | - | - | [Extension] First name in kanji (used only for Japanese names and will be null otherwise) |
| LastNameKanji_Ext | lastname | No | - | - | [Extension] Last name in kanji (used only for Japanese names and will be null otherwise) |

---

### Entity: PolicySearchResultSet

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\PolicySearchResultSet.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** SearchResult
**Description:** Result object returned by the policy admin adapter's searchPolicies() method.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: PolicyStatCodeFilterCriteria

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\PolicyStatCodeFilterCriteria.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Non-persistent entity used for filtering of stat codes.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Policy | ForeignKey | Yes | Policy | - | Policy on which to search for stat codes. |

---

### Entity: PolicySummary

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\PolicySummary.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Contains simplified information about a Policy.  This object is returned during a Policy search (IPolicySearchAdapter.searchPolicies())

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| InsuredName | varchar | No | - | - | - |
| Address | addressline | No | - | - | Deprecated, please use AddressLine1, AddressLine2 instead |
| City | varchar | No | - | - | - |
| PostalCode | postalcode | No | - | - | - |
| PolicyNumber | policynumber | No | - | - | - |
| ProducerCode | shorttext | No | - | - | Agency that sold the policy. |
| EffectiveDate | datetime | No | - | - | Date on which the policy is effective. |
| ExpirationDate | datetime | No | - | - | Date on which the policy expires. |
| LossDate | datetime | No | - | - | Loss date on the Claim for which the summary was retrieved. Useful in some policy systems to determine what policy version this summary represents. |
| AddressLine1 | addressline | No | - | - | - |
| AddressLine1Kanji | addressline | No | - | - | - |
| AddressLine2 | addressline | No | - | - | - |
| AddressLine2Kanji | addressline | No | - | - | - |
| CityKanji | varchar | No | - | - | - |
| VehicleInvolved | ForeignKey | No | PolicySummaryVehicle | - | If non-null, only this vehicle is required for the Claim; others should be omitted from the returned Policy |
| PropertyInvolved | ForeignKey | No | PolicySummaryProperty | - | If non-null, only this property is required for the Claim; others should be omitted from the returned Policy |
| State | TypeKey | No | - | State | Codes (142 total): [AK, AL, AR, AZ, CA, ...] |
| PolicyType | TypeKey | No | - | PolicyType | Type of policy. Codes (14 total): [PersonalAuto, BusinessAuto, CommercialPackage, GeneralLiability, HOPHomeowners, ...] |
| Status | TypeKey | No | - | PolicyStatus | Codes (7 total): [inforce, expired, paymentpastdue, archived, canceled, ...] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| Vehicles | PolicySummaryVehicle | List of vehicles (in summary form) covered by the policy. |
| Properties | PolicySummaryProperty | List of properties (in summary form) covered by the policy. |

---

### Entity: PolicySummaryProperty

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\PolicySummaryProperty.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PolicySummaryRiskUnit
**Description:** Summary information about a property on a policy summary.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| PropertyNumber | integer | Yes | - | - | Number of the property on the policy. |
| BuildingNumber | shorttext | No | - | - | Building number of the property. |
| Location | shorttext | No | - | - | Location number of the property. |
| Notes | shorttext | No | - | - | Other notes on the property. |
| Description | shorttext | No | - | - | Description. |
| Address | addressline | No | - | - | Deprecated, please use AddressLine1, AddressLine2 instead |
| City | varchar | No | - | - | - |
| CityKanji | varchar | No | - | - | - |
| AddressLine1 | addressline | No | - | - | First line of mailing address |
| AddressLine2 | addressline | No | - | - | Second line of mailing address |
| AddressLine1Kanji | addressline | No | - | - | First line of mailing address Kanji |
| AddressLine2Kanji | addressline | No | - | - | Second line of mailing address Kanji |

---

### Entity: PolicySummaryRiskUnit

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\PolicySummaryRiskUnit.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Summary information for a risk unit item on a policy summary.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Selected | bit | No | - | - | Indicates whether the risk unit should be included when fetching the policy from the policy system. |
| PolicySystemId | policysystemid | No | - | - | Identifier for the risk in an external policy system |
| PolicySummary | ForeignKey | Yes | PolicySummary | - | Related policy. |

---

### Entity: PolicySummaryVehicle

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\PolicySummaryVehicle.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** PolicySummaryRiskUnit
**Description:** Summary information about a vehicle on a policy summary.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| VehicleNumber | integer | Yes | - | - | Number of the vehicle on the policy. |
| LicensePlate | varchar | No | - | - | License plate of the vehicle. |
| Make | varchar | No | - | - | Make of the vehicle. |
| Model | varchar | No | - | - | Model of the vehicle. |
| Color | varchar | No | - | - | Color of the vehicle. |
| Vin | vin | No | - | - | VIN of the vehicle. |
| SerialNumber | varchar | No | - | - | Serial number; only use if VIN is not appropriate (e.g. for boats). |
| State | TypeKey | No | - | Jurisdiction | State (Jurisdiction) in which the vehicle is registered. The Jurisdiction must be associated with JurisdictionType.TC_VEHICLE_REG. Codes (97 total): [AK, AL, AR, AZ, CA, ...] |

---

### Entity: PolicyTypeMetricLimits

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\PolicyTypeMetricLimits.eti`
**Entity Type:** `editable`
**Database Table:** `policytypemetriclimits`
**Supertype:** None
**Description:** Lists all the claim and exposure metric limits for a particular policy type

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Generation | integer | Yes | - | - | Default: 0 Generation number, used to identify when metric limits were created or retired |
| PolicyType | TypeKey | Yes | - | PolicyType | Policy type for the limits. Codes (14 total): [PersonalAuto, BusinessAuto, CommercialPackage, GeneralLiability, HOPHomeowners, ...] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| ClaimMetricLimits | ClaimMetricLimit | Claim metric limits for this policy type. |
| ExposureMetricLimits | ExposureMetricLimit | Exposure metric limits for this policy type. |

---

### Entity: RecoveryCoding

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\RecoveryCoding.eti`
**Entity Type:** `versionable`
**Database Table:** `recoverycoding`
**Supertype:** None
**Description:** A unique combination of ReserveLine (Claim, Exposure, CostType, CostCategory, and ReservingCurrency) and RecoveryCategory, against which Recovery and RecoveryReserve transactions are made.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| ReserveLine | ForeignKey | Yes | ReserveLine | - | The ReserveLine to which all associated transactions should be coded. |
| RecoveryCategory | TypeKey | Yes | - | RecoveryCategory | The RecoveryCategory to which all associated transactions should be coded. Codes: [unspecified, salvage, subro, credit_loss, credit_exp, deductible] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| RecoveryTAccounts | RecoveryTAccount | Child collection |
| Transactions | Transaction | Set of transactions that coded to this RecoveryCoding. |

---

### Entity: RecoveryReserveView

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\RecoveryReserveView.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Aggregates the information needed to display a RecoveryReserve using the RecoveryReserve filter of the Financials Transactions page. Subtype of TransactionView.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: RecoverySearchCriteria

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\RecoverySearchCriteria.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Non-persistent set of criteria to use in searching for a specific Recovery.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| ClaimNumber | claimnumber | No | - | - | - |
| CreatedByUser | ForeignKey | No | User | - | Foreign key target: User |
| NameCriteria | ForeignKey | Yes | CCNameCriteria | - | Foreign key target: CCNameCriteria |
| DateCriterionChoice | ForeignKey | Yes | DateCriterionChoice | - | Foreign key target: DateCriterionChoice |
| FinancialCriterion | ForeignKey | Yes | FinancialCriterionMC | - | Foreign key target: FinancialCriterionMC |
| CostType | TypeKey | No | - | CostType | Codes: [claimcost, unspecified, aoexpense, dccexpense] |
| RecoveryStatus | TypeKey | No | - | TransactionStatus | Codes (20 total): [draft, pendingapproval, awaitingsubmission, submitting, requesting, ...] |
| RecoveryCategory | TypeKey | No | - | RecoveryCategory | Codes: [unspecified, salvage, subro, credit_loss, credit_exp, deductible] |

---

### Entity: RecoverySearchView

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\RecoverySearchView.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Aggregates the information needed to display a Recovery on the Recovery Search page. Subtype of TransactionSearchView.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: RecoveryTAccount

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\RecoveryTAccount.eti`
**Entity Type:** `editable`
**Database Table:** `recoverytaccount`
**Supertype:** None
**Description:** Represents the value of Recovery and RecoveryReserve transactions in a certain lifecycle state.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| DebitReservingBalance | money | Yes | - | - | The balance of the reserving currency debit side of this t-account's ledger. |
| CreditReservingBalance | money | Yes | - | - | The balance of the reserving currency credit side of this t-account's ledger. |
| RecoveryCoding | ForeignKey | Yes | RecoveryCoding | - | FK to the RecoveryCoding that this TAccount is assoicated with. |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| RecoveryTAccountLineItems | RecoveryTAccountLineItem | Line items for this RecoveryTAccount. |

---

### Entity: RecoveryTAccountLineItem

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\RecoveryTAccountLineItem.eti`
**Entity Type:** `editable`
**Database Table:** `recoverytaccountlineitem`
**Supertype:** None
**Description:** A specific amount of money, contained with a transaction and belonging to a t-account

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| ReservingAmount | money | Yes | - | - | The amount of money (in the reserving currency) in this line item that was either credited or debited against a RecoveryTAccount. |
| CreditingTransaction | ForeignKey | No | RecTAccountTransaction | - | The TAccountTransaction for which this lineitem credits a t-account. |
| DebitingTransaction | ForeignKey | No | RecTAccountTransaction | - | The TAccountTransaction for which this lineitem debits a t-account. |
| DenormTransaction | ForeignKey | No | RecTAccountTransaction | - | Denormalized FK to RecTAccountTransaction table in order to speed up certain queries.  If both CreditingTransactionID and DebitingTransactionID are not null, then this field is NULL, otherwise this field will have same value as the non-null FK.  This allows us to query against this field only when looking for RecTAccountTransactions that are currently contributing to a RecoveryTAccount. |
| RecoveryTAccount | ForeignKey | Yes | RecoveryTAccount | - | RecoveryTAccount with which this line item is associated. |

---

### Entity: RecoveryView

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\RecoveryView.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Aggregates the information needed to display a Recovery using the Recovery filter of the Financials Transactions page. Subtype of TransactionView.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: ReserveLineWrapper

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ReserveLineWrapper.eti`
**Entity Type:** `versionable`
**Database Table:** `reservelinewrapper`
**Supertype:** None
**Description:** Wraps a ReserveLine associated with a BulkInvoiceItem.  Necessary to allow saving of a draft BulkInvoiceItem that is set to have a new ReserveLine.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| ReserveLine | ForeignKey | No | ReserveLine | - | The ReserveLine wrapped by this ReserveLineWrapper. |
| BulkInvoiceItemInfo | OneToOne | No | BulkInvoiceItemInfo | - | One-to-one link |

---

### Entity: ReserveRule

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ReserveRule.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** CCRule
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| ExposureTypes | AppCritExposureType | Child collection |
| ClaimSegments | AppCritClaimSegment | Child collection |

---

### Entity: ReserveView

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ReserveView.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Aggregates the information needed to display a Reserve using the Reserve filter of the Financials Transactions page. Subtype of TransactionView.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: ServiceRequestChange

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ServiceRequestChange.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\ServiceRequestChange.etx`
**Entity Type:** `editable`
**Database Table:** `servicerequestchange`
**Supertype:** None
**Description:** Represents a change to a ServiceRequest. Instances of this entity are ordered by Sequence.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Sequence | integer | Yes | - | - | The sequence of this change on the ServiceRequest. ServiceRequestChanges are ordered consecutively starting with Sequence of 1. |
| Timestamp | datetime | Yes | - | - | The time at which this change was applied. This timestamp is stored for informational purposes, but it may be possible for the relative timestamps of two instances to incorrectly or ambiguously indicate the relative order of two instances. For reliable ordering, use the Sequence property instead. |
| Description | longtext | No | - | - | An optional explanation for this change. |
| Progress_Chg | bit | Yes | - | - | Default: false True if Progress is changing. |
| QuoteStatus_Chg | bit | Yes | - | - | Default: false True if Quote Status is changing. |
| Instruction_Chg | bit | Yes | - | - | Default: false True if Instruction is changing. |
| ServiceRequest | ForeignKey | Yes | ServiceRequest | - | The related service request. |
| Initiator | ForeignKey | Yes | Contact | - | The user who initiated this change. |
| RelatedStatement | ForeignKey | No | ServiceRequestStatement | - | The service request statement that is related to this change. |
| New_Instruction | ForeignKey | No | ServiceRequestInstruction | - | The new value of ServiceRequest.Instruction, or null if Instruction did not change. Note that it is expected that ServiceRequest.Instruction will only start referring to a particular instruction once -- there should be at most one ServiceRequestChange on a ServiceRequest referring to a particular ServiceRequestInstruction with this foreign key. |
| Operation | TypeKey | No | - | ServiceRequestOperation | The operation performed during this change Codes (19 total): [submitinstruction, specialistacceptedwork, addquote, approvequote, specialistcompletedwork, ...] |
| New_Progress | TypeKey | No | - | ServiceRequestProgress | The new value of ServiceRequest.Progress, or null if Progress did not change. Codes (8 total): [requested, declined, specialistwaiting, inprogress, workcomplete, ...] |
| New_QuoteStatus | TypeKey | No | - | ServiceRequestQuoteStatus | The new value of ServiceRequest.QuoteStatus, or null if Quote Status did not change. Codes: [waitingforapproval, waitingforquote, approved, noquote, quoted] |
| ExpectedServiceCompletionDate_Chg_Ext | bit | Yes | - | - | [Extension] True if ExpectedServiceCompletionDate is changing. |
| New_ExpectedServiceCompletionDate_Ext | datetime | No | - | - | [Extension] The new value of ServiceRequest.ExpectedServiceCompletionDate, or null if ExpectedServiceCompletionDate did not change. |
| ExpectedQuoteCompletionDate_Chg_Ext | bit | Yes | - | - | [Extension] True if ExpectedQuoteCompletionDate is changing. |
| New_ExpectedQuoteCompletionDate_Ext | datetime | No | - | - | [Extension] The new value of ServiceRequest.ExpectedQuoteCompletionDate, or null if ExpectedQuoteCompletionDate did not change. |

---

### Entity: ServiceRequestDocumentLink

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ServiceRequestDocumentLink.eti`
**Entity Type:** `joinarray`
**Database Table:** `servicerequestdocumentlink`
**Supertype:** None
**Description:** Associates a Service Request to a Document. Use ServiceRequest.linkDocument and unlinkDocument to create links between ServiceRequests and documents.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| VisibleToSpecialist | bit | Yes | - | - | Default: false Whether this document should be visible to the specialist. |
| DateSpecialistNotified | datetime | No | - | - | The date that the specialist was notified about the linked document, or null if the specialist has not been notified. |
| ServiceRequest | ForeignKey | Yes | ServiceRequest | - | Service Request the document is linked to. |
| Document | ForeignKey | No | Document | - | Associated Document. Warning: even though there is always a Document associated with this entity, this field may be null when the IDocumentMetadataSource plugin is enabled. To reliably get the associated Document, use the LinkedDocument property. |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| StatementDocumentLinks | ServiceRequestStatementDocumentLink | The join entity that holds the information for statements associated with this document |

---

### Entity: ServiceRequestInstructionService

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ServiceRequestInstructionService.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\ServiceRequestInstructionService.etx`
**Entity Type:** `editable`
**Database Table:** `servicereqinstructionsvc`
**Supertype:** None
**Description:** Join entity between a ServiceRequestInstruction and type of service

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Instruction | ForeignKey | Yes | ServiceRequestInstruction | - | The instruction as part of which the linked service should be performed. |
| Service | ForeignKey | Yes | SpecialistService | - | The service to be performed. |

---

### Entity: ServiceRequestMetric

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ServiceRequestMetric.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\ServiceRequestMetric.etx`
**Entity Type:** `editable`
**Database Table:** `servreqmetric`
**Supertype:** None
**Description:** Metrics related to a service request

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| ServiceRequest | ForeignKey | Yes | ServiceRequest | - | Service Request to which this metric is related. |
| MetricUnit | TypeKey | No | - | MetricUnit | Units for this type of metric. Codes: [numeric, percent, currency, hours, days] |

---

### Entity: ServiceRequestMetricLimit

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ServiceRequestMetricLimit.eti`
**Extension Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\ServiceRequestMetricLimit.etx`
**Entity Type:** `editable`
**Database Table:** `servicerequestmetriclimit`
**Supertype:** None
**Description:** 

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| ServiceRequestMetricType | TypeKey | Yes | - | ServiceRequestMetric | Type of service request metric to which this limit applies Codes: [ServiceTimelinessServiceRequestMetric, SpecialistInitialResponseTimeServiceRequestMetric, InvoiceVarianceVsQuoteServiceRequestMetric, QuoteTimelinessServiceRequestMetric, NumberOfDelaysServiceRequestMetric, ServiceCycleTimeServiceRequestMetric] |
| ServiceCategory_Ext | ForeignKey | No | SpecialistService | - | [Extension] Category of service that this limit applies to, null if it applies to any category |
| SpecialistService_Ext | ForeignKey | No | SpecialistService | - | [Extension] Fully-specified service that this limit applies to, null if it applies to any service |
| MetricUnit_Ext | TypeKey | Yes | - | MetricUnit | [Extension] Units for this type of metric limit. |
| Currency_Ext | TypeKey | No | - | Currency | [Extension] Currency for this limit, for non-money based limits this is always the default currency |
| LimitType_Ext | TypeKey | Yes | - | ServiceRequestMetricLimitType | [Extension] Calculation type for this limit |
| ServiceRequestTier_Ext | TypeKey | No | - | ServiceRequestTier | [Extension] Service request tier to which this limit applies, or null if it applies to any tier |
| CustomerServiceTier_Ext | TypeKey | No | - | CustomerServiceTier | [Extension] Customer service tier that this limit applies to, null if it applies to any service tier |

---

### Entity: ServiceRequestStatement

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ServiceRequestStatement.eti`
**Entity Type:** `editable`
**Database Table:** `servicerequeststatement`
**Supertype:** None
**Description:** An estimation (such as a quote or invoice) received from a specialist and related to a Service Request.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| ReferenceNumber | shorttext | No | - | - | A string identifier assigned to this ServiceRequestStatement by the specialist. The value of this field may only be meaningful to the specialist. |
| StatementCreationTime | datetime | Yes | - | - | The time at which this statement was created. |
| ApprovalDate | datetime | No | - | - | The time at which this statement was approved. |
| Description | longtext | Yes | - | - | The description for the statement |
| DeclinedReason | longtext | No | - | - | The reason the statement was declined. When the state changes this value is recalculated, as the previous value not longer makes sense. |
| ServiceRequest | ForeignKey | Yes | ServiceRequest | - | Service Request the statement is linked to. |
| ApprovedBy | ForeignKey | No | User | - | The user who approved this statement. |
| Source | TypeKey | No | - | StatementSource | The external system from which this data comes  Codes: [manual, gwportal] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| StatementDocumentLinks | ServiceRequestStatementDocumentLink | The join entity that holds the information for documents associated with this statement |
| LineItems | ServiceRequestStatementLineItem | Child collection |

---

### Entity: ServiceRequestStatementDocumentLink

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ServiceRequestStatementDocumentLink.eti`
**Entity Type:** `joinarray`
**Database Table:** `servicereqstatementdoclink`
**Supertype:** None
**Description:** Associates a Service Request Statement to a Document Link.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| ServiceRequestDocumentLink | ForeignKey | Yes | ServiceRequestDocumentLink | - | Service Request Document Link the statement is linked to. |
| ServiceRequestStatement | ForeignKey | Yes | ServiceRequestStatement | - | The associated statement for the document link. |

---

### Entity: ServiceRequestStatementLineItem

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ServiceRequestStatementLineItem.eti`
**Entity Type:** `editable`
**Database Table:** `servicereqstatementline`
**Supertype:** None
**Description:** A line item from a ServiceRequestStatement

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Description | shorttext | No | - | - | - |
| Amount | currencyamount | Yes | - | - | - |
| ServiceRequestStatement | ForeignKey | Yes | ServiceRequestStatement | - | Foreign key target: ServiceRequestStatement |
| Category | TypeKey | No | - | ServiceRequestStatementLineItemCategory | Codes (14 total): [inspection, parts, labor, towing, CourtCosts, ...] |

---

### Entity: Subrogation

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Subrogation.eti`
**Entity Type:** `retireable`
**Database Table:** `subrogation`
**Supertype:** None
**Description:** Represents the investigation that a user must perform to determine whether subrogation should be pursued on the associated Exposure or Claim. 

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| CloseComment | shorttext | No | - | - | Comment upon close of Subrogation opportunity |
| SubrogationSummary | ForeignKey | Yes | SubrogationSummary | - | Associated SubrogationSummary |
| Exposure | ForeignKey | No | Exposure | - | The associated Exposure. If null, this subrogation is a claim-level subrogation. |
| Status | TypeKey | No | - | SubrogationStatus | Status of this subrogation Codes: [closed, review, open] |
| Outcome | TypeKey | No | - | SubroClosedOutcome | SubroClosedOutcome Codes: [full, compromised, uncollectable, discontinued, notpursued] |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| SubroAdversePartyOverrides | SubroAdversePartyOverride | Child collection |

---

### Entity: SubrogationClaimIndicator

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\SubrogationClaimIndicator.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** ClaimIndicator
**Description:** Is subrogation on Claim?

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: SubrogationView

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\SubrogationView.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Subrogation view entity.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: TransactionDefaultView

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\TransactionDefaultView.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Aggregates the information needed to display a Transaction using the All or Custom filters of the Financials Transactions page. Subtype of TransactionView.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: TransactionEditWrapper

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\TransactionEditWrapper.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Wraps a Transaction to keep track of a new amount entered by the user. Used with TransactionWizardHelper. Internally stores an amount in the claim currency and in the currency of the transaction.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| NewTransactionAmount | money | Yes | - | - | Internal storage of the amount in the transaction currency. |
| NewReservingAmount | money | Yes | - | - | Internal storage of the amount in the reserving currency. |
| PrevBaseAmount | money | Yes | - | - | The base amount in the reserving currency for the reserve line corresponding to this row. This is intended to help determine whether the base amount has changed and therefore whether the amount properties should be reset when the reserve line changes. |
| Transaction | ForeignKey | Yes | Transaction | - | Wrapped transaction. |
| PrevReservingCurrency | TypeKey | Yes | - | Currency | The previous reserving currency for the reserve line corresponding to this row. This is intended to help determine whether the reserving currency has changed and therefore whether the amount properties should be reset when the reserve line changes. Codes (7 total): [usd, eur, gbp, cad, aud, ...] |

---

### Entity: TransactionId

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\TransactionId.eti`
**Entity Type:** `nonkeyable`
**Database Table:** `transactionid`
**Supertype:** None
**Description:** Transaction ids sent to create the illusion of idempotency

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| tid | varchar | Yes | - | - | Unique transaction id |
| CreationTime | datetime | No | - | - | Time of creating the transaction id. |

---

### Entity: TransactionLineItem

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\TransactionLineItem.eti`
**Entity Type:** `retireable`
**Database Table:** `transactionlineitem`
**Supertype:** None
**Description:** A line item within a transaction (either reserve, recovery, or payment) for further categorization.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Retired | softentityreference (long) | Yes | - | - | Retireable soft-delete flag (0 = active, non-zero = retired) |
| TransactionAmount | currencyamount | Yes | - | - | The amount of this line item, in the transaction currency. |
| ReservingAmount | currencyamount | Yes | - | - | The amount of this line item in the Currency of the ReserveLine (ReservingCurrency). |
| ClaimAmount | currencyamount | Yes | - | - | The amount of this line item in the Claim's currency. |
| ReportingAmount | currencyamount | Yes | - | - | The amount of this line item in the app's default currency (reporting currency). |
| ClaimForExAmount | currencyamount | Yes | - | - | Default: 0 The foreign exchange adjustment for this line item in the claim currency. This stores the amount by which the current value of ClaimAmount exceeds its original value. |
| ReservingForExAmount | currencyamount | Yes | - | - | Default: 0 The foreign exchange adjustment for this line item in the reserving currency. This stores the amount by which the current value of ReservingAmount exceeds its original value. |
| ReportingForExAmount | currencyamount | Yes | - | - | Default: 0 The foreign exchange adjustment for this line item in the reporting currency. This stores the amount by which the current value of ReportingAmount exceeds its original value. |
| Comments | shorttext | No | - | - | A note or description of the line item. |
| Transaction | ForeignKey | Yes | Transaction | - | The parent transaction. |
| Deductible | ForeignKey | No | Deductible | - | The deductible for which this transaction line item is applied, if any. |
| LineCategory | TypeKey | No | - | linecategory | The category of this line item. Codes (27 total): [deductible, formerdeductible, other, doctor, nurse, ...] |

---

### Entity: TransactionOffset

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\TransactionOffset.eti`
**Entity Type:** `joinarray`
**Database Table:** `transactionoffset`
**Supertype:** None
**Description:** Represents the relationship between a transaction and its offset.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Transaction | ForeignKey | Yes | Transaction | - | The transaction being offset. |
| Offset | ForeignKey | Yes | Transaction | - | The offset transaction, to negate the original transaction. |

---

### Entity: TransactionOnset

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\TransactionOnset.eti`
**Entity Type:** `joinarray`
**Database Table:** `transactiononset`
**Supertype:** None
**Description:** Represents the relationship between a transaction and its onset.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| OnsetPublicID | publicid | No | - | - | PublicID of the onset, used when the FK to the onset has been severed for archiving. |
| Transaction | ForeignKey | Yes | Transaction | - | The transaction being onset. |
| Onset | ForeignKey | No | Transaction | - | The onset (recode or transfer) transaction, same as the original but on the new ReserveLine/Claim. |

---

### Entity: TransactionSearchView

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\TransactionSearchView.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Abstract base view entity that aggregates the information needed to display a Transaction on a Transaction Search page.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: TransactionSetDocument

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\TransactionSetDocument.eti`
**Entity Type:** `joinarray`
**Database Table:** `transsetdocument`
**Supertype:** None
**Description:** Associates a Document to a TransactionSet.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| TransactionSet | ForeignKey | Yes | TransactionSet | - | TransactionSet the document is linked to. |
| Document | ForeignKey | Yes | Document | - | Associated Document. |

---

### Entity: TransactionTAccountOperationsDelegate

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\TransactionTAccountOperationsDelegate.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Status | TypeKey | Yes | - | transactionstatus | Status of the transaction. Further refines the LifeCycleState. Can only change status directly to another status in the same LifeCycleState, which does not affect Taccounts. Codes (20 total): [draft, pendingapproval, awaitingsubmission, submitting, requesting, ...] |
| LifeCycleState | TypeKey | Yes | - | transactionlifecyclestate | Current internal lifecycle state of the transaction. Changing state affects T-accounts. Codes (9 total): [new, draft, pendingapproval, rejected, denied, ...] |

---

### Entity: TransactionView

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\TransactionView.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Abstract base view entity that aggregates the information needed to display a Transaction on the Financials Transactions page.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: ClaimWorkloadClassification

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\ClaimWorkloadClassification.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WorkloadClassification
**Description:** Claim Workload Classification

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: ExposureCondition

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\ExposureCondition.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** ClassificationCondition
**Description:** Exposure Classification Condition

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| ConditionFilters | ExposureConditionFilter | Child collection |

---

### Entity: ExposureConditionFilter

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\ExposureConditionFilter.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** ConditionFilter
**Description:** Classification condition filter by Exposure

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| CoverageType | TypeKey | Yes | - | CoverageType | The coverage type Codes (292 total): [GLCGLCov, GLDeductible, GLPollutionDesignatedCov, GLPollutionShortTermCov, PollutionBroadLimited, ...] |
| CoverageSubType | TypeKey | Yes | - | CoverageSubType | The coverage subtype Codes (327 total): [GLCGLCov_ops_bi, GLCGLCov_ops_pd, GLCGLCov_ops_mp, GLCGLCov_ops_gd, GLCGLCov_prod_bi, ...] |
| LossPartyType | TypeKey | No | - | LossPartyType | The loss party; generally either first or third-party loss. Codes: [insured, third_party] |

---

### Entity: ExposureWorkloadClassification

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\ExposureWorkloadClassification.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** WorkloadClassification
**Description:** Exposure Workload Classification

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: IncidentSeverityCondition

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\IncidentSeverityCondition.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** ClassificationCondition
**Description:** Incident Severity Classification Condition

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

#### Child Arrays & Collections

| Array Name | Target Entity | Description |
|------------|---------------|-------------|
| ConditionFilters | IncidentSeverityConditionFilter | Child collection |

---

### Entity: IncidentSeverityConditionFilter

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\IncidentSeverityConditionFilter.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** ConditionFilter
**Description:** Classification condition filter by Incident Severity

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| IncidentSeverity | TypeKey | Yes | - | SeverityType | Classification condition filter by Incident Severity Codes (19 total): [minor, moderate-gen, moderate-auto, moderate-prop, major-gen, ...] |

---

### Entity: ReserveChangeCountClaimMetric

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\ReserveChangeCountClaimMetric.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** IntegerClaimMetric
**Description:** Number of Reserve Changes

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |

---

### Entity: ServiceRequestMetricEscalationDelegate

**Source:** `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\ServiceRequestMetricEscalationDelegate.eti`
**Entity Type:** `standard`
**Database Table:** `N/A`
**Supertype:** None
**Description:** Not specified in source.

#### Fields

| Field | Type | Required | Reference | Typelist | Notes |
|------|------|----------|-----------|----------|-------|
| ID | Key | Yes | - | - | Primary key, unique identifier |
| PublicID | publicid (varchar 64) | Yes | - | - | Unique public business identifier |
| Escalated | bit | No | - | - | Default: false Indicates if this metric has been previously escalated |

---

