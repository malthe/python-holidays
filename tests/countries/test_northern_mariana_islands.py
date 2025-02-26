#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import unittest
from datetime import date

import holidays
from holidays.constants import MAR


class TestMP(unittest.TestCase):
    # Testing the stub for a US subdivision that is also officially assigned
    # its own country code in ISO 3166-1. The actual holidays are generated by
    # the US Class and tested there.
    def setUp(self):
        self.holidays = holidays.HolidaysMP()

    def test_MP_only(self):
        """Check for a holiday that is not returned by US unless the
        subdivision is specified."""
        self.assertIn(
            "Commonwealth Covenant Day",
            self.holidays.get_list(date(2022, MAR, 24)),
        )

    def test_aliases(self):
        """For coverage purposes"""
        for h in [
            holidays.MP(),
            holidays.MNP(),
            holidays.NorthernMarianaIslands(),
        ]:
            self.assertIsInstance(h, holidays.HolidaysMP)
