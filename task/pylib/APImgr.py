import requests
from pprint import  pprint
from cfg import proxies
from cfg import customer_url
from cfg import medcine_url
from cfg import order_url

class APImgr():
    # 登录系统
    def login_system(self,username="byhy", password="88888888"):
        data = {
            "username": username,
            "password": password
        }
        r = requests.post('http://127.0.0.1/api/mgr/signin', data=data, proxies=proxies)
        ret = r.json()
        pprint(ret)
        # 只有登录成功才能获取到session_id
        if ret["ret"] == 0:
            session_id = r.cookies["sessionid"]
            return ret, session_id
        return ret

    # 客户操作
    # 添加客户
    def add_customers(self,name, phonenumber, address):
        ret1, session_id = self.login_system()
        cookies = dict(sessionid=session_id)
        payload = {
            "action": "add_customer",
            "data": {
                "name": name,
                "phonenumber": phonenumber,
                "address": address
            }
        }
        response = requests.post(customer_url,
                                 json=payload,
                                 cookies=cookies,
                                 proxies=proxies)
        ret = response.json()
        pprint(ret)
        return ret

    # 添加客户,为了测试有的字段不填的情况
    def add_customers2(self, data):
        ret1, session_id = self.login_system()
        cookies = dict(sessionid=session_id)
        payload = {
            "action": "add_customer",
            "data": data
        }
        response = requests.post(customer_url,
                                 json=payload,
                                 cookies=cookies,
                                 proxies=proxies)
        ret = response.json()
        pprint(ret)
        return ret

    # 列出所有客户
    def list_customers(self,pagesize=10,pagenum=1,keywords=''):
        ret1, session_id = self.login_system()
        cookies = dict(sessionid=session_id)

        payload = {
            "action": "list_customer",
            "pagesize": pagesize,
            "pagenum": pagenum,
            "keywords": keywords
        }
        response = requests.get(customer_url,
                                params=payload,
                                cookies=cookies,
                                proxies=proxies)
        ret = response.json()
        pprint(ret)

        return ret


    def customers_should_contain(self,customers_list,id,name,phonenumber,address,exceptedTimes=1):
        item = {
            "address": address,
            "id": id,
            "name": name,
            "phonenumber": phonenumber
        }

        currentTimes = customers_list.count(item)
        if currentTimes != exceptedTimes:
            raise Exception(f"客户列表里面包含了{currentTimes}次指定信息，期望包含{exceptedTimes}次")

    # 删除客户
    # 删除单个客户
    def delete_customers(self,customer_id):
        ret1, session_id = self.login_system()
        cookies = dict(sessionid=session_id)
        payload = {
            "action": "del_customer",
            "id": customer_id
        }
        response = requests.delete(customer_url,
                                   json=payload,
                                   cookies=cookies,
                                   proxies=proxies)
        ret = response.json()
        pprint(ret)
        return ret
    #删除所有客户
    def delete_all_customers(self):
        # 首先列出系统中所有的客户
        ret = self.list_customers(100,1)
        for one in ret["retlist"]:
            self.delete_customers(one["id"])

    # 修改客户信息，根据客户id来修改的
    def edit_customers(self,customer_id, new_name, new_phonenumber, new_address):
        ret1, session_id = self.login_system()
        cookies = dict(sessionid=session_id)
        payload = {
            "action": "modify_customer",
            "id": customer_id,
            "newdata": {
                "name": new_name,
                "phonenumber": new_phonenumber,
                "address": new_address
            }
        }
        response = requests.put(customer_url,
                                json=payload,
                                cookies=cookies,
                                proxies=proxies)
        ret = response.json()
        pprint(ret)
        return ret

    # 药品操作
    #添加药品
    def add_medcines(self,name, desc, sn):
        ret1, session_id = self.login_system()
        cookies = dict(sessionid=session_id)
        payload = {
            "action": "add_medicine",
            "data": {
                "name": name,
                "desc": desc,
                "sn": sn
            }
        }
        response = requests.post(medcine_url,
                                 json=payload,
                                 cookies=cookies,
                                 proxies=proxies)
        ret = response.json()
        pprint(ret)
        return ret

    #  列出所有药品
    def list_medcines(self,pagesize=10,pagenum=1,keywords=''):
        ret1, session_id = self.login_system()
        cookies = dict(sessionid=session_id)
        payload = {
            "action": "list_medicine",
            "pagesize": pagesize,
            "pagenum": pagenum,
            "keywords": keywords
        }
        response = requests.get(medcine_url,
                                params=payload,
                                cookies=cookies,
                                proxies=proxies)
        ret = response.json()
        pprint(ret)
        return ret


    def medcines_should_contain(self,medcines_list,id,name,sn,desc,exceptedTimes=1):
        item = {
            "id": id,
            "name": name,
            "sn": sn,
            "desc": desc
        }

        currentTimes = medcines_list.count(item)
        if currentTimes != exceptedTimes:
            raise Exception(f"客户列表里面包含了{currentTimes}次指定信息，期望包含{exceptedTimes}次")

    # 修改药品
    def edit_medcine(self,medcine_id, new_name, new_desc, new_sn):
        ret1, session_id = self.login_system()
        cookies = dict(sessionid=session_id)

        payload = {
            "action": "modify_medicine",
            "id": medcine_id,
            "newdata": {
                "name": new_name,
                "desc": new_desc,
                "sn": new_sn
            }
        }
        response = requests.put(medcine_url,
                                json=payload,
                                cookies=cookies,
                                proxies=proxies)
        ret = response.json()
        pprint(ret)
        return ret

    # 删除药品
    # 删除单个药品
    def delete_medcines(self,medcine_id):
        ret1, session_id = self.login_system()
        cookies = dict(sessionid=session_id)

        payload = {
            "action": "del_medicine",
            "id": medcine_id
        }
        response = requests.delete(medcine_url,
                                   json=payload,
                                   cookies=cookies,
                                   proxies=proxies)
        ret = response.json()
        pprint(ret)
        return ret
    # 删除所有药品
    def delete_all_medcines(self):
        # 首先列出系统中所有的药品
        ret = self.list_medcines(100,1)
        for one in ret["retlist"]:
            self.delete_medcines(one["id"])

    # 订单操作
    # 增加订单
    def add_orders(self,name, customer_id, medcine_list):
        ret1, session_id = self.login_system("byhy", "88888888")
        cookies = dict(sessionid=session_id)
        payload = {
            "action": "add_order",
            "data": {
                "name": name,
                "customerid": customer_id,
                "medicinelist": medcine_list
            }
        }

        response = requests.post(order_url,
                                 json=payload,
                                 cookies=cookies,
                                 proxies=proxies)
        ret = response.json()
        pprint(ret)
        return ret

    # 列出所有订单
    def list_orders(self,pagesize=10,pagenum=1,keywords=''):
        ret1, session_id = self.login_system("byhy", "88888888")
        cookies = dict(sessionid=session_id)

        payload = {
            "action": "list_order",
            "pagesize": pagesize,
            "pagenum": pagenum,
            "keywords": keywords
        }

        response = requests.get(order_url,
                                params=payload,
                                cookies=cookies,
                                proxies=proxies)

        ret = response.json()
        pprint(ret)
        return ret

    """
    # 这个 "create_date": "2021-03-09T09:12:23.702Z"   不知道怎么处理。
    def orders_should_contain(self,medcines_list,id,name,medicinelist,customer_name,exceptedTimes=1):
        item = {
            "id": id,
            "name": name,
            "medicinelist": medicinelist ,
            "customer_name": customer_name
        }

        currentTimes = medcines_list.count(item)
        if currentTimes != exceptedTimes:
            raise Exception(f"客户列表里面包含了{currentTimes}次指定信息，期望包含{exceptedTimes}次")
    """
    # 删除订单
    # 删除单个订单
    def delete_orders(self,order_id):
        ret1, session_id = self.login_system("byhy", "88888888")
        cookies = dict(sessionid=session_id)

        payload = {
            "action": "delete_order",
            "id": order_id
        }

        response = requests.delete(order_url,
                                   json=payload,
                                   cookies=cookies,
                                   proxies=proxies)
        ret = response.json()
        pprint(ret)
        return ret
    # 删除所有订单
    def delete_all_orders(self):

        # 首先列出系统中所有的药品
        ret = self.list_orders(100,1)

        for one in ret["retlist"]:
            self.delete_orders(one["id"])

apimgr = APImgr()

if __name__ == '__main__':
    apimgr.add_customers("13856963263","深圳市宝安区福永街道")
