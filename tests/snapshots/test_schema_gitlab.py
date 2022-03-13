from enum import Enum
from typing import Any, ClassVar, List, Optional, TypedDict, Union


## Scalars

AlertManagementHttpIntegrationID = Any

AnalyticsDevopsAdoptionEnabledNamespaceID = Any

AppSecFuzzingCoverageCorpusID = Any

AuditEventsExternalAuditEventDestinationID = Any

AwardableID = Any

BigInt = int

BoardID = int

BoardsEpicBoardID = Any

BoardsEpicListID = Any

CiBuildID = Any

CiPipelineID = Any

CiRunnerID = Any

ClustersAgentID = Any

ClustersAgentTokenID = Any

ClustersClusterID = Any

ComplianceManagementFrameworkID = Any

ContainerRepositoryID = Any

CustomEmojiID = Any

CustomerRelationsContactID = Any

CustomerRelationsOrganizationID = Any

DastProfileID = Any

DastProfileScheduleID = Any

DastScannerProfileID = Any

DastSiteProfileID = Any

DastSiteTokenID = Any

DastSiteValidationID = Any

Date = Any

DependencyProxyManifestID = Any

DesignManagementDesignAtVersionID = Any

DesignManagementDesignID = Any

DesignManagementVersionID = Any

DiffNoteID = Any

DiscussionID = Any

Duration = ClassVar['DesignFields']

EnvironmentID = Any

EpicID = Any

EpicTreeSortingID = Any

GitlabErrorTrackingDetailedErrorID = Any

GlobalID = Any

GroupID = Any

ISO8601Date = Any

IncidentManagementEscalationPolicyID = Any

IncidentManagementEscalationRuleID = Any

IncidentManagementOncallParticipantID = Any

IncidentManagementOncallRotationID = Any

IncidentManagementTimelineEventID = Any

IntegrationsPrometheusID = Any

IssuableID = Any

IssueID = Any

IterationID = Any

IterationsCadenceID = Any

JSON = Any

JobID = Any

JsonString = Any

LabelID = Any

ListID = Any

MergeRequestID = Any

MetricsDashboardAnnotationID = Any

MilestoneID = Any

NamespaceID = Any

NoteID = Any

NoteableID = Any

PackagesConanFileMetadatumID = Any

PackagesConanMetadatumID = Any

PackagesDependencyID = Any

PackagesDependencyLinkID = Any

PackagesMavenMetadatumID = Any

PackagesNugetDependencyLinkMetadatumID = Any

PackagesNugetMetadatumID = Any

PackagesPackageFileID = Any

PackagesPackageID = Any

PackagesPypiMetadatumID = Any

PathLockID = Any

PayloadAlertFieldPathSegment = Any

ProjectID = Any

ReleasesLinkID = Any

SecurityTrainingProviderID = Any

SnippetID = Any

TerraformStateID = Any

Time = str

TodoID = Any

TodoableID = Any

UntrustedRegexp = Any

Upload = Any

UserID = Any

UsersSavedReplyID = Any

VulnerabilitiesExternalIssueLinkID = Any

VulnerabilitiesFindingID = Any

VulnerabilitiesScannerID = Any

VulnerabilityID = Any

WorkItemID = Any

WorkItemsTypeID = Any

## Union Types

DependencyLinkMetadata = ClassVar['NugetDependencyLinkMetadata']

Issuable = Union['Epic', 'Issue', 'MergeRequest', 'WorkItemscalarIssuableID']

JobNeedUnion = Union['CiBuildNeed', 'CiJob']

NoteableType = Union['Design', 'Issue', 'MergeRequest']

PackageMetadata = Union['ComposerMetadata', 'ConanMetadata', 'MavenMetadata', 'NugetMetadata', 'PypiMetadata']

VulnerabilityDetail = Union['VulnerabilityDetailBase', 'VulnerabilityDetailBoolean', 'VulnerabilityDetailCode', 'VulnerabilityDetailCommit', 'VulnerabilityDetailDiff', 'VulnerabilityDetailFileLocation', 'VulnerabilityDetailInt', 'VulnerabilityDetailList', 'VulnerabilityDetailMarkdown', 'VulnerabilityDetailModuleLocation', 'VulnerabilityDetailTable', 'VulnerabilityDetailText', 'VulnerabilityDetailUrl']

VulnerabilityLocation = Union['VulnerabilityLocationClusterImageScanning', 'VulnerabilityLocationContainerScanning', 'VulnerabilityLocationCoverageFuzzing', 'VulnerabilityLocationDast', 'VulnerabilityLocationDependencyScanning', 'VulnerabilityLocationGeneric', 'VulnerabilityLocationSast', 'VulnerabilityLocationSecretDetection']

AlertManagementIntegration = TypedDict('AlertManagementIntegration', {
	'active': Optional[bool],
	'apiUrl': Optional[str],
	'id': str,
	'name': Optional[str],
	'token': Optional[str],
	'type': 'AlertManagementIntegrationType',
	'url': Optional[str],
})


CurrentUserTodos = TypedDict('CurrentUserTodos', {
	'currentUserTodos': 'TodoConnection',
})


DesignFields = TypedDict('DesignFields', {
	'diffRefs': 'DiffRefs',
	'event': 'DesignVersionEvent',
	'filename': str,
	'fullPath': str,
	'id': str,
	'image': str,
	'imageV432x230': Optional[str],
	'issue': 'Issue',
	'notesCount': int,
	'project': 'Project',
})


Entry = TypedDict('Entry', {
	'flatPath': str,
	'id': str,
	'name': str,
	'path': str,
	'sha': str,
	'type': 'EntryType',
})


Eventable = TypedDict('Eventable', {
	'events': Optional['EventConnection'],
})


MemberInterface = TypedDict('MemberInterface', {
	'accessLevel': Optional['AccessLevel'],
	'createdAt': Optional['Time'],
	'createdBy': Optional['UserCore'],
	'expiresAt': Optional['Time'],
	'id': str,
	'mergeRequestInteraction': Optional['UserMergeRequestInteraction'],
	'updatedAt': Optional['Time'],
	'user': Optional['UserCore'],
})


NoteableInterface = TypedDict('NoteableInterface', {
	'discussions': 'DiscussionConnection',
	'notes': 'NoteConnection',
})


OrchestrationPolicy = TypedDict('OrchestrationPolicy', {
	'description': str,
	'enabled': bool,
	'name': str,
	'updatedAt': 'Time',
	'yaml': str,
})


PackageFileMetadata = TypedDict('PackageFileMetadata', {
	'createdAt': 'Time',
	'updatedAt': 'Time',
})


ResolvableInterface = TypedDict('ResolvableInterface', {
	'resolvable': bool,
	'resolved': bool,
	'resolvedAt': Optional['Time'],
	'resolvedBy': Optional['UserCore'],
})


Service = TypedDict('Service', {
	'active': Optional[bool],
	'serviceType': Optional['ServiceType'],
	'type': Optional[str],
})


TimeboxReportInterface = TypedDict('TimeboxReportInterface', {
	'report': Optional['TimeboxReport'],
})


Todoable = TypedDict('Todoable', {
	'webUrl': Optional[str],
})


User = TypedDict('User', {
	'assignedMergeRequests': Optional['MergeRequestConnection'],
	'authoredMergeRequests': Optional['MergeRequestConnection'],
	'avatarUrl': Optional[str],
	'bot': bool,
	'callouts': Optional['UserCalloutConnection'],
	'email': Optional[str],
	'gitpodEnabled': Optional[bool],
	'groupCount': Optional[int],
	'groupMemberships': Optional['GroupMemberConnection'],
	'groups': Optional['GroupConnection'],
	'id': str,
	'location': Optional[str],
	'name': str,
	'namespace': Optional['Namespace'],
	'preferencesGitpodPath': Optional[str],
	'profileEnableGitpodPath': Optional[str],
	'projectMemberships': Optional['ProjectMemberConnection'],
	'publicEmail': Optional[str],
	'reviewRequestedMergeRequests': Optional['MergeRequestConnection'],
	'savedReplies': Optional['SavedReplyConnection'],
	'snippets': Optional['SnippetConnection'],
	'starredProjects': Optional['ProjectConnection'],
	'state': 'UserState',
	'status': Optional['UserStatus'],
	'timelogs': Optional['TimelogConnection'],
	'todos': Optional['TodoConnection'],
	'userPermissions': 'UserPermissions',
	'username': str,
	'webPath': str,
	'webUrl': str,
})


AccessLevelEnum = Enum('AccessLevelEnum', 'NO_ACCESS MINIMAL_ACCESS GUEST REPORTER DEVELOPER MAINTAINER OWNER')


AgentTokenStatus = Enum('AgentTokenStatus', 'ACTIVE REVOKED')


AlertManagementAlertSort = Enum('AlertManagementAlertSort', 'updated_desc updated_asc created_desc created_asc UPDATED_DESC UPDATED_ASC CREATED_DESC CREATED_ASC STARTED_AT_ASC STARTED_AT_DESC ENDED_AT_ASC ENDED_AT_DESC CREATED_TIME_ASC CREATED_TIME_DESC UPDATED_TIME_ASC UPDATED_TIME_DESC EVENT_COUNT_ASC EVENT_COUNT_DESC SEVERITY_ASC SEVERITY_DESC STATUS_ASC STATUS_DESC')


AlertManagementDomainFilter = Enum('AlertManagementDomainFilter', 'operations threat_monitoring')


AlertManagementIntegrationType = Enum('AlertManagementIntegrationType', 'PROMETHEUS HTTP')


AlertManagementPayloadAlertFieldName = Enum('AlertManagementPayloadAlertFieldName', 'TITLE DESCRIPTION START_TIME END_TIME SERVICE MONITORING_TOOL HOSTS SEVERITY FINGERPRINT GITLAB_ENVIRONMENT_NAME')


AlertManagementPayloadAlertFieldType = Enum('AlertManagementPayloadAlertFieldType', 'ARRAY DATETIME STRING')


AlertManagementSeverity = Enum('AlertManagementSeverity', 'CRITICAL HIGH MEDIUM LOW INFO UNKNOWN')


AlertManagementStatus = Enum('AlertManagementStatus', 'TRIGGERED ACKNOWLEDGED RESOLVED IGNORED')


ApiFuzzingScanMode = Enum('ApiFuzzingScanMode', 'HAR OPENAPI POSTMAN')


ApprovalRuleType = Enum('ApprovalRuleType', 'REGULAR CODE_OWNER REPORT_APPROVER ANY_APPROVER')


AssigneeWildcardId = Enum('AssigneeWildcardId', 'NONE ANY')


AvailabilityEnum = Enum('AvailabilityEnum', 'NOT_SET BUSY')


BlobViewersType = Enum('BlobViewersType', 'rich simple auxiliary')


CiConfigStatus = Enum('CiConfigStatus', 'VALID INVALID')


CiJobStatus = Enum('CiJobStatus', 'CREATED WAITING_FOR_RESOURCE PREPARING PENDING RUNNING SUCCESS FAILED CANCELED SKIPPED MANUAL SCHEDULED')


CiRunnerAccessLevel = Enum('CiRunnerAccessLevel', 'NOT_PROTECTED REF_PROTECTED')


CiRunnerSort = Enum('CiRunnerSort', 'CONTACTED_ASC CONTACTED_DESC CREATED_ASC CREATED_DESC TOKEN_EXPIRES_AT_ASC TOKEN_EXPIRES_AT_DESC')


CiRunnerStatus = Enum('CiRunnerStatus', 'ACTIVE PAUSED ONLINE OFFLINE STALE NOT_CONNECTED NEVER_CONTACTED')


CiRunnerType = Enum('CiRunnerType', 'INSTANCE_TYPE GROUP_TYPE PROJECT_TYPE')


CodeQualityDegradationSeverity = Enum('CodeQualityDegradationSeverity', 'BLOCKER CRITICAL MAJOR MINOR INFO UNKNOWN')


CommitActionMode = Enum('CommitActionMode', 'CREATE DELETE MOVE UPDATE CHMOD')


CommitEncoding = Enum('CommitEncoding', 'TEXT BASE64')


ComplianceViolationReason = Enum('ComplianceViolationReason', 'APPROVED_BY_MERGE_REQUEST_AUTHOR APPROVED_BY_COMMITTER APPROVED_BY_INSUFFICIENT_USERS')


ComplianceViolationSeverity = Enum('ComplianceViolationSeverity', 'INFO LOW MEDIUM HIGH CRITICAL')


ComplianceViolationSort = Enum('ComplianceViolationSort', 'SEVERITY_LEVEL_DESC SEVERITY_LEVEL_ASC VIOLATION_REASON_DESC VIOLATION_REASON_ASC MERGE_REQUEST_TITLE_DESC MERGE_REQUEST_TITLE_ASC MERGED_AT_DESC MERGED_AT_ASC')


ConanMetadatumFileTypeEnum = Enum('ConanMetadatumFileTypeEnum', 'RECIPE_FILE PACKAGE_FILE')


ContainerExpirationPolicyCadenceEnum = Enum('ContainerExpirationPolicyCadenceEnum', 'EVERY_DAY EVERY_WEEK EVERY_TWO_WEEKS EVERY_MONTH EVERY_THREE_MONTHS')


ContainerExpirationPolicyKeepEnum = Enum('ContainerExpirationPolicyKeepEnum', 'ONE_TAG FIVE_TAGS TEN_TAGS TWENTY_FIVE_TAGS FIFTY_TAGS ONE_HUNDRED_TAGS')


ContainerExpirationPolicyOlderThanEnum = Enum('ContainerExpirationPolicyOlderThanEnum', 'SEVEN_DAYS FOURTEEN_DAYS THIRTY_DAYS SIXTY_DAYS NINETY_DAYS')


ContainerRepositoryCleanupStatus = Enum('ContainerRepositoryCleanupStatus', 'UNSCHEDULED SCHEDULED UNFINISHED ONGOING')


ContainerRepositorySort = Enum('ContainerRepositorySort', 'updated_desc updated_asc created_desc created_asc UPDATED_DESC UPDATED_ASC CREATED_DESC CREATED_ASC NAME_ASC NAME_DESC')


ContainerRepositoryStatus = Enum('ContainerRepositoryStatus', 'DELETE_SCHEDULED DELETE_FAILED')


ContainerRepositoryTagSort = Enum('ContainerRepositoryTagSort', 'NAME_ASC NAME_DESC')


DastProfileCadenceUnit = Enum('DastProfileCadenceUnit', 'DAY WEEK MONTH YEAR')


DastScanMethodType = Enum('DastScanMethodType', 'WEBSITE OPENAPI HAR POSTMAN_COLLECTION')


DastScanTypeEnum = Enum('DastScanTypeEnum', 'PASSIVE ACTIVE')


DastSiteProfileValidationStatusEnum = Enum('DastSiteProfileValidationStatusEnum', 'NONE PENDING_VALIDATION INPROGRESS_VALIDATION PASSED_VALIDATION FAILED_VALIDATION')


DastSiteValidationStatusEnum = Enum('DastSiteValidationStatusEnum', 'PENDING_VALIDATION INPROGRESS_VALIDATION PASSED_VALIDATION FAILED_VALIDATION')


DastSiteValidationStrategyEnum = Enum('DastSiteValidationStrategyEnum', 'TEXT_FILE HEADER META_TAG')


DastTargetTypeEnum = Enum('DastTargetTypeEnum', 'WEBSITE API')


DataVisualizationColorEnum = Enum('DataVisualizationColorEnum', 'BLUE ORANGE AQUA GREEN MAGENTA')


DataVisualizationWeightEnum = Enum('DataVisualizationWeightEnum', 'WEIGHT_50 WEIGHT_100 WEIGHT_200 WEIGHT_300 WEIGHT_400 WEIGHT_500 WEIGHT_600 WEIGHT_700 WEIGHT_800 WEIGHT_900 WEIGHT_950')


DeploymentTier = Enum('DeploymentTier', 'PRODUCTION STAGING TESTING DEVELOPMENT OTHER')


DesignCollectionCopyState = Enum('DesignCollectionCopyState', 'READY IN_PROGRESS ERROR')


DesignVersionEvent = Enum('DesignVersionEvent', 'NONE CREATION MODIFICATION DELETION')


DiffPositionType = Enum('DiffPositionType', 'text image')


DoraMetricBucketingInterval = Enum('DoraMetricBucketingInterval', 'ALL MONTHLY DAILY')


DoraMetricType = Enum('DoraMetricType', 'DEPLOYMENT_FREQUENCY LEAD_TIME_FOR_CHANGES TIME_TO_RESTORE_SERVICE')


EntryType = Enum('EntryType', 'tree blob commit')


EpicSort = Enum('EpicSort', 'start_date_desc start_date_asc end_date_desc end_date_asc START_DATE_DESC START_DATE_ASC END_DATE_DESC END_DATE_ASC TITLE_DESC TITLE_ASC CREATED_AT_ASC CREATED_AT_DESC UPDATED_AT_ASC UPDATED_AT_DESC')


EpicState = Enum('EpicState', 'all opened closed')


EpicStateEvent = Enum('EpicStateEvent', 'REOPEN CLOSE')


EpicWildcardId = Enum('EpicWildcardId', 'NONE ANY')


EscalationRuleStatus = Enum('EscalationRuleStatus', 'ACKNOWLEDGED RESOLVED')


EventAction = Enum('EventAction', 'CREATED UPDATED CLOSED REOPENED PUSHED COMMENTED MERGED JOINED LEFT DESTROYED EXPIRED APPROVED')


GroupMemberRelation = Enum('GroupMemberRelation', 'DIRECT INHERITED DESCENDANTS SHARED_FROM_GROUPS')


GroupPermission = Enum('GroupPermission', 'CREATE_PROJECTS')


HealthStatus = Enum('HealthStatus', 'onTrack needsAttention atRisk')


IssuableSearchableField = Enum('IssuableSearchableField', 'TITLE DESCRIPTION')


IssuableSeverity = Enum('IssuableSeverity', 'UNKNOWN LOW MEDIUM HIGH CRITICAL')


IssuableState = Enum('IssuableState', 'opened closed locked all')


IssueCreationIterationWildcardId = Enum('IssueCreationIterationWildcardId', 'CURRENT')


IssueEscalationStatus = Enum('IssueEscalationStatus', 'TRIGGERED ACKNOWLEDGED RESOLVED IGNORED')


IssueSort = Enum('IssueSort', 'updated_desc updated_asc created_desc created_asc UPDATED_DESC UPDATED_ASC CREATED_DESC CREATED_ASC PRIORITY_ASC PRIORITY_DESC LABEL_PRIORITY_ASC LABEL_PRIORITY_DESC MILESTONE_DUE_ASC MILESTONE_DUE_DESC DUE_DATE_ASC DUE_DATE_DESC RELATIVE_POSITION_ASC SEVERITY_ASC SEVERITY_DESC TITLE_ASC TITLE_DESC POPULARITY_ASC POPULARITY_DESC ESCALATION_STATUS_ASC ESCALATION_STATUS_DESC WEIGHT_ASC WEIGHT_DESC PUBLISHED_ASC PUBLISHED_DESC SLA_DUE_AT_ASC SLA_DUE_AT_DESC BLOCKING_ISSUES_ASC BLOCKING_ISSUES_DESC')


IssueState = Enum('IssueState', 'opened closed locked all')


IssueStateEvent = Enum('IssueStateEvent', 'REOPEN CLOSE')


IssueType = Enum('IssueType', 'ISSUE INCIDENT TEST_CASE REQUIREMENT')


IterationSearchableField = Enum('IterationSearchableField', 'TITLE CADENCE_TITLE')


IterationSort = Enum('IterationSort', 'CADENCE_AND_DUE_DATE_ASC')


IterationState = Enum('IterationState', 'upcoming started current opened closed all')


IterationWildcardId = Enum('IterationWildcardId', 'NONE ANY CURRENT')


JobArtifactFileType = Enum('JobArtifactFileType', 'ARCHIVE METADATA TRACE JUNIT METRICS METRICS_REFEREE NETWORK_REFEREE DOTENV COBERTURA CLUSTER_APPLICATIONS LSIF SAST SECRET_DETECTION DEPENDENCY_SCANNING CONTAINER_SCANNING CLUSTER_IMAGE_SCANNING DAST LICENSE_SCANNING ACCESSIBILITY CODEQUALITY PERFORMANCE BROWSER_PERFORMANCE LOAD_PERFORMANCE TERRAFORM REQUIREMENTS COVERAGE_FUZZING API_FUZZING')


ListLimitMetric = Enum('ListLimitMetric', 'all_metrics issue_count issue_weights')


MeasurementIdentifier = Enum('MeasurementIdentifier', 'PROJECTS USERS ISSUES MERGE_REQUESTS GROUPS PIPELINES PIPELINES_SUCCEEDED PIPELINES_FAILED PIPELINES_CANCELED PIPELINES_SKIPPED')


MergeRequestNewState = Enum('MergeRequestNewState', 'OPEN CLOSED')


MergeRequestReviewState = Enum('MergeRequestReviewState', 'UNREVIEWED REVIEWED ATTENTION_REQUESTED')


MergeRequestSort = Enum('MergeRequestSort', 'updated_desc updated_asc created_desc created_asc UPDATED_DESC UPDATED_ASC CREATED_DESC CREATED_ASC PRIORITY_ASC PRIORITY_DESC LABEL_PRIORITY_ASC LABEL_PRIORITY_DESC MILESTONE_DUE_ASC MILESTONE_DUE_DESC MERGED_AT_ASC MERGED_AT_DESC CLOSED_AT_ASC CLOSED_AT_DESC TITLE_ASC TITLE_DESC')


MergeRequestState = Enum('MergeRequestState', 'opened closed locked all merged')


MergeStatus = Enum('MergeStatus', 'UNCHECKED CHECKING CAN_BE_MERGED CANNOT_BE_MERGED CANNOT_BE_MERGED_RECHECK')


MergeStrategyEnum = Enum('MergeStrategyEnum', 'MERGE_TRAIN ADD_TO_MERGE_TRAIN_WHEN_PIPELINE_SUCCEEDS MERGE_WHEN_PIPELINE_SUCCEEDS')


MilestoneSort = Enum('MilestoneSort', 'updated_desc updated_asc created_desc created_asc UPDATED_DESC UPDATED_ASC CREATED_DESC CREATED_ASC DUE_DATE_ASC DUE_DATE_DESC EXPIRED_LAST_DUE_DATE_ASC EXPIRED_LAST_DUE_DATE_DESC')


MilestoneStateEnum = Enum('MilestoneStateEnum', 'active closed')


MilestoneWildcardId = Enum('MilestoneWildcardId', 'NONE ANY STARTED UPCOMING')


MoveType = Enum('MoveType', 'before after')


MutationOperationMode = Enum('MutationOperationMode', 'REPLACE APPEND REMOVE')


NamespaceProjectSort = Enum('NamespaceProjectSort', 'SIMILARITY STORAGE')


NegatedIterationWildcardId = Enum('NegatedIterationWildcardId', 'CURRENT')


NegatedMilestoneWildcardId = Enum('NegatedMilestoneWildcardId', 'STARTED UPCOMING')


NetworkPolicyKind = Enum('NetworkPolicyKind', 'CiliumNetworkPolicy NetworkPolicy')


OncallRotationUnitEnum = Enum('OncallRotationUnitEnum', 'HOURS DAYS WEEKS')


PackageDependencyType = Enum('PackageDependencyType', 'DEPENDENCIES DEV_DEPENDENCIES BUNDLE_DEPENDENCIES PEER_DEPENDENCIES')


PackageGroupSort = Enum('PackageGroupSort', 'CREATED_DESC CREATED_ASC NAME_DESC NAME_ASC VERSION_DESC VERSION_ASC TYPE_DESC TYPE_ASC PROJECT_PATH_DESC PROJECT_PATH_ASC')


PackageSort = Enum('PackageSort', 'CREATED_DESC CREATED_ASC NAME_DESC NAME_ASC VERSION_DESC VERSION_ASC TYPE_DESC TYPE_ASC')


PackageStatus = Enum('PackageStatus', 'DEFAULT HIDDEN PROCESSING ERROR PENDING_DESTRUCTION')


PackageTypeEnum = Enum('PackageTypeEnum', 'MAVEN NPM CONAN NUGET PYPI COMPOSER GENERIC GOLANG DEBIAN RUBYGEMS HELM TERRAFORM_MODULE')


PipelineConfigSourceEnum = Enum('PipelineConfigSourceEnum', 'UNKNOWN_SOURCE REPOSITORY_SOURCE AUTO_DEVOPS_SOURCE WEBIDE_SOURCE REMOTE_SOURCE EXTERNAL_PROJECT_SOURCE BRIDGE_SOURCE PARAMETER_SOURCE COMPLIANCE_SOURCE')


PipelineScopeEnum = Enum('PipelineScopeEnum', 'RUNNING PENDING FINISHED BRANCHES TAGS')


PipelineStatusEnum = Enum('PipelineStatusEnum', 'CREATED WAITING_FOR_RESOURCE PREPARING PENDING RUNNING FAILED SUCCESS CANCELED SKIPPED MANUAL SCHEDULED')


ProjectMemberRelation = Enum('ProjectMemberRelation', 'DIRECT INHERITED DESCENDANTS INVITED_GROUPS')


RegistryState = Enum('RegistryState', 'PENDING STARTED SYNCED FAILED')


ReleaseAssetLinkType = Enum('ReleaseAssetLinkType', 'OTHER RUNBOOK PACKAGE IMAGE')


ReleaseSort = Enum('ReleaseSort', 'CREATED_DESC CREATED_ASC RELEASED_AT_DESC RELEASED_AT_ASC')


ReleaseTagWildcardId = Enum('ReleaseTagWildcardId', 'NONE ANY')


RequirementState = Enum('RequirementState', 'OPENED ARCHIVED')


RequirementStatusFilter = Enum('RequirementStatusFilter', 'PASSED FAILED MISSING')


RunnerMembershipFilter = Enum('RunnerMembershipFilter', 'DIRECT DESCENDANTS')


SastUiComponentSize = Enum('SastUiComponentSize', 'SMALL MEDIUM LARGE')


ScanStatus = Enum('ScanStatus', 'CREATED SUCCEEDED JOB_FAILED REPORT_ERROR PREPARING PREPARATION_FAILED PURGED')


SecurityReportTypeEnum = Enum('SecurityReportTypeEnum', 'SAST SAST_IAC DAST DEPENDENCY_SCANNING CONTAINER_SCANNING SECRET_DETECTION COVERAGE_FUZZING API_FUZZING CLUSTER_IMAGE_SCANNING')


SecurityScannerType = Enum('SecurityScannerType', 'SAST SAST_IAC DAST DEPENDENCY_SCANNING CONTAINER_SCANNING SECRET_DETECTION COVERAGE_FUZZING API_FUZZING CLUSTER_IMAGE_SCANNING')


SentryErrorStatus = Enum('SentryErrorStatus', 'RESOLVED RESOLVED_IN_NEXT_RELEASE UNRESOLVED IGNORED')


ServiceType = Enum('ServiceType', 'ASANA_SERVICE ASSEMBLA_SERVICE BAMBOO_SERVICE BUGZILLA_SERVICE BUILDKITE_SERVICE CAMPFIRE_SERVICE CONFLUENCE_SERVICE CUSTOM_ISSUE_TRACKER_SERVICE DATADOG_SERVICE DISCORD_SERVICE DRONE_CI_SERVICE EMAILS_ON_PUSH_SERVICE EWM_SERVICE EXTERNAL_WIKI_SERVICE FLOWDOCK_SERVICE GITHUB_SERVICE GITLAB_SLACK_APPLICATION_SERVICE HANGOUTS_CHAT_SERVICE HARBOR_SERVICE IRKER_SERVICE JENKINS_SERVICE JIRA_SERVICE MATTERMOST_SERVICE MATTERMOST_SLASH_COMMANDS_SERVICE MICROSOFT_TEAMS_SERVICE PACKAGIST_SERVICE PIPELINES_EMAIL_SERVICE PIVOTALTRACKER_SERVICE PROMETHEUS_SERVICE PUSHOVER_SERVICE REDMINE_SERVICE SHIMO_SERVICE SLACK_SERVICE SLACK_SLASH_COMMANDS_SERVICE TEAMCITY_SERVICE UNIFY_CIRCUIT_SERVICE WEBEX_TEAMS_SERVICE YOUTRACK_SERVICE ZENTAO_SERVICE')


ShaFormat = Enum('ShaFormat', 'SHORT LONG')


SharedRunnersSetting = Enum('SharedRunnersSetting', 'DISABLED_AND_UNOVERRIDABLE DISABLED_WITH_OVERRIDE ENABLED')


SnippetBlobActionEnum = Enum('SnippetBlobActionEnum', 'create update delete move')


Sort = Enum('Sort', 'updated_desc updated_asc created_desc created_asc UPDATED_DESC UPDATED_ASC CREATED_DESC CREATED_ASC')


TestCaseStatus = Enum('TestCaseStatus', 'error failed success skipped')


TestReportState = Enum('TestReportState', 'PASSED FAILED')


TodoActionEnum = Enum('TodoActionEnum', 'assigned mentioned build_failed marked approval_required unmergeable directly_addressed merge_train_removed review_requested')


TodoStateEnum = Enum('TodoStateEnum', 'pending done')


TodoTargetEnum = Enum('TodoTargetEnum', 'COMMIT ISSUE MERGEREQUEST DESIGN ALERT EPIC')


TrainingUrlRequestStatus = Enum('TrainingUrlRequestStatus', 'PENDING COMPLETED')


TypeEnum = Enum('TypeEnum', 'personal project')


UserCalloutFeatureNameEnum = Enum('UserCalloutFeatureNameEnum', 'GKE_CLUSTER_INTEGRATION GCP_SIGNUP_OFFER CLUSTER_SECURITY_WARNING ULTIMATE_TRIAL GEO_ENABLE_HASHED_STORAGE GEO_MIGRATE_HASHED_STORAGE CANARY_DEPLOYMENT GOLD_TRIAL_BILLINGS SUGGEST_POPOVER_DISMISSED TABS_POSITION_HIGHLIGHT THREAT_MONITORING_INFO TWO_FACTOR_AUTH_RECOVERY_SETTINGS_CHECK WEB_IDE_ALERT_DISMISSED ACTIVE_USER_COUNT_THRESHOLD BUY_PIPELINE_MINUTES_NOTIFICATION_DOT PERSONAL_ACCESS_TOKEN_EXPIRY SUGGEST_PIPELINE FEATURE_FLAGS_NEW_VERSION REGISTRATION_ENABLED_CALLOUT NEW_USER_SIGNUPS_CAP_REACHED UNFINISHED_TAG_CLEANUP_CALLOUT EOA_BRONZE_PLAN_BANNER PIPELINE_NEEDS_BANNER PIPELINE_NEEDS_HOVER_TIP WEB_IDE_CI_ENVIRONMENTS_GUIDANCE SECURITY_CONFIGURATION_UPGRADE_BANNER CLOUD_LICENSING_SUBSCRIPTION_ACTIVATION_BANNER TRIAL_STATUS_REMINDER_D14 TRIAL_STATUS_REMINDER_D3 SECURITY_CONFIGURATION_DEVOPS_ALERT PROFILE_PERSONAL_ACCESS_TOKEN_EXPIRY TERRAFORM_NOTIFICATION_DISMISSED SECURITY_NEWSLETTER_CALLOUT VERIFICATION_REMINDER CI_DEPRECATION_WARNING_FOR_TYPES_KEYWORD SECURITY_TRAINING_FEATURE_PROMOTION STORAGE_ENFORCEMENT_BANNER_FIRST_ENFORCEMENT_THRESHOLD STORAGE_ENFORCEMENT_BANNER_SECOND_ENFORCEMENT_THRESHOLD STORAGE_ENFORCEMENT_BANNER_THIRD_ENFORCEMENT_THRESHOLD STORAGE_ENFORCEMENT_BANNER_FOURTH_ENFORCEMENT_THRESHOLD ATTENTION_REQUESTS_TOP_NAV ATTENTION_REQUESTS_SIDE_NAV')


UserState = Enum('UserState', 'active blocked deactivated')


VisibilityLevelsEnum = Enum('VisibilityLevelsEnum', 'private internal public')


VisibilityScopesEnum = Enum('VisibilityScopesEnum', 'private internal public')


VulnerabilityConfidence = Enum('VulnerabilityConfidence', 'IGNORE UNKNOWN EXPERIMENTAL LOW MEDIUM HIGH CONFIRMED')


VulnerabilityDismissalReason = Enum('VulnerabilityDismissalReason', 'ACCEPTABLE_RISK FALSE_POSITIVE MITIGATING_CONTROL USED_IN_TESTS NOT_APPLICABLE')


VulnerabilityExternalIssueLinkExternalTracker = Enum('VulnerabilityExternalIssueLinkExternalTracker', 'JIRA')


VulnerabilityExternalIssueLinkType = Enum('VulnerabilityExternalIssueLinkType', 'CREATED')


VulnerabilityGrade = Enum('VulnerabilityGrade', 'A B C D F')


VulnerabilityIssueLinkType = Enum('VulnerabilityIssueLinkType', 'RELATED CREATED')


VulnerabilityReportType = Enum('VulnerabilityReportType', 'SAST DEPENDENCY_SCANNING CONTAINER_SCANNING DAST SECRET_DETECTION COVERAGE_FUZZING API_FUZZING CLUSTER_IMAGE_SCANNING GENERIC')


VulnerabilitySeverity = Enum('VulnerabilitySeverity', 'INFO UNKNOWN LOW MEDIUM HIGH CRITICAL')


VulnerabilitySort = Enum('VulnerabilitySort', 'severity_desc severity_asc title_desc title_asc detected_desc detected_asc report_type_desc report_type_asc state_desc state_asc')


VulnerabilityState = Enum('VulnerabilityState', 'CONFIRMED DETECTED DISMISSED RESOLVED')


WeightWildcardId = Enum('WeightWildcardId', 'NONE ANY')


WorkItemState = Enum('WorkItemState', 'OPEN CLOSED')


WorkItemStateEvent = Enum('WorkItemStateEvent', 'REOPEN CLOSE')


AccessLevel = TypedDict('AccessLevel', {
	'integerValue': Optional[int],
	'stringValue': Optional['AccessLevelEnum'],
})


AddProjectToSecurityDashboardPayload = TypedDict('AddProjectToSecurityDashboardPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'project': Optional['Project'],
})


AdminSidekiqQueuesDeleteJobsPayload = TypedDict('AdminSidekiqQueuesDeleteJobsPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'result': Optional['DeleteJobsResponse'],
})


AgentConfiguration = TypedDict('AgentConfiguration', {
	'agentName': Optional[str],
})


AgentConfigurationConnection = TypedDict('AgentConfigurationConnection', {
	'edges': Optional[List['AgentConfigurationEdge']],
	'nodes': Optional[List['AgentConfiguration']],
	'pageInfo': 'PageInfo',
})


AgentConfigurationEdge = TypedDict('AgentConfigurationEdge', {
	'cursor': str,
	'node': Optional['AgentConfiguration'],
})


AgentMetadata = TypedDict('AgentMetadata', {
	'commit': Optional[str],
	'podName': Optional[str],
	'podNamespace': Optional[str],
	'version': Optional[str],
})


AlertManagementAlert = TypedDict('AlertManagementAlert', {
	'assignees': Optional['UserCoreConnection'],
	'createdAt': Optional['Time'],
	'description': Optional[str],
	'details': Optional['JSON'],
	'detailsUrl': str,
	'discussions': 'DiscussionConnection',
	'endedAt': Optional['Time'],
	'environment': Optional['Environment'],
	'eventCount': Optional[int],
	'hosts': Optional[List[str]],
	'iid': str,
	'issue': Optional['Issue'],
	'issueIid': Optional[str],
	'metricsDashboardUrl': Optional[str],
	'monitoringTool': Optional[str],
	'notes': 'NoteConnection',
	'prometheusAlert': Optional['PrometheusAlert'],
	'runbook': Optional[str],
	'service': Optional[str],
	'severity': Optional['AlertManagementSeverity'],
	'startedAt': Optional['Time'],
	'status': Optional['AlertManagementStatus'],
	'title': Optional[str],
	'todos': Optional['TodoConnection'],
	'updatedAt': Optional['Time'],
	'webUrl': str,
})


AlertManagementAlertConnection = TypedDict('AlertManagementAlertConnection', {
	'edges': Optional[List['AlertManagementAlertEdge']],
	'nodes': Optional[List['AlertManagementAlert']],
	'pageInfo': 'PageInfo',
})


AlertManagementAlertEdge = TypedDict('AlertManagementAlertEdge', {
	'cursor': str,
	'node': Optional['AlertManagementAlert'],
})


AlertManagementAlertStatusCountsType = TypedDict('AlertManagementAlertStatusCountsType', {
	'acknowledged': Optional[int],
	'all': Optional[int],
	'ignored': Optional[int],
	'open': Optional[int],
	'resolved': Optional[int],
	'triggered': Optional[int],
})


AlertManagementHttpIntegration = TypedDict('AlertManagementHttpIntegration', {
	'active': Optional[bool],
	'apiUrl': Optional[str],
	'id': str,
	'name': Optional[str],
	'payloadAlertFields': Optional[List['AlertManagementPayloadAlertField']],
	'payloadAttributeMappings': Optional[List['AlertManagementPayloadAlertMappingField']],
	'payloadExample': Optional['JsonString'],
	'token': Optional[str],
	'type': 'AlertManagementIntegrationType',
	'url': Optional[str],
})


AlertManagementHttpIntegrationConnection = TypedDict('AlertManagementHttpIntegrationConnection', {
	'edges': Optional[List['AlertManagementHttpIntegrationEdge']],
	'nodes': Optional[List['AlertManagementHttpIntegration']],
	'pageInfo': 'PageInfo',
})


AlertManagementHttpIntegrationEdge = TypedDict('AlertManagementHttpIntegrationEdge', {
	'cursor': str,
	'node': Optional['AlertManagementHttpIntegration'],
})


AlertManagementIntegrationConnection = TypedDict('AlertManagementIntegrationConnection', {
	'edges': Optional[List['AlertManagementIntegrationEdge']],
	'nodes': Optional[List['AlertManagementIntegration']],
	'pageInfo': 'PageInfo',
})


AlertManagementIntegrationEdge = TypedDict('AlertManagementIntegrationEdge', {
	'cursor': str,
	'node': Optional['AlertManagementIntegration'],
})


AlertManagementPayloadAlertField = TypedDict('AlertManagementPayloadAlertField', {
	'label': Optional[str],
	'path': Optional[List['PayloadAlertFieldPathSegment']],
	'type': Optional['AlertManagementPayloadAlertFieldType'],
})


AlertManagementPayloadAlertMappingField = TypedDict('AlertManagementPayloadAlertMappingField', {
	'fieldName': Optional['AlertManagementPayloadAlertFieldName'],
	'label': Optional[str],
	'path': Optional[List['PayloadAlertFieldPathSegment']],
	'type': Optional['AlertManagementPayloadAlertFieldType'],
})


AlertManagementPrometheusIntegration = TypedDict('AlertManagementPrometheusIntegration', {
	'active': Optional[bool],
	'apiUrl': Optional[str],
	'id': str,
	'name': Optional[str],
	'token': Optional[str],
	'type': 'AlertManagementIntegrationType',
	'url': Optional[str],
})


AlertSetAssigneesPayload = TypedDict('AlertSetAssigneesPayload', {
	'alert': Optional['AlertManagementAlert'],
	'clientMutationId': Optional[str],
	'errors': List[str],
	'issue': Optional['Issue'],
	'todo': Optional['Todo'],
})


AlertTodoCreatePayload = TypedDict('AlertTodoCreatePayload', {
	'alert': Optional['AlertManagementAlert'],
	'clientMutationId': Optional[str],
	'errors': List[str],
	'issue': Optional['Issue'],
	'todo': Optional['Todo'],
})


ApiFuzzingCiConfiguration = TypedDict('ApiFuzzingCiConfiguration', {
	'scanModes': Optional[List['ApiFuzzingScanMode']],
	'scanProfiles': Optional[List['ApiFuzzingScanProfile']],
})


ApiFuzzingCiConfigurationCreatePayload = TypedDict('ApiFuzzingCiConfigurationCreatePayload', {
	'clientMutationId': Optional[str],
	'configurationYaml': Optional[str],
	'errors': List[str],
	'gitlabCiYamlEditPath': Optional[str],
})


ApiFuzzingScanProfile = TypedDict('ApiFuzzingScanProfile', {
	'description': Optional[str],
	'name': Optional[str],
	'yaml': Optional[str],
})


ApprovalRule = TypedDict('ApprovalRule', {
	'approvalsRequired': Optional[int],
	'approved': Optional[bool],
	'approvedBy': Optional['UserCoreConnection'],
	'containsHiddenGroups': Optional[bool],
	'eligibleApprovers': Optional[List['UserCore']],
	'groups': Optional['GroupConnection'],
	'id': 'GlobalID',
	'name': Optional[str],
	'overridden': Optional[bool],
	'section': Optional[str],
	'sourceRule': Optional['ApprovalRule'],
	'type': Optional['ApprovalRuleType'],
	'users': Optional['UserCoreConnection'],
})


AssetType = TypedDict('AssetType', {
	'name': str,
	'type': str,
	'url': str,
})


AwardEmoji = TypedDict('AwardEmoji', {
	'description': str,
	'emoji': str,
	'name': str,
	'unicode': str,
	'unicodeVersion': str,
	'user': 'UserCore',
})


AwardEmojiAddPayload = TypedDict('AwardEmojiAddPayload', {
	'awardEmoji': Optional['AwardEmoji'],
	'clientMutationId': Optional[str],
	'errors': List[str],
})


AwardEmojiConnection = TypedDict('AwardEmojiConnection', {
	'edges': Optional[List['AwardEmojiEdge']],
	'nodes': Optional[List['AwardEmoji']],
	'pageInfo': 'PageInfo',
})


AwardEmojiEdge = TypedDict('AwardEmojiEdge', {
	'cursor': str,
	'node': Optional['AwardEmoji'],
})


AwardEmojiRemovePayload = TypedDict('AwardEmojiRemovePayload', {
	'awardEmoji': Optional['AwardEmoji'],
	'clientMutationId': Optional[str],
	'errors': List[str],
})


AwardEmojiTogglePayload = TypedDict('AwardEmojiTogglePayload', {
	'awardEmoji': Optional['AwardEmoji'],
	'clientMutationId': Optional[str],
	'errors': List[str],
	'toggledOn': bool,
})


BaseService = TypedDict('BaseService', {
	'active': Optional[bool],
	'serviceType': Optional['ServiceType'],
	'type': Optional[str],
})


Blob = TypedDict('Blob', {
	'flatPath': str,
	'id': str,
	'lfsOid': Optional[str],
	'mode': Optional[str],
	'name': str,
	'path': str,
	'sha': str,
	'type': 'EntryType',
	'webPath': Optional[str],
	'webUrl': Optional[str],
})


BlobConnection = TypedDict('BlobConnection', {
	'edges': Optional[List['BlobEdge']],
	'nodes': Optional[List['Blob']],
	'pageInfo': 'PageInfo',
})


BlobEdge = TypedDict('BlobEdge', {
	'cursor': str,
	'node': Optional['Blob'],
})


BlobViewer = TypedDict('BlobViewer', {
	'collapsed': bool,
	'fileType': str,
	'loadAsync': bool,
	'loadingPartialName': str,
	'renderError': Optional[str],
	'tooLarge': bool,
	'type': 'BlobViewersType',
})


Board = TypedDict('Board', {
	'assignee': Optional['UserCore'],
	'createdAt': 'Time',
	'epics': Optional['BoardEpicConnection'],
	'hideBacklogList': Optional[bool],
	'hideClosedList': Optional[bool],
	'id': str,
	'iteration': Optional['Iteration'],
	'iterationCadence': Optional['IterationCadence'],
	'labels': Optional['LabelConnection'],
	'lists': Optional['BoardListConnection'],
	'milestone': Optional['Milestone'],
	'name': Optional[str],
	'updatedAt': 'Time',
	'webPath': str,
	'webUrl': str,
	'weight': Optional[int],
})


BoardConnection = TypedDict('BoardConnection', {
	'edges': Optional[List['BoardEdge']],
	'nodes': Optional[List['Board']],
	'pageInfo': 'PageInfo',
})


BoardEdge = TypedDict('BoardEdge', {
	'cursor': str,
	'node': Optional['Board'],
})


BoardEpic = TypedDict('BoardEpic', {
	'ancestors': Optional['EpicConnection'],
	'author': 'UserCore',
	'awardEmoji': Optional['AwardEmojiConnection'],
	'children': Optional['EpicConnection'],
	'closedAt': Optional['Time'],
	'confidential': Optional[bool],
	'createdAt': Optional['Time'],
	'currentUserTodos': 'TodoConnection',
	'descendantCounts': Optional['EpicDescendantCount'],
	'descendantWeightSum': Optional['EpicDescendantWeights'],
	'description': Optional[str],
	'descriptionHtml': Optional[str],
	'discussions': 'DiscussionConnection',
	'downvotes': int,
	'dueDate': Optional['Time'],
	'dueDateFixed': Optional['Time'],
	'dueDateFromInheritedSource': Optional['Time'],
	'dueDateFromMilestones': Optional['Time'],
	'dueDateIsFixed': Optional[bool],
	'events': Optional['EventConnection'],
	'group': 'Group',
	'hasChildren': bool,
	'hasIssues': bool,
	'hasParent': bool,
	'healthStatus': Optional['EpicHealthStatus'],
	'id': str,
	'iid': str,
	'issues': Optional['EpicIssueConnection'],
	'labels': Optional['LabelConnection'],
	'notes': 'NoteConnection',
	'parent': Optional['Epic'],
	'participants': Optional['UserCoreConnection'],
	'reference': str,
	'relationPath': Optional[str],
	'relativePosition': Optional[int],
	'startDate': Optional['Time'],
	'startDateFixed': Optional['Time'],
	'startDateFromInheritedSource': Optional['Time'],
	'startDateFromMilestones': Optional['Time'],
	'startDateIsFixed': Optional[bool],
	'state': 'EpicState',
	'subscribed': bool,
	'title': Optional[str],
	'titleHtml': Optional[str],
	'updatedAt': Optional['Time'],
	'upvotes': int,
	'userDiscussionsCount': int,
	'userNotesCount': int,
	'userPermissions': 'EpicPermissions',
	'userPreferences': Optional['BoardEpicUserPreferences'],
	'webPath': str,
	'webUrl': str,
})


BoardEpicConnection = TypedDict('BoardEpicConnection', {
	'edges': Optional[List['BoardEpicEdge']],
	'nodes': Optional[List['BoardEpic']],
	'pageInfo': 'PageInfo',
})


BoardEpicCreatePayload = TypedDict('BoardEpicCreatePayload', {
	'clientMutationId': Optional[str],
	'epic': Optional['Epic'],
	'errors': List[str],
})


BoardEpicEdge = TypedDict('BoardEpicEdge', {
	'cursor': str,
	'node': Optional['BoardEpic'],
})


BoardEpicUserPreferences = TypedDict('BoardEpicUserPreferences', {
	'collapsed': bool,
})


BoardList = TypedDict('BoardList', {
	'assignee': Optional['UserCore'],
	'collapsed': Optional[bool],
	'id': str,
	'issues': Optional['IssueConnection'],
	'issuesCount': Optional[int],
	'iteration': Optional['Iteration'],
	'label': Optional['Label'],
	'limitMetric': Optional['ListLimitMetric'],
	'listType': str,
	'maxIssueCount': Optional[int],
	'maxIssueWeight': Optional[int],
	'milestone': Optional['Milestone'],
	'position': Optional[int],
	'title': str,
	'totalWeight': Optional[int],
})


BoardListConnection = TypedDict('BoardListConnection', {
	'edges': Optional[List['BoardListEdge']],
	'nodes': Optional[List['BoardList']],
	'pageInfo': 'PageInfo',
})


BoardListCreatePayload = TypedDict('BoardListCreatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'list': Optional['BoardList'],
})


BoardListEdge = TypedDict('BoardListEdge', {
	'cursor': str,
	'node': Optional['BoardList'],
})


BoardListUpdateLimitMetricsPayload = TypedDict('BoardListUpdateLimitMetricsPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'list': Optional['BoardList'],
})


Branch = TypedDict('Branch', {
	'commit': Optional['Commit'],
	'name': str,
})


BulkEnableDevopsAdoptionNamespacesPayload = TypedDict('BulkEnableDevopsAdoptionNamespacesPayload', {
	'clientMutationId': Optional[str],
	'enabledNamespaces': Optional[List['DevopsAdoptionEnabledNamespace']],
	'errors': List[str],
})


BurnupChartDailyTotals = TypedDict('BurnupChartDailyTotals', {
	'completedCount': int,
	'completedWeight': int,
	'date': 'ISO8601Date',
	'scopeCount': int,
	'scopeWeight': int,
})


CiApplicationSettings = TypedDict('CiApplicationSettings', {
	'keepLatestArtifact': Optional[bool],
})


CiBuildNeed = TypedDict('CiBuildNeed', {
	'id': str,
	'name': Optional[str],
})


CiBuildNeedConnection = TypedDict('CiBuildNeedConnection', {
	'edges': Optional[List['CiBuildNeedEdge']],
	'nodes': Optional[List['CiBuildNeed']],
	'pageInfo': 'PageInfo',
})


CiBuildNeedEdge = TypedDict('CiBuildNeedEdge', {
	'cursor': str,
	'node': Optional['CiBuildNeed'],
})


CiCdSettingsUpdatePayload = TypedDict('CiCdSettingsUpdatePayload', {
	'ciCdSettings': 'ProjectCiCdSetting',
	'clientMutationId': Optional[str],
	'errors': List[str],
})


CiConfig = TypedDict('CiConfig', {
	'errors': Optional[List[str]],
	'mergedYaml': Optional[str],
	'stages': Optional['CiConfigStageConnection'],
	'status': Optional['CiConfigStatus'],
	'warnings': Optional[List[str]],
})


CiConfigGroup = TypedDict('CiConfigGroup', {
	'jobs': Optional['CiConfigJobConnection'],
	'name': Optional[str],
	'size': Optional[int],
})


CiConfigGroupConnection = TypedDict('CiConfigGroupConnection', {
	'edges': Optional[List['CiConfigGroupEdge']],
	'nodes': Optional[List['CiConfigGroup']],
	'pageInfo': 'PageInfo',
})


CiConfigGroupEdge = TypedDict('CiConfigGroupEdge', {
	'cursor': str,
	'node': Optional['CiConfigGroup'],
})


CiConfigJob = TypedDict('CiConfigJob', {
	'afterScript': Optional[List[str]],
	'allowFailure': Optional[bool],
	'beforeScript': Optional[List[str]],
	'environment': Optional[str],
	'except': Optional['CiConfigJobRestriction'],
	'groupName': Optional[str],
	'name': Optional[str],
	'needs': Optional['CiConfigNeedConnection'],
	'only': Optional['CiConfigJobRestriction'],
	'script': Optional[List[str]],
	'stage': Optional[str],
	'tags': Optional[List[str]],
	'when': Optional[str],
})


CiConfigJobConnection = TypedDict('CiConfigJobConnection', {
	'edges': Optional[List['CiConfigJobEdge']],
	'nodes': Optional[List['CiConfigJob']],
	'pageInfo': 'PageInfo',
})


CiConfigJobEdge = TypedDict('CiConfigJobEdge', {
	'cursor': str,
	'node': Optional['CiConfigJob'],
})


CiConfigJobRestriction = TypedDict('CiConfigJobRestriction', {
	'refs': Optional[List[str]],
})


CiConfigNeed = TypedDict('CiConfigNeed', {
	'name': Optional[str],
})


CiConfigNeedConnection = TypedDict('CiConfigNeedConnection', {
	'edges': Optional[List['CiConfigNeedEdge']],
	'nodes': Optional[List['CiConfigNeed']],
	'pageInfo': 'PageInfo',
})


CiConfigNeedEdge = TypedDict('CiConfigNeedEdge', {
	'cursor': str,
	'node': Optional['CiConfigNeed'],
})


CiConfigStage = TypedDict('CiConfigStage', {
	'groups': Optional['CiConfigGroupConnection'],
	'name': Optional[str],
})


CiConfigStageConnection = TypedDict('CiConfigStageConnection', {
	'edges': Optional[List['CiConfigStageEdge']],
	'nodes': Optional[List['CiConfigStage']],
	'pageInfo': 'PageInfo',
})


CiConfigStageEdge = TypedDict('CiConfigStageEdge', {
	'cursor': str,
	'node': Optional['CiConfigStage'],
})


CiGroup = TypedDict('CiGroup', {
	'detailedStatus': Optional['DetailedStatus'],
	'id': str,
	'jobs': Optional['CiJobConnection'],
	'name': Optional[str],
	'size': Optional[int],
})


CiGroupConnection = TypedDict('CiGroupConnection', {
	'edges': Optional[List['CiGroupEdge']],
	'nodes': Optional[List['CiGroup']],
	'pageInfo': 'PageInfo',
})


CiGroupEdge = TypedDict('CiGroupEdge', {
	'cursor': str,
	'node': Optional['CiGroup'],
})


CiJob = TypedDict('CiJob', {
	'active': bool,
	'allowFailure': bool,
	'artifacts': Optional['CiJobArtifactConnection'],
	'cancelable': bool,
	'commitPath': Optional[str],
	'coverage': Optional[float],
	'createdAt': 'Time',
	'createdByTag': bool,
	'detailedStatus': Optional['DetailedStatus'],
	'downstreamPipeline': Optional['Pipeline'],
	'duration': Optional[int],
	'finishedAt': Optional['Time'],
	'id': Optional['JobID'],
	'manualJob': Optional[bool],
	'name': Optional[str],
	'needs': Optional['CiBuildNeedConnection'],
	'pipeline': Optional['Pipeline'],
	'playable': bool,
	'previousStageJobsOrNeeds': Optional['JobNeedUnionConnection'],
	'queuedAt': Optional['Time'],
	'queuedDuration': Optional['Duration'],
	'refName': Optional[str],
	'refPath': Optional[str],
	'retryable': bool,
	'scheduledAt': Optional['Time'],
	'schedulingType': Optional[str],
	'shortSha': str,
	'stage': Optional['CiStage'],
	'startedAt': Optional['Time'],
	'status': Optional['CiJobStatus'],
	'stuck': bool,
	'tags': Optional[List[str]],
	'triggered': Optional[bool],
	'userPermissions': 'JobPermissions',
})


CiJobArtifact = TypedDict('CiJobArtifact', {
	'downloadPath': Optional[str],
	'fileType': Optional['JobArtifactFileType'],
	'name': Optional[str],
})


CiJobArtifactConnection = TypedDict('CiJobArtifactConnection', {
	'edges': Optional[List['CiJobArtifactEdge']],
	'nodes': Optional[List['CiJobArtifact']],
	'pageInfo': 'PageInfo',
})


CiJobArtifactEdge = TypedDict('CiJobArtifactEdge', {
	'cursor': str,
	'node': Optional['CiJobArtifact'],
})


CiJobConnection = TypedDict('CiJobConnection', {
	'count': int,
	'edges': Optional[List['CiJobEdge']],
	'nodes': Optional[List['CiJob']],
	'pageInfo': 'PageInfo',
})


CiJobEdge = TypedDict('CiJobEdge', {
	'cursor': str,
	'node': Optional['CiJob'],
})


CiJobTokenScopeAddProjectPayload = TypedDict('CiJobTokenScopeAddProjectPayload', {
	'ciJobTokenScope': Optional['CiJobTokenScopeType'],
	'clientMutationId': Optional[str],
	'errors': List[str],
})


CiJobTokenScopeRemoveProjectPayload = TypedDict('CiJobTokenScopeRemoveProjectPayload', {
	'ciJobTokenScope': Optional['CiJobTokenScopeType'],
	'clientMutationId': Optional[str],
	'errors': List[str],
})


CiJobTokenScopeType = TypedDict('CiJobTokenScopeType', {
	'projects': 'ProjectConnection',
})


CiMinutesNamespaceMonthlyUsage = TypedDict('CiMinutesNamespaceMonthlyUsage', {
	'minutes': Optional[int],
	'month': Optional[str],
	'monthIso8601': Optional['ISO8601Date'],
	'projects': Optional['CiMinutesProjectMonthlyUsageConnection'],
	'sharedRunnersDuration': Optional[int],
})


CiMinutesNamespaceMonthlyUsageConnection = TypedDict('CiMinutesNamespaceMonthlyUsageConnection', {
	'edges': Optional[List['CiMinutesNamespaceMonthlyUsageEdge']],
	'nodes': Optional[List['CiMinutesNamespaceMonthlyUsage']],
	'pageInfo': 'PageInfo',
})


CiMinutesNamespaceMonthlyUsageEdge = TypedDict('CiMinutesNamespaceMonthlyUsageEdge', {
	'cursor': str,
	'node': Optional['CiMinutesNamespaceMonthlyUsage'],
})


CiMinutesProjectMonthlyUsage = TypedDict('CiMinutesProjectMonthlyUsage', {
	'minutes': Optional[int],
	'name': Optional[str],
})


CiMinutesProjectMonthlyUsageConnection = TypedDict('CiMinutesProjectMonthlyUsageConnection', {
	'edges': Optional[List['CiMinutesProjectMonthlyUsageEdge']],
	'nodes': Optional[List['CiMinutesProjectMonthlyUsage']],
	'pageInfo': 'PageInfo',
})


CiMinutesProjectMonthlyUsageEdge = TypedDict('CiMinutesProjectMonthlyUsageEdge', {
	'cursor': str,
	'node': Optional['CiMinutesProjectMonthlyUsage'],
})


CiRunner = TypedDict('CiRunner', {
	'accessLevel': 'CiRunnerAccessLevel',
	'active': bool,
	'adminUrl': Optional[str],
	'contactedAt': Optional['Time'],
	'createdAt': Optional['Time'],
	'description': Optional[str],
	'editAdminUrl': Optional[str],
	'groups': Optional['GroupConnection'],
	'id': 'CiRunnerID',
	'ipAddress': Optional[str],
	'jobCount': Optional[int],
	'jobs': Optional['CiJobConnection'],
	'locked': Optional[bool],
	'maximumTimeout': Optional[int],
	'paused': bool,
	'privateProjectsMinutesCostFactor': Optional[float],
	'projectCount': Optional[int],
	'projects': Optional['ProjectConnection'],
	'publicProjectsMinutesCostFactor': Optional[float],
	'revision': Optional[str],
	'runUntagged': bool,
	'runnerType': 'CiRunnerType',
	'shortSha': Optional[str],
	'status': 'CiRunnerStatus',
	'tagList': Optional[List[str]],
	'tokenExpiresAt': Optional['Time'],
	'userPermissions': 'RunnerPermissions',
	'version': Optional[str],
})


CiRunnerConnection = TypedDict('CiRunnerConnection', {
	'count': int,
	'edges': Optional[List['CiRunnerEdge']],
	'nodes': Optional[List['CiRunner']],
	'pageInfo': 'PageInfo',
})


CiRunnerEdge = TypedDict('CiRunnerEdge', {
	'cursor': str,
	'editUrl': Optional[str],
	'node': Optional['CiRunner'],
	'webUrl': Optional[str],
})


CiStage = TypedDict('CiStage', {
	'detailedStatus': Optional['DetailedStatus'],
	'groups': Optional['CiGroupConnection'],
	'id': str,
	'jobs': Optional['CiJobConnection'],
	'name': Optional[str],
	'status': Optional[str],
})


CiStageConnection = TypedDict('CiStageConnection', {
	'edges': Optional[List['CiStageEdge']],
	'nodes': Optional[List['CiStage']],
	'pageInfo': 'PageInfo',
})


CiStageEdge = TypedDict('CiStageEdge', {
	'cursor': str,
	'node': Optional['CiStage'],
})


CiTemplate = TypedDict('CiTemplate', {
	'content': str,
	'name': str,
})


ClusterAgent = TypedDict('ClusterAgent', {
	'activityEvents': Optional['ClusterAgentActivityEventConnection'],
	'connections': Optional['ConnectedAgentConnection'],
	'createdAt': Optional['Time'],
	'createdByUser': Optional['UserCore'],
	'id': str,
	'name': Optional[str],
	'project': Optional['Project'],
	'tokens': Optional['ClusterAgentTokenConnection'],
	'updatedAt': Optional['Time'],
	'webPath': Optional[str],
})


ClusterAgentActivityEvent = TypedDict('ClusterAgentActivityEvent', {
	'agentToken': Optional['ClusterAgentToken'],
	'kind': Optional[str],
	'level': Optional[str],
	'recordedAt': Optional['Time'],
	'user': Optional['UserCore'],
})


ClusterAgentActivityEventConnection = TypedDict('ClusterAgentActivityEventConnection', {
	'count': int,
	'edges': Optional[List['ClusterAgentActivityEventEdge']],
	'nodes': Optional[List['ClusterAgentActivityEvent']],
	'pageInfo': 'PageInfo',
})


ClusterAgentActivityEventEdge = TypedDict('ClusterAgentActivityEventEdge', {
	'cursor': str,
	'node': Optional['ClusterAgentActivityEvent'],
})


ClusterAgentConnection = TypedDict('ClusterAgentConnection', {
	'count': int,
	'edges': Optional[List['ClusterAgentEdge']],
	'nodes': Optional[List['ClusterAgent']],
	'pageInfo': 'PageInfo',
})


ClusterAgentDeletePayload = TypedDict('ClusterAgentDeletePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
})


ClusterAgentEdge = TypedDict('ClusterAgentEdge', {
	'cursor': str,
	'node': Optional['ClusterAgent'],
})


ClusterAgentToken = TypedDict('ClusterAgentToken', {
	'clusterAgent': Optional['ClusterAgent'],
	'createdAt': Optional['Time'],
	'createdByUser': Optional['UserCore'],
	'description': Optional[str],
	'id': 'ClustersAgentTokenID',
	'lastUsedAt': Optional['Time'],
	'name': Optional[str],
	'status': Optional['AgentTokenStatus'],
})


ClusterAgentTokenConnection = TypedDict('ClusterAgentTokenConnection', {
	'count': int,
	'edges': Optional[List['ClusterAgentTokenEdge']],
	'nodes': Optional[List['ClusterAgentToken']],
	'pageInfo': 'PageInfo',
})


ClusterAgentTokenCreatePayload = TypedDict('ClusterAgentTokenCreatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'secret': Optional[str],
	'token': Optional['ClusterAgentToken'],
})


ClusterAgentTokenDeletePayload = TypedDict('ClusterAgentTokenDeletePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
})


ClusterAgentTokenEdge = TypedDict('ClusterAgentTokenEdge', {
	'cursor': str,
	'node': Optional['ClusterAgentToken'],
})


ClusterAgentTokenRevokePayload = TypedDict('ClusterAgentTokenRevokePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
})


CodeCoverageActivity = TypedDict('CodeCoverageActivity', {
	'averageCoverage': Optional[float],
	'coverageCount': Optional[int],
	'date': 'Date',
	'projectCount': Optional[int],
})


CodeCoverageActivityConnection = TypedDict('CodeCoverageActivityConnection', {
	'edges': Optional[List['CodeCoverageActivityEdge']],
	'nodes': Optional[List['CodeCoverageActivity']],
	'pageInfo': 'PageInfo',
})


CodeCoverageActivityEdge = TypedDict('CodeCoverageActivityEdge', {
	'cursor': str,
	'node': Optional['CodeCoverageActivity'],
})


CodeCoverageSummary = TypedDict('CodeCoverageSummary', {
	'averageCoverage': Optional[float],
	'coverageCount': Optional[int],
	'lastUpdatedOn': Optional['Date'],
})


CodeQualityDegradation = TypedDict('CodeQualityDegradation', {
	'description': str,
	'fingerprint': str,
	'line': int,
	'path': str,
	'severity': 'CodeQualityDegradationSeverity',
})


CodeQualityDegradationConnection = TypedDict('CodeQualityDegradationConnection', {
	'count': int,
	'edges': Optional[List['CodeQualityDegradationEdge']],
	'nodes': Optional[List['CodeQualityDegradation']],
	'pageInfo': 'PageInfo',
})


CodeQualityDegradationEdge = TypedDict('CodeQualityDegradationEdge', {
	'cursor': str,
	'node': Optional['CodeQualityDegradation'],
})


Commit = TypedDict('Commit', {
	'author': Optional['UserCore'],
	'authorEmail': Optional[str],
	'authorGravatar': Optional[str],
	'authorName': Optional[str],
	'authoredDate': Optional['Time'],
	'description': Optional[str],
	'descriptionHtml': Optional[str],
	'fullTitle': Optional[str],
	'fullTitleHtml': Optional[str],
	'id': str,
	'message': Optional[str],
	'pipelines': Optional['PipelineConnection'],
	'sha': str,
	'shortId': str,
	'signatureHtml': Optional[str],
	'title': Optional[str],
	'titleHtml': Optional[str],
	'webPath': str,
	'webUrl': str,
})


CommitConnection = TypedDict('CommitConnection', {
	'edges': Optional[List['CommitEdge']],
	'nodes': Optional[List['Commit']],
	'pageInfo': 'PageInfo',
})


CommitCreatePayload = TypedDict('CommitCreatePayload', {
	'clientMutationId': Optional[str],
	'commit': Optional['Commit'],
	'commitPipelinePath': Optional[str],
	'content': Optional[List[str]],
	'errors': List[str],
})


CommitEdge = TypedDict('CommitEdge', {
	'cursor': str,
	'node': Optional['Commit'],
})


ComplianceFramework = TypedDict('ComplianceFramework', {
	'color': str,
	'description': str,
	'id': str,
	'name': str,
	'pipelineConfigurationFullPath': Optional[str],
})


ComplianceFrameworkConnection = TypedDict('ComplianceFrameworkConnection', {
	'edges': Optional[List['ComplianceFrameworkEdge']],
	'nodes': Optional[List['ComplianceFramework']],
	'pageInfo': 'PageInfo',
})


ComplianceFrameworkEdge = TypedDict('ComplianceFrameworkEdge', {
	'cursor': str,
	'node': Optional['ComplianceFramework'],
})


ComplianceViolation = TypedDict('ComplianceViolation', {
	'id': str,
	'mergeRequest': 'MergeRequest',
	'reason': 'ComplianceViolationReason',
	'severityLevel': 'ComplianceViolationSeverity',
	'violatingUser': 'UserCore',
})


ComplianceViolationConnection = TypedDict('ComplianceViolationConnection', {
	'edges': Optional[List['ComplianceViolationEdge']],
	'nodes': Optional[List['ComplianceViolation']],
	'pageInfo': 'PageInfo',
})


ComplianceViolationEdge = TypedDict('ComplianceViolationEdge', {
	'cursor': str,
	'node': Optional['ComplianceViolation'],
})


ComposerMetadata = TypedDict('ComposerMetadata', {
	'composerJson': 'PackageComposerJsonType',
	'targetSha': str,
})


ConanFileMetadata = TypedDict('ConanFileMetadata', {
	'conanFileType': 'ConanMetadatumFileTypeEnum',
	'conanPackageReference': Optional[str],
	'createdAt': 'Time',
	'id': 'PackagesConanFileMetadatumID',
	'packageRevision': Optional[str],
	'recipeRevision': str,
	'updatedAt': 'Time',
})


ConanMetadata = TypedDict('ConanMetadata', {
	'createdAt': 'Time',
	'id': 'PackagesConanMetadatumID',
	'packageChannel': str,
	'packageUsername': str,
	'recipe': str,
	'recipePath': str,
	'updatedAt': 'Time',
})


ConfigureContainerScanningPayload = TypedDict('ConfigureContainerScanningPayload', {
	'branch': Optional[str],
	'clientMutationId': Optional[str],
	'errors': List[str],
	'successPath': Optional[str],
})


ConfigureDependencyScanningPayload = TypedDict('ConfigureDependencyScanningPayload', {
	'branch': Optional[str],
	'clientMutationId': Optional[str],
	'errors': List[str],
	'successPath': Optional[str],
})


ConfigureSastIacPayload = TypedDict('ConfigureSastIacPayload', {
	'branch': Optional[str],
	'clientMutationId': Optional[str],
	'errors': List[str],
	'successPath': Optional[str],
})


ConfigureSastPayload = TypedDict('ConfigureSastPayload', {
	'branch': Optional[str],
	'clientMutationId': Optional[str],
	'errors': List[str],
	'successPath': Optional[str],
})


ConfigureSecretDetectionPayload = TypedDict('ConfigureSecretDetectionPayload', {
	'branch': Optional[str],
	'clientMutationId': Optional[str],
	'errors': List[str],
	'successPath': Optional[str],
})


ConnectedAgent = TypedDict('ConnectedAgent', {
	'connectedAt': Optional['Time'],
	'connectionId': Optional['BigInt'],
	'metadata': Optional['AgentMetadata'],
})


ConnectedAgentConnection = TypedDict('ConnectedAgentConnection', {
	'edges': Optional[List['ConnectedAgentEdge']],
	'nodes': Optional[List['ConnectedAgent']],
	'pageInfo': 'PageInfo',
})


ConnectedAgentEdge = TypedDict('ConnectedAgentEdge', {
	'cursor': str,
	'node': Optional['ConnectedAgent'],
})


ContainerExpirationPolicy = TypedDict('ContainerExpirationPolicy', {
	'cadence': 'ContainerExpirationPolicyCadenceEnum',
	'createdAt': 'Time',
	'enabled': bool,
	'keepN': Optional['ContainerExpirationPolicyKeepEnum'],
	'nameRegex': Optional['UntrustedRegexp'],
	'nameRegexKeep': Optional['UntrustedRegexp'],
	'nextRunAt': Optional['Time'],
	'olderThan': Optional['ContainerExpirationPolicyOlderThanEnum'],
	'updatedAt': 'Time',
})


ContainerRepository = TypedDict('ContainerRepository', {
	'canDelete': bool,
	'createdAt': 'Time',
	'expirationPolicyCleanupStatus': Optional['ContainerRepositoryCleanupStatus'],
	'expirationPolicyStartedAt': Optional['Time'],
	'id': str,
	'location': str,
	'name': str,
	'path': str,
	'project': 'Project',
	'status': Optional['ContainerRepositoryStatus'],
	'tagsCount': int,
	'updatedAt': 'Time',
})


ContainerRepositoryConnection = TypedDict('ContainerRepositoryConnection', {
	'edges': Optional[List['ContainerRepositoryEdge']],
	'nodes': Optional[List['ContainerRepository']],
	'pageInfo': 'PageInfo',
})


ContainerRepositoryDetails = TypedDict('ContainerRepositoryDetails', {
	'canDelete': bool,
	'createdAt': 'Time',
	'expirationPolicyCleanupStatus': Optional['ContainerRepositoryCleanupStatus'],
	'expirationPolicyStartedAt': Optional['Time'],
	'id': str,
	'location': str,
	'name': str,
	'path': str,
	'project': 'Project',
	'size': Optional[float],
	'status': Optional['ContainerRepositoryStatus'],
	'tags': Optional['ContainerRepositoryTagConnection'],
	'tagsCount': int,
	'updatedAt': 'Time',
})


ContainerRepositoryEdge = TypedDict('ContainerRepositoryEdge', {
	'cursor': str,
	'node': Optional['ContainerRepository'],
})


ContainerRepositoryTag = TypedDict('ContainerRepositoryTag', {
	'canDelete': bool,
	'createdAt': Optional['Time'],
	'digest': Optional[str],
	'location': str,
	'name': str,
	'path': str,
	'revision': Optional[str],
	'shortRevision': Optional[str],
	'totalSize': Optional['BigInt'],
})


ContainerRepositoryTagConnection = TypedDict('ContainerRepositoryTagConnection', {
	'edges': Optional[List['ContainerRepositoryTagEdge']],
	'nodes': Optional[List['ContainerRepositoryTag']],
	'pageInfo': 'PageInfo',
})


ContainerRepositoryTagEdge = TypedDict('ContainerRepositoryTagEdge', {
	'cursor': str,
	'node': Optional['ContainerRepositoryTag'],
})


CorpusCreatePayload = TypedDict('CorpusCreatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
})


CoverageFuzzingCorpus = TypedDict('CoverageFuzzingCorpus', {
	'id': 'AppSecFuzzingCoverageCorpusID',
	'package': 'PackageDetailsType',
})


CoverageFuzzingCorpusConnection = TypedDict('CoverageFuzzingCorpusConnection', {
	'edges': Optional[List['CoverageFuzzingCorpusEdge']],
	'nodes': Optional[List['CoverageFuzzingCorpus']],
	'pageInfo': 'PageInfo',
})


CoverageFuzzingCorpusEdge = TypedDict('CoverageFuzzingCorpusEdge', {
	'cursor': str,
	'node': Optional['CoverageFuzzingCorpus'],
})


CreateAlertIssuePayload = TypedDict('CreateAlertIssuePayload', {
	'alert': Optional['AlertManagementAlert'],
	'clientMutationId': Optional[str],
	'errors': List[str],
	'issue': Optional['Issue'],
	'todo': Optional['Todo'],
})


CreateAnnotationPayload = TypedDict('CreateAnnotationPayload', {
	'annotation': Optional['MetricsDashboardAnnotation'],
	'clientMutationId': Optional[str],
	'errors': List[str],
})


CreateBoardPayload = TypedDict('CreateBoardPayload', {
	'board': Optional['Board'],
	'clientMutationId': Optional[str],
	'errors': List[str],
})


CreateBranchPayload = TypedDict('CreateBranchPayload', {
	'branch': Optional['Branch'],
	'clientMutationId': Optional[str],
	'errors': List[str],
})


CreateClusterAgentPayload = TypedDict('CreateClusterAgentPayload', {
	'clientMutationId': Optional[str],
	'clusterAgent': Optional['ClusterAgent'],
	'errors': List[str],
})


CreateComplianceFrameworkPayload = TypedDict('CreateComplianceFrameworkPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'framework': Optional['ComplianceFramework'],
})


CreateCustomEmojiPayload = TypedDict('CreateCustomEmojiPayload', {
	'clientMutationId': Optional[str],
	'customEmoji': Optional['CustomEmoji'],
	'errors': List[str],
})


CreateDiffNotePayload = TypedDict('CreateDiffNotePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'note': Optional['Note'],
})


CreateEpicPayload = TypedDict('CreateEpicPayload', {
	'clientMutationId': Optional[str],
	'epic': Optional['Epic'],
	'errors': List[str],
})


CreateImageDiffNotePayload = TypedDict('CreateImageDiffNotePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'note': Optional['Note'],
})


CreateIssuePayload = TypedDict('CreateIssuePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'issue': Optional['Issue'],
})


CreateIterationPayload = TypedDict('CreateIterationPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'iteration': Optional['Iteration'],
})


CreateNotePayload = TypedDict('CreateNotePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'note': Optional['Note'],
})


CreateRequirementPayload = TypedDict('CreateRequirementPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'requirement': Optional['Requirement'],
})


CreateSnippetPayload = TypedDict('CreateSnippetPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'snippet': Optional['Snippet'],
})


CreateTestCasePayload = TypedDict('CreateTestCasePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'testCase': Optional['Issue'],
})


CurrentLicense = TypedDict('CurrentLicense', {
	'activatedAt': Optional['Date'],
	'billableUsersCount': Optional[int],
	'blockChangesAt': Optional['Date'],
	'company': Optional[str],
	'createdAt': Optional['Date'],
	'email': Optional[str],
	'expiresAt': Optional['Date'],
	'id': str,
	'lastSync': Optional['Time'],
	'maximumUserCount': Optional[int],
	'name': Optional[str],
	'plan': str,
	'startsAt': Optional['Date'],
	'type': str,
	'usersInLicenseCount': Optional[int],
	'usersOverLicenseCount': Optional[int],
})


CustomEmoji = TypedDict('CustomEmoji', {
	'external': bool,
	'id': 'CustomEmojiID',
	'name': str,
	'url': str,
})


CustomEmojiConnection = TypedDict('CustomEmojiConnection', {
	'edges': Optional[List['CustomEmojiEdge']],
	'nodes': Optional[List['CustomEmoji']],
	'pageInfo': 'PageInfo',
})


CustomEmojiEdge = TypedDict('CustomEmojiEdge', {
	'cursor': str,
	'node': Optional['CustomEmoji'],
})


CustomerRelationsContact = TypedDict('CustomerRelationsContact', {
	'createdAt': 'Time',
	'description': Optional[str],
	'email': Optional[str],
	'firstName': str,
	'id': str,
	'lastName': str,
	'organization': Optional['CustomerRelationsOrganization'],
	'phone': Optional[str],
	'updatedAt': 'Time',
})


CustomerRelationsContactConnection = TypedDict('CustomerRelationsContactConnection', {
	'edges': Optional[List['CustomerRelationsContactEdge']],
	'nodes': Optional[List['CustomerRelationsContact']],
	'pageInfo': 'PageInfo',
})


CustomerRelationsContactCreatePayload = TypedDict('CustomerRelationsContactCreatePayload', {
	'clientMutationId': Optional[str],
	'contact': Optional['CustomerRelationsContact'],
	'errors': List[str],
})


CustomerRelationsContactEdge = TypedDict('CustomerRelationsContactEdge', {
	'cursor': str,
	'node': Optional['CustomerRelationsContact'],
})


CustomerRelationsContactUpdatePayload = TypedDict('CustomerRelationsContactUpdatePayload', {
	'clientMutationId': Optional[str],
	'contact': Optional['CustomerRelationsContact'],
	'errors': List[str],
})


CustomerRelationsOrganization = TypedDict('CustomerRelationsOrganization', {
	'createdAt': 'Time',
	'defaultRate': Optional[float],
	'description': Optional[str],
	'id': str,
	'name': str,
	'updatedAt': 'Time',
})


CustomerRelationsOrganizationConnection = TypedDict('CustomerRelationsOrganizationConnection', {
	'edges': Optional[List['CustomerRelationsOrganizationEdge']],
	'nodes': Optional[List['CustomerRelationsOrganization']],
	'pageInfo': 'PageInfo',
})


CustomerRelationsOrganizationCreatePayload = TypedDict('CustomerRelationsOrganizationCreatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'organization': Optional['CustomerRelationsOrganization'],
})


CustomerRelationsOrganizationEdge = TypedDict('CustomerRelationsOrganizationEdge', {
	'cursor': str,
	'node': Optional['CustomerRelationsOrganization'],
})


CustomerRelationsOrganizationUpdatePayload = TypedDict('CustomerRelationsOrganizationUpdatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'organization': 'CustomerRelationsOrganization',
})


DastOnDemandScanCreatePayload = TypedDict('DastOnDemandScanCreatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'pipelineUrl': Optional[str],
})


DastProfile = TypedDict('DastProfile', {
	'branch': Optional['DastProfileBranch'],
	'dastProfileSchedule': Optional['DastProfileSchedule'],
	'dastScannerProfile': Optional['DastScannerProfile'],
	'dastSiteProfile': Optional['DastSiteProfile'],
	'description': Optional[str],
	'editPath': Optional[str],
	'id': 'DastProfileID',
	'name': Optional[str],
})


DastProfileBranch = TypedDict('DastProfileBranch', {
	'exists': Optional[bool],
	'name': Optional[str],
})


DastProfileCadence = TypedDict('DastProfileCadence', {
	'duration': Optional[int],
	'unit': Optional['DastProfileCadenceUnit'],
})


DastProfileConnection = TypedDict('DastProfileConnection', {
	'count': int,
	'edges': Optional[List['DastProfileEdge']],
	'nodes': Optional[List['DastProfile']],
	'pageInfo': 'PageInfo',
})


DastProfileCreatePayload = TypedDict('DastProfileCreatePayload', {
	'clientMutationId': Optional[str],
	'dastProfile': Optional['DastProfile'],
	'errors': List[str],
	'pipelineUrl': Optional[str],
})


DastProfileDeletePayload = TypedDict('DastProfileDeletePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
})


DastProfileEdge = TypedDict('DastProfileEdge', {
	'cursor': str,
	'node': Optional['DastProfile'],
})


DastProfileRunPayload = TypedDict('DastProfileRunPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'pipelineUrl': Optional[str],
})


DastProfileSchedule = TypedDict('DastProfileSchedule', {
	'active': Optional[bool],
	'cadence': Optional['DastProfileCadence'],
	'id': 'DastProfileScheduleID',
	'nextRunAt': Optional['Time'],
	'ownerValid': Optional[bool],
	'startsAt': Optional['Time'],
	'timezone': Optional[str],
})


DastProfileUpdatePayload = TypedDict('DastProfileUpdatePayload', {
	'clientMutationId': Optional[str],
	'dastProfile': Optional['DastProfile'],
	'errors': List[str],
	'pipelineUrl': Optional[str],
})


DastScannerProfile = TypedDict('DastScannerProfile', {
	'editPath': Optional[str],
	'id': 'DastScannerProfileID',
	'profileName': Optional[str],
	'referencedInSecurityPolicies': Optional[List[str]],
	'scanType': Optional['DastScanTypeEnum'],
	'showDebugMessages': bool,
	'spiderTimeout': Optional[int],
	'targetTimeout': Optional[int],
	'useAjaxSpider': bool,
})


DastScannerProfileConnection = TypedDict('DastScannerProfileConnection', {
	'edges': Optional[List['DastScannerProfileEdge']],
	'nodes': Optional[List['DastScannerProfile']],
	'pageInfo': 'PageInfo',
})


DastScannerProfileCreatePayload = TypedDict('DastScannerProfileCreatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'id': Optional['DastScannerProfileID'],
})


DastScannerProfileDeletePayload = TypedDict('DastScannerProfileDeletePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
})


DastScannerProfileEdge = TypedDict('DastScannerProfileEdge', {
	'cursor': str,
	'node': Optional['DastScannerProfile'],
})


DastScannerProfileUpdatePayload = TypedDict('DastScannerProfileUpdatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'id': Optional['DastScannerProfileID'],
})


DastSiteProfile = TypedDict('DastSiteProfile', {
	'auth': Optional['DastSiteProfileAuth'],
	'editPath': Optional[str],
	'excludedUrls': Optional[List[str]],
	'id': 'DastSiteProfileID',
	'normalizedTargetUrl': Optional[str],
	'profileName': Optional[str],
	'referencedInSecurityPolicies': Optional[List[str]],
	'requestHeaders': Optional[str],
	'scanMethod': Optional['DastScanMethodType'],
	'targetType': Optional['DastTargetTypeEnum'],
	'targetUrl': Optional[str],
	'userPermissions': 'DastSiteProfilePermissions',
	'validationStatus': Optional['DastSiteProfileValidationStatusEnum'],
})


DastSiteProfileAuth = TypedDict('DastSiteProfileAuth', {
	'enabled': Optional[bool],
	'password': Optional[str],
	'passwordField': Optional[str],
	'url': Optional[str],
	'username': Optional[str],
	'usernameField': Optional[str],
})


DastSiteProfileConnection = TypedDict('DastSiteProfileConnection', {
	'edges': Optional[List['DastSiteProfileEdge']],
	'nodes': Optional[List['DastSiteProfile']],
	'pageInfo': 'PageInfo',
})


DastSiteProfileCreatePayload = TypedDict('DastSiteProfileCreatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'id': Optional['DastSiteProfileID'],
})


DastSiteProfileDeletePayload = TypedDict('DastSiteProfileDeletePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
})


DastSiteProfileEdge = TypedDict('DastSiteProfileEdge', {
	'cursor': str,
	'node': Optional['DastSiteProfile'],
})


DastSiteProfilePermissions = TypedDict('DastSiteProfilePermissions', {
	'createOnDemandDastScan': bool,
})


DastSiteProfileUpdatePayload = TypedDict('DastSiteProfileUpdatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'id': Optional['DastSiteProfileID'],
})


DastSiteTokenCreatePayload = TypedDict('DastSiteTokenCreatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'id': Optional['DastSiteTokenID'],
	'status': Optional['DastSiteProfileValidationStatusEnum'],
	'token': Optional[str],
})


DastSiteValidation = TypedDict('DastSiteValidation', {
	'id': 'DastSiteValidationID',
	'normalizedTargetUrl': Optional[str],
	'status': 'DastSiteProfileValidationStatusEnum',
})


DastSiteValidationConnection = TypedDict('DastSiteValidationConnection', {
	'edges': Optional[List['DastSiteValidationEdge']],
	'nodes': Optional[List['DastSiteValidation']],
	'pageInfo': 'PageInfo',
})


DastSiteValidationCreatePayload = TypedDict('DastSiteValidationCreatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'id': Optional['DastSiteValidationID'],
	'status': Optional['DastSiteProfileValidationStatusEnum'],
})


DastSiteValidationEdge = TypedDict('DastSiteValidationEdge', {
	'cursor': str,
	'node': Optional['DastSiteValidation'],
})


DastSiteValidationRevokePayload = TypedDict('DastSiteValidationRevokePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
})


DeleteAnnotationPayload = TypedDict('DeleteAnnotationPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
})


DeleteJobsResponse = TypedDict('DeleteJobsResponse', {
	'completed': Optional[bool],
	'deletedJobs': Optional[int],
	'queueSize': Optional[int],
})


DependencyProxyBlob = TypedDict('DependencyProxyBlob', {
	'createdAt': 'Time',
	'fileName': str,
	'size': str,
	'updatedAt': 'Time',
})


DependencyProxyBlobConnection = TypedDict('DependencyProxyBlobConnection', {
	'edges': Optional[List['DependencyProxyBlobEdge']],
	'nodes': Optional[List['DependencyProxyBlob']],
	'pageInfo': 'PageInfo',
})


DependencyProxyBlobEdge = TypedDict('DependencyProxyBlobEdge', {
	'cursor': str,
	'node': Optional['DependencyProxyBlob'],
})


DependencyProxyImageTtlGroupPolicy = TypedDict('DependencyProxyImageTtlGroupPolicy', {
	'createdAt': Optional['Time'],
	'enabled': bool,
	'ttl': Optional[int],
	'updatedAt': Optional['Time'],
})


DependencyProxyManifest = TypedDict('DependencyProxyManifest', {
	'createdAt': 'Time',
	'digest': str,
	'fileName': str,
	'id': 'DependencyProxyManifestID',
	'imageName': str,
	'size': str,
	'updatedAt': 'Time',
})


DependencyProxyManifestConnection = TypedDict('DependencyProxyManifestConnection', {
	'edges': Optional[List['DependencyProxyManifestEdge']],
	'nodes': Optional[List['DependencyProxyManifest']],
	'pageInfo': 'PageInfo',
})


DependencyProxyManifestEdge = TypedDict('DependencyProxyManifestEdge', {
	'cursor': str,
	'node': Optional['DependencyProxyManifest'],
})


DependencyProxySetting = TypedDict('DependencyProxySetting', {
	'enabled': bool,
})


Design = TypedDict('Design', {
	'currentUserTodos': 'TodoConnection',
	'diffRefs': 'DiffRefs',
	'discussions': 'DiscussionConnection',
	'event': 'DesignVersionEvent',
	'filename': str,
	'fullPath': str,
	'id': str,
	'image': str,
	'imageV432x230': Optional[str],
	'issue': 'Issue',
	'notes': 'NoteConnection',
	'notesCount': int,
	'project': 'Project',
	'versions': 'DesignVersionConnection',
	'webUrl': str,
})


DesignAtVersion = TypedDict('DesignAtVersion', {
	'design': 'Design',
	'diffRefs': 'DiffRefs',
	'event': 'DesignVersionEvent',
	'filename': str,
	'fullPath': str,
	'id': str,
	'image': str,
	'imageV432x230': Optional[str],
	'issue': 'Issue',
	'notesCount': int,
	'project': 'Project',
	'version': 'DesignVersion',
})


DesignAtVersionConnection = TypedDict('DesignAtVersionConnection', {
	'edges': Optional[List['DesignAtVersionEdge']],
	'nodes': Optional[List['DesignAtVersion']],
	'pageInfo': 'PageInfo',
})


DesignAtVersionEdge = TypedDict('DesignAtVersionEdge', {
	'cursor': str,
	'node': Optional['DesignAtVersion'],
})


DesignCollection = TypedDict('DesignCollection', {
	'copyState': Optional['DesignCollectionCopyState'],
	'design': Optional['Design'],
	'designAtVersion': Optional['DesignAtVersion'],
	'designs': 'DesignConnection',
	'issue': 'Issue',
	'project': 'Project',
	'version': Optional['DesignVersion'],
	'versions': 'DesignVersionConnection',
})


DesignConnection = TypedDict('DesignConnection', {
	'edges': Optional[List['DesignEdge']],
	'nodes': Optional[List['Design']],
	'pageInfo': 'PageInfo',
})


DesignEdge = TypedDict('DesignEdge', {
	'cursor': str,
	'node': Optional['Design'],
})


DesignManagement = TypedDict('DesignManagement', {
	'designAtVersion': Optional['DesignAtVersion'],
	'version': Optional['DesignVersion'],
})


DesignManagementDeletePayload = TypedDict('DesignManagementDeletePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'version': Optional['DesignVersion'],
})


DesignManagementMovePayload = TypedDict('DesignManagementMovePayload', {
	'clientMutationId': Optional[str],
	'designCollection': Optional['DesignCollection'],
	'errors': List[str],
})


DesignManagementUploadPayload = TypedDict('DesignManagementUploadPayload', {
	'clientMutationId': Optional[str],
	'designs': List['Design'],
	'errors': List[str],
	'skippedDesigns': List['Design'],
})


DesignVersion = TypedDict('DesignVersion', {
	'author': 'UserCore',
	'createdAt': 'Time',
	'designAtVersion': 'DesignAtVersion',
	'designs': 'DesignConnection',
	'designsAtVersion': 'DesignAtVersionConnection',
	'id': str,
	'sha': str,
})


DesignVersionConnection = TypedDict('DesignVersionConnection', {
	'edges': Optional[List['DesignVersionEdge']],
	'nodes': Optional[List['DesignVersion']],
	'pageInfo': 'PageInfo',
})


DesignVersionEdge = TypedDict('DesignVersionEdge', {
	'cursor': str,
	'node': Optional['DesignVersion'],
})


DestroyBoardListPayload = TypedDict('DestroyBoardListPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'list': Optional['BoardList'],
})


DestroyBoardPayload = TypedDict('DestroyBoardPayload', {
	'board': Optional['Board'],
	'clientMutationId': Optional[str],
	'errors': List[str],
})


DestroyComplianceFrameworkPayload = TypedDict('DestroyComplianceFrameworkPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
})


DestroyContainerRepositoryPayload = TypedDict('DestroyContainerRepositoryPayload', {
	'clientMutationId': Optional[str],
	'containerRepository': 'ContainerRepository',
	'errors': List[str],
})


DestroyContainerRepositoryTagsPayload = TypedDict('DestroyContainerRepositoryTagsPayload', {
	'clientMutationId': Optional[str],
	'deletedTagNames': List[str],
	'errors': List[str],
})


DestroyCustomEmojiPayload = TypedDict('DestroyCustomEmojiPayload', {
	'clientMutationId': Optional[str],
	'customEmoji': Optional['CustomEmoji'],
	'errors': List[str],
})


DestroyEpicBoardPayload = TypedDict('DestroyEpicBoardPayload', {
	'clientMutationId': Optional[str],
	'epicBoard': Optional['EpicBoard'],
	'errors': List[str],
})


DestroyNotePayload = TypedDict('DestroyNotePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'note': Optional['Note'],
})


DestroyPackageFilePayload = TypedDict('DestroyPackageFilePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
})


DestroyPackagePayload = TypedDict('DestroyPackagePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
})


DestroySnippetPayload = TypedDict('DestroySnippetPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'snippet': Optional['Snippet'],
})


DetailedStatus = TypedDict('DetailedStatus', {
	'action': Optional['StatusAction'],
	'detailsPath': Optional[str],
	'favicon': Optional[str],
	'group': Optional[str],
	'hasDetails': Optional[bool],
	'icon': Optional[str],
	'id': str,
	'label': Optional[str],
	'text': Optional[str],
	'tooltip': Optional[str],
})


DevopsAdoptionEnabledNamespace = TypedDict('DevopsAdoptionEnabledNamespace', {
	'displayNamespace': Optional['Namespace'],
	'id': str,
	'latestSnapshot': Optional['DevopsAdoptionSnapshot'],
	'namespace': Optional['Namespace'],
	'snapshots': Optional['DevopsAdoptionSnapshotConnection'],
})


DevopsAdoptionEnabledNamespaceConnection = TypedDict('DevopsAdoptionEnabledNamespaceConnection', {
	'edges': Optional[List['DevopsAdoptionEnabledNamespaceEdge']],
	'nodes': Optional[List['DevopsAdoptionEnabledNamespace']],
	'pageInfo': 'PageInfo',
})


DevopsAdoptionEnabledNamespaceEdge = TypedDict('DevopsAdoptionEnabledNamespaceEdge', {
	'cursor': str,
	'node': Optional['DevopsAdoptionEnabledNamespace'],
})


DevopsAdoptionSnapshot = TypedDict('DevopsAdoptionSnapshot', {
	'codeOwnersUsedCount': Optional[int],
	'coverageFuzzingEnabledCount': Optional[int],
	'dastEnabledCount': Optional[int],
	'dependencyScanningEnabledCount': Optional[int],
	'deploySucceeded': bool,
	'endTime': 'Time',
	'issueOpened': bool,
	'mergeRequestApproved': bool,
	'mergeRequestOpened': bool,
	'pipelineSucceeded': bool,
	'recordedAt': 'Time',
	'runnerConfigured': bool,
	'sastEnabledCount': Optional[int],
	'securityScanSucceeded': bool,
	'startTime': 'Time',
	'totalProjectsCount': Optional[int],
	'vulnerabilityManagementUsedCount': Optional[int],
})


DevopsAdoptionSnapshotConnection = TypedDict('DevopsAdoptionSnapshotConnection', {
	'edges': Optional[List['DevopsAdoptionSnapshotEdge']],
	'nodes': Optional[List['DevopsAdoptionSnapshot']],
	'pageInfo': 'PageInfo',
})


DevopsAdoptionSnapshotEdge = TypedDict('DevopsAdoptionSnapshotEdge', {
	'cursor': str,
	'node': Optional['DevopsAdoptionSnapshot'],
})


DiffPosition = TypedDict('DiffPosition', {
	'diffRefs': 'DiffRefs',
	'filePath': str,
	'height': Optional[int],
	'newLine': Optional[int],
	'newPath': Optional[str],
	'oldLine': Optional[int],
	'oldPath': Optional[str],
	'positionType': 'DiffPositionType',
	'width': Optional[int],
	'x': Optional[int],
	'y': Optional[int],
})


DiffRefs = TypedDict('DiffRefs', {
	'baseSha': Optional[str],
	'headSha': str,
	'startSha': str,
})


DiffStats = TypedDict('DiffStats', {
	'additions': int,
	'deletions': int,
	'path': str,
})


DiffStatsSummary = TypedDict('DiffStatsSummary', {
	'additions': int,
	'changes': int,
	'deletions': int,
	'fileCount': int,
})


DisableDevopsAdoptionNamespacePayload = TypedDict('DisableDevopsAdoptionNamespacePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
})


Discussion = TypedDict('Discussion', {
	'createdAt': 'Time',
	'id': 'DiscussionID',
	'noteable': Optional['NoteableType'],
	'notes': 'NoteConnection',
	'replyId': 'DiscussionID',
	'resolvable': bool,
	'resolved': bool,
	'resolvedAt': Optional['Time'],
	'resolvedBy': Optional['UserCore'],
})


DiscussionConnection = TypedDict('DiscussionConnection', {
	'edges': Optional[List['DiscussionEdge']],
	'nodes': Optional[List['Discussion']],
	'pageInfo': 'PageInfo',
})


DiscussionEdge = TypedDict('DiscussionEdge', {
	'cursor': str,
	'node': Optional['Discussion'],
})


DiscussionToggleResolvePayload = TypedDict('DiscussionToggleResolvePayload', {
	'clientMutationId': Optional[str],
	'discussion': Optional['Discussion'],
	'errors': List[str],
})


Dora = TypedDict('Dora', {
	'metrics': Optional[List['DoraMetric']],
})


DoraMetric = TypedDict('DoraMetric', {
	'date': Optional[str],
	'value': Optional[int],
})


EchoCreatePayload = TypedDict('EchoCreatePayload', {
	'clientMutationId': Optional[str],
	'echoes': Optional[List[str]],
	'errors': List[str],
})


EnableDevopsAdoptionNamespacePayload = TypedDict('EnableDevopsAdoptionNamespacePayload', {
	'clientMutationId': Optional[str],
	'enabledNamespace': Optional['DevopsAdoptionEnabledNamespace'],
	'errors': List[str],
})


Environment = TypedDict('Environment', {
	'id': str,
	'latestOpenedMostSevereAlert': Optional['AlertManagementAlert'],
	'metricsDashboard': Optional['MetricsDashboard'],
	'name': str,
	'path': str,
	'state': str,
})


EnvironmentConnection = TypedDict('EnvironmentConnection', {
	'edges': Optional[List['EnvironmentEdge']],
	'nodes': Optional[List['Environment']],
	'pageInfo': 'PageInfo',
})


EnvironmentEdge = TypedDict('EnvironmentEdge', {
	'cursor': str,
	'node': Optional['Environment'],
})


EnvironmentsCanaryIngressUpdatePayload = TypedDict('EnvironmentsCanaryIngressUpdatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
})


Epic = TypedDict('Epic', {
	'ancestors': Optional['EpicConnection'],
	'author': 'UserCore',
	'awardEmoji': Optional['AwardEmojiConnection'],
	'children': Optional['EpicConnection'],
	'closedAt': Optional['Time'],
	'confidential': Optional[bool],
	'createdAt': Optional['Time'],
	'currentUserTodos': 'TodoConnection',
	'descendantCounts': Optional['EpicDescendantCount'],
	'descendantWeightSum': Optional['EpicDescendantWeights'],
	'description': Optional[str],
	'descriptionHtml': Optional[str],
	'discussions': 'DiscussionConnection',
	'downvotes': int,
	'dueDate': Optional['Time'],
	'dueDateFixed': Optional['Time'],
	'dueDateFromInheritedSource': Optional['Time'],
	'dueDateFromMilestones': Optional['Time'],
	'dueDateIsFixed': Optional[bool],
	'events': Optional['EventConnection'],
	'group': 'Group',
	'hasChildren': bool,
	'hasIssues': bool,
	'hasParent': bool,
	'healthStatus': Optional['EpicHealthStatus'],
	'id': str,
	'iid': str,
	'issues': Optional['EpicIssueConnection'],
	'labels': Optional['LabelConnection'],
	'notes': 'NoteConnection',
	'parent': Optional['Epic'],
	'participants': Optional['UserCoreConnection'],
	'reference': str,
	'relationPath': Optional[str],
	'relativePosition': Optional[int],
	'startDate': Optional['Time'],
	'startDateFixed': Optional['Time'],
	'startDateFromInheritedSource': Optional['Time'],
	'startDateFromMilestones': Optional['Time'],
	'startDateIsFixed': Optional[bool],
	'state': 'EpicState',
	'subscribed': bool,
	'title': Optional[str],
	'titleHtml': Optional[str],
	'updatedAt': Optional['Time'],
	'upvotes': int,
	'userDiscussionsCount': int,
	'userNotesCount': int,
	'userPermissions': 'EpicPermissions',
	'webPath': str,
	'webUrl': str,
})


EpicAddIssuePayload = TypedDict('EpicAddIssuePayload', {
	'clientMutationId': Optional[str],
	'epic': Optional['Epic'],
	'epicIssue': Optional['EpicIssue'],
	'errors': List[str],
})


EpicBoard = TypedDict('EpicBoard', {
	'hideBacklogList': Optional[bool],
	'hideClosedList': Optional[bool],
	'id': 'BoardsEpicBoardID',
	'labels': Optional['LabelConnection'],
	'lists': Optional['EpicListConnection'],
	'name': Optional[str],
	'webPath': str,
	'webUrl': str,
})


EpicBoardConnection = TypedDict('EpicBoardConnection', {
	'edges': Optional[List['EpicBoardEdge']],
	'nodes': Optional[List['EpicBoard']],
	'pageInfo': 'PageInfo',
})


EpicBoardCreatePayload = TypedDict('EpicBoardCreatePayload', {
	'clientMutationId': Optional[str],
	'epicBoard': Optional['EpicBoard'],
	'errors': List[str],
})


EpicBoardEdge = TypedDict('EpicBoardEdge', {
	'cursor': str,
	'node': Optional['EpicBoard'],
})


EpicBoardListCreatePayload = TypedDict('EpicBoardListCreatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'list': Optional['EpicList'],
})


EpicBoardListDestroyPayload = TypedDict('EpicBoardListDestroyPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'list': Optional['EpicList'],
})


EpicBoardUpdatePayload = TypedDict('EpicBoardUpdatePayload', {
	'clientMutationId': Optional[str],
	'epicBoard': Optional['EpicBoard'],
	'errors': List[str],
})


EpicConnection = TypedDict('EpicConnection', {
	'edges': Optional[List['EpicEdge']],
	'nodes': Optional[List['Epic']],
	'pageInfo': 'PageInfo',
})


EpicDescendantCount = TypedDict('EpicDescendantCount', {
	'closedEpics': Optional[int],
	'closedIssues': Optional[int],
	'openedEpics': Optional[int],
	'openedIssues': Optional[int],
})


EpicDescendantWeights = TypedDict('EpicDescendantWeights', {
	'closedIssues': Optional[int],
	'openedIssues': Optional[int],
})


EpicEdge = TypedDict('EpicEdge', {
	'cursor': str,
	'node': Optional['Epic'],
})


EpicHealthStatus = TypedDict('EpicHealthStatus', {
	'issuesAtRisk': Optional[int],
	'issuesNeedingAttention': Optional[int],
	'issuesOnTrack': Optional[int],
})


EpicIssue = TypedDict('EpicIssue', {
	'alertManagementAlert': Optional['AlertManagementAlert'],
	'assignees': Optional['UserCoreConnection'],
	'author': 'UserCore',
	'blocked': bool,
	'blockedByCount': Optional[int],
	'blockedByIssues': Optional['IssueConnection'],
	'blockingCount': int,
	'closedAt': Optional['Time'],
	'confidential': bool,
	'createNoteEmail': Optional[str],
	'createdAt': 'Time',
	'currentUserTodos': 'TodoConnection',
	'customerRelationsContacts': Optional['CustomerRelationsContactConnection'],
	'description': Optional[str],
	'descriptionHtml': Optional[str],
	'designCollection': Optional['DesignCollection'],
	'discussionLocked': bool,
	'discussions': 'DiscussionConnection',
	'downvotes': int,
	'dueDate': Optional['Time'],
	'emailsDisabled': bool,
	'epic': Optional['Epic'],
	'epicIssueId': str,
	'escalationPolicy': Optional['EscalationPolicyType'],
	'escalationStatus': Optional['IssueEscalationStatus'],
	'healthStatus': Optional['HealthStatus'],
	'hidden': Optional[bool],
	'humanTimeEstimate': Optional[str],
	'humanTotalTimeSpent': Optional[str],
	'id': Optional[str],
	'iid': str,
	'iteration': Optional['Iteration'],
	'labels': Optional['LabelConnection'],
	'mergeRequestsCount': int,
	'metricImages': Optional[List['MetricImage']],
	'milestone': Optional['Milestone'],
	'moved': Optional[bool],
	'movedTo': Optional['Issue'],
	'notes': 'NoteConnection',
	'participants': Optional['UserCoreConnection'],
	'projectId': int,
	'reference': str,
	'relationPath': Optional[str],
	'relativePosition': Optional[int],
	'severity': Optional['IssuableSeverity'],
	'slaDueAt': Optional['Time'],
	'state': 'IssueState',
	'statusPagePublishedIncident': Optional[bool],
	'subscribed': bool,
	'taskCompletionStatus': 'TaskCompletionStatus',
	'timeEstimate': int,
	'timelogs': 'TimelogConnection',
	'title': str,
	'titleHtml': Optional[str],
	'totalTimeSpent': int,
	'type': Optional['IssueType'],
	'updatedAt': 'Time',
	'updatedBy': Optional['UserCore'],
	'upvotes': int,
	'userDiscussionsCount': int,
	'userNotesCount': int,
	'userPermissions': 'IssuePermissions',
	'webPath': str,
	'webUrl': str,
	'weight': Optional[int],
})


EpicIssueConnection = TypedDict('EpicIssueConnection', {
	'count': int,
	'edges': Optional[List['EpicIssueEdge']],
	'nodes': Optional[List['EpicIssue']],
	'pageInfo': 'PageInfo',
	'weight': int,
})


EpicIssueEdge = TypedDict('EpicIssueEdge', {
	'cursor': str,
	'node': Optional['EpicIssue'],
})


EpicList = TypedDict('EpicList', {
	'collapsed': Optional[bool],
	'epics': Optional['EpicConnection'],
	'epicsCount': Optional[int],
	'id': 'BoardsEpicListID',
	'label': Optional['Label'],
	'listType': str,
	'metadata': Optional['EpicListMetadata'],
	'position': Optional[int],
	'title': str,
})


EpicListConnection = TypedDict('EpicListConnection', {
	'edges': Optional[List['EpicListEdge']],
	'nodes': Optional[List['EpicList']],
	'pageInfo': 'PageInfo',
})


EpicListEdge = TypedDict('EpicListEdge', {
	'cursor': str,
	'node': Optional['EpicList'],
})


EpicListMetadata = TypedDict('EpicListMetadata', {
	'epicsCount': Optional[int],
})


EpicMoveListPayload = TypedDict('EpicMoveListPayload', {
	'clientMutationId': Optional[str],
	'epic': Optional['Epic'],
	'errors': List[str],
})


EpicPermissions = TypedDict('EpicPermissions', {
	'adminEpic': bool,
	'awardEmoji': bool,
	'createEpic': bool,
	'createNote': bool,
	'destroyEpic': bool,
	'readEpic': bool,
	'readEpicIid': bool,
	'updateEpic': bool,
})


EpicSetSubscriptionPayload = TypedDict('EpicSetSubscriptionPayload', {
	'clientMutationId': Optional[str],
	'epic': Optional['Epic'],
	'errors': List[str],
})


EpicTreeReorderPayload = TypedDict('EpicTreeReorderPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
})


EscalationPolicyCreatePayload = TypedDict('EscalationPolicyCreatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'escalationPolicy': Optional['EscalationPolicyType'],
})


EscalationPolicyDestroyPayload = TypedDict('EscalationPolicyDestroyPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'escalationPolicy': Optional['EscalationPolicyType'],
})


EscalationPolicyType = TypedDict('EscalationPolicyType', {
	'description': Optional[str],
	'id': Optional['IncidentManagementEscalationPolicyID'],
	'name': Optional[str],
	'rules': Optional[List['EscalationRuleType']],
})


EscalationPolicyTypeConnection = TypedDict('EscalationPolicyTypeConnection', {
	'edges': Optional[List['EscalationPolicyTypeEdge']],
	'nodes': Optional[List['EscalationPolicyType']],
	'pageInfo': 'PageInfo',
})


EscalationPolicyTypeEdge = TypedDict('EscalationPolicyTypeEdge', {
	'cursor': str,
	'node': Optional['EscalationPolicyType'],
})


EscalationPolicyUpdatePayload = TypedDict('EscalationPolicyUpdatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'escalationPolicy': Optional['EscalationPolicyType'],
})


EscalationRuleType = TypedDict('EscalationRuleType', {
	'elapsedTimeSeconds': Optional[int],
	'id': Optional['IncidentManagementEscalationRuleID'],
	'oncallSchedule': Optional['IncidentManagementOncallSchedule'],
	'status': Optional['EscalationRuleStatus'],
	'user': Optional['UserCore'],
})


Event = TypedDict('Event', {
	'action': 'EventAction',
	'author': 'UserCore',
	'createdAt': 'Time',
	'id': str,
	'updatedAt': 'Time',
})


EventConnection = TypedDict('EventConnection', {
	'edges': Optional[List['EventEdge']],
	'nodes': Optional[List['Event']],
	'pageInfo': 'PageInfo',
})


EventEdge = TypedDict('EventEdge', {
	'cursor': str,
	'node': Optional['Event'],
})


ExportRequirementsPayload = TypedDict('ExportRequirementsPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
})


ExternalAuditEventDestination = TypedDict('ExternalAuditEventDestination', {
	'destinationUrl': str,
	'group': 'Group',
	'id': str,
	'verificationToken': str,
})


ExternalAuditEventDestinationConnection = TypedDict('ExternalAuditEventDestinationConnection', {
	'edges': Optional[List['ExternalAuditEventDestinationEdge']],
	'nodes': Optional[List['ExternalAuditEventDestination']],
	'pageInfo': 'PageInfo',
})


ExternalAuditEventDestinationCreatePayload = TypedDict('ExternalAuditEventDestinationCreatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'externalAuditEventDestination': Optional['ExternalAuditEventDestination'],
})


ExternalAuditEventDestinationDestroyPayload = TypedDict('ExternalAuditEventDestinationDestroyPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
})


ExternalAuditEventDestinationEdge = TypedDict('ExternalAuditEventDestinationEdge', {
	'cursor': str,
	'node': Optional['ExternalAuditEventDestination'],
})


ExternalAuditEventDestinationUpdatePayload = TypedDict('ExternalAuditEventDestinationUpdatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'externalAuditEventDestination': Optional['ExternalAuditEventDestination'],
})


ExternalIssue = TypedDict('ExternalIssue', {
	'createdAt': Optional['Time'],
	'externalTracker': Optional[str],
	'relativeReference': Optional[str],
	'status': Optional[str],
	'title': Optional[str],
	'updatedAt': Optional['Time'],
	'webUrl': Optional[str],
})


GeoNode = TypedDict('GeoNode', {
	'containerRepositoriesMaxCapacity': Optional[int],
	'enabled': Optional[bool],
	'filesMaxCapacity': Optional[int],
	'groupWikiRepositoryRegistries': Optional['GroupWikiRepositoryRegistryConnection'],
	'id': str,
	'internalUrl': Optional[str],
	'lfsObjectRegistries': Optional['LfsObjectRegistryConnection'],
	'mergeRequestDiffRegistries': Optional['MergeRequestDiffRegistryConnection'],
	'minimumReverificationInterval': Optional[int],
	'name': Optional[str],
	'packageFileRegistries': Optional['PackageFileRegistryConnection'],
	'pagesDeploymentRegistries': Optional['PagesDeploymentRegistryConnection'],
	'pipelineArtifactRegistries': Optional['PipelineArtifactRegistryConnection'],
	'primary': Optional[bool],
	'reposMaxCapacity': Optional[int],
	'selectiveSyncNamespaces': Optional['NamespaceConnection'],
	'selectiveSyncShards': Optional[List[str]],
	'selectiveSyncType': Optional[str],
	'snippetRepositoryRegistries': Optional['SnippetRepositoryRegistryConnection'],
	'syncObjectStorage': Optional[bool],
	'terraformStateVersionRegistries': Optional['TerraformStateVersionRegistryConnection'],
	'uploadRegistries': Optional['UploadRegistryConnection'],
	'url': Optional[str],
	'verificationMaxCapacity': Optional[int],
})


GitlabSubscriptionActivatePayload = TypedDict('GitlabSubscriptionActivatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'license': Optional['CurrentLicense'],
})


GrafanaIntegration = TypedDict('GrafanaIntegration', {
	'createdAt': 'Time',
	'enabled': bool,
	'grafanaUrl': str,
	'id': str,
	'updatedAt': 'Time',
})


Group = TypedDict('Group', {
	'actualRepositorySizeLimit': Optional[float],
	'additionalPurchasedStorageSize': Optional[float],
	'autoDevopsEnabled': Optional[bool],
	'avatarUrl': Optional[str],
	'billableMembersCount': Optional[int],
	'board': Optional['Board'],
	'boards': Optional['BoardConnection'],
	'codeCoverageActivities': Optional['CodeCoverageActivityConnection'],
	'complianceFrameworks': Optional['ComplianceFrameworkConnection'],
	'contacts': Optional['CustomerRelationsContactConnection'],
	'containerRepositories': Optional['ContainerRepositoryConnection'],
	'containerRepositoriesCount': int,
	'containsLockedProjects': bool,
	'crossProjectPipelineAvailable': bool,
	'customEmoji': Optional['CustomEmojiConnection'],
	'dependencyProxyBlobCount': int,
	'dependencyProxyBlobs': Optional['DependencyProxyBlobConnection'],
	'dependencyProxyImageCount': int,
	'dependencyProxyImagePrefix': str,
	'dependencyProxyImageTtlPolicy': Optional['DependencyProxyImageTtlGroupPolicy'],
	'dependencyProxyManifests': Optional['DependencyProxyManifestConnection'],
	'dependencyProxySetting': Optional['DependencyProxySetting'],
	'dependencyProxyTotalSize': str,
	'descendantGroups': Optional['GroupConnection'],
	'description': Optional[str],
	'descriptionHtml': Optional[str],
	'dora': Optional['Dora'],
	'emailsDisabled': Optional[bool],
	'epic': Optional['Epic'],
	'epicBoard': Optional['EpicBoard'],
	'epicBoards': Optional['EpicBoardConnection'],
	'epics': Optional['EpicConnection'],
	'epicsEnabled': Optional[bool],
	'externalAuditEventDestinations': Optional['ExternalAuditEventDestinationConnection'],
	'fullName': str,
	'fullPath': str,
	'groupMembers': Optional['GroupMemberConnection'],
	'id': str,
	'isTemporaryStorageIncreaseEnabled': bool,
	'issues': Optional['IssueConnection'],
	'iterationCadences': Optional['IterationCadenceConnection'],
	'iterations': Optional['IterationConnection'],
	'label': Optional['Label'],
	'labels': Optional['LabelConnection'],
	'lfsEnabled': Optional[bool],
	'mentionsDisabled': Optional[bool],
	'mergeRequestViolations': Optional['ComplianceViolationConnection'],
	'mergeRequests': Optional['MergeRequestConnection'],
	'milestones': Optional['MilestoneConnection'],
	'name': str,
	'organizations': Optional['CustomerRelationsOrganizationConnection'],
	'packageSettings': Optional['PackageSettings'],
	'packages': Optional['PackageConnection'],
	'parent': Optional['Group'],
	'path': str,
	'projectCreationLevel': Optional[str],
	'projects': 'ProjectConnection',
	'recentIssueBoards': Optional['BoardConnection'],
	'repositorySizeExcessProjectCount': int,
	'requestAccessEnabled': Optional[bool],
	'requireTwoFactorAuthentication': Optional[bool],
	'rootStorageStatistics': Optional['RootStorageStatistics'],
	'runners': Optional['CiRunnerConnection'],
	'shareWithGroupLock': Optional[bool],
	'sharedRunnersSetting': Optional['SharedRunnersSetting'],
	'stats': Optional['GroupStats'],
	'storageSizeLimit': Optional[float],
	'subgroupCreationLevel': Optional[str],
	'temporaryStorageIncreaseEndsOn': Optional['Time'],
	'timelogs': 'TimelogConnection',
	'totalRepositorySize': Optional[float],
	'totalRepositorySizeExcess': Optional[float],
	'twoFactorGracePeriod': Optional[int],
	'userPermissions': 'GroupPermissions',
	'visibility': Optional[str],
	'vulnerabilities': Optional['VulnerabilityConnection'],
	'vulnerabilitiesCountByDay': Optional['VulnerabilitiesCountByDayConnection'],
	'vulnerabilityGrades': List['VulnerableProjectsByGrade'],
	'vulnerabilityScanners': Optional['VulnerabilityScannerConnection'],
	'vulnerabilitySeveritiesCount': Optional['VulnerabilitySeveritiesCount'],
	'webUrl': str,
	'workItemTypes': Optional['WorkItemTypeConnection'],
})


GroupConnection = TypedDict('GroupConnection', {
	'edges': Optional[List['GroupEdge']],
	'nodes': Optional[List['Group']],
	'pageInfo': 'PageInfo',
})


GroupEdge = TypedDict('GroupEdge', {
	'cursor': str,
	'node': Optional['Group'],
})


GroupMember = TypedDict('GroupMember', {
	'accessLevel': Optional['AccessLevel'],
	'createdAt': Optional['Time'],
	'createdBy': Optional['UserCore'],
	'expiresAt': Optional['Time'],
	'group': Optional['Group'],
	'id': str,
	'mergeRequestInteraction': Optional['UserMergeRequestInteraction'],
	'notificationEmail': Optional[str],
	'updatedAt': Optional['Time'],
	'user': Optional['UserCore'],
	'userPermissions': 'GroupPermissions',
})


GroupMemberConnection = TypedDict('GroupMemberConnection', {
	'edges': Optional[List['GroupMemberEdge']],
	'nodes': Optional[List['GroupMember']],
	'pageInfo': 'PageInfo',
})


GroupMemberEdge = TypedDict('GroupMemberEdge', {
	'cursor': str,
	'node': Optional['GroupMember'],
})


GroupPermissions = TypedDict('GroupPermissions', {
	'createProjects': bool,
	'readGroup': bool,
})


GroupReleaseStats = TypedDict('GroupReleaseStats', {
	'releasesCount': Optional[int],
	'releasesPercentage': Optional[int],
})


GroupStats = TypedDict('GroupStats', {
	'releaseStats': Optional['GroupReleaseStats'],
})


GroupUpdatePayload = TypedDict('GroupUpdatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'group': Optional['Group'],
})


GroupWikiRepositoryRegistry = TypedDict('GroupWikiRepositoryRegistry', {
	'createdAt': Optional['Time'],
	'groupWikiRepositoryId': str,
	'id': str,
	'lastSyncFailure': Optional[str],
	'lastSyncedAt': Optional['Time'],
	'retryAt': Optional['Time'],
	'retryCount': Optional[int],
	'state': Optional['RegistryState'],
})


GroupWikiRepositoryRegistryConnection = TypedDict('GroupWikiRepositoryRegistryConnection', {
	'edges': Optional[List['GroupWikiRepositoryRegistryEdge']],
	'nodes': Optional[List['GroupWikiRepositoryRegistry']],
	'pageInfo': 'PageInfo',
})


GroupWikiRepositoryRegistryEdge = TypedDict('GroupWikiRepositoryRegistryEdge', {
	'cursor': str,
	'node': Optional['GroupWikiRepositoryRegistry'],
})


HelmFileMetadata = TypedDict('HelmFileMetadata', {
	'channel': str,
	'createdAt': 'Time',
	'metadata': 'PackageHelmMetadataType',
	'updatedAt': 'Time',
})


HttpIntegrationCreatePayload = TypedDict('HttpIntegrationCreatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'integration': Optional['AlertManagementHttpIntegration'],
})


HttpIntegrationDestroyPayload = TypedDict('HttpIntegrationDestroyPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'integration': Optional['AlertManagementHttpIntegration'],
})


HttpIntegrationResetTokenPayload = TypedDict('HttpIntegrationResetTokenPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'integration': Optional['AlertManagementHttpIntegration'],
})


HttpIntegrationUpdatePayload = TypedDict('HttpIntegrationUpdatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'integration': Optional['AlertManagementHttpIntegration'],
})


IncidentManagementOncallRotation = TypedDict('IncidentManagementOncallRotation', {
	'activePeriod': Optional['OncallRotationActivePeriodType'],
	'endsAt': Optional['Time'],
	'id': 'IncidentManagementOncallRotationID',
	'length': Optional[int],
	'lengthUnit': Optional['OncallRotationUnitEnum'],
	'name': str,
	'participants': Optional['OncallParticipantTypeConnection'],
	'shifts': Optional['IncidentManagementOncallShiftConnection'],
	'startsAt': Optional['Time'],
})


IncidentManagementOncallRotationConnection = TypedDict('IncidentManagementOncallRotationConnection', {
	'edges': Optional[List['IncidentManagementOncallRotationEdge']],
	'nodes': Optional[List['IncidentManagementOncallRotation']],
	'pageInfo': 'PageInfo',
})


IncidentManagementOncallRotationEdge = TypedDict('IncidentManagementOncallRotationEdge', {
	'cursor': str,
	'node': Optional['IncidentManagementOncallRotation'],
})


IncidentManagementOncallSchedule = TypedDict('IncidentManagementOncallSchedule', {
	'description': Optional[str],
	'iid': str,
	'name': str,
	'oncallUsers': Optional[List['UserCore']],
	'rotation': Optional['IncidentManagementOncallRotation'],
	'rotations': 'IncidentManagementOncallRotationConnection',
	'timezone': str,
})


IncidentManagementOncallScheduleConnection = TypedDict('IncidentManagementOncallScheduleConnection', {
	'edges': Optional[List['IncidentManagementOncallScheduleEdge']],
	'nodes': Optional[List['IncidentManagementOncallSchedule']],
	'pageInfo': 'PageInfo',
})


IncidentManagementOncallScheduleEdge = TypedDict('IncidentManagementOncallScheduleEdge', {
	'cursor': str,
	'node': Optional['IncidentManagementOncallSchedule'],
})


IncidentManagementOncallShift = TypedDict('IncidentManagementOncallShift', {
	'endsAt': Optional['Time'],
	'participant': Optional['OncallParticipantType'],
	'startsAt': Optional['Time'],
})


IncidentManagementOncallShiftConnection = TypedDict('IncidentManagementOncallShiftConnection', {
	'edges': Optional[List['IncidentManagementOncallShiftEdge']],
	'nodes': Optional[List['IncidentManagementOncallShift']],
	'pageInfo': 'PageInfo',
})


IncidentManagementOncallShiftEdge = TypedDict('IncidentManagementOncallShiftEdge', {
	'cursor': str,
	'node': Optional['IncidentManagementOncallShift'],
})


InstanceSecurityDashboard = TypedDict('InstanceSecurityDashboard', {
	'projects': 'ProjectConnection',
	'vulnerabilityGrades': List['VulnerableProjectsByGrade'],
	'vulnerabilityScanners': Optional['VulnerabilityScannerConnection'],
	'vulnerabilitySeveritiesCount': Optional['VulnerabilitySeveritiesCount'],
})


Issue = TypedDict('Issue', {
	'alertManagementAlert': Optional['AlertManagementAlert'],
	'assignees': Optional['UserCoreConnection'],
	'author': 'UserCore',
	'blocked': bool,
	'blockedByCount': Optional[int],
	'blockedByIssues': Optional['IssueConnection'],
	'blockingCount': int,
	'closedAt': Optional['Time'],
	'confidential': bool,
	'createNoteEmail': Optional[str],
	'createdAt': 'Time',
	'currentUserTodos': 'TodoConnection',
	'customerRelationsContacts': Optional['CustomerRelationsContactConnection'],
	'description': Optional[str],
	'descriptionHtml': Optional[str],
	'designCollection': Optional['DesignCollection'],
	'discussionLocked': bool,
	'discussions': 'DiscussionConnection',
	'downvotes': int,
	'dueDate': Optional['Time'],
	'emailsDisabled': bool,
	'epic': Optional['Epic'],
	'escalationPolicy': Optional['EscalationPolicyType'],
	'escalationStatus': Optional['IssueEscalationStatus'],
	'healthStatus': Optional['HealthStatus'],
	'hidden': Optional[bool],
	'humanTimeEstimate': Optional[str],
	'humanTotalTimeSpent': Optional[str],
	'id': str,
	'iid': str,
	'iteration': Optional['Iteration'],
	'labels': Optional['LabelConnection'],
	'mergeRequestsCount': int,
	'metricImages': Optional[List['MetricImage']],
	'milestone': Optional['Milestone'],
	'moved': Optional[bool],
	'movedTo': Optional['Issue'],
	'notes': 'NoteConnection',
	'participants': Optional['UserCoreConnection'],
	'projectId': int,
	'reference': str,
	'relativePosition': Optional[int],
	'severity': Optional['IssuableSeverity'],
	'slaDueAt': Optional['Time'],
	'state': 'IssueState',
	'statusPagePublishedIncident': Optional[bool],
	'subscribed': bool,
	'taskCompletionStatus': 'TaskCompletionStatus',
	'timeEstimate': int,
	'timelogs': 'TimelogConnection',
	'title': str,
	'titleHtml': Optional[str],
	'totalTimeSpent': int,
	'type': Optional['IssueType'],
	'updatedAt': 'Time',
	'updatedBy': Optional['UserCore'],
	'upvotes': int,
	'userDiscussionsCount': int,
	'userNotesCount': int,
	'userPermissions': 'IssuePermissions',
	'webPath': str,
	'webUrl': str,
	'weight': Optional[int],
})


IssueConnection = TypedDict('IssueConnection', {
	'count': int,
	'edges': Optional[List['IssueEdge']],
	'nodes': Optional[List['Issue']],
	'pageInfo': 'PageInfo',
	'weight': int,
})


IssueEdge = TypedDict('IssueEdge', {
	'cursor': str,
	'node': Optional['Issue'],
})


IssueMoveListPayload = TypedDict('IssueMoveListPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'issue': Optional['Issue'],
})


IssueMovePayload = TypedDict('IssueMovePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'issue': Optional['Issue'],
})


IssuePermissions = TypedDict('IssuePermissions', {
	'adminIssue': bool,
	'createDesign': bool,
	'createNote': bool,
	'destroyDesign': bool,
	'readDesign': bool,
	'readIssue': bool,
	'reopenIssue': bool,
	'updateIssue': bool,
})


IssueSetAssigneesPayload = TypedDict('IssueSetAssigneesPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'issue': Optional['Issue'],
})


IssueSetConfidentialPayload = TypedDict('IssueSetConfidentialPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'issue': Optional['Issue'],
})


IssueSetCrmContactsPayload = TypedDict('IssueSetCrmContactsPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'issue': Optional['Issue'],
})


IssueSetDueDatePayload = TypedDict('IssueSetDueDatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'issue': Optional['Issue'],
})


IssueSetEpicPayload = TypedDict('IssueSetEpicPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'issue': Optional['Issue'],
})


IssueSetEscalationPolicyPayload = TypedDict('IssueSetEscalationPolicyPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'issue': Optional['Issue'],
})


IssueSetEscalationStatusPayload = TypedDict('IssueSetEscalationStatusPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'issue': Optional['Issue'],
})


IssueSetIterationPayload = TypedDict('IssueSetIterationPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'issue': Optional['Issue'],
})


IssueSetLockedPayload = TypedDict('IssueSetLockedPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'issue': Optional['Issue'],
})


IssueSetSeverityPayload = TypedDict('IssueSetSeverityPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'issue': Optional['Issue'],
})


IssueSetSubscriptionPayload = TypedDict('IssueSetSubscriptionPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'issue': Optional['Issue'],
})


IssueSetWeightPayload = TypedDict('IssueSetWeightPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'issue': Optional['Issue'],
})


IssueStatusCountsType = TypedDict('IssueStatusCountsType', {
	'all': Optional[int],
	'closed': Optional[int],
	'opened': Optional[int],
})


Iteration = TypedDict('Iteration', {
	'createdAt': 'Time',
	'description': Optional[str],
	'descriptionHtml': Optional[str],
	'dueDate': Optional['Time'],
	'id': str,
	'iid': str,
	'iterationCadence': 'IterationCadence',
	'report': Optional['TimeboxReport'],
	'scopedPath': Optional[str],
	'scopedUrl': Optional[str],
	'sequence': int,
	'startDate': Optional['Time'],
	'state': 'IterationState',
	'title': Optional[str],
	'updatedAt': 'Time',
	'webPath': str,
	'webUrl': str,
})


IterationCadence = TypedDict('IterationCadence', {
	'active': Optional[bool],
	'automatic': Optional[bool],
	'description': Optional[str],
	'durationInWeeks': Optional[int],
	'id': 'IterationsCadenceID',
	'iterationsInAdvance': Optional[int],
	'rollOver': bool,
	'startDate': Optional['Time'],
	'title': str,
})


IterationCadenceConnection = TypedDict('IterationCadenceConnection', {
	'edges': Optional[List['IterationCadenceEdge']],
	'nodes': Optional[List['IterationCadence']],
	'pageInfo': 'PageInfo',
})


IterationCadenceCreatePayload = TypedDict('IterationCadenceCreatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'iterationCadence': Optional['IterationCadence'],
})


IterationCadenceDestroyPayload = TypedDict('IterationCadenceDestroyPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'group': 'Group',
})


IterationCadenceEdge = TypedDict('IterationCadenceEdge', {
	'cursor': str,
	'node': Optional['IterationCadence'],
})


IterationCadenceUpdatePayload = TypedDict('IterationCadenceUpdatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'iterationCadence': Optional['IterationCadence'],
})


IterationConnection = TypedDict('IterationConnection', {
	'edges': Optional[List['IterationEdge']],
	'nodes': Optional[List['Iteration']],
	'pageInfo': 'PageInfo',
})


IterationDeletePayload = TypedDict('IterationDeletePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'group': 'Group',
})


IterationEdge = TypedDict('IterationEdge', {
	'cursor': str,
	'node': Optional['Iteration'],
})


JiraImport = TypedDict('JiraImport', {
	'createdAt': Optional['Time'],
	'failedToImportCount': int,
	'importedIssuesCount': int,
	'jiraProjectKey': str,
	'scheduledAt': Optional['Time'],
	'scheduledBy': Optional['UserCore'],
	'totalIssueCount': int,
})


JiraImportConnection = TypedDict('JiraImportConnection', {
	'edges': Optional[List['JiraImportEdge']],
	'nodes': Optional[List['JiraImport']],
	'pageInfo': 'PageInfo',
})


JiraImportEdge = TypedDict('JiraImportEdge', {
	'cursor': str,
	'node': Optional['JiraImport'],
})


JiraImportStartPayload = TypedDict('JiraImportStartPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'jiraImport': Optional['JiraImport'],
})


JiraImportUsersPayload = TypedDict('JiraImportUsersPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'jiraUsers': Optional[List['JiraUser']],
})


JiraProject = TypedDict('JiraProject', {
	'key': str,
	'name': Optional[str],
	'projectId': int,
})


JiraProjectConnection = TypedDict('JiraProjectConnection', {
	'edges': Optional[List['JiraProjectEdge']],
	'nodes': Optional[List['JiraProject']],
	'pageInfo': 'PageInfo',
})


JiraProjectEdge = TypedDict('JiraProjectEdge', {
	'cursor': str,
	'node': Optional['JiraProject'],
})


JiraService = TypedDict('JiraService', {
	'active': Optional[bool],
	'projects': Optional['JiraProjectConnection'],
	'serviceType': Optional['ServiceType'],
	'type': Optional[str],
})


JiraUser = TypedDict('JiraUser', {
	'gitlabId': Optional[int],
	'gitlabName': Optional[str],
	'gitlabUsername': Optional[str],
	'jiraAccountId': str,
	'jiraDisplayName': str,
	'jiraEmail': Optional[str],
})


JobCancelPayload = TypedDict('JobCancelPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'job': Optional['CiJob'],
})


JobNeedUnionConnection = TypedDict('JobNeedUnionConnection', {
	'edges': Optional[List['JobNeedUnionEdge']],
	'nodes': Optional[List['JobNeedUnion']],
	'pageInfo': 'PageInfo',
})


JobNeedUnionEdge = TypedDict('JobNeedUnionEdge', {
	'cursor': str,
	'node': Optional['JobNeedUnion'],
})


JobPermissions = TypedDict('JobPermissions', {
	'readBuild': bool,
	'readJobArtifacts': bool,
	'updateBuild': bool,
})


JobPlayPayload = TypedDict('JobPlayPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'job': Optional['CiJob'],
})


JobRetryPayload = TypedDict('JobRetryPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'job': Optional['CiJob'],
})


JobUnschedulePayload = TypedDict('JobUnschedulePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'job': Optional['CiJob'],
})


Kas = TypedDict('Kas', {
	'enabled': bool,
	'externalUrl': Optional[str],
	'version': Optional[str],
})


Label = TypedDict('Label', {
	'color': str,
	'createdAt': 'Time',
	'description': Optional[str],
	'descriptionHtml': Optional[str],
	'id': str,
	'textColor': str,
	'title': str,
	'updatedAt': 'Time',
})


LabelConnection = TypedDict('LabelConnection', {
	'count': int,
	'edges': Optional[List['LabelEdge']],
	'nodes': Optional[List['Label']],
	'pageInfo': 'PageInfo',
})


LabelCreatePayload = TypedDict('LabelCreatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'label': Optional['Label'],
})


LabelEdge = TypedDict('LabelEdge', {
	'cursor': str,
	'node': Optional['Label'],
})


LfsObjectRegistry = TypedDict('LfsObjectRegistry', {
	'createdAt': Optional['Time'],
	'id': str,
	'lastSyncFailure': Optional[str],
	'lastSyncedAt': Optional['Time'],
	'lfsObjectId': str,
	'retryAt': Optional['Time'],
	'retryCount': Optional[int],
	'state': Optional['RegistryState'],
})


LfsObjectRegistryConnection = TypedDict('LfsObjectRegistryConnection', {
	'edges': Optional[List['LfsObjectRegistryEdge']],
	'nodes': Optional[List['LfsObjectRegistry']],
	'pageInfo': 'PageInfo',
})


LfsObjectRegistryEdge = TypedDict('LfsObjectRegistryEdge', {
	'cursor': str,
	'node': Optional['LfsObjectRegistry'],
})


LicenseHistoryEntry = TypedDict('LicenseHistoryEntry', {
	'activatedAt': Optional['Date'],
	'blockChangesAt': Optional['Date'],
	'company': Optional[str],
	'createdAt': Optional['Date'],
	'email': Optional[str],
	'expiresAt': Optional['Date'],
	'id': str,
	'name': Optional[str],
	'plan': str,
	'startsAt': Optional['Date'],
	'type': str,
	'usersInLicenseCount': Optional[int],
})


LicenseHistoryEntryConnection = TypedDict('LicenseHistoryEntryConnection', {
	'edges': Optional[List['LicenseHistoryEntryEdge']],
	'nodes': Optional[List['LicenseHistoryEntry']],
	'pageInfo': 'PageInfo',
})


LicenseHistoryEntryEdge = TypedDict('LicenseHistoryEntryEdge', {
	'cursor': str,
	'node': Optional['LicenseHistoryEntry'],
})


MarkAsSpamSnippetPayload = TypedDict('MarkAsSpamSnippetPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'snippet': Optional['Snippet'],
})


MavenMetadata = TypedDict('MavenMetadata', {
	'appGroup': str,
	'appName': str,
	'appVersion': Optional[str],
	'createdAt': 'Time',
	'id': 'PackagesMavenMetadatumID',
	'path': str,
	'updatedAt': 'Time',
})


MemberInterfaceConnection = TypedDict('MemberInterfaceConnection', {
	'edges': Optional[List['MemberInterfaceEdge']],
	'nodes': Optional[List['MemberInterface']],
	'pageInfo': 'PageInfo',
})


MemberInterfaceEdge = TypedDict('MemberInterfaceEdge', {
	'cursor': str,
	'node': Optional['MemberInterface'],
})


MergeRequest = TypedDict('MergeRequest', {
	'allowCollaboration': Optional[bool],
	'approvalState': 'MergeRequestApprovalState',
	'approvalsLeft': Optional[int],
	'approvalsRequired': Optional[int],
	'approved': bool,
	'approvedBy': Optional['UserCoreConnection'],
	'assignees': Optional['MergeRequestAssigneeConnection'],
	'author': Optional['MergeRequestAuthor'],
	'autoMergeEnabled': bool,
	'autoMergeStrategy': Optional[str],
	'availableAutoMergeStrategies': Optional[List[str]],
	'commitCount': Optional[int],
	'commits': Optional['CommitConnection'],
	'commitsWithoutMergeCommits': Optional['CommitConnection'],
	'committers': Optional['UserCoreConnection'],
	'conflicts': bool,
	'createdAt': 'Time',
	'currentUserTodos': 'TodoConnection',
	'defaultMergeCommitMessage': Optional[str],
	'defaultMergeCommitMessageWithDescription': Optional[str],
	'defaultSquashCommitMessage': Optional[str],
	'description': Optional[str],
	'descriptionHtml': Optional[str],
	'diffHeadSha': Optional[str],
	'diffRefs': Optional['DiffRefs'],
	'diffStats': Optional[List['DiffStats']],
	'diffStatsSummary': Optional['DiffStatsSummary'],
	'discussionLocked': bool,
	'discussions': 'DiscussionConnection',
	'divergedFromTargetBranch': bool,
	'downvotes': int,
	'draft': bool,
	'forceRemoveSourceBranch': Optional[bool],
	'hasCi': bool,
	'hasSecurityReports': bool,
	'headPipeline': Optional['Pipeline'],
	'humanTimeEstimate': Optional[str],
	'humanTotalTimeSpent': Optional[str],
	'id': str,
	'iid': str,
	'inProgressMergeCommitSha': Optional[str],
	'labels': Optional['LabelConnection'],
	'mergeCommitSha': Optional[str],
	'mergeError': Optional[str],
	'mergeOngoing': bool,
	'mergeStatus': Optional[str],
	'mergeStatusEnum': Optional['MergeStatus'],
	'mergeTrainsCount': Optional[int],
	'mergeUser': Optional['UserCore'],
	'mergeWhenPipelineSucceeds': Optional[bool],
	'mergeable': bool,
	'mergeableDiscussionsState': Optional[bool],
	'mergedAt': Optional['Time'],
	'milestone': Optional['Milestone'],
	'notes': 'NoteConnection',
	'participants': Optional['MergeRequestParticipantConnection'],
	'pipelines': Optional['PipelineConnection'],
	'project': 'Project',
	'projectId': int,
	'rebaseCommitSha': Optional[str],
	'rebaseInProgress': bool,
	'reference': str,
	'reviewers': Optional['MergeRequestReviewerConnection'],
	'securityAutoFix': Optional[bool],
	'securityReportsUpToDateOnTargetBranch': bool,
	'shouldBeRebased': bool,
	'shouldRemoveSourceBranch': Optional[bool],
	'sourceBranch': str,
	'sourceBranchExists': bool,
	'sourceBranchProtected': bool,
	'sourceProject': Optional['Project'],
	'sourceProjectId': Optional[int],
	'squash': bool,
	'squashOnMerge': bool,
	'state': 'MergeRequestState',
	'subscribed': bool,
	'targetBranch': str,
	'targetBranchExists': bool,
	'targetProject': 'Project',
	'targetProjectId': int,
	'taskCompletionStatus': 'TaskCompletionStatus',
	'timeEstimate': int,
	'timelogs': 'TimelogConnection',
	'title': str,
	'titleHtml': Optional[str],
	'totalTimeSpent': int,
	'updatedAt': 'Time',
	'upvotes': int,
	'userDiscussionsCount': Optional[int],
	'userNotesCount': Optional[int],
	'userPermissions': 'MergeRequestPermissions',
	'webUrl': Optional[str],
})


MergeRequestAcceptPayload = TypedDict('MergeRequestAcceptPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'mergeRequest': Optional['MergeRequest'],
})


MergeRequestApprovalState = TypedDict('MergeRequestApprovalState', {
	'approvalRulesOverwritten': Optional[bool],
	'rules': Optional[List['ApprovalRule']],
})


MergeRequestAssignee = TypedDict('MergeRequestAssignee', {
	'assignedMergeRequests': Optional['MergeRequestConnection'],
	'authoredMergeRequests': Optional['MergeRequestConnection'],
	'avatarUrl': Optional[str],
	'bot': bool,
	'callouts': Optional['UserCalloutConnection'],
	'email': Optional[str],
	'gitpodEnabled': Optional[bool],
	'groupCount': Optional[int],
	'groupMemberships': Optional['GroupMemberConnection'],
	'groups': Optional['GroupConnection'],
	'id': str,
	'location': Optional[str],
	'mergeRequestInteraction': Optional['UserMergeRequestInteraction'],
	'name': str,
	'namespace': Optional['Namespace'],
	'preferencesGitpodPath': Optional[str],
	'profileEnableGitpodPath': Optional[str],
	'projectMemberships': Optional['ProjectMemberConnection'],
	'publicEmail': Optional[str],
	'reviewRequestedMergeRequests': Optional['MergeRequestConnection'],
	'savedReplies': Optional['SavedReplyConnection'],
	'snippets': Optional['SnippetConnection'],
	'starredProjects': Optional['ProjectConnection'],
	'state': 'UserState',
	'status': Optional['UserStatus'],
	'timelogs': Optional['TimelogConnection'],
	'todos': Optional['TodoConnection'],
	'userPermissions': 'UserPermissions',
	'username': str,
	'webPath': str,
	'webUrl': str,
})


MergeRequestAssigneeConnection = TypedDict('MergeRequestAssigneeConnection', {
	'edges': Optional[List['MergeRequestAssigneeEdge']],
	'nodes': Optional[List['MergeRequestAssignee']],
	'pageInfo': 'PageInfo',
})


MergeRequestAssigneeEdge = TypedDict('MergeRequestAssigneeEdge', {
	'cursor': str,
	'node': Optional['MergeRequestAssignee'],
})


MergeRequestAuthor = TypedDict('MergeRequestAuthor', {
	'assignedMergeRequests': Optional['MergeRequestConnection'],
	'authoredMergeRequests': Optional['MergeRequestConnection'],
	'avatarUrl': Optional[str],
	'bot': bool,
	'callouts': Optional['UserCalloutConnection'],
	'email': Optional[str],
	'gitpodEnabled': Optional[bool],
	'groupCount': Optional[int],
	'groupMemberships': Optional['GroupMemberConnection'],
	'groups': Optional['GroupConnection'],
	'id': str,
	'location': Optional[str],
	'mergeRequestInteraction': Optional['UserMergeRequestInteraction'],
	'name': str,
	'namespace': Optional['Namespace'],
	'preferencesGitpodPath': Optional[str],
	'profileEnableGitpodPath': Optional[str],
	'projectMemberships': Optional['ProjectMemberConnection'],
	'publicEmail': Optional[str],
	'reviewRequestedMergeRequests': Optional['MergeRequestConnection'],
	'savedReplies': Optional['SavedReplyConnection'],
	'snippets': Optional['SnippetConnection'],
	'starredProjects': Optional['ProjectConnection'],
	'state': 'UserState',
	'status': Optional['UserStatus'],
	'timelogs': Optional['TimelogConnection'],
	'todos': Optional['TodoConnection'],
	'userPermissions': 'UserPermissions',
	'username': str,
	'webPath': str,
	'webUrl': str,
})


MergeRequestConnection = TypedDict('MergeRequestConnection', {
	'count': int,
	'edges': Optional[List['MergeRequestEdge']],
	'nodes': Optional[List['MergeRequest']],
	'pageInfo': 'PageInfo',
	'totalTimeToMerge': Optional[float],
})


MergeRequestCreatePayload = TypedDict('MergeRequestCreatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'mergeRequest': Optional['MergeRequest'],
})


MergeRequestDiffRegistry = TypedDict('MergeRequestDiffRegistry', {
	'createdAt': Optional['Time'],
	'id': str,
	'lastSyncFailure': Optional[str],
	'lastSyncedAt': Optional['Time'],
	'mergeRequestDiffId': str,
	'retryAt': Optional['Time'],
	'retryCount': Optional[int],
	'state': Optional['RegistryState'],
})


MergeRequestDiffRegistryConnection = TypedDict('MergeRequestDiffRegistryConnection', {
	'edges': Optional[List['MergeRequestDiffRegistryEdge']],
	'nodes': Optional[List['MergeRequestDiffRegistry']],
	'pageInfo': 'PageInfo',
})


MergeRequestDiffRegistryEdge = TypedDict('MergeRequestDiffRegistryEdge', {
	'cursor': str,
	'node': Optional['MergeRequestDiffRegistry'],
})


MergeRequestEdge = TypedDict('MergeRequestEdge', {
	'cursor': str,
	'node': Optional['MergeRequest'],
})


MergeRequestParticipant = TypedDict('MergeRequestParticipant', {
	'assignedMergeRequests': Optional['MergeRequestConnection'],
	'authoredMergeRequests': Optional['MergeRequestConnection'],
	'avatarUrl': Optional[str],
	'bot': bool,
	'callouts': Optional['UserCalloutConnection'],
	'email': Optional[str],
	'gitpodEnabled': Optional[bool],
	'groupCount': Optional[int],
	'groupMemberships': Optional['GroupMemberConnection'],
	'groups': Optional['GroupConnection'],
	'id': str,
	'location': Optional[str],
	'mergeRequestInteraction': Optional['UserMergeRequestInteraction'],
	'name': str,
	'namespace': Optional['Namespace'],
	'preferencesGitpodPath': Optional[str],
	'profileEnableGitpodPath': Optional[str],
	'projectMemberships': Optional['ProjectMemberConnection'],
	'publicEmail': Optional[str],
	'reviewRequestedMergeRequests': Optional['MergeRequestConnection'],
	'savedReplies': Optional['SavedReplyConnection'],
	'snippets': Optional['SnippetConnection'],
	'starredProjects': Optional['ProjectConnection'],
	'state': 'UserState',
	'status': Optional['UserStatus'],
	'timelogs': Optional['TimelogConnection'],
	'todos': Optional['TodoConnection'],
	'userPermissions': 'UserPermissions',
	'username': str,
	'webPath': str,
	'webUrl': str,
})


MergeRequestParticipantConnection = TypedDict('MergeRequestParticipantConnection', {
	'edges': Optional[List['MergeRequestParticipantEdge']],
	'nodes': Optional[List['MergeRequestParticipant']],
	'pageInfo': 'PageInfo',
})


MergeRequestParticipantEdge = TypedDict('MergeRequestParticipantEdge', {
	'cursor': str,
	'node': Optional['MergeRequestParticipant'],
})


MergeRequestPermissions = TypedDict('MergeRequestPermissions', {
	'adminMergeRequest': bool,
	'canMerge': bool,
	'cherryPickOnCurrentMergeRequest': bool,
	'createNote': bool,
	'pushToSourceBranch': bool,
	'readMergeRequest': bool,
	'removeSourceBranch': bool,
	'revertOnCurrentMergeRequest': bool,
	'updateMergeRequest': bool,
})


MergeRequestReviewer = TypedDict('MergeRequestReviewer', {
	'assignedMergeRequests': Optional['MergeRequestConnection'],
	'authoredMergeRequests': Optional['MergeRequestConnection'],
	'avatarUrl': Optional[str],
	'bot': bool,
	'callouts': Optional['UserCalloutConnection'],
	'email': Optional[str],
	'gitpodEnabled': Optional[bool],
	'groupCount': Optional[int],
	'groupMemberships': Optional['GroupMemberConnection'],
	'groups': Optional['GroupConnection'],
	'id': str,
	'location': Optional[str],
	'mergeRequestInteraction': Optional['UserMergeRequestInteraction'],
	'name': str,
	'namespace': Optional['Namespace'],
	'preferencesGitpodPath': Optional[str],
	'profileEnableGitpodPath': Optional[str],
	'projectMemberships': Optional['ProjectMemberConnection'],
	'publicEmail': Optional[str],
	'reviewRequestedMergeRequests': Optional['MergeRequestConnection'],
	'savedReplies': Optional['SavedReplyConnection'],
	'snippets': Optional['SnippetConnection'],
	'starredProjects': Optional['ProjectConnection'],
	'state': 'UserState',
	'status': Optional['UserStatus'],
	'timelogs': Optional['TimelogConnection'],
	'todos': Optional['TodoConnection'],
	'userPermissions': 'UserPermissions',
	'username': str,
	'webPath': str,
	'webUrl': str,
})


MergeRequestReviewerConnection = TypedDict('MergeRequestReviewerConnection', {
	'edges': Optional[List['MergeRequestReviewerEdge']],
	'nodes': Optional[List['MergeRequestReviewer']],
	'pageInfo': 'PageInfo',
})


MergeRequestReviewerEdge = TypedDict('MergeRequestReviewerEdge', {
	'cursor': str,
	'node': Optional['MergeRequestReviewer'],
})


MergeRequestReviewerRereviewPayload = TypedDict('MergeRequestReviewerRereviewPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'mergeRequest': Optional['MergeRequest'],
})


MergeRequestSetAssigneesPayload = TypedDict('MergeRequestSetAssigneesPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'mergeRequest': Optional['MergeRequest'],
})


MergeRequestSetDraftPayload = TypedDict('MergeRequestSetDraftPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'mergeRequest': Optional['MergeRequest'],
})


MergeRequestSetLabelsPayload = TypedDict('MergeRequestSetLabelsPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'mergeRequest': Optional['MergeRequest'],
})


MergeRequestSetLockedPayload = TypedDict('MergeRequestSetLockedPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'mergeRequest': Optional['MergeRequest'],
})


MergeRequestSetMilestonePayload = TypedDict('MergeRequestSetMilestonePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'mergeRequest': Optional['MergeRequest'],
})


MergeRequestSetSubscriptionPayload = TypedDict('MergeRequestSetSubscriptionPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'mergeRequest': Optional['MergeRequest'],
})


MergeRequestUpdatePayload = TypedDict('MergeRequestUpdatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'mergeRequest': Optional['MergeRequest'],
})


Metadata = TypedDict('Metadata', {
	'kas': 'Kas',
	'revision': str,
	'version': str,
})


MetricImage = TypedDict('MetricImage', {
	'fileName': Optional[str],
	'filePath': Optional[str],
	'id': str,
	'iid': str,
	'url': str,
})


MetricsDashboard = TypedDict('MetricsDashboard', {
	'annotations': Optional['MetricsDashboardAnnotationConnection'],
	'path': Optional[str],
	'schemaValidationWarnings': Optional[List[str]],
})


MetricsDashboardAnnotation = TypedDict('MetricsDashboardAnnotation', {
	'description': Optional[str],
	'endingAt': Optional['Time'],
	'id': str,
	'panelId': Optional[str],
	'startingAt': Optional['Time'],
})


MetricsDashboardAnnotationConnection = TypedDict('MetricsDashboardAnnotationConnection', {
	'edges': Optional[List['MetricsDashboardAnnotationEdge']],
	'nodes': Optional[List['MetricsDashboardAnnotation']],
	'pageInfo': 'PageInfo',
})


MetricsDashboardAnnotationEdge = TypedDict('MetricsDashboardAnnotationEdge', {
	'cursor': str,
	'node': Optional['MetricsDashboardAnnotation'],
})


Milestone = TypedDict('Milestone', {
	'createdAt': 'Time',
	'description': Optional[str],
	'dueDate': Optional['Time'],
	'expired': bool,
	'groupMilestone': bool,
	'id': str,
	'iid': str,
	'projectMilestone': bool,
	'report': Optional['TimeboxReport'],
	'startDate': Optional['Time'],
	'state': 'MilestoneStateEnum',
	'stats': Optional['MilestoneStats'],
	'subgroupMilestone': bool,
	'title': str,
	'updatedAt': 'Time',
	'webPath': str,
})


MilestoneConnection = TypedDict('MilestoneConnection', {
	'edges': Optional[List['MilestoneEdge']],
	'nodes': Optional[List['Milestone']],
	'pageInfo': 'PageInfo',
})


MilestoneEdge = TypedDict('MilestoneEdge', {
	'cursor': str,
	'node': Optional['Milestone'],
})


MilestoneStats = TypedDict('MilestoneStats', {
	'closedIssuesCount': Optional[int],
	'totalIssuesCount': Optional[int],
})


Mutation = TypedDict('Mutation', {
	'addProjectToSecurityDashboard': 'AddProjectToSecurityDashboardMutationResult',
	'adminSidekiqQueuesDeleteJobs': 'AdminSidekiqQueuesDeleteJobsMutationResult',
	'alertSetAssignees': 'AlertSetAssigneesMutationResult',
	'alertTodoCreate': 'AlertTodoCreateMutationResult',
	'apiFuzzingCiConfigurationCreate': 'ApiFuzzingCiConfigurationCreateMutationResult',
	'awardEmojiAdd': 'AwardEmojiAddMutationResult',
	'awardEmojiRemove': 'AwardEmojiRemoveMutationResult',
	'awardEmojiToggle': 'AwardEmojiToggleMutationResult',
	'boardEpicCreate': 'BoardEpicCreateMutationResult',
	'boardListCreate': 'BoardListCreateMutationResult',
	'boardListUpdateLimitMetrics': 'BoardListUpdateLimitMetricsMutationResult',
	'bulkEnableDevopsAdoptionNamespaces': 'BulkEnableDevopsAdoptionNamespacesMutationResult',
	'ciCdSettingsUpdate': 'CiCdSettingsUpdateMutationResult',
	'ciJobTokenScopeAddProject': 'CiJobTokenScopeAddProjectMutationResult',
	'ciJobTokenScopeRemoveProject': 'CiJobTokenScopeRemoveProjectMutationResult',
	'clusterAgentDelete': 'ClusterAgentDeleteMutationResult',
	'clusterAgentTokenCreate': 'ClusterAgentTokenCreateMutationResult',
	'clusterAgentTokenDelete': 'ClusterAgentTokenDeleteMutationResult',
	'clusterAgentTokenRevoke': 'ClusterAgentTokenRevokeMutationResult',
	'commitCreate': 'CommitCreateMutationResult',
	'configureContainerScanning': 'ConfigureContainerScanningMutationResult',
	'configureDependencyScanning': 'ConfigureDependencyScanningMutationResult',
	'configureSast': 'ConfigureSastMutationResult',
	'configureSastIac': 'ConfigureSastIacMutationResult',
	'configureSecretDetection': 'ConfigureSecretDetectionMutationResult',
	'corpusCreate': 'CorpusCreateMutationResult',
	'createAlertIssue': 'CreateAlertIssueMutationResult',
	'createAnnotation': 'CreateAnnotationMutationResult',
	'createBoard': 'CreateBoardMutationResult',
	'createBranch': 'CreateBranchMutationResult',
	'createClusterAgent': 'CreateClusterAgentMutationResult',
	'createComplianceFramework': 'CreateComplianceFrameworkMutationResult',
	'createCustomEmoji': 'CreateCustomEmojiMutationResult',
	'createDiffNote': 'CreateDiffNoteMutationResult',
	'createEpic': 'CreateEpicMutationResult',
	'createImageDiffNote': 'CreateImageDiffNoteMutationResult',
	'createIssue': 'CreateIssueMutationResult',
	'createIteration': 'CreateIterationMutationResult',
	'createNote': 'CreateNoteMutationResult',
	'createRequirement': 'CreateRequirementMutationResult',
	'createSnippet': 'CreateSnippetMutationResult',
	'createTestCase': 'CreateTestCaseMutationResult',
	'customerRelationsContactCreate': 'CustomerRelationsContactCreateMutationResult',
	'customerRelationsContactUpdate': 'CustomerRelationsContactUpdateMutationResult',
	'customerRelationsOrganizationCreate': 'CustomerRelationsOrganizationCreateMutationResult',
	'customerRelationsOrganizationUpdate': 'CustomerRelationsOrganizationUpdateMutationResult',
	'dastOnDemandScanCreate': 'DastOnDemandScanCreateMutationResult',
	'dastProfileCreate': 'DastProfileCreateMutationResult',
	'dastProfileDelete': 'DastProfileDeleteMutationResult',
	'dastProfileRun': 'DastProfileRunMutationResult',
	'dastProfileUpdate': 'DastProfileUpdateMutationResult',
	'dastScannerProfileCreate': 'DastScannerProfileCreateMutationResult',
	'dastScannerProfileDelete': 'DastScannerProfileDeleteMutationResult',
	'dastScannerProfileUpdate': 'DastScannerProfileUpdateMutationResult',
	'dastSiteProfileCreate': 'DastSiteProfileCreateMutationResult',
	'dastSiteProfileDelete': 'DastSiteProfileDeleteMutationResult',
	'dastSiteProfileUpdate': 'DastSiteProfileUpdateMutationResult',
	'dastSiteTokenCreate': 'DastSiteTokenCreateMutationResult',
	'dastSiteValidationCreate': 'DastSiteValidationCreateMutationResult',
	'dastSiteValidationRevoke': 'DastSiteValidationRevokeMutationResult',
	'deleteAnnotation': 'DeleteAnnotationMutationResult',
	'designManagementDelete': 'DesignManagementDeleteMutationResult',
	'designManagementMove': 'DesignManagementMoveMutationResult',
	'designManagementUpload': 'DesignManagementUploadMutationResult',
	'destroyBoard': 'DestroyBoardMutationResult',
	'destroyBoardList': 'DestroyBoardListMutationResult',
	'destroyComplianceFramework': 'DestroyComplianceFrameworkMutationResult',
	'destroyContainerRepository': 'DestroyContainerRepositoryMutationResult',
	'destroyContainerRepositoryTags': 'DestroyContainerRepositoryTagsMutationResult',
	'destroyCustomEmoji': 'DestroyCustomEmojiMutationResult',
	'destroyEpicBoard': 'DestroyEpicBoardMutationResult',
	'destroyNote': 'DestroyNoteMutationResult',
	'destroyPackage': 'DestroyPackageMutationResult',
	'destroyPackageFile': 'DestroyPackageFileMutationResult',
	'destroySnippet': 'DestroySnippetMutationResult',
	'disableDevopsAdoptionNamespace': 'DisableDevopsAdoptionNamespaceMutationResult',
	'discussionToggleResolve': 'DiscussionToggleResolveMutationResult',
	'echoCreate': 'EchoCreateMutationResult',
	'enableDevopsAdoptionNamespace': 'EnableDevopsAdoptionNamespaceMutationResult',
	'environmentsCanaryIngressUpdate': 'EnvironmentsCanaryIngressUpdateMutationResult',
	'epicAddIssue': 'EpicAddIssueMutationResult',
	'epicBoardCreate': 'EpicBoardCreateMutationResult',
	'epicBoardListCreate': 'EpicBoardListCreateMutationResult',
	'epicBoardListDestroy': 'EpicBoardListDestroyMutationResult',
	'epicBoardUpdate': 'EpicBoardUpdateMutationResult',
	'epicMoveList': 'EpicMoveListMutationResult',
	'epicSetSubscription': 'EpicSetSubscriptionMutationResult',
	'epicTreeReorder': 'EpicTreeReorderMutationResult',
	'escalationPolicyCreate': 'EscalationPolicyCreateMutationResult',
	'escalationPolicyDestroy': 'EscalationPolicyDestroyMutationResult',
	'escalationPolicyUpdate': 'EscalationPolicyUpdateMutationResult',
	'exportRequirements': 'ExportRequirementsMutationResult',
	'externalAuditEventDestinationCreate': 'ExternalAuditEventDestinationCreateMutationResult',
	'externalAuditEventDestinationDestroy': 'ExternalAuditEventDestinationDestroyMutationResult',
	'externalAuditEventDestinationUpdate': 'ExternalAuditEventDestinationUpdateMutationResult',
	'gitlabSubscriptionActivate': 'GitlabSubscriptionActivateMutationResult',
	'groupUpdate': 'GroupUpdateMutationResult',
	'httpIntegrationCreate': 'HttpIntegrationCreateMutationResult',
	'httpIntegrationDestroy': 'HttpIntegrationDestroyMutationResult',
	'httpIntegrationResetToken': 'HttpIntegrationResetTokenMutationResult',
	'httpIntegrationUpdate': 'HttpIntegrationUpdateMutationResult',
	'issueMove': 'IssueMoveMutationResult',
	'issueMoveList': 'IssueMoveListMutationResult',
	'issueSetAssignees': 'IssueSetAssigneesMutationResult',
	'issueSetConfidential': 'IssueSetConfidentialMutationResult',
	'issueSetCrmContacts': 'IssueSetCrmContactsMutationResult',
	'issueSetDueDate': 'IssueSetDueDateMutationResult',
	'issueSetEpic': 'IssueSetEpicMutationResult',
	'issueSetEscalationPolicy': 'IssueSetEscalationPolicyMutationResult',
	'issueSetEscalationStatus': 'IssueSetEscalationStatusMutationResult',
	'issueSetIteration': 'IssueSetIterationMutationResult',
	'issueSetLocked': 'IssueSetLockedMutationResult',
	'issueSetSeverity': 'IssueSetSeverityMutationResult',
	'issueSetSubscription': 'IssueSetSubscriptionMutationResult',
	'issueSetWeight': 'IssueSetWeightMutationResult',
	'iterationCadenceCreate': 'IterationCadenceCreateMutationResult',
	'iterationCadenceDestroy': 'IterationCadenceDestroyMutationResult',
	'iterationCadenceUpdate': 'IterationCadenceUpdateMutationResult',
	'iterationCreate': 'IterationCreateMutationResult',
	'iterationDelete': 'IterationDeleteMutationResult',
	'jiraImportStart': 'JiraImportStartMutationResult',
	'jiraImportUsers': 'JiraImportUsersMutationResult',
	'jobCancel': 'JobCancelMutationResult',
	'jobPlay': 'JobPlayMutationResult',
	'jobRetry': 'JobRetryMutationResult',
	'jobUnschedule': 'JobUnscheduleMutationResult',
	'labelCreate': 'LabelCreateMutationResult',
	'markAsSpamSnippet': 'MarkAsSpamSnippetMutationResult',
	'mergeRequestAccept': 'MergeRequestAcceptMutationResult',
	'mergeRequestCreate': 'MergeRequestCreateMutationResult',
	'mergeRequestReviewerRereview': 'MergeRequestReviewerRereviewMutationResult',
	'mergeRequestSetAssignees': 'MergeRequestSetAssigneesMutationResult',
	'mergeRequestSetDraft': 'MergeRequestSetDraftMutationResult',
	'mergeRequestSetLabels': 'MergeRequestSetLabelsMutationResult',
	'mergeRequestSetLocked': 'MergeRequestSetLockedMutationResult',
	'mergeRequestSetMilestone': 'MergeRequestSetMilestoneMutationResult',
	'mergeRequestSetSubscription': 'MergeRequestSetSubscriptionMutationResult',
	'mergeRequestUpdate': 'MergeRequestUpdateMutationResult',
	'namespaceIncreaseStorageTemporarily': 'NamespaceIncreaseStorageTemporarilyMutationResult',
	'oncallRotationCreate': 'OncallRotationCreateMutationResult',
	'oncallRotationDestroy': 'OncallRotationDestroyMutationResult',
	'oncallRotationUpdate': 'OncallRotationUpdateMutationResult',
	'oncallScheduleCreate': 'OncallScheduleCreateMutationResult',
	'oncallScheduleDestroy': 'OncallScheduleDestroyMutationResult',
	'oncallScheduleUpdate': 'OncallScheduleUpdateMutationResult',
	'pipelineCancel': 'PipelineCancelMutationResult',
	'pipelineDestroy': 'PipelineDestroyMutationResult',
	'pipelineRetry': 'PipelineRetryMutationResult',
	'projectSetComplianceFramework': 'ProjectSetComplianceFrameworkMutationResult',
	'projectSetLocked': 'ProjectSetLockedMutationResult',
	'prometheusIntegrationCreate': 'PrometheusIntegrationCreateMutationResult',
	'prometheusIntegrationResetToken': 'PrometheusIntegrationResetTokenMutationResult',
	'prometheusIntegrationUpdate': 'PrometheusIntegrationUpdateMutationResult',
	'promoteToEpic': 'PromoteToEpicMutationResult',
	'releaseAssetLinkCreate': 'ReleaseAssetLinkCreateMutationResult',
	'releaseAssetLinkDelete': 'ReleaseAssetLinkDeleteMutationResult',
	'releaseAssetLinkUpdate': 'ReleaseAssetLinkUpdateMutationResult',
	'releaseCreate': 'ReleaseCreateMutationResult',
	'releaseDelete': 'ReleaseDeleteMutationResult',
	'releaseUpdate': 'ReleaseUpdateMutationResult',
	'removeProjectFromSecurityDashboard': 'RemoveProjectFromSecurityDashboardMutationResult',
	'repositionImageDiffNote': 'RepositionImageDiffNoteMutationResult',
	'runnerDelete': 'RunnerDeleteMutationResult',
	'runnerUpdate': 'RunnerUpdateMutationResult',
	'runnersRegistrationTokenReset': 'RunnersRegistrationTokenResetMutationResult',
	'savedReplyCreate': 'SavedReplyCreateMutationResult',
	'savedReplyDestroy': 'SavedReplyDestroyMutationResult',
	'savedReplyUpdate': 'SavedReplyUpdateMutationResult',
	'scanExecutionPolicyCommit': 'ScanExecutionPolicyCommitMutationResult',
	'securityPolicyProjectAssign': 'SecurityPolicyProjectAssignMutationResult',
	'securityPolicyProjectCreate': 'SecurityPolicyProjectCreateMutationResult',
	'securityPolicyProjectUnassign': 'SecurityPolicyProjectUnassignMutationResult',
	'securityTrainingUpdate': 'SecurityTrainingUpdateMutationResult',
	'terraformStateDelete': 'TerraformStateDeleteMutationResult',
	'terraformStateLock': 'TerraformStateLockMutationResult',
	'terraformStateUnlock': 'TerraformStateUnlockMutationResult',
	'timelineEventCreate': 'TimelineEventCreateMutationResult',
	'timelineEventDestroy': 'TimelineEventDestroyMutationResult',
	'timelineEventPromoteFromNote': 'TimelineEventPromoteFromNoteMutationResult',
	'timelineEventUpdate': 'TimelineEventUpdateMutationResult',
	'todoCreate': 'TodoCreateMutationResult',
	'todoMarkDone': 'TodoMarkDoneMutationResult',
	'todoRestore': 'TodoRestoreMutationResult',
	'todoRestoreMany': 'TodoRestoreManyMutationResult',
	'todosMarkAllDone': 'TodosMarkAllDoneMutationResult',
	'updateAlertStatus': 'UpdateAlertStatusMutationResult',
	'updateBoard': 'UpdateBoardMutationResult',
	'updateBoardEpicUserPreferences': 'UpdateBoardEpicUserPreferencesMutationResult',
	'updateBoardList': 'UpdateBoardListMutationResult',
	'updateComplianceFramework': 'UpdateComplianceFrameworkMutationResult',
	'updateContainerExpirationPolicy': 'UpdateContainerExpirationPolicyMutationResult',
	'updateDependencyProxyImageTtlGroupPolicy': 'UpdateDependencyProxyImageTtlGroupPolicyMutationResult',
	'updateDependencyProxySettings': 'UpdateDependencyProxySettingsMutationResult',
	'updateEpic': 'UpdateEpicMutationResult',
	'updateEpicBoardList': 'UpdateEpicBoardListMutationResult',
	'updateImageDiffNote': 'UpdateImageDiffNoteMutationResult',
	'updateIssue': 'UpdateIssueMutationResult',
	'updateIteration': 'UpdateIterationMutationResult',
	'updateNamespacePackageSettings': 'UpdateNamespacePackageSettingsMutationResult',
	'updateNote': 'UpdateNoteMutationResult',
	'updateRequirement': 'UpdateRequirementMutationResult',
	'updateSnippet': 'UpdateSnippetMutationResult',
	'userCalloutCreate': 'UserCalloutCreateMutationResult',
	'userPreferencesUpdate': 'UserPreferencesUpdateMutationResult',
	'vulnerabilityConfirm': 'VulnerabilityConfirmMutationResult',
	'vulnerabilityCreate': 'VulnerabilityCreateMutationResult',
	'vulnerabilityDismiss': 'VulnerabilityDismissMutationResult',
	'vulnerabilityExternalIssueLinkCreate': 'VulnerabilityExternalIssueLinkCreateMutationResult',
	'vulnerabilityExternalIssueLinkDestroy': 'VulnerabilityExternalIssueLinkDestroyMutationResult',
	'vulnerabilityFindingDismiss': 'VulnerabilityFindingDismissMutationResult',
	'vulnerabilityResolve': 'VulnerabilityResolveMutationResult',
	'vulnerabilityRevertToDetected': 'VulnerabilityRevertToDetectedMutationResult',
	'workItemCreate': 'WorkItemCreateMutationResult',
	'workItemCreateFromTask': 'WorkItemCreateFromTaskMutationResult',
	'workItemDelete': 'WorkItemDeleteMutationResult',
	'workItemUpdate': 'WorkItemUpdateMutationResult',
})


AddProjectToSecurityDashboardParams = TypedDict('AddProjectToSecurityDashboardParams', {
	'input': 'AddProjectToSecurityDashboardInput',
})


AddProjectToSecurityDashboardMutationResult = ClassVar[Optional['AddProjectToSecurityDashboardPayload']]


AdminSidekiqQueuesDeleteJobsParams = TypedDict('AdminSidekiqQueuesDeleteJobsParams', {
	'input': 'AdminSidekiqQueuesDeleteJobsInput',
})


AdminSidekiqQueuesDeleteJobsMutationResult = ClassVar[Optional['AdminSidekiqQueuesDeleteJobsPayload']]


AlertSetAssigneesParams = TypedDict('AlertSetAssigneesParams', {
	'input': 'AlertSetAssigneesInput',
})


AlertSetAssigneesMutationResult = ClassVar[Optional['AlertSetAssigneesPayload']]


AlertTodoCreateParams = TypedDict('AlertTodoCreateParams', {
	'input': 'AlertTodoCreateInput',
})


AlertTodoCreateMutationResult = ClassVar[Optional['AlertTodoCreatePayload']]


ApiFuzzingCiConfigurationCreateParams = TypedDict('ApiFuzzingCiConfigurationCreateParams', {
	'input': 'ApiFuzzingCiConfigurationCreateInput',
})


ApiFuzzingCiConfigurationCreateMutationResult = ClassVar[Optional['ApiFuzzingCiConfigurationCreatePayload']]


AwardEmojiAddParams = TypedDict('AwardEmojiAddParams', {
	'input': 'AwardEmojiAddInput',
})


AwardEmojiAddMutationResult = ClassVar[Optional['AwardEmojiAddPayload']]


AwardEmojiRemoveParams = TypedDict('AwardEmojiRemoveParams', {
	'input': 'AwardEmojiRemoveInput',
})


AwardEmojiRemoveMutationResult = ClassVar[Optional['AwardEmojiRemovePayload']]


AwardEmojiToggleParams = TypedDict('AwardEmojiToggleParams', {
	'input': 'AwardEmojiToggleInput',
})


AwardEmojiToggleMutationResult = ClassVar[Optional['AwardEmojiTogglePayload']]


BoardEpicCreateParams = TypedDict('BoardEpicCreateParams', {
	'input': 'BoardEpicCreateInput',
})


BoardEpicCreateMutationResult = ClassVar[Optional['BoardEpicCreatePayload']]


BoardListCreateParams = TypedDict('BoardListCreateParams', {
	'input': 'BoardListCreateInput',
})


BoardListCreateMutationResult = ClassVar[Optional['BoardListCreatePayload']]


BoardListUpdateLimitMetricsParams = TypedDict('BoardListUpdateLimitMetricsParams', {
	'input': 'BoardListUpdateLimitMetricsInput',
})


BoardListUpdateLimitMetricsMutationResult = ClassVar[Optional['BoardListUpdateLimitMetricsPayload']]


BulkEnableDevopsAdoptionNamespacesParams = TypedDict('BulkEnableDevopsAdoptionNamespacesParams', {
	'input': 'BulkEnableDevopsAdoptionNamespacesInput',
})


BulkEnableDevopsAdoptionNamespacesMutationResult = ClassVar[Optional['BulkEnableDevopsAdoptionNamespacesPayload']]


CiCdSettingsUpdateParams = TypedDict('CiCdSettingsUpdateParams', {
	'input': 'CiCdSettingsUpdateInput',
})


CiCdSettingsUpdateMutationResult = ClassVar[Optional['CiCdSettingsUpdatePayload']]


CiJobTokenScopeAddProjectParams = TypedDict('CiJobTokenScopeAddProjectParams', {
	'input': 'CiJobTokenScopeAddProjectInput',
})


CiJobTokenScopeAddProjectMutationResult = ClassVar[Optional['CiJobTokenScopeAddProjectPayload']]


CiJobTokenScopeRemoveProjectParams = TypedDict('CiJobTokenScopeRemoveProjectParams', {
	'input': 'CiJobTokenScopeRemoveProjectInput',
})


CiJobTokenScopeRemoveProjectMutationResult = ClassVar[Optional['CiJobTokenScopeRemoveProjectPayload']]


ClusterAgentDeleteParams = TypedDict('ClusterAgentDeleteParams', {
	'input': 'ClusterAgentDeleteInput',
})


ClusterAgentDeleteMutationResult = ClassVar[Optional['ClusterAgentDeletePayload']]


ClusterAgentTokenCreateParams = TypedDict('ClusterAgentTokenCreateParams', {
	'input': 'ClusterAgentTokenCreateInput',
})


ClusterAgentTokenCreateMutationResult = ClassVar[Optional['ClusterAgentTokenCreatePayload']]


ClusterAgentTokenDeleteParams = TypedDict('ClusterAgentTokenDeleteParams', {
	'input': 'ClusterAgentTokenDeleteInput',
})


ClusterAgentTokenDeleteMutationResult = ClassVar[Optional['ClusterAgentTokenDeletePayload']]


ClusterAgentTokenRevokeParams = TypedDict('ClusterAgentTokenRevokeParams', {
	'input': 'ClusterAgentTokenRevokeInput',
})


ClusterAgentTokenRevokeMutationResult = ClassVar[Optional['ClusterAgentTokenRevokePayload']]


CommitCreateParams = TypedDict('CommitCreateParams', {
	'input': 'CommitCreateInput',
})


CommitCreateMutationResult = ClassVar[Optional['CommitCreatePayload']]


ConfigureContainerScanningParams = TypedDict('ConfigureContainerScanningParams', {
	'input': 'ConfigureContainerScanningInput',
})


ConfigureContainerScanningMutationResult = ClassVar[Optional['ConfigureContainerScanningPayload']]


ConfigureDependencyScanningParams = TypedDict('ConfigureDependencyScanningParams', {
	'input': 'ConfigureDependencyScanningInput',
})


ConfigureDependencyScanningMutationResult = ClassVar[Optional['ConfigureDependencyScanningPayload']]


ConfigureSastParams = TypedDict('ConfigureSastParams', {
	'input': 'ConfigureSastInput',
})


ConfigureSastMutationResult = ClassVar[Optional['ConfigureSastPayload']]


ConfigureSastIacParams = TypedDict('ConfigureSastIacParams', {
	'input': 'ConfigureSastIacInput',
})


ConfigureSastIacMutationResult = ClassVar[Optional['ConfigureSastIacPayload']]


ConfigureSecretDetectionParams = TypedDict('ConfigureSecretDetectionParams', {
	'input': 'ConfigureSecretDetectionInput',
})


ConfigureSecretDetectionMutationResult = ClassVar[Optional['ConfigureSecretDetectionPayload']]


CorpusCreateParams = TypedDict('CorpusCreateParams', {
	'input': 'CorpusCreateInput',
})


CorpusCreateMutationResult = ClassVar[Optional['CorpusCreatePayload']]


CreateAlertIssueParams = TypedDict('CreateAlertIssueParams', {
	'input': 'CreateAlertIssueInput',
})


CreateAlertIssueMutationResult = ClassVar[Optional['CreateAlertIssuePayload']]


CreateAnnotationParams = TypedDict('CreateAnnotationParams', {
	'input': 'CreateAnnotationInput',
})


CreateAnnotationMutationResult = ClassVar[Optional['CreateAnnotationPayload']]


CreateBoardParams = TypedDict('CreateBoardParams', {
	'input': 'CreateBoardInput',
})


CreateBoardMutationResult = ClassVar[Optional['CreateBoardPayload']]


CreateBranchParams = TypedDict('CreateBranchParams', {
	'input': 'CreateBranchInput',
})


CreateBranchMutationResult = ClassVar[Optional['CreateBranchPayload']]


CreateClusterAgentParams = TypedDict('CreateClusterAgentParams', {
	'input': 'CreateClusterAgentInput',
})


CreateClusterAgentMutationResult = ClassVar[Optional['CreateClusterAgentPayload']]


CreateComplianceFrameworkParams = TypedDict('CreateComplianceFrameworkParams', {
	'input': 'CreateComplianceFrameworkInput',
})


CreateComplianceFrameworkMutationResult = ClassVar[Optional['CreateComplianceFrameworkPayload']]


CreateCustomEmojiParams = TypedDict('CreateCustomEmojiParams', {
	'input': 'CreateCustomEmojiInput',
})


CreateCustomEmojiMutationResult = ClassVar[Optional['CreateCustomEmojiPayload']]


CreateDiffNoteParams = TypedDict('CreateDiffNoteParams', {
	'input': 'CreateDiffNoteInput',
})


CreateDiffNoteMutationResult = ClassVar[Optional['CreateDiffNotePayload']]


CreateEpicParams = TypedDict('CreateEpicParams', {
	'input': 'CreateEpicInput',
})


CreateEpicMutationResult = ClassVar[Optional['CreateEpicPayload']]


CreateImageDiffNoteParams = TypedDict('CreateImageDiffNoteParams', {
	'input': 'CreateImageDiffNoteInput',
})


CreateImageDiffNoteMutationResult = ClassVar[Optional['CreateImageDiffNotePayload']]


CreateIssueParams = TypedDict('CreateIssueParams', {
	'input': 'CreateIssueInput',
})


CreateIssueMutationResult = ClassVar[Optional['CreateIssuePayload']]


CreateIterationParams = TypedDict('CreateIterationParams', {
	'input': 'CreateIterationInput',
})


CreateIterationMutationResult = ClassVar[Optional['CreateIterationPayload']]


CreateNoteParams = TypedDict('CreateNoteParams', {
	'input': 'CreateNoteInput',
})


CreateNoteMutationResult = ClassVar[Optional['CreateNotePayload']]


CreateRequirementParams = TypedDict('CreateRequirementParams', {
	'input': 'CreateRequirementInput',
})


CreateRequirementMutationResult = ClassVar[Optional['CreateRequirementPayload']]


CreateSnippetParams = TypedDict('CreateSnippetParams', {
	'input': 'CreateSnippetInput',
})


CreateSnippetMutationResult = ClassVar[Optional['CreateSnippetPayload']]


CreateTestCaseParams = TypedDict('CreateTestCaseParams', {
	'input': 'CreateTestCaseInput',
})


CreateTestCaseMutationResult = ClassVar[Optional['CreateTestCasePayload']]


CustomerRelationsContactCreateParams = TypedDict('CustomerRelationsContactCreateParams', {
	'input': 'CustomerRelationsContactCreateInput',
})


CustomerRelationsContactCreateMutationResult = ClassVar[Optional['CustomerRelationsContactCreatePayload']]


CustomerRelationsContactUpdateParams = TypedDict('CustomerRelationsContactUpdateParams', {
	'input': 'CustomerRelationsContactUpdateInput',
})


CustomerRelationsContactUpdateMutationResult = ClassVar[Optional['CustomerRelationsContactUpdatePayload']]


CustomerRelationsOrganizationCreateParams = TypedDict('CustomerRelationsOrganizationCreateParams', {
	'input': 'CustomerRelationsOrganizationCreateInput',
})


CustomerRelationsOrganizationCreateMutationResult = ClassVar[Optional['CustomerRelationsOrganizationCreatePayload']]


CustomerRelationsOrganizationUpdateParams = TypedDict('CustomerRelationsOrganizationUpdateParams', {
	'input': 'CustomerRelationsOrganizationUpdateInput',
})


CustomerRelationsOrganizationUpdateMutationResult = ClassVar[Optional['CustomerRelationsOrganizationUpdatePayload']]


DastOnDemandScanCreateParams = TypedDict('DastOnDemandScanCreateParams', {
	'input': 'DastOnDemandScanCreateInput',
})


DastOnDemandScanCreateMutationResult = ClassVar[Optional['DastOnDemandScanCreatePayload']]


DastProfileCreateParams = TypedDict('DastProfileCreateParams', {
	'input': 'DastProfileCreateInput',
})


DastProfileCreateMutationResult = ClassVar[Optional['DastProfileCreatePayload']]


DastProfileDeleteParams = TypedDict('DastProfileDeleteParams', {
	'input': 'DastProfileDeleteInput',
})


DastProfileDeleteMutationResult = ClassVar[Optional['DastProfileDeletePayload']]


DastProfileRunParams = TypedDict('DastProfileRunParams', {
	'input': 'DastProfileRunInput',
})


DastProfileRunMutationResult = ClassVar[Optional['DastProfileRunPayload']]


DastProfileUpdateParams = TypedDict('DastProfileUpdateParams', {
	'input': 'DastProfileUpdateInput',
})


DastProfileUpdateMutationResult = ClassVar[Optional['DastProfileUpdatePayload']]


DastScannerProfileCreateParams = TypedDict('DastScannerProfileCreateParams', {
	'input': 'DastScannerProfileCreateInput',
})


DastScannerProfileCreateMutationResult = ClassVar[Optional['DastScannerProfileCreatePayload']]


DastScannerProfileDeleteParams = TypedDict('DastScannerProfileDeleteParams', {
	'input': 'DastScannerProfileDeleteInput',
})


DastScannerProfileDeleteMutationResult = ClassVar[Optional['DastScannerProfileDeletePayload']]


DastScannerProfileUpdateParams = TypedDict('DastScannerProfileUpdateParams', {
	'input': 'DastScannerProfileUpdateInput',
})


DastScannerProfileUpdateMutationResult = ClassVar[Optional['DastScannerProfileUpdatePayload']]


DastSiteProfileCreateParams = TypedDict('DastSiteProfileCreateParams', {
	'input': 'DastSiteProfileCreateInput',
})


DastSiteProfileCreateMutationResult = ClassVar[Optional['DastSiteProfileCreatePayload']]


DastSiteProfileDeleteParams = TypedDict('DastSiteProfileDeleteParams', {
	'input': 'DastSiteProfileDeleteInput',
})


DastSiteProfileDeleteMutationResult = ClassVar[Optional['DastSiteProfileDeletePayload']]


DastSiteProfileUpdateParams = TypedDict('DastSiteProfileUpdateParams', {
	'input': 'DastSiteProfileUpdateInput',
})


DastSiteProfileUpdateMutationResult = ClassVar[Optional['DastSiteProfileUpdatePayload']]


DastSiteTokenCreateParams = TypedDict('DastSiteTokenCreateParams', {
	'input': 'DastSiteTokenCreateInput',
})


DastSiteTokenCreateMutationResult = ClassVar[Optional['DastSiteTokenCreatePayload']]


DastSiteValidationCreateParams = TypedDict('DastSiteValidationCreateParams', {
	'input': 'DastSiteValidationCreateInput',
})


DastSiteValidationCreateMutationResult = ClassVar[Optional['DastSiteValidationCreatePayload']]


DastSiteValidationRevokeParams = TypedDict('DastSiteValidationRevokeParams', {
	'input': 'DastSiteValidationRevokeInput',
})


DastSiteValidationRevokeMutationResult = ClassVar[Optional['DastSiteValidationRevokePayload']]


DeleteAnnotationParams = TypedDict('DeleteAnnotationParams', {
	'input': 'DeleteAnnotationInput',
})


DeleteAnnotationMutationResult = ClassVar[Optional['DeleteAnnotationPayload']]


DesignManagementDeleteParams = TypedDict('DesignManagementDeleteParams', {
	'input': 'DesignManagementDeleteInput',
})


DesignManagementDeleteMutationResult = ClassVar[Optional['DesignManagementDeletePayload']]


DesignManagementMoveParams = TypedDict('DesignManagementMoveParams', {
	'input': 'DesignManagementMoveInput',
})


DesignManagementMoveMutationResult = ClassVar[Optional['DesignManagementMovePayload']]


DesignManagementUploadParams = TypedDict('DesignManagementUploadParams', {
	'input': 'DesignManagementUploadInput',
})


DesignManagementUploadMutationResult = ClassVar[Optional['DesignManagementUploadPayload']]


DestroyBoardParams = TypedDict('DestroyBoardParams', {
	'input': 'DestroyBoardInput',
})


DestroyBoardMutationResult = ClassVar[Optional['DestroyBoardPayload']]


DestroyBoardListParams = TypedDict('DestroyBoardListParams', {
	'input': 'DestroyBoardListInput',
})


DestroyBoardListMutationResult = ClassVar[Optional['DestroyBoardListPayload']]


DestroyComplianceFrameworkParams = TypedDict('DestroyComplianceFrameworkParams', {
	'input': 'DestroyComplianceFrameworkInput',
})


DestroyComplianceFrameworkMutationResult = ClassVar[Optional['DestroyComplianceFrameworkPayload']]


DestroyContainerRepositoryParams = TypedDict('DestroyContainerRepositoryParams', {
	'input': 'DestroyContainerRepositoryInput',
})


DestroyContainerRepositoryMutationResult = ClassVar[Optional['DestroyContainerRepositoryPayload']]


DestroyContainerRepositoryTagsParams = TypedDict('DestroyContainerRepositoryTagsParams', {
	'input': 'DestroyContainerRepositoryTagsInput',
})


DestroyContainerRepositoryTagsMutationResult = ClassVar[Optional['DestroyContainerRepositoryTagsPayload']]


DestroyCustomEmojiParams = TypedDict('DestroyCustomEmojiParams', {
	'input': 'DestroyCustomEmojiInput',
})


DestroyCustomEmojiMutationResult = ClassVar[Optional['DestroyCustomEmojiPayload']]


DestroyEpicBoardParams = TypedDict('DestroyEpicBoardParams', {
	'input': 'DestroyEpicBoardInput',
})


DestroyEpicBoardMutationResult = ClassVar[Optional['DestroyEpicBoardPayload']]


DestroyNoteParams = TypedDict('DestroyNoteParams', {
	'input': 'DestroyNoteInput',
})


DestroyNoteMutationResult = ClassVar[Optional['DestroyNotePayload']]


DestroyPackageParams = TypedDict('DestroyPackageParams', {
	'input': 'DestroyPackageInput',
})


DestroyPackageMutationResult = ClassVar[Optional['DestroyPackagePayload']]


DestroyPackageFileParams = TypedDict('DestroyPackageFileParams', {
	'input': 'DestroyPackageFileInput',
})


DestroyPackageFileMutationResult = ClassVar[Optional['DestroyPackageFilePayload']]


DestroySnippetParams = TypedDict('DestroySnippetParams', {
	'input': 'DestroySnippetInput',
})


DestroySnippetMutationResult = ClassVar[Optional['DestroySnippetPayload']]


DisableDevopsAdoptionNamespaceParams = TypedDict('DisableDevopsAdoptionNamespaceParams', {
	'input': 'DisableDevopsAdoptionNamespaceInput',
})


DisableDevopsAdoptionNamespaceMutationResult = ClassVar[Optional['DisableDevopsAdoptionNamespacePayload']]


DiscussionToggleResolveParams = TypedDict('DiscussionToggleResolveParams', {
	'input': 'DiscussionToggleResolveInput',
})


DiscussionToggleResolveMutationResult = ClassVar[Optional['DiscussionToggleResolvePayload']]


EchoCreateParams = TypedDict('EchoCreateParams', {
	'input': 'EchoCreateInput',
})


EchoCreateMutationResult = ClassVar[Optional['EchoCreatePayload']]


EnableDevopsAdoptionNamespaceParams = TypedDict('EnableDevopsAdoptionNamespaceParams', {
	'input': 'EnableDevopsAdoptionNamespaceInput',
})


EnableDevopsAdoptionNamespaceMutationResult = ClassVar[Optional['EnableDevopsAdoptionNamespacePayload']]


EnvironmentsCanaryIngressUpdateParams = TypedDict('EnvironmentsCanaryIngressUpdateParams', {
	'input': 'EnvironmentsCanaryIngressUpdateInput',
})


EnvironmentsCanaryIngressUpdateMutationResult = ClassVar[Optional['EnvironmentsCanaryIngressUpdatePayload']]


EpicAddIssueParams = TypedDict('EpicAddIssueParams', {
	'input': 'EpicAddIssueInput',
})


EpicAddIssueMutationResult = ClassVar[Optional['EpicAddIssuePayload']]


EpicBoardCreateParams = TypedDict('EpicBoardCreateParams', {
	'input': 'EpicBoardCreateInput',
})


EpicBoardCreateMutationResult = ClassVar[Optional['EpicBoardCreatePayload']]


EpicBoardListCreateParams = TypedDict('EpicBoardListCreateParams', {
	'input': 'EpicBoardListCreateInput',
})


EpicBoardListCreateMutationResult = ClassVar[Optional['EpicBoardListCreatePayload']]


EpicBoardListDestroyParams = TypedDict('EpicBoardListDestroyParams', {
	'input': 'EpicBoardListDestroyInput',
})


EpicBoardListDestroyMutationResult = ClassVar[Optional['EpicBoardListDestroyPayload']]


EpicBoardUpdateParams = TypedDict('EpicBoardUpdateParams', {
	'input': 'EpicBoardUpdateInput',
})


EpicBoardUpdateMutationResult = ClassVar[Optional['EpicBoardUpdatePayload']]


EpicMoveListParams = TypedDict('EpicMoveListParams', {
	'input': 'EpicMoveListInput',
})


EpicMoveListMutationResult = ClassVar[Optional['EpicMoveListPayload']]


EpicSetSubscriptionParams = TypedDict('EpicSetSubscriptionParams', {
	'input': 'EpicSetSubscriptionInput',
})


EpicSetSubscriptionMutationResult = ClassVar[Optional['EpicSetSubscriptionPayload']]


EpicTreeReorderParams = TypedDict('EpicTreeReorderParams', {
	'input': 'EpicTreeReorderInput',
})


EpicTreeReorderMutationResult = ClassVar[Optional['EpicTreeReorderPayload']]


EscalationPolicyCreateParams = TypedDict('EscalationPolicyCreateParams', {
	'input': 'EscalationPolicyCreateInput',
})


EscalationPolicyCreateMutationResult = ClassVar[Optional['EscalationPolicyCreatePayload']]


EscalationPolicyDestroyParams = TypedDict('EscalationPolicyDestroyParams', {
	'input': 'EscalationPolicyDestroyInput',
})


EscalationPolicyDestroyMutationResult = ClassVar[Optional['EscalationPolicyDestroyPayload']]


EscalationPolicyUpdateParams = TypedDict('EscalationPolicyUpdateParams', {
	'input': 'EscalationPolicyUpdateInput',
})


EscalationPolicyUpdateMutationResult = ClassVar[Optional['EscalationPolicyUpdatePayload']]


ExportRequirementsParams = TypedDict('ExportRequirementsParams', {
	'input': 'ExportRequirementsInput',
})


ExportRequirementsMutationResult = ClassVar[Optional['ExportRequirementsPayload']]


ExternalAuditEventDestinationCreateParams = TypedDict('ExternalAuditEventDestinationCreateParams', {
	'input': 'ExternalAuditEventDestinationCreateInput',
})


ExternalAuditEventDestinationCreateMutationResult = ClassVar[Optional['ExternalAuditEventDestinationCreatePayload']]


ExternalAuditEventDestinationDestroyParams = TypedDict('ExternalAuditEventDestinationDestroyParams', {
	'input': 'ExternalAuditEventDestinationDestroyInput',
})


ExternalAuditEventDestinationDestroyMutationResult = ClassVar[Optional['ExternalAuditEventDestinationDestroyPayload']]


ExternalAuditEventDestinationUpdateParams = TypedDict('ExternalAuditEventDestinationUpdateParams', {
	'input': 'ExternalAuditEventDestinationUpdateInput',
})


ExternalAuditEventDestinationUpdateMutationResult = ClassVar[Optional['ExternalAuditEventDestinationUpdatePayload']]


GitlabSubscriptionActivateParams = TypedDict('GitlabSubscriptionActivateParams', {
	'input': 'GitlabSubscriptionActivateInput',
})


GitlabSubscriptionActivateMutationResult = ClassVar[Optional['GitlabSubscriptionActivatePayload']]


GroupUpdateParams = TypedDict('GroupUpdateParams', {
	'input': 'GroupUpdateInput',
})


GroupUpdateMutationResult = ClassVar[Optional['GroupUpdatePayload']]


HttpIntegrationCreateParams = TypedDict('HttpIntegrationCreateParams', {
	'input': 'HttpIntegrationCreateInput',
})


HttpIntegrationCreateMutationResult = ClassVar[Optional['HttpIntegrationCreatePayload']]


HttpIntegrationDestroyParams = TypedDict('HttpIntegrationDestroyParams', {
	'input': 'HttpIntegrationDestroyInput',
})


HttpIntegrationDestroyMutationResult = ClassVar[Optional['HttpIntegrationDestroyPayload']]


HttpIntegrationResetTokenParams = TypedDict('HttpIntegrationResetTokenParams', {
	'input': 'HttpIntegrationResetTokenInput',
})


HttpIntegrationResetTokenMutationResult = ClassVar[Optional['HttpIntegrationResetTokenPayload']]


HttpIntegrationUpdateParams = TypedDict('HttpIntegrationUpdateParams', {
	'input': 'HttpIntegrationUpdateInput',
})


HttpIntegrationUpdateMutationResult = ClassVar[Optional['HttpIntegrationUpdatePayload']]


IssueMoveParams = TypedDict('IssueMoveParams', {
	'input': 'IssueMoveInput',
})


IssueMoveMutationResult = ClassVar[Optional['IssueMovePayload']]


IssueMoveListParams = TypedDict('IssueMoveListParams', {
	'input': 'IssueMoveListInput',
})


IssueMoveListMutationResult = ClassVar[Optional['IssueMoveListPayload']]


IssueSetAssigneesParams = TypedDict('IssueSetAssigneesParams', {
	'input': 'IssueSetAssigneesInput',
})


IssueSetAssigneesMutationResult = ClassVar[Optional['IssueSetAssigneesPayload']]


IssueSetConfidentialParams = TypedDict('IssueSetConfidentialParams', {
	'input': 'IssueSetConfidentialInput',
})


IssueSetConfidentialMutationResult = ClassVar[Optional['IssueSetConfidentialPayload']]


IssueSetCrmContactsParams = TypedDict('IssueSetCrmContactsParams', {
	'input': 'IssueSetCrmContactsInput',
})


IssueSetCrmContactsMutationResult = ClassVar[Optional['IssueSetCrmContactsPayload']]


IssueSetDueDateParams = TypedDict('IssueSetDueDateParams', {
	'input': 'IssueSetDueDateInput',
})


IssueSetDueDateMutationResult = ClassVar[Optional['IssueSetDueDatePayload']]


IssueSetEpicParams = TypedDict('IssueSetEpicParams', {
	'input': 'IssueSetEpicInput',
})


IssueSetEpicMutationResult = ClassVar[Optional['IssueSetEpicPayload']]


IssueSetEscalationPolicyParams = TypedDict('IssueSetEscalationPolicyParams', {
	'input': 'IssueSetEscalationPolicyInput',
})


IssueSetEscalationPolicyMutationResult = ClassVar[Optional['IssueSetEscalationPolicyPayload']]


IssueSetEscalationStatusParams = TypedDict('IssueSetEscalationStatusParams', {
	'input': 'IssueSetEscalationStatusInput',
})


IssueSetEscalationStatusMutationResult = ClassVar[Optional['IssueSetEscalationStatusPayload']]


IssueSetIterationParams = TypedDict('IssueSetIterationParams', {
	'input': 'IssueSetIterationInput',
})


IssueSetIterationMutationResult = ClassVar[Optional['IssueSetIterationPayload']]


IssueSetLockedParams = TypedDict('IssueSetLockedParams', {
	'input': 'IssueSetLockedInput',
})


IssueSetLockedMutationResult = ClassVar[Optional['IssueSetLockedPayload']]


IssueSetSeverityParams = TypedDict('IssueSetSeverityParams', {
	'input': 'IssueSetSeverityInput',
})


IssueSetSeverityMutationResult = ClassVar[Optional['IssueSetSeverityPayload']]


IssueSetSubscriptionParams = TypedDict('IssueSetSubscriptionParams', {
	'input': 'IssueSetSubscriptionInput',
})


IssueSetSubscriptionMutationResult = ClassVar[Optional['IssueSetSubscriptionPayload']]


IssueSetWeightParams = TypedDict('IssueSetWeightParams', {
	'input': 'IssueSetWeightInput',
})


IssueSetWeightMutationResult = ClassVar[Optional['IssueSetWeightPayload']]


IterationCadenceCreateParams = TypedDict('IterationCadenceCreateParams', {
	'input': 'IterationCadenceCreateInput',
})


IterationCadenceCreateMutationResult = ClassVar[Optional['IterationCadenceCreatePayload']]


IterationCadenceDestroyParams = TypedDict('IterationCadenceDestroyParams', {
	'input': 'IterationCadenceDestroyInput',
})


IterationCadenceDestroyMutationResult = ClassVar[Optional['IterationCadenceDestroyPayload']]


IterationCadenceUpdateParams = TypedDict('IterationCadenceUpdateParams', {
	'input': 'IterationCadenceUpdateInput',
})


IterationCadenceUpdateMutationResult = ClassVar[Optional['IterationCadenceUpdatePayload']]


IterationCreateParams = TypedDict('IterationCreateParams', {
	'input': 'IterationCreateInput',
})


IterationCreateMutationResult = ClassVar[Optional['IterationCreatePayload']]


IterationDeleteParams = TypedDict('IterationDeleteParams', {
	'input': 'IterationDeleteInput',
})


IterationDeleteMutationResult = ClassVar[Optional['IterationDeletePayload']]


JiraImportStartParams = TypedDict('JiraImportStartParams', {
	'input': 'JiraImportStartInput',
})


JiraImportStartMutationResult = ClassVar[Optional['JiraImportStartPayload']]


JiraImportUsersParams = TypedDict('JiraImportUsersParams', {
	'input': 'JiraImportUsersInput',
})


JiraImportUsersMutationResult = ClassVar[Optional['JiraImportUsersPayload']]


JobCancelParams = TypedDict('JobCancelParams', {
	'input': 'JobCancelInput',
})


JobCancelMutationResult = ClassVar[Optional['JobCancelPayload']]


JobPlayParams = TypedDict('JobPlayParams', {
	'input': 'JobPlayInput',
})


JobPlayMutationResult = ClassVar[Optional['JobPlayPayload']]


JobRetryParams = TypedDict('JobRetryParams', {
	'input': 'JobRetryInput',
})


JobRetryMutationResult = ClassVar[Optional['JobRetryPayload']]


JobUnscheduleParams = TypedDict('JobUnscheduleParams', {
	'input': 'JobUnscheduleInput',
})


JobUnscheduleMutationResult = ClassVar[Optional['JobUnschedulePayload']]


LabelCreateParams = TypedDict('LabelCreateParams', {
	'input': 'LabelCreateInput',
})


LabelCreateMutationResult = ClassVar[Optional['LabelCreatePayload']]


MarkAsSpamSnippetParams = TypedDict('MarkAsSpamSnippetParams', {
	'input': 'MarkAsSpamSnippetInput',
})


MarkAsSpamSnippetMutationResult = ClassVar[Optional['MarkAsSpamSnippetPayload']]


MergeRequestAcceptParams = TypedDict('MergeRequestAcceptParams', {
	'input': 'MergeRequestAcceptInput',
})


MergeRequestAcceptMutationResult = ClassVar[Optional['MergeRequestAcceptPayload']]


MergeRequestCreateParams = TypedDict('MergeRequestCreateParams', {
	'input': 'MergeRequestCreateInput',
})


MergeRequestCreateMutationResult = ClassVar[Optional['MergeRequestCreatePayload']]


MergeRequestReviewerRereviewParams = TypedDict('MergeRequestReviewerRereviewParams', {
	'input': 'MergeRequestReviewerRereviewInput',
})


MergeRequestReviewerRereviewMutationResult = ClassVar[Optional['MergeRequestReviewerRereviewPayload']]


MergeRequestSetAssigneesParams = TypedDict('MergeRequestSetAssigneesParams', {
	'input': 'MergeRequestSetAssigneesInput',
})


MergeRequestSetAssigneesMutationResult = ClassVar[Optional['MergeRequestSetAssigneesPayload']]


MergeRequestSetDraftParams = TypedDict('MergeRequestSetDraftParams', {
	'input': 'MergeRequestSetDraftInput',
})


MergeRequestSetDraftMutationResult = ClassVar[Optional['MergeRequestSetDraftPayload']]


MergeRequestSetLabelsParams = TypedDict('MergeRequestSetLabelsParams', {
	'input': 'MergeRequestSetLabelsInput',
})


MergeRequestSetLabelsMutationResult = ClassVar[Optional['MergeRequestSetLabelsPayload']]


MergeRequestSetLockedParams = TypedDict('MergeRequestSetLockedParams', {
	'input': 'MergeRequestSetLockedInput',
})


MergeRequestSetLockedMutationResult = ClassVar[Optional['MergeRequestSetLockedPayload']]


MergeRequestSetMilestoneParams = TypedDict('MergeRequestSetMilestoneParams', {
	'input': 'MergeRequestSetMilestoneInput',
})


MergeRequestSetMilestoneMutationResult = ClassVar[Optional['MergeRequestSetMilestonePayload']]


MergeRequestSetSubscriptionParams = TypedDict('MergeRequestSetSubscriptionParams', {
	'input': 'MergeRequestSetSubscriptionInput',
})


MergeRequestSetSubscriptionMutationResult = ClassVar[Optional['MergeRequestSetSubscriptionPayload']]


MergeRequestUpdateParams = TypedDict('MergeRequestUpdateParams', {
	'input': 'MergeRequestUpdateInput',
})


MergeRequestUpdateMutationResult = ClassVar[Optional['MergeRequestUpdatePayload']]


NamespaceIncreaseStorageTemporarilyParams = TypedDict('NamespaceIncreaseStorageTemporarilyParams', {
	'input': 'NamespaceIncreaseStorageTemporarilyInput',
})


NamespaceIncreaseStorageTemporarilyMutationResult = ClassVar[Optional['NamespaceIncreaseStorageTemporarilyPayload']]


OncallRotationCreateParams = TypedDict('OncallRotationCreateParams', {
	'input': 'OncallRotationCreateInput',
})


OncallRotationCreateMutationResult = ClassVar[Optional['OncallRotationCreatePayload']]


OncallRotationDestroyParams = TypedDict('OncallRotationDestroyParams', {
	'input': 'OncallRotationDestroyInput',
})


OncallRotationDestroyMutationResult = ClassVar[Optional['OncallRotationDestroyPayload']]


OncallRotationUpdateParams = TypedDict('OncallRotationUpdateParams', {
	'input': 'OncallRotationUpdateInput',
})


OncallRotationUpdateMutationResult = ClassVar[Optional['OncallRotationUpdatePayload']]


OncallScheduleCreateParams = TypedDict('OncallScheduleCreateParams', {
	'input': 'OncallScheduleCreateInput',
})


OncallScheduleCreateMutationResult = ClassVar[Optional['OncallScheduleCreatePayload']]


OncallScheduleDestroyParams = TypedDict('OncallScheduleDestroyParams', {
	'input': 'OncallScheduleDestroyInput',
})


OncallScheduleDestroyMutationResult = ClassVar[Optional['OncallScheduleDestroyPayload']]


OncallScheduleUpdateParams = TypedDict('OncallScheduleUpdateParams', {
	'input': 'OncallScheduleUpdateInput',
})


OncallScheduleUpdateMutationResult = ClassVar[Optional['OncallScheduleUpdatePayload']]


PipelineCancelParams = TypedDict('PipelineCancelParams', {
	'input': 'PipelineCancelInput',
})


PipelineCancelMutationResult = ClassVar[Optional['PipelineCancelPayload']]


PipelineDestroyParams = TypedDict('PipelineDestroyParams', {
	'input': 'PipelineDestroyInput',
})


PipelineDestroyMutationResult = ClassVar[Optional['PipelineDestroyPayload']]


PipelineRetryParams = TypedDict('PipelineRetryParams', {
	'input': 'PipelineRetryInput',
})


PipelineRetryMutationResult = ClassVar[Optional['PipelineRetryPayload']]


ProjectSetComplianceFrameworkParams = TypedDict('ProjectSetComplianceFrameworkParams', {
	'input': 'ProjectSetComplianceFrameworkInput',
})


ProjectSetComplianceFrameworkMutationResult = ClassVar[Optional['ProjectSetComplianceFrameworkPayload']]


ProjectSetLockedParams = TypedDict('ProjectSetLockedParams', {
	'input': 'ProjectSetLockedInput',
})


ProjectSetLockedMutationResult = ClassVar[Optional['ProjectSetLockedPayload']]


PrometheusIntegrationCreateParams = TypedDict('PrometheusIntegrationCreateParams', {
	'input': 'PrometheusIntegrationCreateInput',
})


PrometheusIntegrationCreateMutationResult = ClassVar[Optional['PrometheusIntegrationCreatePayload']]


PrometheusIntegrationResetTokenParams = TypedDict('PrometheusIntegrationResetTokenParams', {
	'input': 'PrometheusIntegrationResetTokenInput',
})


PrometheusIntegrationResetTokenMutationResult = ClassVar[Optional['PrometheusIntegrationResetTokenPayload']]


PrometheusIntegrationUpdateParams = TypedDict('PrometheusIntegrationUpdateParams', {
	'input': 'PrometheusIntegrationUpdateInput',
})


PrometheusIntegrationUpdateMutationResult = ClassVar[Optional['PrometheusIntegrationUpdatePayload']]


PromoteToEpicParams = TypedDict('PromoteToEpicParams', {
	'input': 'PromoteToEpicInput',
})


PromoteToEpicMutationResult = ClassVar[Optional['PromoteToEpicPayload']]


ReleaseAssetLinkCreateParams = TypedDict('ReleaseAssetLinkCreateParams', {
	'input': 'ReleaseAssetLinkCreateInput',
})


ReleaseAssetLinkCreateMutationResult = ClassVar[Optional['ReleaseAssetLinkCreatePayload']]


ReleaseAssetLinkDeleteParams = TypedDict('ReleaseAssetLinkDeleteParams', {
	'input': 'ReleaseAssetLinkDeleteInput',
})


ReleaseAssetLinkDeleteMutationResult = ClassVar[Optional['ReleaseAssetLinkDeletePayload']]


ReleaseAssetLinkUpdateParams = TypedDict('ReleaseAssetLinkUpdateParams', {
	'input': 'ReleaseAssetLinkUpdateInput',
})


ReleaseAssetLinkUpdateMutationResult = ClassVar[Optional['ReleaseAssetLinkUpdatePayload']]


ReleaseCreateParams = TypedDict('ReleaseCreateParams', {
	'input': 'ReleaseCreateInput',
})


ReleaseCreateMutationResult = ClassVar[Optional['ReleaseCreatePayload']]


ReleaseDeleteParams = TypedDict('ReleaseDeleteParams', {
	'input': 'ReleaseDeleteInput',
})


ReleaseDeleteMutationResult = ClassVar[Optional['ReleaseDeletePayload']]


ReleaseUpdateParams = TypedDict('ReleaseUpdateParams', {
	'input': 'ReleaseUpdateInput',
})


ReleaseUpdateMutationResult = ClassVar[Optional['ReleaseUpdatePayload']]


RemoveProjectFromSecurityDashboardParams = TypedDict('RemoveProjectFromSecurityDashboardParams', {
	'input': 'RemoveProjectFromSecurityDashboardInput',
})


RemoveProjectFromSecurityDashboardMutationResult = ClassVar[Optional['RemoveProjectFromSecurityDashboardPayload']]


RepositionImageDiffNoteParams = TypedDict('RepositionImageDiffNoteParams', {
	'input': 'RepositionImageDiffNoteInput',
})


RepositionImageDiffNoteMutationResult = ClassVar[Optional['RepositionImageDiffNotePayload']]


RunnerDeleteParams = TypedDict('RunnerDeleteParams', {
	'input': 'RunnerDeleteInput',
})


RunnerDeleteMutationResult = ClassVar[Optional['RunnerDeletePayload']]


RunnerUpdateParams = TypedDict('RunnerUpdateParams', {
	'input': 'RunnerUpdateInput',
})


RunnerUpdateMutationResult = ClassVar[Optional['RunnerUpdatePayload']]


RunnersRegistrationTokenResetParams = TypedDict('RunnersRegistrationTokenResetParams', {
	'input': 'RunnersRegistrationTokenResetInput',
})


RunnersRegistrationTokenResetMutationResult = ClassVar[Optional['RunnersRegistrationTokenResetPayload']]


SavedReplyCreateParams = TypedDict('SavedReplyCreateParams', {
	'input': 'SavedReplyCreateInput',
})


SavedReplyCreateMutationResult = ClassVar[Optional['SavedReplyCreatePayload']]


SavedReplyDestroyParams = TypedDict('SavedReplyDestroyParams', {
	'input': 'SavedReplyDestroyInput',
})


SavedReplyDestroyMutationResult = ClassVar[Optional['SavedReplyDestroyPayload']]


SavedReplyUpdateParams = TypedDict('SavedReplyUpdateParams', {
	'input': 'SavedReplyUpdateInput',
})


SavedReplyUpdateMutationResult = ClassVar[Optional['SavedReplyUpdatePayload']]


ScanExecutionPolicyCommitParams = TypedDict('ScanExecutionPolicyCommitParams', {
	'input': 'ScanExecutionPolicyCommitInput',
})


ScanExecutionPolicyCommitMutationResult = ClassVar[Optional['ScanExecutionPolicyCommitPayload']]


SecurityPolicyProjectAssignParams = TypedDict('SecurityPolicyProjectAssignParams', {
	'input': 'SecurityPolicyProjectAssignInput',
})


SecurityPolicyProjectAssignMutationResult = ClassVar[Optional['SecurityPolicyProjectAssignPayload']]


SecurityPolicyProjectCreateParams = TypedDict('SecurityPolicyProjectCreateParams', {
	'input': 'SecurityPolicyProjectCreateInput',
})


SecurityPolicyProjectCreateMutationResult = ClassVar[Optional['SecurityPolicyProjectCreatePayload']]


SecurityPolicyProjectUnassignParams = TypedDict('SecurityPolicyProjectUnassignParams', {
	'input': 'SecurityPolicyProjectUnassignInput',
})


SecurityPolicyProjectUnassignMutationResult = ClassVar[Optional['SecurityPolicyProjectUnassignPayload']]


SecurityTrainingUpdateParams = TypedDict('SecurityTrainingUpdateParams', {
	'input': 'SecurityTrainingUpdateInput',
})


SecurityTrainingUpdateMutationResult = ClassVar[Optional['SecurityTrainingUpdatePayload']]


TerraformStateDeleteParams = TypedDict('TerraformStateDeleteParams', {
	'input': 'TerraformStateDeleteInput',
})


TerraformStateDeleteMutationResult = ClassVar[Optional['TerraformStateDeletePayload']]


TerraformStateLockParams = TypedDict('TerraformStateLockParams', {
	'input': 'TerraformStateLockInput',
})


TerraformStateLockMutationResult = ClassVar[Optional['TerraformStateLockPayload']]


TerraformStateUnlockParams = TypedDict('TerraformStateUnlockParams', {
	'input': 'TerraformStateUnlockInput',
})


TerraformStateUnlockMutationResult = ClassVar[Optional['TerraformStateUnlockPayload']]


TimelineEventCreateParams = TypedDict('TimelineEventCreateParams', {
	'input': 'TimelineEventCreateInput',
})


TimelineEventCreateMutationResult = ClassVar[Optional['TimelineEventCreatePayload']]


TimelineEventDestroyParams = TypedDict('TimelineEventDestroyParams', {
	'input': 'TimelineEventDestroyInput',
})


TimelineEventDestroyMutationResult = ClassVar[Optional['TimelineEventDestroyPayload']]


TimelineEventPromoteFromNoteParams = TypedDict('TimelineEventPromoteFromNoteParams', {
	'input': 'TimelineEventPromoteFromNoteInput',
})


TimelineEventPromoteFromNoteMutationResult = ClassVar[Optional['TimelineEventPromoteFromNotePayload']]


TimelineEventUpdateParams = TypedDict('TimelineEventUpdateParams', {
	'input': 'TimelineEventUpdateInput',
})


TimelineEventUpdateMutationResult = ClassVar[Optional['TimelineEventUpdatePayload']]


TodoCreateParams = TypedDict('TodoCreateParams', {
	'input': 'TodoCreateInput',
})


TodoCreateMutationResult = ClassVar[Optional['TodoCreatePayload']]


TodoMarkDoneParams = TypedDict('TodoMarkDoneParams', {
	'input': 'TodoMarkDoneInput',
})


TodoMarkDoneMutationResult = ClassVar[Optional['TodoMarkDonePayload']]


TodoRestoreParams = TypedDict('TodoRestoreParams', {
	'input': 'TodoRestoreInput',
})


TodoRestoreMutationResult = ClassVar[Optional['TodoRestorePayload']]


TodoRestoreManyParams = TypedDict('TodoRestoreManyParams', {
	'input': 'TodoRestoreManyInput',
})


TodoRestoreManyMutationResult = ClassVar[Optional['TodoRestoreManyPayload']]


TodosMarkAllDoneParams = TypedDict('TodosMarkAllDoneParams', {
	'input': 'TodosMarkAllDoneInput',
})


TodosMarkAllDoneMutationResult = ClassVar[Optional['TodosMarkAllDonePayload']]


UpdateAlertStatusParams = TypedDict('UpdateAlertStatusParams', {
	'input': 'UpdateAlertStatusInput',
})


UpdateAlertStatusMutationResult = ClassVar[Optional['UpdateAlertStatusPayload']]


UpdateBoardParams = TypedDict('UpdateBoardParams', {
	'input': 'UpdateBoardInput',
})


UpdateBoardMutationResult = ClassVar[Optional['UpdateBoardPayload']]


UpdateBoardEpicUserPreferencesParams = TypedDict('UpdateBoardEpicUserPreferencesParams', {
	'input': 'UpdateBoardEpicUserPreferencesInput',
})


UpdateBoardEpicUserPreferencesMutationResult = ClassVar[Optional['UpdateBoardEpicUserPreferencesPayload']]


UpdateBoardListParams = TypedDict('UpdateBoardListParams', {
	'input': 'UpdateBoardListInput',
})


UpdateBoardListMutationResult = ClassVar[Optional['UpdateBoardListPayload']]


UpdateComplianceFrameworkParams = TypedDict('UpdateComplianceFrameworkParams', {
	'input': 'UpdateComplianceFrameworkInput',
})


UpdateComplianceFrameworkMutationResult = ClassVar[Optional['UpdateComplianceFrameworkPayload']]


UpdateContainerExpirationPolicyParams = TypedDict('UpdateContainerExpirationPolicyParams', {
	'input': 'UpdateContainerExpirationPolicyInput',
})


UpdateContainerExpirationPolicyMutationResult = ClassVar[Optional['UpdateContainerExpirationPolicyPayload']]


UpdateDependencyProxyImageTtlGroupPolicyParams = TypedDict('UpdateDependencyProxyImageTtlGroupPolicyParams', {
	'input': 'UpdateDependencyProxyImageTtlGroupPolicyInput',
})


UpdateDependencyProxyImageTtlGroupPolicyMutationResult = ClassVar[Optional['UpdateDependencyProxyImageTtlGroupPolicyPayload']]


UpdateDependencyProxySettingsParams = TypedDict('UpdateDependencyProxySettingsParams', {
	'input': 'UpdateDependencyProxySettingsInput',
})


UpdateDependencyProxySettingsMutationResult = ClassVar[Optional['UpdateDependencyProxySettingsPayload']]


UpdateEpicParams = TypedDict('UpdateEpicParams', {
	'input': 'UpdateEpicInput',
})


UpdateEpicMutationResult = ClassVar[Optional['UpdateEpicPayload']]


UpdateEpicBoardListParams = TypedDict('UpdateEpicBoardListParams', {
	'input': 'UpdateEpicBoardListInput',
})


UpdateEpicBoardListMutationResult = ClassVar[Optional['UpdateEpicBoardListPayload']]


UpdateImageDiffNoteParams = TypedDict('UpdateImageDiffNoteParams', {
	'input': 'UpdateImageDiffNoteInput',
})


UpdateImageDiffNoteMutationResult = ClassVar[Optional['UpdateImageDiffNotePayload']]


UpdateIssueParams = TypedDict('UpdateIssueParams', {
	'input': 'UpdateIssueInput',
})


UpdateIssueMutationResult = ClassVar[Optional['UpdateIssuePayload']]


UpdateIterationParams = TypedDict('UpdateIterationParams', {
	'input': 'UpdateIterationInput',
})


UpdateIterationMutationResult = ClassVar[Optional['UpdateIterationPayload']]


UpdateNamespacePackageSettingsParams = TypedDict('UpdateNamespacePackageSettingsParams', {
	'input': 'UpdateNamespacePackageSettingsInput',
})


UpdateNamespacePackageSettingsMutationResult = ClassVar[Optional['UpdateNamespacePackageSettingsPayload']]


UpdateNoteParams = TypedDict('UpdateNoteParams', {
	'input': 'UpdateNoteInput',
})


UpdateNoteMutationResult = ClassVar[Optional['UpdateNotePayload']]


UpdateRequirementParams = TypedDict('UpdateRequirementParams', {
	'input': 'UpdateRequirementInput',
})


UpdateRequirementMutationResult = ClassVar[Optional['UpdateRequirementPayload']]


UpdateSnippetParams = TypedDict('UpdateSnippetParams', {
	'input': 'UpdateSnippetInput',
})


UpdateSnippetMutationResult = ClassVar[Optional['UpdateSnippetPayload']]


UserCalloutCreateParams = TypedDict('UserCalloutCreateParams', {
	'input': 'UserCalloutCreateInput',
})


UserCalloutCreateMutationResult = ClassVar[Optional['UserCalloutCreatePayload']]


UserPreferencesUpdateParams = TypedDict('UserPreferencesUpdateParams', {
	'input': 'UserPreferencesUpdateInput',
})


UserPreferencesUpdateMutationResult = ClassVar[Optional['UserPreferencesUpdatePayload']]


VulnerabilityConfirmParams = TypedDict('VulnerabilityConfirmParams', {
	'input': 'VulnerabilityConfirmInput',
})


VulnerabilityConfirmMutationResult = ClassVar[Optional['VulnerabilityConfirmPayload']]


VulnerabilityCreateParams = TypedDict('VulnerabilityCreateParams', {
	'input': 'VulnerabilityCreateInput',
})


VulnerabilityCreateMutationResult = ClassVar[Optional['VulnerabilityCreatePayload']]


VulnerabilityDismissParams = TypedDict('VulnerabilityDismissParams', {
	'input': 'VulnerabilityDismissInput',
})


VulnerabilityDismissMutationResult = ClassVar[Optional['VulnerabilityDismissPayload']]


VulnerabilityExternalIssueLinkCreateParams = TypedDict('VulnerabilityExternalIssueLinkCreateParams', {
	'input': 'VulnerabilityExternalIssueLinkCreateInput',
})


VulnerabilityExternalIssueLinkCreateMutationResult = ClassVar[Optional['VulnerabilityExternalIssueLinkCreatePayload']]


VulnerabilityExternalIssueLinkDestroyParams = TypedDict('VulnerabilityExternalIssueLinkDestroyParams', {
	'input': 'VulnerabilityExternalIssueLinkDestroyInput',
})


VulnerabilityExternalIssueLinkDestroyMutationResult = ClassVar[Optional['VulnerabilityExternalIssueLinkDestroyPayload']]


VulnerabilityFindingDismissParams = TypedDict('VulnerabilityFindingDismissParams', {
	'input': 'VulnerabilityFindingDismissInput',
})


VulnerabilityFindingDismissMutationResult = ClassVar[Optional['VulnerabilityFindingDismissPayload']]


VulnerabilityResolveParams = TypedDict('VulnerabilityResolveParams', {
	'input': 'VulnerabilityResolveInput',
})


VulnerabilityResolveMutationResult = ClassVar[Optional['VulnerabilityResolvePayload']]


VulnerabilityRevertToDetectedParams = TypedDict('VulnerabilityRevertToDetectedParams', {
	'input': 'VulnerabilityRevertToDetectedInput',
})


VulnerabilityRevertToDetectedMutationResult = ClassVar[Optional['VulnerabilityRevertToDetectedPayload']]


WorkItemCreateParams = TypedDict('WorkItemCreateParams', {
	'input': 'WorkItemCreateInput',
})


WorkItemCreateMutationResult = ClassVar[Optional['WorkItemCreatePayload']]


WorkItemCreateFromTaskParams = TypedDict('WorkItemCreateFromTaskParams', {
	'input': 'WorkItemCreateFromTaskInput',
})


WorkItemCreateFromTaskMutationResult = ClassVar[Optional['WorkItemCreateFromTaskPayload']]


WorkItemDeleteParams = TypedDict('WorkItemDeleteParams', {
	'input': 'WorkItemDeleteInput',
})


WorkItemDeleteMutationResult = ClassVar[Optional['WorkItemDeletePayload']]


WorkItemUpdateParams = TypedDict('WorkItemUpdateParams', {
	'input': 'WorkItemUpdateInput',
})


WorkItemUpdateMutationResult = ClassVar[Optional['WorkItemUpdatePayload']]


Namespace = TypedDict('Namespace', {
	'actualRepositorySizeLimit': Optional[float],
	'additionalPurchasedStorageSize': Optional[float],
	'complianceFrameworks': Optional['ComplianceFrameworkConnection'],
	'containsLockedProjects': bool,
	'crossProjectPipelineAvailable': bool,
	'description': Optional[str],
	'descriptionHtml': Optional[str],
	'fullName': str,
	'fullPath': str,
	'id': str,
	'isTemporaryStorageIncreaseEnabled': bool,
	'lfsEnabled': Optional[bool],
	'name': str,
	'packageSettings': Optional['PackageSettings'],
	'path': str,
	'projects': 'ProjectConnection',
	'repositorySizeExcessProjectCount': int,
	'requestAccessEnabled': Optional[bool],
	'rootStorageStatistics': Optional['RootStorageStatistics'],
	'sharedRunnersSetting': Optional['SharedRunnersSetting'],
	'storageSizeLimit': Optional[float],
	'temporaryStorageIncreaseEndsOn': Optional['Time'],
	'totalRepositorySize': Optional[float],
	'totalRepositorySizeExcess': Optional[float],
	'visibility': Optional[str],
})


NamespaceConnection = TypedDict('NamespaceConnection', {
	'edges': Optional[List['NamespaceEdge']],
	'nodes': Optional[List['Namespace']],
	'pageInfo': 'PageInfo',
})


NamespaceEdge = TypedDict('NamespaceEdge', {
	'cursor': str,
	'node': Optional['Namespace'],
})


NamespaceIncreaseStorageTemporarilyPayload = TypedDict('NamespaceIncreaseStorageTemporarilyPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'namespace': Optional['Namespace'],
})


NetworkPolicy = TypedDict('NetworkPolicy', {
	'enabled': bool,
	'environments': Optional['EnvironmentConnection'],
	'fromAutoDevops': bool,
	'kind': 'NetworkPolicyKind',
	'name': str,
	'namespace': str,
	'updatedAt': 'Time',
	'yaml': str,
})


NetworkPolicyConnection = TypedDict('NetworkPolicyConnection', {
	'edges': Optional[List['NetworkPolicyEdge']],
	'nodes': Optional[List['NetworkPolicy']],
	'pageInfo': 'PageInfo',
})


NetworkPolicyEdge = TypedDict('NetworkPolicyEdge', {
	'cursor': str,
	'node': Optional['NetworkPolicy'],
})


Note = TypedDict('Note', {
	'author': 'UserCore',
	'body': str,
	'bodyHtml': Optional[str],
	'confidential': Optional[bool],
	'createdAt': 'Time',
	'discussion': Optional['Discussion'],
	'id': 'NoteID',
	'position': Optional['DiffPosition'],
	'project': Optional['Project'],
	'resolvable': bool,
	'resolved': bool,
	'resolvedAt': Optional['Time'],
	'resolvedBy': Optional['UserCore'],
	'system': bool,
	'systemNoteIconName': Optional[str],
	'updatedAt': 'Time',
	'url': Optional[str],
	'userPermissions': 'NotePermissions',
})


NoteConnection = TypedDict('NoteConnection', {
	'edges': Optional[List['NoteEdge']],
	'nodes': Optional[List['Note']],
	'pageInfo': 'PageInfo',
})


NoteEdge = TypedDict('NoteEdge', {
	'cursor': str,
	'node': Optional['Note'],
})


NotePermissions = TypedDict('NotePermissions', {
	'adminNote': bool,
	'awardEmoji': bool,
	'createNote': bool,
	'readNote': bool,
	'repositionNote': bool,
	'resolveNote': bool,
})


NugetDependencyLinkMetadata = TypedDict('NugetDependencyLinkMetadata', {
	'id': 'PackagesNugetDependencyLinkMetadatumID',
	'targetFramework': str,
})


NugetMetadata = TypedDict('NugetMetadata', {
	'iconUrl': Optional[str],
	'id': 'PackagesNugetMetadatumID',
	'licenseUrl': Optional[str],
	'projectUrl': Optional[str],
})


OncallParticipantType = TypedDict('OncallParticipantType', {
	'colorPalette': Optional[str],
	'colorWeight': Optional[str],
	'id': 'IncidentManagementOncallParticipantID',
	'user': 'UserCore',
})


OncallParticipantTypeConnection = TypedDict('OncallParticipantTypeConnection', {
	'edges': Optional[List['OncallParticipantTypeEdge']],
	'nodes': Optional[List['OncallParticipantType']],
	'pageInfo': 'PageInfo',
})


OncallParticipantTypeEdge = TypedDict('OncallParticipantTypeEdge', {
	'cursor': str,
	'node': Optional['OncallParticipantType'],
})


OncallRotationActivePeriodType = TypedDict('OncallRotationActivePeriodType', {
	'endTime': Optional[str],
	'startTime': Optional[str],
})


OncallRotationCreatePayload = TypedDict('OncallRotationCreatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'oncallRotation': Optional['IncidentManagementOncallRotation'],
})


OncallRotationDestroyPayload = TypedDict('OncallRotationDestroyPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'oncallRotation': Optional['IncidentManagementOncallRotation'],
})


OncallRotationUpdatePayload = TypedDict('OncallRotationUpdatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'oncallRotation': Optional['IncidentManagementOncallRotation'],
})


OncallScheduleCreatePayload = TypedDict('OncallScheduleCreatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'oncallSchedule': Optional['IncidentManagementOncallSchedule'],
})


OncallScheduleDestroyPayload = TypedDict('OncallScheduleDestroyPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'oncallSchedule': Optional['IncidentManagementOncallSchedule'],
})


OncallScheduleUpdatePayload = TypedDict('OncallScheduleUpdatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'oncallSchedule': Optional['IncidentManagementOncallSchedule'],
})


Package = TypedDict('Package', {
	'canDestroy': bool,
	'createdAt': 'Time',
	'id': 'PackagesPackageID',
	'metadata': Optional['PackageMetadata'],
	'name': str,
	'packageType': 'PackageTypeEnum',
	'pipelines': Optional['PipelineConnection'],
	'project': 'Project',
	'status': 'PackageStatus',
	'tags': Optional['PackageTagConnection'],
	'updatedAt': 'Time',
	'version': Optional[str],
	'versions': Optional['PackageConnection'],
})


PackageComposerJsonType = TypedDict('PackageComposerJsonType', {
	'license': Optional[str],
	'name': Optional[str],
	'type': Optional[str],
	'version': Optional[str],
})


PackageConnection = TypedDict('PackageConnection', {
	'count': int,
	'edges': Optional[List['PackageEdge']],
	'nodes': Optional[List['Package']],
	'pageInfo': 'PageInfo',
})


PackageDependency = TypedDict('PackageDependency', {
	'id': 'PackagesDependencyID',
	'name': str,
	'versionPattern': str,
})


PackageDependencyLink = TypedDict('PackageDependencyLink', {
	'dependency': Optional['PackageDependency'],
	'dependencyType': 'PackageDependencyType',
	'id': 'PackagesDependencyLinkID',
	'metadata': Optional['DependencyLinkMetadata'],
})


PackageDependencyLinkConnection = TypedDict('PackageDependencyLinkConnection', {
	'edges': Optional[List['PackageDependencyLinkEdge']],
	'nodes': Optional[List['PackageDependencyLink']],
	'pageInfo': 'PageInfo',
})


PackageDependencyLinkEdge = TypedDict('PackageDependencyLinkEdge', {
	'cursor': str,
	'node': Optional['PackageDependencyLink'],
})


PackageDetailsType = TypedDict('PackageDetailsType', {
	'canDestroy': bool,
	'composerConfigRepositoryUrl': Optional[str],
	'composerUrl': Optional[str],
	'conanUrl': Optional[str],
	'createdAt': 'Time',
	'dependencyLinks': Optional['PackageDependencyLinkConnection'],
	'id': 'PackagesPackageID',
	'mavenUrl': Optional[str],
	'metadata': Optional['PackageMetadata'],
	'name': str,
	'npmUrl': Optional[str],
	'nugetUrl': Optional[str],
	'packageFiles': Optional['PackageFileConnection'],
	'packageType': 'PackageTypeEnum',
	'pipelines': Optional['PipelineConnection'],
	'project': 'Project',
	'pypiSetupUrl': Optional[str],
	'pypiUrl': Optional[str],
	'status': 'PackageStatus',
	'tags': Optional['PackageTagConnection'],
	'updatedAt': 'Time',
	'version': Optional[str],
	'versions': Optional['PackageConnection'],
})


PackageEdge = TypedDict('PackageEdge', {
	'cursor': str,
	'node': Optional['Package'],
})


PackageFile = TypedDict('PackageFile', {
	'createdAt': 'Time',
	'downloadPath': str,
	'fileMd5': Optional[str],
	'fileMetadata': Optional['PackageFileMetadata'],
	'fileName': str,
	'fileSha1': Optional[str],
	'fileSha256': Optional[str],
	'id': 'PackagesPackageFileID',
	'size': str,
	'updatedAt': 'Time',
})


PackageFileConnection = TypedDict('PackageFileConnection', {
	'edges': Optional[List['PackageFileEdge']],
	'nodes': Optional[List['PackageFile']],
	'pageInfo': 'PageInfo',
})


PackageFileEdge = TypedDict('PackageFileEdge', {
	'cursor': str,
	'node': Optional['PackageFile'],
})


PackageFileRegistry = TypedDict('PackageFileRegistry', {
	'createdAt': Optional['Time'],
	'id': str,
	'lastSyncFailure': Optional[str],
	'lastSyncedAt': Optional['Time'],
	'packageFileId': str,
	'retryAt': Optional['Time'],
	'retryCount': Optional[int],
	'state': Optional['RegistryState'],
})


PackageFileRegistryConnection = TypedDict('PackageFileRegistryConnection', {
	'edges': Optional[List['PackageFileRegistryEdge']],
	'nodes': Optional[List['PackageFileRegistry']],
	'pageInfo': 'PageInfo',
})


PackageFileRegistryEdge = TypedDict('PackageFileRegistryEdge', {
	'cursor': str,
	'node': Optional['PackageFileRegistry'],
})


PackageHelmDependencyType = TypedDict('PackageHelmDependencyType', {
	'alias': Optional[str],
	'condition': Optional[str],
	'enabled': Optional[bool],
	'importValues': Optional[List['JSON']],
	'name': Optional[str],
	'repository': Optional[str],
	'tags': Optional[List[str]],
	'version': Optional[str],
})


PackageHelmMaintainerType = TypedDict('PackageHelmMaintainerType', {
	'email': Optional[str],
	'name': Optional[str],
	'url': Optional[str],
})


PackageHelmMetadataType = TypedDict('PackageHelmMetadataType', {
	'annotations': Optional['JSON'],
	'apiVersion': str,
	'appVersion': Optional[str],
	'condition': Optional[str],
	'dependencies': Optional[List['PackageHelmDependencyType']],
	'deprecated': Optional[bool],
	'description': Optional[str],
	'home': Optional[str],
	'icon': Optional[str],
	'keywords': Optional[List[str]],
	'kubeVersion': Optional[str],
	'maintainers': Optional[List['PackageHelmMaintainerType']],
	'name': str,
	'sources': Optional[List[str]],
	'tags': Optional[str],
	'type': Optional[str],
	'version': str,
})


PackageSettings = TypedDict('PackageSettings', {
	'genericDuplicateExceptionRegex': Optional['UntrustedRegexp'],
	'genericDuplicatesAllowed': bool,
	'mavenDuplicateExceptionRegex': Optional['UntrustedRegexp'],
	'mavenDuplicatesAllowed': bool,
})


PackageTag = TypedDict('PackageTag', {
	'createdAt': 'Time',
	'id': str,
	'name': str,
	'updatedAt': 'Time',
})


PackageTagConnection = TypedDict('PackageTagConnection', {
	'edges': Optional[List['PackageTagEdge']],
	'nodes': Optional[List['PackageTag']],
	'pageInfo': 'PageInfo',
})


PackageTagEdge = TypedDict('PackageTagEdge', {
	'cursor': str,
	'node': Optional['PackageTag'],
})


PageInfo = TypedDict('PageInfo', {
	'endCursor': Optional[str],
	'hasNextPage': bool,
	'hasPreviousPage': bool,
	'startCursor': Optional[str],
})


PagesDeploymentRegistry = TypedDict('PagesDeploymentRegistry', {
	'createdAt': Optional['Time'],
	'id': str,
	'lastSyncFailure': Optional[str],
	'lastSyncedAt': Optional['Time'],
	'pagesDeploymentId': str,
	'retryAt': Optional['Time'],
	'retryCount': Optional[int],
	'state': Optional['RegistryState'],
})


PagesDeploymentRegistryConnection = TypedDict('PagesDeploymentRegistryConnection', {
	'edges': Optional[List['PagesDeploymentRegistryEdge']],
	'nodes': Optional[List['PagesDeploymentRegistry']],
	'pageInfo': 'PageInfo',
})


PagesDeploymentRegistryEdge = TypedDict('PagesDeploymentRegistryEdge', {
	'cursor': str,
	'node': Optional['PagesDeploymentRegistry'],
})


PathLock = TypedDict('PathLock', {
	'id': 'PathLockID',
	'path': Optional[str],
	'user': Optional['UserCore'],
})


PathLockConnection = TypedDict('PathLockConnection', {
	'edges': Optional[List['PathLockEdge']],
	'nodes': Optional[List['PathLock']],
	'pageInfo': 'PageInfo',
})


PathLockEdge = TypedDict('PathLockEdge', {
	'cursor': str,
	'node': Optional['PathLock'],
})


Pipeline = TypedDict('Pipeline', {
	'active': bool,
	'beforeSha': Optional[str],
	'cancelable': bool,
	'codeQualityReports': Optional['CodeQualityDegradationConnection'],
	'commit': Optional['Commit'],
	'commitPath': Optional[str],
	'committedAt': Optional['Time'],
	'complete': bool,
	'configSource': Optional['PipelineConfigSourceEnum'],
	'coverage': Optional[float],
	'createdAt': 'Time',
	'dastProfile': Optional['DastProfile'],
	'detailedStatus': 'DetailedStatus',
	'downstream': Optional['PipelineConnection'],
	'duration': Optional[int],
	'finishedAt': Optional['Time'],
	'id': str,
	'iid': str,
	'job': Optional['CiJob'],
	'jobArtifacts': Optional[List['CiJobArtifact']],
	'jobs': Optional['CiJobConnection'],
	'path': Optional[str],
	'project': Optional['Project'],
	'queuedDuration': Optional['Duration'],
	'ref': Optional[str],
	'refPath': Optional[str],
	'retryable': bool,
	'securityReportFindings': Optional['PipelineSecurityReportFindingConnection'],
	'securityReportSummary': Optional['SecurityReportSummary'],
	'sha': Optional[str],
	'sourceJob': Optional['CiJob'],
	'stages': Optional['CiStageConnection'],
	'startedAt': Optional['Time'],
	'status': 'PipelineStatusEnum',
	'testReportSummary': 'TestReportSummary',
	'testSuite': Optional['TestSuite'],
	'updatedAt': 'Time',
	'upstream': Optional['Pipeline'],
	'user': Optional['UserCore'],
	'userPermissions': 'PipelinePermissions',
	'usesNeeds': Optional[bool],
	'warningMessages': Optional[List['PipelineMessage']],
	'warnings': bool,
})


PipelineAnalytics = TypedDict('PipelineAnalytics', {
	'monthPipelinesLabels': Optional[List[str]],
	'monthPipelinesSuccessful': Optional[List[int]],
	'monthPipelinesTotals': Optional[List[int]],
	'pipelineTimesLabels': Optional[List[str]],
	'pipelineTimesValues': Optional[List[int]],
	'weekPipelinesLabels': Optional[List[str]],
	'weekPipelinesSuccessful': Optional[List[int]],
	'weekPipelinesTotals': Optional[List[int]],
	'yearPipelinesLabels': Optional[List[str]],
	'yearPipelinesSuccessful': Optional[List[int]],
	'yearPipelinesTotals': Optional[List[int]],
})


PipelineArtifactRegistry = TypedDict('PipelineArtifactRegistry', {
	'createdAt': Optional['Time'],
	'id': str,
	'lastSyncFailure': Optional[str],
	'lastSyncedAt': Optional['Time'],
	'pipelineArtifactId': str,
	'retryAt': Optional['Time'],
	'retryCount': Optional[int],
	'state': Optional['RegistryState'],
})


PipelineArtifactRegistryConnection = TypedDict('PipelineArtifactRegistryConnection', {
	'edges': Optional[List['PipelineArtifactRegistryEdge']],
	'nodes': Optional[List['PipelineArtifactRegistry']],
	'pageInfo': 'PageInfo',
})


PipelineArtifactRegistryEdge = TypedDict('PipelineArtifactRegistryEdge', {
	'cursor': str,
	'node': Optional['PipelineArtifactRegistry'],
})


PipelineCancelPayload = TypedDict('PipelineCancelPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
})


PipelineConnection = TypedDict('PipelineConnection', {
	'count': int,
	'edges': Optional[List['PipelineEdge']],
	'nodes': Optional[List['Pipeline']],
	'pageInfo': 'PageInfo',
})


PipelineCounts = TypedDict('PipelineCounts', {
	'all': Optional[int],
	'finished': Optional[int],
	'pending': Optional[int],
	'running': Optional[int],
})


PipelineDestroyPayload = TypedDict('PipelineDestroyPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
})


PipelineEdge = TypedDict('PipelineEdge', {
	'cursor': str,
	'node': Optional['Pipeline'],
})


PipelineMessage = TypedDict('PipelineMessage', {
	'content': str,
	'id': str,
})


PipelinePermissions = TypedDict('PipelinePermissions', {
	'adminPipeline': bool,
	'destroyPipeline': bool,
	'updatePipeline': bool,
})


PipelineRetryPayload = TypedDict('PipelineRetryPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'pipeline': Optional['Pipeline'],
})


PipelineSecurityReportFinding = TypedDict('PipelineSecurityReportFinding', {
	'assets': Optional[List['AssetType']],
	'confidence': Optional[str],
	'description': Optional[str],
	'evidence': Optional['VulnerabilityEvidence'],
	'falsePositive': Optional[bool],
	'identifiers': List['VulnerabilityIdentifier'],
	'links': Optional[List['VulnerabilityLink']],
	'location': Optional['VulnerabilityLocation'],
	'name': Optional[str],
	'project': Optional['Project'],
	'projectFingerprint': Optional[str],
	'reportType': Optional['VulnerabilityReportType'],
	'scanner': Optional['VulnerabilityScanner'],
	'severity': Optional['VulnerabilitySeverity'],
	'solution': Optional[str],
	'state': Optional['VulnerabilityState'],
	'title': Optional[str],
	'uuid': Optional[str],
})


PipelineSecurityReportFindingConnection = TypedDict('PipelineSecurityReportFindingConnection', {
	'edges': Optional[List['PipelineSecurityReportFindingEdge']],
	'nodes': Optional[List['PipelineSecurityReportFinding']],
	'pageInfo': 'PageInfo',
})


PipelineSecurityReportFindingEdge = TypedDict('PipelineSecurityReportFindingEdge', {
	'cursor': str,
	'node': Optional['PipelineSecurityReportFinding'],
})


Project = TypedDict('Project', {
	'actualRepositorySizeLimit': Optional[float],
	'agentConfigurations': Optional['AgentConfigurationConnection'],
	'alertManagementAlert': Optional['AlertManagementAlert'],
	'alertManagementAlertStatusCounts': Optional['AlertManagementAlertStatusCountsType'],
	'alertManagementAlerts': Optional['AlertManagementAlertConnection'],
	'alertManagementHttpIntegrations': Optional['AlertManagementHttpIntegrationConnection'],
	'alertManagementIntegrations': Optional['AlertManagementIntegrationConnection'],
	'alertManagementPayloadFields': Optional[List['AlertManagementPayloadAlertField']],
	'allowMergeOnSkippedPipeline': Optional[bool],
	'apiFuzzingCiConfiguration': Optional['ApiFuzzingCiConfiguration'],
	'archived': Optional[bool],
	'autocloseReferencedIssues': Optional[bool],
	'avatarUrl': Optional[str],
	'board': Optional['Board'],
	'boards': Optional['BoardConnection'],
	'ciCdSettings': Optional['ProjectCiCdSetting'],
	'ciConfigPathOrDefault': str,
	'ciJobTokenScope': Optional['CiJobTokenScopeType'],
	'ciTemplate': Optional['CiTemplate'],
	'clusterAgent': Optional['ClusterAgent'],
	'clusterAgents': Optional['ClusterAgentConnection'],
	'codeCoverageSummary': Optional['CodeCoverageSummary'],
	'complianceFrameworks': Optional['ComplianceFrameworkConnection'],
	'containerExpirationPolicy': Optional['ContainerExpirationPolicy'],
	'containerRegistryEnabled': Optional[bool],
	'containerRepositories': Optional['ContainerRepositoryConnection'],
	'containerRepositoriesCount': int,
	'corpuses': Optional['CoverageFuzzingCorpusConnection'],
	'createdAt': Optional['Time'],
	'dastProfile': Optional['DastProfile'],
	'dastProfiles': Optional['DastProfileConnection'],
	'dastScannerProfiles': Optional['DastScannerProfileConnection'],
	'dastSiteProfile': Optional['DastSiteProfile'],
	'dastSiteProfiles': Optional['DastSiteProfileConnection'],
	'dastSiteValidations': Optional['DastSiteValidationConnection'],
	'description': Optional[str],
	'descriptionHtml': Optional[str],
	'dora': Optional['Dora'],
	'environment': Optional['Environment'],
	'environments': Optional['EnvironmentConnection'],
	'forksCount': int,
	'fullPath': str,
	'grafanaIntegration': Optional['GrafanaIntegration'],
	'group': Optional['Group'],
	'httpUrlToRepo': Optional[str],
	'id': str,
	'importStatus': Optional[str],
	'incidentManagementEscalationPolicies': Optional['EscalationPolicyTypeConnection'],
	'incidentManagementEscalationPolicy': Optional['EscalationPolicyType'],
	'incidentManagementOncallSchedules': Optional['IncidentManagementOncallScheduleConnection'],
	'incidentManagementTimelineEvent': Optional['TimelineEventType'],
	'incidentManagementTimelineEvents': Optional['TimelineEventTypeConnection'],
	'issue': Optional['Issue'],
	'issueStatusCounts': Optional['IssueStatusCountsType'],
	'issues': Optional['IssueConnection'],
	'issuesEnabled': Optional[bool],
	'iterationCadences': Optional['IterationCadenceConnection'],
	'iterations': Optional['IterationConnection'],
	'jiraImportStatus': Optional[str],
	'jiraImports': Optional['JiraImportConnection'],
	'jobs': Optional['CiJobConnection'],
	'jobsEnabled': Optional[bool],
	'label': Optional['Label'],
	'labels': Optional['LabelConnection'],
	'lastActivityAt': Optional['Time'],
	'lfsEnabled': Optional[bool],
	'mergeCommitTemplate': Optional[str],
	'mergeRequest': Optional['MergeRequest'],
	'mergeRequests': Optional['MergeRequestConnection'],
	'mergeRequestsEnabled': Optional[bool],
	'mergeRequestsFfOnlyEnabled': Optional[bool],
	'milestones': Optional['MilestoneConnection'],
	'name': str,
	'nameWithNamespace': str,
	'namespace': Optional['Namespace'],
	'networkPolicies': Optional['NetworkPolicyConnection'],
	'onlyAllowMergeIfAllDiscussionsAreResolved': Optional[bool],
	'onlyAllowMergeIfPipelineSucceeds': Optional[bool],
	'openIssuesCount': Optional[int],
	'packages': Optional['PackageConnection'],
	'path': str,
	'pathLocks': Optional['PathLockConnection'],
	'pipeline': Optional['Pipeline'],
	'pipelineAnalytics': Optional['PipelineAnalytics'],
	'pipelineCounts': Optional['PipelineCounts'],
	'pipelines': Optional['PipelineConnection'],
	'printingMergeRequestLinkEnabled': Optional[bool],
	'projectMembers': Optional['MemberInterfaceConnection'],
	'publicJobs': Optional[bool],
	'pushRules': Optional['PushRules'],
	'recentIssueBoards': Optional['BoardConnection'],
	'release': Optional['Release'],
	'releases': Optional['ReleaseConnection'],
	'removeSourceBranchAfterMerge': Optional[bool],
	'repository': Optional['Repository'],
	'repositorySizeExcess': Optional[float],
	'requestAccessEnabled': Optional[bool],
	'requirement': Optional['Requirement'],
	'requirementStatesCount': Optional['RequirementStatesCount'],
	'requirements': Optional['RequirementConnection'],
	'sastCiConfiguration': Optional['SastCiConfiguration'],
	'scanExecutionPolicies': Optional['ScanExecutionPolicyConnection'],
	'scanResultPolicies': Optional['ScanResultPolicyConnection'],
	'securityDashboardPath': Optional[str],
	'securityScanners': Optional['SecurityScanners'],
	'securityTrainingProviders': Optional[List['ProjectSecurityTraining']],
	'securityTrainingUrls': Optional[List['SecurityTrainingUrl']],
	'sentryDetailedError': Optional['SentryDetailedError'],
	'sentryErrors': Optional['SentryErrorCollection'],
	'serviceDeskAddress': Optional[str],
	'serviceDeskEnabled': Optional[bool],
	'services': Optional['ServiceConnection'],
	'sharedRunnersEnabled': Optional[bool],
	'snippets': Optional['SnippetConnection'],
	'snippetsEnabled': Optional[bool],
	'squashCommitTemplate': Optional[str],
	'squashReadOnly': bool,
	'sshUrlToRepo': Optional[str],
	'starCount': int,
	'statistics': Optional['ProjectStatistics'],
	'suggestionCommitMessage': Optional[str],
	'tagList': Optional[str],
	'terraformState': Optional['TerraformState'],
	'terraformStates': Optional['TerraformStateConnection'],
	'timelogs': Optional['TimelogConnection'],
	'topics': Optional[List[str]],
	'userPermissions': 'ProjectPermissions',
	'visibility': Optional[str],
	'vulnerabilities': Optional['VulnerabilityConnection'],
	'vulnerabilitiesCountByDay': Optional['VulnerabilitiesCountByDayConnection'],
	'vulnerabilityScanners': Optional['VulnerabilityScannerConnection'],
	'vulnerabilitySeveritiesCount': Optional['VulnerabilitySeveritiesCount'],
	'webUrl': Optional[str],
	'wikiEnabled': Optional[bool],
	'workItemTypes': Optional['WorkItemTypeConnection'],
})


ProjectCiCdSetting = TypedDict('ProjectCiCdSetting', {
	'jobTokenScopeEnabled': Optional[bool],
	'keepLatestArtifact': Optional[bool],
	'mergePipelinesEnabled': Optional[bool],
	'mergeTrainsEnabled': Optional[bool],
	'project': Optional['Project'],
})


ProjectConnection = TypedDict('ProjectConnection', {
	'edges': Optional[List['ProjectEdge']],
	'nodes': Optional[List['Project']],
	'pageInfo': 'PageInfo',
})


ProjectEdge = TypedDict('ProjectEdge', {
	'cursor': str,
	'node': Optional['Project'],
})


ProjectMember = TypedDict('ProjectMember', {
	'accessLevel': Optional['AccessLevel'],
	'createdAt': Optional['Time'],
	'createdBy': Optional['UserCore'],
	'expiresAt': Optional['Time'],
	'id': str,
	'mergeRequestInteraction': Optional['UserMergeRequestInteraction'],
	'project': Optional['Project'],
	'updatedAt': Optional['Time'],
	'user': Optional['UserCore'],
	'userPermissions': 'ProjectPermissions',
})


ProjectMemberConnection = TypedDict('ProjectMemberConnection', {
	'edges': Optional[List['ProjectMemberEdge']],
	'nodes': Optional[List['ProjectMember']],
	'pageInfo': 'PageInfo',
})


ProjectMemberEdge = TypedDict('ProjectMemberEdge', {
	'cursor': str,
	'node': Optional['ProjectMember'],
})


ProjectPermissions = TypedDict('ProjectPermissions', {
	'adminOperations': bool,
	'adminPathLocks': bool,
	'adminProject': bool,
	'adminRemoteMirror': bool,
	'adminWiki': bool,
	'archiveProject': bool,
	'changeNamespace': bool,
	'changeVisibilityLevel': bool,
	'createDeployment': bool,
	'createDesign': bool,
	'createIssue': bool,
	'createLabel': bool,
	'createMergeRequestFrom': bool,
	'createMergeRequestIn': bool,
	'createPages': bool,
	'createPipeline': bool,
	'createPipelineSchedule': bool,
	'createSnippet': bool,
	'createWiki': bool,
	'destroyDesign': bool,
	'destroyPages': bool,
	'destroyWiki': bool,
	'downloadCode': bool,
	'downloadWikiCode': bool,
	'forkProject': bool,
	'pushCode': bool,
	'pushToDeleteProtectedBranch': bool,
	'readCommitStatus': bool,
	'readCycleAnalytics': bool,
	'readDesign': bool,
	'readMergeRequest': bool,
	'readPagesContent': bool,
	'readProject': bool,
	'readProjectMember': bool,
	'readWiki': bool,
	'removeForkProject': bool,
	'removePages': bool,
	'removeProject': bool,
	'renameProject': bool,
	'requestAccess': bool,
	'updatePages': bool,
	'updateWiki': bool,
	'uploadFile': bool,
})


ProjectSecurityTraining = TypedDict('ProjectSecurityTraining', {
	'description': Optional[str],
	'id': 'GlobalID',
	'isEnabled': bool,
	'isPrimary': bool,
	'logoUrl': Optional[str],
	'name': str,
	'url': str,
})


ProjectSetComplianceFrameworkPayload = TypedDict('ProjectSetComplianceFrameworkPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'project': Optional['Project'],
})


ProjectSetLockedPayload = TypedDict('ProjectSetLockedPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'project': Optional['Project'],
})


ProjectStatistics = TypedDict('ProjectStatistics', {
	'buildArtifactsSize': float,
	'commitCount': float,
	'lfsObjectsSize': float,
	'packagesSize': float,
	'pipelineArtifactsSize': Optional[float],
	'repositorySize': float,
	'snippetsSize': Optional[float],
	'storageSize': float,
	'uploadsSize': Optional[float],
	'wikiSize': Optional[float],
})


PrometheusAlert = TypedDict('PrometheusAlert', {
	'humanizedText': str,
	'id': str,
})


PrometheusIntegrationCreatePayload = TypedDict('PrometheusIntegrationCreatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'integration': Optional['AlertManagementPrometheusIntegration'],
})


PrometheusIntegrationResetTokenPayload = TypedDict('PrometheusIntegrationResetTokenPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'integration': Optional['AlertManagementPrometheusIntegration'],
})


PrometheusIntegrationUpdatePayload = TypedDict('PrometheusIntegrationUpdatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'integration': Optional['AlertManagementPrometheusIntegration'],
})


PromoteToEpicPayload = TypedDict('PromoteToEpicPayload', {
	'clientMutationId': Optional[str],
	'epic': Optional['Epic'],
	'errors': List[str],
	'issue': Optional['Issue'],
})


PushRules = TypedDict('PushRules', {
	'rejectUnsignedCommits': bool,
})


PypiMetadata = TypedDict('PypiMetadata', {
	'id': 'PackagesPypiMetadatumID',
	'requiredPython': Optional[str],
})


Query = TypedDict('Query', {
	'boardList': 'BoardListQueryResult',
	'ciApplicationSettings': 'CiApplicationSettingsQueryResult',
	'ciConfig': 'CiConfigQueryResult',
	'ciMinutesUsage': 'CiMinutesUsageQueryResult',
	'containerRepository': 'ContainerRepositoryQueryResult',
	'currentLicense': 'CurrentLicenseQueryResult',
	'currentUser': 'CurrentUserQueryResult',
	'designManagement': 'DesignManagementQueryResult',
	'devopsAdoptionEnabledNamespaces': 'DevopsAdoptionEnabledNamespacesQueryResult',
	'echo': 'EchoQueryResult',
	'geoNode': 'GeoNodeQueryResult',
	'gitpodEnabled': 'GitpodEnabledQueryResult',
	'group': 'GroupQueryResult',
	'instanceSecurityDashboard': 'InstanceSecurityDashboardQueryResult',
	'instanceStatisticsMeasurements': 'InstanceStatisticsMeasurementsQueryResult',
	'issue': 'IssueQueryResult',
	'iteration': 'IterationQueryResult',
	'licenseHistoryEntries': 'LicenseHistoryEntriesQueryResult',
	'mergeRequest': 'MergeRequestQueryResult',
	'metadata': 'MetadataQueryResult',
	'milestone': 'MilestoneQueryResult',
	'namespace': 'NamespaceQueryResult',
	'package': 'PackageQueryResult',
	'project': 'ProjectQueryResult',
	'projects': 'ProjectsQueryResult',
	'queryComplexity': 'QueryComplexityQueryResult',
	'runner': 'RunnerQueryResult',
	'runnerPlatforms': 'RunnerPlatformsQueryResult',
	'runnerSetup': 'RunnerSetupQueryResult',
	'runners': 'RunnersQueryResult',
	'snippets': 'SnippetsQueryResult',
	'subscriptionFutureEntries': 'SubscriptionFutureEntriesQueryResult',
	'timelogs': 'TimelogsQueryResult',
	'topics': 'TopicsQueryResult',
	'usageTrendsMeasurements': 'UsageTrendsMeasurementsQueryResult',
	'user': 'UserQueryResult',
	'users': 'UsersQueryResult',
	'vulnerabilities': 'VulnerabilitiesQueryResult',
	'vulnerabilitiesCountByDay': 'VulnerabilitiesCountByDayQueryResult',
	'vulnerability': 'VulnerabilityQueryResult',
	'workItem': 'WorkItemQueryResult',
})


BoardListParams = TypedDict('BoardListParams', {
	'id': 'ListID',
	'issueFilters': Optional['BoardIssueInput'],
})


BoardListQueryResult = ClassVar[Optional['BoardList']]


CiApplicationSettingsQueryResult = ClassVar[Optional['CiApplicationSettings']]


CiConfigParams = TypedDict('CiConfigParams', {
	'projectPath': str,
	'sha': Optional[str],
	'content': str,
	'dryRun': Optional[bool],
})


CiConfigQueryResult = ClassVar[Optional['CiConfig']]


CiMinutesUsageParams = TypedDict('CiMinutesUsageParams', {
	'after': Optional[str],
	'before': Optional[str],
	'first': Optional[int],
	'last': Optional[int],
	'namespaceId': Optional['NamespaceID'],
})


CiMinutesUsageQueryResult = ClassVar[Optional['CiMinutesNamespaceMonthlyUsageConnection']]


ContainerRepositoryParams = TypedDict('ContainerRepositoryParams', {
	'id': 'ContainerRepositoryID',
})


ContainerRepositoryQueryResult = ClassVar[Optional['ContainerRepositoryDetails']]


CurrentLicenseQueryResult = ClassVar[Optional['CurrentLicense']]


CurrentUserQueryResult = ClassVar[Optional['UserCore']]


DesignManagementQueryResult = ClassVar['DesignManagement']


DevopsAdoptionEnabledNamespacesParams = TypedDict('DevopsAdoptionEnabledNamespacesParams', {
	'displayNamespaceId': Optional['NamespaceID'],
	'after': Optional[str],
	'before': Optional[str],
	'first': Optional[int],
	'last': Optional[int],
})


DevopsAdoptionEnabledNamespacesQueryResult = ClassVar[Optional['DevopsAdoptionEnabledNamespaceConnection']]


EchoParams = TypedDict('EchoParams', {
	'text': str,
})


EchoQueryResult = str


GeoNodeParams = TypedDict('GeoNodeParams', {
	'name': Optional[str],
})


GeoNodeQueryResult = ClassVar[Optional['GeoNode']]


GitpodEnabledQueryResult = bool


GroupParams = TypedDict('GroupParams', {
	'fullPath': str,
})


GroupQueryResult = ClassVar[Optional['Group']]


InstanceSecurityDashboardQueryResult = ClassVar[Optional['InstanceSecurityDashboard']]


InstanceStatisticsMeasurementsParams = TypedDict('InstanceStatisticsMeasurementsParams', {
	'identifier': 'MeasurementIdentifier',
	'recordedAfter': Optional['Time'],
	'recordedBefore': Optional['Time'],
	'after': Optional[str],
	'before': Optional[str],
	'first': Optional[int],
	'last': Optional[int],
})


InstanceStatisticsMeasurementsQueryResult = ClassVar[Optional['UsageTrendsMeasurementConnection']]


IssueParams = TypedDict('IssueParams', {
	'id': 'IssueID',
})


IssueQueryResult = ClassVar[Optional['Issue']]


IterationParams = TypedDict('IterationParams', {
	'id': 'IterationID',
})


IterationQueryResult = ClassVar[Optional['Iteration']]


LicenseHistoryEntriesParams = TypedDict('LicenseHistoryEntriesParams', {
	'after': Optional[str],
	'before': Optional[str],
	'first': Optional[int],
	'last': Optional[int],
})


LicenseHistoryEntriesQueryResult = ClassVar[Optional['LicenseHistoryEntryConnection']]


MergeRequestParams = TypedDict('MergeRequestParams', {
	'id': 'MergeRequestID',
})


MergeRequestQueryResult = ClassVar[Optional['MergeRequest']]


MetadataQueryResult = ClassVar[Optional['Metadata']]


MilestoneParams = TypedDict('MilestoneParams', {
	'id': 'MilestoneID',
})


MilestoneQueryResult = ClassVar[Optional['Milestone']]


NamespaceParams = TypedDict('NamespaceParams', {
	'fullPath': str,
})


NamespaceQueryResult = ClassVar[Optional['Namespace']]


PackageParams = TypedDict('PackageParams', {
	'id': 'PackagesPackageID',
})


PackageQueryResult = ClassVar[Optional['PackageDetailsType']]


ProjectParams = TypedDict('ProjectParams', {
	'fullPath': str,
})


ProjectQueryResult = ClassVar[Optional['Project']]


ProjectsParams = TypedDict('ProjectsParams', {
	'membership': Optional[bool],
	'search': Optional[str],
	'ids': Optional[List[str]],
	'searchNamespaces': Optional[bool],
	'sort': Optional[str],
	'topics': Optional[List[str]],
	'after': Optional[str],
	'before': Optional[str],
	'first': Optional[int],
	'last': Optional[int],
})


ProjectsQueryResult = ClassVar[Optional['ProjectConnection']]


QueryComplexityQueryResult = ClassVar[Optional['QueryComplexity']]


RunnerParams = TypedDict('RunnerParams', {
	'id': 'CiRunnerID',
})


RunnerQueryResult = ClassVar[Optional['CiRunner']]


RunnerPlatformsParams = TypedDict('RunnerPlatformsParams', {
	'after': Optional[str],
	'before': Optional[str],
	'first': Optional[int],
	'last': Optional[int],
})


RunnerPlatformsQueryResult = ClassVar[Optional['RunnerPlatformConnection']]


RunnerSetupParams = TypedDict('RunnerSetupParams', {
	'platform': str,
	'architecture': str,
})


RunnerSetupQueryResult = ClassVar[Optional['RunnerSetup']]


RunnersParams = TypedDict('RunnersParams', {
	'paused': Optional[bool],
	'status': Optional['CiRunnerStatus'],
	'type': Optional['CiRunnerType'],
	'tagList': Optional[List[str]],
	'search': Optional[str],
	'sort': Optional['CiRunnerSort'],
	'after': Optional[str],
	'before': Optional[str],
	'first': Optional[int],
	'last': Optional[int],
})


RunnersQueryResult = ClassVar[Optional['CiRunnerConnection']]


SnippetsParams = TypedDict('SnippetsParams', {
	'ids': Optional[List['SnippetID']],
	'visibility': Optional['VisibilityScopesEnum'],
	'authorId': Optional['UserID'],
	'projectId': Optional['ProjectID'],
	'type': Optional['TypeEnum'],
	'explore': Optional[bool],
	'after': Optional[str],
	'before': Optional[str],
	'first': Optional[int],
	'last': Optional[int],
})


SnippetsQueryResult = ClassVar[Optional['SnippetConnection']]


SubscriptionFutureEntriesParams = TypedDict('SubscriptionFutureEntriesParams', {
	'after': Optional[str],
	'before': Optional[str],
	'first': Optional[int],
	'last': Optional[int],
})


SubscriptionFutureEntriesQueryResult = ClassVar[Optional['SubscriptionFutureEntryConnection']]


TimelogsParams = TypedDict('TimelogsParams', {
	'startDate': Optional['Time'],
	'endDate': Optional['Time'],
	'startTime': Optional['Time'],
	'endTime': Optional['Time'],
	'projectId': Optional['ProjectID'],
	'groupId': Optional['GroupID'],
	'username': Optional[str],
	'after': Optional[str],
	'before': Optional[str],
	'first': Optional[int],
	'last': Optional[int],
})


TimelogsQueryResult = ClassVar[Optional['TimelogConnection']]


TopicsParams = TypedDict('TopicsParams', {
	'search': Optional[str],
	'after': Optional[str],
	'before': Optional[str],
	'first': Optional[int],
	'last': Optional[int],
})


TopicsQueryResult = ClassVar[Optional['TopicConnection']]


UsageTrendsMeasurementsParams = TypedDict('UsageTrendsMeasurementsParams', {
	'identifier': 'MeasurementIdentifier',
	'recordedAfter': Optional['Time'],
	'recordedBefore': Optional['Time'],
	'after': Optional[str],
	'before': Optional[str],
	'first': Optional[int],
	'last': Optional[int],
})


UsageTrendsMeasurementsQueryResult = ClassVar[Optional['UsageTrendsMeasurementConnection']]


UserParams = TypedDict('UserParams', {
	'id': Optional['UserID'],
	'username': Optional[str],
})


UserQueryResult = ClassVar[Optional['UserCore']]


UsersParams = TypedDict('UsersParams', {
	'ids': Optional[List[str]],
	'usernames': Optional[List[str]],
	'sort': Optional['Sort'],
	'search': Optional[str],
	'admins': Optional[bool],
	'after': Optional[str],
	'before': Optional[str],
	'first': Optional[int],
	'last': Optional[int],
})


UsersQueryResult = ClassVar[Optional['UserCoreConnection']]


VulnerabilitiesParams = TypedDict('VulnerabilitiesParams', {
	'projectId': Optional[List[str]],
	'reportType': Optional[List['VulnerabilityReportType']],
	'severity': Optional[List['VulnerabilitySeverity']],
	'state': Optional[List['VulnerabilityState']],
	'scanner': Optional[List[str]],
	'scannerId': Optional[List['VulnerabilitiesScannerID']],
	'sort': Optional['VulnerabilitySort'],
	'hasResolution': Optional[bool],
	'hasIssues': Optional[bool],
	'image': Optional[List[str]],
	'clusterId': Optional[List['ClustersClusterID']],
	'clusterAgentId': Optional[List['ClustersAgentID']],
	'after': Optional[str],
	'before': Optional[str],
	'first': Optional[int],
	'last': Optional[int],
})


VulnerabilitiesQueryResult = ClassVar[Optional['VulnerabilityConnection']]


VulnerabilitiesCountByDayParams = TypedDict('VulnerabilitiesCountByDayParams', {
	'startDate': 'ISO8601Date',
	'endDate': 'ISO8601Date',
	'after': Optional[str],
	'before': Optional[str],
	'first': Optional[int],
	'last': Optional[int],
})


VulnerabilitiesCountByDayQueryResult = ClassVar[Optional['VulnerabilitiesCountByDayConnection']]


VulnerabilityParams = TypedDict('VulnerabilityParams', {
	'id': 'VulnerabilityID',
})


VulnerabilityQueryResult = ClassVar[Optional['Vulnerability']]


WorkItemParams = TypedDict('WorkItemParams', {
	'id': 'WorkItemID',
})


WorkItemQueryResult = ClassVar[Optional['WorkItem']]


QueryComplexity = TypedDict('QueryComplexity', {
	'limit': Optional[int],
	'score': Optional[int],
})


RecentFailures = TypedDict('RecentFailures', {
	'baseBranch': Optional[str],
	'count': Optional[int],
})


Release = TypedDict('Release', {
	'assets': Optional['ReleaseAssets'],
	'author': Optional['UserCore'],
	'commit': Optional['Commit'],
	'createdAt': Optional['Time'],
	'description': Optional[str],
	'descriptionHtml': Optional[str],
	'evidences': Optional['ReleaseEvidenceConnection'],
	'links': Optional['ReleaseLinks'],
	'milestones': Optional['MilestoneConnection'],
	'name': Optional[str],
	'releasedAt': Optional['Time'],
	'tagName': Optional[str],
	'tagPath': Optional[str],
	'upcomingRelease': Optional[bool],
})


ReleaseAssetLink = TypedDict('ReleaseAssetLink', {
	'directAssetPath': Optional[str],
	'directAssetUrl': Optional[str],
	'external': Optional[bool],
	'id': str,
	'linkType': Optional['ReleaseAssetLinkType'],
	'name': Optional[str],
	'url': Optional[str],
})


ReleaseAssetLinkConnection = TypedDict('ReleaseAssetLinkConnection', {
	'edges': Optional[List['ReleaseAssetLinkEdge']],
	'nodes': Optional[List['ReleaseAssetLink']],
	'pageInfo': 'PageInfo',
})


ReleaseAssetLinkCreatePayload = TypedDict('ReleaseAssetLinkCreatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'link': Optional['ReleaseAssetLink'],
})


ReleaseAssetLinkDeletePayload = TypedDict('ReleaseAssetLinkDeletePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'link': Optional['ReleaseAssetLink'],
})


ReleaseAssetLinkEdge = TypedDict('ReleaseAssetLinkEdge', {
	'cursor': str,
	'node': Optional['ReleaseAssetLink'],
})


ReleaseAssetLinkUpdatePayload = TypedDict('ReleaseAssetLinkUpdatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'link': Optional['ReleaseAssetLink'],
})


ReleaseAssets = TypedDict('ReleaseAssets', {
	'count': Optional[int],
	'links': Optional['ReleaseAssetLinkConnection'],
	'sources': Optional['ReleaseSourceConnection'],
})


ReleaseConnection = TypedDict('ReleaseConnection', {
	'count': int,
	'edges': Optional[List['ReleaseEdge']],
	'nodes': Optional[List['Release']],
	'pageInfo': 'PageInfo',
})


ReleaseCreatePayload = TypedDict('ReleaseCreatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'release': Optional['Release'],
})


ReleaseDeletePayload = TypedDict('ReleaseDeletePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'release': Optional['Release'],
})


ReleaseEdge = TypedDict('ReleaseEdge', {
	'cursor': str,
	'node': Optional['Release'],
})


ReleaseEvidence = TypedDict('ReleaseEvidence', {
	'collectedAt': Optional['Time'],
	'filepath': Optional[str],
	'id': str,
	'sha': Optional[str],
})


ReleaseEvidenceConnection = TypedDict('ReleaseEvidenceConnection', {
	'edges': Optional[List['ReleaseEvidenceEdge']],
	'nodes': Optional[List['ReleaseEvidence']],
	'pageInfo': 'PageInfo',
})


ReleaseEvidenceEdge = TypedDict('ReleaseEvidenceEdge', {
	'cursor': str,
	'node': Optional['ReleaseEvidence'],
})


ReleaseLinks = TypedDict('ReleaseLinks', {
	'closedIssuesUrl': Optional[str],
	'closedMergeRequestsUrl': Optional[str],
	'editUrl': Optional[str],
	'mergedMergeRequestsUrl': Optional[str],
	'openedIssuesUrl': Optional[str],
	'openedMergeRequestsUrl': Optional[str],
	'selfUrl': Optional[str],
})


ReleaseSource = TypedDict('ReleaseSource', {
	'format': Optional[str],
	'url': Optional[str],
})


ReleaseSourceConnection = TypedDict('ReleaseSourceConnection', {
	'edges': Optional[List['ReleaseSourceEdge']],
	'nodes': Optional[List['ReleaseSource']],
	'pageInfo': 'PageInfo',
})


ReleaseSourceEdge = TypedDict('ReleaseSourceEdge', {
	'cursor': str,
	'node': Optional['ReleaseSource'],
})


ReleaseUpdatePayload = TypedDict('ReleaseUpdatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'release': Optional['Release'],
})


RemoveProjectFromSecurityDashboardPayload = TypedDict('RemoveProjectFromSecurityDashboardPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
})


RepositionImageDiffNotePayload = TypedDict('RepositionImageDiffNotePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'note': Optional['Note'],
})


Repository = TypedDict('Repository', {
	'blobs': Optional['RepositoryBlobConnection'],
	'branchNames': Optional[List[str]],
	'diskPath': Optional[str],
	'empty': bool,
	'exists': bool,
	'paginatedTree': Optional['TreeConnection'],
	'rootRef': Optional[str],
	'tree': Optional['Tree'],
})


RepositoryBlob = TypedDict('RepositoryBlob', {
	'archived': Optional[bool],
	'blamePath': Optional[str],
	'canCurrentUserPushToBranch': Optional[bool],
	'canModifyBlob': Optional[bool],
	'codeNavigationPath': Optional[str],
	'codeOwners': Optional[List['UserCore']],
	'editBlobPath': Optional[str],
	'environmentExternalUrlForRouteMap': Optional[str],
	'environmentFormattedExternalUrl': Optional[str],
	'externalStorage': Optional[str],
	'externalStorageUrl': Optional[str],
	'fileType': Optional[str],
	'findFilePath': Optional[str],
	'forkAndEditPath': Optional[str],
	'forkAndViewPath': Optional[str],
	'gitpodBlobUrl': Optional[str],
	'historyPath': Optional[str],
	'id': str,
	'ideEditPath': Optional[str],
	'ideForkAndEditPath': Optional[str],
	'language': Optional[str],
	'lfsOid': Optional[str],
	'mode': Optional[str],
	'name': Optional[str],
	'oid': str,
	'path': str,
	'permalinkPath': Optional[str],
	'pipelineEditorPath': Optional[str],
	'plainData': Optional[str],
	'projectBlobPathRoot': Optional[str],
	'rawBlob': Optional[str],
	'rawPath': Optional[str],
	'rawSize': Optional[int],
	'rawTextBlob': Optional[str],
	'replacePath': Optional[str],
	'richViewer': Optional['BlobViewer'],
	'simpleViewer': 'BlobViewer',
	'size': Optional[int],
	'storedExternally': Optional[bool],
	'webPath': Optional[str],
})


RepositoryBlobConnection = TypedDict('RepositoryBlobConnection', {
	'edges': Optional[List['RepositoryBlobEdge']],
	'nodes': Optional[List['RepositoryBlob']],
	'pageInfo': 'PageInfo',
})


RepositoryBlobEdge = TypedDict('RepositoryBlobEdge', {
	'cursor': str,
	'node': Optional['RepositoryBlob'],
})


Requirement = TypedDict('Requirement', {
	'author': 'UserCore',
	'createdAt': 'Time',
	'description': Optional[str],
	'descriptionHtml': Optional[str],
	'id': str,
	'iid': str,
	'lastTestReportManuallyCreated': Optional[bool],
	'lastTestReportState': Optional['TestReportState'],
	'project': 'Project',
	'state': 'RequirementState',
	'testReports': Optional['TestReportConnection'],
	'title': Optional[str],
	'titleHtml': Optional[str],
	'updatedAt': 'Time',
	'userPermissions': 'RequirementPermissions',
})


RequirementConnection = TypedDict('RequirementConnection', {
	'edges': Optional[List['RequirementEdge']],
	'nodes': Optional[List['Requirement']],
	'pageInfo': 'PageInfo',
})


RequirementEdge = TypedDict('RequirementEdge', {
	'cursor': str,
	'node': Optional['Requirement'],
})


RequirementPermissions = TypedDict('RequirementPermissions', {
	'adminRequirement': bool,
	'createRequirement': bool,
	'destroyRequirement': bool,
	'readRequirement': bool,
	'updateRequirement': bool,
})


RequirementStatesCount = TypedDict('RequirementStatesCount', {
	'archived': Optional[int],
	'opened': Optional[int],
})


RootStorageStatistics = TypedDict('RootStorageStatistics', {
	'buildArtifactsSize': float,
	'dependencyProxySize': float,
	'lfsObjectsSize': float,
	'packagesSize': float,
	'pipelineArtifactsSize': float,
	'repositorySize': float,
	'snippetsSize': float,
	'storageSize': float,
	'uploadsSize': float,
	'wikiSize': float,
})


RunnerArchitecture = TypedDict('RunnerArchitecture', {
	'downloadLocation': str,
	'name': str,
})


RunnerArchitectureConnection = TypedDict('RunnerArchitectureConnection', {
	'edges': Optional[List['RunnerArchitectureEdge']],
	'nodes': Optional[List['RunnerArchitecture']],
	'pageInfo': 'PageInfo',
})


RunnerArchitectureEdge = TypedDict('RunnerArchitectureEdge', {
	'cursor': str,
	'node': Optional['RunnerArchitecture'],
})


RunnerDeletePayload = TypedDict('RunnerDeletePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
})


RunnerPermissions = TypedDict('RunnerPermissions', {
	'deleteRunner': bool,
	'readRunner': bool,
	'updateRunner': bool,
})


RunnerPlatform = TypedDict('RunnerPlatform', {
	'architectures': Optional['RunnerArchitectureConnection'],
	'humanReadableName': str,
	'name': str,
})


RunnerPlatformConnection = TypedDict('RunnerPlatformConnection', {
	'edges': Optional[List['RunnerPlatformEdge']],
	'nodes': Optional[List['RunnerPlatform']],
	'pageInfo': 'PageInfo',
})


RunnerPlatformEdge = TypedDict('RunnerPlatformEdge', {
	'cursor': str,
	'node': Optional['RunnerPlatform'],
})


RunnerSetup = TypedDict('RunnerSetup', {
	'installInstructions': str,
	'registerInstructions': Optional[str],
})


RunnerUpdatePayload = TypedDict('RunnerUpdatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'runner': Optional['CiRunner'],
})


RunnersRegistrationTokenResetPayload = TypedDict('RunnersRegistrationTokenResetPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'token': Optional[str],
})


SastCiConfiguration = TypedDict('SastCiConfiguration', {
	'analyzers': Optional['SastCiConfigurationAnalyzersEntityConnection'],
	'global': Optional['SastCiConfigurationEntityConnection'],
	'pipeline': Optional['SastCiConfigurationEntityConnection'],
})


SastCiConfigurationAnalyzersEntity = TypedDict('SastCiConfigurationAnalyzersEntity', {
	'description': Optional[str],
	'enabled': Optional[bool],
	'label': Optional[str],
	'name': Optional[str],
	'variables': Optional['SastCiConfigurationEntityConnection'],
})


SastCiConfigurationAnalyzersEntityConnection = TypedDict('SastCiConfigurationAnalyzersEntityConnection', {
	'edges': Optional[List['SastCiConfigurationAnalyzersEntityEdge']],
	'nodes': Optional[List['SastCiConfigurationAnalyzersEntity']],
	'pageInfo': 'PageInfo',
})


SastCiConfigurationAnalyzersEntityEdge = TypedDict('SastCiConfigurationAnalyzersEntityEdge', {
	'cursor': str,
	'node': Optional['SastCiConfigurationAnalyzersEntity'],
})


SastCiConfigurationEntity = TypedDict('SastCiConfigurationEntity', {
	'defaultValue': Optional[str],
	'description': Optional[str],
	'field': Optional[str],
	'label': Optional[str],
	'options': Optional['SastCiConfigurationOptionsEntityConnection'],
	'size': Optional['SastUiComponentSize'],
	'type': Optional[str],
	'value': Optional[str],
})


SastCiConfigurationEntityConnection = TypedDict('SastCiConfigurationEntityConnection', {
	'edges': Optional[List['SastCiConfigurationEntityEdge']],
	'nodes': Optional[List['SastCiConfigurationEntity']],
	'pageInfo': 'PageInfo',
})


SastCiConfigurationEntityEdge = TypedDict('SastCiConfigurationEntityEdge', {
	'cursor': str,
	'node': Optional['SastCiConfigurationEntity'],
})


SastCiConfigurationOptionsEntity = TypedDict('SastCiConfigurationOptionsEntity', {
	'label': Optional[str],
	'value': Optional[str],
})


SastCiConfigurationOptionsEntityConnection = TypedDict('SastCiConfigurationOptionsEntityConnection', {
	'edges': Optional[List['SastCiConfigurationOptionsEntityEdge']],
	'nodes': Optional[List['SastCiConfigurationOptionsEntity']],
	'pageInfo': 'PageInfo',
})


SastCiConfigurationOptionsEntityEdge = TypedDict('SastCiConfigurationOptionsEntityEdge', {
	'cursor': str,
	'node': Optional['SastCiConfigurationOptionsEntity'],
})


SavedReply = TypedDict('SavedReply', {
	'content': str,
	'id': 'UsersSavedReplyID',
	'name': str,
})


SavedReplyConnection = TypedDict('SavedReplyConnection', {
	'edges': Optional[List['SavedReplyEdge']],
	'nodes': Optional[List['SavedReply']],
	'pageInfo': 'PageInfo',
})


SavedReplyCreatePayload = TypedDict('SavedReplyCreatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'savedReply': Optional['SavedReply'],
})


SavedReplyDestroyPayload = TypedDict('SavedReplyDestroyPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'savedReply': Optional['SavedReply'],
})


SavedReplyEdge = TypedDict('SavedReplyEdge', {
	'cursor': str,
	'node': Optional['SavedReply'],
})


SavedReplyUpdatePayload = TypedDict('SavedReplyUpdatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'savedReply': Optional['SavedReply'],
})


Scan = TypedDict('Scan', {
	'errors': List[str],
	'name': str,
	'status': 'ScanStatus',
	'warnings': List[str],
})


ScanConnection = TypedDict('ScanConnection', {
	'edges': Optional[List['ScanEdge']],
	'nodes': Optional[List['Scan']],
	'pageInfo': 'PageInfo',
})


ScanEdge = TypedDict('ScanEdge', {
	'cursor': str,
	'node': Optional['Scan'],
})


ScanExecutionPolicy = TypedDict('ScanExecutionPolicy', {
	'description': str,
	'enabled': bool,
	'name': str,
	'updatedAt': 'Time',
	'yaml': str,
})


ScanExecutionPolicyCommitPayload = TypedDict('ScanExecutionPolicyCommitPayload', {
	'branch': Optional[str],
	'clientMutationId': Optional[str],
	'errors': List[str],
})


ScanExecutionPolicyConnection = TypedDict('ScanExecutionPolicyConnection', {
	'edges': Optional[List['ScanExecutionPolicyEdge']],
	'nodes': Optional[List['ScanExecutionPolicy']],
	'pageInfo': 'PageInfo',
})


ScanExecutionPolicyEdge = TypedDict('ScanExecutionPolicyEdge', {
	'cursor': str,
	'node': Optional['ScanExecutionPolicy'],
})


ScanResultPolicy = TypedDict('ScanResultPolicy', {
	'description': str,
	'enabled': bool,
	'name': str,
	'updatedAt': 'Time',
	'yaml': str,
})


ScanResultPolicyConnection = TypedDict('ScanResultPolicyConnection', {
	'edges': Optional[List['ScanResultPolicyEdge']],
	'nodes': Optional[List['ScanResultPolicy']],
	'pageInfo': 'PageInfo',
})


ScanResultPolicyEdge = TypedDict('ScanResultPolicyEdge', {
	'cursor': str,
	'node': Optional['ScanResultPolicy'],
})


ScannedResource = TypedDict('ScannedResource', {
	'requestMethod': Optional[str],
	'url': Optional[str],
})


ScannedResourceConnection = TypedDict('ScannedResourceConnection', {
	'edges': Optional[List['ScannedResourceEdge']],
	'nodes': Optional[List['ScannedResource']],
	'pageInfo': 'PageInfo',
})


ScannedResourceEdge = TypedDict('ScannedResourceEdge', {
	'cursor': str,
	'node': Optional['ScannedResource'],
})


SecurityPolicyProjectAssignPayload = TypedDict('SecurityPolicyProjectAssignPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
})


SecurityPolicyProjectCreatePayload = TypedDict('SecurityPolicyProjectCreatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'project': Optional['Project'],
})


SecurityPolicyProjectUnassignPayload = TypedDict('SecurityPolicyProjectUnassignPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
})


SecurityReportSummary = TypedDict('SecurityReportSummary', {
	'apiFuzzing': Optional['SecurityReportSummarySection'],
	'clusterImageScanning': Optional['SecurityReportSummarySection'],
	'containerScanning': Optional['SecurityReportSummarySection'],
	'coverageFuzzing': Optional['SecurityReportSummarySection'],
	'dast': Optional['SecurityReportSummarySection'],
	'dependencyScanning': Optional['SecurityReportSummarySection'],
	'generic': Optional['SecurityReportSummarySection'],
	'sast': Optional['SecurityReportSummarySection'],
	'secretDetection': Optional['SecurityReportSummarySection'],
})


SecurityReportSummarySection = TypedDict('SecurityReportSummarySection', {
	'scannedResources': Optional['ScannedResourceConnection'],
	'scannedResourcesCount': Optional[int],
	'scannedResourcesCsvPath': Optional[str],
	'scans': 'ScanConnection',
	'vulnerabilitiesCount': Optional[int],
})


SecurityScanners = TypedDict('SecurityScanners', {
	'available': Optional[List['SecurityScannerType']],
	'enabled': Optional[List['SecurityScannerType']],
	'pipelineRun': Optional[List['SecurityScannerType']],
})


SecurityTrainingUpdatePayload = TypedDict('SecurityTrainingUpdatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'training': Optional['ProjectSecurityTraining'],
})


SecurityTrainingUrl = TypedDict('SecurityTrainingUrl', {
	'name': Optional[str],
	'status': Optional['TrainingUrlRequestStatus'],
	'url': Optional[str],
})


SentryDetailedError = TypedDict('SentryDetailedError', {
	'count': int,
	'culprit': str,
	'externalBaseUrl': str,
	'externalUrl': str,
	'firstReleaseLastCommit': Optional[str],
	'firstReleaseShortVersion': Optional[str],
	'firstReleaseVersion': Optional[str],
	'firstSeen': 'Time',
	'frequency': List['SentryErrorFrequency'],
	'gitlabCommit': Optional[str],
	'gitlabCommitPath': Optional[str],
	'gitlabIssuePath': Optional[str],
	'id': str,
	'integrated': Optional[bool],
	'lastReleaseLastCommit': Optional[str],
	'lastReleaseShortVersion': Optional[str],
	'lastReleaseVersion': Optional[str],
	'lastSeen': 'Time',
	'message': Optional[str],
	'sentryId': str,
	'sentryProjectId': str,
	'sentryProjectName': str,
	'sentryProjectSlug': str,
	'shortId': str,
	'status': 'SentryErrorStatus',
	'tags': 'SentryErrorTags',
	'title': str,
	'type': str,
	'userCount': int,
})


SentryError = TypedDict('SentryError', {
	'count': int,
	'culprit': str,
	'externalUrl': str,
	'firstSeen': 'Time',
	'frequency': List['SentryErrorFrequency'],
	'id': str,
	'lastSeen': 'Time',
	'message': Optional[str],
	'sentryId': str,
	'sentryProjectId': str,
	'sentryProjectName': str,
	'sentryProjectSlug': str,
	'shortId': str,
	'status': 'SentryErrorStatus',
	'title': str,
	'type': str,
	'userCount': int,
})


SentryErrorCollection = TypedDict('SentryErrorCollection', {
	'detailedError': Optional['SentryDetailedError'],
	'errorStackTrace': Optional['SentryErrorStackTrace'],
	'errors': Optional['SentryErrorConnection'],
	'externalUrl': Optional[str],
})


SentryErrorConnection = TypedDict('SentryErrorConnection', {
	'edges': Optional[List['SentryErrorEdge']],
	'nodes': Optional[List['SentryError']],
	'pageInfo': 'PageInfo',
})


SentryErrorEdge = TypedDict('SentryErrorEdge', {
	'cursor': str,
	'node': Optional['SentryError'],
})


SentryErrorFrequency = TypedDict('SentryErrorFrequency', {
	'count': int,
	'time': 'Time',
})


SentryErrorStackTrace = TypedDict('SentryErrorStackTrace', {
	'dateReceived': str,
	'issueId': str,
	'stackTraceEntries': List['SentryErrorStackTraceEntry'],
})


SentryErrorStackTraceContext = TypedDict('SentryErrorStackTraceContext', {
	'code': str,
	'line': int,
})


SentryErrorStackTraceEntry = TypedDict('SentryErrorStackTraceEntry', {
	'col': Optional[str],
	'fileName': Optional[str],
	'function': Optional[str],
	'line': Optional[str],
	'traceContext': Optional[List['SentryErrorStackTraceContext']],
})


SentryErrorTags = TypedDict('SentryErrorTags', {
	'level': Optional[str],
	'logger': Optional[str],
})


ServiceConnection = TypedDict('ServiceConnection', {
	'edges': Optional[List['ServiceEdge']],
	'nodes': Optional[List['Service']],
	'pageInfo': 'PageInfo',
})


ServiceEdge = TypedDict('ServiceEdge', {
	'cursor': str,
	'node': Optional['Service'],
})


Snippet = TypedDict('Snippet', {
	'author': Optional['UserCore'],
	'blobs': Optional['SnippetBlobConnection'],
	'createdAt': 'Time',
	'description': Optional[str],
	'descriptionHtml': Optional[str],
	'discussions': 'DiscussionConnection',
	'fileName': Optional[str],
	'httpUrlToRepo': Optional[str],
	'id': 'SnippetID',
	'notes': 'NoteConnection',
	'project': Optional['Project'],
	'rawUrl': str,
	'sshUrlToRepo': Optional[str],
	'title': str,
	'updatedAt': 'Time',
	'userPermissions': 'SnippetPermissions',
	'visibilityLevel': 'VisibilityLevelsEnum',
	'webUrl': str,
})


SnippetBlob = TypedDict('SnippetBlob', {
	'binary': bool,
	'externalStorage': Optional[str],
	'mode': Optional[str],
	'name': Optional[str],
	'path': Optional[str],
	'plainData': Optional[str],
	'rawPath': str,
	'rawPlainData': Optional[str],
	'renderedAsText': bool,
	'richData': Optional[str],
	'richViewer': Optional['SnippetBlobViewer'],
	'simpleViewer': 'SnippetBlobViewer',
	'size': int,
})


SnippetBlobConnection = TypedDict('SnippetBlobConnection', {
	'edges': Optional[List['SnippetBlobEdge']],
	'hasUnretrievableBlobs': bool,
	'nodes': Optional[List['SnippetBlob']],
	'pageInfo': 'PageInfo',
})


SnippetBlobEdge = TypedDict('SnippetBlobEdge', {
	'cursor': str,
	'node': Optional['SnippetBlob'],
})


SnippetBlobViewer = TypedDict('SnippetBlobViewer', {
	'collapsed': bool,
	'fileType': str,
	'loadAsync': bool,
	'loadingPartialName': str,
	'renderError': Optional[str],
	'tooLarge': bool,
	'type': 'BlobViewersType',
})


SnippetConnection = TypedDict('SnippetConnection', {
	'edges': Optional[List['SnippetEdge']],
	'nodes': Optional[List['Snippet']],
	'pageInfo': 'PageInfo',
})


SnippetEdge = TypedDict('SnippetEdge', {
	'cursor': str,
	'node': Optional['Snippet'],
})


SnippetPermissions = TypedDict('SnippetPermissions', {
	'adminSnippet': bool,
	'awardEmoji': bool,
	'createNote': bool,
	'readSnippet': bool,
	'reportSnippet': bool,
	'updateSnippet': bool,
})


SnippetRepositoryRegistry = TypedDict('SnippetRepositoryRegistry', {
	'createdAt': Optional['Time'],
	'id': str,
	'lastSyncFailure': Optional[str],
	'lastSyncedAt': Optional['Time'],
	'retryAt': Optional['Time'],
	'retryCount': Optional[int],
	'snippetRepositoryId': str,
	'state': Optional['RegistryState'],
})


SnippetRepositoryRegistryConnection = TypedDict('SnippetRepositoryRegistryConnection', {
	'edges': Optional[List['SnippetRepositoryRegistryEdge']],
	'nodes': Optional[List['SnippetRepositoryRegistry']],
	'pageInfo': 'PageInfo',
})


SnippetRepositoryRegistryEdge = TypedDict('SnippetRepositoryRegistryEdge', {
	'cursor': str,
	'node': Optional['SnippetRepositoryRegistry'],
})


StatusAction = TypedDict('StatusAction', {
	'buttonTitle': Optional[str],
	'icon': Optional[str],
	'id': str,
	'method': Optional[str],
	'path': Optional[str],
	'title': Optional[str],
})


Submodule = TypedDict('Submodule', {
	'flatPath': str,
	'id': str,
	'name': str,
	'path': str,
	'sha': str,
	'treeUrl': Optional[str],
	'type': 'EntryType',
	'webUrl': Optional[str],
})


SubmoduleConnection = TypedDict('SubmoduleConnection', {
	'edges': Optional[List['SubmoduleEdge']],
	'nodes': Optional[List['Submodule']],
	'pageInfo': 'PageInfo',
})


SubmoduleEdge = TypedDict('SubmoduleEdge', {
	'cursor': str,
	'node': Optional['Submodule'],
})


Subscription = TypedDict('Subscription', {
	'issuableAssigneesUpdated': 'IssuableAssigneesUpdatedSubscriptionResult',
	'issuableTitleUpdated': 'IssuableTitleUpdatedSubscriptionResult',
	'issueCrmContactsUpdated': 'IssueCrmContactsUpdatedSubscriptionResult',
})


IssuableAssigneesUpdatedParams = TypedDict('IssuableAssigneesUpdatedParams', {
	'issuableId': 'IssuableID',
})


IssuableAssigneesUpdatedSubscriptionResult = ClassVar[Optional['Issuable']]


IssuableTitleUpdatedParams = TypedDict('IssuableTitleUpdatedParams', {
	'issuableId': 'IssuableID',
})


IssuableTitleUpdatedSubscriptionResult = ClassVar[Optional['Issuable']]


IssueCrmContactsUpdatedParams = TypedDict('IssueCrmContactsUpdatedParams', {
	'issuableId': 'IssuableID',
})


IssueCrmContactsUpdatedSubscriptionResult = ClassVar[Optional['Issuable']]


SubscriptionFutureEntry = TypedDict('SubscriptionFutureEntry', {
	'company': Optional[str],
	'email': Optional[str],
	'expiresAt': Optional['Date'],
	'name': Optional[str],
	'plan': str,
	'startsAt': Optional['Date'],
	'type': str,
	'usersInLicenseCount': Optional[int],
})


SubscriptionFutureEntryConnection = TypedDict('SubscriptionFutureEntryConnection', {
	'edges': Optional[List['SubscriptionFutureEntryEdge']],
	'nodes': Optional[List['SubscriptionFutureEntry']],
	'pageInfo': 'PageInfo',
})


SubscriptionFutureEntryEdge = TypedDict('SubscriptionFutureEntryEdge', {
	'cursor': str,
	'node': Optional['SubscriptionFutureEntry'],
})


TaskCompletionStatus = TypedDict('TaskCompletionStatus', {
	'completedCount': int,
	'count': int,
})


TerraformState = TypedDict('TerraformState', {
	'createdAt': 'Time',
	'id': str,
	'latestVersion': Optional['TerraformStateVersion'],
	'lockedAt': Optional['Time'],
	'lockedByUser': Optional['UserCore'],
	'name': str,
	'updatedAt': 'Time',
})


TerraformStateConnection = TypedDict('TerraformStateConnection', {
	'count': int,
	'edges': Optional[List['TerraformStateEdge']],
	'nodes': Optional[List['TerraformState']],
	'pageInfo': 'PageInfo',
})


TerraformStateDeletePayload = TypedDict('TerraformStateDeletePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
})


TerraformStateEdge = TypedDict('TerraformStateEdge', {
	'cursor': str,
	'node': Optional['TerraformState'],
})


TerraformStateLockPayload = TypedDict('TerraformStateLockPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
})


TerraformStateUnlockPayload = TypedDict('TerraformStateUnlockPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
})


TerraformStateVersion = TypedDict('TerraformStateVersion', {
	'createdAt': 'Time',
	'createdByUser': Optional['UserCore'],
	'downloadPath': Optional[str],
	'id': str,
	'job': Optional['CiJob'],
	'serial': Optional[int],
	'updatedAt': 'Time',
})


TerraformStateVersionRegistry = TypedDict('TerraformStateVersionRegistry', {
	'createdAt': Optional['Time'],
	'id': str,
	'lastSyncFailure': Optional[str],
	'lastSyncedAt': Optional['Time'],
	'retryAt': Optional['Time'],
	'retryCount': Optional[int],
	'state': Optional['RegistryState'],
	'terraformStateVersionId': str,
})


TerraformStateVersionRegistryConnection = TypedDict('TerraformStateVersionRegistryConnection', {
	'edges': Optional[List['TerraformStateVersionRegistryEdge']],
	'nodes': Optional[List['TerraformStateVersionRegistry']],
	'pageInfo': 'PageInfo',
})


TerraformStateVersionRegistryEdge = TypedDict('TerraformStateVersionRegistryEdge', {
	'cursor': str,
	'node': Optional['TerraformStateVersionRegistry'],
})


TestCase = TypedDict('TestCase', {
	'attachmentUrl': Optional[str],
	'classname': Optional[str],
	'executionTime': Optional[float],
	'file': Optional[str],
	'name': Optional[str],
	'recentFailures': Optional['RecentFailures'],
	'stackTrace': Optional[str],
	'status': Optional['TestCaseStatus'],
	'systemOutput': Optional[str],
})


TestCaseConnection = TypedDict('TestCaseConnection', {
	'count': int,
	'edges': Optional[List['TestCaseEdge']],
	'nodes': Optional[List['TestCase']],
	'pageInfo': 'PageInfo',
})


TestCaseEdge = TypedDict('TestCaseEdge', {
	'cursor': str,
	'node': Optional['TestCase'],
})


TestReport = TypedDict('TestReport', {
	'author': Optional['UserCore'],
	'createdAt': 'Time',
	'id': str,
	'state': 'TestReportState',
})


TestReportConnection = TypedDict('TestReportConnection', {
	'edges': Optional[List['TestReportEdge']],
	'nodes': Optional[List['TestReport']],
	'pageInfo': 'PageInfo',
})


TestReportEdge = TypedDict('TestReportEdge', {
	'cursor': str,
	'node': Optional['TestReport'],
})


TestReportSummary = TypedDict('TestReportSummary', {
	'testSuites': 'TestSuiteSummaryConnection',
	'total': 'TestReportTotal',
})


TestReportTotal = TypedDict('TestReportTotal', {
	'count': Optional[int],
	'error': Optional[int],
	'failed': Optional[int],
	'skipped': Optional[int],
	'success': Optional[int],
	'suiteError': Optional[str],
	'time': Optional[float],
})


TestSuite = TypedDict('TestSuite', {
	'errorCount': Optional[int],
	'failedCount': Optional[int],
	'name': Optional[str],
	'skippedCount': Optional[int],
	'successCount': Optional[int],
	'suiteError': Optional[str],
	'testCases': Optional['TestCaseConnection'],
	'totalCount': Optional[int],
	'totalTime': Optional[float],
})


TestSuiteSummary = TypedDict('TestSuiteSummary', {
	'buildIds': Optional[List[str]],
	'errorCount': Optional[int],
	'failedCount': Optional[int],
	'name': Optional[str],
	'skippedCount': Optional[int],
	'successCount': Optional[int],
	'suiteError': Optional[str],
	'totalCount': Optional[int],
	'totalTime': Optional[float],
})


TestSuiteSummaryConnection = TypedDict('TestSuiteSummaryConnection', {
	'count': int,
	'edges': Optional[List['TestSuiteSummaryEdge']],
	'nodes': Optional[List['TestSuiteSummary']],
	'pageInfo': 'PageInfo',
})


TestSuiteSummaryEdge = TypedDict('TestSuiteSummaryEdge', {
	'cursor': str,
	'node': Optional['TestSuiteSummary'],
})


TimeReportStats = TypedDict('TimeReportStats', {
	'complete': Optional['TimeboxMetrics'],
	'incomplete': Optional['TimeboxMetrics'],
	'total': Optional['TimeboxMetrics'],
})


TimeboxMetrics = TypedDict('TimeboxMetrics', {
	'count': int,
	'weight': int,
})


TimeboxReport = TypedDict('TimeboxReport', {
	'burnupTimeSeries': Optional[List['BurnupChartDailyTotals']],
	'stats': Optional['TimeReportStats'],
})


TimelineEventCreatePayload = TypedDict('TimelineEventCreatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'timelineEvent': Optional['TimelineEventType'],
})


TimelineEventDestroyPayload = TypedDict('TimelineEventDestroyPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'timelineEvent': Optional['TimelineEventType'],
})


TimelineEventPromoteFromNotePayload = TypedDict('TimelineEventPromoteFromNotePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'timelineEvent': Optional['TimelineEventType'],
})


TimelineEventType = TypedDict('TimelineEventType', {
	'action': str,
	'author': Optional['UserCore'],
	'createdAt': 'Time',
	'editable': bool,
	'id': 'IncidentManagementTimelineEventID',
	'incident': 'Issue',
	'note': Optional[str],
	'noteHtml': Optional[str],
	'occurredAt': 'Time',
	'promotedFromNote': Optional['Note'],
	'updatedAt': 'Time',
	'updatedByUser': Optional['UserCore'],
})


TimelineEventTypeConnection = TypedDict('TimelineEventTypeConnection', {
	'edges': Optional[List['TimelineEventTypeEdge']],
	'nodes': Optional[List['TimelineEventType']],
	'pageInfo': 'PageInfo',
})


TimelineEventTypeEdge = TypedDict('TimelineEventTypeEdge', {
	'cursor': str,
	'node': Optional['TimelineEventType'],
})


TimelineEventUpdatePayload = TypedDict('TimelineEventUpdatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'timelineEvent': Optional['TimelineEventType'],
})


Timelog = TypedDict('Timelog', {
	'issue': Optional['Issue'],
	'mergeRequest': Optional['MergeRequest'],
	'note': Optional['Note'],
	'spentAt': Optional['Time'],
	'summary': Optional[str],
	'timeSpent': int,
	'user': 'UserCore',
})


TimelogConnection = TypedDict('TimelogConnection', {
	'edges': Optional[List['TimelogEdge']],
	'nodes': Optional[List['Timelog']],
	'pageInfo': 'PageInfo',
})


TimelogEdge = TypedDict('TimelogEdge', {
	'cursor': str,
	'node': Optional['Timelog'],
})


Todo = TypedDict('Todo', {
	'action': 'TodoActionEnum',
	'author': 'UserCore',
	'body': str,
	'createdAt': 'Time',
	'group': Optional['Group'],
	'id': str,
	'project': Optional['Project'],
	'state': 'TodoStateEnum',
	'target': 'Todoable',
	'targetType': 'TodoTargetEnum',
})


TodoConnection = TypedDict('TodoConnection', {
	'edges': Optional[List['TodoEdge']],
	'nodes': Optional[List['Todo']],
	'pageInfo': 'PageInfo',
})


TodoCreatePayload = TypedDict('TodoCreatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'todo': Optional['Todo'],
})


TodoEdge = TypedDict('TodoEdge', {
	'cursor': str,
	'node': Optional['Todo'],
})


TodoMarkDonePayload = TypedDict('TodoMarkDonePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'todo': 'Todo',
})


TodoRestoreManyPayload = TypedDict('TodoRestoreManyPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'todos': List['Todo'],
})


TodoRestorePayload = TypedDict('TodoRestorePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'todo': 'Todo',
})


TodosMarkAllDonePayload = TypedDict('TodosMarkAllDonePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'todos': List['Todo'],
})


Topic = TypedDict('Topic', {
	'avatarUrl': Optional[str],
	'description': Optional[str],
	'descriptionHtml': Optional[str],
	'id': str,
	'name': str,
})


TopicConnection = TypedDict('TopicConnection', {
	'edges': Optional[List['TopicEdge']],
	'nodes': Optional[List['Topic']],
	'pageInfo': 'PageInfo',
})


TopicEdge = TypedDict('TopicEdge', {
	'cursor': str,
	'node': Optional['Topic'],
})


Tree = TypedDict('Tree', {
	'blobs': 'BlobConnection',
	'lastCommit': Optional['Commit'],
	'submodules': 'SubmoduleConnection',
	'trees': 'TreeEntryConnection',
})


TreeConnection = TypedDict('TreeConnection', {
	'edges': Optional[List['TreeEdge']],
	'nodes': Optional[List['Tree']],
	'pageInfo': 'PageInfo',
})


TreeEdge = TypedDict('TreeEdge', {
	'cursor': str,
	'node': Optional['Tree'],
})


TreeEntry = TypedDict('TreeEntry', {
	'flatPath': str,
	'id': str,
	'name': str,
	'path': str,
	'sha': str,
	'type': 'EntryType',
	'webPath': Optional[str],
	'webUrl': Optional[str],
})


TreeEntryConnection = TypedDict('TreeEntryConnection', {
	'edges': Optional[List['TreeEntryEdge']],
	'nodes': Optional[List['TreeEntry']],
	'pageInfo': 'PageInfo',
})


TreeEntryEdge = TypedDict('TreeEntryEdge', {
	'cursor': str,
	'node': Optional['TreeEntry'],
})


UpdateAlertStatusPayload = TypedDict('UpdateAlertStatusPayload', {
	'alert': Optional['AlertManagementAlert'],
	'clientMutationId': Optional[str],
	'errors': List[str],
	'issue': Optional['Issue'],
	'todo': Optional['Todo'],
})


UpdateBoardEpicUserPreferencesPayload = TypedDict('UpdateBoardEpicUserPreferencesPayload', {
	'clientMutationId': Optional[str],
	'epicUserPreferences': Optional['BoardEpicUserPreferences'],
	'errors': List[str],
})


UpdateBoardListPayload = TypedDict('UpdateBoardListPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'list': Optional['BoardList'],
})


UpdateBoardPayload = TypedDict('UpdateBoardPayload', {
	'board': Optional['Board'],
	'clientMutationId': Optional[str],
	'errors': List[str],
})


UpdateComplianceFrameworkPayload = TypedDict('UpdateComplianceFrameworkPayload', {
	'clientMutationId': Optional[str],
	'complianceFramework': Optional['ComplianceFramework'],
	'errors': List[str],
})


UpdateContainerExpirationPolicyPayload = TypedDict('UpdateContainerExpirationPolicyPayload', {
	'clientMutationId': Optional[str],
	'containerExpirationPolicy': Optional['ContainerExpirationPolicy'],
	'errors': List[str],
})


UpdateDependencyProxyImageTtlGroupPolicyPayload = TypedDict('UpdateDependencyProxyImageTtlGroupPolicyPayload', {
	'clientMutationId': Optional[str],
	'dependencyProxyImageTtlPolicy': Optional['DependencyProxyImageTtlGroupPolicy'],
	'errors': List[str],
})


UpdateDependencyProxySettingsPayload = TypedDict('UpdateDependencyProxySettingsPayload', {
	'clientMutationId': Optional[str],
	'dependencyProxySetting': Optional['DependencyProxySetting'],
	'errors': List[str],
})


UpdateEpicBoardListPayload = TypedDict('UpdateEpicBoardListPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'list': Optional['EpicList'],
})


UpdateEpicPayload = TypedDict('UpdateEpicPayload', {
	'clientMutationId': Optional[str],
	'epic': Optional['Epic'],
	'errors': List[str],
})


UpdateImageDiffNotePayload = TypedDict('UpdateImageDiffNotePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'note': Optional['Note'],
})


UpdateIssuePayload = TypedDict('UpdateIssuePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'issue': Optional['Issue'],
})


UpdateIterationPayload = TypedDict('UpdateIterationPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'iteration': Optional['Iteration'],
})


UpdateNamespacePackageSettingsPayload = TypedDict('UpdateNamespacePackageSettingsPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'packageSettings': Optional['PackageSettings'],
})


UpdateNotePayload = TypedDict('UpdateNotePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'note': Optional['Note'],
})


UpdateRequirementPayload = TypedDict('UpdateRequirementPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'requirement': Optional['Requirement'],
})


UpdateSnippetPayload = TypedDict('UpdateSnippetPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'snippet': Optional['Snippet'],
})


UploadRegistry = TypedDict('UploadRegistry', {
	'createdAt': Optional['Time'],
	'fileId': str,
	'id': str,
	'lastSyncFailure': Optional[str],
	'lastSyncedAt': Optional['Time'],
	'retryAt': Optional['Time'],
	'retryCount': Optional[int],
	'state': Optional['RegistryState'],
})


UploadRegistryConnection = TypedDict('UploadRegistryConnection', {
	'edges': Optional[List['UploadRegistryEdge']],
	'nodes': Optional[List['UploadRegistry']],
	'pageInfo': 'PageInfo',
})


UploadRegistryEdge = TypedDict('UploadRegistryEdge', {
	'cursor': str,
	'node': Optional['UploadRegistry'],
})


UsageTrendsMeasurement = TypedDict('UsageTrendsMeasurement', {
	'count': int,
	'identifier': 'MeasurementIdentifier',
	'recordedAt': Optional['Time'],
})


UsageTrendsMeasurementConnection = TypedDict('UsageTrendsMeasurementConnection', {
	'edges': Optional[List['UsageTrendsMeasurementEdge']],
	'nodes': Optional[List['UsageTrendsMeasurement']],
	'pageInfo': 'PageInfo',
})


UsageTrendsMeasurementEdge = TypedDict('UsageTrendsMeasurementEdge', {
	'cursor': str,
	'node': Optional['UsageTrendsMeasurement'],
})


UserCallout = TypedDict('UserCallout', {
	'dismissedAt': Optional['Time'],
	'featureName': Optional['UserCalloutFeatureNameEnum'],
})


UserCalloutConnection = TypedDict('UserCalloutConnection', {
	'edges': Optional[List['UserCalloutEdge']],
	'nodes': Optional[List['UserCallout']],
	'pageInfo': 'PageInfo',
})


UserCalloutCreatePayload = TypedDict('UserCalloutCreatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'userCallout': 'UserCallout',
})


UserCalloutEdge = TypedDict('UserCalloutEdge', {
	'cursor': str,
	'node': Optional['UserCallout'],
})


UserCore = TypedDict('UserCore', {
	'assignedMergeRequests': Optional['MergeRequestConnection'],
	'authoredMergeRequests': Optional['MergeRequestConnection'],
	'avatarUrl': Optional[str],
	'bot': bool,
	'callouts': Optional['UserCalloutConnection'],
	'email': Optional[str],
	'gitpodEnabled': Optional[bool],
	'groupCount': Optional[int],
	'groupMemberships': Optional['GroupMemberConnection'],
	'groups': Optional['GroupConnection'],
	'id': str,
	'location': Optional[str],
	'name': str,
	'namespace': Optional['Namespace'],
	'preferencesGitpodPath': Optional[str],
	'profileEnableGitpodPath': Optional[str],
	'projectMemberships': Optional['ProjectMemberConnection'],
	'publicEmail': Optional[str],
	'reviewRequestedMergeRequests': Optional['MergeRequestConnection'],
	'savedReplies': Optional['SavedReplyConnection'],
	'snippets': Optional['SnippetConnection'],
	'starredProjects': Optional['ProjectConnection'],
	'state': 'UserState',
	'status': Optional['UserStatus'],
	'timelogs': Optional['TimelogConnection'],
	'todos': Optional['TodoConnection'],
	'userPermissions': 'UserPermissions',
	'username': str,
	'webPath': str,
	'webUrl': str,
})


UserCoreConnection = TypedDict('UserCoreConnection', {
	'edges': Optional[List['UserCoreEdge']],
	'nodes': Optional[List['UserCore']],
	'pageInfo': 'PageInfo',
})


UserCoreEdge = TypedDict('UserCoreEdge', {
	'cursor': str,
	'node': Optional['UserCore'],
})


UserMergeRequestInteraction = TypedDict('UserMergeRequestInteraction', {
	'applicableApprovalRules': Optional[List['ApprovalRule']],
	'approved': bool,
	'canMerge': bool,
	'canUpdate': bool,
	'reviewState': Optional['MergeRequestReviewState'],
	'reviewed': bool,
})


UserPermissions = TypedDict('UserPermissions', {
	'createSnippet': bool,
})


UserPreferences = TypedDict('UserPreferences', {
	'issuesSort': Optional['IssueSort'],
})


UserPreferencesUpdatePayload = TypedDict('UserPreferencesUpdatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'userPreferences': Optional['UserPreferences'],
})


UserStatus = TypedDict('UserStatus', {
	'availability': 'AvailabilityEnum',
	'emoji': Optional[str],
	'message': Optional[str],
	'messageHtml': Optional[str],
})


VulnerabilitiesCountByDay = TypedDict('VulnerabilitiesCountByDay', {
	'critical': int,
	'date': 'ISO8601Date',
	'high': int,
	'info': int,
	'low': int,
	'medium': int,
	'total': int,
	'unknown': int,
})


VulnerabilitiesCountByDayConnection = TypedDict('VulnerabilitiesCountByDayConnection', {
	'edges': Optional[List['VulnerabilitiesCountByDayEdge']],
	'nodes': Optional[List['VulnerabilitiesCountByDay']],
	'pageInfo': 'PageInfo',
})


VulnerabilitiesCountByDayEdge = TypedDict('VulnerabilitiesCountByDayEdge', {
	'cursor': str,
	'node': Optional['VulnerabilitiesCountByDay'],
})


Vulnerability = TypedDict('Vulnerability', {
	'confirmedAt': Optional['Time'],
	'confirmedBy': Optional['UserCore'],
	'description': Optional[str],
	'descriptionHtml': Optional[str],
	'details': List['VulnerabilityDetail'],
	'detectedAt': 'Time',
	'discussions': 'DiscussionConnection',
	'dismissedAt': Optional['Time'],
	'dismissedBy': Optional['UserCore'],
	'externalIssueLinks': 'VulnerabilityExternalIssueLinkConnection',
	'falsePositive': Optional[bool],
	'hasSolutions': Optional[bool],
	'id': str,
	'identifiers': List['VulnerabilityIdentifier'],
	'issueLinks': 'VulnerabilityIssueLinkConnection',
	'links': List['VulnerabilityLink'],
	'location': Optional['VulnerabilityLocation'],
	'mergeRequest': Optional['MergeRequest'],
	'message': Optional[str],
	'notes': 'NoteConnection',
	'primaryIdentifier': Optional['VulnerabilityIdentifier'],
	'project': Optional['Project'],
	'reportType': Optional['VulnerabilityReportType'],
	'resolvedAt': Optional['Time'],
	'resolvedBy': Optional['UserCore'],
	'resolvedOnDefaultBranch': bool,
	'scanner': Optional['VulnerabilityScanner'],
	'severity': Optional['VulnerabilitySeverity'],
	'state': Optional['VulnerabilityState'],
	'title': Optional[str],
	'userNotesCount': int,
	'userPermissions': 'VulnerabilityPermissions',
	'vulnerabilityPath': Optional[str],
})


VulnerabilityConfirmPayload = TypedDict('VulnerabilityConfirmPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'vulnerability': Optional['Vulnerability'],
})


VulnerabilityConnection = TypedDict('VulnerabilityConnection', {
	'edges': Optional[List['VulnerabilityEdge']],
	'nodes': Optional[List['Vulnerability']],
	'pageInfo': 'PageInfo',
})


VulnerabilityCreatePayload = TypedDict('VulnerabilityCreatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'vulnerability': Optional['Vulnerability'],
})


VulnerabilityDetailBase = TypedDict('VulnerabilityDetailBase', {
	'description': Optional[str],
	'fieldName': Optional[str],
	'name': Optional[str],
})


VulnerabilityDetailBoolean = TypedDict('VulnerabilityDetailBoolean', {
	'description': Optional[str],
	'fieldName': Optional[str],
	'name': Optional[str],
	'value': bool,
})


VulnerabilityDetailCode = TypedDict('VulnerabilityDetailCode', {
	'description': Optional[str],
	'fieldName': Optional[str],
	'lang': Optional[str],
	'name': Optional[str],
	'value': str,
})


VulnerabilityDetailCommit = TypedDict('VulnerabilityDetailCommit', {
	'description': Optional[str],
	'fieldName': Optional[str],
	'name': Optional[str],
	'value': str,
})


VulnerabilityDetailDiff = TypedDict('VulnerabilityDetailDiff', {
	'after': str,
	'before': str,
	'description': Optional[str],
	'fieldName': Optional[str],
	'name': Optional[str],
})


VulnerabilityDetailFileLocation = TypedDict('VulnerabilityDetailFileLocation', {
	'description': Optional[str],
	'fieldName': Optional[str],
	'fileName': str,
	'lineEnd': int,
	'lineStart': int,
	'name': Optional[str],
})


VulnerabilityDetailInt = TypedDict('VulnerabilityDetailInt', {
	'description': Optional[str],
	'fieldName': Optional[str],
	'name': Optional[str],
	'value': int,
})


VulnerabilityDetailList = TypedDict('VulnerabilityDetailList', {
	'description': Optional[str],
	'fieldName': Optional[str],
	'items': List['VulnerabilityDetail'],
	'name': Optional[str],
})


VulnerabilityDetailMarkdown = TypedDict('VulnerabilityDetailMarkdown', {
	'description': Optional[str],
	'fieldName': Optional[str],
	'name': Optional[str],
	'value': str,
})


VulnerabilityDetailModuleLocation = TypedDict('VulnerabilityDetailModuleLocation', {
	'description': Optional[str],
	'fieldName': Optional[str],
	'moduleName': str,
	'name': Optional[str],
	'offset': int,
})


VulnerabilityDetailTable = TypedDict('VulnerabilityDetailTable', {
	'description': Optional[str],
	'fieldName': Optional[str],
	'headers': List['VulnerabilityDetail'],
	'name': Optional[str],
	'rows': List['VulnerabilityDetail'],
})


VulnerabilityDetailText = TypedDict('VulnerabilityDetailText', {
	'description': Optional[str],
	'fieldName': Optional[str],
	'name': Optional[str],
	'value': str,
})


VulnerabilityDetailUrl = TypedDict('VulnerabilityDetailUrl', {
	'description': Optional[str],
	'fieldName': Optional[str],
	'href': str,
	'name': Optional[str],
	'text': Optional[str],
})


VulnerabilityDismissPayload = TypedDict('VulnerabilityDismissPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'vulnerability': Optional['Vulnerability'],
})


VulnerabilityEdge = TypedDict('VulnerabilityEdge', {
	'cursor': str,
	'node': Optional['Vulnerability'],
})


VulnerabilityEvidence = TypedDict('VulnerabilityEvidence', {
	'request': Optional['VulnerabilityRequest'],
	'response': Optional['VulnerabilityResponse'],
	'source': Optional['VulnerabilityEvidenceSource'],
	'summary': Optional[str],
	'supportingMessages': Optional[List['VulnerabilityEvidenceSupportingMessage']],
})


VulnerabilityEvidenceSource = TypedDict('VulnerabilityEvidenceSource', {
	'identifier': str,
	'name': str,
	'url': Optional[str],
})


VulnerabilityEvidenceSupportingMessage = TypedDict('VulnerabilityEvidenceSupportingMessage', {
	'name': str,
	'request': Optional['VulnerabilityRequest'],
	'response': Optional['VulnerabilityResponse'],
})


VulnerabilityExternalIssueLink = TypedDict('VulnerabilityExternalIssueLink', {
	'externalIssue': Optional['ExternalIssue'],
	'id': 'VulnerabilitiesExternalIssueLinkID',
	'linkType': 'VulnerabilityExternalIssueLinkType',
})


VulnerabilityExternalIssueLinkConnection = TypedDict('VulnerabilityExternalIssueLinkConnection', {
	'edges': Optional[List['VulnerabilityExternalIssueLinkEdge']],
	'nodes': Optional[List['VulnerabilityExternalIssueLink']],
	'pageInfo': 'PageInfo',
})


VulnerabilityExternalIssueLinkCreatePayload = TypedDict('VulnerabilityExternalIssueLinkCreatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'externalIssueLink': Optional['VulnerabilityExternalIssueLink'],
})


VulnerabilityExternalIssueLinkDestroyPayload = TypedDict('VulnerabilityExternalIssueLinkDestroyPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
})


VulnerabilityExternalIssueLinkEdge = TypedDict('VulnerabilityExternalIssueLinkEdge', {
	'cursor': str,
	'node': Optional['VulnerabilityExternalIssueLink'],
})


VulnerabilityFindingDismissPayload = TypedDict('VulnerabilityFindingDismissPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'finding': Optional['PipelineSecurityReportFinding'],
})


VulnerabilityIdentifier = TypedDict('VulnerabilityIdentifier', {
	'externalId': Optional[str],
	'externalType': Optional[str],
	'name': Optional[str],
	'url': Optional[str],
})


VulnerabilityIssueLink = TypedDict('VulnerabilityIssueLink', {
	'id': str,
	'issue': Optional['Issue'],
	'linkType': 'VulnerabilityIssueLinkType',
})


VulnerabilityIssueLinkConnection = TypedDict('VulnerabilityIssueLinkConnection', {
	'edges': Optional[List['VulnerabilityIssueLinkEdge']],
	'nodes': Optional[List['VulnerabilityIssueLink']],
	'pageInfo': 'PageInfo',
})


VulnerabilityIssueLinkEdge = TypedDict('VulnerabilityIssueLinkEdge', {
	'cursor': str,
	'node': Optional['VulnerabilityIssueLink'],
})


VulnerabilityLink = TypedDict('VulnerabilityLink', {
	'name': Optional[str],
	'url': str,
})


VulnerabilityLocationClusterImageScanning = TypedDict('VulnerabilityLocationClusterImageScanning', {
	'dependency': Optional['VulnerableDependency'],
	'image': Optional[str],
	'kubernetesResource': Optional['VulnerableKubernetesResource'],
	'operatingSystem': Optional[str],
})


VulnerabilityLocationContainerScanning = TypedDict('VulnerabilityLocationContainerScanning', {
	'dependency': Optional['VulnerableDependency'],
	'image': Optional[str],
	'operatingSystem': Optional[str],
})


VulnerabilityLocationCoverageFuzzing = TypedDict('VulnerabilityLocationCoverageFuzzing', {
	'blobPath': Optional[str],
	'crashAddress': Optional[str],
	'crashType': Optional[str],
	'endLine': Optional[str],
	'file': Optional[str],
	'stacktraceSnippet': Optional[str],
	'startLine': Optional[str],
	'vulnerableClass': Optional[str],
	'vulnerableMethod': Optional[str],
})


VulnerabilityLocationDast = TypedDict('VulnerabilityLocationDast', {
	'hostname': Optional[str],
	'param': Optional[str],
	'path': Optional[str],
	'requestMethod': Optional[str],
})


VulnerabilityLocationDependencyScanning = TypedDict('VulnerabilityLocationDependencyScanning', {
	'blobPath': Optional[str],
	'dependency': Optional['VulnerableDependency'],
	'file': Optional[str],
})


VulnerabilityLocationGeneric = TypedDict('VulnerabilityLocationGeneric', {
	'description': Optional[str],
})


VulnerabilityLocationSast = TypedDict('VulnerabilityLocationSast', {
	'blobPath': Optional[str],
	'endLine': Optional[str],
	'file': Optional[str],
	'startLine': Optional[str],
	'vulnerableClass': Optional[str],
	'vulnerableMethod': Optional[str],
})


VulnerabilityLocationSecretDetection = TypedDict('VulnerabilityLocationSecretDetection', {
	'blobPath': Optional[str],
	'endLine': Optional[str],
	'file': Optional[str],
	'startLine': Optional[str],
	'vulnerableClass': Optional[str],
	'vulnerableMethod': Optional[str],
})


VulnerabilityPermissions = TypedDict('VulnerabilityPermissions', {
	'adminVulnerability': bool,
	'adminVulnerabilityExternalIssueLink': bool,
	'adminVulnerabilityIssueLink': bool,
	'createVulnerability': bool,
	'createVulnerabilityExport': bool,
	'createVulnerabilityFeedback': bool,
	'destroyVulnerabilityFeedback': bool,
	'readVulnerabilityFeedback': bool,
	'updateVulnerabilityFeedback': bool,
})


VulnerabilityRequest = TypedDict('VulnerabilityRequest', {
	'body': Optional[str],
	'headers': List['VulnerabilityRequestResponseHeader'],
	'method': Optional[str],
	'url': Optional[str],
})


VulnerabilityRequestResponseHeader = TypedDict('VulnerabilityRequestResponseHeader', {
	'name': Optional[str],
	'value': Optional[str],
})


VulnerabilityResolvePayload = TypedDict('VulnerabilityResolvePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'vulnerability': Optional['Vulnerability'],
})


VulnerabilityResponse = TypedDict('VulnerabilityResponse', {
	'body': Optional[str],
	'headers': List['VulnerabilityRequestResponseHeader'],
	'reasonPhrase': Optional[str],
	'statusCode': Optional[int],
})


VulnerabilityRevertToDetectedPayload = TypedDict('VulnerabilityRevertToDetectedPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'vulnerability': Optional['Vulnerability'],
})


VulnerabilityScanner = TypedDict('VulnerabilityScanner', {
	'externalId': Optional[str],
	'id': Optional[str],
	'name': Optional[str],
	'reportType': Optional['VulnerabilityReportType'],
	'vendor': Optional[str],
})


VulnerabilityScannerConnection = TypedDict('VulnerabilityScannerConnection', {
	'edges': Optional[List['VulnerabilityScannerEdge']],
	'nodes': Optional[List['VulnerabilityScanner']],
	'pageInfo': 'PageInfo',
})


VulnerabilityScannerEdge = TypedDict('VulnerabilityScannerEdge', {
	'cursor': str,
	'node': Optional['VulnerabilityScanner'],
})


VulnerabilitySeveritiesCount = TypedDict('VulnerabilitySeveritiesCount', {
	'critical': Optional[int],
	'high': Optional[int],
	'info': Optional[int],
	'low': Optional[int],
	'medium': Optional[int],
	'unknown': Optional[int],
})


VulnerableDependency = TypedDict('VulnerableDependency', {
	'package': Optional['VulnerablePackage'],
	'version': Optional[str],
})


VulnerableKubernetesResource = TypedDict('VulnerableKubernetesResource', {
	'agent': Optional['ClusterAgent'],
	'clusterId': Optional['ClustersClusterID'],
	'containerName': str,
	'kind': str,
	'name': str,
	'namespace': str,
})


VulnerablePackage = TypedDict('VulnerablePackage', {
	'name': Optional[str],
})


VulnerableProjectsByGrade = TypedDict('VulnerableProjectsByGrade', {
	'count': int,
	'grade': 'VulnerabilityGrade',
	'projects': 'ProjectConnection',
})


WorkItem = TypedDict('WorkItem', {
	'description': Optional[str],
	'descriptionHtml': Optional[str],
	'id': 'WorkItemID',
	'iid': str,
	'lockVersion': int,
	'state': 'WorkItemState',
	'title': str,
	'titleHtml': Optional[str],
	'workItemType': 'WorkItemType',
})


WorkItemCreateFromTaskPayload = TypedDict('WorkItemCreateFromTaskPayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'newWorkItem': Optional['WorkItem'],
	'workItem': Optional['WorkItem'],
})


WorkItemCreatePayload = TypedDict('WorkItemCreatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'workItem': Optional['WorkItem'],
})


WorkItemDeletePayload = TypedDict('WorkItemDeletePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'project': Optional['Project'],
})


WorkItemType = TypedDict('WorkItemType', {
	'iconName': Optional[str],
	'id': 'WorkItemsTypeID',
	'name': str,
})


WorkItemTypeConnection = TypedDict('WorkItemTypeConnection', {
	'edges': Optional[List['WorkItemTypeEdge']],
	'nodes': Optional[List['WorkItemType']],
	'pageInfo': 'PageInfo',
})


WorkItemTypeEdge = TypedDict('WorkItemTypeEdge', {
	'cursor': str,
	'node': Optional['WorkItemType'],
})


WorkItemUpdatePayload = TypedDict('WorkItemUpdatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'workItem': Optional['WorkItem'],
})


IterationCreatePayload = TypedDict('IterationCreatePayload', {
	'clientMutationId': Optional[str],
	'errors': List[str],
	'iteration': Optional['Iteration'],
})


AddProjectToSecurityDashboardInput = TypedDict('AddProjectToSecurityDashboardInput', {
	'id': 'ProjectID',
	'clientMutationId': Optional[str],
})


AdminSidekiqQueuesDeleteJobsInput = TypedDict('AdminSidekiqQueuesDeleteJobsInput', {
	'user': Optional[str],
	'project': Optional[str],
	'rootNamespace': Optional[str],
	'clientId': Optional[str],
	'callerId': Optional[str],
	'remoteIp': Optional[str],
	'relatedClass': Optional[str],
	'featureCategory': Optional[str],
	'subscriptionPlan': Optional[str],
	'workerClass': Optional[str],
	'queueName': str,
	'clientMutationId': Optional[str],
})


AlertManagementPayloadAlertFieldInput = TypedDict('AlertManagementPayloadAlertFieldInput', {
	'fieldName': 'AlertManagementPayloadAlertFieldName',
	'path': List['PayloadAlertFieldPathSegment'],
	'label': Optional[str],
	'type': 'AlertManagementPayloadAlertFieldType',
})


AlertSetAssigneesInput = TypedDict('AlertSetAssigneesInput', {
	'projectPath': str,
	'iid': str,
	'assigneeUsernames': List[str],
	'operationMode': Optional['MutationOperationMode'],
	'clientMutationId': Optional[str],
})


AlertTodoCreateInput = TypedDict('AlertTodoCreateInput', {
	'projectPath': str,
	'iid': str,
	'clientMutationId': Optional[str],
})


ApiFuzzingCiConfigurationCreateInput = TypedDict('ApiFuzzingCiConfigurationCreateInput', {
	'projectPath': str,
	'apiSpecificationFile': str,
	'authPassword': Optional[str],
	'authUsername': Optional[str],
	'scanMode': 'ApiFuzzingScanMode',
	'scanProfile': Optional[str],
	'target': str,
	'clientMutationId': Optional[str],
})


AwardEmojiAddInput = TypedDict('AwardEmojiAddInput', {
	'awardableId': 'AwardableID',
	'name': str,
	'clientMutationId': Optional[str],
})


AwardEmojiRemoveInput = TypedDict('AwardEmojiRemoveInput', {
	'awardableId': 'AwardableID',
	'name': str,
	'clientMutationId': Optional[str],
})


AwardEmojiToggleInput = TypedDict('AwardEmojiToggleInput', {
	'awardableId': 'AwardableID',
	'name': str,
	'clientMutationId': Optional[str],
})


BoardEpicCreateInput = TypedDict('BoardEpicCreateInput', {
	'groupPath': str,
	'boardId': 'BoardsEpicBoardID',
	'listId': 'BoardsEpicListID',
	'title': str,
	'clientMutationId': Optional[str],
})


BoardIssueInput = TypedDict('BoardIssueInput', {
	'labelName': Optional[List[str]],
	'authorUsername': Optional[str],
	'myReactionEmoji': Optional[str],
	'iids': Optional[List[str]],
	'milestoneTitle': Optional[str],
	'assigneeUsername': Optional[List[str]],
	'releaseTag': Optional[str],
	'types': Optional[List['IssueType']],
	'milestoneWildcardId': Optional['MilestoneWildcardId'],
	'epicId': Optional['EpicID'],
	'iterationTitle': Optional[str],
	'weight': Optional[str],
	'iterationId': Optional[List['IterationID']],
	'not': Optional['NegatedBoardIssueInput'],
	'search': Optional[str],
	'assigneeWildcardId': Optional['AssigneeWildcardId'],
	'confidential': Optional[bool],
	'epicWildcardId': Optional['EpicWildcardId'],
	'iterationWildcardId': Optional['IterationWildcardId'],
	'iterationCadenceId': Optional[List['IterationsCadenceID']],
	'weightWildcardId': Optional['WeightWildcardId'],
})


BoardListCreateInput = TypedDict('BoardListCreateInput', {
	'backlog': Optional[bool],
	'labelId': Optional['LabelID'],
	'boardId': 'BoardID',
	'milestoneId': Optional['MilestoneID'],
	'iterationId': Optional['IterationID'],
	'assigneeId': Optional['UserID'],
	'clientMutationId': Optional[str],
})


BoardListUpdateLimitMetricsInput = TypedDict('BoardListUpdateLimitMetricsInput', {
	'listId': 'ListID',
	'limitMetric': Optional['ListLimitMetric'],
	'maxIssueCount': Optional[int],
	'maxIssueWeight': Optional[int],
	'clientMutationId': Optional[str],
})


BulkEnableDevopsAdoptionNamespacesInput = TypedDict('BulkEnableDevopsAdoptionNamespacesInput', {
	'namespaceIds': List['NamespaceID'],
	'displayNamespaceId': Optional['NamespaceID'],
	'clientMutationId': Optional[str],
})


CiCdSettingsUpdateInput = TypedDict('CiCdSettingsUpdateInput', {
	'fullPath': str,
	'keepLatestArtifact': Optional[bool],
	'jobTokenScopeEnabled': Optional[bool],
	'mergePipelinesEnabled': Optional[bool],
	'mergeTrainsEnabled': Optional[bool],
	'clientMutationId': Optional[str],
})


CiJobTokenScopeAddProjectInput = TypedDict('CiJobTokenScopeAddProjectInput', {
	'projectPath': str,
	'targetProjectPath': str,
	'clientMutationId': Optional[str],
})


CiJobTokenScopeRemoveProjectInput = TypedDict('CiJobTokenScopeRemoveProjectInput', {
	'projectPath': str,
	'targetProjectPath': str,
	'clientMutationId': Optional[str],
})


ClusterAgentDeleteInput = TypedDict('ClusterAgentDeleteInput', {
	'id': 'ClustersAgentID',
	'clientMutationId': Optional[str],
})


ClusterAgentTokenCreateInput = TypedDict('ClusterAgentTokenCreateInput', {
	'clusterAgentId': 'ClustersAgentID',
	'description': Optional[str],
	'name': str,
	'clientMutationId': Optional[str],
})


ClusterAgentTokenDeleteInput = TypedDict('ClusterAgentTokenDeleteInput', {
	'id': 'ClustersAgentTokenID',
	'clientMutationId': Optional[str],
})


ClusterAgentTokenRevokeInput = TypedDict('ClusterAgentTokenRevokeInput', {
	'id': 'ClustersAgentTokenID',
	'clientMutationId': Optional[str],
})


CommitAction = TypedDict('CommitAction', {
	'action': 'CommitActionMode',
	'content': Optional[str],
	'encoding': Optional['CommitEncoding'],
	'executeFilemode': Optional[bool],
	'filePath': str,
	'lastCommitId': Optional[str],
	'previousPath': Optional[str],
})


CommitCreateInput = TypedDict('CommitCreateInput', {
	'projectPath': str,
	'branch': str,
	'startBranch': Optional[str],
	'message': str,
	'actions': List['CommitAction'],
	'clientMutationId': Optional[str],
})


ComplianceFrameworkInput = TypedDict('ComplianceFrameworkInput', {
	'name': Optional[str],
	'description': Optional[str],
	'color': Optional[str],
	'pipelineConfigurationFullPath': Optional[str],
})


ComplianceViolationInput = TypedDict('ComplianceViolationInput', {
	'projectIds': Optional[List['ProjectID']],
	'mergedBefore': Optional['Date'],
	'mergedAfter': Optional['Date'],
})


ConfigureContainerScanningInput = TypedDict('ConfigureContainerScanningInput', {
	'projectPath': str,
	'clientMutationId': Optional[str],
})


ConfigureDependencyScanningInput = TypedDict('ConfigureDependencyScanningInput', {
	'projectPath': str,
	'clientMutationId': Optional[str],
})


ConfigureSastIacInput = TypedDict('ConfigureSastIacInput', {
	'projectPath': str,
	'clientMutationId': Optional[str],
})


ConfigureSastInput = TypedDict('ConfigureSastInput', {
	'projectPath': str,
	'configuration': 'SastCiConfigurationInput',
	'clientMutationId': Optional[str],
})


ConfigureSecretDetectionInput = TypedDict('ConfigureSecretDetectionInput', {
	'projectPath': str,
	'clientMutationId': Optional[str],
})


CorpusCreateInput = TypedDict('CorpusCreateInput', {
	'packageId': 'PackagesPackageID',
	'fullPath': str,
	'clientMutationId': Optional[str],
})


CreateAlertIssueInput = TypedDict('CreateAlertIssueInput', {
	'projectPath': str,
	'iid': str,
	'clientMutationId': Optional[str],
})


CreateAnnotationInput = TypedDict('CreateAnnotationInput', {
	'environmentId': Optional['EnvironmentID'],
	'clusterId': Optional['ClustersClusterID'],
	'startingAt': 'Time',
	'endingAt': Optional['Time'],
	'dashboardPath': str,
	'description': str,
	'clientMutationId': Optional[str],
})


CreateBoardInput = TypedDict('CreateBoardInput', {
	'projectPath': Optional[str],
	'groupPath': Optional[str],
	'name': Optional[str],
	'hideBacklogList': Optional[bool],
	'hideClosedList': Optional[bool],
	'assigneeId': Optional['UserID'],
	'milestoneId': Optional['MilestoneID'],
	'iterationId': Optional['IterationID'],
	'iterationCadenceId': Optional['IterationsCadenceID'],
	'weight': Optional[int],
	'labels': Optional[List[str]],
	'labelIds': Optional[List['LabelID']],
	'clientMutationId': Optional[str],
})


CreateBranchInput = TypedDict('CreateBranchInput', {
	'projectPath': str,
	'name': str,
	'ref': str,
	'clientMutationId': Optional[str],
})


CreateClusterAgentInput = TypedDict('CreateClusterAgentInput', {
	'projectPath': str,
	'name': str,
	'clientMutationId': Optional[str],
})


CreateComplianceFrameworkInput = TypedDict('CreateComplianceFrameworkInput', {
	'namespacePath': str,
	'params': 'ComplianceFrameworkInput',
	'clientMutationId': Optional[str],
})


CreateCustomEmojiInput = TypedDict('CreateCustomEmojiInput', {
	'groupPath': str,
	'name': str,
	'url': str,
	'clientMutationId': Optional[str],
})


CreateDiffNoteInput = TypedDict('CreateDiffNoteInput', {
	'noteableId': 'NoteableID',
	'body': str,
	'confidential': Optional[bool],
	'position': 'DiffPositionInput',
	'clientMutationId': Optional[str],
})


CreateEpicInput = TypedDict('CreateEpicInput', {
	'groupPath': str,
	'title': Optional[str],
	'description': Optional[str],
	'confidential': Optional[bool],
	'startDateFixed': Optional[str],
	'dueDateFixed': Optional[str],
	'startDateIsFixed': Optional[bool],
	'dueDateIsFixed': Optional[bool],
	'addLabelIds': Optional[List[str]],
	'removeLabelIds': Optional[List[str]],
	'color': Optional[str],
	'clientMutationId': Optional[str],
})


CreateImageDiffNoteInput = TypedDict('CreateImageDiffNoteInput', {
	'noteableId': 'NoteableID',
	'body': str,
	'confidential': Optional[bool],
	'position': 'DiffImagePositionInput',
	'clientMutationId': Optional[str],
})


CreateIssueInput = TypedDict('CreateIssueInput', {
	'description': Optional[str],
	'dueDate': Optional['ISO8601Date'],
	'confidential': Optional[bool],
	'locked': Optional[bool],
	'type': Optional['IssueType'],
	'projectPath': str,
	'iid': Optional[int],
	'title': str,
	'milestoneId': Optional['MilestoneID'],
	'labels': Optional[List[str]],
	'labelIds': Optional[List['LabelID']],
	'createdAt': Optional['Time'],
	'mergeRequestToResolveDiscussionsOf': Optional['MergeRequestID'],
	'discussionToResolve': Optional[str],
	'assigneeIds': Optional[List['UserID']],
	'moveBeforeId': Optional['IssueID'],
	'moveAfterId': Optional['IssueID'],
	'healthStatus': Optional['HealthStatus'],
	'weight': Optional[int],
	'epicId': Optional['EpicID'],
	'iterationId': Optional['IterationID'],
	'iterationWildcardId': Optional['IssueCreationIterationWildcardId'],
	'iterationCadenceId': Optional['IterationsCadenceID'],
	'clientMutationId': Optional[str],
})


CreateIterationInput = TypedDict('CreateIterationInput', {
	'projectPath': Optional[str],
	'groupPath': Optional[str],
	'iterationsCadenceId': Optional['IterationsCadenceID'],
	'title': Optional[str],
	'description': Optional[str],
	'startDate': Optional[str],
	'dueDate': Optional[str],
	'clientMutationId': Optional[str],
})


CreateNoteInput = TypedDict('CreateNoteInput', {
	'noteableId': 'NoteableID',
	'body': str,
	'confidential': Optional[bool],
	'discussionId': Optional['DiscussionID'],
	'mergeRequestDiffHeadSha': Optional[str],
	'clientMutationId': Optional[str],
})


CreateRequirementInput = TypedDict('CreateRequirementInput', {
	'title': Optional[str],
	'description': Optional[str],
	'projectPath': str,
	'clientMutationId': Optional[str],
})


CreateSnippetInput = TypedDict('CreateSnippetInput', {
	'title': str,
	'description': Optional[str],
	'visibilityLevel': 'VisibilityLevelsEnum',
	'projectPath': Optional[str],
	'uploadedFiles': Optional[List[str]],
	'blobActions': Optional[List['SnippetBlobActionInputType']],
	'clientMutationId': Optional[str],
})


CreateTestCaseInput = TypedDict('CreateTestCaseInput', {
	'title': str,
	'description': Optional[str],
	'labelIds': Optional[List[str]],
	'projectPath': str,
	'clientMutationId': Optional[str],
})


CustomerRelationsContactCreateInput = TypedDict('CustomerRelationsContactCreateInput', {
	'groupId': 'GroupID',
	'organizationId': Optional['CustomerRelationsOrganizationID'],
	'firstName': str,
	'lastName': str,
	'phone': Optional[str],
	'email': Optional[str],
	'description': Optional[str],
	'clientMutationId': Optional[str],
})


CustomerRelationsContactUpdateInput = TypedDict('CustomerRelationsContactUpdateInput', {
	'id': 'CustomerRelationsContactID',
	'organizationId': Optional['CustomerRelationsOrganizationID'],
	'firstName': Optional[str],
	'lastName': Optional[str],
	'phone': Optional[str],
	'email': Optional[str],
	'description': Optional[str],
	'clientMutationId': Optional[str],
})


CustomerRelationsOrganizationCreateInput = TypedDict('CustomerRelationsOrganizationCreateInput', {
	'groupId': 'GroupID',
	'name': str,
	'defaultRate': Optional[float],
	'description': Optional[str],
	'clientMutationId': Optional[str],
})


CustomerRelationsOrganizationUpdateInput = TypedDict('CustomerRelationsOrganizationUpdateInput', {
	'id': 'CustomerRelationsOrganizationID',
	'name': Optional[str],
	'defaultRate': Optional[float],
	'description': Optional[str],
	'clientMutationId': Optional[str],
})


DastOnDemandScanCreateInput = TypedDict('DastOnDemandScanCreateInput', {
	'fullPath': str,
	'dastSiteProfileId': 'DastSiteProfileID',
	'dastScannerProfileId': Optional['DastScannerProfileID'],
	'clientMutationId': Optional[str],
})


DastProfileCadenceInput = TypedDict('DastProfileCadenceInput', {
	'unit': Optional['DastProfileCadenceUnit'],
	'duration': Optional[int],
})


DastProfileCreateInput = TypedDict('DastProfileCreateInput', {
	'fullPath': str,
	'dastProfileSchedule': Optional['DastProfileScheduleInput'],
	'name': str,
	'description': Optional[str],
	'branchName': Optional[str],
	'dastSiteProfileId': 'DastSiteProfileID',
	'dastScannerProfileId': 'DastScannerProfileID',
	'runAfterCreate': Optional[bool],
	'clientMutationId': Optional[str],
})


DastProfileDeleteInput = TypedDict('DastProfileDeleteInput', {
	'id': 'DastProfileID',
	'clientMutationId': Optional[str],
})


DastProfileRunInput = TypedDict('DastProfileRunInput', {
	'id': 'DastProfileID',
	'clientMutationId': Optional[str],
})


DastProfileScheduleInput = TypedDict('DastProfileScheduleInput', {
	'active': Optional[bool],
	'startsAt': Optional['Time'],
	'timezone': Optional[str],
	'cadence': Optional['DastProfileCadenceInput'],
})


DastProfileUpdateInput = TypedDict('DastProfileUpdateInput', {
	'id': 'DastProfileID',
	'dastProfileSchedule': Optional['DastProfileScheduleInput'],
	'name': Optional[str],
	'description': Optional[str],
	'branchName': Optional[str],
	'dastSiteProfileId': Optional['DastSiteProfileID'],
	'dastScannerProfileId': Optional['DastScannerProfileID'],
	'runAfterUpdate': Optional[bool],
	'clientMutationId': Optional[str],
})


DastScannerProfileCreateInput = TypedDict('DastScannerProfileCreateInput', {
	'fullPath': str,
	'profileName': str,
	'spiderTimeout': Optional[int],
	'targetTimeout': Optional[int],
	'scanType': Optional['DastScanTypeEnum'],
	'useAjaxSpider': Optional[bool],
	'showDebugMessages': Optional[bool],
	'clientMutationId': Optional[str],
})


DastScannerProfileDeleteInput = TypedDict('DastScannerProfileDeleteInput', {
	'id': 'DastScannerProfileID',
	'clientMutationId': Optional[str],
})


DastScannerProfileUpdateInput = TypedDict('DastScannerProfileUpdateInput', {
	'id': 'DastScannerProfileID',
	'profileName': str,
	'spiderTimeout': int,
	'targetTimeout': int,
	'scanType': Optional['DastScanTypeEnum'],
	'useAjaxSpider': Optional[bool],
	'showDebugMessages': Optional[bool],
	'clientMutationId': Optional[str],
})


DastSiteProfileAuthInput = TypedDict('DastSiteProfileAuthInput', {
	'enabled': Optional[bool],
	'url': Optional[str],
	'usernameField': Optional[str],
	'passwordField': Optional[str],
	'username': Optional[str],
	'password': Optional[str],
})


DastSiteProfileCreateInput = TypedDict('DastSiteProfileCreateInput', {
	'profileName': str,
	'targetUrl': Optional[str],
	'targetType': Optional['DastTargetTypeEnum'],
	'scanMethod': Optional['DastScanMethodType'],
	'requestHeaders': Optional[str],
	'auth': Optional['DastSiteProfileAuthInput'],
	'fullPath': str,
	'excludedUrls': Optional[List[str]],
	'clientMutationId': Optional[str],
})


DastSiteProfileDeleteInput = TypedDict('DastSiteProfileDeleteInput', {
	'id': 'DastSiteProfileID',
	'clientMutationId': Optional[str],
})


DastSiteProfileUpdateInput = TypedDict('DastSiteProfileUpdateInput', {
	'profileName': str,
	'targetUrl': Optional[str],
	'targetType': Optional['DastTargetTypeEnum'],
	'scanMethod': Optional['DastScanMethodType'],
	'requestHeaders': Optional[str],
	'auth': Optional['DastSiteProfileAuthInput'],
	'id': 'DastSiteProfileID',
	'excludedUrls': Optional[List[str]],
	'clientMutationId': Optional[str],
})


DastSiteTokenCreateInput = TypedDict('DastSiteTokenCreateInput', {
	'fullPath': str,
	'targetUrl': Optional[str],
	'clientMutationId': Optional[str],
})


DastSiteValidationCreateInput = TypedDict('DastSiteValidationCreateInput', {
	'fullPath': str,
	'dastSiteTokenId': 'DastSiteTokenID',
	'validationPath': str,
	'strategy': Optional['DastSiteValidationStrategyEnum'],
	'clientMutationId': Optional[str],
})


DastSiteValidationRevokeInput = TypedDict('DastSiteValidationRevokeInput', {
	'fullPath': str,
	'normalizedTargetUrl': str,
	'clientMutationId': Optional[str],
})


DeleteAnnotationInput = TypedDict('DeleteAnnotationInput', {
	'id': 'MetricsDashboardAnnotationID',
	'clientMutationId': Optional[str],
})


DesignManagementDeleteInput = TypedDict('DesignManagementDeleteInput', {
	'projectPath': str,
	'iid': str,
	'filenames': List[str],
	'clientMutationId': Optional[str],
})


DesignManagementMoveInput = TypedDict('DesignManagementMoveInput', {
	'id': 'DesignManagementDesignID',
	'previous': Optional['DesignManagementDesignID'],
	'next': Optional['DesignManagementDesignID'],
	'clientMutationId': Optional[str],
})


DesignManagementUploadInput = TypedDict('DesignManagementUploadInput', {
	'projectPath': str,
	'iid': str,
	'files': List['Upload'],
	'clientMutationId': Optional[str],
})


DestroyBoardInput = TypedDict('DestroyBoardInput', {
	'id': 'BoardID',
	'clientMutationId': Optional[str],
})


DestroyBoardListInput = TypedDict('DestroyBoardListInput', {
	'listId': 'ListID',
	'clientMutationId': Optional[str],
})


DestroyComplianceFrameworkInput = TypedDict('DestroyComplianceFrameworkInput', {
	'id': 'ComplianceManagementFrameworkID',
	'clientMutationId': Optional[str],
})


DestroyContainerRepositoryInput = TypedDict('DestroyContainerRepositoryInput', {
	'id': 'ContainerRepositoryID',
	'clientMutationId': Optional[str],
})


DestroyContainerRepositoryTagsInput = TypedDict('DestroyContainerRepositoryTagsInput', {
	'id': 'ContainerRepositoryID',
	'tagNames': List[str],
	'clientMutationId': Optional[str],
})


DestroyCustomEmojiInput = TypedDict('DestroyCustomEmojiInput', {
	'id': 'CustomEmojiID',
	'clientMutationId': Optional[str],
})


DestroyEpicBoardInput = TypedDict('DestroyEpicBoardInput', {
	'id': 'BoardsEpicBoardID',
	'clientMutationId': Optional[str],
})


DestroyNoteInput = TypedDict('DestroyNoteInput', {
	'id': 'NoteID',
	'clientMutationId': Optional[str],
})


DestroyPackageFileInput = TypedDict('DestroyPackageFileInput', {
	'id': 'PackagesPackageFileID',
	'clientMutationId': Optional[str],
})


DestroyPackageInput = TypedDict('DestroyPackageInput', {
	'id': 'PackagesPackageID',
	'clientMutationId': Optional[str],
})


DestroySnippetInput = TypedDict('DestroySnippetInput', {
	'id': 'SnippetID',
	'clientMutationId': Optional[str],
})


DiffImagePositionInput = TypedDict('DiffImagePositionInput', {
	'baseSha': Optional[str],
	'headSha': str,
	'startSha': str,
	'paths': 'DiffPathsInput',
	'height': int,
	'width': int,
	'x': int,
	'y': int,
})


DiffPathsInput = TypedDict('DiffPathsInput', {
	'newPath': Optional[str],
	'oldPath': Optional[str],
})


DiffPositionInput = TypedDict('DiffPositionInput', {
	'baseSha': Optional[str],
	'headSha': str,
	'startSha': str,
	'paths': 'DiffPathsInput',
	'newLine': Optional[int],
	'oldLine': Optional[int],
})


DisableDevopsAdoptionNamespaceInput = TypedDict('DisableDevopsAdoptionNamespaceInput', {
	'id': List['AnalyticsDevopsAdoptionEnabledNamespaceID'],
	'clientMutationId': Optional[str],
})


DiscussionToggleResolveInput = TypedDict('DiscussionToggleResolveInput', {
	'id': 'DiscussionID',
	'resolve': bool,
	'clientMutationId': Optional[str],
})


EchoCreateInput = TypedDict('EchoCreateInput', {
	'errors': Optional[List[str]],
	'messages': Optional[List[str]],
	'clientMutationId': Optional[str],
})


EnableDevopsAdoptionNamespaceInput = TypedDict('EnableDevopsAdoptionNamespaceInput', {
	'namespaceId': 'NamespaceID',
	'displayNamespaceId': Optional['NamespaceID'],
	'clientMutationId': Optional[str],
})


EnvironmentsCanaryIngressUpdateInput = TypedDict('EnvironmentsCanaryIngressUpdateInput', {
	'id': 'EnvironmentID',
	'weight': int,
	'clientMutationId': Optional[str],
})


EpicAddIssueInput = TypedDict('EpicAddIssueInput', {
	'iid': str,
	'groupPath': str,
	'projectPath': str,
	'issueIid': str,
	'clientMutationId': Optional[str],
})


EpicBoardCreateInput = TypedDict('EpicBoardCreateInput', {
	'name': Optional[str],
	'hideBacklogList': Optional[bool],
	'hideClosedList': Optional[bool],
	'labels': Optional[List[str]],
	'labelIds': Optional[List['LabelID']],
	'groupPath': Optional[str],
	'clientMutationId': Optional[str],
})


EpicBoardListCreateInput = TypedDict('EpicBoardListCreateInput', {
	'backlog': Optional[bool],
	'labelId': Optional['LabelID'],
	'boardId': 'BoardsEpicBoardID',
	'clientMutationId': Optional[str],
})


EpicBoardListDestroyInput = TypedDict('EpicBoardListDestroyInput', {
	'listId': 'BoardsEpicListID',
	'clientMutationId': Optional[str],
})


EpicBoardUpdateInput = TypedDict('EpicBoardUpdateInput', {
	'name': Optional[str],
	'hideBacklogList': Optional[bool],
	'hideClosedList': Optional[bool],
	'labels': Optional[List[str]],
	'labelIds': Optional[List['LabelID']],
	'id': 'BoardsEpicBoardID',
	'clientMutationId': Optional[str],
})


EpicFilters = TypedDict('EpicFilters', {
	'labelName': Optional[List[str]],
	'authorUsername': Optional[str],
	'myReactionEmoji': Optional[str],
	'not': Optional['NegatedEpicBoardIssueInput'],
	'search': Optional[str],
	'confidential': Optional[bool],
})


EpicMoveListInput = TypedDict('EpicMoveListInput', {
	'boardId': 'BoardsEpicBoardID',
	'epicId': 'EpicID',
	'fromListId': Optional['BoardsEpicListID'],
	'toListId': 'BoardsEpicListID',
	'moveBeforeId': Optional['EpicID'],
	'moveAfterId': Optional['EpicID'],
	'clientMutationId': Optional[str],
})


EpicSetSubscriptionInput = TypedDict('EpicSetSubscriptionInput', {
	'iid': str,
	'groupPath': str,
	'subscribedState': bool,
	'clientMutationId': Optional[str],
})


EpicTreeNodeFieldsInputType = TypedDict('EpicTreeNodeFieldsInputType', {
	'id': 'EpicTreeSortingID',
	'adjacentReferenceId': Optional['EpicTreeSortingID'],
	'relativePosition': Optional['MoveType'],
	'newParentId': Optional['EpicID'],
})


EpicTreeReorderInput = TypedDict('EpicTreeReorderInput', {
	'baseEpicId': 'EpicID',
	'moved': 'EpicTreeNodeFieldsInputType',
	'clientMutationId': Optional[str],
})


EscalationPolicyCreateInput = TypedDict('EscalationPolicyCreateInput', {
	'projectPath': str,
	'name': str,
	'description': Optional[str],
	'rules': List['EscalationRuleInput'],
	'clientMutationId': Optional[str],
})


EscalationPolicyDestroyInput = TypedDict('EscalationPolicyDestroyInput', {
	'id': 'IncidentManagementEscalationPolicyID',
	'clientMutationId': Optional[str],
})


EscalationPolicyUpdateInput = TypedDict('EscalationPolicyUpdateInput', {
	'id': 'IncidentManagementEscalationPolicyID',
	'name': Optional[str],
	'description': Optional[str],
	'rules': Optional[List['EscalationRuleInput']],
	'clientMutationId': Optional[str],
})


EscalationRuleInput = TypedDict('EscalationRuleInput', {
	'oncallScheduleIid': Optional[str],
	'username': Optional[str],
	'elapsedTimeSeconds': int,
	'status': 'EscalationRuleStatus',
})


ExportRequirementsInput = TypedDict('ExportRequirementsInput', {
	'sort': Optional['Sort'],
	'state': Optional['RequirementState'],
	'search': Optional[str],
	'authorUsername': Optional[List[str]],
	'projectPath': str,
	'selectedFields': Optional[List[str]],
	'clientMutationId': Optional[str],
})


ExternalAuditEventDestinationCreateInput = TypedDict('ExternalAuditEventDestinationCreateInput', {
	'destinationUrl': str,
	'groupPath': str,
	'clientMutationId': Optional[str],
})


ExternalAuditEventDestinationDestroyInput = TypedDict('ExternalAuditEventDestinationDestroyInput', {
	'id': 'AuditEventsExternalAuditEventDestinationID',
	'clientMutationId': Optional[str],
})


ExternalAuditEventDestinationUpdateInput = TypedDict('ExternalAuditEventDestinationUpdateInput', {
	'id': 'AuditEventsExternalAuditEventDestinationID',
	'destinationUrl': Optional[str],
	'clientMutationId': Optional[str],
})


GitlabSubscriptionActivateInput = TypedDict('GitlabSubscriptionActivateInput', {
	'activationCode': str,
	'clientMutationId': Optional[str],
})


GroupUpdateInput = TypedDict('GroupUpdateInput', {
	'fullPath': str,
	'sharedRunnersSetting': 'SharedRunnersSetting',
	'clientMutationId': Optional[str],
})


HttpIntegrationCreateInput = TypedDict('HttpIntegrationCreateInput', {
	'projectPath': str,
	'name': str,
	'active': bool,
	'payloadExample': Optional['JsonString'],
	'payloadAttributeMappings': Optional[List['AlertManagementPayloadAlertFieldInput']],
	'clientMutationId': Optional[str],
})


HttpIntegrationDestroyInput = TypedDict('HttpIntegrationDestroyInput', {
	'id': 'AlertManagementHttpIntegrationID',
	'clientMutationId': Optional[str],
})


HttpIntegrationResetTokenInput = TypedDict('HttpIntegrationResetTokenInput', {
	'id': 'AlertManagementHttpIntegrationID',
	'clientMutationId': Optional[str],
})


HttpIntegrationUpdateInput = TypedDict('HttpIntegrationUpdateInput', {
	'id': 'AlertManagementHttpIntegrationID',
	'name': Optional[str],
	'active': Optional[bool],
	'payloadExample': Optional['JsonString'],
	'payloadAttributeMappings': Optional[List['AlertManagementPayloadAlertFieldInput']],
	'clientMutationId': Optional[str],
})


IssueMoveInput = TypedDict('IssueMoveInput', {
	'projectPath': str,
	'iid': str,
	'targetProjectPath': str,
	'clientMutationId': Optional[str],
})


IssueMoveListInput = TypedDict('IssueMoveListInput', {
	'projectPath': str,
	'iid': str,
	'boardId': 'BoardID',
	'fromListId': Optional[str],
	'toListId': Optional[str],
	'moveBeforeId': Optional[str],
	'moveAfterId': Optional[str],
	'epicId': Optional['EpicID'],
	'clientMutationId': Optional[str],
})


IssueSetAssigneesInput = TypedDict('IssueSetAssigneesInput', {
	'projectPath': str,
	'iid': str,
	'assigneeUsernames': List[str],
	'operationMode': Optional['MutationOperationMode'],
	'clientMutationId': Optional[str],
})


IssueSetConfidentialInput = TypedDict('IssueSetConfidentialInput', {
	'projectPath': str,
	'iid': str,
	'confidential': bool,
	'clientMutationId': Optional[str],
})


IssueSetCrmContactsInput = TypedDict('IssueSetCrmContactsInput', {
	'projectPath': str,
	'iid': str,
	'contactIds': List['CustomerRelationsContactID'],
	'operationMode': Optional['MutationOperationMode'],
	'clientMutationId': Optional[str],
})


IssueSetDueDateInput = TypedDict('IssueSetDueDateInput', {
	'projectPath': str,
	'iid': str,
	'dueDate': Optional['Time'],
	'clientMutationId': Optional[str],
})


IssueSetEpicInput = TypedDict('IssueSetEpicInput', {
	'projectPath': str,
	'iid': str,
	'epicId': Optional['EpicID'],
	'clientMutationId': Optional[str],
})


IssueSetEscalationPolicyInput = TypedDict('IssueSetEscalationPolicyInput', {
	'projectPath': str,
	'iid': str,
	'escalationPolicyId': Optional['IncidentManagementEscalationPolicyID'],
	'clientMutationId': Optional[str],
})


IssueSetEscalationStatusInput = TypedDict('IssueSetEscalationStatusInput', {
	'projectPath': str,
	'iid': str,
	'status': 'IssueEscalationStatus',
	'clientMutationId': Optional[str],
})


IssueSetIterationInput = TypedDict('IssueSetIterationInput', {
	'projectPath': str,
	'iid': str,
	'iterationId': Optional['IterationID'],
	'clientMutationId': Optional[str],
})


IssueSetLockedInput = TypedDict('IssueSetLockedInput', {
	'projectPath': str,
	'iid': str,
	'locked': bool,
	'clientMutationId': Optional[str],
})


IssueSetSeverityInput = TypedDict('IssueSetSeverityInput', {
	'projectPath': str,
	'iid': str,
	'severity': 'IssuableSeverity',
	'clientMutationId': Optional[str],
})


IssueSetSubscriptionInput = TypedDict('IssueSetSubscriptionInput', {
	'subscribedState': bool,
	'projectPath': str,
	'iid': str,
	'clientMutationId': Optional[str],
})


IssueSetWeightInput = TypedDict('IssueSetWeightInput', {
	'projectPath': str,
	'iid': str,
	'weight': Optional[int],
	'clientMutationId': Optional[str],
})


IterationCadenceCreateInput = TypedDict('IterationCadenceCreateInput', {
	'groupPath': str,
	'title': Optional[str],
	'durationInWeeks': Optional[int],
	'iterationsInAdvance': Optional[int],
	'startDate': Optional['Time'],
	'automatic': bool,
	'active': bool,
	'rollOver': Optional[bool],
	'description': Optional[str],
	'clientMutationId': Optional[str],
})


IterationCadenceDestroyInput = TypedDict('IterationCadenceDestroyInput', {
	'id': 'IterationsCadenceID',
	'clientMutationId': Optional[str],
})


IterationCadenceUpdateInput = TypedDict('IterationCadenceUpdateInput', {
	'id': 'IterationsCadenceID',
	'title': Optional[str],
	'durationInWeeks': Optional[int],
	'iterationsInAdvance': Optional[int],
	'startDate': Optional['Time'],
	'automatic': Optional[bool],
	'active': Optional[bool],
	'rollOver': Optional[bool],
	'description': Optional[str],
	'clientMutationId': Optional[str],
})


IterationDeleteInput = TypedDict('IterationDeleteInput', {
	'id': 'IterationID',
	'clientMutationId': Optional[str],
})


JiraImportStartInput = TypedDict('JiraImportStartInput', {
	'jiraProjectKey': str,
	'jiraProjectName': Optional[str],
	'projectPath': str,
	'usersMapping': Optional[List['JiraUsersMappingInputType']],
	'clientMutationId': Optional[str],
})


JiraImportUsersInput = TypedDict('JiraImportUsersInput', {
	'projectPath': str,
	'startAt': Optional[int],
	'clientMutationId': Optional[str],
})


JiraUsersMappingInputType = TypedDict('JiraUsersMappingInputType', {
	'gitlabId': Optional[int],
	'jiraAccountId': str,
})


JobCancelInput = TypedDict('JobCancelInput', {
	'id': 'CiBuildID',
	'clientMutationId': Optional[str],
})


JobPlayInput = TypedDict('JobPlayInput', {
	'id': 'CiBuildID',
	'clientMutationId': Optional[str],
})


JobRetryInput = TypedDict('JobRetryInput', {
	'id': 'CiBuildID',
	'clientMutationId': Optional[str],
})


JobUnscheduleInput = TypedDict('JobUnscheduleInput', {
	'id': 'CiBuildID',
	'clientMutationId': Optional[str],
})


LabelCreateInput = TypedDict('LabelCreateInput', {
	'projectPath': Optional[str],
	'groupPath': Optional[str],
	'title': str,
	'description': Optional[str],
	'color': Optional[str],
	'clientMutationId': Optional[str],
})


MarkAsSpamSnippetInput = TypedDict('MarkAsSpamSnippetInput', {
	'id': 'SnippetID',
	'clientMutationId': Optional[str],
})


MergeRequestAcceptInput = TypedDict('MergeRequestAcceptInput', {
	'projectPath': str,
	'iid': str,
	'strategy': Optional['MergeStrategyEnum'],
	'commitMessage': Optional[str],
	'sha': str,
	'squashCommitMessage': Optional[str],
	'shouldRemoveSourceBranch': Optional[bool],
	'squash': Optional[bool],
	'clientMutationId': Optional[str],
})


MergeRequestCreateInput = TypedDict('MergeRequestCreateInput', {
	'projectPath': str,
	'title': str,
	'sourceBranch': str,
	'targetBranch': str,
	'description': Optional[str],
	'labels': Optional[List[str]],
	'clientMutationId': Optional[str],
})


MergeRequestReviewerRereviewInput = TypedDict('MergeRequestReviewerRereviewInput', {
	'projectPath': str,
	'iid': str,
	'userId': 'UserID',
	'clientMutationId': Optional[str],
})


MergeRequestSetAssigneesInput = TypedDict('MergeRequestSetAssigneesInput', {
	'projectPath': str,
	'iid': str,
	'assigneeUsernames': List[str],
	'operationMode': Optional['MutationOperationMode'],
	'clientMutationId': Optional[str],
})


MergeRequestSetDraftInput = TypedDict('MergeRequestSetDraftInput', {
	'projectPath': str,
	'iid': str,
	'draft': bool,
	'clientMutationId': Optional[str],
})


MergeRequestSetLabelsInput = TypedDict('MergeRequestSetLabelsInput', {
	'projectPath': str,
	'iid': str,
	'labelIds': List['LabelID'],
	'operationMode': Optional['MutationOperationMode'],
	'clientMutationId': Optional[str],
})


MergeRequestSetLockedInput = TypedDict('MergeRequestSetLockedInput', {
	'projectPath': str,
	'iid': str,
	'locked': bool,
	'clientMutationId': Optional[str],
})


MergeRequestSetMilestoneInput = TypedDict('MergeRequestSetMilestoneInput', {
	'projectPath': str,
	'iid': str,
	'milestoneId': Optional['MilestoneID'],
	'clientMutationId': Optional[str],
})


MergeRequestSetSubscriptionInput = TypedDict('MergeRequestSetSubscriptionInput', {
	'subscribedState': bool,
	'projectPath': str,
	'iid': str,
	'clientMutationId': Optional[str],
})


MergeRequestUpdateInput = TypedDict('MergeRequestUpdateInput', {
	'projectPath': str,
	'iid': str,
	'title': Optional[str],
	'targetBranch': Optional[str],
	'description': Optional[str],
	'state': Optional['MergeRequestNewState'],
	'clientMutationId': Optional[str],
})


MergeRequestsResolverNegatedParams = TypedDict('MergeRequestsResolverNegatedParams', {
	'labels': Optional[List[str]],
	'milestoneTitle': Optional[str],
})


NamespaceIncreaseStorageTemporarilyInput = TypedDict('NamespaceIncreaseStorageTemporarilyInput', {
	'id': 'NamespaceID',
	'clientMutationId': Optional[str],
})


NegatedBoardIssueInput = TypedDict('NegatedBoardIssueInput', {
	'labelName': Optional[List[str]],
	'authorUsername': Optional[str],
	'myReactionEmoji': Optional[str],
	'iids': Optional[List[str]],
	'milestoneTitle': Optional[str],
	'assigneeUsername': Optional[List[str]],
	'releaseTag': Optional[str],
	'types': Optional[List['IssueType']],
	'milestoneWildcardId': Optional['MilestoneWildcardId'],
	'epicId': Optional['EpicID'],
	'iterationTitle': Optional[str],
	'weight': Optional[str],
	'iterationId': Optional[List['IterationID']],
	'iterationWildcardId': Optional['NegatedIterationWildcardId'],
})


NegatedEpicBoardIssueInput = TypedDict('NegatedEpicBoardIssueInput', {
	'labelName': Optional[List[str]],
	'authorUsername': Optional[str],
	'myReactionEmoji': Optional[str],
})


NegatedEpicFilterInput = TypedDict('NegatedEpicFilterInput', {
	'labelName': Optional[List[str]],
	'authorUsername': Optional[str],
	'myReactionEmoji': Optional[str],
})


NegatedIssueFilterInput = TypedDict('NegatedIssueFilterInput', {
	'assigneeId': Optional[str],
	'assigneeUsernames': Optional[List[str]],
	'authorUsername': Optional[str],
	'iids': Optional[List[str]],
	'labelName': Optional[List[str]],
	'milestoneTitle': Optional[List[str]],
	'milestoneWildcardId': Optional['NegatedMilestoneWildcardId'],
	'myReactionEmoji': Optional[str],
	'releaseTag': Optional[List[str]],
	'types': Optional[List['IssueType']],
	'epicId': Optional[str],
	'weight': Optional[str],
	'iterationId': Optional[List[str]],
	'iterationWildcardId': Optional['IterationWildcardId'],
})


OncallRotationActivePeriodInputType = TypedDict('OncallRotationActivePeriodInputType', {
	'startTime': str,
	'endTime': str,
})


OncallRotationCreateInput = TypedDict('OncallRotationCreateInput', {
	'projectPath': str,
	'scheduleIid': str,
	'name': str,
	'startsAt': 'OncallRotationDateInputType',
	'endsAt': Optional['OncallRotationDateInputType'],
	'rotationLength': 'OncallRotationLengthInputType',
	'activePeriod': Optional['OncallRotationActivePeriodInputType'],
	'participants': List['OncallUserInputType'],
	'clientMutationId': Optional[str],
})


OncallRotationDateInputType = TypedDict('OncallRotationDateInputType', {
	'date': str,
	'time': str,
})


OncallRotationDestroyInput = TypedDict('OncallRotationDestroyInput', {
	'projectPath': str,
	'scheduleIid': str,
	'id': 'IncidentManagementOncallRotationID',
	'clientMutationId': Optional[str],
})


OncallRotationLengthInputType = TypedDict('OncallRotationLengthInputType', {
	'length': int,
	'unit': 'OncallRotationUnitEnum',
})


OncallRotationUpdateInput = TypedDict('OncallRotationUpdateInput', {
	'id': 'IncidentManagementOncallRotationID',
	'name': Optional[str],
	'startsAt': Optional['OncallRotationDateInputType'],
	'endsAt': Optional['OncallRotationDateInputType'],
	'rotationLength': Optional['OncallRotationLengthInputType'],
	'activePeriod': Optional['OncallRotationActivePeriodInputType'],
	'participants': Optional[List['OncallUserInputType']],
	'clientMutationId': Optional[str],
})


OncallScheduleCreateInput = TypedDict('OncallScheduleCreateInput', {
	'projectPath': str,
	'name': str,
	'description': Optional[str],
	'timezone': str,
	'clientMutationId': Optional[str],
})


OncallScheduleDestroyInput = TypedDict('OncallScheduleDestroyInput', {
	'projectPath': str,
	'iid': str,
	'clientMutationId': Optional[str],
})


OncallScheduleUpdateInput = TypedDict('OncallScheduleUpdateInput', {
	'projectPath': str,
	'iid': str,
	'name': Optional[str],
	'description': Optional[str],
	'timezone': Optional[str],
	'clientMutationId': Optional[str],
})


OncallUserInputType = TypedDict('OncallUserInputType', {
	'username': str,
	'colorPalette': Optional['DataVisualizationColorEnum'],
	'colorWeight': Optional['DataVisualizationWeightEnum'],
})


PipelineCancelInput = TypedDict('PipelineCancelInput', {
	'id': 'CiPipelineID',
	'clientMutationId': Optional[str],
})


PipelineDestroyInput = TypedDict('PipelineDestroyInput', {
	'id': 'CiPipelineID',
	'clientMutationId': Optional[str],
})


PipelineRetryInput = TypedDict('PipelineRetryInput', {
	'id': 'CiPipelineID',
	'clientMutationId': Optional[str],
})


ProjectSetComplianceFrameworkInput = TypedDict('ProjectSetComplianceFrameworkInput', {
	'projectId': 'ProjectID',
	'complianceFrameworkId': Optional['ComplianceManagementFrameworkID'],
	'clientMutationId': Optional[str],
})


ProjectSetLockedInput = TypedDict('ProjectSetLockedInput', {
	'projectPath': str,
	'filePath': str,
	'lock': bool,
	'clientMutationId': Optional[str],
})


PrometheusIntegrationCreateInput = TypedDict('PrometheusIntegrationCreateInput', {
	'projectPath': str,
	'active': bool,
	'apiUrl': str,
	'clientMutationId': Optional[str],
})


PrometheusIntegrationResetTokenInput = TypedDict('PrometheusIntegrationResetTokenInput', {
	'id': 'IntegrationsPrometheusID',
	'clientMutationId': Optional[str],
})


PrometheusIntegrationUpdateInput = TypedDict('PrometheusIntegrationUpdateInput', {
	'id': 'IntegrationsPrometheusID',
	'active': Optional[bool],
	'apiUrl': Optional[str],
	'clientMutationId': Optional[str],
})


PromoteToEpicInput = TypedDict('PromoteToEpicInput', {
	'projectPath': str,
	'iid': str,
	'groupPath': Optional[str],
	'clientMutationId': Optional[str],
})


ReleaseAssetLinkCreateInput = TypedDict('ReleaseAssetLinkCreateInput', {
	'name': str,
	'url': str,
	'directAssetPath': Optional[str],
	'linkType': Optional['ReleaseAssetLinkType'],
	'projectPath': str,
	'tagName': str,
	'clientMutationId': Optional[str],
})


ReleaseAssetLinkDeleteInput = TypedDict('ReleaseAssetLinkDeleteInput', {
	'id': 'ReleasesLinkID',
	'clientMutationId': Optional[str],
})


ReleaseAssetLinkInput = TypedDict('ReleaseAssetLinkInput', {
	'name': str,
	'url': str,
	'directAssetPath': Optional[str],
	'linkType': Optional['ReleaseAssetLinkType'],
})


ReleaseAssetLinkUpdateInput = TypedDict('ReleaseAssetLinkUpdateInput', {
	'id': 'ReleasesLinkID',
	'name': Optional[str],
	'url': Optional[str],
	'directAssetPath': Optional[str],
	'linkType': Optional['ReleaseAssetLinkType'],
	'clientMutationId': Optional[str],
})


ReleaseAssetsInput = TypedDict('ReleaseAssetsInput', {
	'links': Optional[List['ReleaseAssetLinkInput']],
})


ReleaseCreateInput = TypedDict('ReleaseCreateInput', {
	'projectPath': str,
	'tagName': str,
	'ref': Optional[str],
	'name': Optional[str],
	'description': Optional[str],
	'releasedAt': Optional['Time'],
	'milestones': Optional[List[str]],
	'assets': Optional['ReleaseAssetsInput'],
	'clientMutationId': Optional[str],
})


ReleaseDeleteInput = TypedDict('ReleaseDeleteInput', {
	'projectPath': str,
	'tagName': str,
	'clientMutationId': Optional[str],
})


ReleaseUpdateInput = TypedDict('ReleaseUpdateInput', {
	'projectPath': str,
	'tagName': str,
	'name': Optional[str],
	'description': Optional[str],
	'releasedAt': Optional['Time'],
	'milestones': Optional[List[str]],
	'clientMutationId': Optional[str],
})


RemoveProjectFromSecurityDashboardInput = TypedDict('RemoveProjectFromSecurityDashboardInput', {
	'id': 'ProjectID',
	'clientMutationId': Optional[str],
})


RepositionImageDiffNoteInput = TypedDict('RepositionImageDiffNoteInput', {
	'id': 'DiffNoteID',
	'position': 'UpdateDiffImagePositionInput',
	'clientMutationId': Optional[str],
})


RunnerDeleteInput = TypedDict('RunnerDeleteInput', {
	'id': 'CiRunnerID',
	'clientMutationId': Optional[str],
})


RunnerUpdateInput = TypedDict('RunnerUpdateInput', {
	'id': 'CiRunnerID',
	'description': Optional[str],
	'maximumTimeout': Optional[int],
	'accessLevel': Optional['CiRunnerAccessLevel'],
	'paused': Optional[bool],
	'locked': Optional[bool],
	'runUntagged': Optional[bool],
	'tagList': Optional[List[str]],
	'publicProjectsMinutesCostFactor': Optional[float],
	'privateProjectsMinutesCostFactor': Optional[float],
	'clientMutationId': Optional[str],
})


RunnersRegistrationTokenResetInput = TypedDict('RunnersRegistrationTokenResetInput', {
	'type': 'CiRunnerType',
	'id': Optional[str],
	'clientMutationId': Optional[str],
})


SastCiConfigurationAnalyzersEntityInput = TypedDict('SastCiConfigurationAnalyzersEntityInput', {
	'name': str,
	'enabled': bool,
	'variables': Optional[List['SastCiConfigurationEntityInput']],
})


SastCiConfigurationEntityInput = TypedDict('SastCiConfigurationEntityInput', {
	'field': str,
	'defaultValue': str,
	'value': str,
})


SastCiConfigurationInput = TypedDict('SastCiConfigurationInput', {
	'global': Optional[List['SastCiConfigurationEntityInput']],
	'pipeline': Optional[List['SastCiConfigurationEntityInput']],
	'analyzers': Optional[List['SastCiConfigurationAnalyzersEntityInput']],
})


SavedReplyCreateInput = TypedDict('SavedReplyCreateInput', {
	'name': str,
	'content': str,
	'clientMutationId': Optional[str],
})


SavedReplyDestroyInput = TypedDict('SavedReplyDestroyInput', {
	'id': 'UsersSavedReplyID',
	'clientMutationId': Optional[str],
})


SavedReplyUpdateInput = TypedDict('SavedReplyUpdateInput', {
	'id': 'UsersSavedReplyID',
	'name': str,
	'content': str,
	'clientMutationId': Optional[str],
})


ScanExecutionPolicyCommitInput = TypedDict('ScanExecutionPolicyCommitInput', {
	'fullPath': Optional[str],
	'policyYaml': str,
	'operationMode': 'MutationOperationMode',
	'name': Optional[str],
	'clientMutationId': Optional[str],
})


SecurityPolicyProjectAssignInput = TypedDict('SecurityPolicyProjectAssignInput', {
	'fullPath': Optional[str],
	'securityPolicyProjectId': 'ProjectID',
	'clientMutationId': Optional[str],
})


SecurityPolicyProjectCreateInput = TypedDict('SecurityPolicyProjectCreateInput', {
	'fullPath': Optional[str],
	'clientMutationId': Optional[str],
})


SecurityPolicyProjectUnassignInput = TypedDict('SecurityPolicyProjectUnassignInput', {
	'projectPath': str,
	'clientMutationId': Optional[str],
})


SecurityTrainingUpdateInput = TypedDict('SecurityTrainingUpdateInput', {
	'projectPath': str,
	'providerId': 'SecurityTrainingProviderID',
	'isEnabled': bool,
	'isPrimary': Optional[bool],
	'clientMutationId': Optional[str],
})


SnippetBlobActionInputType = TypedDict('SnippetBlobActionInputType', {
	'action': 'SnippetBlobActionEnum',
	'previousPath': Optional[str],
	'filePath': str,
	'content': Optional[str],
})


TerraformStateDeleteInput = TypedDict('TerraformStateDeleteInput', {
	'id': 'TerraformStateID',
	'clientMutationId': Optional[str],
})


TerraformStateLockInput = TypedDict('TerraformStateLockInput', {
	'id': 'TerraformStateID',
	'clientMutationId': Optional[str],
})


TerraformStateUnlockInput = TypedDict('TerraformStateUnlockInput', {
	'id': 'TerraformStateID',
	'clientMutationId': Optional[str],
})


Timeframe = TypedDict('Timeframe', {
	'start': 'Date',
	'end': 'Date',
})


TimelineEventCreateInput = TypedDict('TimelineEventCreateInput', {
	'incidentId': 'IssueID',
	'note': str,
	'occurredAt': 'Time',
	'clientMutationId': Optional[str],
})


TimelineEventDestroyInput = TypedDict('TimelineEventDestroyInput', {
	'id': 'IncidentManagementTimelineEventID',
	'clientMutationId': Optional[str],
})


TimelineEventPromoteFromNoteInput = TypedDict('TimelineEventPromoteFromNoteInput', {
	'noteId': 'NoteID',
	'clientMutationId': Optional[str],
})


TimelineEventUpdateInput = TypedDict('TimelineEventUpdateInput', {
	'id': 'IncidentManagementTimelineEventID',
	'note': Optional[str],
	'occurredAt': Optional['Time'],
	'clientMutationId': Optional[str],
})


TodoCreateInput = TypedDict('TodoCreateInput', {
	'targetId': 'TodoableID',
	'clientMutationId': Optional[str],
})


TodoMarkDoneInput = TypedDict('TodoMarkDoneInput', {
	'id': 'TodoID',
	'clientMutationId': Optional[str],
})


TodoRestoreInput = TypedDict('TodoRestoreInput', {
	'id': 'TodoID',
	'clientMutationId': Optional[str],
})


TodoRestoreManyInput = TypedDict('TodoRestoreManyInput', {
	'ids': List['TodoID'],
	'clientMutationId': Optional[str],
})


TodosMarkAllDoneInput = TypedDict('TodosMarkAllDoneInput', {
	'targetId': Optional['TodoableID'],
	'clientMutationId': Optional[str],
})


UpdateAlertStatusInput = TypedDict('UpdateAlertStatusInput', {
	'projectPath': str,
	'iid': str,
	'status': 'AlertManagementStatus',
	'clientMutationId': Optional[str],
})


UpdateBoardEpicUserPreferencesInput = TypedDict('UpdateBoardEpicUserPreferencesInput', {
	'boardId': 'BoardID',
	'epicId': 'EpicID',
	'collapsed': bool,
	'clientMutationId': Optional[str],
})


UpdateBoardInput = TypedDict('UpdateBoardInput', {
	'name': Optional[str],
	'hideBacklogList': Optional[bool],
	'hideClosedList': Optional[bool],
	'id': 'BoardID',
	'assigneeId': Optional['UserID'],
	'milestoneId': Optional['MilestoneID'],
	'iterationId': Optional['IterationID'],
	'iterationCadenceId': Optional['IterationsCadenceID'],
	'weight': Optional[int],
	'labels': Optional[List[str]],
	'labelIds': Optional[List['LabelID']],
	'clientMutationId': Optional[str],
})


UpdateBoardListInput = TypedDict('UpdateBoardListInput', {
	'position': Optional[int],
	'collapsed': Optional[bool],
	'listId': 'ListID',
	'clientMutationId': Optional[str],
})


UpdateComplianceFrameworkInput = TypedDict('UpdateComplianceFrameworkInput', {
	'id': 'ComplianceManagementFrameworkID',
	'params': 'ComplianceFrameworkInput',
	'clientMutationId': Optional[str],
})


UpdateContainerExpirationPolicyInput = TypedDict('UpdateContainerExpirationPolicyInput', {
	'projectPath': str,
	'enabled': Optional[bool],
	'cadence': Optional['ContainerExpirationPolicyCadenceEnum'],
	'olderThan': Optional['ContainerExpirationPolicyOlderThanEnum'],
	'keepN': Optional['ContainerExpirationPolicyKeepEnum'],
	'nameRegex': Optional['UntrustedRegexp'],
	'nameRegexKeep': Optional['UntrustedRegexp'],
	'clientMutationId': Optional[str],
})


UpdateDependencyProxyImageTtlGroupPolicyInput = TypedDict('UpdateDependencyProxyImageTtlGroupPolicyInput', {
	'groupPath': str,
	'enabled': Optional[bool],
	'ttl': Optional[int],
	'clientMutationId': Optional[str],
})


UpdateDependencyProxySettingsInput = TypedDict('UpdateDependencyProxySettingsInput', {
	'groupPath': str,
	'enabled': Optional[bool],
	'clientMutationId': Optional[str],
})


UpdateDiffImagePositionInput = TypedDict('UpdateDiffImagePositionInput', {
	'x': Optional[int],
	'y': Optional[int],
	'width': Optional[int],
	'height': Optional[int],
})


UpdateEpicBoardListInput = TypedDict('UpdateEpicBoardListInput', {
	'position': Optional[int],
	'collapsed': Optional[bool],
	'listId': 'BoardsEpicListID',
	'clientMutationId': Optional[str],
})


UpdateEpicInput = TypedDict('UpdateEpicInput', {
	'iid': str,
	'groupPath': str,
	'title': Optional[str],
	'description': Optional[str],
	'confidential': Optional[bool],
	'startDateFixed': Optional[str],
	'dueDateFixed': Optional[str],
	'startDateIsFixed': Optional[bool],
	'dueDateIsFixed': Optional[bool],
	'addLabelIds': Optional[List[str]],
	'removeLabelIds': Optional[List[str]],
	'color': Optional[str],
	'stateEvent': Optional['EpicStateEvent'],
	'clientMutationId': Optional[str],
})


UpdateImageDiffNoteInput = TypedDict('UpdateImageDiffNoteInput', {
	'id': 'NoteID',
	'body': Optional[str],
	'position': Optional['UpdateDiffImagePositionInput'],
	'clientMutationId': Optional[str],
})


UpdateIssueInput = TypedDict('UpdateIssueInput', {
	'projectPath': str,
	'iid': str,
	'description': Optional[str],
	'dueDate': Optional['ISO8601Date'],
	'confidential': Optional[bool],
	'locked': Optional[bool],
	'type': Optional['IssueType'],
	'title': Optional[str],
	'milestoneId': Optional[str],
	'addLabelIds': Optional[List[str]],
	'removeLabelIds': Optional[List[str]],
	'labelIds': Optional[List[str]],
	'stateEvent': Optional['IssueStateEvent'],
	'healthStatus': Optional['HealthStatus'],
	'weight': Optional[int],
	'epicId': Optional['EpicID'],
	'clientMutationId': Optional[str],
})


UpdateIterationInput = TypedDict('UpdateIterationInput', {
	'groupPath': str,
	'id': str,
	'title': Optional[str],
	'description': Optional[str],
	'startDate': Optional[str],
	'dueDate': Optional[str],
	'clientMutationId': Optional[str],
})


UpdateNamespacePackageSettingsInput = TypedDict('UpdateNamespacePackageSettingsInput', {
	'namespacePath': str,
	'mavenDuplicatesAllowed': Optional[bool],
	'mavenDuplicateExceptionRegex': Optional['UntrustedRegexp'],
	'genericDuplicatesAllowed': Optional[bool],
	'genericDuplicateExceptionRegex': Optional['UntrustedRegexp'],
	'clientMutationId': Optional[str],
})


UpdateNoteInput = TypedDict('UpdateNoteInput', {
	'id': 'NoteID',
	'body': Optional[str],
	'confidential': Optional[bool],
	'clientMutationId': Optional[str],
})


UpdateRequirementInput = TypedDict('UpdateRequirementInput', {
	'title': Optional[str],
	'description': Optional[str],
	'projectPath': str,
	'state': Optional['RequirementState'],
	'iid': str,
	'lastTestReportState': Optional['TestReportState'],
	'clientMutationId': Optional[str],
})


UpdateSnippetInput = TypedDict('UpdateSnippetInput', {
	'id': 'SnippetID',
	'title': Optional[str],
	'description': Optional[str],
	'visibilityLevel': Optional['VisibilityLevelsEnum'],
	'blobActions': Optional[List['SnippetBlobActionInputType']],
	'clientMutationId': Optional[str],
})


UserCalloutCreateInput = TypedDict('UserCalloutCreateInput', {
	'featureName': str,
	'clientMutationId': Optional[str],
})


UserPreferencesUpdateInput = TypedDict('UserPreferencesUpdateInput', {
	'issuesSort': Optional['IssueSort'],
	'clientMutationId': Optional[str],
})


VulnerabilityConfirmInput = TypedDict('VulnerabilityConfirmInput', {
	'id': 'VulnerabilityID',
	'clientMutationId': Optional[str],
})


VulnerabilityCreateInput = TypedDict('VulnerabilityCreateInput', {
	'project': 'ProjectID',
	'name': str,
	'description': str,
	'scanner': 'VulnerabilityScannerInput',
	'identifiers': List['VulnerabilityIdentifierInput'],
	'state': Optional['VulnerabilityState'],
	'severity': Optional['VulnerabilitySeverity'],
	'confidence': Optional['VulnerabilityConfidence'],
	'solution': Optional[str],
	'message': Optional[str],
	'detectedAt': Optional['Time'],
	'confirmedAt': Optional['Time'],
	'resolvedAt': Optional['Time'],
	'dismissedAt': Optional['Time'],
	'clientMutationId': Optional[str],
})


VulnerabilityDismissInput = TypedDict('VulnerabilityDismissInput', {
	'id': 'VulnerabilityID',
	'comment': Optional[str],
	'dismissalReason': Optional['VulnerabilityDismissalReason'],
	'clientMutationId': Optional[str],
})


VulnerabilityExternalIssueLinkCreateInput = TypedDict('VulnerabilityExternalIssueLinkCreateInput', {
	'id': 'VulnerabilityID',
	'linkType': 'VulnerabilityExternalIssueLinkType',
	'externalTracker': 'VulnerabilityExternalIssueLinkExternalTracker',
	'clientMutationId': Optional[str],
})


VulnerabilityExternalIssueLinkDestroyInput = TypedDict('VulnerabilityExternalIssueLinkDestroyInput', {
	'id': 'VulnerabilitiesExternalIssueLinkID',
	'clientMutationId': Optional[str],
})


VulnerabilityFindingDismissInput = TypedDict('VulnerabilityFindingDismissInput', {
	'id': 'VulnerabilitiesFindingID',
	'comment': Optional[str],
	'dismissalReason': Optional['VulnerabilityDismissalReason'],
	'clientMutationId': Optional[str],
})


VulnerabilityIdentifierInput = TypedDict('VulnerabilityIdentifierInput', {
	'name': str,
	'url': str,
	'externalType': Optional[str],
	'externalId': Optional[str],
})


VulnerabilityResolveInput = TypedDict('VulnerabilityResolveInput', {
	'id': 'VulnerabilityID',
	'clientMutationId': Optional[str],
})


VulnerabilityRevertToDetectedInput = TypedDict('VulnerabilityRevertToDetectedInput', {
	'id': 'VulnerabilityID',
	'clientMutationId': Optional[str],
})


VulnerabilityScannerInput = TypedDict('VulnerabilityScannerInput', {
	'id': str,
	'name': str,
	'url': str,
	'vendor': Optional['VulnerabilityScannerVendorInput'],
	'version': str,
})


VulnerabilityScannerVendorInput = TypedDict('VulnerabilityScannerVendorInput', {
	'name': str,
})


WorkItemConvertTaskInput = TypedDict('WorkItemConvertTaskInput', {
	'lineNumberEnd': int,
	'lineNumberStart': int,
	'lockVersion': int,
	'title': str,
	'workItemTypeId': 'WorkItemsTypeID',
})


WorkItemCreateFromTaskInput = TypedDict('WorkItemCreateFromTaskInput', {
	'id': 'WorkItemID',
	'workItemData': 'WorkItemConvertTaskInput',
	'clientMutationId': Optional[str],
})


WorkItemCreateInput = TypedDict('WorkItemCreateInput', {
	'description': Optional[str],
	'projectPath': str,
	'title': str,
	'workItemTypeId': 'WorkItemsTypeID',
	'clientMutationId': Optional[str],
})


WorkItemDeleteInput = TypedDict('WorkItemDeleteInput', {
	'id': 'WorkItemID',
	'clientMutationId': Optional[str],
})


WorkItemUpdateInput = TypedDict('WorkItemUpdateInput', {
	'id': 'WorkItemID',
	'stateEvent': Optional['WorkItemStateEvent'],
	'title': Optional[str],
	'clientMutationId': Optional[str],
})


IterationCreateInput = TypedDict('IterationCreateInput', {
	'projectPath': Optional[str],
	'groupPath': Optional[str],
	'iterationsCadenceId': Optional['IterationsCadenceID'],
	'title': Optional[str],
	'description': Optional[str],
	'startDate': Optional[str],
	'dueDate': Optional[str],
	'clientMutationId': Optional[str],
})


