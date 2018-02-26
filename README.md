# jool
Feature generation for bug prediction

## Installation

```
pipenv --three
pipenv install
```

For private repositories, you will need to set up a private and public rsa key as environment variables as such:

```
export JOOL_PUBLIC_KEY="~/.ssh/id_rsa.pub"
export JOOL_PRIVATE_KEY="~/.ssh/id_rsa"
```

## Run tests

```
pipenv run tox
```
