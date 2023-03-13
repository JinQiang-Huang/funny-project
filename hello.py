import random
import string

def get_upper():
    upper_value = string.ascii_uppercase
    count = random.randint(1,3)
    return random.choices(upper_value, k=count)

def get_lower():
    lower_value = string.ascii_lowercase
    count = random.randint(1,3)
    return random.choices(lower_value + '1234567890', k=count)

def get_special():
    special_value = string.punctuation
    count = random.randint(1,3)
    return random.choices(special_value, k=count)

def generate_password():