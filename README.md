<img align="right" width="200" height="auto" src="https://github.com/gchq/Gaffer/raw/develop/logos/logo.png">

# Gaffer Python Client

![ci](https://github.com/gchq/gafferpy/actions/workflows/continuous-integration.yaml/badge.svg)
[<img src="https://img.shields.io/badge/docs-passing-success.svg?logo=readthedocs">](https://gchq.github.io/gafferpy/)

## Features

- Persistently connect to a Gaffer rest api to run operations
- Connect using PKI certificates and SSL
- Generate Python client code for custom Operations, Predicates, Binary Operators and Functions
- Turn existing json queries into Python objects

## Installation

`gafferpy` requires Python 3.6+. We do not currently release `gafferpy` on PyPI, but you can install it over ssh with:

```bash
pip install git+https://github.com/gchq/gafferpy.git
```

Or if you have the source code locally and want any changes you make reflected in your installation, you can run:

```bash
pip install -e .
```

## Quick Start

The Python shell connects to a running Gaffer REST API.
You can start the Gaffer [`road-traffic-demo`](https://github.com/gchq/Gaffer/blob/master/example/road-traffic/README.md) REST server from the Gaffer repository, using the command:

```bash
mvn clean install -pl :road-traffic-demo -Proad-traffic-demo,quick
```
To connect to the running Gaffer API from Python (more information on the Python shell can be found [here](https://gchq.github.io/gaffer-doc/latest/user-guide/apis/python-api/)):
```python
# Import the client library and connector
from gafferpy import gaffer as g
from gafferpy import gaffer_connector

# Instantiate a connector
gc = gaffer_connector.GafferConnector("http://localhost:8080/rest/latest")
```
Then perform requests against it:
```python
# You can use the connector to perform GET requests
schema = gc.execute_get(g.GetSchema())

# And also run operations
elements = gc.execute_operation(
    operation=g.GetAllElements()
)

# Multiple operations
elements = gc.execute_operations(
    operations=[
        g.GetAllElements(),
        g.Limit(result_limit=3)
    ]
)

# And operation chains
elements = gc.execute_operation_chain(
    operation_chain=g.OperationChain(
        operations=[
            g.GetAllElements(),
            g.Limit(
                truncate=True,
                result_limit=3
            )
        ]
    )
)
```

See [Operations Guide](https://gchq.github.io/gaffer-doc/latest/reference/operations-guide/operations) for more examples of operations in Python.

## Developer Guide

### Coding Style
Please ensure that your coding style is consistent with the rest of the Gaffer project. Guides on the coding style for `gafferpy` and Gaffer can be found [here](https://gchq.github.io/gaffer-doc/latest/development-guide/ways-of-working).

### Testing

The `gafferpy` tests are implemented using `tox` and `pytest`.
To run the tests, install the `gafferpy` 'dev' extra:
```bash
pip install -e ".[dev]" # the quotes ensure compatibilty with zsh
```
This will install extra development dependecies for running tests and building documentation.

`gafferpy` has both unit tests and integration tests - the integration tests use the Road Traffic Example to test the Python API. If this is not running, the integration tests are skipped. It is advisable that the integration tests are run prior to any code commits to ensure they do not fail due to any code changes.

*For help starting the Road Traffic Example, see the [Quick Start](#quick-start) section above.*

To run the tests, execute the below from the root directory of `gafferpy`:
```bash
tox
```
By default, `tox` will and try run the tests in multiple test envs (different Python versions) - if they do not exist then they are skipped.
To run the test for a specifc test env e.g. Python3.9, run:
```bash
tox -e py39
```

### Building the documentation

To build the docs locally, assuming you have Make and Python installed, and `gafferpy` installed with the 'dev' extra:
```bash
cd docs
make html
```

### Generating the Python API
`gafferpy` has the ability to regenerate the Python API based upon the Gaffer REST API that a `GafferConnector` object is pointing at - a more detailed description and examples of how to do this can be found [here](./src/fishbowl/README.md).

## License

Copyright 2016-2024 Crown Copyright

Licensed under the Apache License, Version 2.0 \(the "License"\); you may not use this file except in compliance with the License. You may obtain a copy of the License at

[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
