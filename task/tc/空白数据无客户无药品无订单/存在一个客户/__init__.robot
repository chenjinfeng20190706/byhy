*** Settings ***
Library  pylib.APImgr

Suite Setup     add_customers   武汉市桥西医院1     13345679931     武汉市桥西医院北路1

Suite Teardown  delete_all_customers