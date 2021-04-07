from lib.WebOpAdmin import webopadmin
from hytest import *

class tc_0001:

    name = "添加课程 tc_0001 "

    def setup(self):
        # 删除所有的课程
        webopadmin.DeleteAllCourses()

    def teardown(self):
        # 删除所有的课程
        webopadmin.DeleteAllCourses()

    def teststeps(self):

        STEP(1,"添加初中化学和初中物理两门课程")

        webopadmin.AddCourse("初中化学","初中化学课程",2)
        webopadmin.AddCourse("初中物理","初中物理课程",1)

        STEP(2,"检查添加的课程是否正确")

        INFO("先列出所有的课程")
        courses = webopadmin.ListCourses()
        print(courses)

        CHECK_POINT("列出的课程与添加的课程一致",courses==["初中物理","初中化学"])





