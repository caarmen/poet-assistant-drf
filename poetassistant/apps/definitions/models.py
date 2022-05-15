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

from poetassistant.apps.commonapi.partofspeech import PartOfSpeech
from poetassistant.apps.definitions import apps


class Dictionary(models.Model):
    """
    Dictionary entry model
    """
    rowid = models.IntegerField(primary_key=True)
    word = models.CharField(max_length=128)
    part_of_speech = models.CharField(max_length=1)
    definition = models.TextField()

    objects = models.Manager()

    def part_of_speech_enum(self):
        """
        :returns: the part of speech of the word
        :rtype: PartOfSpeech
        """
        return {
            'a': PartOfSpeech.ADJECTIVE,
            'r': PartOfSpeech.ADVERB,
            'n': PartOfSpeech.NOUN,
            'v': PartOfSpeech.VERB
        }[self.part_of_speech]

    # pylint: disable=too-few-public-methods
    class Meta:
        """
        Definition model meta data
        """
        db_table = 'dictionary'
        unique_together = ("word", "definition")
        app_label = apps.DefinitionsConfig.name
