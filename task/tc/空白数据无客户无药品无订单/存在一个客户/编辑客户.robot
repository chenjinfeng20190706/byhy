*** Settings ***
Library  pylib.APImgr


*** Test Cases ***
#修改客户名称
API-0202
    ${retadd}  add customers    武汉市桥西医院     13345679934     武汉市桥西医院北路
    should be true   $retadd["ret"] == 0

    #获取刚添加的客户id
    ${cuntomer_id}   evaluate  $retadd["id"]

    ${ret_edit}     edit_customers   ${cuntomer_id}     武汉市桥西医院88     13345679934     武汉市桥西医院北路

    should be true      $ret_edit["ret"]==0

    #列出客户信息
    ${list_customer}    list customers

    customers_should_contain   ${list_customer}[retlist]
                               ...      ${cuntomer_id}
                               ...      武汉市桥西医院88
                               ...      13345679934
                               ...      武汉市桥西医院北路

    [Teardown]      delete_customers   ${cuntomer_id}
#修改客户电话
API-0203
    ${retadd}  add customers    武汉市桥西医院     13345679934     武汉市桥西医院北路
    should be true   $retadd["ret"] == 0

    #获取刚添加的客户id
    ${cuntomer_id}   evaluate  $retadd["id"]

    ${ret_edit}     edit_customers   ${cuntomer_id}     武汉市桥西医院     13345679988     武汉市桥西医院北路

    should be true      $ret_edit["ret"]==0

    #列出客户信息
    ${list_customer}    list customers

    customers_should_contain   ${list_customer}[retlist]
                               ...      ${cuntomer_id}
                               ...      武汉市桥西医院
                               ...      13345679988
                               ...      武汉市桥西医院北路

    [Teardown]      delete_customers   ${cuntomer_id}


#修改客户地址
API-0204
    ${retadd}  add customers    武汉市桥西医院     13345679934     武汉市桥西医院北路88
    should be true   $retadd["ret"] == 0

    #获取刚添加的客户id
    ${cuntomer_id}   evaluate  $retadd["id"]

    ${ret_edit}     edit_customers   ${cuntomer_id}     武汉市桥西医院     13345679934     武汉市桥西医院北路

    should be true      $ret_edit["ret"]==0

    #列出客户信息
    ${list_customer}    list customers

    customers_should_contain   ${list_customer}[retlist]
                               ...      ${cuntomer_id}
                               ...      武汉市桥西医院
                               ...      13345679934
                               ...      武汉市桥西医院北路

    [Teardown]      delete_customers   ${cuntomer_id}

#修改 客户名称 和 客户电话
API-0205
    ${retadd}  add customers    武汉市桥西医院     13345679934     武汉市桥西医院北路
    should be true   $retadd["ret"] == 0

    #获取刚添加的客户id
    ${cuntomer_id}   evaluate  $retadd["id"]

    ${ret_edit}     edit_customers   ${cuntomer_id}     武汉市桥西医院88     13345679988     武汉市桥西医院北路

    should be true      $ret_edit["ret"]==0

    #列出客户信息
    ${list_customer}    list customers

    customers_should_contain   ${list_customer}[retlist]
                               ...      ${cuntomer_id}
                               ...      武汉市桥西医院88
                               ...      13345679988
                               ...      武汉市桥西医院北路

    [Teardown]      delete_customers   ${cuntomer_id}
#修改 客户名称 和 客户地址
API-0206
    ${retadd}  add customers    武汉市桥西医院88     13345679934     武汉市桥西医院北路88
    should be true   $retadd["ret"] == 0

    #获取刚添加的客户id
    ${cuntomer_id}   evaluate  $retadd["id"]

    ${ret_edit}     edit_customers   ${cuntomer_id}     武汉市桥西医院     13345679934     武汉市桥西医院北路

    should be true      $ret_edit["ret"]==0

    #列出客户信息
    ${list_customer}    list customers

    customers_should_contain   ${list_customer}[retlist]
                               ...      ${cuntomer_id}
                               ...      武汉市桥西医院
                               ...      13345679934
                               ...      武汉市桥西医院北路

    [Teardown]      delete_customers   ${cuntomer_id}

# 修改 客户电话 和 客户地址
API-0207
    ${retadd}  add customers    武汉市桥西医院     13345679934     武汉市桥西医院北路
    should be true   $retadd["ret"] == 0

    #获取刚添加的客户id
    ${cuntomer_id}   evaluate  $retadd["id"]

    ${ret_edit}     edit_customers   ${cuntomer_id}     武汉市桥西医院     13345679988     武汉市桥西医院北路88

    should be true      $ret_edit["ret"]==0

    #列出客户信息
    ${list_customer}    list customers

    customers_should_contain   ${list_customer}[retlist]
                               ...      ${cuntomer_id}
                               ...      武汉市桥西医院
                               ...      13345679988
                               ...      武汉市桥西医院北路88

    [Teardown]      delete_customers   ${cuntomer_id}

#修改 客户名称、客户电话 和 客户地址
API-0208
    ${retadd}  add customers    武汉市桥西医院     13345679934     武汉市桥西医院北路
    should be true   $retadd["ret"] == 0

    #获取刚添加的客户id
    ${cuntomer_id}   evaluate  $retadd["id"]

    ${ret_edit}     edit_customers   ${cuntomer_id}     武汉市桥西医院88     13345679988     武汉市桥西医院北路88

    should be true      $ret_edit["ret"]==0

    #列出客户信息
    ${list_customer}    list customers

    customers_should_contain   ${list_customer}[retlist]
                               ...      ${cuntomer_id}
                               ...      武汉市桥西医院88
                               ...      13345679988
                               ...      武汉市桥西医院北路88

    [Teardown]      delete_customers   ${cuntomer_id}

# 存在两个客户,改第二个客户的名称使之与第一个客户的名称一致
API-0209
    ${retadd1}  add customers    武汉市桥西医院11     13345679911     武汉市桥西医院北路11
    should be true   $retadd1["ret"] == 0
    #获取刚添加的客户id
    ${cuntomer1_id}   evaluate  $retadd1["id"]

    ${retadd2}  add customers    武汉市桥西医院22     13345679922     武汉市桥西医院北路22
    should be true   $retadd2["ret"] == 0
    #获取刚添加的客户id
    ${cuntomer2_id}   evaluate  $retadd2["id"]

    #编辑之前列出客户信息
    ${list1_customer}    list customers

    # 编辑客户
    ${ret_edit}     edit_customers   ${cuntomer2_id}     武汉市桥西医院11     13345679911     武汉市桥西医院北路11

    #测试用
    log      ${ret_edit}[ret]

    should be true      $ret_edit["ret"]==1
    should be true      $ret_edit["msg"]=="客户名已经存在"

    #编辑之后列出客户信息
    ${list2_customer}    list customers

    should be equal     ${list1_customer}   ${list2_customer}

    [Teardown]      run keywords   delete_customers  ${cuntomer1_id}
                    ...     AND   delete_customers  ${cuntomer2_id}


