import requests
from pprint import pprint
from cfg import proxies,medcine_url
from login_module import login
from medicines_module import list_medicines

def delete_medcines(medcine_id):
    ret1, session_id = login.login_system("byhy", "88888888")
    cookies = dict(sessionid=session_id)

    payload = {
        "action":"del_medicine",
        "id": medcine_id
    }

    response = requests.delete(medcine_url,
                               json=payload,
                               cookies=cookies,
                               proxies=proxies)
    ret = response.json()
    pprint(ret)

    return ret

def delete_all_medcines():

    # 首先列出系统中所有的药品
    ret = list_medicines.list_medcines()

    for one in ret["retlist"]:
        delete_medcines(one["id"])

if __name__ == '__main__':
    ret = delete_medcines(32)

    # delete_all_medcines()
