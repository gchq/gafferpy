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
from gafferpy import gaffer_connector

from .conftest import skip_connection

skip_connection()


pytestmark = pytest.mark.parametrize(
    "client_class,gc",
    [
        (
            "urllib",
            gaffer_connector.GafferConnector(
                "http://localhost:8080/rest/latest",
                client_class="urllib"
            )
        ),
        (
            "requests",
            gaffer_connector.GafferConnector(
                "http://localhost:8080/rest/latest",
                client_class="requests"
            )
        )
    ]
)


def test_execute_operation(client_class, gc):
    elements = gc.execute_operation(
        g.GetElements(
            input=[
                g.EntitySeed("M5:10")
            ],
            view=g.View(
                edges=[
                    g.ElementDefinition(
                        group="JunctionLocatedAt"
                    )
                ]
            )
        )
    )

    assert elements == [
        g.Edge("JunctionLocatedAt", "M5:10", "390466,225615",
               True, {}, "SOURCE"
               )
    ]


def test_is_operation_supported(client_class, gc):
    response = gc.is_operation_supported(
        g.IsOperationSupported(
            operation="uk.gov.gchq.gaffer.operation.impl.get.GetAllElements"
        ),
        json_result=True
    )
    response.pop("next")

    expected_response_json = {"name": "uk.gov.gchq.gaffer.operation.impl.get.GetAllElements",
                              "summary": "Gets all elements compatible with a provided View",
                              "fields": [{"name": "view",
                                          "className": "uk.gov.gchq.gaffer.data.elementdefinition.view.View",
                                          "required": False},
                                         {"name": "options",
                                          "className": "java.util.Map<java.lang.String,java.lang.String>",
                                          "required": False},
                                         {"name": "directedType",
                                          "summary": "Is the Edge directed?",
                                             "className": "java.lang.String",
                                             "options": ["DIRECTED",
                                                         "UNDIRECTED",
                                                         "EITHER"],
                                             "required": False},
                                         {"name": "views",
                                          "className": "java.util.List<uk.gov.gchq.gaffer.data.elementdefinition.view.View>",
                                             "required": False}],
                              "exampleJson": {"class": "uk.gov.gchq.gaffer.operation.impl.get.GetAllElements"},
                              "outputClassName": "java.lang.Iterable<uk.gov.gchq.gaffer.data.element.Element>"}

    assert response == expected_response_json


def test_execute_get(client_class, gc):
    response = gc.execute_get(
        g.GetSchema(),
        json_result=True
    )

    assert isinstance(response, dict) and response != {}


def test_dummy_header(client_class, gc):
    """
    Test that the addition of a dummy header does not effect the standard test
    """
    gc = gaffer_connector.GafferConnector(
        "http://localhost:8080/rest/latest",
        headers={
            "dummy_Header": "value"},
        client_class=client_class
    )

    elements = gc.execute_operation(
        g.GetElements(
            input=[
                g.EntitySeed("M5:10")
            ],
            view=g.View(
                edges=[
                    g.ElementDefinition(
                        group="JunctionLocatedAt"
                    )
                ]
            )
        )
    )

    assert elements == [g.Edge("JunctionLocatedAt", "M5:10", "390466,225615", True, {},
                               "SOURCE")]


def test_class_initilisation(client_class, gc):
    """
    Test that the gaffer_connector class is correctly initialised with instance attributes
    """
    host = "http://localhost:8080/rest/latest"
    verbose = False
    headers = {"dummy_Header": "value"}
    gc = gaffer_connector.GafferConnector(
        host, verbose, headers, client_class=client_class
    )

    actuals = [gc._host, gc._verbose, gc._headers]
    expecteds = [host, verbose, headers]

    for actual, expected in zip(actuals, expecteds):
        assert actual == expected


def test_raise_connection_error(client_class, gc):
    """
    Test that a ConnectionError is correctly raised when a HTTP 404 error is caught
    """
    # Define a host that has an invalid endpoint in order to get a HTTP 404 error
    host_with_bad_endpoint = "http://localhost:8080/badEndPoint"
    gc = gaffer_connector.GafferConnector(
        host_with_bad_endpoint, client_class=client_class)

    # Check that a ConnectionError is raised (which is catching the underlying HTTP 404)
    with pytest.raises(ConnectionError):
        gc.execute_get(g.GetOperations())


def test_raise_connection_error_https(client_class, gc):
    """
    Test that an error is correctly raised when a HTTPS endpoint cannot be found
    """
    # Define a host that uses https
    host_with_ssh_endpoint = "https://localhost:8080/rest/latest"
    gc = gaffer_connector.GafferConnector(
        host_with_ssh_endpoint, client_class=client_class)

    # Check that an OSError is raised (caused by SSLError)
    with pytest.raises(OSError):
        gc.execute_get(g.GetOperations())
