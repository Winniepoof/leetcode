class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        # """
        # for i in range(len(nums)-1):
        #     if nums[i]==val:
        #         del nums[i]
        # return nums
        i=0
        for j in range(0,len(nums)):
            if nums[j]==val:
                continue
            if nums[j]!=val:
                nums[i]=nums[j]
                print(nums[i],end='\t')
                i+=1
        return i

s=Solution
nums=[0,1,2,2,3,0,4,2]
v=2
print(nums)
print(Solution.removeElement(s,nums,v))
