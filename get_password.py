'''
密码长度不能小于6
密码里可以包含英文字母，数字，符号
至少包含一个大写字母
至少包含一个特殊符号
'''

import random
import string


def get_upper():
    upper_value = string.ascii_uppercase
    count = random.randint(1, 3)
    return random.choices(upper_value, k=count)


def get_special():
    special_value = string.punctuation
    count = random.randint(1, 3)
    return random.choices(special_value, k=count)


def get_lower(remain):
    lower_value = string.ascii_lowercase
    return random.choices(lower_value + '1234567890', k=remain)


def generate_password(length):
    if length < 6:
        length = 6

    li = []
    upper_value = get_upper()
    li.extend(upper_value)

    special_value = get_special()
    li.extend(special_value)

    remain_number = length - len(li)
    lower_value = get_lower(remain_number)
    li.extend(lower_value)

    random.shuffle(li)
    password_value = ''.join(li)

    return password_value


if __name__ == '__main__':
    try:
        number = input("Please enter length of password you want to create:")
        print(generate_password(int(number)))
    except:
        print("404")