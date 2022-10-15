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
Thesaurus models
"""
from django.db import models

from poetassistant.apps.db.dbrouter import DbRouter
from poetassistant.apps.thesaurus import apps


class ThesaurusEntry(models.Model):
    """
    Thesaurus entry model
    """

    ADJECTIVE = "ADJ"
    ADVERB = "ADV"
    NOUN = "NOUN"
    VERB = "VERB"

    # pylint: disable=duplicate-code
    PART_OF_SPEECH_CHOICES = [
        (ADJECTIVE, "Adjective"),
        (ADVERB, "Adverb"),
        (NOUN, "Noun"),
        (VERB, "Verb"),
    ]
    rowid = models.IntegerField(primary_key=True)
    word = models.CharField(max_length=128)
    word_type = models.CharField(max_length=4, choices=PART_OF_SPEECH_CHOICES)
    synonyms = models.CharField(max_length=2860)
    antonyms = models.CharField(max_length=128)

    objects = models.Manager()

    # pylint: disable=too-few-public-methods
    class Meta:
        """
        Thesaurus model meta data
        """

        db_table = "thesaurus"
        app_label = apps.ThesaurusConfig.name


DbRouter.register_model(ThesaurusEntry)
