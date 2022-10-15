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
Rhymes serializers
"""
from rest_framework import serializers

from poetassistant.apps.rhymes.models import Rhymes


class RhymesSerializer(serializers.HyperlinkedModelSerializer):
    """
    Rhyme serializer
    """

    syllables_type = serializers.SerializerMethodField()
    syllables = serializers.SerializerMethodField()

    @staticmethod
    def get_syllables_type(obj):
        """
        :returns: the type of syllable match for a rhyme entry
        """
        return obj.syllables_type

    @staticmethod
    def get_syllables(obj):
        """
        :returns: the matching syllables for a rhyme entry
        """
        return obj.syllables

    # pylint: disable=too-few-public-methods
    class Meta:
        """
        Rhyme serializer meta data
        """

        model = Rhymes
        fields = ["syllables_type", "syllables", "word"]
