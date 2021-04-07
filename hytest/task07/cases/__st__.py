from lib.WebOpAdmin import webopadmin

def suite_setup():
    # 打开浏览器
    webopadmin.setupWebTest()
    # 登录系统
    webopadmin.loginWebSite("auto", "sdfsdfsdf")

def suite_teardown():
    webopadmin.tearDownWebTest()