import unittest
import numpy as np
from duration_calculator import calculate_duration


class TestDurationCalculator(unittest.TestCase):

    def test_today(self):
        today = np.datetime64('today', 'D')
        self.assertEqual(calculate_duration(today), 0)

    def test_one_day_ago(self):
        yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
        self.assertEqual(calculate_duration(yesterday), 1)

    def test_ten_days_ago(self):
        ten_days_ago = np.datetime64('today', 'D') - np.timedelta64(10, 'D')
        self.assertEqual(calculate_duration(ten_days_ago), 10)


if __name__ == "__main__":
    unittest.main()