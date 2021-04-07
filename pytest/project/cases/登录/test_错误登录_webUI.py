import pytest
from  lib.webUI import login,openBrowser,closeBrowser
def setup_module():
    openBrowser()

def teardown_module():
    closeBrowser()

class Test_错误登录:
    def test_UI_0001(self):
        print("\n 用例 UI-0001")

        alertText = login(None,"88888888")

        assert alertText == "请输入用户名"

    def test_UI_0002(self):
        print("\n 用例 UI-0002")

        alertText = login("byhy",None)

        assert alertText == "请输入密码"

    def test_UI_0003(self):
        print("\n 用例 UI-0003")

        alertText = login("byh","88888888")

        assert alertText == "登录失败 : 用户名或者密码错误"

