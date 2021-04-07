import requests
from pprint import pprint
from cfg import proxies,order_url
from login_module import login

def add_orders(name,customer_id,medcine_list):
    ret1,session_id = login.login_system("byhy","88888888")
    cookies = dict(sessionid=session_id)
    payload = {
        "action":"add_order",
        "data":{
            "name":name,
            "customerid":customer_id,
            "medicinelist":medcine_list
        }
    }

    response = requests.post(order_url,
                      json=payload,
                      cookies=cookies,
                      proxies=proxies)
    ret = response.json()
    pprint(ret)
    return ret
if __name__ == '__main__':
    ret = add_orders("武汉市桥西医院82订单",
                     132,
                     [{"id": 63, "amount": 10, "name": "青霉素 国字号"}])




