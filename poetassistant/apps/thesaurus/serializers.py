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
Thesaurus serializers
"""

from rest_framework import serializers

from poetassistant.apps.commonapi.partofspeech import PartOfSpeechField
from poetassistant.apps.thesaurus.models import ThesaurusEntry


class CsvListField(serializers.ListField):
    """
    Serializer which convets a comma-separated string into a list of strings
    """

    def get_attribute(self, instance):
        result = super().get_attribute(instance)
        return [x for x in result.split(",") if x]


class ThesaurusEntrySerializer(serializers.HyperlinkedModelSerializer):
    """
    Thesaurus entry serialzier
    """

    synonyms = CsvListField(child=serializers.CharField())
    antonyms = CsvListField(child=serializers.CharField())
    part_of_speech = PartOfSpeechField(
        noun_value=ThesaurusEntry.NOUN,
        verb_value=ThesaurusEntry.VERB,
        adjective_value=ThesaurusEntry.ADJECTIVE,
        adverb_value=ThesaurusEntry.ADVERB,
        source="word_type",
    )

    # pylint: disable=too-few-public-methods
    class Meta:
        """
        Thesaurus entry serializer meta data
        """

        model = ThesaurusEntry
        fields = ["part_of_speech", "synonyms", "antonyms"]
