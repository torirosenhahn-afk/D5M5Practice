from DE_test_demo.Demo.calculator import calcualtor

#class inheritance
class Sci_calculator(calcualtor):
    def __init__(self, a, b):
        super().__init__(a, b)

    def get_exp(self):
        return 