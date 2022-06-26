from main import can_jump


def test_can_jump():
    case = [2, 3, 1, 1, 4]
    assert can_jump(case)


def test_can_not_jump():
    case = [3, 0, 0, 0, 0]
    assert not can_jump(case)


def test_can_jump_large():
    case = [3, 0, 0, 0]
    assert can_jump(case)
