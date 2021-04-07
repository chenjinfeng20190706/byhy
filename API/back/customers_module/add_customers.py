import requests
from pprint import pprint
from cfg import proxies,customer_url
from login_module import login

def add_customers(name,phonenumber,address):
    ret1,session_id = login.login_system("byhy","88888888")
    cookies = dict(sessionid=session_id)
    payload = {
        "action":"add_customer",
        "data":{
            "name":name,
            "phonenumber":phonenumber,
            "address":address
        }
    }

    response = requests.post(customer_url,
                      json=payload,
                      cookies=cookies,
                      proxies=proxies)
    ret = response.json()
    pprint(ret)
    return ret
if __name__ == '__main__':
    ret = add_customers("武汉市桥西医院","13345679934","武汉市桥西医院北路")

