from lib.keywords import webopadmin
def suite_setup():
    webopadmin.AddTeacher("孔子","kongzi","孔子老师",1,["初中语文"])
    webopadmin.AddTeacher("庄子","zhuangzi","庄子老师",3,["初中数学"])

def suite_teardown():
    webopadmin.DeleteAllTeachers()
