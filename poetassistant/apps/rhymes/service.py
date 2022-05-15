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
Rheymes service module
"""
from poetassistant.apps.rhymes.models import Rhymes


class RhymesService:
    """
    Rhymes service
    """
    _subquery_template = """
        SELECT
          source_word_variants.rowid,
          '{syllables_type}' AS syllables_type,
          source_word_variants.{syllables_type} AS syllables,
          '{syllables_sort_key}' AS syllables_type_sort_key,
          source_word_variants.variant_number,
          rhymes_word_variants.word,
          rhymes_word_variants.has_definition,
          source_word_variants.{syllables_type}
        FROM
          word_variants AS source_word_variants
          JOIN word_variants AS rhymes_word_variants ON source_word_variants.{syllables_type} = rhymes_word_variants.{syllables_type}
          AND source_word_variants.word != rhymes_word_variants.word
        WHERE
          rhymes_word_variants.has_definition = 1
          AND source_word_variants.word = %s
    """

    _union_template = """
        UNION
    """

    _order_by_template = """
        ORDER BY
          syllables_type_sort_key,
          source_word_variants.variant_number,
          rhymes_word_variants.word
    """

    def __init__(self):
        self._full_query_template = self._union_template.join([
            self._create_subquery_template('stress_syllables', '1'),
            self._create_subquery_template('last_three_syllables', '2'),
            self._create_subquery_template('last_two_syllables', '3'),
            self._create_subquery_template('last_syllable', '4'),
        ]) + self._order_by_template

    @staticmethod
    def _create_subquery_template(syllables_type, syllables_sort_key):
        return RhymesService._subquery_template.format(
            **{'syllables_type': syllables_type, 'syllables_sort_key': syllables_sort_key})

    def create_queryset(self, word):
        """
        :returns: a rhymes query set for rhymes of the given word
        """
        return Rhymes.objects.none() if word is None else Rhymes.objects.using('poet_assistant').raw(
            self._full_query_template, [word, word, word, word])
