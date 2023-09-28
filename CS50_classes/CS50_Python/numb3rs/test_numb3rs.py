from numb3rs import validate


def test_IPv4_1():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("255.256.256.256") == False


def test_IPv4_2():
    assert validate("cat") == False
    assert validate("1.2.a.4") == False
    assert validate("1.2.3b.4") == False
    assert validate("1.2.3") == False
    assert validate("10.10.10.10.10") == False
