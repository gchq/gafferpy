#
# Copyright 2022 Crown Copyright
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

"""
This module has been generated with fishbowl.
To make changes, either extend these classes or change fishbowl.
"""

import typing
from gafferpy.gaffer_core import AbstractPredicate,Function,Predicate
from gafferpy.gaffer_functions import ElementTransformer


class DefaultUserPredicate(AbstractPredicate):
    CLASS = "uk.gov.gchq.gaffer.access.predicate.user.DefaultUserPredicate"

    def __init__(
        self,
        auths: typing.Optional[typing.List[str]] = None,
        creating_user_id: typing.Optional[str] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.auths = auths
        self.creating_user_id = creating_user_id

    def to_json(self):
        function_json = super().to_json()
        if self.auths is not None:
            function_json["auths"] = self.auths
        if self.creating_user_id is not None:
            function_json["creatingUserId"] = self.creating_user_id
        return function_json


class NoAccessUserPredicate(AbstractPredicate):
    CLASS = "uk.gov.gchq.gaffer.access.predicate.user.NoAccessUserPredicate"

    def __init__(self):
        super().__init__(_class_name=self.CLASS)

    def to_json(self):
        return super().to_json()


class UnrestrictedAccessUserPredicate(AbstractPredicate):
    CLASS = "uk.gov.gchq.gaffer.access.predicate.user.UnrestrictedAccessUserPredicate"

    def __init__(self):
        super().__init__(_class_name=self.CLASS)

    def to_json(self):
        return super().to_json()


class ElementJoinComparator(AbstractPredicate):
    CLASS = "uk.gov.gchq.gaffer.data.element.comparison.ElementJoinComparator"

    def __init__(
        self,
        group_by_properties: typing.Optional[typing.Set[str]] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.group_by_properties = group_by_properties

    def to_json(self):
        function_json = super().to_json()
        if self.group_by_properties is not None:
            function_json["groupByProperties"] = self.group_by_properties
        return function_json


class ElementFilter(AbstractPredicate):
    CLASS = "uk.gov.gchq.gaffer.data.element.function.ElementFilter"

    def __init__(
        self,
        predicates: typing.Optional[typing.List[typing.Any]] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.predicates = predicates

    def to_json(self):
        function_json = super().to_json()
        if self.predicates is not None:
            function_json["predicates"] = self.predicates
        return function_json


class PropertiesFilter(AbstractPredicate):
    CLASS = "uk.gov.gchq.gaffer.data.element.function.PropertiesFilter"

    def __init__(
        self,
        predicates: typing.Optional[typing.List[typing.Any]] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.predicates = predicates

    def to_json(self):
        function_json = super().to_json()
        if self.predicates is not None:
            function_json["predicates"] = self.predicates
        return function_json


class NamedViewWriteUserPredicate(AbstractPredicate):
    CLASS = "uk.gov.gchq.gaffer.data.elementdefinition.view.access.predicate.user.NamedViewWriteUserPredicate"

    def __init__(
        self,
        auths: typing.Optional[typing.List[str]] = None,
        creating_user_id: typing.Optional[str] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.auths = auths
        self.creating_user_id = creating_user_id

    def to_json(self):
        function_json = super().to_json()
        if self.auths is not None:
            function_json["auths"] = self.auths
        if self.creating_user_id is not None:
            function_json["creatingUserId"] = self.creating_user_id
        return function_json


class FederatedGraphReadUserPredicate(AbstractPredicate):
    CLASS = "uk.gov.gchq.gaffer.federatedstore.access.predicate.user.FederatedGraphReadUserPredicate"

    def __init__(
        self,
        public: typing.Optional[bool] = None,
        auths: typing.Optional[typing.List[str]] = None,
        creating_user_id: typing.Optional[str] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.public = public
        self.auths = auths
        self.creating_user_id = creating_user_id

    def to_json(self):
        function_json = super().to_json()
        if self.public is not None:
            function_json["public"] = self.public
        if self.auths is not None:
            function_json["auths"] = self.auths
        if self.creating_user_id is not None:
            function_json["creatingUserId"] = self.creating_user_id
        return function_json


class FederatedGraphWriteUserPredicate(AbstractPredicate):
    CLASS = "uk.gov.gchq.gaffer.federatedstore.access.predicate.user.FederatedGraphWriteUserPredicate"

    def __init__(
        self,
        creating_user_id: typing.Optional[str] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.creating_user_id = creating_user_id

    def to_json(self):
        function_json = super().to_json()
        if self.creating_user_id is not None:
            function_json["creatingUserId"] = self.creating_user_id
        return function_json


class TransformAndFilter(AbstractPredicate):
    CLASS = "uk.gov.gchq.gaffer.graph.hook.migrate.predicate.TransformAndFilter"

    def __init__(
        self,
        filter: typing.Optional[ElementFilter] = None,
        transformer: typing.Optional[ElementTransformer] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.filter = filter
        self.transformer = transformer

    def to_json(self):
        function_json = super().to_json()
        if self.filter is not None:
            function_json["filter"] = self.filter
        if self.transformer is not None:
            function_json["transformer"] = self.transformer
        return function_json


class ExampleFilterFunction(AbstractPredicate):
    CLASS = "uk.gov.gchq.gaffer.rest.example.ExampleFilterFunction"

    def __init__(self):
        super().__init__(_class_name=self.CLASS)

    def to_json(self):
        return super().to_json()


class HyperLogLogPlusIsLessThan(AbstractPredicate):
    CLASS = "uk.gov.gchq.gaffer.sketches.clearspring.cardinality.predicate.HyperLogLogPlusIsLessThan"

    def __init__(
        self,
        value: typing.Optional[int] = None,
        or_equal_to: typing.Optional[bool] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.value = value
        self.or_equal_to = or_equal_to

    def to_json(self):
        function_json = super().to_json()
        if self.value is not None:
            function_json["value"] = self.value
        if self.or_equal_to is not None:
            function_json["orEqualTo"] = self.or_equal_to
        return function_json


class HllSketchIsLessThan(AbstractPredicate):
    CLASS = "uk.gov.gchq.gaffer.sketches.datasketches.cardinality.predicate.HllSketchIsLessThan"

    def __init__(
        self,
        value: typing.Optional[int] = None,
        or_equal_to: typing.Optional[bool] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.value = value
        self.or_equal_to = or_equal_to

    def to_json(self):
        function_json = super().to_json()
        if self.value is not None:
            function_json["value"] = self.value
        if self.or_equal_to is not None:
            function_json["orEqualTo"] = self.or_equal_to
        return function_json


class AggregatorUtilIsElementAggregated(AbstractPredicate):
    CLASS = "uk.gov.gchq.gaffer.store.util.AggregatorUtil$IsElementAggregated"

    def __init__(self):
        super().__init__(_class_name=self.CLASS)

    def to_json(self):
        return super().to_json()


class RBMBackedTimestampSetInRange(AbstractPredicate):
    CLASS = "uk.gov.gchq.gaffer.time.predicate.RBMBackedTimestampSetInRange"

    def __init__(
        self,
        start_time: typing.Optional[typing.Any] = None,
        end_time: typing.Optional[typing.Any] = None,
        include_all_timestamps: typing.Optional[bool] = None,
        time_unit: typing.Optional[str] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.start_time = start_time
        self.end_time = end_time
        self.include_all_timestamps = include_all_timestamps
        self.time_unit = time_unit

    def to_json(self):
        function_json = super().to_json()
        if self.start_time is not None:
            function_json["startTime"] = self.start_time
        if self.end_time is not None:
            function_json["endTime"] = self.end_time
        if self.include_all_timestamps is not None:
            function_json["includeAllTimestamps"] = self.include_all_timestamps
        if self.time_unit is not None:
            function_json["timeUnit"] = self.time_unit
        return function_json


class AgeOff(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.impl.predicate.AgeOff"

    def __init__(
        self,
        age_off_hours: typing.Optional[int] = None,
        age_off_days: typing.Optional[int] = None,
        age_off_time: typing.Optional[int] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.age_off_hours = age_off_hours
        self.age_off_days = age_off_days
        self.age_off_time = age_off_time

    def to_json(self):
        function_json = super().to_json()
        if self.age_off_hours is not None:
            function_json["ageOffHours"] = self.age_off_hours
        if self.age_off_days is not None:
            function_json["ageOffDays"] = self.age_off_days
        if self.age_off_time is not None:
            function_json["ageOffTime"] = self.age_off_time
        return function_json


class AgeOffFromDays(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.impl.predicate.AgeOffFromDays"

    def __init__(self):
        super().__init__(_class_name=self.CLASS)

    def to_json(self):
        return super().to_json()


class And(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.impl.predicate.And"

    def __init__(
        self,
        predicates: typing.Optional[typing.List[typing.Any]] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.predicates = predicates

    def to_json(self):
        function_json = super().to_json()
        if self.predicates is not None:
            function_json["predicates"] = self.predicates
        return function_json


class AreEqual(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.impl.predicate.AreEqual"

    def __init__(self):
        super().__init__(_class_name=self.CLASS)

    def to_json(self):
        return super().to_json()


class AreIn(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.impl.predicate.AreIn"

    def __init__(
        self,
        values: typing.Optional[typing.List[typing.Any]] = None,
        null_or_empty_values_accepted: typing.Optional[bool] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.values = values
        self.null_or_empty_values_accepted = null_or_empty_values_accepted

    def to_json(self):
        function_json = super().to_json()
        if self.values is not None:
            function_json["values"] = self.values
        if self.null_or_empty_values_accepted is not None:
            function_json["nullOrEmptyValuesAccepted"] = self.null_or_empty_values_accepted
        return function_json


class CollectionContains(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.impl.predicate.CollectionContains"

    def __init__(
        self,
        value: typing.Optional[typing.Any] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.value = value

    def to_json(self):
        function_json = super().to_json()
        if self.value is not None:
            function_json["value"] = self.value
        return function_json


class Exists(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.impl.predicate.Exists"

    def __init__(self):
        super().__init__(_class_name=self.CLASS)

    def to_json(self):
        return super().to_json()


class If(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.impl.predicate.If"

    def __init__(
        self,
        otherwise: typing.Optional[Predicate] = None,
        predicate: typing.Optional[Predicate] = None,
        condition: typing.Optional[bool] = None,
        then: typing.Optional[Predicate] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.otherwise = otherwise
        self.predicate = predicate
        self.condition = condition
        self.then = then

    def to_json(self):
        function_json = super().to_json()
        if self.otherwise is not None:
            function_json["otherwise"] = self.otherwise
        if self.predicate is not None:
            function_json["predicate"] = self.predicate
        if self.condition is not None:
            function_json["condition"] = self.condition
        if self.then is not None:
            function_json["then"] = self.then
        return function_json


class IsA(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.impl.predicate.IsA"

    def __init__(
        self,
        type: typing.Optional[str] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.type = type

    def to_json(self):
        function_json = super().to_json()
        if self.type is not None:
            function_json["type"] = self.type
        return function_json


class IsEqual(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.impl.predicate.IsEqual"

    def __init__(
        self,
        value: typing.Optional[typing.Any] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.value = value

    def to_json(self):
        function_json = super().to_json()
        if self.value is not None:
            function_json["value"] = self.value
        return function_json


class IsFalse(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.impl.predicate.IsFalse"

    def __init__(self):
        super().__init__(_class_name=self.CLASS)

    def to_json(self):
        return super().to_json()


class IsIn(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.impl.predicate.IsIn"

    def __init__(
        self,
        values: typing.Optional[typing.List[typing.Any]] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.values = values

    def to_json(self):
        function_json = super().to_json()
        if self.values is not None:
            function_json["values"] = self.values
        return function_json


class IsLessThan(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.impl.predicate.IsLessThan"

    def __init__(
        self,
        value: typing.Optional[typing.Any] = None,
        or_equal_to: typing.Optional[bool] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.value = value
        self.or_equal_to = or_equal_to

    def to_json(self):
        function_json = super().to_json()
        if self.value is not None:
            function_json["value"] = self.value
        if self.or_equal_to is not None:
            function_json["orEqualTo"] = self.or_equal_to
        return function_json


class IsLongerThan(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.impl.predicate.IsLongerThan"

    def __init__(
        self,
        min_length: typing.Optional[int] = None,
        or_equal_to: typing.Optional[bool] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.min_length = min_length
        self.or_equal_to = or_equal_to

    def to_json(self):
        function_json = super().to_json()
        if self.min_length is not None:
            function_json["minLength"] = self.min_length
        if self.or_equal_to is not None:
            function_json["orEqualTo"] = self.or_equal_to
        return function_json


class IsMoreThan(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.impl.predicate.IsMoreThan"

    def __init__(
        self,
        value: typing.Optional[typing.Any] = None,
        or_equal_to: typing.Optional[bool] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.value = value
        self.or_equal_to = or_equal_to

    def to_json(self):
        function_json = super().to_json()
        if self.value is not None:
            function_json["value"] = self.value
        if self.or_equal_to is not None:
            function_json["orEqualTo"] = self.or_equal_to
        return function_json


class IsShorterThan(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.impl.predicate.IsShorterThan"

    def __init__(
        self,
        max_length: typing.Optional[int] = None,
        or_equal_to: typing.Optional[bool] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.max_length = max_length
        self.or_equal_to = or_equal_to

    def to_json(self):
        function_json = super().to_json()
        if self.max_length is not None:
            function_json["maxLength"] = self.max_length
        if self.or_equal_to is not None:
            function_json["orEqualTo"] = self.or_equal_to
        return function_json


class IsTrue(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.impl.predicate.IsTrue"

    def __init__(self):
        super().__init__(_class_name=self.CLASS)

    def to_json(self):
        return super().to_json()


class IsXLessThanY(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.impl.predicate.IsXLessThanY"

    def __init__(self):
        super().__init__(_class_name=self.CLASS)

    def to_json(self):
        return super().to_json()


class IsXMoreThanY(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.impl.predicate.IsXMoreThanY"

    def __init__(self):
        super().__init__(_class_name=self.CLASS)

    def to_json(self):
        return super().to_json()


class MapContains(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.impl.predicate.MapContains"

    def __init__(
        self,
        key: typing.Optional[str] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.key = key

    def to_json(self):
        function_json = super().to_json()
        if self.key is not None:
            function_json["key"] = self.key
        return function_json


class MapContainsPredicate(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.impl.predicate.MapContainsPredicate"

    def __init__(
        self,
        key_predicate: typing.Optional[Predicate] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.key_predicate = key_predicate

    def to_json(self):
        function_json = super().to_json()
        if self.key_predicate is not None:
            function_json["keyPredicate"] = self.key_predicate
        return function_json


class MultiRegex(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.impl.predicate.MultiRegex"

    def __init__(
        self,
        value: typing.Optional[typing.List[typing.Any]] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.value = value

    def to_json(self):
        function_json = super().to_json()
        if self.value is not None:
            function_json["value"] = self.value
        return function_json


class Not(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.impl.predicate.Not"

    def __init__(
        self,
        predicate: typing.Optional[Predicate] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.predicate = predicate

    def to_json(self):
        function_json = super().to_json()
        if self.predicate is not None:
            function_json["predicate"] = self.predicate
        return function_json


class Or(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.impl.predicate.Or"

    def __init__(
        self,
        predicates: typing.Optional[typing.List[typing.Any]] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.predicates = predicates

    def to_json(self):
        function_json = super().to_json()
        if self.predicates is not None:
            function_json["predicates"] = self.predicates
        return function_json


class Regex(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.impl.predicate.Regex"

    def __init__(
        self,
        value: typing.Optional[typing.Any] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.value = value

    def to_json(self):
        function_json = super().to_json()
        if self.value is not None:
            function_json["value"] = self.value
        return function_json


class StringContains(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.impl.predicate.StringContains"

    def __init__(
        self,
        ignore_case: typing.Optional[bool] = None,
        value: typing.Optional[str] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.ignore_case = ignore_case
        self.value = value

    def to_json(self):
        function_json = super().to_json()
        if self.ignore_case is not None:
            function_json["ignoreCase"] = self.ignore_case
        if self.value is not None:
            function_json["value"] = self.value
        return function_json


class InDateRange(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.impl.predicate.range.InDateRange"

    def __init__(
        self,
        end_offset: typing.Optional[int] = None,
        offset_unit: typing.Optional[str] = None,
        start_offset: typing.Optional[int] = None,
        start_inclusive: typing.Optional[bool] = None,
        start: typing.Optional[str] = None,
        time_zone: typing.Optional[str] = None,
        end: typing.Optional[str] = None,
        end_inclusive: typing.Optional[bool] = None,
        time_unit: typing.Optional[str] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.end_offset = end_offset
        self.offset_unit = offset_unit
        self.start_offset = start_offset
        self.start_inclusive = start_inclusive
        self.start = start
        self.time_zone = time_zone
        self.end = end
        self.end_inclusive = end_inclusive
        self.time_unit = time_unit

    def to_json(self):
        function_json = super().to_json()
        if self.end_offset is not None:
            function_json["endOffset"] = self.end_offset
        if self.offset_unit is not None:
            function_json["offsetUnit"] = self.offset_unit
        if self.start_offset is not None:
            function_json["startOffset"] = self.start_offset
        if self.start_inclusive is not None:
            function_json["startInclusive"] = self.start_inclusive
        if self.start is not None:
            function_json["start"] = self.start
        if self.time_zone is not None:
            function_json["timeZone"] = self.time_zone
        if self.end is not None:
            function_json["end"] = self.end
        if self.end_inclusive is not None:
            function_json["endInclusive"] = self.end_inclusive
        if self.time_unit is not None:
            function_json["timeUnit"] = self.time_unit
        return function_json


class InDateRangeDual(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.impl.predicate.range.InDateRangeDual"

    def __init__(
        self,
        end_fully_contained: typing.Optional[bool] = None,
        end_offset: typing.Optional[int] = None,
        offset_unit: typing.Optional[str] = None,
        start_offset: typing.Optional[int] = None,
        start_inclusive: typing.Optional[bool] = None,
        start: typing.Optional[str] = None,
        time_zone: typing.Optional[str] = None,
        end: typing.Optional[str] = None,
        end_inclusive: typing.Optional[bool] = None,
        start_fully_contained: typing.Optional[bool] = None,
        time_unit: typing.Optional[str] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.end_fully_contained = end_fully_contained
        self.end_offset = end_offset
        self.offset_unit = offset_unit
        self.start_offset = start_offset
        self.start_inclusive = start_inclusive
        self.start = start
        self.time_zone = time_zone
        self.end = end
        self.end_inclusive = end_inclusive
        self.start_fully_contained = start_fully_contained
        self.time_unit = time_unit

    def to_json(self):
        function_json = super().to_json()
        if self.end_fully_contained is not None:
            function_json["endFullyContained"] = self.end_fully_contained
        if self.end_offset is not None:
            function_json["endOffset"] = self.end_offset
        if self.offset_unit is not None:
            function_json["offsetUnit"] = self.offset_unit
        if self.start_offset is not None:
            function_json["startOffset"] = self.start_offset
        if self.start_inclusive is not None:
            function_json["startInclusive"] = self.start_inclusive
        if self.start is not None:
            function_json["start"] = self.start
        if self.time_zone is not None:
            function_json["timeZone"] = self.time_zone
        if self.end is not None:
            function_json["end"] = self.end
        if self.end_inclusive is not None:
            function_json["endInclusive"] = self.end_inclusive
        if self.start_fully_contained is not None:
            function_json["startFullyContained"] = self.start_fully_contained
        if self.time_unit is not None:
            function_json["timeUnit"] = self.time_unit
        return function_json


class InRange(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.impl.predicate.range.InRange"

    def __init__(
        self,
        start_inclusive: typing.Optional[bool] = None,
        start: typing.Optional[typing.Any] = None,
        end: typing.Optional[typing.Any] = None,
        end_inclusive: typing.Optional[bool] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.start_inclusive = start_inclusive
        self.start = start
        self.end = end
        self.end_inclusive = end_inclusive

    def to_json(self):
        function_json = super().to_json()
        if self.start_inclusive is not None:
            function_json["startInclusive"] = self.start_inclusive
        if self.start is not None:
            function_json["start"] = self.start
        if self.end is not None:
            function_json["end"] = self.end
        if self.end_inclusive is not None:
            function_json["endInclusive"] = self.end_inclusive
        return function_json


class InRangeDual(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.impl.predicate.range.InRangeDual"

    def __init__(
        self,
        end_fully_contained: typing.Optional[bool] = None,
        start_inclusive: typing.Optional[bool] = None,
        start: typing.Optional[typing.Any] = None,
        end: typing.Optional[typing.Any] = None,
        end_inclusive: typing.Optional[bool] = None,
        start_fully_contained: typing.Optional[bool] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.end_fully_contained = end_fully_contained
        self.start_inclusive = start_inclusive
        self.start = start
        self.end = end
        self.end_inclusive = end_inclusive
        self.start_fully_contained = start_fully_contained

    def to_json(self):
        function_json = super().to_json()
        if self.end_fully_contained is not None:
            function_json["endFullyContained"] = self.end_fully_contained
        if self.start_inclusive is not None:
            function_json["startInclusive"] = self.start_inclusive
        if self.start is not None:
            function_json["start"] = self.start
        if self.end is not None:
            function_json["end"] = self.end
        if self.end_inclusive is not None:
            function_json["endInclusive"] = self.end_inclusive
        if self.start_fully_contained is not None:
            function_json["startFullyContained"] = self.start_fully_contained
        return function_json


class InTimeRange(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.impl.predicate.range.InTimeRange"

    def __init__(
        self,
        end_offset: typing.Optional[int] = None,
        offset_unit: typing.Optional[str] = None,
        start_offset: typing.Optional[int] = None,
        start_inclusive: typing.Optional[bool] = None,
        start: typing.Optional[str] = None,
        time_zone: typing.Optional[str] = None,
        end: typing.Optional[str] = None,
        end_inclusive: typing.Optional[bool] = None,
        time_unit: typing.Optional[str] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.end_offset = end_offset
        self.offset_unit = offset_unit
        self.start_offset = start_offset
        self.start_inclusive = start_inclusive
        self.start = start
        self.time_zone = time_zone
        self.end = end
        self.end_inclusive = end_inclusive
        self.time_unit = time_unit

    def to_json(self):
        function_json = super().to_json()
        if self.end_offset is not None:
            function_json["endOffset"] = self.end_offset
        if self.offset_unit is not None:
            function_json["offsetUnit"] = self.offset_unit
        if self.start_offset is not None:
            function_json["startOffset"] = self.start_offset
        if self.start_inclusive is not None:
            function_json["startInclusive"] = self.start_inclusive
        if self.start is not None:
            function_json["start"] = self.start
        if self.time_zone is not None:
            function_json["timeZone"] = self.time_zone
        if self.end is not None:
            function_json["end"] = self.end
        if self.end_inclusive is not None:
            function_json["endInclusive"] = self.end_inclusive
        if self.time_unit is not None:
            function_json["timeUnit"] = self.time_unit
        return function_json


class InTimeRangeDual(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.impl.predicate.range.InTimeRangeDual"

    def __init__(
        self,
        end_fully_contained: typing.Optional[bool] = None,
        end_offset: typing.Optional[int] = None,
        offset_unit: typing.Optional[str] = None,
        start_offset: typing.Optional[int] = None,
        start_inclusive: typing.Optional[bool] = None,
        start: typing.Optional[str] = None,
        time_zone: typing.Optional[str] = None,
        end: typing.Optional[str] = None,
        end_inclusive: typing.Optional[bool] = None,
        start_fully_contained: typing.Optional[bool] = None,
        time_unit: typing.Optional[str] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.end_fully_contained = end_fully_contained
        self.end_offset = end_offset
        self.offset_unit = offset_unit
        self.start_offset = start_offset
        self.start_inclusive = start_inclusive
        self.start = start
        self.time_zone = time_zone
        self.end = end
        self.end_inclusive = end_inclusive
        self.start_fully_contained = start_fully_contained
        self.time_unit = time_unit

    def to_json(self):
        function_json = super().to_json()
        if self.end_fully_contained is not None:
            function_json["endFullyContained"] = self.end_fully_contained
        if self.end_offset is not None:
            function_json["endOffset"] = self.end_offset
        if self.offset_unit is not None:
            function_json["offsetUnit"] = self.offset_unit
        if self.start_offset is not None:
            function_json["startOffset"] = self.start_offset
        if self.start_inclusive is not None:
            function_json["startInclusive"] = self.start_inclusive
        if self.start is not None:
            function_json["start"] = self.start
        if self.time_zone is not None:
            function_json["timeZone"] = self.time_zone
        if self.end is not None:
            function_json["end"] = self.end
        if self.end_inclusive is not None:
            function_json["endInclusive"] = self.end_inclusive
        if self.start_fully_contained is not None:
            function_json["startFullyContained"] = self.start_fully_contained
        if self.time_unit is not None:
            function_json["timeUnit"] = self.time_unit
        return function_json


class AdaptedPredicate(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.predicate.AdaptedPredicate"

    def __init__(
        self,
        predicate: typing.Optional[Predicate] = None,
        input_adapter: typing.Optional[Function] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.predicate = predicate
        self.input_adapter = input_adapter

    def to_json(self):
        function_json = super().to_json()
        if self.predicate is not None:
            function_json["predicate"] = self.predicate
        if self.input_adapter is not None:
            function_json["inputAdapter"] = self.input_adapter
        return function_json


class PredicateComposite(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.predicate.PredicateComposite"

    def __init__(
        self,
        predicates: typing.Optional[typing.List[typing.Any]] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.predicates = predicates

    def to_json(self):
        function_json = super().to_json()
        if self.predicates is not None:
            function_json["predicates"] = self.predicates
        return function_json


class PredicateMap(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.predicate.PredicateMap"

    def __init__(
        self,
        predicate: typing.Optional[Predicate] = None,
        key: typing.Optional[typing.Any] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.predicate = predicate
        self.key = key

    def to_json(self):
        function_json = super().to_json()
        if self.predicate is not None:
            function_json["predicate"] = self.predicate
        if self.key is not None:
            function_json["key"] = self.key
        return function_json


class IntegerTupleAdaptedPredicate(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.tuple.predicate.IntegerTupleAdaptedPredicate"

    def __init__(
        self,
        predicate: typing.Optional[Predicate] = None,
        input_adapter: typing.Optional[Function] = None,
        selection: typing.Optional[typing.List[int]] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.predicate = predicate
        self.input_adapter = input_adapter
        self.selection = selection

    def to_json(self):
        function_json = super().to_json()
        if self.predicate is not None:
            function_json["predicate"] = self.predicate
        if self.input_adapter is not None:
            function_json["inputAdapter"] = self.input_adapter
        if self.selection is not None:
            function_json["selection"] = self.selection
        return function_json


class TupleAdaptedPredicate(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.tuple.predicate.TupleAdaptedPredicate"

    def __init__(
        self,
        predicate: typing.Optional[Predicate] = None,
        input_adapter: typing.Optional[Function] = None,
        selection: typing.Optional[typing.List[typing.Any]] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.predicate = predicate
        self.input_adapter = input_adapter
        self.selection = selection

    def to_json(self):
        function_json = super().to_json()
        if self.predicate is not None:
            function_json["predicate"] = self.predicate
        if self.input_adapter is not None:
            function_json["inputAdapter"] = self.input_adapter
        if self.selection is not None:
            function_json["selection"] = self.selection
        return function_json


class TupleAdaptedPredicateComposite(AbstractPredicate):
    CLASS = "uk.gov.gchq.koryphe.tuple.predicate.TupleAdaptedPredicateComposite"

    def __init__(
        self,
        predicates: typing.Optional[typing.List[typing.Any]] = None,
    ):
        super().__init__(_class_name=self.CLASS)
        self.predicates = predicates

    def to_json(self):
        function_json = super().to_json()
        if self.predicates is not None:
            function_json["predicates"] = self.predicates
        return function_json
