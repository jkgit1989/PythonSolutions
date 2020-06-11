def solution(A):
    left_side = A[0]
    right_side = sum(A) - A[0]

    diff = abs(left_side-right_side)

    for i in range(1, len(A) - 1):
        left_side += A[i]
        right_side -= A[i]

        current_diff = abs(left_side - right_side)

        if diff > current_diff:
            diff = current_diff

    return diff

print(solution([3, 1, 2, 4, 3,6,9]))
