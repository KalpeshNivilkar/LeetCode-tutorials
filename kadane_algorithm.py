def maxsum(num):
    cursum = 0
    maxsum = float('-inf')

    for i in num:
        cursum += 1
        maxsum = max(cursum,maxsum)

        if cursum == 0:
            cursum = 0
    return maxsum
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxsum(arr))  