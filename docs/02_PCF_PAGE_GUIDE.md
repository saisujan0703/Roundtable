# Guidewire PolicyCenter PCF Page Guide

> **Target Codebase**: Guidewire PolicyCenter 10.2.1 (`project-version=10.2.1.1711`, Platform `10.201.1`, Gosu `1.14.26`)  
> **Source Directory**: `C:\GW10\PolicyCenter\modules\configuration`  
> **Generated Documentation**: `C:\Users\Student\Documents\roundtable\docs\02_PCF_PAGE_GUIDE.md`

---

## 1. Overview of PCF (Page Configuration Format) in PolicyCenter 10

PolicyCenter's UI is declaratively defined in XML files called **PCF** files, located under:
`modules/configuration/config/web/pcf/`

All PCF files validate against the central XML Schema:
`modules/pcf.xsd` (referenced relatively, e.g. `../../../../../pcf.xsd`).

### Key PCF Element Types
* **`<Page>`**: Top-level page accessible via URL/TabBar, containing entry points, variables, and screens.
* **`<Screen>`**: Container for the page body, providing toolbars, alerts, and panels.
* **`<DetailViewPanel>` (`DV`)**: Form panel organizing inputs into columns.
* **`<ListViewPanel>` (`LV`)**: Table panel iterating over an array or query result using `<RowIterator>`.
* **`<Toolbar>` / `<ToolbarButton>`**: Action controls at the top of a page, screen, or panel.
* **`<InputSet>` / `<PanelRef>`**: Modular, reusable sub-components.

---

## 2. Real Existing Patterns in the Codebase

### Real Toolbar Buttons with Gosu Actions
In PolicyCenter, buttons use the `action` attribute to run arbitrary Gosu statements.

#### Example 1: `ActivityDetailToolbarButtonSet.approval.pcf`
Location: `modules/configuration/config/web/pcf/activity/ActivityDetailToolbarButtonSet.approval.pcf` (Lines 22–33)
```xml
<ToolbarButton
  action="gw.api.web.activity.ActivityUtil.approveActivity(activity, note); gw.api.web.workspace.WorkspaceUtil.closeWorksheetIfActiveAndRefreshTop(CurrentLocation)"
  hideIfReadOnly="true"
  id="ActivityDetailToolbarButtons_ApproveButton"
  label="DisplayKey.get(&quot;Web.ActivityDetail.Button.Approve&quot;)"
  visible="perm.Activity.approve(activity) and not activity.Approved"/>

<ToolbarButton
  action="gw.api.web.activity.ActivityUtil.rejectActivity(activity, note); gw.api.web.workspace.WorkspaceUtil.closeWorksheetIfActiveAndRefreshTop(CurrentLocation)"
  hideIfReadOnly="true"
  id="ActivityDetailToolbarButtons_RejectButton"
  label="DisplayKey.get(&quot;Web.ActivityDetail.Button.Decline&quot;)"
  visible="perm.Activity.approve(activity) and not activity.Approved"/>
```

#### Example 2: `StatusTransitionToolbarButtonSet.pcf`
Location: `modules/configuration/config/web/pcf/bizrules/StatusTransitionToolbarButtonSet.pcf` (Lines 78–85)
```xml
<ToolbarButton
  action="stateHolder.changeHeadVersionStatusInNewBundle(RuleStatus.TC_APPROVED)"
  available="!stateHolder.ImportInProgress"
  hideIfEditable="true"
  id="PromoteToApproved"
  label="DisplayKey.get(&quot;BizRules.StatusTransitionToolbarButtonSet.PromoteToApproved&quot;)"
  tooltip="DisplayKey.get('BizRules.StatusTransitionToolbarButtonSet.PromoteToApprovedTooltip')"
  visible="stateHolder.LatestVersionSelected and stateHolder.SelectedVersion.Status == RuleStatus.TC_STAGED and gw.bizrules.pcf.RulePermissionUIHelper.canApproveRule(stateHolder.getSelectedVersion())"/>
```

#### Example 3: Embedded Gosu `<Code>` in PCFs
Location: `modules/configuration/config/web/pcf/tools/apd/APDGenerateProductToolbarButtonSet.pcf` (Lines 26–31)
```xml
<Code><![CDATA[
  function commitAsNeeded() {
    if (CurrentLocation.isInEditMode()) {
      CurrentLocation.commit()
      CurrentLocation.startEditing()
    }
  }
]]></Code>
```

### Real Form Inputs from `ActivityDetailDV.approval.pcf`
Location: `modules/configuration/config/web/pcf/activity/ActivityDetailDV.approval.pcf` (Lines 18–46)
```xml
<TextInput
  editable="true"
  id="Subject"
  label="DisplayKey.get(&quot;Web.ActivityDetail.Subject&quot;)"
  required="true"
  value="activity.Subject"/>
<TextAreaInput
  editable="true"
  id="Description"
  label="DisplayKey.get(&quot;Web.ActivityDetail.Description&quot;)"
  numRows="3"
  value="activity.Description"/>
<TypeKeyInput
  editable="true"
  id="Priority"
  label="DisplayKey.get(&quot;Web.ActivityDetail.Priority&quot;)"
  value="activity.Priority"
  valueType="typekey.Priority"/>
<DateInput
  editable="true"
  id="TargetDate"
  label="DisplayKey.get(&quot;Web.ActivityDetail.TargetDate&quot;)"
  value="activity.TargetDate"/>
```

---

## 3. Step-by-Step: Building the Roundtable Brief UI

We will build two PCF pages:
1. `RoundtableBriefListPage.pcf`: Table listing all generated briefs with approval badges.
2. `RoundtableBriefDetailPage.pcf`: Full detail view showing evidence, citations, 5 approval statuses, and action buttons.

### Step 3.1: Create UI Helper Gosu Class
PolicyCenter best practice is to place UI button logic inside a helper class under `modules/configuration/gsrc/`:

**File Target**: `modules/configuration/gsrc/roundtable/web/RoundtableUIHelper.gs`
```gosu
package roundtable.web

uses entity.RoundtableBrief
uses pcf.RoundtableBriefDetailPage
uses pcf.RoundtableBriefListPage
uses pcf.APDProductDefinition
uses roundtable.apd.RoundtableToAPDService

@Export
class RoundtableUIHelper {

  /**
   * Updates a specific team's approval status in a new database transaction bundle.
   * Can be invoked whether the page is in read-only or edit mode.
   */
  public static function updateTeamStatus(brief : RoundtableBrief, teamName : String, status : RoundtableApprovalStatus) {
    gw.transaction.Transaction.runWithNewBundle(\bundle -> {
      var localBrief = bundle.add(brief)
      switch (teamName.toLowerCase()) {
        case "claims":
          localBrief.ClaimsStatus = status
          break
        case "actuarial":
          localBrief.ActuarialStatus = status
          break
        case "underwriting":
          localBrief.UnderwritingStatus = status
          break
        case "marketing":
          localBrief.MarketingStatus = status
          break
        case "compliance":
          localBrief.ComplianceStatus = status
          break
      }
      
      // If all 5 teams have approved, record the ApprovedDate
      if (localBrief.ClaimsStatus == TC_APPROVED
          and localBrief.ActuarialStatus == TC_APPROVED
          and localBrief.UnderwritingStatus == TC_APPROVED
          and localBrief.MarketingStatus == TC_APPROVED
          and localBrief.ComplianceStatus == TC_APPROVED
          and localBrief.ApprovedDate == null) {
        localBrief.ApprovedDate = java.util.Date.CurrentDate
      }
    })
  }

  /**
   * Pushes an approved brief into APD as a new APDProduct and navigates to the APD designer.
   */
  public static function pushToAPD(brief : RoundtableBrief) {
    var apdProduct = RoundtableToAPDService.createApdProductFromBrief(brief)
    APDProductDefinition.go(apdProduct)
  }
}
```

---

### Step 3.2: Create the List Page `RoundtableBriefListPage.pcf`
**File Target**: `modules/configuration/config/web/pcf/roundtable/RoundtableBriefListPage.pcf`

```xml
<?xml version="1.0"?>
<PCF
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="../../../../../pcf.xsd">
  <Page
    canEdit="false"
    canVisit="perm.System.viewpolicyfile or perm.System.viewaccount"
    id="RoundtableBriefListPage"
    title="&quot;Roundtable Product Decision Briefs&quot;">
    <Variable
      initialValue="gw.api.database.Query.make(RoundtableBrief).select()"
      name="allBriefs"
      recalculateOnRefresh="true"
      type="gw.api.database.IQueryBeanResult&lt;RoundtableBrief&gt;"/>
    <Screen
      id="RoundtableBriefListScreen">
      <Toolbar>
        <ToolbarButton
          action="RoundtableBriefDetailPage.go(new RoundtableBrief())"
          id="NewBriefButton"
          label="&quot;New Brief&quot;"/>
      </Toolbar>
      <ListViewPanel
        id="RoundtableBriefLV">
        <RowIterator
          editable="false"
          elementName="brief"
          value="allBriefs"
          valueType="gw.api.database.IQueryBeanResult&lt;RoundtableBrief&gt;">
          <Row>
            <TextCell
              action="RoundtableBriefDetailPage.go(brief)"
              id="TitleCell"
              label="&quot;Brief Title&quot;"
              value="brief.Title"/>
            <TextCell
              id="TargetLineCell"
              label="&quot;Target Line&quot;"
              value="brief.TargetLineCode"/>
            <DateCell
              dateFormat="short"
              id="CreatedDateCell"
              label="&quot;Created Date&quot;"
              value="brief.CreatedDate"/>
            <TypeKeyCell
              id="ClaimsStatusCell"
              label="&quot;Claims&quot;"
              value="brief.ClaimsStatus"
              valueType="typekey.RoundtableApprovalStatus"/>
            <TypeKeyCell
              id="ActuarialStatusCell"
              label="&quot;Actuarial&quot;"
              value="brief.ActuarialStatus"
              valueType="typekey.RoundtableApprovalStatus"/>
            <TypeKeyCell
              id="UWStatusCell"
              label="&quot;Underwriting&quot;"
              value="brief.UnderwritingStatus"
              valueType="typekey.RoundtableApprovalStatus"/>
            <TypeKeyCell
              id="MarketingStatusCell"
              label="&quot;Marketing&quot;"
              value="brief.MarketingStatus"
              valueType="typekey.RoundtableApprovalStatus"/>
            <TypeKeyCell
              id="ComplianceStatusCell"
              label="&quot;Compliance&quot;"
              value="brief.ComplianceStatus"
              valueType="typekey.RoundtableApprovalStatus"/>
            <BooleanRadioCell
              id="PushedToApdCell"
              label="&quot;In APD&quot;"
              value="brief.PushedToApd"/>
          </Row>
        </RowIterator>
      </ListViewPanel>
    </Screen>
  </Page>
</PCF>
```

---

### Step 3.3: Create Detail View Panel `RoundtableBriefDV.pcf`
**File Target**: `modules/configuration/config/web/pcf/roundtable/RoundtableBriefDV.pcf`

```xml
<?xml version="1.0"?>
<PCF
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="../../../../../pcf.xsd">
  <DetailViewPanel
    id="RoundtableBriefDV">
    <Require
      name="brief"
      type="RoundtableBrief"/>
    <InputColumn>
      <Label
        label="&quot;Product Concept Overview&quot;"/>
      <TextInput
        editable="true"
        id="TitleInput"
        label="&quot;Title&quot;"
        required="true"
        value="brief.Title"/>
      <TextInput
        editable="true"
        id="TargetLineInput"
        label="&quot;Target Line Code&quot;"
        value="brief.TargetLineCode"/>
      <TextAreaInput
        editable="true"
        id="ProductSummaryInput"
        label="&quot;Product Summary&quot;"
        numRows="3"
        value="brief.ProductSummary"/>
      <DateInput
        editable="true"
        id="CreatedDateInput"
        label="&quot;Date Generated&quot;"
        value="brief.CreatedDate"/>
      <DateInput
        editable="false"
        id="ApprovedDateInput"
        label="&quot;Fully Approved Date&quot;"
        value="brief.ApprovedDate"
        visible="brief.ApprovedDate != null"/>

      <Label
        label="&quot;Decision Support &amp; Evidence&quot;"/>
      <TextAreaInput
        editable="true"
        id="EvidenceTextInput"
        label="&quot;Synthesized Evidence&quot;"
        numRows="6"
        value="brief.EvidenceText"/>
      <TextAreaInput
        editable="true"
        id="CompetitorComparisonInput"
        label="&quot;Competitor Comparison&quot;"
        numRows="4"
        value="brief.CompetitorComparison"/>
      <TextAreaInput
        editable="true"
        id="DirectionalEstimatesInput"
        label="&quot;Directional Estimates&quot;"
        numRows="4"
        value="brief.DirectionalEstimates"/>
      <TextAreaInput
        editable="true"
        id="CitationsInput"
        label="&quot;Cited References&quot;"
        numRows="4"
        value="brief.Citations"/>
    </InputColumn>
    <InputColumn>
      <Label
        label="&quot;Multi-Disciplinary Approval Statuses&quot;"/>
      <TypeKeyInput
        editable="true"
        id="ClaimsStatusInput"
        label="&quot;Claims Team&quot;"
        value="brief.ClaimsStatus"
        valueType="typekey.RoundtableApprovalStatus"/>
      <TypeKeyInput
        editable="true"
        id="ActuarialStatusInput"
        label="&quot;Actuarial Team&quot;"
        value="brief.ActuarialStatus"
        valueType="typekey.RoundtableApprovalStatus"/>
      <TypeKeyInput
        editable="true"
        id="UnderwritingStatusInput"
        label="&quot;Underwriting Team&quot;"
        value="brief.UnderwritingStatus"
        valueType="typekey.RoundtableApprovalStatus"/>
      <TypeKeyInput
        editable="true"
        id="MarketingStatusInput"
        label="&quot;Marketing Team&quot;"
        value="brief.MarketingStatus"
        valueType="typekey.RoundtableApprovalStatus"/>
      <TypeKeyInput
        editable="true"
        id="ComplianceStatusInput"
        label="&quot;Compliance Team&quot;"
        value="brief.ComplianceStatus"
        valueType="typekey.RoundtableApprovalStatus"/>

      <Label
        label="&quot;Advanced Product Designer (APD) Status&quot;"/>
      <BooleanRadioInput
        editable="false"
        id="PushedToApdInput"
        label="&quot;Pushed to APD&quot;"
        value="brief.PushedToApd"/>
      <TextInput
        editable="false"
        id="ApdProductCodeInput"
        label="&quot;APD Product Code&quot;"
        value="brief.ApdProductCode"
        visible="brief.ApdProductCode != null"/>
    </InputColumn>
  </DetailViewPanel>
</PCF>
```

---

### Step 3.4: Create the Detail Page with Action Buttons `RoundtableBriefDetailPage.pcf`
**File Target**: `modules/configuration/config/web/pcf/roundtable/RoundtableBriefDetailPage.pcf`

```xml
<?xml version="1.0"?>
<PCF
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="../../../../../pcf.xsd">
  <Page
    canEdit="true"
    canVisit="true"
    id="RoundtableBriefDetailPage"
    parent="RoundtableBriefListPage()"
    showUpLink="true"
    title="&quot;Brief: &quot; + (brief.Title ?: &quot;New Brief&quot;)">
    <LocationEntryPoint
      signature="RoundtableBriefDetailPage(brief : RoundtableBrief)"/>
    <Variable
      name="brief"
      type="RoundtableBrief"/>
    <Variable
      initialValue="brief.ClaimsStatus == TC_APPROVED and brief.ActuarialStatus == TC_APPROVED and brief.UnderwritingStatus == TC_APPROVED and brief.MarketingStatus == TC_APPROVED and brief.ComplianceStatus == TC_APPROVED"
      name="isFullyApproved"
      recalculateOnRefresh="true"
      type="Boolean"/>
    <Screen
      id="RoundtableBriefDetailScreen">
      <Toolbar>
        <EditButtons/>
        
        <!-- Quick Action Buttons for Approving/Rejecting as Underwriting -->
        <ToolbarButton
          action="roundtable.web.RoundtableUIHelper.updateTeamStatus(brief, &quot;underwriting&quot;, TC_APPROVED)"
          id="ApproveUWButton"
          label="&quot;Approve (UW)&quot;"
          visible="brief.UnderwritingStatus != TC_APPROVED"/>
        <ToolbarButton
          action="roundtable.web.RoundtableUIHelper.updateTeamStatus(brief, &quot;underwriting&quot;, TC_REJECTED)"
          id="RejectUWButton"
          label="&quot;Reject (UW)&quot;"
          visible="brief.UnderwritingStatus != TC_REJECTED"/>

        <!-- Downstream Push to APD Action -->
        <ToolbarButton
          action="roundtable.web.RoundtableUIHelper.pushToAPD(brief)"
          confirmMessage="&quot;This will create a new product definition in Advanced Product Designer. Proceed?&quot;"
          id="PushToAPDButton"
          label="&quot;Push to APD Product Model&quot;"
          visible="isFullyApproved and not brief.PushedToApd"/>
      </Toolbar>
      
      <!-- Informational banner when fully approved -->
      <AlertBar
        id="ApprovedBanner"
        label="&quot;This brief has received all 5 team approvals and is ready for APD configuration.&quot;"
        visible="isFullyApproved and not brief.PushedToApd"/>
        
      <PanelRef
        def="RoundtableBriefDV(brief)"/>
    </Screen>
  </Page>
</PCF>
```

---

## 4. Hooking the Page into the Main Menu (`TabBar.pcf`)

To make the new page accessible from the top navigation bar in PolicyCenter:
File: `modules/configuration/config/web/pcf/TabBar.pcf`

Inside `<TabBar>`:
```xml
<Tab
  action="RoundtableBriefListPage.go()"
  id="RoundtableTab"
  label="&quot;Roundtable Briefs&quot;"
  shortcut="R"/>
```

---

## 5. Verification Rules for PCF Syntax

* **No arbitrary XML tags**: Every PCF element must match `modules/pcf.xsd`.
* **String values in PCF**: Must be quoted string literals (`"..."`) or Gosu expressions returning `String`.
* **Escaping quotes in XML attributes**: Inside XML attribute values, double quotes must be written as `&quot;` (e.g. `label="DisplayKey.get(&quot;Button.Save&quot;)"`).
* **Bundle persistence**: If a button updates an entity outside of the page's edit session (or while read-only), always wrap the change in `gw.transaction.Transaction.runWithNewBundle(\bundle -> { ... })`.
