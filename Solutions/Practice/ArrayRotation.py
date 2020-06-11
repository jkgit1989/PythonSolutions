import math

def solution(A,n):

    result = [None] * len(A)
    print(result)

    for i in range(len(A)):

        result[(i+n)%len(A)] = A[i]

    return result

print(solution([7,2,8,3,5],2))