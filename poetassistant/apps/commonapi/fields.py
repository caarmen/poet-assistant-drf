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
Part of speech enum
"""

from enum import Enum

from rest_framework.fields import ChoiceField


class PartOfSpeech(str, Enum):
    """
    Part of speech enum
    """

    NOUN = "noun"
    VERB = "verb"
    ADJECTIVE = "adjective"
    ADVERB = "adverb"
    UNKNOWN = "unknown"


# pylint: disable=abstract-method
class PartOfSpeechField(ChoiceField):
    """
    Serialize a part of speech field from the model to the common PartOfSpeech enum
    """

    def __init__(
        self,
        noun_value: str,
        verb_value: str,
        adjective_value: str,
        adverb_value: str,
        **kwargs,
    ):
        super().__init__(choices=[e.value for e in PartOfSpeech], **kwargs)
        self._model_to_api_part_of_speech = {
            noun_value: PartOfSpeech.NOUN,
            verb_value: PartOfSpeech.VERB,
            adjective_value: PartOfSpeech.ADJECTIVE,
            adverb_value: PartOfSpeech.ADVERB,
        }

    def to_representation(self, value) -> PartOfSpeech:
        """
        Map the part of speech from the model to the common api enum
        """
        return self._model_to_api_part_of_speech.get(value, PartOfSpeech.UNKNOWN)
