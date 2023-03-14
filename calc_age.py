'''
计算年龄
使用时间戳相减
当前时间-出生年月
'''

import time
try:
    input_name = input("请输入您的出生年月 例如:(2000-01-01): ")
    current_time = int(time.time())
    data_of_brith = int(time.mktime(time.strptime(input_name, "%Y-%m-%d")))
    sec_time = int((current_time-data_of_brith))
    min_time = int((current_time-data_of_brith)/60)
    hour_time = int((current_time-data_of_brith)/60/60)
    day_time = int((current_time-data_of_brith)/60/60/24)
    year_time = int((current_time-data_of_brith)/60/60/24/365)

    print('当前时间: {}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
    print('您在这世上已经浪费了{}年,{}天,{}小时,{}分钟,{}秒。(Just Kidding!)'.format(
        year_time, day_time, hour_time, min_time, sec_time))
except:
    print("您输入的格式有误")
