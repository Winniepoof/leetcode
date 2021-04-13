class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res=[]
        def recursion(path,candy):
            if len(candy)==0:
                self.res.append(path)
            for i,item in enumerate(candy):
                recursion(path+[item],candy[:i]+candy[i+1:])
        recursion([],nums)
        return self.res

s=Solution
nums=[1,2,3]
print(s.permute(s,nums))