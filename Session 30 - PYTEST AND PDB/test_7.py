
import pytest

@pytest.fixture
def pre_data():
    # requirements to run a code.
    req = {"python":3,"django":2,"pandas":1,"numpy":1}
    return req

@pytest.mark.xfail
def test_method_1(pre_data):
    python = 3
    assert pre_data["python"] == python

@pytest.mark.skip
def test_method_2(pre_data):
    django = 1
    assert pre_data["django"] == django