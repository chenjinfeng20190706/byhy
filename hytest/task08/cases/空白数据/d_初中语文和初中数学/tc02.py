from lib.keywords import webopadmin
from hytest import INFO,CHECK_POINT,STEP

class tc002:
    name = "添加老师功能tc002"

    def setup(self):
        webopadmin.DeleteAllTeachers()

    def teardown(self):
        webopadmin.DeleteAllTeachers()

    def teststeps(self):
        STEP(1,"添加老师")
        webopadmin.AddTeacher("陈锦峰","chenjinfeng","陈锦峰老师",2,["初中语文"])
        webopadmin.AddTeacher("陈惠","chenhui","陈惠老师老师",1,["初中数学"])

        STEP(2,"列出所有的老师")
        teacherList = webopadmin.ListTeachers()

        STEP(3,"检查列出的老师与添加的老师是否一致")
        CHECK_POINT("列出的老师与添加的老师一致",teacherList == ['陈惠','陈锦峰'])


class tc003:
    name = "添加培训班tc003"

    def setup(self):
        webopadmin.DeleteAllClasses()

    def teardown(self):
        webopadmin.DeleteAllClasses()

    def teststeps(self):
        STEP(1, "添加培训班")
        webopadmin.AddClass("初中班","初中班描述",1,["初中语文","初中数学"])

        STEP(2, "列出所有的培训班")
        classList = webopadmin.ListClassses()

        STEP(3, "检查列出的培训班与添加的培训班是否一致")
        CHECK_POINT("列出的培训班与添加的培训班一致", classList == ["初中班"])

