from enum import Enum
from typing import ClassVar, List, Optional, TypedDict


UserType = Enum('UserType', 'STAFF ADMIN')


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


Query = TypedDict('Query', {
	'me': 'MeQueryResult',
})


MeQueryResult = ClassVar['User']


Mutation = TypedDict('Mutation', {
	'login': 'LoginMutationResult',
	'signUp': 'SignUpMutationResult',
	'logout': 'LogoutMutationResult',
})


LoginParams = TypedDict('LoginParams', {
	'input': 'LoginInput',
})


LoginMutationResult = ClassVar['User']


SignUpParams = TypedDict('SignUpParams', {
	'input': 'SignUpInput',
})


SignUpMutationResult = ClassVar['User']


LogoutMutationResult = bool


SignUpInput = TypedDict('SignUpInput', {
	'email': str,
	'username': str,
	'first_name': str,
	'last_name': str,
	'password': str,
})


LoginInput = TypedDict('LoginInput', {
	'identifier': str,
	'password': str,
})


