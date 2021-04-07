from lib.webui import *

def suite_setup():
    INFO('suite_setup')
    open_browser()


def suite_teardown():
    INFO('suite_teardown')
    wd = GSTORE['wd']
    wd.quit()