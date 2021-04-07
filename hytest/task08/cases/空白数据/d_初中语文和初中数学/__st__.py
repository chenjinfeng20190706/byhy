from lib.keywords import webopadmin
def suite_setup():
    # 删除所有的课程
    webopadmin.DeleteAllCourses()

    # 添加初中语文和初中数学两门课程
    webopadmin.AddCourse("初中语文","初中语文描述",1)
    webopadmin.AddCourse("初中数学","初中数学描述",2)

def suite_teardown():
    # 删除所有的课程
    webopadmin.DeleteAllCourses()





