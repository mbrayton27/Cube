import unittest
import cube

class TestCube(unittest.TestCase):
    def test_cube1(self):
        result = cube.vol(4)
        self.assertEqual(result, 64)

    def test_cube(self):
        result = cube.vol(1.5)
        self.assertEqual(result, 3.375)

    def test_cube3(self):
        result = cube.vol(-1)
        self.assertEqual(result, -1)
if __name__ == '__main__':
    unittest.main()
