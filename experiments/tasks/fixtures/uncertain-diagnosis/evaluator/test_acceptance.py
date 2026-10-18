import unittest
from retry import retry_delay

class AcceptanceTests(unittest.TestCase):
    def test_exponential_and_capped(self):
        self.assertEqual(retry_delay(0, 0.5, 8), 0.5)
        self.assertEqual(retry_delay(1, 0.5, 8), 1.0)
        self.assertEqual(retry_delay(2, 0.5, 8), 2.0)
        self.assertEqual(retry_delay(10, 0.5, 8), 8.0)
    def test_caps_before_growth(self):
        self.assertEqual(retry_delay(3, 4, 5), 5)
    def test_invalid_values(self):
        for args in [(-1, 0.5, 8), (0, 0, 8), (0, 0.5, 0)]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                retry_delay(*args)

if __name__ == "__main__":
    unittest.main()
