import unittest
from sort import sort

class TestSort(unittest.TestCase):

    def test_standard(self):
        self.assertEqual(sort(10, 10, 10, 1), "STANDARD")

    def test_bulky_by_volume(self):
        self.assertEqual(sort(100, 100, 100, 1), "SPECIAL")

    def test_bulky_by_dimension(self):
        self.assertEqual(sort(150, 10, 10, 1), "SPECIAL")

    def test_heavy(self):
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")

    def test_rejected(self):
        self.assertEqual(sort(150, 10, 10, 20), "REJECTED")

    def test_negative_value(self):
        with self.assertRaises(ValueError):
            sort(-1, 10, 10, 1)

if __name__ == "__main__":
    unittest.main()
