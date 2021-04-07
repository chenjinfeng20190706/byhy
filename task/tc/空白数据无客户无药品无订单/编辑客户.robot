*** Settings ***
Library  pylib.APImgr


*** Test Cases ***
API-0201
    ${ret_edit}     edit_customers      8888    武汉市桥西医院     13345679934     武汉市桥西医院北路

    should be true      $ret_edit["ret"]==1
    should be true      $ret_edit["msg"]==客户ID不存在

    ${ret_list}     list customers

    should be true  $ret_list["retlist"]==[]




