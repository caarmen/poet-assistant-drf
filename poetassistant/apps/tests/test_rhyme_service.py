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
Test that we find the expected rhymes
"""

import pytest

from poetassistant.apps.rhymes.serializers import RhymesSerializer
from poetassistant.apps.rhymes.service import create_queryset


@pytest.mark.django_db(databases=["poet_assistant"])
# pylint: disable=too-few-public-methods
class TestRhymeService:
    """
    Test that we find the expected rhymes
    """

    def test_rhymes(self):
        """
        Test that we find the expected rhymes
        """
        queryset = create_queryset("booked")
        serializer = RhymesSerializer(list(queryset), many=True)
        actual_rhymes = [dict(rhyme_entry) for rhyme_entry in serializer.data]
        expected_rhymes = [
            {
                "syllables_type": "stress_syllables",
                "syllables": "UHKT",
                "word": "cooked",
            },
            {
                "syllables_type": "stress_syllables",
                "syllables": "UHKT",
                "word": "hooked",
            },
            {
                "syllables_type": "stress_syllables",
                "syllables": "UHKT",
                "word": "looked",
            },
            {
                "syllables_type": "stress_syllables",
                "syllables": "UHKT",
                "word": "overcooked",
            },
            {
                "syllables_type": "stress_syllables",
                "syllables": "UHKT",
                "word": "precooked",
            },
            {
                "syllables_type": "last_syllable",
                "syllables": "UHKT",
                "word": "cooked",
            },
            {
                "syllables_type": "last_syllable",
                "syllables": "UHKT",
                "word": "hooked",
            },
            {
                "syllables_type": "last_syllable",
                "syllables": "UHKT",
                "word": "looked",
            },
            {
                "syllables_type": "last_syllable",
                "syllables": "UHKT",
                "word": "overcooked",
            },
            {
                "syllables_type": "last_syllable",
                "syllables": "UHKT",
                "word": "overlooked",
            },
            {
                "syllables_type": "last_syllable",
                "syllables": "UHKT",
                "word": "precooked",
            },
        ]
        assert actual_rhymes == expected_rhymes
