# encoding=utf-8
# 按顺序执行测试用例
from src.a_pytest.b_sequence.Calc import Calc


class TestClass:

    @classmethod
    def setup_class(cls):
        print(u"单元测试前，创建 Calc 类的实例")
        cls.c = Calc()

    @classmethod
    def teardown_class(cls):
        pass

    # 具体的测试用例，一定要以 test 开头
    def test_add(self):
        assert self.c.add(1, 2, 12) == 16

    def test_sub(self):
        assert self.c.sub(2, 1, 3) == -2

    def test_mul(self):
        assert Calc.mul(2, 3, 5) == 30

    def test_div(self):
        assert Calc.div(8, 2, 4) == 1
