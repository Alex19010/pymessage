from .models import User
import random


def save():
    chaw = '1234567890qwertyuiopasdfghjklzxcvbnm'
    str_ = ''
    num = 7
    while num >= 0:
        nums = random.randint(0, len(chaw)-1)
        str_ += chaw[nums]
        num -= 1
    return str_