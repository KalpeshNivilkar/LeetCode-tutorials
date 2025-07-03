def maximumSubarray(number):
    currSum = 0
    maxSum = float('-inf')

    for i in number:
        currSum += i
        maxSum = max(currSum,maxSum)

        if currSum == 0:
            currSum = 0
    
    return maxSum

arr = [-2,3,4,1,-2,-3,1,2]
print(maximumSubarray(arr))