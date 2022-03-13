from enum import Enum
from typing import ClassVar, List, Optional, TypedDict


_CallingCodeOrdering = Enum('_CallingCodeOrdering', '_id_asc _id_desc name_asc name_desc')


_CountryOrdering = Enum('_CountryOrdering', '_id_asc _id_desc alpha2Code_asc alpha2Code_desc alpha3Code_asc alpha3Code_desc area_asc area_desc capital_asc capital_desc populationDensity_asc populationDensity_desc demonym_asc demonym_desc gini_asc gini_desc name_asc name_desc nativeName_asc nativeName_desc numericCode_asc numericCode_desc population_asc population_desc')


_CurrencyOrdering = Enum('_CurrencyOrdering', '_id_asc _id_desc code_asc code_desc name_asc name_desc symbol_asc symbol_desc')


_DistanceToOtherCountryOrdering = Enum('_DistanceToOtherCountryOrdering', 'distanceInKm_asc distanceInKm_desc countryName_asc countryName_desc _id_asc _id_desc')


_FlagOrdering = Enum('_FlagOrdering', '_id_asc _id_desc emoji_asc emoji_desc emojiUnicode_asc emojiUnicode_desc svgFile_asc svgFile_desc')


_LanguageOrdering = Enum('_LanguageOrdering', '_id_asc _id_desc iso639_1_asc iso639_1_desc iso639_2_asc iso639_2_desc name_asc name_desc nativeName_asc nativeName_desc')


_RegionalBlocOrdering = Enum('_RegionalBlocOrdering', '_id_asc _id_desc acronym_asc acronym_desc name_asc name_desc')


_RegionOrdering = Enum('_RegionOrdering', '_id_asc _id_desc name_asc name_desc')


_RelationDirections = Enum('_RelationDirections', 'IN OUT')


_SubregionOrdering = Enum('_SubregionOrdering', '_id_asc _id_desc name_asc name_desc')


_TimezoneOrdering = Enum('_TimezoneOrdering', '_id_asc _id_desc name_asc name_desc')


_TopLevelDomainOrdering = Enum('_TopLevelDomainOrdering', '_id_asc _id_desc name_asc name_desc')


_TranslationOrdering = Enum('_TranslationOrdering', '_id_asc _id_desc languageCode_asc languageCode_desc value_asc value_desc')


AreaUnit = Enum('AreaUnit', 'SQUARE_KILOMETERS SQUARE_METERS SQUARE_MILES')


_Neo4jDate = TypedDict('_Neo4jDate', {
	'year': Optional[int],
	'month': Optional[int],
	'day': Optional[int],
	'formatted': Optional[str],
})


_Neo4jDateTime = TypedDict('_Neo4jDateTime', {
	'year': Optional[int],
	'month': Optional[int],
	'day': Optional[int],
	'hour': Optional[int],
	'minute': Optional[int],
	'second': Optional[int],
	'millisecond': Optional[int],
	'microsecond': Optional[int],
	'nanosecond': Optional[int],
	'timezone': Optional[str],
	'formatted': Optional[str],
})


_Neo4jLocalDateTime = TypedDict('_Neo4jLocalDateTime', {
	'year': Optional[int],
	'month': Optional[int],
	'day': Optional[int],
	'hour': Optional[int],
	'minute': Optional[int],
	'second': Optional[int],
	'millisecond': Optional[int],
	'microsecond': Optional[int],
	'nanosecond': Optional[int],
	'formatted': Optional[str],
})


_Neo4jLocalTime = TypedDict('_Neo4jLocalTime', {
	'hour': Optional[int],
	'minute': Optional[int],
	'second': Optional[int],
	'millisecond': Optional[int],
	'microsecond': Optional[int],
	'nanosecond': Optional[int],
	'formatted': Optional[str],
})


_Neo4jPoint = TypedDict('_Neo4jPoint', {
	'x': Optional[float],
	'y': Optional[float],
	'z': Optional[float],
	'longitude': Optional[float],
	'latitude': Optional[float],
	'height': Optional[float],
	'crs': Optional[str],
	'srid': Optional[int],
})


_Neo4jTime = TypedDict('_Neo4jTime', {
	'hour': Optional[int],
	'minute': Optional[int],
	'second': Optional[int],
	'millisecond': Optional[int],
	'microsecond': Optional[int],
	'nanosecond': Optional[int],
	'timezone': Optional[str],
	'formatted': Optional[str],
})


AlternativeSpelling = TypedDict('AlternativeSpelling', {
	'_id': str,
	'name': str,
	'countries': Optional[List['Country']],
})


Area = TypedDict('Area', {
	'value': Optional[float],
	'unit': Optional[str],
	'populationDensity': Optional[float],
})


CallingCode = TypedDict('CallingCode', {
	'_id': Optional[str],
	'name': str,
	'countries': Optional[List['Country']],
})


Country = TypedDict('Country', {
	'_id': Optional[str],
	'alpha2Code': str,
	'alpha3Code': str,
	'area': Optional[float],
	'capital': str,
	'populationDensity': Optional[float],
	'convertedArea': Optional['Area'],
	'demonym': str,
	'gini': Optional[float],
	'location': '_Neo4jPoint',
	'name': str,
	'nameTranslations': Optional[List['Translation']],
	'nativeName': str,
	'numericCode': Optional[str],
	'population': float,
	'topLevelDomains': Optional[List['TopLevelDomain']],
	'callingCodes': Optional[List['CallingCode']],
	'alternativeSpellings': Optional[List['AlternativeSpelling']],
	'timezones': Optional[List['Timezone']],
	'borders': Optional[List['Country']],
	'subregion': Optional['Subregion'],
	'officialLanguages': Optional[List['Language']],
	'currencies': Optional[List['Currency']],
	'regionalBlocs': Optional[List['RegionalBloc']],
	'flag': Optional['Flag'],
	'distanceToOtherCountries': Optional[List['DistanceToOtherCountry']],
	'shortestPathToOtherCountry': Optional[List['Country']],
})


Currency = TypedDict('Currency', {
	'_id': Optional[str],
	'code': str,
	'name': str,
	'symbol': str,
	'countries': Optional[List['Country']],
})


DistanceToOtherCountry = TypedDict('DistanceToOtherCountry', {
	'distanceInKm': Optional[float],
	'countryName': Optional[str],
	'_id': Optional[str],
})


Flag = TypedDict('Flag', {
	'_id': Optional[str],
	'emoji': str,
	'emojiUnicode': str,
	'svgFile': str,
	'country': Optional['Country'],
})


Language = TypedDict('Language', {
	'_id': Optional[str],
	'iso639_1': str,
	'iso639_2': str,
	'name': str,
	'nativeName': str,
	'countries': Optional[List['Country']],
})


OtherAcronym = TypedDict('OtherAcronym', {
	'_id': str,
	'name': str,
	'regionalBlocs': Optional[List['RegionalBloc']],
})


OtherName = TypedDict('OtherName', {
	'_id': str,
	'name': str,
	'regionalBlocs': Optional[List['RegionalBloc']],
})


Query = TypedDict('Query', {
	'Country': 'CountryQueryResult',
	'Timezone': 'TimezoneQueryResult',
	'Subregion': 'SubregionQueryResult',
	'Region': 'RegionQueryResult',
	'Language': 'LanguageQueryResult',
	'Currency': 'CurrencyQueryResult',
	'RegionalBloc': 'RegionalBlocQueryResult',
	'Translation': 'TranslationQueryResult',
	'Flag': 'FlagQueryResult',
	'DistanceToOtherCountry': 'DistanceToOtherCountryQueryResult',
	'TopLevelDomain': 'TopLevelDomainQueryResult',
	'CallingCode': 'CallingCodeQueryResult',
})


CountryParams = TypedDict('CountryParams', {
	'_id': Optional[str],
	'alpha2Code': Optional[str],
	'alpha3Code': Optional[str],
	'area': Optional[float],
	'capital': Optional[str],
	'populationDensity': Optional[float],
	'demonym': Optional[str],
	'gini': Optional[float],
	'location': Optional['_Neo4jPointInput'],
	'name': Optional[str],
	'nativeName': Optional[str],
	'numericCode': Optional[str],
	'population': Optional[float],
	'first': Optional[int],
	'offset': Optional[int],
	'orderBy': Optional[List['_CountryOrdering']],
	'filter': Optional['_CountryFilter'],
})


CountryQueryResult = ClassVar[Optional[List['Country']]]


TimezoneParams = TypedDict('TimezoneParams', {
	'_id': Optional[str],
	'name': Optional[str],
	'first': Optional[int],
	'offset': Optional[int],
	'orderBy': Optional[List['_TimezoneOrdering']],
	'filter': Optional['_TimezoneFilter'],
})


TimezoneQueryResult = ClassVar[Optional[List['Timezone']]]


SubregionParams = TypedDict('SubregionParams', {
	'_id': Optional[str],
	'name': Optional[str],
	'first': Optional[int],
	'offset': Optional[int],
	'orderBy': Optional[List['_SubregionOrdering']],
	'filter': Optional['_SubregionFilter'],
})


SubregionQueryResult = ClassVar[Optional[List['Subregion']]]


RegionParams = TypedDict('RegionParams', {
	'_id': Optional[str],
	'name': Optional[str],
	'first': Optional[int],
	'offset': Optional[int],
	'orderBy': Optional[List['_RegionOrdering']],
	'filter': Optional['_RegionFilter'],
})


RegionQueryResult = ClassVar[Optional[List['Region']]]


LanguageParams = TypedDict('LanguageParams', {
	'_id': Optional[str],
	'iso639_1': Optional[str],
	'iso639_2': Optional[str],
	'name': Optional[str],
	'nativeName': Optional[str],
	'first': Optional[int],
	'offset': Optional[int],
	'orderBy': Optional[List['_LanguageOrdering']],
	'filter': Optional['_LanguageFilter'],
})


LanguageQueryResult = ClassVar[Optional[List['Language']]]


CurrencyParams = TypedDict('CurrencyParams', {
	'_id': Optional[str],
	'code': Optional[str],
	'name': Optional[str],
	'symbol': Optional[str],
	'first': Optional[int],
	'offset': Optional[int],
	'orderBy': Optional[List['_CurrencyOrdering']],
	'filter': Optional['_CurrencyFilter'],
})


CurrencyQueryResult = ClassVar[Optional[List['Currency']]]


RegionalBlocParams = TypedDict('RegionalBlocParams', {
	'_id': Optional[str],
	'acronym': Optional[str],
	'name': Optional[str],
	'first': Optional[int],
	'offset': Optional[int],
	'orderBy': Optional[List['_RegionalBlocOrdering']],
	'filter': Optional['_RegionalBlocFilter'],
})


RegionalBlocQueryResult = ClassVar[Optional[List['RegionalBloc']]]


TranslationParams = TypedDict('TranslationParams', {
	'_id': Optional[str],
	'languageCode': Optional[str],
	'value': Optional[str],
	'first': Optional[int],
	'offset': Optional[int],
	'orderBy': Optional[List['_TranslationOrdering']],
	'filter': Optional['_TranslationFilter'],
})


TranslationQueryResult = ClassVar[Optional[List['Translation']]]


FlagParams = TypedDict('FlagParams', {
	'_id': Optional[str],
	'emoji': Optional[str],
	'emojiUnicode': Optional[str],
	'svgFile': Optional[str],
	'first': Optional[int],
	'offset': Optional[int],
	'orderBy': Optional[List['_FlagOrdering']],
	'filter': Optional['_FlagFilter'],
})


FlagQueryResult = ClassVar[Optional[List['Flag']]]


DistanceToOtherCountryParams = TypedDict('DistanceToOtherCountryParams', {
	'distanceInKm': Optional[float],
	'countryName': Optional[str],
	'_id': Optional[str],
	'first': Optional[int],
	'offset': Optional[int],
	'orderBy': Optional[List['_DistanceToOtherCountryOrdering']],
	'filter': Optional['_DistanceToOtherCountryFilter'],
})


DistanceToOtherCountryQueryResult = ClassVar[Optional[List['DistanceToOtherCountry']]]


TopLevelDomainParams = TypedDict('TopLevelDomainParams', {
	'_id': Optional[str],
	'name': Optional[str],
	'first': Optional[int],
	'offset': Optional[int],
	'orderBy': Optional[List['_TopLevelDomainOrdering']],
	'filter': Optional['_TopLevelDomainFilter'],
})


TopLevelDomainQueryResult = ClassVar[Optional[List['TopLevelDomain']]]


CallingCodeParams = TypedDict('CallingCodeParams', {
	'_id': Optional[str],
	'name': Optional[str],
	'first': Optional[int],
	'offset': Optional[int],
	'orderBy': Optional[List['_CallingCodeOrdering']],
	'filter': Optional['_CallingCodeFilter'],
})


CallingCodeQueryResult = ClassVar[Optional[List['CallingCode']]]


Region = TypedDict('Region', {
	'_id': Optional[str],
	'name': str,
	'subregions': Optional[List['Subregion']],
})


RegionalBloc = TypedDict('RegionalBloc', {
	'_id': Optional[str],
	'acronym': str,
	'name': str,
	'otherAcronyms': Optional[List['OtherAcronym']],
	'otherNames': Optional[List['OtherName']],
	'countries': Optional[List['Country']],
})


Subregion = TypedDict('Subregion', {
	'_id': Optional[str],
	'name': str,
	'region': Optional['Region'],
	'countries': Optional[List['Country']],
})


Timezone = TypedDict('Timezone', {
	'_id': Optional[str],
	'name': str,
	'countries': Optional[List['Country']],
})


TopLevelDomain = TypedDict('TopLevelDomain', {
	'_id': Optional[str],
	'name': str,
	'countries': Optional[List['Country']],
})


Translation = TypedDict('Translation', {
	'_id': Optional[str],
	'languageCode': str,
	'value': str,
})


_CallingCodeFilter = TypedDict('_CallingCodeFilter', {
	'AND': Optional[List['_CallingCodeFilter']],
	'OR': Optional[List['_CallingCodeFilter']],
	'name': Optional[str],
	'name_not': Optional[str],
	'name_in': Optional[List[str]],
	'name_not_in': Optional[List[str]],
	'name_contains': Optional[str],
	'name_not_contains': Optional[str],
	'name_starts_with': Optional[str],
	'name_not_starts_with': Optional[str],
	'name_ends_with': Optional[str],
	'name_not_ends_with': Optional[str],
	'countries': Optional['_CountryFilter'],
	'countries_not': Optional['_CountryFilter'],
	'countries_in': Optional[List['_CountryFilter']],
	'countries_not_in': Optional[List['_CountryFilter']],
	'countries_some': Optional['_CountryFilter'],
	'countries_none': Optional['_CountryFilter'],
	'countries_single': Optional['_CountryFilter'],
	'countries_every': Optional['_CountryFilter'],
})


_CountryFilter = TypedDict('_CountryFilter', {
	'AND': Optional[List['_CountryFilter']],
	'OR': Optional[List['_CountryFilter']],
	'alpha2Code': Optional[str],
	'alpha2Code_not': Optional[str],
	'alpha2Code_in': Optional[List[str]],
	'alpha2Code_not_in': Optional[List[str]],
	'alpha2Code_contains': Optional[str],
	'alpha2Code_not_contains': Optional[str],
	'alpha2Code_starts_with': Optional[str],
	'alpha2Code_not_starts_with': Optional[str],
	'alpha2Code_ends_with': Optional[str],
	'alpha2Code_not_ends_with': Optional[str],
	'alpha3Code': Optional[str],
	'alpha3Code_not': Optional[str],
	'alpha3Code_in': Optional[List[str]],
	'alpha3Code_not_in': Optional[List[str]],
	'alpha3Code_contains': Optional[str],
	'alpha3Code_not_contains': Optional[str],
	'alpha3Code_starts_with': Optional[str],
	'alpha3Code_not_starts_with': Optional[str],
	'alpha3Code_ends_with': Optional[str],
	'alpha3Code_not_ends_with': Optional[str],
	'area': Optional[float],
	'area_not': Optional[float],
	'area_in': Optional[List[float]],
	'area_not_in': Optional[List[float]],
	'area_lt': Optional[float],
	'area_lte': Optional[float],
	'area_gt': Optional[float],
	'area_gte': Optional[float],
	'capital': Optional[str],
	'capital_not': Optional[str],
	'capital_in': Optional[List[str]],
	'capital_not_in': Optional[List[str]],
	'capital_contains': Optional[str],
	'capital_not_contains': Optional[str],
	'capital_starts_with': Optional[str],
	'capital_not_starts_with': Optional[str],
	'capital_ends_with': Optional[str],
	'capital_not_ends_with': Optional[str],
	'demonym': Optional[str],
	'demonym_not': Optional[str],
	'demonym_in': Optional[List[str]],
	'demonym_not_in': Optional[List[str]],
	'demonym_contains': Optional[str],
	'demonym_not_contains': Optional[str],
	'demonym_starts_with': Optional[str],
	'demonym_not_starts_with': Optional[str],
	'demonym_ends_with': Optional[str],
	'demonym_not_ends_with': Optional[str],
	'gini': Optional[float],
	'gini_not': Optional[float],
	'gini_in': Optional[List[float]],
	'gini_not_in': Optional[List[float]],
	'gini_lt': Optional[float],
	'gini_lte': Optional[float],
	'gini_gt': Optional[float],
	'gini_gte': Optional[float],
	'location': Optional['_Neo4jPointInput'],
	'location_not': Optional['_Neo4jPointInput'],
	'location_distance': Optional['_Neo4jPointDistanceFilter'],
	'location_distance_lt': Optional['_Neo4jPointDistanceFilter'],
	'location_distance_lte': Optional['_Neo4jPointDistanceFilter'],
	'location_distance_gt': Optional['_Neo4jPointDistanceFilter'],
	'location_distance_gte': Optional['_Neo4jPointDistanceFilter'],
	'name': Optional[str],
	'name_not': Optional[str],
	'name_in': Optional[List[str]],
	'name_not_in': Optional[List[str]],
	'name_contains': Optional[str],
	'name_not_contains': Optional[str],
	'name_starts_with': Optional[str],
	'name_not_starts_with': Optional[str],
	'name_ends_with': Optional[str],
	'name_not_ends_with': Optional[str],
	'nameTranslations': Optional['_TranslationFilter'],
	'nameTranslations_not': Optional['_TranslationFilter'],
	'nameTranslations_in': Optional[List['_TranslationFilter']],
	'nameTranslations_not_in': Optional[List['_TranslationFilter']],
	'nameTranslations_some': Optional['_TranslationFilter'],
	'nameTranslations_none': Optional['_TranslationFilter'],
	'nameTranslations_single': Optional['_TranslationFilter'],
	'nameTranslations_every': Optional['_TranslationFilter'],
	'nativeName': Optional[str],
	'nativeName_not': Optional[str],
	'nativeName_in': Optional[List[str]],
	'nativeName_not_in': Optional[List[str]],
	'nativeName_contains': Optional[str],
	'nativeName_not_contains': Optional[str],
	'nativeName_starts_with': Optional[str],
	'nativeName_not_starts_with': Optional[str],
	'nativeName_ends_with': Optional[str],
	'nativeName_not_ends_with': Optional[str],
	'numericCode': Optional[str],
	'numericCode_not': Optional[str],
	'numericCode_in': Optional[List[str]],
	'numericCode_not_in': Optional[List[str]],
	'numericCode_contains': Optional[str],
	'numericCode_not_contains': Optional[str],
	'numericCode_starts_with': Optional[str],
	'numericCode_not_starts_with': Optional[str],
	'numericCode_ends_with': Optional[str],
	'numericCode_not_ends_with': Optional[str],
	'population': Optional[float],
	'population_not': Optional[float],
	'population_in': Optional[List[float]],
	'population_not_in': Optional[List[float]],
	'population_lt': Optional[float],
	'population_lte': Optional[float],
	'population_gt': Optional[float],
	'population_gte': Optional[float],
	'topLevelDomains': Optional['_TopLevelDomainFilter'],
	'topLevelDomains_not': Optional['_TopLevelDomainFilter'],
	'topLevelDomains_in': Optional[List['_TopLevelDomainFilter']],
	'topLevelDomains_not_in': Optional[List['_TopLevelDomainFilter']],
	'topLevelDomains_some': Optional['_TopLevelDomainFilter'],
	'topLevelDomains_none': Optional['_TopLevelDomainFilter'],
	'topLevelDomains_single': Optional['_TopLevelDomainFilter'],
	'topLevelDomains_every': Optional['_TopLevelDomainFilter'],
	'callingCodes': Optional['_CallingCodeFilter'],
	'callingCodes_not': Optional['_CallingCodeFilter'],
	'callingCodes_in': Optional[List['_CallingCodeFilter']],
	'callingCodes_not_in': Optional[List['_CallingCodeFilter']],
	'callingCodes_some': Optional['_CallingCodeFilter'],
	'callingCodes_none': Optional['_CallingCodeFilter'],
	'callingCodes_single': Optional['_CallingCodeFilter'],
	'callingCodes_every': Optional['_CallingCodeFilter'],
	'timezones': Optional['_TimezoneFilter'],
	'timezones_not': Optional['_TimezoneFilter'],
	'timezones_in': Optional[List['_TimezoneFilter']],
	'timezones_not_in': Optional[List['_TimezoneFilter']],
	'timezones_some': Optional['_TimezoneFilter'],
	'timezones_none': Optional['_TimezoneFilter'],
	'timezones_single': Optional['_TimezoneFilter'],
	'timezones_every': Optional['_TimezoneFilter'],
	'borders': Optional['_CountryFilter'],
	'borders_not': Optional['_CountryFilter'],
	'borders_in': Optional[List['_CountryFilter']],
	'borders_not_in': Optional[List['_CountryFilter']],
	'borders_some': Optional['_CountryFilter'],
	'borders_none': Optional['_CountryFilter'],
	'borders_single': Optional['_CountryFilter'],
	'borders_every': Optional['_CountryFilter'],
	'subregion': Optional['_SubregionFilter'],
	'subregion_not': Optional['_SubregionFilter'],
	'subregion_in': Optional[List['_SubregionFilter']],
	'subregion_not_in': Optional[List['_SubregionFilter']],
	'officialLanguages': Optional['_LanguageFilter'],
	'officialLanguages_not': Optional['_LanguageFilter'],
	'officialLanguages_in': Optional[List['_LanguageFilter']],
	'officialLanguages_not_in': Optional[List['_LanguageFilter']],
	'officialLanguages_some': Optional['_LanguageFilter'],
	'officialLanguages_none': Optional['_LanguageFilter'],
	'officialLanguages_single': Optional['_LanguageFilter'],
	'officialLanguages_every': Optional['_LanguageFilter'],
	'currencies': Optional['_CurrencyFilter'],
	'currencies_not': Optional['_CurrencyFilter'],
	'currencies_in': Optional[List['_CurrencyFilter']],
	'currencies_not_in': Optional[List['_CurrencyFilter']],
	'currencies_some': Optional['_CurrencyFilter'],
	'currencies_none': Optional['_CurrencyFilter'],
	'currencies_single': Optional['_CurrencyFilter'],
	'currencies_every': Optional['_CurrencyFilter'],
	'regionalBlocs': Optional['_RegionalBlocFilter'],
	'regionalBlocs_not': Optional['_RegionalBlocFilter'],
	'regionalBlocs_in': Optional[List['_RegionalBlocFilter']],
	'regionalBlocs_not_in': Optional[List['_RegionalBlocFilter']],
	'regionalBlocs_some': Optional['_RegionalBlocFilter'],
	'regionalBlocs_none': Optional['_RegionalBlocFilter'],
	'regionalBlocs_single': Optional['_RegionalBlocFilter'],
	'regionalBlocs_every': Optional['_RegionalBlocFilter'],
	'flag': Optional['_FlagFilter'],
	'flag_not': Optional['_FlagFilter'],
	'flag_in': Optional[List['_FlagFilter']],
	'flag_not_in': Optional[List['_FlagFilter']],
	'distanceToOtherCountries': Optional['_DistanceToOtherCountryFilter'],
	'distanceToOtherCountries_not': Optional['_DistanceToOtherCountryFilter'],
	'distanceToOtherCountries_in': Optional[List['_DistanceToOtherCountryFilter']],
	'distanceToOtherCountries_not_in': Optional[List['_DistanceToOtherCountryFilter']],
	'distanceToOtherCountries_some': Optional['_DistanceToOtherCountryFilter'],
	'distanceToOtherCountries_none': Optional['_DistanceToOtherCountryFilter'],
	'distanceToOtherCountries_single': Optional['_DistanceToOtherCountryFilter'],
	'distanceToOtherCountries_every': Optional['_DistanceToOtherCountryFilter'],
	'shortestPathToOtherCountry': Optional['_CountryFilter'],
	'shortestPathToOtherCountry_not': Optional['_CountryFilter'],
	'shortestPathToOtherCountry_in': Optional[List['_CountryFilter']],
	'shortestPathToOtherCountry_not_in': Optional[List['_CountryFilter']],
	'shortestPathToOtherCountry_some': Optional['_CountryFilter'],
	'shortestPathToOtherCountry_none': Optional['_CountryFilter'],
	'shortestPathToOtherCountry_single': Optional['_CountryFilter'],
	'shortestPathToOtherCountry_every': Optional['_CountryFilter'],
})


_CurrencyFilter = TypedDict('_CurrencyFilter', {
	'AND': Optional[List['_CurrencyFilter']],
	'OR': Optional[List['_CurrencyFilter']],
	'code': Optional[str],
	'code_not': Optional[str],
	'code_in': Optional[List[str]],
	'code_not_in': Optional[List[str]],
	'code_contains': Optional[str],
	'code_not_contains': Optional[str],
	'code_starts_with': Optional[str],
	'code_not_starts_with': Optional[str],
	'code_ends_with': Optional[str],
	'code_not_ends_with': Optional[str],
	'name': Optional[str],
	'name_not': Optional[str],
	'name_in': Optional[List[str]],
	'name_not_in': Optional[List[str]],
	'name_contains': Optional[str],
	'name_not_contains': Optional[str],
	'name_starts_with': Optional[str],
	'name_not_starts_with': Optional[str],
	'name_ends_with': Optional[str],
	'name_not_ends_with': Optional[str],
	'symbol': Optional[str],
	'symbol_not': Optional[str],
	'symbol_in': Optional[List[str]],
	'symbol_not_in': Optional[List[str]],
	'symbol_contains': Optional[str],
	'symbol_not_contains': Optional[str],
	'symbol_starts_with': Optional[str],
	'symbol_not_starts_with': Optional[str],
	'symbol_ends_with': Optional[str],
	'symbol_not_ends_with': Optional[str],
	'countries': Optional['_CountryFilter'],
	'countries_not': Optional['_CountryFilter'],
	'countries_in': Optional[List['_CountryFilter']],
	'countries_not_in': Optional[List['_CountryFilter']],
	'countries_some': Optional['_CountryFilter'],
	'countries_none': Optional['_CountryFilter'],
	'countries_single': Optional['_CountryFilter'],
	'countries_every': Optional['_CountryFilter'],
})


_DistanceToOtherCountryFilter = TypedDict('_DistanceToOtherCountryFilter', {
	'AND': Optional[List['_DistanceToOtherCountryFilter']],
	'OR': Optional[List['_DistanceToOtherCountryFilter']],
	'distanceInKm': Optional[float],
	'distanceInKm_not': Optional[float],
	'distanceInKm_in': Optional[List[float]],
	'distanceInKm_not_in': Optional[List[float]],
	'distanceInKm_lt': Optional[float],
	'distanceInKm_lte': Optional[float],
	'distanceInKm_gt': Optional[float],
	'distanceInKm_gte': Optional[float],
	'countryName': Optional[str],
	'countryName_not': Optional[str],
	'countryName_in': Optional[List[str]],
	'countryName_not_in': Optional[List[str]],
	'countryName_contains': Optional[str],
	'countryName_not_contains': Optional[str],
	'countryName_starts_with': Optional[str],
	'countryName_not_starts_with': Optional[str],
	'countryName_ends_with': Optional[str],
	'countryName_not_ends_with': Optional[str],
})


_FlagFilter = TypedDict('_FlagFilter', {
	'AND': Optional[List['_FlagFilter']],
	'OR': Optional[List['_FlagFilter']],
	'emoji': Optional[str],
	'emoji_not': Optional[str],
	'emoji_in': Optional[List[str]],
	'emoji_not_in': Optional[List[str]],
	'emoji_contains': Optional[str],
	'emoji_not_contains': Optional[str],
	'emoji_starts_with': Optional[str],
	'emoji_not_starts_with': Optional[str],
	'emoji_ends_with': Optional[str],
	'emoji_not_ends_with': Optional[str],
	'emojiUnicode': Optional[str],
	'emojiUnicode_not': Optional[str],
	'emojiUnicode_in': Optional[List[str]],
	'emojiUnicode_not_in': Optional[List[str]],
	'emojiUnicode_contains': Optional[str],
	'emojiUnicode_not_contains': Optional[str],
	'emojiUnicode_starts_with': Optional[str],
	'emojiUnicode_not_starts_with': Optional[str],
	'emojiUnicode_ends_with': Optional[str],
	'emojiUnicode_not_ends_with': Optional[str],
	'svgFile': Optional[str],
	'svgFile_not': Optional[str],
	'svgFile_in': Optional[List[str]],
	'svgFile_not_in': Optional[List[str]],
	'svgFile_contains': Optional[str],
	'svgFile_not_contains': Optional[str],
	'svgFile_starts_with': Optional[str],
	'svgFile_not_starts_with': Optional[str],
	'svgFile_ends_with': Optional[str],
	'svgFile_not_ends_with': Optional[str],
	'country': Optional['_CountryFilter'],
	'country_not': Optional['_CountryFilter'],
	'country_in': Optional[List['_CountryFilter']],
	'country_not_in': Optional[List['_CountryFilter']],
})


_LanguageFilter = TypedDict('_LanguageFilter', {
	'AND': Optional[List['_LanguageFilter']],
	'OR': Optional[List['_LanguageFilter']],
	'iso639_1': Optional[str],
	'iso639_1_not': Optional[str],
	'iso639_1_in': Optional[List[str]],
	'iso639_1_not_in': Optional[List[str]],
	'iso639_1_contains': Optional[str],
	'iso639_1_not_contains': Optional[str],
	'iso639_1_starts_with': Optional[str],
	'iso639_1_not_starts_with': Optional[str],
	'iso639_1_ends_with': Optional[str],
	'iso639_1_not_ends_with': Optional[str],
	'iso639_2': Optional[str],
	'iso639_2_not': Optional[str],
	'iso639_2_in': Optional[List[str]],
	'iso639_2_not_in': Optional[List[str]],
	'iso639_2_contains': Optional[str],
	'iso639_2_not_contains': Optional[str],
	'iso639_2_starts_with': Optional[str],
	'iso639_2_not_starts_with': Optional[str],
	'iso639_2_ends_with': Optional[str],
	'iso639_2_not_ends_with': Optional[str],
	'name': Optional[str],
	'name_not': Optional[str],
	'name_in': Optional[List[str]],
	'name_not_in': Optional[List[str]],
	'name_contains': Optional[str],
	'name_not_contains': Optional[str],
	'name_starts_with': Optional[str],
	'name_not_starts_with': Optional[str],
	'name_ends_with': Optional[str],
	'name_not_ends_with': Optional[str],
	'nativeName': Optional[str],
	'nativeName_not': Optional[str],
	'nativeName_in': Optional[List[str]],
	'nativeName_not_in': Optional[List[str]],
	'nativeName_contains': Optional[str],
	'nativeName_not_contains': Optional[str],
	'nativeName_starts_with': Optional[str],
	'nativeName_not_starts_with': Optional[str],
	'nativeName_ends_with': Optional[str],
	'nativeName_not_ends_with': Optional[str],
	'countries': Optional['_CountryFilter'],
	'countries_not': Optional['_CountryFilter'],
	'countries_in': Optional[List['_CountryFilter']],
	'countries_not_in': Optional[List['_CountryFilter']],
	'countries_some': Optional['_CountryFilter'],
	'countries_none': Optional['_CountryFilter'],
	'countries_single': Optional['_CountryFilter'],
	'countries_every': Optional['_CountryFilter'],
})


_Neo4jDateInput = TypedDict('_Neo4jDateInput', {
	'year': Optional[int],
	'month': Optional[int],
	'day': Optional[int],
	'formatted': Optional[str],
})


_Neo4jDateTimeInput = TypedDict('_Neo4jDateTimeInput', {
	'year': Optional[int],
	'month': Optional[int],
	'day': Optional[int],
	'hour': Optional[int],
	'minute': Optional[int],
	'second': Optional[int],
	'millisecond': Optional[int],
	'microsecond': Optional[int],
	'nanosecond': Optional[int],
	'timezone': Optional[str],
	'formatted': Optional[str],
})


_Neo4jLocalDateTimeInput = TypedDict('_Neo4jLocalDateTimeInput', {
	'year': Optional[int],
	'month': Optional[int],
	'day': Optional[int],
	'hour': Optional[int],
	'minute': Optional[int],
	'second': Optional[int],
	'millisecond': Optional[int],
	'microsecond': Optional[int],
	'nanosecond': Optional[int],
	'formatted': Optional[str],
})


_Neo4jLocalTimeInput = TypedDict('_Neo4jLocalTimeInput', {
	'hour': Optional[int],
	'minute': Optional[int],
	'second': Optional[int],
	'millisecond': Optional[int],
	'microsecond': Optional[int],
	'nanosecond': Optional[int],
	'formatted': Optional[str],
})


_Neo4jPointDistanceFilter = TypedDict('_Neo4jPointDistanceFilter', {
	'point': '_Neo4jPointInput',
	'distance': float,
})


_Neo4jPointInput = TypedDict('_Neo4jPointInput', {
	'x': Optional[float],
	'y': Optional[float],
	'z': Optional[float],
	'longitude': Optional[float],
	'latitude': Optional[float],
	'height': Optional[float],
	'crs': Optional[str],
	'srid': Optional[int],
})


_Neo4jTimeInput = TypedDict('_Neo4jTimeInput', {
	'hour': Optional[int],
	'minute': Optional[int],
	'second': Optional[int],
	'millisecond': Optional[int],
	'microsecond': Optional[int],
	'nanosecond': Optional[int],
	'timezone': Optional[str],
	'formatted': Optional[str],
})


_RegionalBlocFilter = TypedDict('_RegionalBlocFilter', {
	'AND': Optional[List['_RegionalBlocFilter']],
	'OR': Optional[List['_RegionalBlocFilter']],
	'acronym': Optional[str],
	'acronym_not': Optional[str],
	'acronym_in': Optional[List[str]],
	'acronym_not_in': Optional[List[str]],
	'acronym_contains': Optional[str],
	'acronym_not_contains': Optional[str],
	'acronym_starts_with': Optional[str],
	'acronym_not_starts_with': Optional[str],
	'acronym_ends_with': Optional[str],
	'acronym_not_ends_with': Optional[str],
	'name': Optional[str],
	'name_not': Optional[str],
	'name_in': Optional[List[str]],
	'name_not_in': Optional[List[str]],
	'name_contains': Optional[str],
	'name_not_contains': Optional[str],
	'name_starts_with': Optional[str],
	'name_not_starts_with': Optional[str],
	'name_ends_with': Optional[str],
	'name_not_ends_with': Optional[str],
	'countries': Optional['_CountryFilter'],
	'countries_not': Optional['_CountryFilter'],
	'countries_in': Optional[List['_CountryFilter']],
	'countries_not_in': Optional[List['_CountryFilter']],
	'countries_some': Optional['_CountryFilter'],
	'countries_none': Optional['_CountryFilter'],
	'countries_single': Optional['_CountryFilter'],
	'countries_every': Optional['_CountryFilter'],
})


_RegionFilter = TypedDict('_RegionFilter', {
	'AND': Optional[List['_RegionFilter']],
	'OR': Optional[List['_RegionFilter']],
	'name': Optional[str],
	'name_not': Optional[str],
	'name_in': Optional[List[str]],
	'name_not_in': Optional[List[str]],
	'name_contains': Optional[str],
	'name_not_contains': Optional[str],
	'name_starts_with': Optional[str],
	'name_not_starts_with': Optional[str],
	'name_ends_with': Optional[str],
	'name_not_ends_with': Optional[str],
	'subregions': Optional['_SubregionFilter'],
	'subregions_not': Optional['_SubregionFilter'],
	'subregions_in': Optional[List['_SubregionFilter']],
	'subregions_not_in': Optional[List['_SubregionFilter']],
	'subregions_some': Optional['_SubregionFilter'],
	'subregions_none': Optional['_SubregionFilter'],
	'subregions_single': Optional['_SubregionFilter'],
	'subregions_every': Optional['_SubregionFilter'],
})


_SubregionFilter = TypedDict('_SubregionFilter', {
	'AND': Optional[List['_SubregionFilter']],
	'OR': Optional[List['_SubregionFilter']],
	'name': Optional[str],
	'name_not': Optional[str],
	'name_in': Optional[List[str]],
	'name_not_in': Optional[List[str]],
	'name_contains': Optional[str],
	'name_not_contains': Optional[str],
	'name_starts_with': Optional[str],
	'name_not_starts_with': Optional[str],
	'name_ends_with': Optional[str],
	'name_not_ends_with': Optional[str],
	'region': Optional['_RegionFilter'],
	'region_not': Optional['_RegionFilter'],
	'region_in': Optional[List['_RegionFilter']],
	'region_not_in': Optional[List['_RegionFilter']],
	'countries': Optional['_CountryFilter'],
	'countries_not': Optional['_CountryFilter'],
	'countries_in': Optional[List['_CountryFilter']],
	'countries_not_in': Optional[List['_CountryFilter']],
	'countries_some': Optional['_CountryFilter'],
	'countries_none': Optional['_CountryFilter'],
	'countries_single': Optional['_CountryFilter'],
	'countries_every': Optional['_CountryFilter'],
})


_TimezoneFilter = TypedDict('_TimezoneFilter', {
	'AND': Optional[List['_TimezoneFilter']],
	'OR': Optional[List['_TimezoneFilter']],
	'name': Optional[str],
	'name_not': Optional[str],
	'name_in': Optional[List[str]],
	'name_not_in': Optional[List[str]],
	'name_contains': Optional[str],
	'name_not_contains': Optional[str],
	'name_starts_with': Optional[str],
	'name_not_starts_with': Optional[str],
	'name_ends_with': Optional[str],
	'name_not_ends_with': Optional[str],
	'countries': Optional['_CountryFilter'],
	'countries_not': Optional['_CountryFilter'],
	'countries_in': Optional[List['_CountryFilter']],
	'countries_not_in': Optional[List['_CountryFilter']],
	'countries_some': Optional['_CountryFilter'],
	'countries_none': Optional['_CountryFilter'],
	'countries_single': Optional['_CountryFilter'],
	'countries_every': Optional['_CountryFilter'],
})


_TopLevelDomainFilter = TypedDict('_TopLevelDomainFilter', {
	'AND': Optional[List['_TopLevelDomainFilter']],
	'OR': Optional[List['_TopLevelDomainFilter']],
	'name': Optional[str],
	'name_not': Optional[str],
	'name_in': Optional[List[str]],
	'name_not_in': Optional[List[str]],
	'name_contains': Optional[str],
	'name_not_contains': Optional[str],
	'name_starts_with': Optional[str],
	'name_not_starts_with': Optional[str],
	'name_ends_with': Optional[str],
	'name_not_ends_with': Optional[str],
	'countries': Optional['_CountryFilter'],
	'countries_not': Optional['_CountryFilter'],
	'countries_in': Optional[List['_CountryFilter']],
	'countries_not_in': Optional[List['_CountryFilter']],
	'countries_some': Optional['_CountryFilter'],
	'countries_none': Optional['_CountryFilter'],
	'countries_single': Optional['_CountryFilter'],
	'countries_every': Optional['_CountryFilter'],
})


_TranslationFilter = TypedDict('_TranslationFilter', {
	'AND': Optional[List['_TranslationFilter']],
	'OR': Optional[List['_TranslationFilter']],
	'languageCode': Optional[str],
	'languageCode_not': Optional[str],
	'languageCode_in': Optional[List[str]],
	'languageCode_not_in': Optional[List[str]],
	'languageCode_contains': Optional[str],
	'languageCode_not_contains': Optional[str],
	'languageCode_starts_with': Optional[str],
	'languageCode_not_starts_with': Optional[str],
	'languageCode_ends_with': Optional[str],
	'languageCode_not_ends_with': Optional[str],
	'value': Optional[str],
	'value_not': Optional[str],
	'value_in': Optional[List[str]],
	'value_not_in': Optional[List[str]],
	'value_contains': Optional[str],
	'value_not_contains': Optional[str],
	'value_starts_with': Optional[str],
	'value_not_starts_with': Optional[str],
	'value_ends_with': Optional[str],
	'value_not_ends_with': Optional[str],
})


