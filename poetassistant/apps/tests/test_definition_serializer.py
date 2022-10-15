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
Test our definition serialization/deserialization
"""
from poetassistant.apps.definitions.models import Dictionary
from poetassistant.apps.definitions.serializers import DictionarySerializer


class TestDefinitionSerializer:
    """
    Test our definition serialization/deserialization
    """

    def test_serialization(self):
        """
        Verify we can serialize a definition
        """
        definition_entry = Dictionary(
            word="test",
            part_of_speech=Dictionary.VERB,
            definition="to write unit tests",
        )
        expected_after = {
            "part_of_speech": "verb",
            "definition": "to write unit tests",
        }
        actual_after = DictionarySerializer(definition_entry).data
        assert actual_after == expected_after

    def test_deserialization(self):
        """
        Verify we can deserialize a definition
        """
        before = {
            "part_of_speech": "noun",
            "definition": "this is where we're here now",
        }
        serializer = DictionarySerializer(data=before)
        assert serializer.is_valid()
        actual_after = serializer.validated_data
        assert actual_after.part_of_speech == Dictionary.NOUN
        assert actual_after.definition == "this is where we're here now"
