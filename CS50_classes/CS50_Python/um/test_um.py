from um import count


def test_count():
    assert count("Um, thanks for the album.") == 1
    assert count("um") == 1
    assert count("Um, thanks, um...") == 2
    assert count("Um?") == 1
    assert count("Hey UM?") == 1
    assert count("UMM what!") == 0
    assert count("no Um! hi um? um. who") == 3
    assert count("WHat U.m?") == 0
