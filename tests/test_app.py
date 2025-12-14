import unittest
# A simple dummy test that always passes
class TestApp(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()