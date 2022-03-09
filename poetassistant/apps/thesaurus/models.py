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
from django.db import models

from poetassistant.apps.thesaurus import apps


class ThesaurusEntry(models.Model):
    rowid = models.IntegerField(primary_key=True)
    word = models.CharField(max_length=128)
    word_type = models.CharField(max_length=4)
    synonyms = models.CharField(max_length=2860)
    antonyms = models.CharField(max_length=128)

    objects = models.Manager()

    class Meta:
        db_table = 'thesaurus'
        app_label = apps.ThesaurusConfig.name
