import pytest

from exam import calculate_marks


def test_full_marks():
    assert calculate_marks(100, 100) == 100.0


def test_zero_marks():
    assert calculate_marks(0, 100) == 0.0


def test_partial_marks():
    assert calculate_marks(45, 60) == 75.0


@pytest.mark.parametrize(
    "obtained, total",
    [
        ("50", 100),
        (None, 100),
        (True, 100),
        (-1, 100),
        (101, 100),
        (50, 0),
    ],
)
def test_invalid_input(obtained, total):
    with pytest.raises(ValueError):
        calculate_marks(obtained, total)
