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
from http import HTTPStatus

import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db(databases=["poet_assistant"])
class TestRhymesApi:
    """
    Test that we find the expected rhymes
    """

    def test_rhymes_ok(self):
        """
        Verify that we have expected rhymes
        """
        response = APIClient().get("/rhymes/?word=heart&page_size=100")
        assert response.status_code == HTTPStatus.OK
        json = response.json()
        results = json["results"]
        assert len(results) == 61
        assert results[0] == {
            "syllables_type": "stress_syllables",
            "syllables": "AART",
            "word": "apart",
        }
        assert results[21] == {
            "syllables_type": "stress_syllables",
            "syllables": "AART",
            "word": "tarte",
        }
        assert results[22] == {
            "syllables_type": "last_syllable",
            "syllables": "AART",
            "word": "apart",
        }
        assert results[60] == {
            "syllables_type": "last_syllable",
            "syllables": "AART",
            "word": "upstart",
        }

    def test_rhyme_not_found(self):
        """
        Verify that we have an expected error if no entry is found
        """
        response = APIClient().get("/rhymes/?word=nothinghere")
        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_rhyme_empty_parameter(self):
        """
        Verify that we have an expected error if no entry is found
        """
        response = APIClient().get("/rhymes/?word=")
        assert response.status_code == HTTPStatus.BAD_REQUEST

    def test_rhymes_missing_parameter(self):
        """
        Verify that we have an expected error if no entry is found
        """
        response = APIClient().get("/rhymes/")
        assert response.status_code == HTTPStatus.BAD_REQUEST
