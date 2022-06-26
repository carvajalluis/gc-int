from main import nearest_power_of_two


def test_128():
    assert nearest_power_of_two(130) == 128


def test_4():
    assert nearest_power_of_two(5) == 4
