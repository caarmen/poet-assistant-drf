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
Test that we find the expected thesaurus entries
"""
from http import HTTPStatus

import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db(databases=["poet_assistant"])
class TestThesaurusApi:
    """
    Test that we find the expected thesaurus entries
    """

    def test_thesaurus_ok(self):
        """
        Verify that we have expected thesaurus entries
        """
        response = APIClient().get("/thesaurus/?word=abbreviate")
        assert response.status_code == HTTPStatus.OK
        json = response.json()
        assert json["results"] == [
            {
                "part_of_speech": "verb",
                "synonyms": ["reduce"],
                "antonyms": [],
            },
            {
                "part_of_speech": "verb",
                "synonyms": [
                    "reduce",
                    "cut",
                    "abridge",
                    "contract",
                    "decrease",
                    "minify",
                    "lessen",
                    "shorten",
                    "foreshorten",
                ],
                "antonyms": ["expand"],
            },
        ]

    def test_thesaurus_not_found(self):
        """
        Verify that we have an expected error if no entry is found
        """
        response = APIClient().get("/thesaurus/?word=blahblahblah")
        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_thesaurus_empty_parameter(self):
        """
        Verify that we have an expected error if no entry is found
        """
        response = APIClient().get("/thesaurus/?word=")
        assert response.status_code == HTTPStatus.BAD_REQUEST

    def test_thesaurus_missing_parameter(self):
        """
        Verify that we have an expected error if no entry is found
        """
        response = APIClient().get("/thesaurus/")
        assert response.status_code == HTTPStatus.BAD_REQUEST
