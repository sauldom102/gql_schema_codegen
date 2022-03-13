from typing_extensions import Unpack
from graphql import GraphQLResolveInfo
from ..snapshots.test_schema import LoginParams, LoginMutationResult, MeQueryResult, SignUpParams, SignUpMutationResult, LogoutMutationResult, User, UserType
from ariadne import QueryType, MutationType


mocked_user: User = {
    'id': '1',
    'email': 'saulydominguez@gmail.com',
    'dob': '28/05/1999',
    'first_name': 'Saul',
    'last_name': 'Dominguez',
    'full_name': 'Saul Dominguez',
    'username': 'saulydominguez',
    'people': [],
    'type': UserType.ADMIN
}

query = QueryType()


@query.field('me')
def resolve_me(obj, info: GraphQLResolveInfo) -> MeQueryResult:
    # implementation to obtain current user
    return mocked_user


mutation = MutationType()


@mutation.field('login')
def resolve_login(_, info: GraphQLResolveInfo, **params: Unpack[LoginParams]) -> LoginMutationResult:
    _input = params['input']
    # you can use typed _input var down here

    # login implementation
    return mocked_user


@mutation.field('signUp')
def resolve_sign_up(_, info: GraphQLResolveInfo, **params: Unpack[SignUpParams]) -> SignUpMutationResult:
    # login implementation
    return mocked_user


@mutation.field('logout')
def resolve_logout(_, info: GraphQLResolveInfo) -> LogoutMutationResult:
    # logout implementation
    return True
