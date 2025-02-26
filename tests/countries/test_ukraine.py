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

from holidays.countries.ukraine import Ukraine, UA, UKR
from tests.common import TestCase


class TestUkraine(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Ukraine)

    def test_country_aliases(self):
        self.assertCountryAliases(Ukraine, UA, UKR)

    def test_no_holidays(self):
        self.assertNoHolidays(Ukraine(years=1917))

    def test_new_year_day(self):
        self.assertHoliday(f"{year}-01-01" for year in range(1918, 1930))
        self.assertNoHoliday(f"{year}-01-01" for year in range(1930, 1948))
        self.assertNoHolidayName("Новий рік", Ukraine(years=range(1930, 1948)))
        self.assertHoliday(f"{year}-01-01" for year in range(1948, 2050))

        dt = (
            "2011-01-03",
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_christmas_julian_day(self):
        self.assertNoHoliday(f"{year}-01-07" for year in range(1918, 1991))
        self.assertNoHolidayName(
            "Різдво Христове (за юліанським календарем)",
            Ukraine(years=range(1918, 1991)),
        )
        self.assertHoliday(f"{year}-01-07" for year in range(1991, 2050))

        dt = (
            "2012-01-09",
            "2017-01-09",
            "2018-01-08",
            "2023-01-09",
            "2024-01-08",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_womens_day(self):
        self.assertNoHoliday(f"{year}-03-08" for year in range(1918, 1966))
        self.assertNoHolidayName(
            "Міжнародний жіночий день", Ukraine(years=range(1918, 1966))
        )
        self.assertHoliday(f"{year}-03-08" for year in range(1966, 2050))

        dt = (
            "2014-03-10",
            "2015-03-09",
            "2020-03-09",
            "2025-03-10",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_easter(self):
        name = "Великдень (Пасха)"
        self.assertNoHolidayName(name, Ukraine(years=range(1918, 1991)))

        self.assertHolidaysName(
            name,
            "2010-04-04",
            "2011-04-24",
            "2012-04-15",
            "2013-05-05",
            "2014-04-20",
            "2015-04-12",
            "2016-05-01",
            "2017-04-16",
            "2018-04-08",
            "2019-04-28",
            "2020-04-19",
            "2021-05-02",
            "2022-04-24",
            "2023-04-16",
        )

        dt = (
            "2010-04-05",
            "2011-04-25",
            "2012-04-16",
            "2013-05-06",
            "2014-04-21",
            "2015-04-13",
            "2016-05-03",
            "2017-04-17",
            "2018-04-09",
            "2019-04-29",
            "2020-04-20",
            "2021-05-04",
            "2022-04-25",
            "2023-04-17",
            # special cases
            "2000-05-03",
            "2005-05-03",
            "2027-05-04",
            "2032-05-04",
            "2062-05-02",
            "2073-05-02",
            "2078-05-10",
            "2084-05-02",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_trinity(self):
        name = "Трійця"
        self.assertNoHolidayName(name, Ukraine(years=range(1918, 1991)))

        self.assertHolidaysName(
            name,
            "2010-05-23",
            "2011-06-12",
            "2012-06-03",
            "2013-06-23",
            "2014-06-08",
            "2015-05-31",
            "2016-06-19",
            "2017-06-04",
            "2018-05-27",
            "2019-06-16",
            "2020-06-07",
            "2021-06-20",
            "2022-06-12",
            "2023-06-04",
        )

        dt = (
            "2010-05-24",
            "2011-06-13",
            "2012-06-04",
            "2013-06-24",
            "2014-06-09",
            "2015-06-01",
            "2016-06-20",
            "2017-06-05",
            "2018-05-28",
            "2019-06-17",
            "2020-06-08",
            "2021-06-21",
            "2022-06-13",
            "2023-06-05",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_labour_day(self):
        name_before = "День міжнародної солідарності трудящих"
        name_after = "День праці"
        self.assertHoliday(f"{year}-05-01" for year in range(1918, 2050))
        self.assertHoliday(f"{year}-05-02" for year in range(1929, 2018))
        self.assertNoHoliday("1928-05-02", "2018-05-02")
        self.assertNoHolidayName(name_after, Ukraine(years=range(1918, 2018)))
        self.assertNoHolidayName(name_before, Ukraine(years=range(2018, 2050)))

        dt = (
            "2010-05-03",
            "2010-05-04",
            "2011-05-03",
            "2015-05-04",
            "2016-05-03",
            "2021-05-03",
            "2022-05-02",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_victory_day(self):
        name = (
            "День перемоги над нацизмом у Другій світовій війні "
            "(День перемоги)"
        )
        self.assertHoliday(f"{year}-05-09" for year in range(1965, 2050))
        self.assertNoHoliday("1944-05-09", "1947-05-09", "1964-05-09")
        self.assertNoHolidayName(name, Ukraine(years=range(1918, 2016)))
        self.assertHoliday(
            "1945-05-09", "1945-09-03", "1946-05-09", "1946-09-03"
        )

        dt = (
            "2010-05-10",
            "2015-05-11",
            "2020-05-11",
            "2021-05-10",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_constitution_day(self):
        self.assertNoHoliday(f"{year}-06-28" for year in range(1918, 1997))
        self.assertNoHolidayName(
            "День Конституції України", Ukraine(years=range(1918, 1997))
        )
        self.assertHoliday(f"{year}-06-28" for year in range(1997, 2050))

        dt = (
            "2014-06-30",
            "2015-06-29",
            "2020-06-29",
            "2025-06-30",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_statehood_day(self):
        self.assertNoHoliday(f"{year}-07-28" for year in range(1918, 2022))
        self.assertNoHolidayName(
            "День Української Державності", Ukraine(years=range(1918, 2022))
        )
        self.assertHoliday(f"{year}-07-28" for year in range(2022, 2050))

        dt = ("2024-07-29",)
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_independence_day(self):
        self.assertNoHoliday(f"{year}-08-24" for year in range(1918, 1992))
        self.assertNoHolidayName(
            "День незалежності України", Ukraine(years=range(1918, 1991))
        )
        self.assertHoliday("1991-07-16")
        self.assertNoHoliday("1990-07-16", "1992-07-16")
        self.assertHoliday(f"{year}-08-24" for year in range(1992, 2050))

        dt = (
            "2013-08-26",
            "2014-08-25",
            "2019-08-26",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_defenders_day(self):
        name_before = "День захисника України"
        name_after = "День захисників і захисниць України"
        self.assertNoHoliday(f"{year}-10-14" for year in range(1918, 2015))
        self.assertHoliday(f"{year}-10-14" for year in range(2015, 2050))
        self.assertNoHolidayName(name_before, Ukraine(years=range(1918, 2015)))
        self.assertNoHolidayName(name_before, Ukraine(years=range(2021, 2050)))
        self.assertNoHolidayName(name_after, Ukraine(years=range(1918, 2021)))

        dt = (
            "2017-10-16",
            "2018-10-15",
            "2023-10-16",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_october_revolution_day(self):
        self.assertHoliday(f"{year}-11-07" for year in range(1918, 2000))
        self.assertHoliday(f"{year}-11-08" for year in range(1918, 2000))
        self.assertNoHoliday(f"{year}-11-07" for year in range(2000, 2050))
        self.assertNoHoliday(f"{year}-11-08" for year in range(2000, 2050))
        self.assertNoHolidayName(
            "Річниця Великої Жовтневої соціалістичної революції",
            Ukraine(years=range(2000, 2050)),
        )

        dt = (
            "1997-11-10",
            "1999-11-09",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_christmas_gregorian_day(self):
        self.assertNoHoliday(f"{year}-12-25" for year in range(1918, 2017))
        self.assertNoHolidayName(
            "Різдво Христове (за григоріанським календарем)",
            Ukraine(years=range(1918, 2017)),
        )
        self.assertHoliday(f"{year}-12-25" for year in range(2017, 2050))

        dt = (
            "2021-12-27",
            "2022-12-26",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_old_holidays(self):
        self.assertHoliday(f"{year}-01-22" for year in range(1918, 1951))
        self.assertNoHoliday(f"{year}-01-22" for year in range(1951, 2050))
        self.assertNoHolidayName(
            "День пам’яті 9 січня 1905 року", Ukraine(years=range(1951, 2050))
        )

        self.assertHoliday(f"{year}-03-18" for year in range(1918, 1929))
        self.assertNoHoliday(f"{year}-03-18" for year in range(1929, 2050))
        self.assertNoHolidayName(
            "День Паризької Комуни", Ukraine(years=range(1929, 2050))
        )

        self.assertHoliday(f"{year}-12-05" for year in range(1937, 1981))
        self.assertNoHoliday(f"{year}-12-05" for year in range(1981, 2050))
        self.assertHoliday(f"{year}-10-07" for year in range(1981, 1991))
        self.assertNoHoliday(f"{year}-10-07" for year in range(1991, 2050))
        self.assertNoHolidayName(
            "День Конституції СРСР", Ukraine(years=range(1918, 1937))
        )
        self.assertNoHolidayName(
            "День Конституції СРСР", Ukraine(years=range(1991, 2050))
        )

    def test_2018(self):
        # https://www.buhoblik.org.ua/kadry-zarplata/vremya/3678-3678-normi-trivalosti-robochogo-chasu.html
        self.assertHolidayDates(
            "2018-01-01",
            "2018-01-07",
            "2018-01-08",
            "2018-03-08",
            "2018-04-08",
            "2018-04-09",
            "2018-05-01",
            "2018-05-09",
            "2018-05-27",
            "2018-05-28",
            "2018-06-28",
            "2018-08-24",
            "2018-10-14",
            "2018-10-15",
            "2018-12-25",
        )

    def test_2019(self):
        # https://www.buhoblik.org.ua/kadry-zarplata/vremya/3946-3946-normi-trivalosti-robochogo-chasu.html
        self.assertHolidayDates(
            "2019-01-01",
            "2019-01-07",
            "2019-03-08",
            "2019-04-28",
            "2019-04-29",
            "2019-05-01",
            "2019-05-09",
            "2019-06-16",
            "2019-06-17",
            "2019-06-28",
            "2019-08-24",
            "2019-08-26",
            "2019-10-14",
            "2019-12-25",
        )

    def test_2020(self):
        # https://www.buhoblik.org.ua/kadry-zarplata/vremya/4058-4058-normi-trivalosti-robochogo-chasu.html
        self.assertHolidayDates(
            "2020-01-01",
            "2020-01-07",
            "2020-03-08",
            "2020-03-09",
            "2020-04-19",
            "2020-04-20",
            "2020-05-01",
            "2020-05-09",
            "2020-05-11",
            "2020-06-07",
            "2020-06-08",
            "2020-06-28",
            "2020-06-29",
            "2020-08-24",
            "2020-10-14",
            "2020-12-25",
        )

    def test_2021(self):
        # https://www.buhoblik.org.ua/kadry-zarplata/vremya/4221-4221-norma-trivalosti-robochogo-chasu.html
        self.assertHolidayDates(
            "2021-01-01",
            "2021-01-07",
            "2021-03-08",
            "2021-05-01",
            "2021-05-02",
            "2021-05-03",
            "2021-05-04",
            "2021-05-09",
            "2021-05-10",
            "2021-06-20",
            "2021-06-21",
            "2021-06-28",
            "2021-08-24",
            "2021-10-14",
            "2021-12-25",
            "2021-12-27",
        )

    def test_2022(self):
        # https://www.buhoblik.org.ua/kadry-zarplata/vremya/4246-norma-trivalosti-robochogo-chasu-2022.html
        self.assertHolidayDates(
            "2022-01-01",
            "2022-01-03",
            "2022-01-07",
            "2022-03-08",
            "2022-04-24",
            "2022-04-25",
            "2022-05-01",
            "2022-05-02",
            "2022-05-09",
            "2022-06-12",
            "2022-06-13",
            "2022-06-28",
            "2022-07-28",
            "2022-08-24",
            "2022-10-14",
            "2022-12-25",
            "2022-12-26",
        )

    def test_l10n_default(self):
        def run_tests(languages):
            for language in languages:
                ua = Ukraine(language=language)
                self.assertEqual(ua["2022-01-01"], "Новий рік")
                self.assertEqual(
                    ua["2022-12-25"],
                    "Різдво Христове (за григоріанським календарем)",
                )

        run_tests((Ukraine.default_language, None, "invalid"))

        self.set_language("en_US")
        run_tests((Ukraine.default_language,))

    def test_l10n_en_us(self):
        en_us = "en_US"
        ua = Ukraine(language=en_us)

        self.assertEqual(ua["2022-01-01"], "New Year's Day")
        self.assertEqual(ua["2022-01-07"], "Christmas (Julian calendar)")
        self.assertEqual(ua["2022-12-25"], "Christmas (Gregorian calendar)")
        self.assertEqual(ua["2023-01-02"], "New Year's Day (Observed)")

        self.set_language(en_us)
        for language in (None, en_us, "invalid"):
            ua = Ukraine(language=language)
            self.assertEqual(ua["2022-01-01"], "New Year's Day")
            self.assertEqual(ua["2022-01-07"], "Christmas (Julian calendar)")
            self.assertEqual(
                ua["2022-12-25"], "Christmas (Gregorian calendar)"
            )
            self.assertEqual(ua["2023-01-02"], "New Year's Day (Observed)")
