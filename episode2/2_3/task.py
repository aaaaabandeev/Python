# todo: replace this with an actual task
def task_1(str):
    list = []
    for i in str.split(' '):
        if i != ' ':
            list.append(i)
    return len(list[-1])


def task_2(str):
    list =[]
    for i in str.split(' '):
        if i != ' ':
            list.append(i)
    for d in range(0, len(list)-1, 2):
        list[d], list[d+1]=list[d+1], list[d]
    final =" ".join(list)
    return final


def task_3(str):
    a = str.split(' ')
    count=0

    for i in range(0, len(a)-1):
        if (a[i][-1]==a[i+1][0]):
            count+=1
    return count
