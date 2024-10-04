#!/bin/bash
# Copyright 2024 Crown Copyright
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

if [ -z "${1}" ]; then
  echo "Missing version argument"
  exit 1
fi

# Upadate all the init python files
while read -r FILE
do
  sed -ri "s/(^__version__ = \")(.*)/\1${1}\"/" "${FILE}"
done < <(find . -type f -name "__init__.py")

# Update the docs
sed -ri "s/(^release = \")(.*)/\1${1}\"/" docs/source/conf.py
