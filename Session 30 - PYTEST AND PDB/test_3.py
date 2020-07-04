## Way of Selecting or filtering Test Cases:
# 1-> Marking the test cases
# 2-> Running the test cases with substring matching approach.

import pytest
#1st method


def correct_fun(x):
    return x+5


@pytest.mark.one
def test_method1():
    assert correct_fun(4) == 9


@pytest.mark.aadarsh
def test_method2():
    assert correct_fun(5) == 10

# -m is used to tell pytest that we are going to pass
# the name of the marker after space