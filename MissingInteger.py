def solution(A):
    # write your code in Python 3.6
    A = list(set(A))
    m = 1
    for i in A:
        if i > 0 and i ==m:
            m += 1
    return m
