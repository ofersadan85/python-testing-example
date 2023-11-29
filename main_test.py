import pytest
from main import *


def test_something():
    result = something()
    assert result == 4
    assert type(result) == int


@pytest.mark.parametrize(
        ("input_args", "expected_result"),
        [
            ((2, 3), 5),
            ((1, 3), 4),
            ((3.0, 4.5), 7)
        ])
def test_add(input_args, expected_result):
    # print(input_args)
    # print(expected_result)
    result = add(*input_args)
    assert result == expected_result
    assert type(result) == int


def test_square():
    assert square(2) == 4
    assert square(10) == 100


def test_everything():
    number = something()
    assert number == 4
    number = add(number, 3)
    assert number == 7
    number = square(number)
    assert number == 49

def test_error():
    assert 0 == 1
