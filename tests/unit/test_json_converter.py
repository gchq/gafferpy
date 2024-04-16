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
import json

from gafferpy import gaffer as g
from gafferpy.gaffer_core import JsonConverter


def test_throw_improper_string_json():
    with pytest.raises(json.JSONDecodeError):
        JsonConverter.from_json("Not json")


def test_throw_when_op():
    with pytest.raises(TypeError):
        JsonConverter.from_json(g.GetAllElements())


def test_throw_when_not_json(non_serialisable_object):
    with pytest.raises(TypeError):
        JsonConverter.from_json(non_serialisable_object())


def test_correct_json(get_all_elements_json):
    assert JsonConverter.from_json(get_all_elements_json) == g.GetAllElements()


def test_incorrect_json(get_all_elements_json):
    with pytest.raises(TypeError):
        JsonConverter.from_json(get_all_elements_json, g.GetAllGraphIds())
