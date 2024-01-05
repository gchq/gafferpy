#
# Copyright 2016-2023 Crown Copyright
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

import pytest

from gafferpy import gaffer as g

from .conftest import skip_connection, _get_operations

skip_connection()


@pytest.fixture(params=_get_operations())
def operations_to_test(request):
    return request.param


def test_all_supported_operations_have_classes(operations_to_test):
    assert operations_to_test in g.JsonConverter.GENERIC_JSON_CONVERTERS


def test_all_supported_operation_examples(gc):
    operation_details = gc.execute_get(
        g.GetOperationsDetails(), json_result=True
    )
    for detail in operation_details:
        try:
            gc.execute_operation(
                g.JsonConverter.from_json(
                    detail["exampleJson"],
                    class_name=detail["name"]
                )
            )
        except ConnectionError as e:
            # Ignore 500 as a lot of operation examples won't run as they have dummy data
            # We just care they are valid operations and don't return 400 error
            if "HTTP error 500" in e.__str__():
                pass
            else:
                raise e


def _get_all_subclasses(cls):
    all_subclasses = []

    for subclass in cls.__subclasses__():
        if hasattr(subclass, "CLASS"):
            all_subclasses.append(subclass)
            all_subclasses.extend(_get_all_subclasses(subclass))

    return all_subclasses


def test_all_operation_classes_are_valid(gc):
    # TODO: This should be in fishbowl tests in the future
    # only the spring-rest has this endpoint
    try:
        response = gc.execute_get(
            g.GetOperationsDetailsAll(),
            json_result=True
        )
    except BaseException:
        return

    response = [operation["name"] for operation in response]

    operation_subclasses = _get_all_subclasses(g.Operation)
    expected_response = set(c.CLASS for c in operation_subclasses)

    assert sorted(expected_response) == sorted(response)
