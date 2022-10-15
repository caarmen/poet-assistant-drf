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
Test that we find the expected wotd entries
"""
import datetime

import pytest

from poetassistant.apps.wotd.service import get_wotd_list, WotdEntry


@pytest.mark.django_db(databases=["poet_assistant"])
class TestWotdService:
    """
    Test that we find the expected wotd entries
    """

    # pylint: disable=too-many-statements
    def test_single_word(self):
        """
        Check for a variety of individual wotd entries.
        The expected words come from the wotd test of the iOS app:
         https://github.com/caarmen/poet-assistant-ios/blob/master/PoetAssistantTests/WotdTest.swift
        """
        _test_wotd("2018-11-24", "vaccinate")
        _test_wotd("2018-11-23", "devaluation")
        _test_wotd("2018-11-22", "copulation")
        _test_wotd("2018-11-21", "fuselage")
        _test_wotd("2018-11-20", "lyricist")
        _test_wotd("2018-11-19", "emphysema")
        _test_wotd("2018-11-18", "auscultation")
        _test_wotd("2018-11-17", "hypotonia")
        _test_wotd("2018-11-16", "brigadier")
        _test_wotd("2018-11-15", "gallstone")
        _test_wotd("2018-11-14", "unspoilt")
        _test_wotd("2018-11-13", "sprayer")
        _test_wotd("2018-11-12", "tufa")
        _test_wotd("2018-11-11", "braised")
        _test_wotd("2018-11-10", "unselfishly")
        _test_wotd("2018-11-09", "economise")
        _test_wotd("2018-11-08", "navel")
        _test_wotd("2018-11-07", "rhombus")
        _test_wotd("2018-11-06", "swinish")
        _test_wotd("2018-11-05", "offshoot")
        _test_wotd("2018-11-04", "personation")
        _test_wotd("2018-11-03", "sorrowing")
        _test_wotd("2018-11-02", "leasehold")
        _test_wotd("2018-11-01", "blowout")
        _test_wotd("2018-10-31", "dropout")
        _test_wotd("2018-10-30", "interrogatively")
        _test_wotd("2018-10-29", "indelible")
        _test_wotd("2018-10-28", "sprit")
        _test_wotd("2018-10-27", "semiotic")
        _test_wotd("2018-10-26", "normalisation")
        _test_wotd("2018-10-25", "overladen")
        _test_wotd("2018-10-24", "deist")
        _test_wotd("2018-10-23", "silviculture")
        _test_wotd("2018-10-22", "heathenism")
        _test_wotd("2018-10-21", "divisive")
        _test_wotd("2018-10-20", "unripe")
        _test_wotd("2018-10-19", "soviet")
        _test_wotd("2018-10-18", "napped")
        _test_wotd("2018-10-17", "minder")
        _test_wotd("2018-10-16", "heighten")
        _test_wotd("2018-10-15", "karat")
        _test_wotd("2018-10-14", "phosphorous")
        _test_wotd("2018-10-13", "firearm")
        _test_wotd("2018-10-12", "hypotenuse")
        _test_wotd("2018-10-11", "boldface")
        _test_wotd("2018-10-10", "recapitulate")
        _test_wotd("2018-10-09", "alchemist")
        _test_wotd("2018-10-08", "abrogate")
        _test_wotd("2018-10-07", "binnacle")
        _test_wotd("2018-10-06", "unimpressive")
        _test_wotd("2018-10-05", "insanitary")
        _test_wotd("2018-10-04", "friday")
        _test_wotd("2018-10-03", "ancestress")
        _test_wotd("2018-10-02", "badminton")
        _test_wotd("2018-10-01", "bioremediation")
        _test_wotd("2018-09-30", "servo")
        _test_wotd("2018-09-29", "mobilisation")
        _test_wotd("2018-09-28", "taproot")
        _test_wotd("2018-09-27", "relinquishing")
        _test_wotd("2018-09-26", "creosote")
        _test_wotd("2018-09-25", "autograph")
        _test_wotd("2018-09-24", "catechetical")
        _test_wotd("2018-09-23", "jib")
        _test_wotd("2018-09-22", "protraction")
        _test_wotd("2018-09-21", "ambit")
        _test_wotd("2018-09-20", "panchayat")
        _test_wotd("2018-09-19", "deb")
        _test_wotd("2018-09-18", "territorially")
        _test_wotd("2018-09-17", "hart")
        _test_wotd("2018-09-16", "downtrodden")
        _test_wotd("2018-09-15", "prolapse")
        _test_wotd("2018-09-14", "metaphysically")
        _test_wotd("2018-09-13", "substratum")
        _test_wotd("2018-09-12", "adroitly")
        _test_wotd("2018-09-11", "isi")
        _test_wotd("2018-09-10", "yardarm")
        _test_wotd("2018-09-09", "pullout")
        _test_wotd("2018-09-08", "computationally")
        _test_wotd("2018-09-07", "schoolyard")
        _test_wotd("2018-09-06", "advisedly")
        _test_wotd("2018-09-05", "maxillofacial")
        _test_wotd("2018-09-04", "belike")
        _test_wotd("2018-09-03", "storyteller")
        _test_wotd("2018-09-02", "blip")
        _test_wotd("2018-09-01", "colorist")
        _test_wotd("2018-08-31", "scythe")
        _test_wotd("2018-08-30", "timbered")
        _test_wotd("2018-08-29", "overspread")
        _test_wotd("2018-08-28", "succinct")
        _test_wotd("2018-08-27", "masochistic")
        _test_wotd("2018-08-26", "maltreatment")
        _test_wotd("2018-08-25", "dampen")
        _test_wotd("2018-08-24", "bichromate")
        _test_wotd("2018-08-23", "subluxation")
        _test_wotd("2018-08-22", "prodigiously")
        _test_wotd("2018-08-21", "superficiality")
        _test_wotd("2018-08-20", "territorially")
        _test_wotd("2018-08-19", "unconstrained")
        _test_wotd("2018-08-18", "literati")
        _test_wotd("2018-08-17", "dispossessed")

    def test_list_wotd(self):
        """
        Check for an expected list of wotd entries
        """
        date = datetime.datetime(year=2021, month=11, day=28)
        expected_wotd_list = [
            WotdEntry(date=datetime.date(2021, 11, 28), word="clothesline"),
            WotdEntry(date=datetime.date(2021, 11, 27), word="solstice"),
            WotdEntry(date=datetime.date(2021, 11, 26), word="methylphenidate"),
        ]
        actual_wotd_list = get_wotd_list(date, 3)
        assert actual_wotd_list == expected_wotd_list


def _test_wotd(date_str: str, expected_word: str):
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    actual_wotds = get_wotd_list(date, 1)
    assert len(actual_wotds) == 1
    actual_wotd = actual_wotds[0]
    assert actual_wotd.date == date
    assert actual_wotd.word == expected_word
