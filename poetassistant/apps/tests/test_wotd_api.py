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
Test that we find the expected wotd entries
"""
import datetime
from http import HTTPStatus

import pytest
from rest_framework.test import APIClient

from poetassistant.apps.wotd.serializers import WotdSerializer
from poetassistant.apps.wotd.service import WotdEntry


@pytest.mark.django_db(databases=["poet_assistant"])
class TestWotdApi:
    """
    Test that we find the expected wotd entries
    """

    def test_wotd_today_ok(self):
        """
        Verify that we have a wotd for today
        """
        response = APIClient().get("/wotd/")
        assert response.status_code == HTTPStatus.OK
        json = response.json()
        serializer = WotdSerializer(data=json, many=True)
        assert serializer.is_valid()
        actual_list = serializer.validated_data
        assert len(actual_list) == 1
        actual_wotd = actual_list[0]
        assert isinstance(actual_wotd, WotdEntry)
        assert actual_wotd.date is not None
        assert actual_wotd.word is not None

    def test_wotd_specific_date_list_ok(self):
        """
        For a query requesting 3 days ending 2021-11-22:
        Here's a snippet of a few days of words:
        2021-11-23: cytokinesis (shouldn't be included)
        2021-11-22: airfield
        2021-11-21: teem
        2021-11-20: traitorous
        2021-11-19: unplug (shouldn't be included)
        """

        response = APIClient().get("/wotd/?before=2021-11-22&size=3")
        assert response.status_code == HTTPStatus.OK
        json = response.json()
        expected_list = [
            WotdEntry(date=datetime.date(2021, 11, 22), word="airfield"),
            WotdEntry(date=datetime.date(2021, 11, 21), word="teem"),
            WotdEntry(date=datetime.date(2021, 11, 20), word="traitorous"),
        ]
        serializer = WotdSerializer(data=json, many=True)
        assert serializer.is_valid()

        actual_list = serializer.validated_data
        assert actual_list == expected_list

    def test_wotd_specific_date_one_item_ok(self):
        """
        Verify that we have the expected single wotd for a single date.
        """
        response = APIClient().get("/wotd/?before=2021-11-21")
        assert response.status_code == HTTPStatus.OK
        json = response.json()
        expected_wotd = WotdEntry(date=datetime.date(2021, 11, 21), word="teem")
        serializer = WotdSerializer(data=json, many=True)
        assert serializer.is_valid()

        actual_list = serializer.validated_data
        assert len(actual_list) == 1
        assert actual_list[0] == expected_wotd

    def test_wotd_too_big_page_size(self):
        """
        Verify that we can't request pages that are too big
        """
        response = APIClient().get("/wotd/?size=500")
        assert response.status_code == HTTPStatus.BAD_REQUEST

    def test_wotd_zero_big_page_size(self):
        """
        Verify that we can't request pages that are too big
        """
        response = APIClient().get("/wotd/?size=0")
        assert response.status_code == HTTPStatus.BAD_REQUEST

    def test_wotd_negative_big_page_size(self):
        """
        Verify that we can't request pages that are too big
        """
        response = APIClient().get("/wotd/?size=-1")
        assert response.status_code == HTTPStatus.BAD_REQUEST
