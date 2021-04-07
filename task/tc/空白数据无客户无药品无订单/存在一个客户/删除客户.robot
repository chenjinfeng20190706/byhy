*** Settings ***
Library  pylib.APImgr

*** Test Cases ***
API-0252
    #操作之前先列出客户
    ${list_customer_before}     list customers

    ${retadd}  add customers    武汉市桥西医院     13345679934     武汉市桥西医院北路
    should be true   $retadd["ret"] == 0

    #获取刚添加的客户id
    ${cuntomer_id}   evaluate  $retadd["id"]

    #删除客户
    ${ret_delete}     delete_customers   ${cuntomer_id}

    should be true   $ret_delete["ret"]==0

    #操作之后列出客户
    ${list_customer_after}     list customers

    should be equal     ${list_customer_before}     ${list_customer_after}



