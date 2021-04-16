class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) == 1:
            return str(nums[0])
        nums = [str(i) for i in nums]
        nums = sorted(nums, key=lambda x: x[0],reverse=True)
        print(nums)
        a = ''.join(nums)
        return a

s=Solution
nums=[3,30,34,5,9]
# print(nums)
# for i in range(len(nums) - 1):
#     for j in range(i+1, len(nums)):
#         if nums[i] < nums[j]:
#             temp = nums[j]
#             nums[j] = nums[i]
#             nums[i] = temp
# print(nums)
# nums=str(nums)
# a=' '.join(nums)
print(s.largestNumber(s,nums))