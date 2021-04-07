import pytest
def setup_module():
    print('\n *** 初始化-模块 ***')

def teardown_module():
    print('\n ***   清除-模块 ***')

@pytest.mark.网页测试
@pytest.mark.兼容性测试
class Test_错误密码22222:

    @pytest.mark.smoke
    def test_C002021(self):
        print('\n用例C001001')
        assert 1 == 1

    def test_C002022(self):
        print('\n用例C001002')
        assert 2 == 2