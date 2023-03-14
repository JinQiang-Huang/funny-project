'''
终端动态显示时间
'''

import time

def t_clock():
    while True:
        Ymd = time.strftime("%Y-%m-%d", time.localtime())
        HMS = time.asctime().split()
        print("This is current time:", Ymd, HMS[3], end="")
        time.sleep(1)
        print('\r', end="", flush=True)  # 清屏和刷新

try:
    t_clock()
except KeyboardInterrupt:
    pass