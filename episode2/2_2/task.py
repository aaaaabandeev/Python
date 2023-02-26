import math
# Пример 1
def task_1(A):
    sum = 0
    for i in range(len(A)):
        if A[i] > 0:
            sum += A[i]
    return sum


# Пример 2
def task_2(A):
    arif = sum(A)/len(A)
    return arif


# Пример 3
def task_3(A):
    arif = sum(A)/len(A)
    sumsum = 0
    for i in range(len(A)):
        sumsum += ((A[i] - arif) ** 2)
    final = (math.sqrt(sumsum/len(A)) )
    return final
