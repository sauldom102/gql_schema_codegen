<div align="center">
  <h1 align="center">gql_schema_codegen</h1>
  <h4 align="center">Easily generate Python typings from a GrapqhQL schema.</h4>
</div>

<div align="center">
  <a align="center" href="https://github.com/sauldom102?tab=followers">
    <img src="https://img.shields.io/github/followers/sauldom102?label=Follow%20%40sauldom102&style=social" />
  </a>
</div>

<br />

Let's go straight to the point, here you can see a very simple input schema content and its corresponding output:

<details>
<summary><b>Input GraphQL schema</b></summary>

```graphql
schema {
  query: Query
  mutation: Mutation
}

enum UserType {
  STAFF
  ADMIN
}

type User {
  id: ID!
  email: String
  username: String!
  first_name: String!
  last_name: String!
  full_name: String!
  dob: String @date(format: "%Y-%m-%d")
  type: UserType!
  people: [String]
}

type Query {
  me: User!
}

input SignUpInput {
  email: String!
  username: String!
  first_name: String!
  last_name: String!
  password: String!
}

input LoginInput {
  identifier: String!
  password: String!
}

type Mutation {
  login(input: LoginInput!): User!
  signUp(input: SignUpInput!): User!
  logout: Boolean
}
```
</details>

<details>
  <summary><b>Output Python typings</b></summary>

```python
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
```
</details>

There are some more complex examples available under [tests](tests) if you are curious about how accurate is this tool.

## Motivation

While I was trying out [Ariadne](https://ariadnegraphql.org/) (a library for implementing GraphQL servers using schema-first approach) and writing the resolvers for the queries and mutations that I defined in my GraphQL schema, I was missing the ability to define the types for the params and the return values.
I hope this library helps some devs to write better typed resolvers for their projects, while keeping the resolvers code synced with the schema definition.

<details>
  <summary><b>Ariadne example with typed resolvers</b></summary>
  
  ```python
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
```
</details>


## Installation

You can easily install it via pip:

```bash
$ pip install gql_schema_codegen
```

## Usage

Three use cases depending on where the GraphQL schema is defined:

### 1. Generate types from a single schema file

This is the simplest case, you have just a single file with all the types declared there.

```bash
$ python -m gql_schema_codegen -p ./schema.graphql -t ./schema_types.py
```

###  2. Generate types from a remote GraphQL server

You have deployed a GraphQL server with introspection enabled, you can just provide a link to that server and this tool will do its job.

```bash
$ python -m gql_schema_codegen -u https://gitlab.com/api/graphql -t ./schema_types.py
```

⚠️ For now, it only works with public schemas, without any authentication required. I will be adding support for this soon.

###  3. Generate types from different schema files in a directory

It's a common thing that you don't have your schema definition centralized in a single file but in multiple ones instead, if that's your case you can provide that directory path where all the graphql/gql files are located and this tool will find them and merge them into a single schema to process it later on.

```bash
$ python -m gql_schema_codegen -p ./dir_with_gql_types -t ./schema_types.py
```

If you just need more info about how to run it:

```bash
$ python -m gql_schema_codegen --help
usage: __main__.py [-h] [--schema-path SCHEMA_PATH] [--schema-url SCHEMA_URL] [--to-path TO_PATH] [--config-file CONFIG_FILE]

Generate python file with types from a GraphQL schema file.

optional arguments:
  -h, --help            show this help message and exit
  --schema-path SCHEMA_PATH, -p SCHEMA_PATH
                        path of the schema file (default: schema.graphql)
  --schema-url SCHEMA_URL, -u SCHEMA_URL
                        url of the schema
  --to-path TO_PATH, -t TO_PATH
                        wanted output file path (default: schema_types.py)
  --config-file CONFIG_FILE, -c CONFIG_FILE
                        path of the config file in yaml format (default: gql_schema_codegen.config.yml)
```


#### Custom scalars support

By default, scalars found in your schema will be generated as `Any`, if you already know the types for these scalars you can create a custom config file and define these types there:

```yaml
scalars:
  DateTime: str
  Time: str
  BigInt: int
  BoardID: int
  Duration: DesignFields
```

Notice how you can also set another type from your schema (or a Python class) as custom value for your scalar.

## Tests

They are simple snapshot tests, they work by comparing the output with the expected output, each test corresponds to a file stored under `tests/snapshots`.
You will find different tests declared in the `tests` directory.
If you want to run them you need to install the [`pytest-snapshot`](https://pypi.org/project/pytest-snapshot/) module first. Then, you can run them with:

```bash
$ pytest --snapshot-update
```

You can also run a specific test this way:

```bash
$ pytest --snapshot-update -k "test_pokeapi_schema_snapshot"
```

##  Contribution

Feel free to open some issues and/or pull requests if you want to participate in the development of this module, either just by proposing changes or by actively participating with code. At the moment of writing this, I have at least a couple of ideas planned to improve the way this generator works. ✨

## Support

If you like the work I do and want to support me, you can do it below:

<a href="https://www.buymeacoffee.com/sauldom102" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

##  License

MIT
