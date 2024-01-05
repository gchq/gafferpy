#
# Copyright 2016-2023 Crown Copyright
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


"""
This module contains Python copies of common Gaffer java types.
"""

from typing import Any, Dict, List, Optional, Set, Tuple
import logging
import re

from gafferpy.gaffer_core import ElementSeed, EntitySeed, EdgeSeed, Element, JsonConverter, Function, BinaryOperator, Predicate
from gafferpy.gaffer_operations import Operation

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

anys = (
    "T", "Object", "Object[]", "?", "OBJ", "java.lang.Object", "I", "I_ITEM",
    "java.lang.Class", "uk.gov.gchq.gaffer.access.predicate.AccessPredicate"
)
lists = "java.lang.Iterable", "java.util.List", "java.util.Collection"
dicts = "java.util.Map", "java.util.LinkedHashMap", "java.util.Properties", "uk.gov.gchq.gaffer.store.schema.Schema"
strings = "java.lang.String", "char"
ints = "java.lang.Integer", "java.lang.Long", "int"


def parse_java_type_to_string(java_type: str, return_full_path: bool = True) -> str:
    """
    Parse a Java type into a Python type and return as a string.

    Args:
        java_type: String of a Java type
        return_full_path: Whether to return the full `gafferpy` path to a class i.e.
            `gafferpy.gaffer_core.Function`, or just the class i.e. `Function`

    Returns:
        String of Python type
    """

    python_type = parse_java_type(java_type)
    if isinstance(python_type, type):
        if python_type.__module__ == "builtins":
            return python_type.__name__
        type_name = f"{python_type.__module__}.{python_type.__name__}"
    else:
        type_name = str(python_type)

    if return_full_path is False and 'gafferpy' in type_name:
        gafferpy_class = re.findall("gafferpy[\\w+ \\.]*", type_name)[0]
        # replace the full gafferpy path with just class name
        type_name = type_name.replace(gafferpy_class, gafferpy_class.split('.')[-1])

    return type_name


def parse_java_type(java_type: str) -> type:
    """
    Parse a Java type into a Python type object.

    Args:
        java_type: String of a Java type

    Returns:
        Python type
    """
    if "[]" in java_type:
        array_type = java_type.split("[]")[0]
        return List[parse_java_type(array_type)]
    if "<" in java_type:
        split = java_type.split("<")
        outter_type = split[0]
        inner_type = ">".join(split[1].split(">")[:-1])
        if outter_type in anys:
            return Any
        if inner_type in anys:
            return parse_java_type(outter_type)
        try:
            return parse_java_type(outter_type)[parse_java_type(inner_type)]
        except BaseException:
            if "java.util.function.BinaryOperator" in java_type:
                return BinaryOperator
            if "java.util.function.Function" in java_type:
                return Function
            if "java.util.function.Predicate" in java_type:
                return Predicate
            logger.warning(
                f"Unable to determine Python type for Java type {java_type}, using typing.Any")
            return Any
    if "," in java_type:
        split = java_type.split(",")
        first_type = split[0]
        remaining_types = ",".join(split[1:])
        return parse_java_type(first_type), parse_java_type(remaining_types)
    if java_type in anys:
        return Any
    if java_type in lists:
        return List
    if java_type in dicts:
        return Dict
    if java_type in strings:
        return str
    if java_type in ints:
        return int
    if java_type == "java.lang.Float":
        return float
    if java_type == "java.lang.Boolean":
        return bool
    if java_type == "java.util.Set":
        return Set
    if java_type == "uk.gov.gchq.gaffer.commonutil.pair.Pair":
        return Tuple
    if java_type == "uk.gov.gchq.gaffer.data.element.id.ElementId":
        return ElementSeed
    if java_type == "uk.gov.gchq.gaffer.data.element.id.EntityId":
        return EntitySeed
    if java_type == "uk.gov.gchq.gaffer.data.element.id.EdgeId":
        return EdgeSeed
    if java_type == "uk.gov.gchq.gaffer.data.element.Element":
        return Element
    if java_type == "uk.gov.gchq.gaffer.operation.Operation":
        return Operation

    if java_type in JsonConverter.CLASS_MAP:
        return JsonConverter.CLASS_MAP[java_type]
    return Any


def long(value: int) -> Dict[str, int]:
    """
    Convert integer value to an object that Gaffer can serialise into a Java Long type.

    Args:
        value: Integer value to convert

    Returns:
        Dictionary that can be serialised to a Java Long.
    """
    return {"java.lang.Long": value}


def date(value: int) -> Dict[str, int]:
    """
    Convert integer value to an object that Gaffer can serialise into a Java Date type.

    Args:
        value: Integer value to convert

    Returns:
        Dictionary that can be serialised to a Java Date.
    """
    return {"java.util.Date": value}


def freq_map(map_value: Dict[Any, int]) -> Dict[str, Dict[Any, int]]:
    """
    Convert {k:v} dict to an object that Gaffer can serialise into a Gaffer FreqMap type.

    Args:
        value: Dictionary to convert

    Returns:
        Dictionary that can be serialised to a Gaffer FreqMap.
    """
    return {"uk.gov.gchq.gaffer.types.FreqMap": map_value}


def tree_set(set: Set[Any]) -> Dict[str, Set[Any]]:
    """
    Convert set to an object that Gaffer can serialise into a Java TreeSet type.

    Args:
        set: Set to convert

    Returns:
        Dictionary that can be serialised to a Java TreeSet.
    """
    return {"java.util.TreeSet": set}


def type_value(
    type: Optional[Any] = None,
    value: Optional[Any] = None
) -> Dict[str, Dict[str, Any]]:
    """
    Convert a type and value to an object that Gaffer can serialise into a Gaffer TypeSubTypeValue type.

    Args:
        type: Populates `type` field in a Gaffer TypeSubTypeValue object
        value: Populates `value` field in a Gaffer TypeSubTypeValue object

    Returns:
        Dictionary that can be serialised to a Gaffer TypeSubTypeValue.
    """
    map = {}
    if type is not None:
        map["type"] = type
    if value is not None:
        map["value"] = value
    return {"uk.gov.gchq.gaffer.types.TypeSubTypeValue": map}


def type_subtype_value(
    type: Optional[Any] = None,
    subType: Optional[Any] = None,
    value: Optional[Any] = None
) -> Dict[str, Dict[str, Any]]:
    """
    Convert a type, subType and value to an object that Gaffer can serialise into a Gaffer TypeSubTypeValue type.

    Args:
        type: Populates `type` field in a Gaffer TypeSubTypeValue object
        subType: Populates `subType` field in a Gaffer TypeSubTypeValue object
        value: Populates `value` field in a Gaffer TypeSubTypeValue object

    Returns:
        Dictionary that can be serialised to a Gaffer TypeSubTypeValue.
    """
    map = {}
    if type is not None:
        map["type"] = type
    if subType is not None:
        map["subType"] = subType
    if value is not None:
        map["value"] = value
    return {"uk.gov.gchq.gaffer.types.TypeSubTypeValue": map}


def hyper_log_log_plus(
    offers: List[Any],
    p: int = 5,
    sp: int = 5
) -> Dict[str, Dict[str, Dict[str, Any]]]:
    """
    Convert a list of objects to an object that Gaffer can serialise into a HyperLogLogPlus Sketch.

    Args:
        offers: Objects to add to the Sketch
        p: Defines the accuracy and ultimately the size of Sketch.
        sp: Defines the error properties of the Sketch sparse mode.

    Returns:
        Dictionary that can be serialised to a clearspring HyperLogLogPlus Sketch.
    """
    return {"com.clearspring.analytics.stream.cardinality.HyperLogLogPlus": {
        "hyperLogLogPlus": {"p": p, "sp": sp, "offers": offers}}}


def hll_sketch(
    values: List[Any],
    log_k: int = 10
) -> Dict[str, Dict[str, Any]]:
    """
    Convert a list of objects to an object that Gaffer can serialise into a HyperLogLog Sketch.

    Args:
        values: Objects to add to the Sketch
        log_k: Defines the accuracy and ultimately the size of Sketch.

    Returns:
        Dictionary that can be serialised to a clearspring HyperLogLog Sketch.
    """
    return {
        "org.apache.datasketches.hll.HllSketch": {
            "logK": log_k,
            "values": values
        }
    }
