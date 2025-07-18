# class Solution(object):
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

# # Create object and call method
# sol = Solution()
# arr = [2, 7, 11, 15]
# target = 9
# print(sol.twoSum(arr, target))  # Output: [0, 1]



# def twoSum(nums,target):
#     for i in range (len(nums)):
#         for j in range(i + 1 ,len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i,j]

# arr = [2,7,12,16]
# target = 9
# print(twoSum(arr,target))

















def twoSum(num,target):
    for i in range(len(num)):
        for j in range(i+1 , len(num)):
            if num[i] + num[j] == target:
                return[i,j]
arr = [1,2,4,5]
target = 9
print(twoSum(arr,target))