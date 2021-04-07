*** Settings ***
Library  pylib.APImgr

*** Test Cases ***
API-0251
    ${ret_delete}       delete_customers    8888

    log to console      ${ret_delete}

    should be true      $ret_delete["ret"]==1
    should be true      $ret_delete["msg"]==客户ID不存在

