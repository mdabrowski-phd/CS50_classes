from working import convert
import pytest


def test_format():
    with pytest.raises(ValueError):
        convert('9 AM - 5 PM')
    with pytest.raises(ValueError):
        convert('09:00 AM - 17:00 PM')


def test_time():
    with pytest.raises(ValueError):
        convert('13 AM to 9 PM')
    with pytest.raises(ValueError):
        convert('5:60 AM to 11:30 PM')


def test_return_value():
    assert convert('5 AM to 9 PM') == '05:00 to 21:00'


def test_return_value2():
    assert convert('5 AM to 9 PM') != '5:0 to 21:00'
