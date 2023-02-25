import math
def task_1(N):
    X = 1
    for i in range(2, N + 1):
        X = X * i
    return X


def task_2(N):
    chislo = int(((((1 + math.sqrt(5))/2) ** (N - 1)) - (((1 - math.sqrt(5))/2) ** (N - 1)))/math.sqrt(5))
    return chislo


def task_3(N):
    dels = []
    if N > 0:
        for i in range (1, N+1):
            if N % i == 0:
                dels.append(i)
    return dels
