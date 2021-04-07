import pytest
from  lib.webOpAdmin import webopadmin
def setup_module():
    webopadmin.openBrowser()

def teardown_module():
    webopadmin.closeBrowser()

class Test_错误登录:
    def test_UI_0001(self):
        print("\n 用例 UI-0001")

        alertText = webopadmin.loginAndCheck(None,"88888888")

        assert alertText == "请输入用户名"

    def test_UI_0002(self):
        print("\n 用例 UI-0002")

        alertText = webopadmin.loginAndCheck("byhy",None)

        assert alertText == "请输入密码"

    def test_UI_0003(self):
        print("\n 用例 UI-0003")

        alertText = webopadmin.loginAndCheck("byh","88888888")

        assert alertText == "登录失败 : 用户名或者密码错误"

