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
Port the java implementation of Random.nextInt() using a seed.
This is so we have the same words of the day across the different platforms (android, iOS, ...)
We also ported the java version to the iOS app:
https://github.com/caarmen/poet-assistant-ios/blob/master/PoetAssistantLexiconsFramework/src/wotd/Random.swift
One of the java implementations (for Android):
https://android.googlesource.com/platform/libcore.git/+/refs/heads/marshmallow-mr3-release/luni/src/main/java/java/util/Random.java
"""

class Random:
    """
    Random number generator
    """
    _seed = 0
    _multiplier = 0x5deece66d

    def set_seed(self, input_seed):
        """
        Set the seed for the generation of random numbers
        """
        self._seed = self._create_seed(input_seed)

    @classmethod
    def _create_seed(cls, input_seed):
        return (input_seed ^ cls._multiplier) & ((1 << 48) - 1)

    def next_int(self, upper_bound):
        """
        :returns: a random int between 0 and upper_bound, exclusive
        :rtype: int
        """
        if (upper_bound & -upper_bound) == upper_bound:
            return self._next(31)
        bits = self._next(31)
        val = bits % upper_bound
        while bits - val + (upper_bound - 1) < 0:
            bits = self._next(31)
            val = bits % upper_bound

        return val

    def _next(self, bits):
        self._seed = (self._seed * self._multiplier + 0xb) & ((1 << 48) - 1)
        return self._seed >> (48 - bits)
