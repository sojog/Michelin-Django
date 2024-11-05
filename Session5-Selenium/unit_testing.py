import unittest
import time

class TestRandomStuff(unittest.TestCase):
    def test_equality(self):
        time.sleep(3)
        self.assertEqual(2, 3)

    def test_differences(self):
        time.sleep(2)
        self.assertGreater(10, 3)

if __name__== "__main__":
    unittest.main()

