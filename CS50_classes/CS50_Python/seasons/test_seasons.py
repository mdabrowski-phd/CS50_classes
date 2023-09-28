from seasons import convert


def test_seasons():
    assert convert(2021, 9, 14) == "One million, fifty-one thousand, two hundred minutes"
    assert convert(2023, 9, 14) == "Zero minutes"
    assert convert(1990, 4, 19) == "Seventeen million, five hundred sixty-nine thousand, four hundred forty minutes"
