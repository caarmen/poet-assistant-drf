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
from rest_framework.viewsets import GenericViewSet

from poetassistant.apps.commonapi.pagination import NoEmptyPagePagination
from poetassistant.apps.commonapi.search import RequiredSearchListModelMixin
from poetassistant.apps.definitions.models import Dictionary
from poetassistant.apps.definitions.serializers import DictionarySerializer


class DefinitionSet(RequiredSearchListModelMixin, GenericViewSet):
    """
    View set to list definition entries
    """

    queryset = Dictionary.objects.all().order_by("part_of_speech", "definition")
    pagination_class = NoEmptyPagePagination
    serializer_class = DictionarySerializer
