import unittest
from app import greeting

class TestApp(unittest.TestCase):
    def test_default_greeting(self):
        self.assertEqual(greeting(), "Hello, Jenkins! Your pipeline works.")

    def test_custom_name(self):
        self.assertIn("Balu", greeting("Balu"))

if __name__ == "__main__":
    unittest.main()
