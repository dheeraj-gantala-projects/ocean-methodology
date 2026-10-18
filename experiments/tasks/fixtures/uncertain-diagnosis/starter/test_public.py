import unittest
from retry import retry_delay

class PublicTests(unittest.TestCase):
    def test_first_attempt(self):
        self.assertEqual(retry_delay(0), 0.5)
    def test_second_attempt(self):
        self.assertEqual(retry_delay(1), 1.0)

if __name__ == "__main__":
    unittest.main()
