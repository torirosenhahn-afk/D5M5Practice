import unittest
from DE_test_demo.Demo.calculator import calcualtor

class TestOperations(unittest.TestCase):

    def setUp(self):
        self.calc - calcualtor(8,2)

    def test_sum(self):
        self.assertEqual(self.calc.get_prod(), 16, "The sum is wrong")

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
        