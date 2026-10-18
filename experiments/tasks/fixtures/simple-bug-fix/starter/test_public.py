import unittest
from discount import discounted_total

class PublicTests(unittest.TestCase):
    def test_zero_discount(self):
        self.assertAlmostEqual(discounted_total(100, 0), 100)
    def test_fifty_percent_discount(self):
        self.assertAlmostEqual(discounted_total(100, 50), 50)

if __name__ == "__main__":
    unittest.main()
