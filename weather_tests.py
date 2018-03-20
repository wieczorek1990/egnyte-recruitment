import unittest

import weather


class WeatherTest(unittest.TestCase):
    def test_minimum_temperature_spread(self):
        with open('weather.dat') as file_:
            dy = weather.minimum_temperature_spread(file_.read())
        self.assertEqual(dy, '2')


if __name__ == '__main__':
    unittest.main()
