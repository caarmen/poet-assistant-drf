# Copyright (c) 2022 - present Carmen Alvarez
#
# This file is part of Poet Assistant.
#
# Poet Assistant is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Poet Assistant is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Poet Assistant.  If not, see <http://www.gnu.org/licenses/>.
"""
Test our wotd serialization/deserialization
"""

from datetime import date

from poetassistant.apps.wotd.serializers import WotdSerializer
from poetassistant.apps.wotd.service import WotdEntry


class TestWotdSerializer:
    """
    Test our wotd serialization/deserialization
    """

    def test_serialization(self):
        """
        Verify we can serialize a WotdEntry
        """
        before = WotdEntry(date=date(2022, 10, 15), word="hello")
        expected_after = {
            "date": "2022-10-15",
            "word": "hello",
        }
        actual_after = WotdSerializer(before).data
        assert actual_after == expected_after

    def test_deserialization(self):
        """
        Verify we can deserialize a WotdEntry
        """
        before = {
            "date": "1999-03-26",
            "word": "long time ago",
        }
        expected_after = WotdEntry(date=date(1999, 3, 26), word="long time ago")
        serializer = WotdSerializer(data=before)
        assert serializer.is_valid()
        actual_after = serializer.validated_data
        assert actual_after == expected_after
