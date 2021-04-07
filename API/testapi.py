from lib.APImgr import  apimgr

apimgr.login_system()
apimgr.list_medcines()

# apimgr.add_customers("武汉市桥西医院","13345679934","武汉市桥西医院北路")
apimgr.list_customers()
#
# apimgr.add_medcines("青霉素", "青霉素 国字号","099877883837")
apimgr.list_medcines()


# apimgr.add_orders("订单002",139,[{"id":72,"amount":20,"name":"青霉素"}])
#
# apimgr.add_orders("订单003",139,[{"id":72,"amount":30,"name":"青霉素"}])
apimgr.list_orders()
apimgr.delete_all_orders()
apimgr.list_orders()









