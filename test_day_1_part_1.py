mport unittest
from day_1_part_1 import fuel_required
class TestFuelCalculations(unittest.TestCase):
    def test_fuel_required(self):
        self.assertEqual(fuel_required(12), 2)
        self.assertEqual(fuel_required(14), 2)
        self.assertEqual(fuel_required(1969), 654)
        self.assertEqual(fuel_required(100756), 33583)


if __name__ == '__main__':
    unittest.main()