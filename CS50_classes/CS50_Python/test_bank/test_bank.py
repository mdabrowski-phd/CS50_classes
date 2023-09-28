from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0


def test_h_preceding():
    assert value("hard") == 20
    assert value("HARD") == 20


def test_else():
    assert value("bla") == 100
    assert value("BLA") == 100
