*** Settings ***
Library  pylib.APImgr

*** Test Cases ***
API-0152
    ${retadd}  add customers    武汉市桥西医院11     13345679941     武汉市桥西医院北路11
    should be true   $retadd["ret"] == 0

    #获取刚添加的客户id
    ${cuntomer_id}   evaluate  $retadd["id"]

    #列出客户信息
    ${list_customer}    list customers

    customers_should_contain   ${list_customer}[retlist]
                               ...      ${cuntomer_id}
                               ...      武汉市桥西医院11
                               ...      13345679941
                               ...      武汉市桥西医院北路11


    [Teardown]      delete_customers   ${cuntomer_id}