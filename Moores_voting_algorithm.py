
def majorityElement(nums):
    n = len(nums)

    for val in nums:
        freq = 0
        for el in nums:
            if el == val:
                freq += 1
        return  val
arr = [1,2,3,2,1,1,1,1,]
print(majorityElement(arr))