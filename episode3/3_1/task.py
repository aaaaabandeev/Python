import math


def task_1(text):
    list=text.strip('.').split('.')

    dict = {i.strip(): len(i.strip().split(' ')) for i in list}
    return dict


def task_2(x1, y1, x2, y2):
    final = ((math.sqrt(x1-x2))**2 + (y1 - y2)**2)
    return final
