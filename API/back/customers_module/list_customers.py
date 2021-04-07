import requests
from pprint import pprint
from cfg import proxies,customer_url
from login_module import login

def list_customers():
    ret1, session_id = login.login_system("byhy", "88888888")
    cookies = dict(sessionid=session_id)

    payload = {
        "action":"list_customer",
        "pagesize":10,
        "pagenum":1,
        "keywords":""
    }

    response = requests.get(customer_url,
                            params=payload,
                            cookies=cookies,
                            proxies=proxies)

    ret = response.json()
    pprint(ret)

    return ret
if __name__ == '__main__':
    list_customers()