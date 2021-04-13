class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        b=[]
        # nums=sorted(nums,reverse=True)
        # print(nums)
        if len(nums)==1:
            return str(nums[0])
        for i in range(len(nums)):
            b.append(str(nums[i]))
        print(b)
        i=0
        #for i in range(len(max(b))):
        c=sorted(b,key=lambda x:int(x[0]),reverse=True)
        print(c)
        #c = sorted(b, key=lambda x: int(x[1]), reverse=True)
        # d=sorted(c,key=lambda x:int(x[1]),reverse=True)
        # print(d)

        # for i in b:
        #     for j in b[i:]:
        #         temp=i
        #         if len(i)<len(j):
        d=[[]*(len(nums)+1)]
        for i in b:
            d[len(i)-1].append(int(i))
        return d




        # a=''.join(c)
        # return a

s=Solution
nums=[3,30,34,5,9]
print(nums)
for i in range(len(nums) - 1):
    for j in range(i+1, len(nums)):
        if nums[i] < nums[j]:
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp
print(nums)
# nums=str(nums)
# a=' '.join(nums)
print(s.largestNumber(s,nums))