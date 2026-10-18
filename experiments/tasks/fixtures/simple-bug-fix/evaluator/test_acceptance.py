import unittest
from discount import discounted_total

class AcceptanceTests(unittest.TestCase):
    def test_discount_range(self):
        self.assertAlmostEqual(discounted_total(80, 25), 60)
        self.assertAlmostEqual(discounted_total(19.99, 10), 17.991)
    def test_zero_and_full_discount(self):
        self.assertAlmostEqual(discounted_total(10, 0), 10)
        self.assertAlmostEqual(discounted_total(10, 100), 0)
    def test_invalid_inputs_rejected(self):
        for args in [(-1, 10), (10, -1), (10, 101)]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                discounted_total(*args)

if __name__ == "__main__":
    unittest.main()
