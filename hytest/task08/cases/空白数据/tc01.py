from lib.keywords import webopadmin
from hytest import *
class tc001:
    name = "添加课程功能tc001"

    def setup(self):
        webopadmin.DeleteAllCourses()

    def teardown(self):
        webopadmin.DeleteAllCourses()

    def teststeps(self):

        STEP(1,"添加java课程和python课程")
        webopadmin.AddCourse("java","java描述",2)
        webopadmin.AddCourse("Python","Python",1)

        STEP(2,"列出所有的课程")
        courses = webopadmin.ListCourses()
        print(courses)

        STEP(3,"检查列出的课程与添加的是否一致")
        CHECK_POINT("列出的课程与添加的一致",courses==["Python","java"])













