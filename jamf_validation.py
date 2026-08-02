# Copyright (c) 2026 Splunk Inc.
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
"""Validation helpers for Jamf API identifiers."""

from urllib.parse import quote


def quote_username(value: object) -> str:
    """Quote a username while rejecting path-normalization segments."""
    username = str(value)
    if username in {".", ".."}:
        raise ValueError("Invalid username: exact dot segments are not allowed")
    return quote(username, safe="")
