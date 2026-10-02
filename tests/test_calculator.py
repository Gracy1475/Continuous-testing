import pytest

from calculator import add, divide, multiply, subtract


@pytest.mark.parametrize(
    ("first", "second", "expected"),
    [
        (2, 3, 5),
        (-2, 3, 1),
        (-2, -3, -5),
        (0, 5, 5),
        (0, 0, 0),
        (2.5, 1.25, 3.75),
    ],
)
def test_add(first, second, expected):
    assert add(first, second) == expected


@pytest.mark.parametrize(
    ("first", "second", "expected"),
    [
        (5, 3, 2),
        (3, 5, -2),
        (-5, -3, -2),
        (0, 5, -5),
        (5, 0, 5),
        (5.5, 2.25, 3.25),
    ],
)
def test_subtract(first, second, expected):
    assert subtract(first, second) == expected


@pytest.mark.parametrize(
    ("first", "second", "expected"),
    [
        (2, 3, 6),
        (-2, 3, -6),
        (-2, -3, 6),
        (0, 5, 0),
        (5, 0, 0),
        (2.5, 2, 5.0),
    ],
)
def test_multiply(first, second, expected):
    assert multiply(first, second) == expected


@pytest.mark.parametrize(
    ("first", "second", "expected"),
    [
        (6, 3, 2),
        (-6, 3, -2),
        (-6, -3, 2),
        (0, 5, 0),
        (5, 2, 2.5),
        (1, 3, pytest.approx(1 / 3)),
    ],
)
def test_divide(first, second, expected):
    assert divide(first, second) == expected


@pytest.mark.parametrize("dividend", [1, -1, 0, 2.5])
def test_divide_by_zero_raises(dividend):
    with pytest.raises(ZeroDivisionError):
        divide(dividend, 0)
        
def test_add_large_numbers():
    assert add(1000,2000)==3000