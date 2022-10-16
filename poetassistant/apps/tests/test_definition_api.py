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
Test that we find the expected definitions
"""
from http import HTTPStatus

import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db(databases=["poet_assistant"])
class TestDefinitionApi:
    """
    Test that we find the expected definitions
    """

    def test_definitions_ok(self):
        """
        Verify that we have expected definitions
        """
        response = APIClient().get("/definitions/?word=dwindling")
        assert response.status_code == HTTPStatus.OK
        json = response.json()
        results = json["results"]
        assert len(results) == 2
        assert results == [
            {
                "part_of_speech": "adjective",
                "definition": "gradually decreasing until little remains",
            },
            {"part_of_speech": "noun", "definition": "a becoming gradually less"},
        ]

    def test_definition_not_found(self):
        """
        Verify that we have an expected error if no entry is found
        """
        response = APIClient().get("/definitions/?word=qsdfqsdqf")
        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_definition_empty_parameter(self):
        """
        Verify that we have an expected error if no entry is found
        """
        response = APIClient().get("/definitions/?word=")
        assert response.status_code == HTTPStatus.BAD_REQUEST

    def test_definition_missing_parameter(self):
        """
        Verify that we have an expected error if no entry is found
        """
        response = APIClient().get("/definitions/")
        assert response.status_code == HTTPStatus.BAD_REQUEST
