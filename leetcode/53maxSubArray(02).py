class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        ma=nums[0]
        for i in range(len(nums)):
            j=i
            sum=0
            while j<len(nums):
                sum=max(sum+nums[j],nums[j])
                j+=1
                if sum>ma:
                    ma=sum
        return ma

s=Solution
#[822,2542,-421,522,624,34,20,-42,64,-423]
#[1,-2,5,-3,5]
a=[822,2542,-421,522,624,34,20,-42,64,-423]
print(s.maxSubArray(s,a))
