import requests
from pprint import pprint
from cfg import proxies,medcine_url
from login_module import login

def edit_medcine(medcine_id,new_name,new_desc,new_sn):
    ret1, session_id = login.login_system("byhy", "88888888")
    # pprint(ret1)
    # pprint(session_id)
    cookies = dict(sessionid=session_id)

    payload = {
        "action":"modify_medicine",
        "id": medcine_id,
        "newdata":{
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

if __name__ == '__main__':
    ret = edit_medcine(129,"武汉市桥西医院129","18598021850","武汉市桥西医院北路129")

