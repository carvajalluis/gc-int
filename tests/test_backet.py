from main import is_balanced


def test_balanced():
    assert is_balanced("(()(()))")


def test_balanced_invalid():
    assert not is_balanced(")(")


def test_imbalanced():
    assert not is_balanced("(()()))")


def test_empty():
    assert is_balanced("")


def test_multiple_roots():
    assert is_balanced("(((())())())()")
