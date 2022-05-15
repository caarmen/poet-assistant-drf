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
Rhymes view module
"""
from rest_framework import filters
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from poetassistant.apps.rhymes import service
from poetassistant.apps.rhymes.serializers import RhymesSerializer


class WordSearchFilter(filters.SearchFilter):
    """
    Filter to search by word
    """
    search_param = "word"


class RhymeSet(ListModelMixin,
               GenericViewSet):
    """
    View set to list rhyme entries
    """
    serializer_class = RhymesSerializer
    filter_backends = [WordSearchFilter]
    search_fields = ['=word']

    def _get_search_word(self):
        return self.request.query_params.get(WordSearchFilter.search_param, None)

    def _create_queryset(self):
        return service.create_queryset(self._get_search_word())

    def get_queryset(self):
        return self._create_queryset()

    def filter_queryset(self, queryset):
        return self._create_queryset()
