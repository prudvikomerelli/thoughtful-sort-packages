import unittest
from sort import sort

class TestSort(unittest.TestCase):

    def test_standard(self):
        self.assertEqual(sort(10, 10, 10, 1), "STANDARD")

    def test_bulky_by_volume_boundary(self):
        # Exactly 1,000,000 cm^3
        self.assertEqual(sort(100, 100, 100, 1), "SPECIAL")

    def test_bulky_by_dimension_boundary(self):
        # Exactly 150 cm on one dimension
        self.assertEqual(sort(150, 10, 10, 1), "SPECIAL")

    def test_heavy_boundary(self):
        # Exactly 20 kg
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")

    def test_rejected_bulky_and_heavy(self):
        self.assertEqual(sort(150, 10, 10, 20), "REJECTED")

    def test_negative_value(self):
        with self.assertRaises(ValueError):
            sort(-1, 10, 10, 1)

    # ✅ Added edge-case test #1: bulky by dimension only (volume small)
    def test_bulky_dimension_only_small_volume(self):
        # One dimension >= 150 makes it bulky even if volume is tiny
        self.assertEqual(sort(150, 1, 1, 1), "SPECIAL")

    # ✅ Added edge-case test #2: bulky by volume only (all dimensions < 150)
    def test_bulky_volume_only_all_dims_under_150(self):
        # Volume >= 1,000,000 makes it bulky even if all dims < 150
        # 101 * 100 * 100 = 1,010,000 and max dimension is 101 (<150)
        self.assertEqual(sort(101, 100, 100, 1), "SPECIAL")


if __name__ == "__main__":
    unittest.main()
