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
Custom search filter
"""
from drf_spectacular.utils import extend_schema
from rest_framework import serializers
from rest_framework.mixins import ListModelMixin


# pylint: disable=abstract-method
class SearchParamSerializer(serializers.Serializer):
    """
    Validation of search query param
    """

    word = serializers.CharField(
        required=True,
        help_text="The word to look up",
    )


class RequiredSearchListModelMixin(ListModelMixin):
    """
    Require the "word" search query param
    """

    @extend_schema(parameters=[SearchParamSerializer])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def filter_queryset(self, queryset):
        """
        Filter the queryset with the search param
        """
        search_word = self.get_search_word()
        queryset = super().filter_queryset(queryset)
        return queryset.filter(word=search_word)

    def get_search_word(self):
        """
        Get the search word from the query params
        """
        params_serializer = SearchParamSerializer(data=self.request.query_params)
        params_serializer.is_valid(raise_exception=True)
        return params_serializer.validated_data.get("word")
