*** Settings ***
Library  pylib.APImgr

*** Test Cases ***
API-0151
    ${retadd}  add customers    武汉市桥西医院     13345679934     武汉市桥西医院北路
    should be true   $retadd["ret"] == 0

    #获取刚添加的客户id
    ${cuntomer_id}   evaluate  $retadd["id"]

    #列出客户信息
    ${list_customer}    list customers

    ${customer_info}    evaluate    $list_customer["retlist"][0]

    should be true  $cuntomer_id==$customer_info["id"]
    should be true  $customer_info["name"]=="武汉市桥西医院"
    should be true  $customer_info["phonenumber"]=="13345679934"
    should be true  $customer_info["address"]=="武汉市桥西医院北路"

    [Teardown]      delete_customers   ${cuntomer_id}


#不知道   客户名字段缺失   这个怎么实现！！！！！！
API-0153
    ${customer_data}    evaluate    {"phonenumber": 13598652696,"address": "武汉市桥西医院北路"}
    ${retadd}  add customers2    ${customer_data}
    should be true   $retadd["ret"] == 1
    should be true   $retadd["msg"] == "请求消息参数错误"

    #列出客户信息
    ${list_customer}    list customers

    should be true   $list_customer["retlist"] == []







