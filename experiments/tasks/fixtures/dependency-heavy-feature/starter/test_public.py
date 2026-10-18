import unittest
from slug import slugify

class PublicTests(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(slugify("Hello World"), "hello-world")
    def test_lowercase(self):
        self.assertEqual(slugify("UPPER"), "upper")

if __name__ == "__main__":
    unittest.main()
