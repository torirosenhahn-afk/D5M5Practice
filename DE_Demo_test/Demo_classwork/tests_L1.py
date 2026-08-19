import unittest
from DE_test_demo.Demo.calculator import calcualtor

class TestOperations(unittest.TestCase):
    
    def test_sum(self):
        calculation = calcualtor(8,2)
        anwer = calculation.get_sum()
        self.assertEqual(anwer, 10, "The sum is wrong")

    def test_diff(self):
        calculation = calcualtor(8,2)
        anwer = calculation.get_diff()
        self.assertEqual(anwer, 6, "The difference is wrong")

    def test_div(self):
        calculation = calcualtor(8,2)
        anwer = calculation.get_div()
        self.assertEqual(anwer, 4, "The division is wrong")

    def test_prod(self):
        calculation = calcualtor(8,2)
        anwer = calculation.get_prod()
        self.assertEqual(anwer, 16, "The product is wrong")

if __name__ == "__main__":
    unittest.main()
        