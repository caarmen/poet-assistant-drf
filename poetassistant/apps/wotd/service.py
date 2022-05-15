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
Wotd service module
"""
from dataclasses import dataclass
from datetime import datetime, timedelta

from poetassistant.apps.wotd.models import Stem
from poetassistant.apps.wotd.random import Random


@dataclass
class WotdEntry:
    """
    Wotd entry data class
    """
    word: str
    date: datetime.date


# When looking up random words, their "frequency" is a factor in the selection.
# Words which are too frequent (a, the, why) are not interesting words.
# Words which are too rare (aalto) are likely not interesting either.

# Note: we want the words with frequency between 1500 and 25000 exclusive, to
# return the same values as in the android/ios implementations.
_MIN_INTERESTING_FREQUENCY = 1500
_MAX_INTERESTING_FREQUENCY = 25000


def get_wotd_list(before_date, page_size):
    """
    :returns: the list of page_size words of the day before the before_date
    """
    result = []
    for date_position in range(0, page_size):
        date_millis = _get_date_millis(before_date, date_position)
        word = _get_wotd(date_millis)
        date = datetime.fromtimestamp(date_millis / 1000).date().isoformat()
        result.append(WotdEntry(word=word, date=date))
    return result


def _get_wotd(date_millis):
    interesting_stem_entries = Stem.objects.using('poet_assistant').exclude(
        google_ngram_frequency__lte=_MIN_INTERESTING_FREQUENCY).exclude(
        google_ngram_frequency__gte=_MAX_INTERESTING_FREQUENCY)
    db_position = _get_db_position_for_date(date_millis, interesting_stem_entries.count())
    return interesting_stem_entries[db_position].word


def _get_db_position_for_date(date_millis, db_size):
    rnd = Random()
    rnd.set_seed(date_millis)
    return rnd.next_int(db_size)


def _get_date_millis(input_date_midnight, days_before):
    target_date_midnight = input_date_midnight - timedelta(days_before)
    return int(datetime.fromordinal(target_date_midnight.toordinal()).timestamp() * 1000)
