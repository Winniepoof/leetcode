class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]


s=Solution()
nums=[3,3]
b=[2,7,11,15]
target=6
b=[]
print(Solution.twoSum(s,nums,target))
