from selenium import webdriver
from time import sleep
class WebOpAdmin():
# class   keywords():
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    # 打开浏览器
    def setupWebTest(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
    #关闭浏览器
    def tearDownWebTest(self):
        self.driver.close()
    #登录系统
    def loginWebSite(self,userName,passWord):
        self.driver.get("http://localhost/mgr/login/login.html")
        self.driver.find_element_by_id("username").send_keys(userName)
        self.driver.find_element_by_id("password").send_keys(passWord)
        self.driver.find_element_by_tag_name("button").click()
    #删除所有的课程
    def DeleteAllCourses(self):
        # 点击课程
        self.driver.find_element_by_css_selector("a[ui-sref=\"course\"]").click()
        sleep(1)
        self.driver.implicitly_wait(1)
        while True:
            eles = self.driver.find_elements_by_css_selector("button[ng-click=\"delOne(one)\"]")
            if eles == []:
                break
            eles[0].click()
            self.driver.find_element_by_css_selector(".btn-primary").click()
            sleep(1)
        self.driver.implicitly_wait(10)
    #增加课程
    def AddCourse(self,courseName,courseDesc,courseIndex):
        # 点击课程
        self.driver.find_element_by_css_selector("a[ui-sref=\"course\"]").click()
        sleep(1)
        self.driver.find_element_by_css_selector("button[ng-click=\"showAddOne=true\"]").click()
        self.driver.find_element_by_css_selector("input[ng-model=\"addData.name\"]").clear()
        self.driver.find_element_by_css_selector("input[ng-model=\"addData.name\"]").send_keys(courseName)
        self.driver.find_element_by_css_selector("textarea[ng-model=\"addData.desc\"]").clear()
        self.driver.find_element_by_css_selector("textarea[ng-model=\"addData.desc\"]").send_keys(courseDesc)
        self.driver.find_element_by_css_selector("input[ng-model=\"addData.display_idx\"]").clear()
        self.driver.find_element_by_css_selector("input[ng-model=\"addData.display_idx\"]").send_keys(courseIndex)
        self.driver.find_element_by_css_selector("button[ng-click=\"addOne()\"]").click()
    #获取列表的课程名称
    def ListCourses(self):
        # 点击课程
        self.driver.find_element_by_css_selector("a[ui-sref=\"course\"]").click()
        sleep(1)
        self.driver.implicitly_wait(1)
        courseList = []
        eles = self.driver.find_elements_by_css_selector("tr td:nth-child(2)")
        for ele in eles:
            courseList.append(ele.text)
        self.driver.implicitly_wait(10)
        return courseList
    # 删除所有的老师
    def DeleteAllTeachers(self):
        # 点击老师
        self.driver.find_element_by_css_selector("a[ui-sref=\"teacher\"]").click()
        sleep(1)
        self.driver.implicitly_wait(1)
        while True:
            eles = self.driver.find_elements_by_css_selector("button[ng-click=\"delOne(one)\"]")
            if eles == []:
                break
            eles[0].click()
            self.driver.find_element_by_css_selector(".btn-primary").click()
            sleep(1)
        self.driver.implicitly_wait(10)
    #增加老师,教的课程传列表进去
    def AddTeacher(self,teacherName,teacherUserName,teacherDesc,teacherIndex,teachCourseList):
        # 点击老师
        self.driver.find_element_by_css_selector("a[ui-sref=\"teacher\"]").click()
        sleep(1)
        self.driver.find_element_by_css_selector("button[ng-click=\"showAddOne=true\"]").click()
        self.driver.find_element_by_css_selector("input[ng-model=\"addEditData.realname\"]").clear()
        self.driver.find_element_by_css_selector("input[ng-model=\"addEditData.realname\"]").send_keys(teacherName)
        self.driver.find_element_by_css_selector("input[ng-model=\"addEditData.username\"]").clear()
        self.driver.find_element_by_css_selector("input[ng-model=\"addEditData.username\"]").send_keys(teacherUserName)
        self.driver.find_element_by_css_selector("textarea[ng-model=\"addEditData.desc\"]").clear()
        self.driver.find_element_by_css_selector("textarea[ng-model=\"addEditData.desc\"]").send_keys(teacherDesc)
        self.driver.find_element_by_css_selector("input[ng-model=\"addEditData.display_idx\"]").clear()
        self.driver.find_element_by_css_selector("input[ng-model=\"addEditData.display_idx\"]").send_keys(teacherIndex)
        self.driver.implicitly_wait(1)
        while True:
            eles = self.driver.find_elements_by_css_selector("button[ng-click=\"addEditData.delTeachCourse(course)\"]")
            if  eles == []:
                break
            for ele in eles:
                ele.click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_tag_name("select").click()
        # 处理老师教的课程
        for teachCourse in teachCourseList:
            self.driver.find_element_by_css_selector(f"option[label=\"{teachCourse}\"]").click()
            self.driver.find_element_by_css_selector(".fa-plus").click()
        self.driver.find_element_by_css_selector("button[ng-click=\"addOne()\"]").click()
    #列出老师
    def ListTeachers(self):
        # 点击老师
        self.driver.find_element_by_css_selector("a[ui-sref=\"teacher\"]").click()
        sleep(1)
        self.driver.implicitly_wait(1)
        teacheresList = []
        eles = self.driver.find_elements_by_css_selector("tr td:nth-child(2)")
        for ele in eles:
            teacheresList.append(ele.text)
        self.driver.implicitly_wait(10)
        return teacheresList
    # 删除所有的班级
    def DeleteAllClasses(self):
        # 点击培训班
        self.driver.find_element_by_css_selector("a[ui-sref=\"training\"]").click()
        sleep(1)
        self.driver.implicitly_wait(1)
        while True:
            eles = self.driver.find_elements_by_css_selector("button[ng-click=\"delOne(one)\"]")
            if eles == []:
                break
            eles[0].click()
            self.driver.find_element_by_css_selector(".btn-primary").click()
            sleep(1)
        self.driver.implicitly_wait(10)
    def AddClass(self,className,classDesc,classIndex,containCourses):
        # 点击培训班
        self.driver.find_element_by_css_selector("a[ui-sref=\"training\"]").click()
        sleep(1)
        self.driver.find_element_by_css_selector("button[ng-click=\"showAddOne=true\"]").click()
        self.driver.find_element_by_css_selector("input[ng-model=\"addEditData.name\"]").clear()
        self.driver.find_element_by_css_selector("input[ng-model=\"addEditData.name\"]").send_keys(className)
        self.driver.find_element_by_css_selector("textarea[ng-model=\"addEditData.desc\"]").clear()
        self.driver.find_element_by_css_selector("textarea[ng-model=\"addEditData.desc\"]").send_keys(classDesc)
        self.driver.find_element_by_css_selector("input[ng-model=\"addEditData.display_idx\"]").clear()
        self.driver.find_element_by_css_selector("input[ng-model=\"addEditData.display_idx\"]").send_keys(classIndex)
        self.driver.implicitly_wait(1)
        while True:
            eles = self.driver.find_elements_by_css_selector("button[ng-click=\"addEditData.delTeachCourse(course)\"]")
            if eles == []:
                break
            for ele in eles:
                ele.click()
        self.driver.implicitly_wait(10)
        # 处理培训班包含的课程
        for containCourse in containCourses:
            self.driver.find_element_by_tag_name("select").click()
            self.driver.find_element_by_css_selector(f"option[label=\"{containCourse}\"]").click()
            self.driver.find_element_by_css_selector(".fa-plus").click()
        self.driver.find_element_by_css_selector("button[ng-click=\"addOne()\"]").click()
    def ListClassses(self):
        # 点击培训班
        self.driver.find_element_by_css_selector("a[ui-sref=\"training\"]").click()
        sleep(1)
        self.driver.implicitly_wait(1)
        ClasssesList = []
        eles = self.driver.find_elements_by_css_selector("tr td:nth-child(2)")
        for ele in eles:
            ClasssesList.append(ele.text)
        self.driver.implicitly_wait(10)
        return ClasssesList
    def DeleteAllClassDatas(self):
        # 点击培训班期
        self.driver.find_element_by_css_selector("a[ui-sref=\"traininggrade\"]").click()
        sleep(1)
        self.driver.implicitly_wait(1)
        while True:
            eles = self.driver.find_elements_by_css_selector("button[ng-click=\"delOne(one)\"]")
            if eles == []:
                break
            eles[0].click()
            self.driver.find_element_by_css_selector(".btn-primary").click()
            sleep(1)
        self.driver.implicitly_wait(10)
    def AddClassData(self,classDatas,classDataDesc,classDataIndex,belongClass):
        # 点击培训班期
        self.driver.find_element_by_css_selector("a[ui-sref=\"traininggrade\"]").click()
        sleep(1)
        self.driver.find_element_by_css_selector("button[ng-click=\"showAddOne=true\"]").click()
        self.driver.find_element_by_css_selector("input[ng-model=\"addEditData.name\"]").clear()
        self.driver.find_element_by_css_selector("input[ng-model=\"addEditData.name\"]").send_keys(classDatas)
        self.driver.find_element_by_css_selector("textarea[ng-model=\"addEditData.desc\"]").clear()
        self.driver.find_element_by_css_selector("textarea[ng-model=\"addEditData.desc\"]").send_keys(classDataDesc)
        self.driver.find_element_by_css_selector("input[ng-model=\"addEditData.display_idx\"]").clear()
        self.driver.find_element_by_css_selector("input[ng-model=\"addEditData.display_idx\"]").send_keys(classDataIndex)
        self.driver.find_element_by_tag_name("select").click()
        self.driver.find_element_by_css_selector(f"option[label=\"{belongClass}\"]").click()
        self.driver.find_element_by_css_selector("button[ng-click=\"addOne()\"]").click()
    def ListClassDatas(self):
        # 点击培训班期
        self.driver.find_element_by_css_selector("a[ui-sref=\"traininggrade\"]").click()
        sleep(1)
        self.driver.implicitly_wait(1)
        ClasssesDatasList = []
        eles = self.driver.find_elements_by_css_selector("tr td:nth-child(2)")
        for ele in eles:
            ClasssesDatasList.append(ele.text)
        self.driver.implicitly_wait(10)
        return ClasssesDatasList
    def DeleteAllStudents(self):
        #点击学生
        self.driver.find_element_by_css_selector("a[ui-sref=\"student\"]").click()
        sleep(1)
        self.driver.implicitly_wait(1)
        while True:
            eles = self.driver.find_elements_by_css_selector("button[ng-click=\"delOne(one)\"]")
            if eles == []:
                break
            eles[0].click()
            self.driver.find_element_by_css_selector(".btn-primary").click()
            sleep(1)
        self.driver.implicitly_wait(10)
    def AddStudent(self,studentName,studengUserName,studentDesc,belongClass,belongClassData):
        # 点击学生      这个得难点在于那个选择入学日期那里该怎么进行操作？？？
        self.driver.find_element_by_css_selector("a[ui-sref=\"student\"]").click()
        sleep(1)
        self.driver.find_element_by_css_selector("button[ng-click=\"showAddOne=true\"]").click()
        self.driver.find_element_by_css_selector("input[ng-model=\"addEditData.realname\"]").clear()
        self.driver.find_element_by_css_selector("input[ng-model=\"addEditData.realname\"]").send_keys(studentName)
        self.driver.find_element_by_css_selector("input[ng-model=\"addEditData.username\"]").clear()
        self.driver.find_element_by_css_selector("input[ng-model=\"addEditData.username\"]").send_keys(studengUserName)
        self.driver.find_element_by_tag_name("textarea").clear()
        self.driver.find_element_by_tag_name("textarea").send_keys(studentDesc)
        #入学时间，不知道怎么操作了
        # 默认为当前的时间，没有做更改
        # 选择所属培训班
        eles = self.driver.find_elements_by_css_selector("select[ng-options*=trainingList]")
        eles[1].click()
        eles = self.driver.find_elements_by_css_selector(f"option[label=\"{belongClass}\"]")
        eles[1].click()
        #选择所属培训班期
        eles = self.driver.find_elements_by_css_selector("select[ng-options*=traininggradeList]")
        eles[1].click()
        eles = self.driver.find_elements_by_css_selector(f"option[label=\"{belongClassData}\"]")
        eles[1].click()
        #点击确定
        self.driver.find_element_by_css_selector("button[ng-click=\"addOne()\"]").click()

    def ListStudents(self):
        # 点击学生
        self.driver.find_element_by_css_selector("a[ui-sref=\"student\"]").click()
        sleep(1)
        self.driver.implicitly_wait(1)
        StudentsList = []
        eles = self.driver.find_elements_by_css_selector("tr td:nth-child(1)")
        for ele in eles:
            StudentsList.append(ele.text)
        self.driver.implicitly_wait(10)
        return StudentsList

webopadmin = WebOpAdmin()

if __name__ == '__main__':
    s1 = WebOpAdmin()
    s1.setupWebTest()
    s1.loginWebSite("auto","sdfsdfsdf")
    # print(s1.ListClassses())
    # s1.DeleteAllCourses()
    # s1.AddClassData("1","1","1","ab")
    # s1.AddClassData("2","2","2","a")
    # s1.AddClassData("3","3","3","b")
    # s1.AddClass("a","a","2",["aa"])
    # s1.AddClass("b","b","3",["bb"])
    # print(s1.ListClassses())
    # print(s1.ListClassDatas())
    # s1.DeleteAllClassDatas()
    # s1.DeleteAllStudents()
    s1.AddStudent("ccc","ccc","ccc","aa","aa1")
    print(s1.ListStudents())
    s1.tearDownWebTest()














































"""
老师，我有个问题，想请您帮忙分析一下，具体是这样子复现的。
我的系统中有两门课程  aa,bb
然后呢，进行调试代码的时候，
第1种情况：第170行代码我有写列出所有的班级看一下（因为系统中没有班级，会等待10S），
然后后面再增加一个班级，就是173行代码，就这样执行----结果是执行完之后在系统中没有该班级。
第2种情况：在上面的基础上将176行代码打开，执行完之后系统中又有该班级。
第3种情况：将176行代码注释掉，打开174行代码，执行之后，系统中又有这两个班级。
问题就是为什么会出现第一种情况？很奇怪。
"""
# 我去，在list的那里，没有课程或者老师或者班级或者班期的时候设置临时等待时间，就没有这个问题了。但是
# 命名就是独立的方法啊，怎么可能会有影响呢！！！！！！