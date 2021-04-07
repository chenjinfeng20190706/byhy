import pytest
def setup_module():
    print('\n *** 初始化-模块 ***')

def teardown_module():
    print('\n ***   清除-模块 ***')

# pytestmark =pytest.mark.性能测试
pytestmark = [pytest.mark.易用性测试, pytest.mark.Xx测试]


class Test_错误密码:

    @classmethod
    def setup_class(cls):
        print('\n === 初始化-类 ===')

    @classmethod
    def teardown_class(cls):
        print('\n === 清除 - 类 ===')

    def setup_method(self):
        print('\n --- 初始化-方法  ---')

    def teardown_method(self):
        print('\n --- 清除  -方法 ---')

    @pytest.mark.smoke
    def test_C001001(self):
        print('\n用例C001001')
        assert 1 == 1

    def test_C001002(self):
        print('\n用例C001002')
        assert 2 == 2

    def test_C001003(self):
        print('\n用例C001003')
        assert 3 == 2

class Test_错误密码22222:

    def test_C002021(self):
        print('\n用例C001001')
        assert 1 == 1

    @pytest.mark.网页测试
    def test_C002022(self):
        print('\n用例C001002')
        assert 2 == 2
