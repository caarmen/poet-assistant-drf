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
Definitions view module
"""
from rest_framework import filters
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from poetassistant.apps.definitions.models import Dictionary
from poetassistant.apps.definitions.serializers import DictionarySerializer


class WordSearchFilter(filters.SearchFilter):
    """
    Filter to search by word
    """
    search_param = "word"


class DefinitionSet(ListModelMixin, GenericViewSet):
    """
    View set to list definition entries
    """
    queryset = Dictionary.objects.using('poet_assistant').all().order_by('word', 'part_of_speech', 'definition')
    serializer_class = DictionarySerializer
    filter_backends = [WordSearchFilter]
    search_fields = ['=word']
