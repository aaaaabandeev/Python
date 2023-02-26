import math
def task_1(list, per):
    list.sort
    a = 0
    b = len(list)//2
    c = len(list) - 1

    while list[b]!=per and a<=c:
        if per>list[b]:
            a=b+1
        else:
            c=b-1
        b = (a + c)// 2
    return str(b)



def task_2(chislo):
    a=0
    for i in range(2, chislo // 2 + 1):
        if (chislo % i == 0):
            a += 1
    if (a == 0):
        return True
    else:
        return False
