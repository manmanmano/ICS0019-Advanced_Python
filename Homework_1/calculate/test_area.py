import unittest
from triangle_madang import triangle as t


class TestArea(unittest.TestCase):

    def test_if_area_is_equal(self):
        self.assertEqual(t.calculate_area(8, 8), 32, "Should be 32")

    def test_if_area_is_not_equal(self):
        self.assertNotEqual(t.calculate_area(10, 2), 12, "Should be 2")

    def test_if_area_works_with_float(self):
        self.assertEqual(t.calculate_area(8, 17.3), float(8*17.3/2))


if __name__ == 'main':
    unittest.main()
