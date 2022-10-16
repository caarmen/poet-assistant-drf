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
Test our thesaurus serialization/deserialization
"""

from poetassistant.apps.thesaurus.models import ThesaurusEntry
from poetassistant.apps.thesaurus.serializers import ThesaurusEntrySerializer


class TestThesaurusSerializer:
    """
    Test our thesaurus serialization/deserialization
    """

    def test_serialization(self):
        """
        Verify we can serialize a ThesaurusEntry
        """
        thesaurus_entry = ThesaurusEntry(
            word="test",
            word_type=ThesaurusEntry.NOUN,
            synonyms="attempt,try",
            antonyms="give up",
        )
        expected_after = {
            "part_of_speech": "noun",
            "synonyms": ["attempt", "try"],
            "antonyms": ["give up"],
        }
        actual_after = ThesaurusEntrySerializer(thesaurus_entry).data
        assert actual_after == expected_after

    def test_deserialization(self):
        """
        Verify we can deserialize a ThesaurusEntry
        """
        before = {
            "part_of_speech": "noun",
            "synonyms": ["attempt", "try"],
            "antonyms": ["give up"],
        }
        serializer = ThesaurusEntrySerializer(data=before)
        assert serializer.is_valid()
        actual_after = serializer.validated_data
        assert actual_after.word_type == ThesaurusEntry.NOUN
        assert actual_after.synonyms == "attempt,try"
        assert actual_after.antonyms == "give up"

    def test_serialization_empty_antonyms(self):
        """
        Verify we can serialize a ThesaurusEntry having no antonyms
        """
        thesaurus_entry = ThesaurusEntry(
            word="test",
            word_type=ThesaurusEntry.NOUN,
            synonyms="attempt,try",
            antonyms="",
        )
        expected_after = {
            "part_of_speech": "noun",
            "synonyms": ["attempt", "try"],
            "antonyms": [],
        }
        actual_after = ThesaurusEntrySerializer(thesaurus_entry).data
        assert actual_after == expected_after

    def test_deserialization_empty_antonyms(self):
        """
        Verify we can deserialize a ThesaurusEntry having no antonyms
        """
        before = {
            "part_of_speech": "noun",
            "synonyms": ["attempt", "try"],
            "antonyms": [],
        }
        serializer = ThesaurusEntrySerializer(data=before)
        assert serializer.is_valid()
        actual_after = serializer.validated_data
        assert actual_after.word_type == ThesaurusEntry.NOUN
        assert actual_after.synonyms == "attempt,try"
        assert actual_after.antonyms == ""

    def test_serialization_empty_synonyms(self):
        """
        Verify we can serialize a ThesaurusEntry having no synonyms
        """
        thesaurus_entry = ThesaurusEntry(
            word="test",
            word_type=ThesaurusEntry.NOUN,
            synonyms="",
            antonyms="give up",
        )
        expected_after = {
            "part_of_speech": "noun",
            "synonyms": [],
            "antonyms": ["give up"],
        }
        actual_after = ThesaurusEntrySerializer(thesaurus_entry).data
        assert actual_after == expected_after

    def test_deserialization_empty_synonyms(self):
        """
        Verify we can deserialize a ThesaurusEntry having no synonyms
        """
        before = {
            "part_of_speech": "noun",
            "synonyms": [],
            "antonyms": ["give up"],
        }
        serializer = ThesaurusEntrySerializer(data=before)
        assert serializer.is_valid()
        actual_after = serializer.validated_data
        assert actual_after.word_type == ThesaurusEntry.NOUN
        assert actual_after.synonyms == ""
        assert actual_after.antonyms == "give up"
