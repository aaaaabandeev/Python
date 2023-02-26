def task_1(str):
    dict={}
    for i in str:
        if i.isalpha():
            if i.lower() in dict:
                dict[i.lower()] += 1
            else:
                dict[i.lower()] = 1
    return dict


def task_2(list):

    return sum(set(list))


def task_3(cities):
    final = ', '.join(cities)
    final += "."
    return final


def task_4(a, b):
    final = list(set(a) & set(b))
    return final
