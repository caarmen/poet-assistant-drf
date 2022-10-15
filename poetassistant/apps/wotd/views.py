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
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from poetassistant.apps.wotd import service
from poetassistant.apps.wotd.serializers import WotdSerializer, WotdParamsSerializer


class WotdSet(GenericViewSet):
    """
    View set to list words of the day
    """

    pagination_class = None
    serializer_class = WotdSerializer

    # pylint: disable=unused-argument
    # noinspection PyUnusedLocal
    @extend_schema(parameters=[WotdParamsSerializer])
    def list(self, request):
        """
        :returns: a response containing the list of words of the day
        """
        wotd_list = self.get_queryset()
        serializer = super().get_serializer(wotd_list, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        filter_serializer = WotdParamsSerializer(data=self.request.query_params)
        filter_serializer.is_valid(raise_exception=True)
        return service.get_wotd_list(
            before_date=filter_serializer.validated_data["before"],
            page_size=filter_serializer.validated_data["size"],
        )
