from DE_test_demo.Demo.calculator import calcualtor

def test_sum():
    calculation = calcualtor(8, 2)
    assert calculation.get_sum() == 10

def test_diff():
    calculation = calcualtor(8, 2)
    assert calculation.get_diff() == 6

def test_div():
    calculation = calcualtor(8, 2)
    assert calculation.get_div() == 4

def test_prod():
    calculation = calcualtor(8, 2)
    assert calculation.get_prod() == 16
