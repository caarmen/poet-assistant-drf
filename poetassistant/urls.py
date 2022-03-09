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
"""poetassistant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view

from poetassistant.apps.definitions.views import DefinitionSet
from poetassistant.apps.rhymes.views import RhymeSet
from poetassistant.apps.thesaurus.views import ThesaurusEntrySet

schema_view = get_schema_view(title="Poet Assistant API")

router = routers.DefaultRouter()
router.register(r'rhymes', RhymeSet, "rhymes")
router.register(r'thesaurus', ThesaurusEntrySet, "thesaurus")
router.register(r'definitions', DefinitionSet, "definitions")

urlpatterns = [
    path('', include(router.urls)),
    path('schema', schema_view)
]
