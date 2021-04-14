class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        res=[nums[0]]
        ma=res[0]
        for i in range(1,len(nums)):
            res.append(max(res[i-1] + nums[i], nums[i]))
            #res.append(max(ma+nums[i+1],nums[i+1]))
            if res[-1]>ma:
                ma=res[-1]
        return ma

s=Solution
#[822,2542,-421,522,624,34,20,-42,64,-423]
#[1,-2,5,-3,5]
a=[822,2542,-421,522,624,34,20,-42,64,-423]
print(s.maxSubArray(s,a))
