# Fishbowl

## Features
Fishbowl generates code for the core `gafferpy` classes by pointing to a running Gaffer REST API.
It generates the classes for:

- [Operations](../gafferpy/generated_api/operations.py)
- [Predicates](../gafferpy/generated_api/predicates.py)
- [Functions](../gafferpy/generated_api/functions.py)
- [Binary Operators](../gafferpy/generated_api/binary_operators.py)
- [Config Endpoints](../gafferpy/generated_api/config.py)

This is done automatically on every Gaffer release from a standard spring-rest API and placed into `gafferpy`'s [generated_api](../gafferpy/generated_api) directory.

If you have custom Gaffer Java classes from the list above, `fishbowl` can generate the `gafferpy` classes for them.

## Quick Start

To regenerate the core `gafferpy` library from a spring-rest Gaffer API, first start the Gaffer API from the root directory of the Gaffer repository:
```bash
mvn spring-boot:run -pl :spring-rest -Pdemo
```
You can then use `fishbowl` to generate the Python API:
```python
from gafferpy.gaffer_connector import GafferConnector
from fishbowl.fishbowl import Fishbowl

gc = GafferConnector("http://localhost:8080/rest")
fb = Fishbowl(gaffer_connector=gc)
```
Your Python files will be appear in a folder called `generated`.

You can then use these classes in normal `gafferpy` operations:
```python
import generated
gc.execute(generated.operations.YourCustomOperation(custom_field=True))
gc.execute(generated.operations.OperationChain(
    operations=[
        generated.operations.GetAllElements(), 
        generated.operations.Count()
    ]
))
```