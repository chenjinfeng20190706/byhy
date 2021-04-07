import pytest
from  lib.webUI import login,openBrowser,closeBrowser
def setup_module():
    openBrowser()

def teardown_module():
    closeBrowser()

class Test_错误登录:
    @pytest.mark.parametrize('username, password, expectedalert', [
        (None, '88888888', '请输入用户名'),
        ('byhy', None, '请输入密码'),
        ('byh', '88888888', '登录失败 : 用户名或者密码错误'),
        ('byhy', '8888888', '登录失败 : 用户名或者密码错误'),
        ('byhy', '888888888', '登录失败 : 用户名或者密码错误'),
    ])
    def test_UI_0001_UI_0005(self,username,password,expectedalert):

        alertText = login(username, password)
        assert alertText == expectedalert



