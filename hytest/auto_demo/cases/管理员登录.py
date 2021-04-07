from time import sleep
from lib.webui import *

class UI_000X:

    # ddt_cases 里面每个字典元素 定义一个用例的数据
    # 其中： name是该用例的名称， para是用例的参数
    ddt_cases = [
        {
            'name': '登录 - UI-0001',
            'para': [None, '88888888',"请输入用户名"]
        },
        {
            'name': '登录 - UI-0002',
            'para': ['byhy', None,"请输入密码"]
        },
        {
            'name': '登录 - UI-0003',
            'para': ['byh', '88888888',"登录失败 : 用户名或者密码错误"]
        },
        {
            'name': '登录 - UI-0004',
            'para': ['byhy', '8888888',"登录失败 : 用户名或者密码错误"]
        },
        {
            'name': '登录 - UI-0005',
            'para': ['byhy', '888888888',"登录失败 : 用户名或者密码错误"]
        }
    ]

    # 调用时，
    # hytest 框架执行时，会自动创建出5份用例实例
    # 并且在调用 teststeps时，把每个用例的参数设置在 self.para 中
    # 用例代码 可以直接从 self.para 中获取参数
    def teststeps(self):
        wd = GSTORE['wd']

        # 取出参数
        username, password,info = self.para

        STEP(1,"输入网址")
        wd.get('http://127.0.0.1/mgr/sign.html')

        STEP(2,"输入用户名密码")
        if username is not None:
            wd.find_element_by_id('username').send_keys(username)
        if password is not None:
            wd.find_element_by_id('password').send_keys(password)

        STEP(3,"点击登录")
        wd.find_element_by_tag_name('button').click()
        sleep(1)

        notify = wd.switch_to.alert.text

        INFO("检查点")
        CHECK_POINT("弹出提示信息",notify == info)

        wd.switch_to.alert.accept()

    def teardown(self):
        wd = GSTORE['wd']
        wd.find_element_by_id('username').clear()
        wd.find_element_by_id('password').clear()
"""
class UI_0002:
    name = '登录 UI_0002'

    def teardown(self):
        wd = GSTORE['wd']
        wd.find_element_by_id('username').clear()
        wd.find_element_by_id('password').clear()

    def teststeps(self):
        wd = GSTORE['wd']

        STEP(1,"输入网址")
        wd.get('http://127.0.0.1/mgr/sign.html')

        STEP(2,"输入用户名密码")
        wd.find_element_by_id('username').send_keys('byhy')
        # wd.find_element_by_id('password').send_keys('88888888')

        STEP(3,"点击登录")
        wd.find_element_by_tag_name('button').click()

        notify = wd.switch_to.alert.text

        INFO("检查点")
        CHECK_POINT("弹出提示信息",notify == "请输入密码")

        wd.switch_to.alert.accept()
"""




