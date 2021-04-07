from lib.keywords import webopadmin

def suite_setup():
    webopadmin.AddClassData("初中班1期","初中班1期描述",1,"初中班")

def suite_teardown():
    webopadmin.DeleteAllClassDatas()



