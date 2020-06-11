def solution(A):
    global_max=0
    local_max=0
    for i in range(1,len(A)):

        d = A[i] - A[i-1]
        local_max = max(d,local_max+d)
        global_max= max(global_max,local_max)

    return global_max

print(solution([132,111,234,543,321,223,23,43,44,32]))
print(solution([23171, 21011, 21123, 21366, 21013, 21367]))