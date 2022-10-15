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
Pagination customizations
"""
from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination


class NoEmptyPagePaginator(Paginator):
    """
    Paginator which raises an error if the first page is empty
    """

    def __init__(self, object_list, per_page):
        super().__init__(object_list, per_page, allow_empty_first_page=False)


class NoEmptyPagePagination(PageNumberPagination):
    """
    Pagination using NoEmptyPagePaginator
    """

    django_paginator_class = NoEmptyPagePaginator
    page_size_query_param = "page_size"
