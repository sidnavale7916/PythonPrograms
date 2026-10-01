from Code.Check_Even_Odd_Num import Even_Odd


def test_even_number():
    assert Even_Odd(10) == "Even"


def test_odd_number():
    assert Even_Odd(7) == "Odd"


def test_zero():
    assert Even_Odd(0) == "Even"


def test_negative_even():
    assert Even_Odd(-4) == "Even"


def test_negative_odd():
    assert Even_Odd(-5) == "Odd"
