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
import unittest

from jamf_validation import quote_username


class QuoteUsernameTests(unittest.TestCase):
    def test_quotes_path_delimiters(self):
        self.assertEqual(quote_username("team/user@example.com"), "team%2Fuser%40example.com")

    def test_rejects_exact_dot_segments(self):
        for username in (".", ".."):
            with self.subTest(username=username), self.assertRaises(ValueError):
                quote_username(username)


if __name__ == "__main__":
    unittest.main()
