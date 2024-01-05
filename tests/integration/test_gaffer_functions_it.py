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

from .conftest import skip_connection, _get_functions

skip_connection()


@pytest.fixture(params=_get_functions())
def functions_to_test(request):
    return request.param


def test_all_functions_have_classes(functions_to_test):
    assert functions_to_test in g.JsonConverter.GENERIC_JSON_CONVERTERS
