from lib.keywords import webopadmin

def suite_setup():
    webopadmin.AddClass("初中班","初中班描述",1,["初中语文","初中数学"])

def suite_teardown():
    webopadmin.DeleteAllClasses()
