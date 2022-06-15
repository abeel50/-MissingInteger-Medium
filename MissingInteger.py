def checkPerm(A):
    length_A = len(A)
    if len(set(A)) != length_A:
        return False
    n = length_A
    if  ((n * (n  + 1 )) // 2) - sum(A) != 0:
        return False
    return True

def solution(A):
    # write your code in Python 3.6
    if all((x < 0 for x in A)):
        return 1
    elif checkPerm(A):
        return A[-1] + 1
    else:
        A = list(set(A))
        posSum = sum(x for x in A if x > 0)
        n = len(A) + 1
        return (n * (n  + 1 ))//2 - posSum