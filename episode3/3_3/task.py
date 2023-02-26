import string

def task_1(A):
    count = 0
    num = A[0]
    for i in A:
        mera = A.count(i)
        if(count < mera):
            count = mera
            num = i
    return num



def task_2(bib, bob):
    n = 8
    correct = True
    for i in range(n):
        for j in range(n):
            for j in range(1 + 1, n):
                if bib[1] == bib[j] or bob[i] == bob[j] or abs(bib[i] - bib[j]) == abs(bob[i] - bob[j]):
                    correct = False
            if correct:
                return 'NO'
            else:
                return 'YES'



def task_3(x, y, xc, yc, r):
    if((xc-x)**2 + (yc-y)**2 == r**2 or (xc-x)**2 + (yc-y)**2 <= r**2):
        return True
    else:
        return False



def task_4(A):
    count = 0
    for i in range(1, len(A)-1):
        if A[i]>A[i+1] and A[i]>A[i-1]:
            count += 1
    return count



def task_5(key):
    value_list = list(string.digits)
    eng_lower_list = list(string.ascii_lowercase)
    op = open('file.txt', 'r')
    text = op.read().lower()
    res = ""
    for i in list(text):
        if i in value_list:
            letter_pos = value_list.index(i) + key
            list_len = len(value_list)
            letter_pos %= list_len
            r = value_list[letter_pos]
        elif i in eng_lower_list:
            letter_pos = eng_lower_list.index(i) + key
            list_len = len(eng_lower_list)
            letter_pos %= list_len
            r = eng_lower_list[letter_pos]
        else:
            r = i
        res += r
    res = res.replace(' ', 'b').split('\n')
    op.close()
    return res
