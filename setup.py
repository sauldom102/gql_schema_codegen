from setuptools import setup, find_packages

packages = find_packages()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="gql_schema_codegen",
    packages=packages,
    version="1.0",
    author="Saul Dominguez",
    author_email="saulydominguez@gmail.com",
    description="A module to generate Python typings from a GrapqhQL schema",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sauldom102/gql_schema_codegen",
    py_modules=['gql_schema_codegen', ],
    install_requires=[
        'graphql-core==3.2.0',
        'graphqlclient==0.2.4',
        'argparse==1.4.0',
        'pytest-snapshot==0.8.1',
        'pytest==7.1.1'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
