from cfg import *
from lib.keywords import webopadmin

def suite_setup():
    #打开网页
    webopadmin.setupWebTest()
    # 登录网址
    webopadmin.loginWebSite(userAdmin["userName"],userAdmin["password"])

    # 删除所有的学生
    webopadmin.DeleteAllStudents()
    # 删除所有的培训班期
    webopadmin.DeleteAllClassDatas()
    # 删除所有的培训班
    webopadmin.DeleteAllClasses()
    # 删除所有的老师
    webopadmin.DeleteAllTeachers()
    #删除所有的课程
    webopadmin.DeleteAllCourses()

def suite_teardown():
    webopadmin.tearDownWebTest()

