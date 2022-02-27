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

from rest_framework import serializers

from poetassistant.apps.thesaurus.models.thesaurusentry import ThesaurusEntry


class CsvListField(serializers.ListField):

    def get_attribute(self, instance):
        result = super().get_attribute(instance)
        return [x for x in result.split(',') if x]


class ThesaurusEntrySerializer(serializers.HyperlinkedModelSerializer):
    synonyms = CsvListField(child=serializers.CharField())
    antonyms = CsvListField(child=serializers.CharField())

    class Meta:
        model = ThesaurusEntry
        fields = ['part-of-speech', 'word', 'synonyms', 'antonyms']
        extra_kwargs = {
            'part-of-speech': {'source': 'word_type'}
        }
