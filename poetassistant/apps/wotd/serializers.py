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
Wotd serializers
"""
import dataclasses
from datetime import datetime

from rest_framework import serializers

from poetassistant.apps.wotd.service import WotdEntry


# pylint: disable=abstract-method
class WotdSerializer(serializers.Serializer):
    """
    Wotd serializer
    """

    date = serializers.DateField()
    word = serializers.CharField()

    # pylint: disable=too-few-public-methods
    class Meta:
        """
        Wotd serializer metadata
        """

        fields = [f.name for f in dataclasses.fields(WotdEntry)]


def _default_before():
    return datetime.utcnow().date()


# pylint: disable=abstract-method
class WotdParamsSerializer(serializers.Serializer):
    """
    Validation of wotd query params
    """

    size = serializers.IntegerField(
        required=False,
        min_value=1,
        default=1,
        help_text="The number of words of the day",
    )
    before = serializers.DateField(
        required=False,
        default=_default_before,
        help_text="Return words of the day prior to and including this date",
    )
