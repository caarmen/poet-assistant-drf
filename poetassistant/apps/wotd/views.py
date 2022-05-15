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
Wotd view module
"""
from datetime import datetime

from django.utils.encoding import force_str
from rest_framework.exceptions import ValidationError
from rest_framework.filters import BaseFilterBackend
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from poetassistant.apps.wotd.serializers import WotdSerializer
from poetassistant.apps.wotd.service import WotdService


class WotdFilterBackend(BaseFilterBackend):
    """
    Defines search filters for the wotd
    """

    def get_schema_operation_parameters(self, view):
        return [
            {
                'name': 'size',
                'required': False,
                'in': 'query',
                'description': force_str('The number of words of the day'),
                'schema': {
                    'type': 'int',
                },
            },
            {
                'name': 'before',
                'required': False,
                'in': 'query',
                'description':
                    force_str('Return words of the day prior to and including this date'),
                'schema': {
                    'type': 'date',
                },
            },
        ]

    def filter_queryset(self, request, queryset, view):
        return queryset


class WotdSet(GenericViewSet):
    """
    View set to list rhyme entries
    """
    pagination_class = None
    filter_backends = [WotdFilterBackend]
    serializer_class = WotdSerializer

    _default_page_size_value = 1
    _service = WotdService()

    def list(self, request, format=None):
        """
        :returns: a response containing the list of words of the day
        """
        wotd_list = self.get_queryset()
        serializer = super().get_serializer(wotd_list, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        return self._service.get_wotd_list(self._get_before(), self._get_page_size())

    def _default_before_value(self):
        return datetime.utcnow().date()

    def _get_page_size(self):
        param_size = self.request.query_params.get("size", None)
        try:
            return self._default_page_size_value if param_size is None else int(param_size)
        except ValueError:
            raise ValidationError(f"Invalid value {param_size} for size")

    def _get_before(self):
        param_before = self.request.query_params.get("before", None)
        try:
            return self._default_before_value() if param_before is None \
                else datetime.fromisoformat(param_before).date()
        except ValueError:
            raise ValidationError(f"Invalid value {param_before} for before")
