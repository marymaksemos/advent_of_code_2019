import unittest
from day_1_part_2 import fuel_required,total_fuel_required
class TestFuelCalculator(unittest.TestCase):
    def test_fuel_required(self):
        self.assertEqual(fuel_required(14), 2)
        self.assertEqual(fuel_required(1969), 966)
        self.assertEqual(fuel_required(100756), 50346)

    def test_total_fuel_required(self):
        self.assertEqual(total_fuel_required([14, 1969, 100756]), 51314)


if __name__ == '__main__':
    unittest.main()              
