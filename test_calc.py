from calc import multiply, divide, summ, subtract
def test_multiply():
    assert multiply(4, 3) == 12
test_multiply()

def test_divide():
    assert divide(10, 2) == 5
    # assert divide(10, 0) == "Ошибка, нельзя делить на ноль."
test_divide()

def test_subtract():
    assert subtract(9, 6) == 3
test_subtract()

def test_summ():
    assert summ(3, 5) == 8
test_summ()
