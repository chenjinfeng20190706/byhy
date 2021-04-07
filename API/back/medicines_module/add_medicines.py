import requests
from pprint import pprint
from cfg import proxies,medcine_url
from login_module import login

def add_medcines(name,desc,sn):
    ret1,session_id = login.login_system("byhy","88888888")
    cookies = dict(sessionid=session_id)
    payload = {
        "action":"add_medicine",
        "data":{
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
if __name__ == '__main__':
    ret = add_medcines("青霉素", "青霉素 国字号","099877883837")

