import requests
from pprint import pprint
from cfg import proxies,customer_url
from login_module import login
from customers_module import list_customers

def delete_customers(customer_id):
    ret1, session_id = login.login_system("byhy", "88888888")
    cookies = dict(sessionid=session_id)

    payload = {
        "action":"del_customer",
        "id": customer_id
    }

    response = requests.delete(customer_url,
                               json=payload,
                               cookies=cookies,
                               proxies=proxies)
    pprint(response.text)
    ret = response.json()
    pprint(ret)

    return ret

def delete_all_customers():
    # 首先列出系统中所有的客户
    ret = list_customers.list_customers()

    for one in ret["retlist"]:
        delete_customers(one["id"])

if __name__ == '__main__':
    ret = delete_customers(131)

    # delete_all_customers()
