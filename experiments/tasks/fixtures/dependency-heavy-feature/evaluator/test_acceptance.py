import unittest
from slug import slugify

class AcceptanceTests(unittest.TestCase):
    def test_normalizes_runs_and_unicode(self):
        self.assertEqual(slugify("  Hello---World!!  "), "hello-world")
        self.assertEqual(slugify("café 東京"), "caf")
    def test_bounded_without_trailing_separator(self):
        self.assertEqual(slugify("alpha beta gamma", 10), "alpha-bet")
        self.assertEqual(slugify("hello-world", 5), "hello")
    def test_empty_and_invalid_length(self):
        self.assertEqual(slugify("!!!"), "")
        with self.assertRaises(ValueError):
            slugify("hello", 0)

if __name__ == "__main__":
    unittest.main()
