import unittest

from main import sum_numbers

class TestSum(unittest.TestCase):
    def test_sum_int(self):
        result_sum = sum_numbers(2,3)
        self.assertEqual(result_sum, 5 )

    def test_sum_float(self):
        result_sum = sum_numbers(2.4,3.6)
        self.assertEqual(result_sum, 6.0 )