## Way of Selecting or filtering Test Cases:
# 1-> Marking the test cases
# 2-> Running the test cases with substring matching approach.

#2nd method
def correct_fun(x):
    return x+5

def test_method1():
    assert correct_fun(4) == 9

def test_method2():
    assert correct_fun(5) == 10

# substring test_method is present in both the test cases
# we pass substring to match by "-k" flag
# cmd: py.test -k test_method -v
# runs both the tests

# substring test_method2 is present in only one
# cmd: py.test -k test_method2 -v
# runs only one of them, deselect the other
