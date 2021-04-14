class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # res=[]
        # nums=sorted(nums)
        # for i in range(len(nums)-2):
        #     for j in range(i,len(nums)-1) :
        #         # if nums[i]!=nums[j]:
        #             for k in range(j,len(nums)) :
        #                   #  if nums[k]!=nums[j]:
        #                         if nums[i]+nums[j]+nums[k]==0 and i!=j!=k:
        #                             res.append([nums[i],nums[j],nums[k]])
        # return res

        # res=[]
        # nums=sorted(nums)
        # for i in range(len(nums)-1):
        #     for j in range(i,len(nums)):
        #         tem=0-(nums[i]+nums[j])
        #         if tem in nums and tem!=nums[i]!=nums[j] :
        #             res.append([nums[i],nums[j],tem])
        # return res

        nums=sorted(nums)
        res=[]
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while left<right:
                c=nums[i] + nums[left] + nums[right]
                if c==0:
                    res.append([nums[i],nums[left],nums[right]])

                    while nums[right]==nums[right-1] and right>left:
                        right-=1

                    while nums[left]==nums[left+1] and right>left:
                        left+=1
                    right -= 1
                    left += 1
                elif c>0 :
                    right-=1

                else:left+=1
        return res


s=Solution
nums = [-1,0,1,2,-1,-4]
print(Solution.threeSum(s,nums))