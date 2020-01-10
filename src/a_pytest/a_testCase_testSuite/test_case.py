# encoding=utf-8
# 测试用例


# 被测试类
class MyClass(object):
    @classmethod
    def sum(cls, a, b):
        return a + b

    @classmethod
    def sub(cls, a, b):
        return a - b


# 测试类

class TestClass:
    @classmethod
    def setup_class(cls):
        """初始化类固件"""
        print("\nsetUpClass\n")

    @classmethod
    def teardown_class(cls):
        """重构类固件"""
        print("\ntearDownClass\n")

    # 初始化工作
    def setup(self):
        self.a = 3
        self.b = 1
        print("\nsetUp")

    # 退出清理工作
    @staticmethod
    def teardown():
        print("\ntearDown")

    # 具体的测试用例，一定要以 test 开头
    def test_sum(self):
        # 断言两数之和是否为 4
        assert MyClass.sum(self.a, self.b) == 4

    def test_sub(self):
        # 断言两数只差是否为 2
        assert MyClass.sub(self.a, self.b) == 2
