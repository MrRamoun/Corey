#%%
from DRY import Calc

add = Calc.add
sub = Calc.subtract
mul = Calc.multiply
div = Calc.divide

class CalcTestCase:
    """Test Calc Class in DRY.py"""
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_add(self):
        n1 = 10
        n2 = 6
        self.assertTrue(add(n1, n2), n1 + n2)

    def test_sub(self):
        n1 = 20
        n2 = 4
        self.assertTrue(sub(n1, n2), n1 - n2)

    def test_mul(self):
        n1 = 2
        n2 = 8
        self.assertTrue(mul(n1, n2), n1 * n2)

    def test_div(self):
        n1 = 32
        n2 = 2
        self.assertTrue(div(n1, n2), n1 / n2)