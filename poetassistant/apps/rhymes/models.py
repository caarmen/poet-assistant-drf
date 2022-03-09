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

from poetassistant.apps.rhymes import apps


class Rhymes(models.Model):
    rowid = models.IntegerField(primary_key=True)
    word = models.CharField(max_length=34)
    variant_number = models.IntegerField()
    stress_syllables = models.CharField(max_length=24)
    last_three_syllables = models.CharField(16)
    last_two_syllables = models.CharField(12)
    last_syllable = models.CharField(8)
    has_definition = models.IntegerField()

    objects = models.Manager()

    class Meta:
        db_table = 'word_variants'
        unique_together = ("word", "variant_number")
        app_label = apps.RhymesConfig.name
