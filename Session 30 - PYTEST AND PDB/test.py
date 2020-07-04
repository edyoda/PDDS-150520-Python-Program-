import pytest


def modified_func(x):
    if x%2==0:
        return x+5
    else:
        return x-5


def correct_fun(x):
    return x+5


def test_method():
    assert modified_func(3) == 8  # -2

def test_method_2():
    assert modified_func(4) == 9
