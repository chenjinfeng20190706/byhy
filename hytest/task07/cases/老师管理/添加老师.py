from lib.WebOpAdmin import webopadmin
from hytest import *

class tc_10001:
    name = "添加老师tc_10001"

    def setup(self):
        # 删除所有的老师
        webopadmin.DeleteAllTeachers()
        # 删除所有的课程
        webopadmin.DeleteAllCourses()

        # 添加java课程和python课程两门课程
        webopadmin.AddCourse("java","java课程",1)
        webopadmin.AddCourse("python","python课程",2)

    def teardown(self):
        # 删除所有的老师
        webopadmin.DeleteAllTeachers()
        # 删除所有的课程
        webopadmin.DeleteAllCourses()

    def teststeps(self):
        STEP(1, "添加张三老师")
        webopadmin.AddTeacher("张三","zhangsan","张三老师",1,["python","java"])

        STEP(2,"检查添加的老师是否正确")

        INFO("先列出老师")
        teacher_list = webopadmin.ListTeachers()
        print(teacher_list)

        INFO("检查列出的老师与添加的是否一致")
        CHECK_POINT("列出的老师与添加的一致",teacher_list == ["张三"])




