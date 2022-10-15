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
Definitions serializers
"""
from rest_framework import serializers

from poetassistant.apps.commonapi.fields import PartOfSpeechField
from poetassistant.apps.definitions.models import Dictionary


# pylint: disable=too-few-public-methods
class DictionarySerializer(serializers.HyperlinkedModelSerializer):
    """
    Definition entry serializer
    """

    part_of_speech = PartOfSpeechField(
        noun_value=Dictionary.NOUN,
        verb_value=Dictionary.VERB,
        adjective_value=Dictionary.ADJECTIVE,
        adverb_value=Dictionary.ADVERB,
    )

    class Meta:
        """
        Definition serializer meta data
        """

        model = Dictionary
        fields = ["part_of_speech", "definition"]
