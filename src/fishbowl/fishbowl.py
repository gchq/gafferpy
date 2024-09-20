#
# Copyright 2023-2024 Crown Copyright
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from pathlib import Path
import re
import shutil
from jinja2 import Environment, FileSystemLoader
from gafferpy.gaffer_connector import GafferConnector
from gafferpy.gaffer_core import JsonConverter
from gafferpy.gaffer_types import parse_java_type_to_string
from collections import defaultdict
from typing import Any, Callable, Dict, List, Set
from datetime import datetime


class Fishbowl:
    def __init__(
        self,
        gaffer_connector: GafferConnector,
        generated_directory_path: str = "generated"
    ):
        self._gaffer_connector = gaffer_connector
        self.generated_directory_path = generated_directory_path
        print("Generating Python API from REST service...")
        self._generate_library()
        print(
            "Successfully generated Python API! To import operations, predicates and "
            "functions, use the following command: "
            f"\n`from {str(generated_directory_path)} import *`"
        )

    def _write_to_file(self, file_path: Path, data: str) -> None:
        if data:
            file_path.unlink()  # removes file
            with open(file_path, "w+") as file:
                file.write(data)

    def _get_config_name(self, url: str) -> str:
        name = url.replace("/graph", "").replace("/config", "")
        # Remove parameter
        name = re.sub(r"\/\{.*\}", "", name)
        # Make CamelCase class name
        name = name.strip("/")
        name = "Get" + "".join([name[0].upper() + name[1:] for name in name.split("/")])
        return name

    def _get_function_dict(self) -> Dict[str, Callable]:
        return {
            "short_name": lambda n: n.rsplit(".", 1)[1].replace("$", ""),
            "snake_case": JsonConverter.to_snake_case,
            "get_fields": lambda f: self._gaffer_connector.get(
                f"/graph/config/serialisedFields/{f}", json_result=True
            ),
            "get_field_types": lambda f: self._gaffer_connector.get(
                f"/graph/config/serialisedFields/{f}/classes", json_result=True
            ),
            "config_name": self._get_config_name,
            "get_config_parameter": lambda n: re.sub(r".*\{", "", re.sub(r"\}.*", "", n)),
            "parse_java_type": parse_java_type_to_string
        }

    def _generate_library(self):
        parent_dir = Path(__file__).parent
        templates_dir = parent_dir / "templates"
        file_loader = FileSystemLoader(templates_dir)
        self.env = Environment(loader=file_loader)
        self.env.globals['copyright_years'] = f"2022-{datetime.now().year}"

        operations_python = self._generate_operations()
        functions_python = self._generate_transform_functions()
        predicates_python = self._generate_filter_functions()
        binary_operators_python = self._generate_aggregation_functions()
        config_python = self._generate_config()

        if not self.generated_directory_path.exists():
            self.generated_directory_path.mkdir()

        self._write_to_file(
            self.generated_directory_path / "functions.py",
            functions_python
        )
        self._write_to_file(
            self.generated_directory_path / "predicates.py",
            predicates_python
        )
        self._write_to_file(
            self.generated_directory_path / "binaryoperators.py",
            binary_operators_python
        )
        self._write_to_file(
            self.generated_directory_path / "config.py",
            config_python
        )
        self._write_to_file(
            self.generated_directory_path / "operations.py",
            operations_python
        )
        self._write_to_file(
            self.generated_directory_path / "__init__.py",
            "__all__ = [\"operations\", \"predicates\", \"functions\", "
            "\"binary_operators\", \"config\"]\n"
        )

    def _generate_transform_functions(self) -> str:
        return self._generate_functions(
            "transformFunctions",
            "AbstractFunction"
        )

    def _generate_filter_functions(self) -> str:
        return self._generate_functions(
            "filterFunctions",
            "AbstractPredicate"
        )

    def _generate_aggregation_functions(self) -> str:
        return self._generate_functions(
            "aggregationFunctions",
            "AbstractBinaryOperator"
        )

    def _generate_functions(
        self,
        path: str,
        base_class: str,
        base_class_import_path: str = "gafferpy.gaffer_core"
    ) -> str:
        # Older Gaffer versions may be missing some function endpoints
        try:
            functions = self._gaffer_connector.get(f"/graph/config/{path}", json_result=True)
        except ConnectionError:
            print(f"/graph/config/{path} not present, skipping")
            return ""

        functions = sorted(functions)
        manual_imports = {base_class_import_path: {base_class}}
        imports = self._generate_import_strings(functions, manual_imports)

        function_template = self.env.get_template("functions.py.j2")
        function_template.globals.update(self._get_function_dict())
        return function_template.render(
            functions=functions,
            import_path=base_class_import_path,
            base_class=base_class,
            imports=imports
        )

    def _generate_operations(self) -> str:
        # spring-rest has an endpoint for every store operation, even ones unsupported by the store
        # Check if this is supported: 2.0.0+, 1.23.0+
        try:
            operation_summaries = self._gaffer_connector.get(
                "/graph/operations/details/all", json_result=True)
        except ConnectionError:
            try:
                operation_summaries = self._gaffer_connector.get(
                    "/graph/operations/details", json_result=True)
            except ConnectionError:
                print(f"/graph/operations/details/ not present, skipping operations")
                return ""

        operation_summaries = sorted(operation_summaries, key=lambda op: op["name"])

        op_names = [op["name"] for op in operation_summaries]

        imports = self._generate_import_strings(op_names)

        template = self.env.get_template("operations.py.j2")
        template.globals.update(self._get_function_dict())
        return template.render(
            operations=operation_summaries,
            imports=imports
        )

    def _generate_config(self) -> str:
        # Gaffer 2 spring-rest uses openapi3 rather than swagger2
        try:
            api_summaries = self._gaffer_connector.get("/v3/api-docs", json_result=True)
        except ConnectionError:
            try:
                api_summaries = self._gaffer_connector.get("/swagger.json", json_result=True)
            except ConnectionError:
                print(f"swagger information not present, skipping config")
                return ""

        configs = [
            path for path, data in api_summaries["paths"].items()
            if path.startswith("/graph/") and "get" in data
        ]

        template = self.env.get_template("config.py.j2")
        template.globals.update(self._get_function_dict())
        return template.render(configs=configs)

    def _generate_import_strings(self,
                                 funcs: List[Any],
                                 manual_imports: Dict[str,
                                                      Set] = dict()) -> List[str]:
        """
        To stop circular import issues during generation, we only want to import the specific class names we need.
        I.e. rather than `from gafferpy.gaffer_binaroperators import *`, we want
        `from gafferpy.gaffer_binaryoperators import BinaryOperator, ...`

        Args:
            funcs: List of Gaffer Functions, Predicates or BinaryOperators for which to generate import strings.
            manual_imports: Dictionary of manual imports to add, where the keys are manual import paths and values are
                the class to import.

        Returns:
            List of import strings e.g. `from gafferpy.gaffer_binaryoperators import BinaryOperator`

        """
        get_field_types = self._get_function_dict()["get_field_types"]

        class_names = [func.split(".")[-1] for func in funcs]

        import_map = defaultdict(set)
        #  add the manual imports first
        import_map.update(manual_imports)

        for func in funcs:
            for java_type in get_field_types(func).values():
                python_type = parse_java_type_to_string(java_type)
                if "gafferpy" not in python_type:
                    continue

                gafferpy_import = re.findall("gafferpy[\\w+ \\.]*", python_type)[0]
                gafferpy_import = gafferpy_import.replace("generated_api.", "gaffer_")
                import_parts = gafferpy_import.split(".")
                module = ".".join(import_parts[:-1])
                _class = import_parts[-1]
                # only import classes not already defined in the file in question
                if _class not in class_names:
                    import_map[module].add(_class)

        return [
            f"from {import_path} import {','.join(sorted(classes))}" for import_path,
            classes in import_map.items()
        ]

    def get_connector(self):
        return self._gaffer_connector

    def tear_down(self):
        self._gaffer_connector.close_connection()
        shutil.rmtree(self.generated_directory_path)
