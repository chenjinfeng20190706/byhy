import requests
from pprint import pprint
from cfg import proxies,customer_url
from login_module import login

def edit_customers(customer_id,new_name,new_phonenumber,new_address):
    ret1, session_id = login.login_system("byhy", "88888888")
    # pprint(ret1)
    # pprint(session_id)
    cookies = dict(sessionid=session_id)

    payload = {
        "action":"modify_customer",
        "id": customer_id,
        "newdata":{
            "name":new_name,
            "phonenumber":new_phonenumber,
            "address":new_address
        }
    }

    response = requests.put(customer_url,
                            json=payload,
                            cookies=cookies,
                            proxies=proxies)
    ret = response.json()
    pprint(ret)
    return ret

if __name__ == '__main__':
    ret = edit_customers(129,"武汉市桥西医院129","18598021850","武汉市桥西医院北路129")

