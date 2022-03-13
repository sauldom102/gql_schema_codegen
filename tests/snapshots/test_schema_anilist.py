from enum import Enum
from typing import Any, ClassVar, List, Optional, TypedDict, Union


## Scalars

CountryCode = Any

FuzzyDateInt = Any

Json = Any

## Union Types

ActivityUnion = Union['TextActivity', 'ListActivity', 'MessageActivity']

LikeableUnion = Union['ListActivity', 'TextActivity', 'MessageActivity', 'ActivityReply', 'Thread', 'ThreadComment']

NotificationUnion = Union['AiringNotification', 'FollowingNotification', 'ActivityMessageNotification', 'ActivityMentionNotification', 'ActivityReplyNotification', 'ActivityReplySubscribedNotification', 'ActivityLikeNotification', 'ActivityReplyLikeNotification', 'ThreadCommentMentionNotification', 'ThreadCommentReplyNotification', 'ThreadCommentSubscribedNotification', 'ThreadCommentLikeNotification', 'ThreadLikeNotification', 'RelatedMediaAdditionNotification', 'MediaDataChangeNotification', 'MediaMergeNotification', 'MediaDeletionNotification']

ActivitySort = Enum('ActivitySort', 'ID ID_DESC PINNED')


ActivityType = Enum('ActivityType', 'TEXT ANIME_LIST MANGA_LIST MESSAGE MEDIA_LIST')


AiringSort = Enum('AiringSort', 'ID ID_DESC MEDIA_ID MEDIA_ID_DESC TIME TIME_DESC EPISODE EPISODE_DESC')


CharacterRole = Enum('CharacterRole', 'MAIN SUPPORTING BACKGROUND')


CharacterSort = Enum('CharacterSort', 'ID ID_DESC ROLE ROLE_DESC SEARCH_MATCH FAVOURITES FAVOURITES_DESC RELEVANCE')


ExternalLinkMediaType = Enum('ExternalLinkMediaType', 'ANIME MANGA STAFF')


ExternalLinkType = Enum('ExternalLinkType', 'INFO STREAMING SOCIAL')


LikeableType = Enum('LikeableType', 'THREAD THREAD_COMMENT ACTIVITY ACTIVITY_REPLY')


MediaFormat = Enum('MediaFormat', 'TV TV_SHORT MOVIE SPECIAL OVA ONA MUSIC MANGA NOVEL ONE_SHOT')


MediaListSort = Enum('MediaListSort', 'MEDIA_ID MEDIA_ID_DESC SCORE SCORE_DESC STATUS STATUS_DESC PROGRESS PROGRESS_DESC PROGRESS_VOLUMES PROGRESS_VOLUMES_DESC REPEAT REPEAT_DESC PRIORITY PRIORITY_DESC STARTED_ON STARTED_ON_DESC FINISHED_ON FINISHED_ON_DESC ADDED_TIME ADDED_TIME_DESC UPDATED_TIME UPDATED_TIME_DESC MEDIA_TITLE_ROMAJI MEDIA_TITLE_ROMAJI_DESC MEDIA_TITLE_ENGLISH MEDIA_TITLE_ENGLISH_DESC MEDIA_TITLE_NATIVE MEDIA_TITLE_NATIVE_DESC MEDIA_POPULARITY MEDIA_POPULARITY_DESC')


MediaListStatus = Enum('MediaListStatus', 'CURRENT PLANNING COMPLETED DROPPED PAUSED REPEATING')


MediaRankType = Enum('MediaRankType', 'RATED POPULAR')


MediaRelation = Enum('MediaRelation', 'ADAPTATION PREQUEL SEQUEL PARENT SIDE_STORY CHARACTER SUMMARY ALTERNATIVE SPIN_OFF OTHER SOURCE COMPILATION CONTAINS')


MediaSeason = Enum('MediaSeason', 'WINTER SPRING SUMMER FALL')


MediaSort = Enum('MediaSort', 'ID ID_DESC TITLE_ROMAJI TITLE_ROMAJI_DESC TITLE_ENGLISH TITLE_ENGLISH_DESC TITLE_NATIVE TITLE_NATIVE_DESC TYPE TYPE_DESC FORMAT FORMAT_DESC START_DATE START_DATE_DESC END_DATE END_DATE_DESC SCORE SCORE_DESC POPULARITY POPULARITY_DESC TRENDING TRENDING_DESC EPISODES EPISODES_DESC DURATION DURATION_DESC STATUS STATUS_DESC CHAPTERS CHAPTERS_DESC VOLUMES VOLUMES_DESC UPDATED_AT UPDATED_AT_DESC SEARCH_MATCH FAVOURITES FAVOURITES_DESC')


MediaSource = Enum('MediaSource', 'ORIGINAL MANGA LIGHT_NOVEL VISUAL_NOVEL VIDEO_GAME OTHER NOVEL DOUJINSHI ANIME WEB_NOVEL LIVE_ACTION GAME COMIC MULTIMEDIA_PROJECT PICTURE_BOOK')


MediaStatus = Enum('MediaStatus', 'FINISHED RELEASING NOT_YET_RELEASED CANCELLED HIATUS')


MediaTrendSort = Enum('MediaTrendSort', 'ID ID_DESC MEDIA_ID MEDIA_ID_DESC DATE DATE_DESC SCORE SCORE_DESC POPULARITY POPULARITY_DESC TRENDING TRENDING_DESC EPISODE EPISODE_DESC')


MediaType = Enum('MediaType', 'ANIME MANGA')


ModActionType = Enum('ModActionType', 'NOTE BAN DELETE EDIT EXPIRE REPORT RESET ANON')


ModRole = Enum('ModRole', 'ADMIN LEAD_DEVELOPER DEVELOPER LEAD_COMMUNITY COMMUNITY DISCORD_COMMUNITY LEAD_ANIME_DATA ANIME_DATA LEAD_MANGA_DATA MANGA_DATA LEAD_SOCIAL_MEDIA SOCIAL_MEDIA RETIRED')


NotificationType = Enum('NotificationType', 'ACTIVITY_MESSAGE ACTIVITY_REPLY FOLLOWING ACTIVITY_MENTION THREAD_COMMENT_MENTION THREAD_SUBSCRIBED THREAD_COMMENT_REPLY AIRING ACTIVITY_LIKE ACTIVITY_REPLY_LIKE THREAD_LIKE THREAD_COMMENT_LIKE ACTIVITY_REPLY_SUBSCRIBED RELATED_MEDIA_ADDITION MEDIA_DATA_CHANGE MEDIA_MERGE MEDIA_DELETION')


RecommendationRating = Enum('RecommendationRating', 'NO_RATING RATE_UP RATE_DOWN')


RecommendationSort = Enum('RecommendationSort', 'ID ID_DESC RATING RATING_DESC')


ReviewRating = Enum('ReviewRating', 'NO_VOTE UP_VOTE DOWN_VOTE')


ReviewSort = Enum('ReviewSort', 'ID ID_DESC SCORE SCORE_DESC RATING RATING_DESC CREATED_AT CREATED_AT_DESC UPDATED_AT UPDATED_AT_DESC')


RevisionHistoryAction = Enum('RevisionHistoryAction', 'CREATE EDIT')


ScoreFormat = Enum('ScoreFormat', 'POINT_100 POINT_10_DECIMAL POINT_10 POINT_5 POINT_3')


SiteTrendSort = Enum('SiteTrendSort', 'DATE DATE_DESC COUNT COUNT_DESC CHANGE CHANGE_DESC')


StaffLanguage = Enum('StaffLanguage', 'JAPANESE ENGLISH KOREAN ITALIAN SPANISH PORTUGUESE FRENCH GERMAN HEBREW HUNGARIAN')


StaffSort = Enum('StaffSort', 'ID ID_DESC ROLE ROLE_DESC LANGUAGE LANGUAGE_DESC SEARCH_MATCH FAVOURITES FAVOURITES_DESC RELEVANCE')


StudioSort = Enum('StudioSort', 'ID ID_DESC NAME NAME_DESC SEARCH_MATCH FAVOURITES FAVOURITES_DESC')


SubmissionSort = Enum('SubmissionSort', 'ID ID_DESC')


SubmissionStatus = Enum('SubmissionStatus', 'PENDING REJECTED PARTIALLY_ACCEPTED ACCEPTED')


ThreadCommentSort = Enum('ThreadCommentSort', 'ID ID_DESC')


ThreadSort = Enum('ThreadSort', 'ID ID_DESC TITLE TITLE_DESC CREATED_AT CREATED_AT_DESC UPDATED_AT UPDATED_AT_DESC REPLIED_AT REPLIED_AT_DESC REPLY_COUNT REPLY_COUNT_DESC VIEW_COUNT VIEW_COUNT_DESC IS_STICKY SEARCH_MATCH')


UserSort = Enum('UserSort', 'ID ID_DESC USERNAME USERNAME_DESC WATCHED_TIME WATCHED_TIME_DESC CHAPTERS_READ CHAPTERS_READ_DESC SEARCH_MATCH')


UserStaffNameLanguage = Enum('UserStaffNameLanguage', 'ROMAJI_WESTERN ROMAJI NATIVE')


UserStatisticsSort = Enum('UserStatisticsSort', 'ID ID_DESC COUNT COUNT_DESC PROGRESS PROGRESS_DESC MEAN_SCORE MEAN_SCORE_DESC')


UserTitleLanguage = Enum('UserTitleLanguage', 'ROMAJI ENGLISH NATIVE ROMAJI_STYLISED ENGLISH_STYLISED NATIVE_STYLISED')


ActivityLikeNotification = TypedDict('ActivityLikeNotification', {
	'id': int,
	'userId': int,
	'type': Optional['NotificationType'],
	'activityId': int,
	'context': Optional[str],
	'createdAt': Optional[int],
	'activity': Optional['ActivityUnion'],
	'user': Optional['User'],
})


ActivityMentionNotification = TypedDict('ActivityMentionNotification', {
	'id': int,
	'userId': int,
	'type': Optional['NotificationType'],
	'activityId': int,
	'context': Optional[str],
	'createdAt': Optional[int],
	'activity': Optional['ActivityUnion'],
	'user': Optional['User'],
})


ActivityMessageNotification = TypedDict('ActivityMessageNotification', {
	'id': int,
	'userId': int,
	'type': Optional['NotificationType'],
	'activityId': int,
	'context': Optional[str],
	'createdAt': Optional[int],
	'message': Optional['MessageActivity'],
	'user': Optional['User'],
})


ActivityReply = TypedDict('ActivityReply', {
	'id': int,
	'userId': Optional[int],
	'activityId': Optional[int],
	'text': Optional[str],
	'likeCount': int,
	'isLiked': Optional[bool],
	'createdAt': int,
	'user': Optional['User'],
	'likes': Optional[List['User']],
})


ActivityReplyLikeNotification = TypedDict('ActivityReplyLikeNotification', {
	'id': int,
	'userId': int,
	'type': Optional['NotificationType'],
	'activityId': int,
	'context': Optional[str],
	'createdAt': Optional[int],
	'activity': Optional['ActivityUnion'],
	'user': Optional['User'],
})


ActivityReplyNotification = TypedDict('ActivityReplyNotification', {
	'id': int,
	'userId': int,
	'type': Optional['NotificationType'],
	'activityId': int,
	'context': Optional[str],
	'createdAt': Optional[int],
	'activity': Optional['ActivityUnion'],
	'user': Optional['User'],
})


ActivityReplySubscribedNotification = TypedDict('ActivityReplySubscribedNotification', {
	'id': int,
	'userId': int,
	'type': Optional['NotificationType'],
	'activityId': int,
	'context': Optional[str],
	'createdAt': Optional[int],
	'activity': Optional['ActivityUnion'],
	'user': Optional['User'],
})


AiringNotification = TypedDict('AiringNotification', {
	'id': int,
	'type': Optional['NotificationType'],
	'animeId': int,
	'episode': int,
	'contexts': Optional[List[str]],
	'createdAt': Optional[int],
	'media': Optional['Media'],
})


AiringProgression = TypedDict('AiringProgression', {
	'episode': Optional[float],
	'score': Optional[float],
	'watching': Optional[int],
})


AiringSchedule = TypedDict('AiringSchedule', {
	'id': int,
	'airingAt': int,
	'timeUntilAiring': int,
	'episode': int,
	'mediaId': int,
	'media': Optional['Media'],
})


AiringScheduleConnection = TypedDict('AiringScheduleConnection', {
	'edges': Optional[List['AiringScheduleEdge']],
	'nodes': Optional[List['AiringSchedule']],
	'pageInfo': Optional['PageInfo'],
})


AiringScheduleEdge = TypedDict('AiringScheduleEdge', {
	'node': Optional['AiringSchedule'],
	'id': Optional[int],
})


AniChartUser = TypedDict('AniChartUser', {
	'user': Optional['User'],
	'settings': Optional['Json'],
	'highlights': Optional['Json'],
})


Character = TypedDict('Character', {
	'id': int,
	'name': Optional['CharacterName'],
	'image': Optional['CharacterImage'],
	'description': Optional[str],
	'gender': Optional[str],
	'dateOfBirth': Optional['FuzzyDate'],
	'age': Optional[str],
	'bloodType': Optional[str],
	'isFavourite': bool,
	'isFavouriteBlocked': bool,
	'siteUrl': Optional[str],
	'media': Optional['MediaConnection'],
	'updatedAt': Optional[int],
	'favourites': Optional[int],
	'modNotes': Optional[str],
})


CharacterConnection = TypedDict('CharacterConnection', {
	'edges': Optional[List['CharacterEdge']],
	'nodes': Optional[List['Character']],
	'pageInfo': Optional['PageInfo'],
})


CharacterEdge = TypedDict('CharacterEdge', {
	'node': Optional['Character'],
	'id': Optional[int],
	'role': Optional['CharacterRole'],
	'name': Optional[str],
	'voiceActors': Optional[List['Staff']],
	'voiceActorRoles': Optional[List['StaffRoleType']],
	'media': Optional[List['Media']],
	'favouriteOrder': Optional[int],
})


CharacterImage = TypedDict('CharacterImage', {
	'large': Optional[str],
	'medium': Optional[str],
})


CharacterName = TypedDict('CharacterName', {
	'first': Optional[str],
	'middle': Optional[str],
	'last': Optional[str],
	'full': Optional[str],
	'native': Optional[str],
	'alternative': Optional[List[str]],
	'alternativeSpoiler': Optional[List[str]],
	'userPreferred': Optional[str],
})


CharacterSubmission = TypedDict('CharacterSubmission', {
	'id': int,
	'character': Optional['Character'],
	'submission': Optional['Character'],
	'submitter': Optional['User'],
	'assignee': Optional['User'],
	'status': Optional['SubmissionStatus'],
	'notes': Optional[str],
	'source': Optional[str],
	'locked': Optional[bool],
	'createdAt': Optional[int],
})


CharacterSubmissionConnection = TypedDict('CharacterSubmissionConnection', {
	'edges': Optional[List['CharacterSubmissionEdge']],
	'nodes': Optional[List['CharacterSubmission']],
	'pageInfo': Optional['PageInfo'],
})


CharacterSubmissionEdge = TypedDict('CharacterSubmissionEdge', {
	'node': Optional['CharacterSubmission'],
	'role': Optional['CharacterRole'],
	'voiceActors': Optional[List['Staff']],
	'submittedVoiceActors': Optional[List['StaffSubmission']],
})


Deleted = TypedDict('Deleted', {
	'deleted': Optional[bool],
})


Favourites = TypedDict('Favourites', {
	'anime': Optional['MediaConnection'],
	'manga': Optional['MediaConnection'],
	'characters': Optional['CharacterConnection'],
	'staff': Optional['StaffConnection'],
	'studios': Optional['StudioConnection'],
})


FollowingNotification = TypedDict('FollowingNotification', {
	'id': int,
	'userId': int,
	'type': Optional['NotificationType'],
	'context': Optional[str],
	'createdAt': Optional[int],
	'user': Optional['User'],
})


FormatStats = TypedDict('FormatStats', {
	'format': Optional['MediaFormat'],
	'amount': Optional[int],
})


FuzzyDate = TypedDict('FuzzyDate', {
	'year': Optional[int],
	'month': Optional[int],
	'day': Optional[int],
})


GenreStats = TypedDict('GenreStats', {
	'genre': Optional[str],
	'amount': Optional[int],
	'meanScore': Optional[int],
	'timeWatched': Optional[int],
})


InternalPage = TypedDict('InternalPage', {
	'mediaSubmissions': Optional[List['MediaSubmission']],
	'characterSubmissions': Optional[List['CharacterSubmission']],
	'staffSubmissions': Optional[List['StaffSubmission']],
	'revisionHistory': Optional[List['RevisionHistory']],
	'reports': Optional[List['Report']],
	'modActions': Optional[List['ModAction']],
	'userBlockSearch': Optional[List['User']],
	'pageInfo': Optional['PageInfo'],
	'users': Optional[List['User']],
	'media': Optional[List['Media']],
	'characters': Optional[List['Character']],
	'staff': Optional[List['Staff']],
	'studios': Optional[List['Studio']],
	'mediaList': Optional[List['MediaList']],
	'airingSchedules': Optional[List['AiringSchedule']],
	'mediaTrends': Optional[List['MediaTrend']],
	'notifications': Optional[List['NotificationUnion']],
	'followers': Optional[List['User']],
	'following': Optional[List['User']],
	'activities': Optional[List['ActivityUnion']],
	'activityReplies': Optional[List['ActivityReply']],
	'threads': Optional[List['Thread']],
	'threadComments': Optional[List['ThreadComment']],
	'reviews': Optional[List['Review']],
	'recommendations': Optional[List['Recommendation']],
	'likes': Optional[List['User']],
})


ListActivity = TypedDict('ListActivity', {
	'id': int,
	'userId': Optional[int],
	'type': Optional['ActivityType'],
	'replyCount': int,
	'status': Optional[str],
	'progress': Optional[str],
	'isLocked': Optional[bool],
	'isSubscribed': Optional[bool],
	'likeCount': int,
	'isLiked': Optional[bool],
	'isPinned': Optional[bool],
	'siteUrl': Optional[str],
	'createdAt': int,
	'user': Optional['User'],
	'media': Optional['Media'],
	'replies': Optional[List['ActivityReply']],
	'likes': Optional[List['User']],
})


ListActivityOption = TypedDict('ListActivityOption', {
	'disabled': Optional[bool],
	'type': Optional['MediaListStatus'],
})


ListScoreStats = TypedDict('ListScoreStats', {
	'meanScore': Optional[int],
	'standardDeviation': Optional[int],
})


Media = TypedDict('Media', {
	'id': int,
	'idMal': Optional[int],
	'title': Optional['MediaTitle'],
	'type': Optional['MediaType'],
	'format': Optional['MediaFormat'],
	'status': Optional['MediaStatus'],
	'description': Optional[str],
	'startDate': Optional['FuzzyDate'],
	'endDate': Optional['FuzzyDate'],
	'season': Optional['MediaSeason'],
	'seasonYear': Optional[int],
	'seasonInt': Optional[int],
	'episodes': Optional[int],
	'duration': Optional[int],
	'chapters': Optional[int],
	'volumes': Optional[int],
	'countryOfOrigin': Optional['CountryCode'],
	'isLicensed': Optional[bool],
	'source': Optional['MediaSource'],
	'hashtag': Optional[str],
	'trailer': Optional['MediaTrailer'],
	'updatedAt': Optional[int],
	'coverImage': Optional['MediaCoverImage'],
	'bannerImage': Optional[str],
	'genres': Optional[List[str]],
	'synonyms': Optional[List[str]],
	'averageScore': Optional[int],
	'meanScore': Optional[int],
	'popularity': Optional[int],
	'isLocked': Optional[bool],
	'trending': Optional[int],
	'favourites': Optional[int],
	'tags': Optional[List['MediaTag']],
	'relations': Optional['MediaConnection'],
	'characters': Optional['CharacterConnection'],
	'staff': Optional['StaffConnection'],
	'studios': Optional['StudioConnection'],
	'isFavourite': bool,
	'isFavouriteBlocked': bool,
	'isAdult': Optional[bool],
	'nextAiringEpisode': Optional['AiringSchedule'],
	'airingSchedule': Optional['AiringScheduleConnection'],
	'trends': Optional['MediaTrendConnection'],
	'externalLinks': Optional[List['MediaExternalLink']],
	'streamingEpisodes': Optional[List['MediaStreamingEpisode']],
	'rankings': Optional[List['MediaRank']],
	'mediaListEntry': Optional['MediaList'],
	'reviews': Optional['ReviewConnection'],
	'recommendations': Optional['RecommendationConnection'],
	'stats': Optional['MediaStats'],
	'siteUrl': Optional[str],
	'autoCreateForumThread': Optional[bool],
	'isRecommendationBlocked': Optional[bool],
	'modNotes': Optional[str],
})


MediaCharacter = TypedDict('MediaCharacter', {
	'id': Optional[int],
	'role': Optional['CharacterRole'],
	'roleNotes': Optional[str],
	'dubGroup': Optional[str],
	'characterName': Optional[str],
	'character': Optional['Character'],
	'voiceActor': Optional['Staff'],
})


MediaConnection = TypedDict('MediaConnection', {
	'edges': Optional[List['MediaEdge']],
	'nodes': Optional[List['Media']],
	'pageInfo': Optional['PageInfo'],
})


MediaCoverImage = TypedDict('MediaCoverImage', {
	'extraLarge': Optional[str],
	'large': Optional[str],
	'medium': Optional[str],
	'color': Optional[str],
})


MediaDataChangeNotification = TypedDict('MediaDataChangeNotification', {
	'id': int,
	'type': Optional['NotificationType'],
	'mediaId': int,
	'context': Optional[str],
	'reason': Optional[str],
	'createdAt': Optional[int],
	'media': Optional['Media'],
})


MediaDeletionNotification = TypedDict('MediaDeletionNotification', {
	'id': int,
	'type': Optional['NotificationType'],
	'deletedMediaTitle': Optional[str],
	'context': Optional[str],
	'reason': Optional[str],
	'createdAt': Optional[int],
})


MediaEdge = TypedDict('MediaEdge', {
	'node': Optional['Media'],
	'id': Optional[int],
	'relationType': Optional['MediaRelation'],
	'isMainStudio': bool,
	'characters': Optional[List['Character']],
	'characterRole': Optional['CharacterRole'],
	'characterName': Optional[str],
	'roleNotes': Optional[str],
	'dubGroup': Optional[str],
	'staffRole': Optional[str],
	'voiceActors': Optional[List['Staff']],
	'voiceActorRoles': Optional[List['StaffRoleType']],
	'favouriteOrder': Optional[int],
})


MediaExternalLink = TypedDict('MediaExternalLink', {
	'id': int,
	'url': Optional[str],
	'site': str,
	'siteId': Optional[int],
	'type': Optional['ExternalLinkType'],
	'language': Optional[str],
	'color': Optional[str],
	'icon': Optional[str],
})


MediaList = TypedDict('MediaList', {
	'id': int,
	'userId': int,
	'mediaId': int,
	'status': Optional['MediaListStatus'],
	'score': Optional[float],
	'progress': Optional[int],
	'progressVolumes': Optional[int],
	'repeat': Optional[int],
	'priority': Optional[int],
	'private': Optional[bool],
	'notes': Optional[str],
	'hiddenFromStatusLists': Optional[bool],
	'customLists': Optional['Json'],
	'advancedScores': Optional['Json'],
	'startedAt': Optional['FuzzyDate'],
	'completedAt': Optional['FuzzyDate'],
	'updatedAt': Optional[int],
	'createdAt': Optional[int],
	'media': Optional['Media'],
	'user': Optional['User'],
})


MediaListCollection = TypedDict('MediaListCollection', {
	'lists': Optional[List['MediaListGroup']],
	'user': Optional['User'],
	'hasNextChunk': Optional[bool],
	'statusLists': Optional[List[List['MediaList']]],
	'customLists': Optional[List[List['MediaList']]],
})


MediaListGroup = TypedDict('MediaListGroup', {
	'entries': Optional[List['MediaList']],
	'name': Optional[str],
	'isCustomList': Optional[bool],
	'isSplitCompletedList': Optional[bool],
	'status': Optional['MediaListStatus'],
})


MediaListOptions = TypedDict('MediaListOptions', {
	'scoreFormat': Optional['ScoreFormat'],
	'rowOrder': Optional[str],
	'useLegacyLists': Optional[bool],
	'animeList': Optional['MediaListTypeOptions'],
	'mangaList': Optional['MediaListTypeOptions'],
	'sharedTheme': Optional['Json'],
	'sharedThemeEnabled': Optional[bool],
})


MediaListTypeOptions = TypedDict('MediaListTypeOptions', {
	'sectionOrder': Optional[List[str]],
	'splitCompletedSectionByFormat': Optional[bool],
	'theme': Optional['Json'],
	'customLists': Optional[List[str]],
	'advancedScoring': Optional[List[str]],
	'advancedScoringEnabled': Optional[bool],
})


MediaMergeNotification = TypedDict('MediaMergeNotification', {
	'id': int,
	'type': Optional['NotificationType'],
	'mediaId': int,
	'deletedMediaTitles': Optional[List[str]],
	'context': Optional[str],
	'reason': Optional[str],
	'createdAt': Optional[int],
	'media': Optional['Media'],
})


MediaRank = TypedDict('MediaRank', {
	'id': int,
	'rank': int,
	'type': 'MediaRankType',
	'format': 'MediaFormat',
	'year': Optional[int],
	'season': Optional['MediaSeason'],
	'allTime': Optional[bool],
	'context': str,
})


MediaStats = TypedDict('MediaStats', {
	'scoreDistribution': Optional[List['ScoreDistribution']],
	'statusDistribution': Optional[List['StatusDistribution']],
	'airingProgression': Optional[List['AiringProgression']],
})


MediaStreamingEpisode = TypedDict('MediaStreamingEpisode', {
	'title': Optional[str],
	'thumbnail': Optional[str],
	'url': Optional[str],
	'site': Optional[str],
})


MediaSubmission = TypedDict('MediaSubmission', {
	'id': int,
	'submitter': Optional['User'],
	'assignee': Optional['User'],
	'status': Optional['SubmissionStatus'],
	'submitterStats': Optional['Json'],
	'notes': Optional[str],
	'source': Optional[str],
	'changes': Optional[List[str]],
	'locked': Optional[bool],
	'media': Optional['Media'],
	'submission': Optional['Media'],
	'characters': Optional[List['MediaSubmissionComparison']],
	'staff': Optional[List['MediaSubmissionComparison']],
	'studios': Optional[List['MediaSubmissionComparison']],
	'relations': Optional[List['MediaEdge']],
	'externalLinks': Optional[List['MediaSubmissionComparison']],
	'createdAt': Optional[int],
})


MediaSubmissionComparison = TypedDict('MediaSubmissionComparison', {
	'submission': Optional['MediaSubmissionEdge'],
	'character': Optional['MediaCharacter'],
	'staff': Optional['StaffEdge'],
	'studio': Optional['StudioEdge'],
	'externalLink': Optional['MediaExternalLink'],
})


MediaSubmissionEdge = TypedDict('MediaSubmissionEdge', {
	'id': Optional[int],
	'characterRole': Optional['CharacterRole'],
	'staffRole': Optional[str],
	'roleNotes': Optional[str],
	'dubGroup': Optional[str],
	'characterName': Optional[str],
	'isMain': Optional[bool],
	'character': Optional['Character'],
	'characterSubmission': Optional['Character'],
	'voiceActor': Optional['Staff'],
	'voiceActorSubmission': Optional['Staff'],
	'staff': Optional['Staff'],
	'staffSubmission': Optional['Staff'],
	'studio': Optional['Studio'],
	'externalLink': Optional['MediaExternalLink'],
	'media': Optional['Media'],
})


MediaTag = TypedDict('MediaTag', {
	'id': int,
	'name': str,
	'description': Optional[str],
	'category': Optional[str],
	'rank': Optional[int],
	'isGeneralSpoiler': Optional[bool],
	'isMediaSpoiler': Optional[bool],
	'isAdult': Optional[bool],
	'userId': Optional[int],
})


MediaTitle = TypedDict('MediaTitle', {
	'romaji': Optional[str],
	'english': Optional[str],
	'native': Optional[str],
	'userPreferred': Optional[str],
})


MediaTrailer = TypedDict('MediaTrailer', {
	'id': Optional[str],
	'site': Optional[str],
	'thumbnail': Optional[str],
})


MediaTrend = TypedDict('MediaTrend', {
	'mediaId': int,
	'date': int,
	'trending': int,
	'averageScore': Optional[int],
	'popularity': Optional[int],
	'inProgress': Optional[int],
	'releasing': bool,
	'episode': Optional[int],
	'media': Optional['Media'],
})


MediaTrendConnection = TypedDict('MediaTrendConnection', {
	'edges': Optional[List['MediaTrendEdge']],
	'nodes': Optional[List['MediaTrend']],
	'pageInfo': Optional['PageInfo'],
})


MediaTrendEdge = TypedDict('MediaTrendEdge', {
	'node': Optional['MediaTrend'],
})


MessageActivity = TypedDict('MessageActivity', {
	'id': int,
	'recipientId': Optional[int],
	'messengerId': Optional[int],
	'type': Optional['ActivityType'],
	'replyCount': int,
	'message': Optional[str],
	'isLocked': Optional[bool],
	'isSubscribed': Optional[bool],
	'likeCount': int,
	'isLiked': Optional[bool],
	'isPrivate': Optional[bool],
	'siteUrl': Optional[str],
	'createdAt': int,
	'recipient': Optional['User'],
	'messenger': Optional['User'],
	'replies': Optional[List['ActivityReply']],
	'likes': Optional[List['User']],
})


ModAction = TypedDict('ModAction', {
	'id': int,
	'user': Optional['User'],
	'mod': Optional['User'],
	'type': Optional['ModActionType'],
	'objectId': Optional[int],
	'objectType': Optional[str],
	'data': Optional[str],
	'createdAt': int,
})


Mutation = TypedDict('Mutation', {
	'UpdateUser': 'UpdateUserMutationResult',
	'SaveMediaListEntry': 'SaveMediaListEntryMutationResult',
	'UpdateMediaListEntries': 'UpdateMediaListEntriesMutationResult',
	'DeleteMediaListEntry': 'DeleteMediaListEntryMutationResult',
	'DeleteCustomList': 'DeleteCustomListMutationResult',
	'SaveTextActivity': 'SaveTextActivityMutationResult',
	'SaveMessageActivity': 'SaveMessageActivityMutationResult',
	'SaveListActivity': 'SaveListActivityMutationResult',
	'DeleteActivity': 'DeleteActivityMutationResult',
	'ToggleActivityPin': 'ToggleActivityPinMutationResult',
	'ToggleActivitySubscription': 'ToggleActivitySubscriptionMutationResult',
	'SaveActivityReply': 'SaveActivityReplyMutationResult',
	'DeleteActivityReply': 'DeleteActivityReplyMutationResult',
	'ToggleLike': 'ToggleLikeMutationResult',
	'ToggleLikeV2': 'ToggleLikeV2MutationResult',
	'ToggleFollow': 'ToggleFollowMutationResult',
	'ToggleFavourite': 'ToggleFavouriteMutationResult',
	'UpdateFavouriteOrder': 'UpdateFavouriteOrderMutationResult',
	'SaveReview': 'SaveReviewMutationResult',
	'DeleteReview': 'DeleteReviewMutationResult',
	'RateReview': 'RateReviewMutationResult',
	'SaveRecommendation': 'SaveRecommendationMutationResult',
	'SaveThread': 'SaveThreadMutationResult',
	'DeleteThread': 'DeleteThreadMutationResult',
	'ToggleThreadSubscription': 'ToggleThreadSubscriptionMutationResult',
	'SaveThreadComment': 'SaveThreadCommentMutationResult',
	'DeleteThreadComment': 'DeleteThreadCommentMutationResult',
	'UpdateAniChartSettings': 'UpdateAniChartSettingsMutationResult',
	'UpdateAniChartHighlights': 'UpdateAniChartHighlightsMutationResult',
})


UpdateUserParams = TypedDict('UpdateUserParams', {
	'about': Optional[str],
	'titleLanguage': Optional['UserTitleLanguage'],
	'displayAdultContent': Optional[bool],
	'airingNotifications': Optional[bool],
	'scoreFormat': Optional['ScoreFormat'],
	'rowOrder': Optional[str],
	'profileColor': Optional[str],
	'donatorBadge': Optional[str],
	'notificationOptions': Optional[List['NotificationOptionInput']],
	'timezone': Optional[str],
	'activityMergeTime': Optional[int],
	'animeListOptions': Optional['MediaListOptionsInput'],
	'mangaListOptions': Optional['MediaListOptionsInput'],
	'staffNameLanguage': Optional['UserStaffNameLanguage'],
	'restrictMessagesToFollowing': Optional[bool],
	'disabledListActivity': Optional[List['ListActivityOptionInput']],
})


UpdateUserMutationResult = ClassVar[Optional['User']]


SaveMediaListEntryParams = TypedDict('SaveMediaListEntryParams', {
	'id': Optional[int],
	'mediaId': Optional[int],
	'status': Optional['MediaListStatus'],
	'score': Optional[float],
	'scoreRaw': Optional[int],
	'progress': Optional[int],
	'progressVolumes': Optional[int],
	'repeat': Optional[int],
	'priority': Optional[int],
	'private': Optional[bool],
	'notes': Optional[str],
	'hiddenFromStatusLists': Optional[bool],
	'customLists': Optional[List[str]],
	'advancedScores': Optional[List[float]],
	'startedAt': Optional['FuzzyDateInput'],
	'completedAt': Optional['FuzzyDateInput'],
})


SaveMediaListEntryMutationResult = ClassVar[Optional['MediaList']]


UpdateMediaListEntriesParams = TypedDict('UpdateMediaListEntriesParams', {
	'status': Optional['MediaListStatus'],
	'score': Optional[float],
	'scoreRaw': Optional[int],
	'progress': Optional[int],
	'progressVolumes': Optional[int],
	'repeat': Optional[int],
	'priority': Optional[int],
	'private': Optional[bool],
	'notes': Optional[str],
	'hiddenFromStatusLists': Optional[bool],
	'advancedScores': Optional[List[float]],
	'startedAt': Optional['FuzzyDateInput'],
	'completedAt': Optional['FuzzyDateInput'],
	'ids': Optional[List[int]],
})


UpdateMediaListEntriesMutationResult = ClassVar[Optional[List['MediaList']]]


DeleteMediaListEntryParams = TypedDict('DeleteMediaListEntryParams', {
	'id': Optional[int],
})


DeleteMediaListEntryMutationResult = ClassVar[Optional['Deleted']]


DeleteCustomListParams = TypedDict('DeleteCustomListParams', {
	'customList': Optional[str],
	'type': Optional['MediaType'],
})


DeleteCustomListMutationResult = ClassVar[Optional['Deleted']]


SaveTextActivityParams = TypedDict('SaveTextActivityParams', {
	'id': Optional[int],
	'text': Optional[str],
	'locked': Optional[bool],
})


SaveTextActivityMutationResult = ClassVar[Optional['TextActivity']]


SaveMessageActivityParams = TypedDict('SaveMessageActivityParams', {
	'id': Optional[int],
	'message': Optional[str],
	'recipientId': Optional[int],
	'private': Optional[bool],
	'locked': Optional[bool],
	'asMod': Optional[bool],
})


SaveMessageActivityMutationResult = ClassVar[Optional['MessageActivity']]


SaveListActivityParams = TypedDict('SaveListActivityParams', {
	'id': Optional[int],
	'locked': Optional[bool],
})


SaveListActivityMutationResult = ClassVar[Optional['ListActivity']]


DeleteActivityParams = TypedDict('DeleteActivityParams', {
	'id': Optional[int],
})


DeleteActivityMutationResult = ClassVar[Optional['Deleted']]


ToggleActivityPinParams = TypedDict('ToggleActivityPinParams', {
	'id': Optional[int],
	'pinned': Optional[bool],
})


ToggleActivityPinMutationResult = ClassVar[Optional['ActivityUnion']]


ToggleActivitySubscriptionParams = TypedDict('ToggleActivitySubscriptionParams', {
	'activityId': Optional[int],
	'subscribe': Optional[bool],
})


ToggleActivitySubscriptionMutationResult = ClassVar[Optional['ActivityUnion']]


SaveActivityReplyParams = TypedDict('SaveActivityReplyParams', {
	'id': Optional[int],
	'activityId': Optional[int],
	'text': Optional[str],
	'asMod': Optional[bool],
})


SaveActivityReplyMutationResult = ClassVar[Optional['ActivityReply']]


DeleteActivityReplyParams = TypedDict('DeleteActivityReplyParams', {
	'id': Optional[int],
})


DeleteActivityReplyMutationResult = ClassVar[Optional['Deleted']]


ToggleLikeParams = TypedDict('ToggleLikeParams', {
	'id': Optional[int],
	'type': Optional['LikeableType'],
})


ToggleLikeMutationResult = ClassVar[Optional[List['User']]]


ToggleLikeV2Params = TypedDict('ToggleLikeV2Params', {
	'id': Optional[int],
	'type': Optional['LikeableType'],
})


ToggleLikeV2MutationResult = ClassVar[Optional['LikeableUnion']]


ToggleFollowParams = TypedDict('ToggleFollowParams', {
	'userId': Optional[int],
})


ToggleFollowMutationResult = ClassVar[Optional['User']]


ToggleFavouriteParams = TypedDict('ToggleFavouriteParams', {
	'animeId': Optional[int],
	'mangaId': Optional[int],
	'characterId': Optional[int],
	'staffId': Optional[int],
	'studioId': Optional[int],
})


ToggleFavouriteMutationResult = ClassVar[Optional['Favourites']]


UpdateFavouriteOrderParams = TypedDict('UpdateFavouriteOrderParams', {
	'animeIds': Optional[List[int]],
	'mangaIds': Optional[List[int]],
	'characterIds': Optional[List[int]],
	'staffIds': Optional[List[int]],
	'studioIds': Optional[List[int]],
	'animeOrder': Optional[List[int]],
	'mangaOrder': Optional[List[int]],
	'characterOrder': Optional[List[int]],
	'staffOrder': Optional[List[int]],
	'studioOrder': Optional[List[int]],
})


UpdateFavouriteOrderMutationResult = ClassVar[Optional['Favourites']]


SaveReviewParams = TypedDict('SaveReviewParams', {
	'id': Optional[int],
	'mediaId': Optional[int],
	'body': Optional[str],
	'summary': Optional[str],
	'score': Optional[int],
	'private': Optional[bool],
})


SaveReviewMutationResult = ClassVar[Optional['Review']]


DeleteReviewParams = TypedDict('DeleteReviewParams', {
	'id': Optional[int],
})


DeleteReviewMutationResult = ClassVar[Optional['Deleted']]


RateReviewParams = TypedDict('RateReviewParams', {
	'reviewId': Optional[int],
	'rating': Optional['ReviewRating'],
})


RateReviewMutationResult = ClassVar[Optional['Review']]


SaveRecommendationParams = TypedDict('SaveRecommendationParams', {
	'mediaId': Optional[int],
	'mediaRecommendationId': Optional[int],
	'rating': Optional['RecommendationRating'],
})


SaveRecommendationMutationResult = ClassVar[Optional['Recommendation']]


SaveThreadParams = TypedDict('SaveThreadParams', {
	'id': Optional[int],
	'title': Optional[str],
	'body': Optional[str],
	'categories': Optional[List[int]],
	'mediaCategories': Optional[List[int]],
	'sticky': Optional[bool],
	'locked': Optional[bool],
})


SaveThreadMutationResult = ClassVar[Optional['Thread']]


DeleteThreadParams = TypedDict('DeleteThreadParams', {
	'id': Optional[int],
})


DeleteThreadMutationResult = ClassVar[Optional['Deleted']]


ToggleThreadSubscriptionParams = TypedDict('ToggleThreadSubscriptionParams', {
	'threadId': Optional[int],
	'subscribe': Optional[bool],
})


ToggleThreadSubscriptionMutationResult = ClassVar[Optional['Thread']]


SaveThreadCommentParams = TypedDict('SaveThreadCommentParams', {
	'id': Optional[int],
	'threadId': Optional[int],
	'parentCommentId': Optional[int],
	'comment': Optional[str],
	'locked': Optional[bool],
})


SaveThreadCommentMutationResult = ClassVar[Optional['ThreadComment']]


DeleteThreadCommentParams = TypedDict('DeleteThreadCommentParams', {
	'id': Optional[int],
})


DeleteThreadCommentMutationResult = ClassVar[Optional['Deleted']]


UpdateAniChartSettingsParams = TypedDict('UpdateAniChartSettingsParams', {
	'titleLanguage': Optional[str],
	'outgoingLinkProvider': Optional[str],
	'theme': Optional[str],
	'sort': Optional[str],
})


UpdateAniChartSettingsMutationResult = ClassVar[Optional['Json']]


UpdateAniChartHighlightsParams = TypedDict('UpdateAniChartHighlightsParams', {
	'highlights': Optional[List['AniChartHighlightInput']],
})


UpdateAniChartHighlightsMutationResult = ClassVar[Optional['Json']]


NotificationOption = TypedDict('NotificationOption', {
	'type': Optional['NotificationType'],
	'enabled': Optional[bool],
})


Page = TypedDict('Page', {
	'pageInfo': Optional['PageInfo'],
	'users': Optional[List['User']],
	'media': Optional[List['Media']],
	'characters': Optional[List['Character']],
	'staff': Optional[List['Staff']],
	'studios': Optional[List['Studio']],
	'mediaList': Optional[List['MediaList']],
	'airingSchedules': Optional[List['AiringSchedule']],
	'mediaTrends': Optional[List['MediaTrend']],
	'notifications': Optional[List['NotificationUnion']],
	'followers': Optional[List['User']],
	'following': Optional[List['User']],
	'activities': Optional[List['ActivityUnion']],
	'activityReplies': Optional[List['ActivityReply']],
	'threads': Optional[List['Thread']],
	'threadComments': Optional[List['ThreadComment']],
	'reviews': Optional[List['Review']],
	'recommendations': Optional[List['Recommendation']],
	'likes': Optional[List['User']],
})


PageInfo = TypedDict('PageInfo', {
	'total': Optional[int],
	'perPage': Optional[int],
	'currentPage': Optional[int],
	'lastPage': Optional[int],
	'hasNextPage': Optional[bool],
})


ParsedMarkdown = TypedDict('ParsedMarkdown', {
	'html': Optional[str],
})


Query = TypedDict('Query', {
	'Page': 'PageQueryResult',
	'Media': 'MediaQueryResult',
	'MediaTrend': 'MediaTrendQueryResult',
	'AiringSchedule': 'AiringScheduleQueryResult',
	'Character': 'CharacterQueryResult',
	'Staff': 'StaffQueryResult',
	'MediaList': 'MediaListQueryResult',
	'MediaListCollection': 'MediaListCollectionQueryResult',
	'GenreCollection': 'GenreCollectionQueryResult',
	'MediaTagCollection': 'MediaTagCollectionQueryResult',
	'User': 'UserQueryResult',
	'Viewer': 'ViewerQueryResult',
	'Notification': 'NotificationQueryResult',
	'Studio': 'StudioQueryResult',
	'Review': 'ReviewQueryResult',
	'Activity': 'ActivityQueryResult',
	'ActivityReply': 'ActivityReplyQueryResult',
	'Following': 'FollowingQueryResult',
	'Follower': 'FollowerQueryResult',
	'Thread': 'ThreadQueryResult',
	'ThreadComment': 'ThreadCommentQueryResult',
	'Recommendation': 'RecommendationQueryResult',
	'Like': 'LikeQueryResult',
	'Markdown': 'MarkdownQueryResult',
	'AniChartUser': 'AniChartUserQueryResult',
	'SiteStatistics': 'SiteStatisticsQueryResult',
	'ExternalLinkSourceCollection': 'ExternalLinkSourceCollectionQueryResult',
})


PageParams = TypedDict('PageParams', {
	'page': Optional[int],
	'perPage': Optional[int],
})


PageQueryResult = ClassVar[Optional['Page']]


MediaParams = TypedDict('MediaParams', {
	'id': Optional[int],
	'idMal': Optional[int],
	'startDate': Optional['FuzzyDateInt'],
	'endDate': Optional['FuzzyDateInt'],
	'season': Optional['MediaSeason'],
	'seasonYear': Optional[int],
	'type': Optional['MediaType'],
	'format': Optional['MediaFormat'],
	'status': Optional['MediaStatus'],
	'episodes': Optional[int],
	'duration': Optional[int],
	'chapters': Optional[int],
	'volumes': Optional[int],
	'isAdult': Optional[bool],
	'genre': Optional[str],
	'tag': Optional[str],
	'minimumTagRank': Optional[int],
	'tagCategory': Optional[str],
	'onList': Optional[bool],
	'licensedBy': Optional[str],
	'licensedById': Optional[int],
	'averageScore': Optional[int],
	'popularity': Optional[int],
	'source': Optional['MediaSource'],
	'countryOfOrigin': Optional['CountryCode'],
	'isLicensed': Optional[bool],
	'search': Optional[str],
	'id_not': Optional[int],
	'id_in': Optional[List[int]],
	'id_not_in': Optional[List[int]],
	'idMal_not': Optional[int],
	'idMal_in': Optional[List[int]],
	'idMal_not_in': Optional[List[int]],
	'startDate_greater': Optional['FuzzyDateInt'],
	'startDate_lesser': Optional['FuzzyDateInt'],
	'startDate_like': Optional[str],
	'endDate_greater': Optional['FuzzyDateInt'],
	'endDate_lesser': Optional['FuzzyDateInt'],
	'endDate_like': Optional[str],
	'format_in': Optional[List['MediaFormat']],
	'format_not': Optional['MediaFormat'],
	'format_not_in': Optional[List['MediaFormat']],
	'status_in': Optional[List['MediaStatus']],
	'status_not': Optional['MediaStatus'],
	'status_not_in': Optional[List['MediaStatus']],
	'episodes_greater': Optional[int],
	'episodes_lesser': Optional[int],
	'duration_greater': Optional[int],
	'duration_lesser': Optional[int],
	'chapters_greater': Optional[int],
	'chapters_lesser': Optional[int],
	'volumes_greater': Optional[int],
	'volumes_lesser': Optional[int],
	'genre_in': Optional[List[str]],
	'genre_not_in': Optional[List[str]],
	'tag_in': Optional[List[str]],
	'tag_not_in': Optional[List[str]],
	'tagCategory_in': Optional[List[str]],
	'tagCategory_not_in': Optional[List[str]],
	'licensedBy_in': Optional[List[str]],
	'licensedById_in': Optional[List[int]],
	'averageScore_not': Optional[int],
	'averageScore_greater': Optional[int],
	'averageScore_lesser': Optional[int],
	'popularity_not': Optional[int],
	'popularity_greater': Optional[int],
	'popularity_lesser': Optional[int],
	'source_in': Optional[List['MediaSource']],
	'sort': Optional[List['MediaSort']],
})


MediaQueryResult = ClassVar[Optional['Media']]


MediaTrendParams = TypedDict('MediaTrendParams', {
	'mediaId': Optional[int],
	'date': Optional[int],
	'trending': Optional[int],
	'averageScore': Optional[int],
	'popularity': Optional[int],
	'episode': Optional[int],
	'releasing': Optional[bool],
	'mediaId_not': Optional[int],
	'mediaId_in': Optional[List[int]],
	'mediaId_not_in': Optional[List[int]],
	'date_greater': Optional[int],
	'date_lesser': Optional[int],
	'trending_greater': Optional[int],
	'trending_lesser': Optional[int],
	'trending_not': Optional[int],
	'averageScore_greater': Optional[int],
	'averageScore_lesser': Optional[int],
	'averageScore_not': Optional[int],
	'popularity_greater': Optional[int],
	'popularity_lesser': Optional[int],
	'popularity_not': Optional[int],
	'episode_greater': Optional[int],
	'episode_lesser': Optional[int],
	'episode_not': Optional[int],
	'sort': Optional[List['MediaTrendSort']],
})


MediaTrendQueryResult = ClassVar[Optional['MediaTrend']]


AiringScheduleParams = TypedDict('AiringScheduleParams', {
	'id': Optional[int],
	'mediaId': Optional[int],
	'episode': Optional[int],
	'airingAt': Optional[int],
	'notYetAired': Optional[bool],
	'id_not': Optional[int],
	'id_in': Optional[List[int]],
	'id_not_in': Optional[List[int]],
	'mediaId_not': Optional[int],
	'mediaId_in': Optional[List[int]],
	'mediaId_not_in': Optional[List[int]],
	'episode_not': Optional[int],
	'episode_in': Optional[List[int]],
	'episode_not_in': Optional[List[int]],
	'episode_greater': Optional[int],
	'episode_lesser': Optional[int],
	'airingAt_greater': Optional[int],
	'airingAt_lesser': Optional[int],
	'sort': Optional[List['AiringSort']],
})


AiringScheduleQueryResult = ClassVar[Optional['AiringSchedule']]


CharacterParams = TypedDict('CharacterParams', {
	'id': Optional[int],
	'isBirthday': Optional[bool],
	'search': Optional[str],
	'id_not': Optional[int],
	'id_in': Optional[List[int]],
	'id_not_in': Optional[List[int]],
	'sort': Optional[List['CharacterSort']],
})


CharacterQueryResult = ClassVar[Optional['Character']]


StaffParams = TypedDict('StaffParams', {
	'id': Optional[int],
	'isBirthday': Optional[bool],
	'search': Optional[str],
	'id_not': Optional[int],
	'id_in': Optional[List[int]],
	'id_not_in': Optional[List[int]],
	'sort': Optional[List['StaffSort']],
})


StaffQueryResult = ClassVar[Optional['Staff']]


MediaListParams = TypedDict('MediaListParams', {
	'id': Optional[int],
	'userId': Optional[int],
	'userName': Optional[str],
	'type': Optional['MediaType'],
	'status': Optional['MediaListStatus'],
	'mediaId': Optional[int],
	'isFollowing': Optional[bool],
	'notes': Optional[str],
	'startedAt': Optional['FuzzyDateInt'],
	'completedAt': Optional['FuzzyDateInt'],
	'compareWithAuthList': Optional[bool],
	'userId_in': Optional[List[int]],
	'status_in': Optional[List['MediaListStatus']],
	'status_not_in': Optional[List['MediaListStatus']],
	'status_not': Optional['MediaListStatus'],
	'mediaId_in': Optional[List[int]],
	'mediaId_not_in': Optional[List[int]],
	'notes_like': Optional[str],
	'startedAt_greater': Optional['FuzzyDateInt'],
	'startedAt_lesser': Optional['FuzzyDateInt'],
	'startedAt_like': Optional[str],
	'completedAt_greater': Optional['FuzzyDateInt'],
	'completedAt_lesser': Optional['FuzzyDateInt'],
	'completedAt_like': Optional[str],
	'sort': Optional[List['MediaListSort']],
})


MediaListQueryResult = ClassVar[Optional['MediaList']]


MediaListCollectionParams = TypedDict('MediaListCollectionParams', {
	'userId': Optional[int],
	'userName': Optional[str],
	'type': Optional['MediaType'],
	'status': Optional['MediaListStatus'],
	'notes': Optional[str],
	'startedAt': Optional['FuzzyDateInt'],
	'completedAt': Optional['FuzzyDateInt'],
	'forceSingleCompletedList': Optional[bool],
	'chunk': Optional[int],
	'perChunk': Optional[int],
	'status_in': Optional[List['MediaListStatus']],
	'status_not_in': Optional[List['MediaListStatus']],
	'status_not': Optional['MediaListStatus'],
	'notes_like': Optional[str],
	'startedAt_greater': Optional['FuzzyDateInt'],
	'startedAt_lesser': Optional['FuzzyDateInt'],
	'startedAt_like': Optional[str],
	'completedAt_greater': Optional['FuzzyDateInt'],
	'completedAt_lesser': Optional['FuzzyDateInt'],
	'completedAt_like': Optional[str],
	'sort': Optional[List['MediaListSort']],
})


MediaListCollectionQueryResult = ClassVar[Optional['MediaListCollection']]


GenreCollectionQueryResult = ClassVar[Optional[List[str]]]


MediaTagCollectionParams = TypedDict('MediaTagCollectionParams', {
	'status': Optional[int],
})


MediaTagCollectionQueryResult = ClassVar[Optional[List['MediaTag']]]


UserParams = TypedDict('UserParams', {
	'id': Optional[int],
	'name': Optional[str],
	'isModerator': Optional[bool],
	'search': Optional[str],
	'sort': Optional[List['UserSort']],
})


UserQueryResult = ClassVar[Optional['User']]


ViewerQueryResult = ClassVar[Optional['User']]


NotificationParams = TypedDict('NotificationParams', {
	'type': Optional['NotificationType'],
	'resetNotificationCount': Optional[bool],
	'type_in': Optional[List['NotificationType']],
})


NotificationQueryResult = ClassVar[Optional['NotificationUnion']]


StudioParams = TypedDict('StudioParams', {
	'id': Optional[int],
	'search': Optional[str],
	'id_not': Optional[int],
	'id_in': Optional[List[int]],
	'id_not_in': Optional[List[int]],
	'sort': Optional[List['StudioSort']],
})


StudioQueryResult = ClassVar[Optional['Studio']]


ReviewParams = TypedDict('ReviewParams', {
	'id': Optional[int],
	'mediaId': Optional[int],
	'userId': Optional[int],
	'mediaType': Optional['MediaType'],
	'sort': Optional[List['ReviewSort']],
})


ReviewQueryResult = ClassVar[Optional['Review']]


ActivityParams = TypedDict('ActivityParams', {
	'id': Optional[int],
	'userId': Optional[int],
	'messengerId': Optional[int],
	'mediaId': Optional[int],
	'type': Optional['ActivityType'],
	'isFollowing': Optional[bool],
	'hasReplies': Optional[bool],
	'hasRepliesOrTypeText': Optional[bool],
	'createdAt': Optional[int],
	'id_not': Optional[int],
	'id_in': Optional[List[int]],
	'id_not_in': Optional[List[int]],
	'userId_not': Optional[int],
	'userId_in': Optional[List[int]],
	'userId_not_in': Optional[List[int]],
	'messengerId_not': Optional[int],
	'messengerId_in': Optional[List[int]],
	'messengerId_not_in': Optional[List[int]],
	'mediaId_not': Optional[int],
	'mediaId_in': Optional[List[int]],
	'mediaId_not_in': Optional[List[int]],
	'type_not': Optional['ActivityType'],
	'type_in': Optional[List['ActivityType']],
	'type_not_in': Optional[List['ActivityType']],
	'createdAt_greater': Optional[int],
	'createdAt_lesser': Optional[int],
	'sort': Optional[List['ActivitySort']],
})


ActivityQueryResult = ClassVar[Optional['ActivityUnion']]


ActivityReplyParams = TypedDict('ActivityReplyParams', {
	'id': Optional[int],
	'activityId': Optional[int],
})


ActivityReplyQueryResult = ClassVar[Optional['ActivityReply']]


FollowingParams = TypedDict('FollowingParams', {
	'userId': int,
	'sort': Optional[List['UserSort']],
})


FollowingQueryResult = ClassVar[Optional['User']]


FollowerParams = TypedDict('FollowerParams', {
	'userId': int,
	'sort': Optional[List['UserSort']],
})


FollowerQueryResult = ClassVar[Optional['User']]


ThreadParams = TypedDict('ThreadParams', {
	'id': Optional[int],
	'userId': Optional[int],
	'replyUserId': Optional[int],
	'subscribed': Optional[bool],
	'categoryId': Optional[int],
	'mediaCategoryId': Optional[int],
	'search': Optional[str],
	'id_in': Optional[List[int]],
	'sort': Optional[List['ThreadSort']],
})


ThreadQueryResult = ClassVar[Optional['Thread']]


ThreadCommentParams = TypedDict('ThreadCommentParams', {
	'id': Optional[int],
	'threadId': Optional[int],
	'userId': Optional[int],
	'sort': Optional[List['ThreadCommentSort']],
})


ThreadCommentQueryResult = ClassVar[Optional[List['ThreadComment']]]


RecommendationParams = TypedDict('RecommendationParams', {
	'id': Optional[int],
	'mediaId': Optional[int],
	'mediaRecommendationId': Optional[int],
	'userId': Optional[int],
	'rating': Optional[int],
	'onList': Optional[bool],
	'rating_greater': Optional[int],
	'rating_lesser': Optional[int],
	'sort': Optional[List['RecommendationSort']],
})


RecommendationQueryResult = ClassVar[Optional['Recommendation']]


LikeParams = TypedDict('LikeParams', {
	'likeableId': Optional[int],
	'type': Optional['LikeableType'],
})


LikeQueryResult = ClassVar[Optional['User']]


MarkdownParams = TypedDict('MarkdownParams', {
	'markdown': str,
})


MarkdownQueryResult = ClassVar[Optional['ParsedMarkdown']]


AniChartUserQueryResult = ClassVar[Optional['AniChartUser']]


SiteStatisticsQueryResult = ClassVar[Optional['SiteStatistics']]


ExternalLinkSourceCollectionParams = TypedDict('ExternalLinkSourceCollectionParams', {
	'id': Optional[int],
	'type': Optional['ExternalLinkType'],
	'mediaType': Optional['ExternalLinkMediaType'],
})


ExternalLinkSourceCollectionQueryResult = ClassVar[Optional[List['MediaExternalLink']]]


Recommendation = TypedDict('Recommendation', {
	'id': int,
	'rating': Optional[int],
	'userRating': Optional['RecommendationRating'],
	'media': Optional['Media'],
	'mediaRecommendation': Optional['Media'],
	'user': Optional['User'],
})


RecommendationConnection = TypedDict('RecommendationConnection', {
	'edges': Optional[List['RecommendationEdge']],
	'nodes': Optional[List['Recommendation']],
	'pageInfo': Optional['PageInfo'],
})


RecommendationEdge = TypedDict('RecommendationEdge', {
	'node': Optional['Recommendation'],
})


RelatedMediaAdditionNotification = TypedDict('RelatedMediaAdditionNotification', {
	'id': int,
	'type': Optional['NotificationType'],
	'mediaId': int,
	'context': Optional[str],
	'createdAt': Optional[int],
	'media': Optional['Media'],
})


Report = TypedDict('Report', {
	'id': int,
	'reporter': Optional['User'],
	'reported': Optional['User'],
	'reason': Optional[str],
	'createdAt': Optional[int],
	'cleared': Optional[bool],
})


Review = TypedDict('Review', {
	'id': int,
	'userId': int,
	'mediaId': int,
	'mediaType': Optional['MediaType'],
	'summary': Optional[str],
	'body': Optional[str],
	'rating': Optional[int],
	'ratingAmount': Optional[int],
	'userRating': Optional['ReviewRating'],
	'score': Optional[int],
	'private': Optional[bool],
	'siteUrl': Optional[str],
	'createdAt': int,
	'updatedAt': int,
	'user': Optional['User'],
	'media': Optional['Media'],
})


ReviewConnection = TypedDict('ReviewConnection', {
	'edges': Optional[List['ReviewEdge']],
	'nodes': Optional[List['Review']],
	'pageInfo': Optional['PageInfo'],
})


ReviewEdge = TypedDict('ReviewEdge', {
	'node': Optional['Review'],
})


RevisionHistory = TypedDict('RevisionHistory', {
	'id': int,
	'action': Optional['RevisionHistoryAction'],
	'changes': Optional['Json'],
	'user': Optional['User'],
	'media': Optional['Media'],
	'character': Optional['Character'],
	'staff': Optional['Staff'],
	'studio': Optional['Studio'],
	'externalLink': Optional['MediaExternalLink'],
	'createdAt': Optional[int],
})


ScoreDistribution = TypedDict('ScoreDistribution', {
	'score': Optional[int],
	'amount': Optional[int],
})


SiteStatistics = TypedDict('SiteStatistics', {
	'users': Optional['SiteTrendConnection'],
	'anime': Optional['SiteTrendConnection'],
	'manga': Optional['SiteTrendConnection'],
	'characters': Optional['SiteTrendConnection'],
	'staff': Optional['SiteTrendConnection'],
	'studios': Optional['SiteTrendConnection'],
	'reviews': Optional['SiteTrendConnection'],
})


SiteTrend = TypedDict('SiteTrend', {
	'date': int,
	'count': int,
	'change': int,
})


SiteTrendConnection = TypedDict('SiteTrendConnection', {
	'edges': Optional[List['SiteTrendEdge']],
	'nodes': Optional[List['SiteTrend']],
	'pageInfo': Optional['PageInfo'],
})


SiteTrendEdge = TypedDict('SiteTrendEdge', {
	'node': Optional['SiteTrend'],
})


Staff = TypedDict('Staff', {
	'id': int,
	'name': Optional['StaffName'],
	'language': Optional['StaffLanguage'],
	'languageV2': Optional[str],
	'image': Optional['StaffImage'],
	'description': Optional[str],
	'primaryOccupations': Optional[List[str]],
	'gender': Optional[str],
	'dateOfBirth': Optional['FuzzyDate'],
	'dateOfDeath': Optional['FuzzyDate'],
	'age': Optional[int],
	'yearsActive': Optional[List[int]],
	'homeTown': Optional[str],
	'bloodType': Optional[str],
	'isFavourite': bool,
	'isFavouriteBlocked': bool,
	'siteUrl': Optional[str],
	'staffMedia': Optional['MediaConnection'],
	'characters': Optional['CharacterConnection'],
	'characterMedia': Optional['MediaConnection'],
	'updatedAt': Optional[int],
	'staff': Optional['Staff'],
	'submitter': Optional['User'],
	'submissionStatus': Optional[int],
	'submissionNotes': Optional[str],
	'favourites': Optional[int],
	'modNotes': Optional[str],
})


StaffConnection = TypedDict('StaffConnection', {
	'edges': Optional[List['StaffEdge']],
	'nodes': Optional[List['Staff']],
	'pageInfo': Optional['PageInfo'],
})


StaffEdge = TypedDict('StaffEdge', {
	'node': Optional['Staff'],
	'id': Optional[int],
	'role': Optional[str],
	'favouriteOrder': Optional[int],
})


StaffImage = TypedDict('StaffImage', {
	'large': Optional[str],
	'medium': Optional[str],
})


StaffName = TypedDict('StaffName', {
	'first': Optional[str],
	'middle': Optional[str],
	'last': Optional[str],
	'full': Optional[str],
	'native': Optional[str],
	'alternative': Optional[List[str]],
	'userPreferred': Optional[str],
})


StaffRoleType = TypedDict('StaffRoleType', {
	'voiceActor': Optional['Staff'],
	'roleNotes': Optional[str],
	'dubGroup': Optional[str],
})


StaffStats = TypedDict('StaffStats', {
	'staff': Optional['Staff'],
	'amount': Optional[int],
	'meanScore': Optional[int],
	'timeWatched': Optional[int],
})


StaffSubmission = TypedDict('StaffSubmission', {
	'id': int,
	'staff': Optional['Staff'],
	'submission': Optional['Staff'],
	'submitter': Optional['User'],
	'assignee': Optional['User'],
	'status': Optional['SubmissionStatus'],
	'notes': Optional[str],
	'source': Optional[str],
	'locked': Optional[bool],
	'createdAt': Optional[int],
})


StatusDistribution = TypedDict('StatusDistribution', {
	'status': Optional['MediaListStatus'],
	'amount': Optional[int],
})


Studio = TypedDict('Studio', {
	'id': int,
	'name': str,
	'isAnimationStudio': bool,
	'media': Optional['MediaConnection'],
	'siteUrl': Optional[str],
	'isFavourite': bool,
	'favourites': Optional[int],
})


StudioConnection = TypedDict('StudioConnection', {
	'edges': Optional[List['StudioEdge']],
	'nodes': Optional[List['Studio']],
	'pageInfo': Optional['PageInfo'],
})


StudioEdge = TypedDict('StudioEdge', {
	'node': Optional['Studio'],
	'id': Optional[int],
	'isMain': bool,
	'favouriteOrder': Optional[int],
})


StudioStats = TypedDict('StudioStats', {
	'studio': Optional['Studio'],
	'amount': Optional[int],
	'meanScore': Optional[int],
	'timeWatched': Optional[int],
})


TagStats = TypedDict('TagStats', {
	'tag': Optional['MediaTag'],
	'amount': Optional[int],
	'meanScore': Optional[int],
	'timeWatched': Optional[int],
})


TextActivity = TypedDict('TextActivity', {
	'id': int,
	'userId': Optional[int],
	'type': Optional['ActivityType'],
	'replyCount': int,
	'text': Optional[str],
	'siteUrl': Optional[str],
	'isLocked': Optional[bool],
	'isSubscribed': Optional[bool],
	'likeCount': int,
	'isLiked': Optional[bool],
	'isPinned': Optional[bool],
	'createdAt': int,
	'user': Optional['User'],
	'replies': Optional[List['ActivityReply']],
	'likes': Optional[List['User']],
})


Thread = TypedDict('Thread', {
	'id': int,
	'title': Optional[str],
	'body': Optional[str],
	'userId': int,
	'replyUserId': Optional[int],
	'replyCommentId': Optional[int],
	'replyCount': Optional[int],
	'viewCount': Optional[int],
	'isLocked': Optional[bool],
	'isSticky': Optional[bool],
	'isSubscribed': Optional[bool],
	'likeCount': int,
	'isLiked': Optional[bool],
	'repliedAt': Optional[int],
	'createdAt': int,
	'updatedAt': int,
	'user': Optional['User'],
	'replyUser': Optional['User'],
	'likes': Optional[List['User']],
	'siteUrl': Optional[str],
	'categories': Optional[List['ThreadCategory']],
	'mediaCategories': Optional[List['Media']],
})


ThreadCategory = TypedDict('ThreadCategory', {
	'id': int,
	'name': str,
})


ThreadComment = TypedDict('ThreadComment', {
	'id': int,
	'userId': Optional[int],
	'threadId': Optional[int],
	'comment': Optional[str],
	'likeCount': int,
	'isLiked': Optional[bool],
	'siteUrl': Optional[str],
	'createdAt': int,
	'updatedAt': int,
	'thread': Optional['Thread'],
	'user': Optional['User'],
	'likes': Optional[List['User']],
	'childComments': Optional['Json'],
	'isLocked': Optional[bool],
})


ThreadCommentLikeNotification = TypedDict('ThreadCommentLikeNotification', {
	'id': int,
	'userId': int,
	'type': Optional['NotificationType'],
	'commentId': int,
	'context': Optional[str],
	'createdAt': Optional[int],
	'thread': Optional['Thread'],
	'comment': Optional['ThreadComment'],
	'user': Optional['User'],
})


ThreadCommentMentionNotification = TypedDict('ThreadCommentMentionNotification', {
	'id': int,
	'userId': int,
	'type': Optional['NotificationType'],
	'commentId': int,
	'context': Optional[str],
	'createdAt': Optional[int],
	'thread': Optional['Thread'],
	'comment': Optional['ThreadComment'],
	'user': Optional['User'],
})


ThreadCommentReplyNotification = TypedDict('ThreadCommentReplyNotification', {
	'id': int,
	'userId': int,
	'type': Optional['NotificationType'],
	'commentId': int,
	'context': Optional[str],
	'createdAt': Optional[int],
	'thread': Optional['Thread'],
	'comment': Optional['ThreadComment'],
	'user': Optional['User'],
})


ThreadCommentSubscribedNotification = TypedDict('ThreadCommentSubscribedNotification', {
	'id': int,
	'userId': int,
	'type': Optional['NotificationType'],
	'commentId': int,
	'context': Optional[str],
	'createdAt': Optional[int],
	'thread': Optional['Thread'],
	'comment': Optional['ThreadComment'],
	'user': Optional['User'],
})


ThreadLikeNotification = TypedDict('ThreadLikeNotification', {
	'id': int,
	'userId': int,
	'type': Optional['NotificationType'],
	'threadId': int,
	'context': Optional[str],
	'createdAt': Optional[int],
	'thread': Optional['Thread'],
	'comment': Optional['ThreadComment'],
	'user': Optional['User'],
})


User = TypedDict('User', {
	'id': int,
	'name': str,
	'about': Optional[str],
	'avatar': Optional['UserAvatar'],
	'bannerImage': Optional[str],
	'isFollowing': Optional[bool],
	'isFollower': Optional[bool],
	'isBlocked': Optional[bool],
	'bans': Optional['Json'],
	'options': Optional['UserOptions'],
	'mediaListOptions': Optional['MediaListOptions'],
	'favourites': Optional['Favourites'],
	'statistics': Optional['UserStatisticTypes'],
	'unreadNotificationCount': Optional[int],
	'siteUrl': Optional[str],
	'donatorTier': Optional[int],
	'donatorBadge': Optional[str],
	'moderatorRoles': Optional[List['ModRole']],
	'createdAt': Optional[int],
	'updatedAt': Optional[int],
	'stats': Optional['UserStats'],
	'moderatorStatus': Optional[str],
	'previousNames': Optional[List['UserPreviousName']],
})


UserActivityHistory = TypedDict('UserActivityHistory', {
	'date': Optional[int],
	'amount': Optional[int],
	'level': Optional[int],
})


UserAvatar = TypedDict('UserAvatar', {
	'large': Optional[str],
	'medium': Optional[str],
})


UserCountryStatistic = TypedDict('UserCountryStatistic', {
	'count': int,
	'meanScore': float,
	'minutesWatched': int,
	'chaptersRead': int,
	'mediaIds': List[int],
	'country': Optional['CountryCode'],
})


UserFormatStatistic = TypedDict('UserFormatStatistic', {
	'count': int,
	'meanScore': float,
	'minutesWatched': int,
	'chaptersRead': int,
	'mediaIds': List[int],
	'format': Optional['MediaFormat'],
})


UserGenreStatistic = TypedDict('UserGenreStatistic', {
	'count': int,
	'meanScore': float,
	'minutesWatched': int,
	'chaptersRead': int,
	'mediaIds': List[int],
	'genre': Optional[str],
})


UserLengthStatistic = TypedDict('UserLengthStatistic', {
	'count': int,
	'meanScore': float,
	'minutesWatched': int,
	'chaptersRead': int,
	'mediaIds': List[int],
	'length': Optional[str],
})


UserModData = TypedDict('UserModData', {
	'alts': Optional[List['User']],
	'bans': Optional['Json'],
	'ip': Optional['Json'],
	'counts': Optional['Json'],
	'privacy': Optional[int],
	'email': Optional[str],
})


UserOptions = TypedDict('UserOptions', {
	'titleLanguage': Optional['UserTitleLanguage'],
	'displayAdultContent': Optional[bool],
	'airingNotifications': Optional[bool],
	'profileColor': Optional[str],
	'notificationOptions': Optional[List['NotificationOption']],
	'timezone': Optional[str],
	'activityMergeTime': Optional[int],
	'staffNameLanguage': Optional['UserStaffNameLanguage'],
	'restrictMessagesToFollowing': Optional[bool],
	'disabledListActivity': Optional[List['ListActivityOption']],
})


UserPreviousName = TypedDict('UserPreviousName', {
	'name': Optional[str],
	'createdAt': Optional[int],
	'updatedAt': Optional[int],
})


UserReleaseYearStatistic = TypedDict('UserReleaseYearStatistic', {
	'count': int,
	'meanScore': float,
	'minutesWatched': int,
	'chaptersRead': int,
	'mediaIds': List[int],
	'releaseYear': Optional[int],
})


UserScoreStatistic = TypedDict('UserScoreStatistic', {
	'count': int,
	'meanScore': float,
	'minutesWatched': int,
	'chaptersRead': int,
	'mediaIds': List[int],
	'score': Optional[int],
})


UserStaffStatistic = TypedDict('UserStaffStatistic', {
	'count': int,
	'meanScore': float,
	'minutesWatched': int,
	'chaptersRead': int,
	'mediaIds': List[int],
	'staff': Optional['Staff'],
})


UserStartYearStatistic = TypedDict('UserStartYearStatistic', {
	'count': int,
	'meanScore': float,
	'minutesWatched': int,
	'chaptersRead': int,
	'mediaIds': List[int],
	'startYear': Optional[int],
})


UserStatistics = TypedDict('UserStatistics', {
	'count': int,
	'meanScore': float,
	'standardDeviation': float,
	'minutesWatched': int,
	'episodesWatched': int,
	'chaptersRead': int,
	'volumesRead': int,
	'formats': Optional[List['UserFormatStatistic']],
	'statuses': Optional[List['UserStatusStatistic']],
	'scores': Optional[List['UserScoreStatistic']],
	'lengths': Optional[List['UserLengthStatistic']],
	'releaseYears': Optional[List['UserReleaseYearStatistic']],
	'startYears': Optional[List['UserStartYearStatistic']],
	'genres': Optional[List['UserGenreStatistic']],
	'tags': Optional[List['UserTagStatistic']],
	'countries': Optional[List['UserCountryStatistic']],
	'voiceActors': Optional[List['UserVoiceActorStatistic']],
	'staff': Optional[List['UserStaffStatistic']],
	'studios': Optional[List['UserStudioStatistic']],
})


UserStatisticTypes = TypedDict('UserStatisticTypes', {
	'anime': Optional['UserStatistics'],
	'manga': Optional['UserStatistics'],
})


UserStats = TypedDict('UserStats', {
	'watchedTime': Optional[int],
	'chaptersRead': Optional[int],
	'activityHistory': Optional[List['UserActivityHistory']],
	'animeStatusDistribution': Optional[List['StatusDistribution']],
	'mangaStatusDistribution': Optional[List['StatusDistribution']],
	'animeScoreDistribution': Optional[List['ScoreDistribution']],
	'mangaScoreDistribution': Optional[List['ScoreDistribution']],
	'animeListScores': Optional['ListScoreStats'],
	'mangaListScores': Optional['ListScoreStats'],
	'favouredGenresOverview': Optional[List['GenreStats']],
	'favouredGenres': Optional[List['GenreStats']],
	'favouredTags': Optional[List['TagStats']],
	'favouredActors': Optional[List['StaffStats']],
	'favouredStaff': Optional[List['StaffStats']],
	'favouredStudios': Optional[List['StudioStats']],
	'favouredYears': Optional[List['YearStats']],
	'favouredFormats': Optional[List['FormatStats']],
})


UserStatusStatistic = TypedDict('UserStatusStatistic', {
	'count': int,
	'meanScore': float,
	'minutesWatched': int,
	'chaptersRead': int,
	'mediaIds': List[int],
	'status': Optional['MediaListStatus'],
})


UserStudioStatistic = TypedDict('UserStudioStatistic', {
	'count': int,
	'meanScore': float,
	'minutesWatched': int,
	'chaptersRead': int,
	'mediaIds': List[int],
	'studio': Optional['Studio'],
})


UserTagStatistic = TypedDict('UserTagStatistic', {
	'count': int,
	'meanScore': float,
	'minutesWatched': int,
	'chaptersRead': int,
	'mediaIds': List[int],
	'tag': Optional['MediaTag'],
})


UserVoiceActorStatistic = TypedDict('UserVoiceActorStatistic', {
	'count': int,
	'meanScore': float,
	'minutesWatched': int,
	'chaptersRead': int,
	'mediaIds': List[int],
	'voiceActor': Optional['Staff'],
	'characterIds': List[int],
})


YearStats = TypedDict('YearStats', {
	'year': Optional[int],
	'amount': Optional[int],
	'meanScore': Optional[int],
})


AiringScheduleInput = TypedDict('AiringScheduleInput', {
	'airingAt': Optional[int],
	'episode': Optional[int],
	'timeUntilAiring': Optional[int],
})


AniChartHighlightInput = TypedDict('AniChartHighlightInput', {
	'mediaId': Optional[int],
	'highlight': Optional[str],
})


CharacterNameInput = TypedDict('CharacterNameInput', {
	'first': Optional[str],
	'middle': Optional[str],
	'last': Optional[str],
	'native': Optional[str],
	'alternative': Optional[List[str]],
	'alternativeSpoiler': Optional[List[str]],
})


FuzzyDateInput = TypedDict('FuzzyDateInput', {
	'year': Optional[int],
	'month': Optional[int],
	'day': Optional[int],
})


ListActivityOptionInput = TypedDict('ListActivityOptionInput', {
	'disabled': Optional[bool],
	'type': Optional['MediaListStatus'],
})


MediaExternalLinkInput = TypedDict('MediaExternalLinkInput', {
	'id': int,
	'url': str,
	'site': str,
})


MediaListOptionsInput = TypedDict('MediaListOptionsInput', {
	'sectionOrder': Optional[List[str]],
	'splitCompletedSectionByFormat': Optional[bool],
	'customLists': Optional[List[str]],
	'advancedScoring': Optional[List[str]],
	'advancedScoringEnabled': Optional[bool],
	'theme': Optional[str],
})


MediaTitleInput = TypedDict('MediaTitleInput', {
	'romaji': Optional[str],
	'english': Optional[str],
	'native': Optional[str],
})


NotificationOptionInput = TypedDict('NotificationOptionInput', {
	'type': Optional['NotificationType'],
	'enabled': Optional[bool],
})


StaffNameInput = TypedDict('StaffNameInput', {
	'first': Optional[str],
	'middle': Optional[str],
	'last': Optional[str],
	'native': Optional[str],
	'alternative': Optional[List[str]],
})


