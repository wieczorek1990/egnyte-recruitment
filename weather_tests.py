import unittest

import weather


class WeatherTest(unittest.TestCase):
    def test_minimum_temperature_spread(self):
        with open('weather.dat') as file_:
            day_no = weather.minimum_temperature_spread(file_.read())
        self.assertEqual(day_no, '2')


if __name__ == '__main__':
    unittest.main()
