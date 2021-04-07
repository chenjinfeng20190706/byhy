from lib.keywords import webopadmin
from hytest import *

class tc004:
    name = "添加培训班期tc004"

    def setup(self):
        webopadmin.DeleteAllClassDatas()

    def teardown(self):
        webopadmin.DeleteAllClassDatas()

    def teststeps(self):
        STEP(1,"添加初中班1期 ")
        webopadmin.AddClassData("初中班1期","初中班1期描述",1,"初中班")

        STEP(2, "列出所有培训班期")
        list_classdates = webopadmin.ListClassDatas()

        STEP(3,"检查列出的培训班期与添加的培训班期是否一致")
        CHECK_POINT("列出的培训班期与添加的培训班期一致",list_classdates==["初中班1期"])

