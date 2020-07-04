import pytest

check_list = [("3+5",8),("4-2",2),("5*5",25)]

@pytest.mark.parametrize("test_input,expected",check_list)
def test_eval(test_input,expected):
    assert eval(test_input) == expected