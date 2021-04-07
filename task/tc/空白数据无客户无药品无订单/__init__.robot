*** Settings ***
Library  pylib.APImgr
Suite Setup     run keywords    delete_all_orders
                ...      AND    delete_all_medcines
                ...      AND    delete_all_customers
