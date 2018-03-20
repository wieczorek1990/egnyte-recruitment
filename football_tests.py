import unittest

import football


class WeatherTest(unittest.TestCase):
    def test_minimum_goals_difference(self):
        with open('football.dat') as file_:
            name = football.minimum_goals_difference(file_.read())
        self.assertEqual(name, 'Arsenal')


if __name__ == '__main__':
    unittest.main()
