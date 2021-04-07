import requests
from pprint import pprint
from cfg import proxies,order_url
from login_module import login
from orders_module import list_orders

def delete_orders(order_id):
    ret1, session_id = login.login_system("byhy", "88888888")
    cookies = dict(sessionid=session_id)

    payload = {
        "action":"delete_order",
        "id": order_id
    }

    response = requests.delete(order_url,
                               json=payload,
                               cookies=cookies,
                               proxies=proxies)
    ret = response.json()
    pprint(ret)

    return ret

def delete_all_orders():

    # 首先列出系统中所有的药品
    ret = list_orders.list_orders()

    for one in ret["retlist"]:
        delete_orders(one["id"])

if __name__ == '__main__':
    ret = delete_orders(22)

    # delete_all_orders()
