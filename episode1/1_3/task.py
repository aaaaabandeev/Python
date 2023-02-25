# Пример 1
def task_1(n):
    X = 0
    while n <= 10:
        X = X + 1/n
        n += 1
    return X


# Пример 2
def task_2(x, n):
    Y = 0
    while x <= 17:
        Y = Y + x/n
        n += 2
    return Y


# Пример 3
def task_3(n):
    Y = 0
    x = 0
    while x <= n:
        Y = Y * n
        n += 1
    return Y


# Пример 4
def task_4(x, n):
    X = 1
    Y = 1
    i = 2
    while i <= n:
        X *= (Y + i)/i
    return X


# Пример 5
def task_5(x, n):
    X = 0
    y = 1
    i = 1
    while i <= n:
        X += (y * i) / (2*i)
    return X


# Пример 6
def task_6(n):
    z = 1
    i = 2
    while i <= n+1:
        z *= i
        i += 2
    return z
