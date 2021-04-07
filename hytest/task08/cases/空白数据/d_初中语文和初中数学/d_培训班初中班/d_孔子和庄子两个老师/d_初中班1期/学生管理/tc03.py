from lib.keywords import webopadmin
from hytest import *
from time import sleep

class tc0003:
    name = "添加学生tc0003"

    def setup(self):
        webopadmin.DeleteAllStudents()

    def teardown(self):
        webopadmin.DeleteAllStudents()

    def teststeps(self):
        STEP(1,"添加学生关羽和张飞")
        webopadmin.AddStudent("关羽","guanyu","青龙偃月刀","初中班","初中班1期")
        sleep(1)
        webopadmin.AddStudent("张飞","zhangfei","什么武器来着忘了","初中班","初中班1期")

        STEP(2,"列出所有的学生")
        student_list = webopadmin.ListStudents()
        INFO(student_list)

        STEP(3,"检查列出的学生是否与添加的一致")
        CHECK_POINT("列出的学生与添的学生一致",student_list==["张飞","关羽"])
