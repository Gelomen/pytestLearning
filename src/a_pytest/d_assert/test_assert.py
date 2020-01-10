# encoding=utf-8
# 断言

import pytest


# 被测试类
class MyClass(object):

    @classmethod
    def sum(cls, a, b):
        return a + b

    @classmethod
    def div(cls, a, b):
        return a / b

    @classmethod
    def return_none(cls):
        return None


# 测试类
class TestClass:
    def test_assert_int(self):
        # try:
        a, b = 1, 2
        num = 4
        assert a + b, num

    def test_assert_true(self):
        assert (1 == 2) == True


if __name__ == "__main__":
    pytest.main()
