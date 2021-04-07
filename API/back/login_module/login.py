import requests
from pprint import pprint
from cfg import proxies

def login_system(username,password):
    data = {
        "username" : username,
        "password" : password
    }
    r = requests.post('http://127.0.0.1/api/mgr/signin', data = data,proxies=proxies)
    ret = r.json()
    # 只有登录成功才能获取到session_id
    if ret["ret"] == 0:
        session_id = r.cookies["sessionid"]
        return ret,session_id
    return ret

if __name__ == '__main__':
    ret = login_system("byhy","88888888")
    pprint(ret)
