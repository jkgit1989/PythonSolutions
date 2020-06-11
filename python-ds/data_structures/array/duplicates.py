def duplicate(arr):
    res = []
    for x in arr:
        if arr[abs(x) - 1] < 0:
            res.append(abs(x))
        else:
            nums[abs(x) - 1] *= -1
    return res

arr = [20,10,10,10,15,5,100,200, 201]
result = duplicate(arr)
print(result)