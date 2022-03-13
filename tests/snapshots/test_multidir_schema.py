from enum import Enum
from typing import ClassVar, List, Optional, TypedDict


UserType = Enum('UserType', 'STAFF ADMIN')


Mutation = TypedDict('Mutation', {
	'logout': 'LogoutMutationResult',
	'login': 'LoginMutationResult',
	'signUp': 'SignUpMutationResult',
})


LogoutMutationResult = bool


LoginParams = TypedDict('LoginParams', {
	'input': 'LoginInput',
})


LoginMutationResult = ClassVar['User']


SignUpParams = TypedDict('SignUpParams', {
	'input': 'SignUpInput',
})


SignUpMutationResult = ClassVar['User']


Query = TypedDict('Query', {
	'me': 'MeQueryResult',
})


MeQueryResult = ClassVar['User']


User = TypedDict('User', {
	'id': str,
	'email': Optional[str],
	'username': str,
	'first_name': str,
	'last_name': str,
	'full_name': str,
	'dob': Optional[str],
	'type': 'UserType',
	'people': Optional[List[str]],
})


LoginInput = TypedDict('LoginInput', {
	'identifier': str,
	'password': str,
})


SignUpInput = TypedDict('SignUpInput', {
	'email': str,
	'username': str,
	'first_name': str,
	'last_name': str,
	'password': str,
})


