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
Definitions models
"""
from django.db import models

from poetassistant.apps.db.dbrouter import DbRouter
from poetassistant.apps.definitions import apps


class Dictionary(models.Model):
    """
    Dictionary entry model
    """

    ADJECTIVE = "a"
    ADVERB = "r"
    NOUN = "n"
    VERB = "v"

    # pylint: disable=duplicate-code
    PART_OF_SPEECH_CHOICES = [
        (ADJECTIVE, "Adjective"),
        (ADVERB, "Adverb"),
        (NOUN, "Noun"),
        (VERB, "Verb"),
    ]

    rowid = models.IntegerField(primary_key=True)
    word = models.CharField(max_length=128)
    part_of_speech = models.CharField(max_length=1, choices=PART_OF_SPEECH_CHOICES)
    definition = models.TextField()

    objects = models.Manager()

    # pylint: disable=too-few-public-methods
    class Meta:
        """
        Definition model meta data
        """

        db_table = "dictionary"
        unique_together = ("word", "definition")
        app_label = apps.DefinitionsConfig.name


DbRouter.register_model(Dictionary)
