class TestClass:
    def test_1(self):
        list1 = self.fun_test_2()
        assert 8 in list1

    def fun_test_2(self):
        self.list1 = [1,3,5,8]
        return self.list1

# cmd: pytest test_4.py