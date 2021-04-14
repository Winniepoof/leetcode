class Solution(object):
    def twoSum(self,nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic={}
        for i,ele in enumerate(nums):
            if target-ele in dic:
                return [dic[target-ele],i]
            else:
                dic[nums[i]]=i


        # a = []
        # for i in range(len(nums)):
        #     if target - nums[i] in nums[0:i] + nums[i + 1:]:
        #         if nums.index(nums[i]) != nums.index(target - nums[i]):
        #             a.append(nums.index(nums[i]))
        #             a.append(nums.index(target - nums[i]))
        #         else:
        #             continue
        #         return a
        # return False



s=Solution()
nums=[3,3]
b=[2,7,11,15]
t=13
target=6
a={2:0,7:1}
print(a.__contains__(1))
print(a.__contains__(0))
print(a[7])
print(Solution.twoSum(s,nums,target))
print(Solution.twoSum(s,b,t))
