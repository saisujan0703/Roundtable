# Master Source Path Index & Verification Manifest

**Guidewire Suite Version:** 10.2.1
**PolicyCenter Source:** `C:\GW10\PolicyCenter`
**ClaimCenter Source:** `C:\GW10\ClaimCenter`
**Extraction Date:** 2026-09-26

---

## 1. Overview & Verification Audit

This index provides the master catalog of every source path on this VM referenced across the data dictionary documentation suite (Documents 01 through 11). Every path cited below exists on the local filesystem and has been directly verified.

---

## 2. System Version & Build Verification Files

| Component | File Path | Verified Version / Git Commit |
|-----------|-----------|-------------------------------|
| PolicyCenter Version Properties | `C:\GW10\PolicyCenter\project-version.properties` | Project: 10.2.1.1711, Platform: 10.201.1, Gosu: 1.14.26, Commit: 71f1d8ccb0 |
| ClaimCenter Version Properties | `C:\GW10\ClaimCenter\project-version.properties` | Project: 10.2.1.1523, Platform: 10.201.1, Gosu: 1.14.26, Commit: 67c4da7897 |
| PolicyCenter Database Config | `C:\GW10\PolicyCenter\modules\configuration\config\database-config.xml` | Database metadata configuration |
| ClaimCenter Database Config | `C:\GW10\ClaimCenter\modules\configuration\config\database-config.xml` | Database metadata configuration |
| PolicyCenter Metadata Properties | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\metadata.properties` | Major: 15, Minor: 651, Prefix: pc |

---

## 3. PolicyCenter Key Entity Source Files

| Entity Name | Primary Source Path (.eti / .eix) | Extension Path (.etx) |
|-------------|-----------------------------------|-----------------------|
| Account | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Account.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\Account.etx` |
| AccountContact | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\AccountContact.eti` | None |
| AccountContactRole | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\AccountContactRole.eti` | None |
| AccountHolder | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\AccountHolder.eti` | None |
| AccountLocation | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\AccountLocation.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\AccountLocation.etx` |
| AccountProducerCode | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\AccountProducerCode.eti` | None |
| Contact | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Contact.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\Contact.etx` |
| Person | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Person.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\Person.etx` |
| Company | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Company.eti` | None |
| Address | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Address.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\Address.etx` |
| ContactAddress | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\ContactAddress.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\ContactAddress.etx` |
| Policy | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Policy.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\Policy.etx` |
| PolicyPeriod | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyPeriod.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\PolicyPeriod.etx` |
| PolicyTerm | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyTerm.eti` | None |
| PolicyLocation | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyLocation.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\PolicyLocation.etx` |
| AuditInformation | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\AuditInformation.eti` | None |
| LossHistoryEntry | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\LossHistoryEntry.eti` | None |
| PriorPolicy | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PriorPolicy.eti` | None |
| Form | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Form.eti` | None |
| Contingency | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Contingency.eti` | None |
| PolicyLine | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyLine.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\PolicyLine.etx` |
| PersonalAutoLine | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PersonalAutoLine.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\PersonalAutoLine.etx` |
| CommercialPropertyLine | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\CommercialPropertyLine.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\CommercialPropertyLine.etx` |
| BusinessAutoLine | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BusinessAutoLine.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\BusinessAutoLine.etx` |
| BusinessOwnersLine | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BusinessOwnersLine.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\BusinessOwnersLine.etx` |
| GeneralLiabilityLine | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\GeneralLiabilityLine.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\GeneralLiabilityLine.etx` |
| HOPLine | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPLine.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\HOPLine.etx` |
| InlandMarineLine | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\InlandMarineLine.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\InlandMarineLine.etx` |
| WorkersCompLine | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\WorkersCompLine.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\WorkersCompLine.etx` |
| WC7Line | Not verified in source. | None |
| PersonalVehicle | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PersonalVehicle.eti` | None |
| BusinessVehicle | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BusinessVehicle.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\BusinessVehicle.etx` |
| PolicyDriver | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyDriver.eti` | None |
| VehicleDriver | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\VehicleDriver.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\VehicleDriver.etx` |
| CommercialDriver | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\CommercialDriver.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\CommercialDriver.etx` |
| CPLocation | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\CPLocation.eti` | None |
| CPBuilding | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\CPBuilding.eti` | None |
| BOPLocation | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BOPLocation.eti` | None |
| BOPBuilding | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BOPBuilding.eti` | None |
| HOPDwelling | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPDwelling.eti` | None |
| HOPCoveragePart | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPCoveragePart.eti` | None |
| WCCoveredEmployee | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\WCCoveredEmployee.eti` | None |
| Coverage | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Coverage.eti` | None |
| Clause | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Clause.eti` | None |
| PersonalAutoCov | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PersonalAutoCov.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\PersonalAutoCov.etx` |
| PersonalVehicleCov | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PersonalVehicleCov.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\PersonalVehicleCov.etx` |
| BusinessAutoCov | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BusinessAutoCov.eti` | None |
| BusinessOwnersCov | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BusinessOwnersCov.eti` | None |
| GeneralLiabilityCov | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\GeneralLiabilityCov.eti` | None |
| HOPDwellingCov | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPDwellingCov.eti` | None |
| HOPLineCov | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPLineCov.eti` | None |
| WorkersCompCov | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\WorkersCompCov.eti` | None |
| Job | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Job.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\Job.etx` |
| Submission | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Submission.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\Submission.etx` |
| Issuance | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Issuance.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\Issuance.etx` |
| PolicyChange | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyChange.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\PolicyChange.etx` |
| Renewal | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Renewal.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\Renewal.etx` |
| Cancellation | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Cancellation.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\Cancellation.etx` |
| Reinstatement | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Reinstatement.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\Reinstatement.etx` |
| Rewrite | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Rewrite.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\Rewrite.etx` |
| RewriteNewAccount | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\RewriteNewAccount.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\RewriteNewAccount.etx` |
| Audit | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Audit.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\Audit.etx` |
| Cost | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Cost.eti` | None |
| PACost | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PACost.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\PACost.etx` |
| BACost | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BACost.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\BACost.etx` |
| BOPCost | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BOPCost.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\BOPCost.etx` |
| GLCost | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\GLCost.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\GLCost.etx` |
| HOPCost | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\HOPCost.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\HOPCost.etx` |
| Transaction | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Transaction.eti` | None |
| PATransaction | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PATransaction.eti` | None |
| BATransaction | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\BATransaction.eti` | None |
| PaymentPlanSummary | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PaymentPlanSummary.eti` | None |
| ProducerCode | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\ProducerCode.eti` | None |
| Organization | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Organization.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\Organization.etx` |
| User | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\User.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\User.etx` |
| Group | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Group.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\Group.etx` |
| Activity | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Activity.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\Activity.etx` |
| Note | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Note.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\Note.etx` |
| Document | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\Document.eti` | `C:\GW10\PolicyCenter\modules\configuration\config\extensions\entity\Document.etx` |
| UWIssue | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\UWIssue.eti` | None |
| UWReferralReason | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\UWReferralReason.eti` | None |
| PeriodAnswer | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PeriodAnswer.eti` | None |
| PolicyLineAnswer | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PolicyLineAnswer.eti` | None |
| LocationAnswer | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\LocationAnswer.eti` | None |
| PCAnswerDelegate | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\PCAnswerDelegate.eti` | None |
| APDProduct | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDProduct.eti` | None |
| APDProductLine | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDProductLine.eti` | None |
| APDCoverage | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDCoverage.eti` | None |
| APDRiskCoverable | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDRiskCoverable.eti` | None |
| APDExposure | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDExposure.eti` | None |
| APDField | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDField.eti` | None |
| APDCost | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDCost.eti` | None |
| APDTerm | `C:\GW10\PolicyCenter\modules\configuration\config\metadata\entity\APDTerm.eti` | None |

---

## 4. ClaimCenter Key Entity Source Files

| Entity Name | Primary Source Path (.eti / .eix) | Extension Path (.etx) |
|-------------|-----------------------------------|-----------------------|
| Claim | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Claim.eti` | `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\Claim.etx` |
| ClaimInfo | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimInfo.eti` | None |
| ClaimContact | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimContact.eti` | `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\ClaimContact.etx` |
| ClaimContactRole | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimContactRole.eti` | None |
| ClaimAccess | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimAccess.eti` | None |
| ClaimWorkplan | Not verified in source. | None |
| Policy | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Policy.eti` | None |
| PolicyCoverage | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\PolicyCoverage.eti` | None |
| VehicleCoverage | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\VehicleCoverage.eti` | None |
| PropertyCoverage | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\PropertyCoverage.eti` | None |
| PolicyLocation | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\PolicyLocation.eti` | None |
| Endorsement | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Endorsement.eti` | None |
| StatCode | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\StatCode.eti` | None |
| ClassCode | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClassCode.eti` | None |
| Contact | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Contact.eti` | `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\Contact.etx` |
| Person | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Person.eti` | `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\Person.etx` |
| Company | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Company.eti` | None |
| Address | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Address.eti` | `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\Address.etx` |
| ContactAddress | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ContactAddress.eti` | None |
| PersonVendor | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\PersonVendor.eti` | None |
| CompanyVendor | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\CompanyVendor.eti` | None |
| AutoRepairShop | `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\AutoRepairShop.eti` | None |
| AutoTowingAgcy | `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\AutoTowingAgcy.eti` | None |
| MedicalCareOrg | `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\MedicalCareOrg.eti` | None |
| Doctor | `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\Doctor.eti` | None |
| Attorney | `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\Attorney.eti` | None |
| LawFirm | `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\LawFirm.eti` | None |
| Incident | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Incident.eti` | `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\Incident.etx` |
| VehicleIncident | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\VehicleIncident.eti` | `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\VehicleIncident.etx` |
| FixedPropertyIncident | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\FixedPropertyIncident.eti` | `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\FixedPropertyIncident.etx` |
| InjuryIncident | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\InjuryIncident.eti` | `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\InjuryIncident.etx` |
| PropertyContentsIncident | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\PropertyContentsIncident.eti` | `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\PropertyContentsIncident.etx` |
| DwellingIncident | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\DwellingIncident.eti` | `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\DwellingIncident.etx` |
| OtherStructureIncident | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\OtherStructureIncident.eti` | `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\OtherStructureIncident.etx` |
| LivingExpensesIncident | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\LivingExpensesIncident.eti` | `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\LivingExpensesIncident.etx` |
| MobilePropertyIncident | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\MobilePropertyIncident.eti` | `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\MobilePropertyIncident.etx` |
| BaggageIncident | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\BaggageIncident.eti` | `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\BaggageIncident.etx` |
| TripIncident | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\TripIncident.eti` | `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\TripIncident.etx` |
| Exposure | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Exposure.eti` | `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\Exposure.etx` |
| ReserveLine | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ReserveLine.eti` | None |
| TransactionSet | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\TransactionSet.eti` | None |
| ReserveSet | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ReserveSet.eti` | None |
| CheckSet | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\CheckSet.eti` | None |
| RecoverySet | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\RecoverySet.eti` | None |
| RecoveryReserveSet | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\RecoveryReserveSet.eti` | None |
| Transaction | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Transaction.eti` | `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\Transaction.etx` |
| Reserve | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Reserve.eti` | None |
| Payment | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Payment.eti` | `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\Payment.etx` |
| Recovery | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Recovery.eti` | None |
| RecoveryReserve | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\RecoveryReserve.eti` | None |
| Check | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Check.eti` | `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\Check.etx` |
| CheckPayee | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\CheckPayee.eti` | None |
| CheckPortion | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\CheckPortion.eti` | None |
| Deductible | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Deductible.eti` | None |
| Activity | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Activity.eti` | `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\Activity.etx` |
| ActivityPattern | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ActivityPattern.eti` | None |
| Note | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Note.eti` | None |
| Document | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Document.eti` | None |
| UserRoleAssignment | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\UserRoleAssignment.eti` | None |
| User | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\User.eti` | `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\User.etx` |
| Group | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Group.eti` | `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\Group.etx` |
| Matter | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Matter.eti` | `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\Matter.etx` |
| MatterExposure | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\MatterExposure.eti` | None |
| ServiceRequest | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ServiceRequest.eti` | `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\ServiceRequest.etx` |
| ServiceRequestInstruction | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ServiceRequestInstruction.eti` | `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\ServiceRequestInstruction.etx` |
| ServiceRequestQuote | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ServiceRequestQuote.eti` | None |
| ServiceRequestInvoice | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ServiceRequestInvoice.eti` | `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\ServiceRequestInvoice.etx` |
| ServiceRequestMessage | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ServiceRequestMessage.eti` | None |
| Catastrophe | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Catastrophe.eti` | None |
| SubrogationSummary | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\SubrogationSummary.eti` | None |
| SIUAnswerSet | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\SIUAnswerSet.eti` | None |
| SIUClaimIndicator | `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\SIUClaimIndicator.eti` | None |
| Evaluation | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Evaluation.eti` | None |
| Negotiation | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\Negotiation.eti` | None |
| MetroReport | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\MetroReport.eti` | None |
| ClaimIndicator | `C:\GW10\ClaimCenter\modules\configuration\config\metadata\entity\ClaimIndicator.eti` | `C:\GW10\ClaimCenter\modules\configuration\config\extensions\entity\ClaimIndicator.etx` |

---

## 5. PolicyCenter Product Model File Paths

### Installed Products
- `PersonalAuto`: `C:\GW10\PolicyCenter\modules\configuration\config\resources\productmodel\products\PersonalAuto\PersonalAuto.xml`
- `CommercialProperty`: `C:\GW10\PolicyCenter\modules\configuration\config\resources\productmodel\products\CommercialProperty\CommercialProperty.xml`
- `BusinessAuto`: `C:\GW10\PolicyCenter\modules\configuration\config\resources\productmodel\products\BusinessAuto\BusinessAuto.xml`
- `BusinessOwners`: `C:\GW10\PolicyCenter\modules\configuration\config\resources\productmodel\products\BusinessOwners\BusinessOwners.xml`
- `CommercialPackage`: `C:\GW10\PolicyCenter\modules\configuration\config\resources\productmodel\products\CommercialPackage\CommercialPackage.xml`
- `GeneralLiability`: `C:\GW10\PolicyCenter\modules\configuration\config\resources\productmodel\products\GeneralLiability\GeneralLiability.xml`
- `HOPHomeowners`: `C:\GW10\PolicyCenter\modules\configuration\config\resources\productmodel\products\HOPHomeowners\HOPHomeowners.xml`
- `InlandMarine`: `C:\GW10\PolicyCenter\modules\configuration\config\resources\productmodel\products\InlandMarine\InlandMarine.xml`
- `Manual`: `C:\GW10\PolicyCenter\modules\configuration\config\resources\productmodel\products\Manual\Manual.xml`
- `WorkersComp`: `C:\GW10\PolicyCenter\modules\configuration\config\resources\productmodel\products\WorkersComp\WorkersComp.xml`
- `WC7WorkersComp`: `C:\GW10\PolicyCenter\modules\configuration\config\resources\productmodel\products\WC7WorkersComp\WC7WorkersComp.xml`

### Installed Policy Line Patterns
- `PersonalAutoLine`: `C:\GW10\PolicyCenter\modules\configuration\config\resources\productmodel\policylinepatterns\PersonalAutoLine\PersonalAutoLine.xml`
- `CPLine`: `C:\GW10\PolicyCenter\modules\configuration\config\resources\productmodel\policylinepatterns\CPLine\CPLine.xml`
- `BusinessAutoLine`: `C:\GW10\PolicyCenter\modules\configuration\config\resources\productmodel\policylinepatterns\BusinessAutoLine\BusinessAutoLine.xml`
- `BOPLine`: `C:\GW10\PolicyCenter\modules\configuration\config\resources\productmodel\policylinepatterns\BOPLine\BOPLine.xml`
- `GLLine`: `C:\GW10\PolicyCenter\modules\configuration\config\resources\productmodel\policylinepatterns\GLLine\GLLine.xml`
- `HOPLine`: `C:\GW10\PolicyCenter\modules\configuration\config\resources\productmodel\policylinepatterns\HOPLine\HOPLine.xml`
- `IMLine`: `C:\GW10\PolicyCenter\modules\configuration\config\resources\productmodel\policylinepatterns\IMLine\IMLine.xml`
- `ManualLine`: `C:\GW10\PolicyCenter\modules\configuration\config\resources\productmodel\policylinepatterns\ManualLine\ManualLine.xml`
- `WorkersCompLine`: `C:\GW10\PolicyCenter\modules\configuration\config\resources\productmodel\policylinepatterns\WorkersCompLine\WorkersCompLine.xml`
- `WC7Line`: `C:\GW10\PolicyCenter\modules\configuration\config\resources\productmodel\policylinepatterns\WC7Line\WC7Line.xml`

---

## 6. Sample & Demo Data Source Paths

### PolicyCenter Sample Data Files
- `C:\GW10\PolicyCenter\modules\configuration\sampledata\source\sample_data.xml`
- `C:\GW10\PolicyCenter\modules\configuration\config\sampledata\vendorservicetree.xml`
- `C:\GW10\PolicyCenter\modules\configuration\config\import\source\system_data.xml`
- `C:\GW10\PolicyCenter\modules\configuration\config\content\ratebooks\WC7_RTM_Demo_Rating-v1.xml`
- `C:\GW10\PolicyCenter\modules\configuration\config\content\ratebooks\WC7_RTM_Demo_Rating-v2.xml`
- `C:\GW10\PolicyCenter\modules\configuration\gsrc\gw\sampledata\small\SmallSampleAccountData.gs`
- `C:\GW10\PolicyCenter\modules\configuration\gsrc\gw\sampledata\small\SmallSamplePolicyData.gs`
- `C:\GW10\PolicyCenter\modules\configuration\gsrc\gw\sampledata\tiny\TinySampleCommunityData.gs`
- `C:\GW10\PolicyCenter\modules\configuration\gsrc\gw\sampledata\large\LargeSamplePolicyData.gs`
- `C:\GW10\PolicyCenter\modules\configuration\gsrc\gw\sampledata\GenerateCommercialPropertyPolicies.gs`

### ClaimCenter Sample Data Files
- `C:\GW10\ClaimCenter\modules\configuration\gsrc\gw\sampledata\SamplePersonalAutoClaims.gs`
- `C:\GW10\ClaimCenter\modules\configuration\gsrc\gw\sampledata\SampleCommercialAutoClaims.gs`
- `C:\GW10\ClaimCenter\modules\configuration\gsrc\gw\sampledata\SampleCommercialPropertyClaims.gs`
- `C:\GW10\ClaimCenter\modules\configuration\gsrc\gw\sampledata\SampleGeneralLiabilityClaims.gs`
- `C:\GW10\ClaimCenter\modules\configuration\gsrc\gw\sampledata\SampleWorkersCompClaims.gs`
- `C:\GW10\ClaimCenter\modules\configuration\gsrc\gw\sampledata\SampleHOPClaimWithHO2Policy.gs`
- `C:\GW10\ClaimCenter\modules\configuration\gsrc\gw\sampledata\SampleCatastrophes.gs`
- `C:\GW10\ClaimCenter\modules\configuration\gsrc\gw\sampledata\SampleContacts.gs`
- `C:\GW10\ClaimCenter\modules\configuration\config\sampledata\vendorservicetree.xml`
- `C:\GW10\ClaimCenter\modules\configuration\config\sampledata\vendorservicedetails.xml`
- `C:\GW10\ClaimCenter\modules\configuration\config\sampledata\servicerequestmetriclimits.xml`
- `C:\GW10\ClaimCenter\modules\configuration\config\import\source\system_data.xml`
- `C:\GW10\ClaimCenter\modules\configuration\config\import\gen\activity-patterns.csv`
- `C:\GW10\ClaimCenter\modules\configuration\config\import\gen\authority-limits.csv`
