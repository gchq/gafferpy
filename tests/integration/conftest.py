#
# Copyright 2023 Crown Copyright
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

from urllib.error import URLError

import pytest

from gafferpy import gaffer_connector, gaffer as g


def _connection_test():
    gc = gaffer_connector.GafferConnector(
        'http://localhost:8080/rest/latest'
    )
    try:
        gc.execute_get(operation=g.GetStatus())
        return True
    except (URLError, ConnectionError):
        return False


def skip_connection():
    if not _connection_test():
        pytest.skip(
            reason="Skipping integration tests as cannot connect to localhost",
            allow_module_level=True
        )


def _return_gaffer_connector():
    return gaffer_connector.GafferConnector(
        'http://localhost:8080/rest/latest'
    )


@pytest.fixture
def gc():
    """
    Vanilla Gaffer Connector used in various test modules
    """
    return _return_gaffer_connector()


def _get_predicates(gc=_return_gaffer_connector()):
    predicates = gc.execute_get(
        g.GetFilterFunctions()
    )
    predicates = g.json.loads(predicates)

    ignore_predicates = [
        'uk.gov.gchq.koryphe.predicate.AdaptedPredicate',
        'uk.gov.gchq.koryphe.predicate.AdaptedPredicate',
        'uk.gov.gchq.koryphe.predicate.PredicateComposite',
        'uk.gov.gchq.gaffer.rest.example.ExampleFilterFunction',
        'uk.gov.gchq.koryphe.tuple.predicate.TupleAdaptedPredicate',
        'uk.gov.gchq.gaffer.data.element.function.ElementFilter',
        'uk.gov.gchq.koryphe.tuple.predicate.TupleAdaptedPredicateComposite',
        'uk.gov.gchq.gaffer.store.util.AggregatorUtil$IsElementAggregated',
        'uk.gov.gchq.gaffer.graph.hook.migrate.predicate.TransformAndFilter',
        'uk.gov.gchq.gaffer.data.element.function.PropertiesFilter'
    ]

    predicates = [pred for pred in predicates if pred not in ignore_predicates]

    return predicates


def _get_functions(gc=_return_gaffer_connector()):
    functions = gc.execute_get(
        g.GetTransformFunctions()
    )
    functions = g.json.loads(functions)

    ignore_functions = [
        'uk.gov.gchq.gaffer.operation.data.generator.EdgeIdExtractor',
        'uk.gov.gchq.gaffer.store.util.AggregatorUtil$ToIngestElementKey',
        'uk.gov.gchq.gaffer.rest.example.ExampleDomainObjectGenerator',
        'uk.gov.gchq.gaffer.data.element.function.ElementTransformer',
        'uk.gov.gchq.gaffer.traffic.generator.RoadTrafficCsvElementGenerator',
        'uk.gov.gchq.gaffer.store.util.AggregatorUtil$ToElementKey',
        'uk.gov.gchq.koryphe.function.FunctionComposite',
        'uk.gov.gchq.gaffer.rest.example.ExampleTransformFunction',
        'uk.gov.gchq.gaffer.data.graph.function.walk.ExtractWalkEdgesFromHop',
        'uk.gov.gchq.gaffer.traffic.transform.DescriptionTransform',
        'uk.gov.gchq.gaffer.store.util.AggregatorUtil$ToQueryElementKey',
        'uk.gov.gchq.koryphe.tuple.TupleInputAdapter',
        'uk.gov.gchq.gaffer.operation.data.generator.EntityIdExtractor',
        'uk.gov.gchq.gaffer.traffic.generator.RoadTrafficStringElementGenerator',
        'uk.gov.gchq.gaffer.rest.example.ExampleElementGenerator',
        'uk.gov.gchq.gaffer.sketches.datasketches.cardinality.HllSketchEntityGenerator',
        'uk.gov.gchq.gaffer.sketches.clearspring.cardinality.HyperLogLogPlusEntityGenerator',
        'uk.gov.gchq.gaffer.data.element.function.PropertiesTransformer'
    ]

    functions = [func for func in functions if func not in ignore_functions]

    return functions


def _get_operations(gc=_return_gaffer_connector()):
    operations = gc.execute_get(
        g.GetOperations()
    )
    operations = g.json.loads(operations)

    return operations
