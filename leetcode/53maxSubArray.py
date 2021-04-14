class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        def s(num):
            sum=0
            for i in range(len(num)):
                sum+=num[i]
            return sum
        res=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)+1):
                print(nums[i:j])
                res.append(s(nums[i:j]))
        return max(max(res),max(nums))

s=Solution
a=[822,2542,-421,522,624,34,20,-42,64,-423]
# print(a[0:1])
print(s.maxSubArray(s,a))
