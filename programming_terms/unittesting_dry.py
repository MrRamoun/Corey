#%%
from DRY import Calc
import unittest

add = Calc.add
sub = Calc.subtract
mul = Calc.multiply
div = Calc.divide

class CalcTestCase(unittest.TestCase):
    """Test Calc Class in DRY.py"""
    def setUp(self):
        self.n1 = 10
        self.n2 = 6

    def tearDown(self):
        pass

    def test_add(self):        
        self.assertTrue(add(self.n1, self.n2), self.n1 + self.n2)

    def test_sub(self):        
        self.assertTrue(sub(self.n1, self.n2), self.n1 - self.n2)

    def test_mul(self):        
        self.assertTrue(mul(self.n1, self.n2), self.n1 * self.n2)

    def test_div(self):        
        self.assertTrue(div(self.n1, self.n2), self.n1 / self.n2)

if __name__ == '__main__':
    unittest.main()
    # TODO: fix the problems in here