class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 1:
            if abs(nums[0] - 24) < 0.001:
                return True
            else:
                return False
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                c1 = nums[i]
                c2 = nums[j]
                possible = [c1 + c2, c1 - c2, c2 - c1, c1 * c2]
                if c1 != 0:
                    possible.append(c2 / c1)
                if c2 != 0:
                    possible.append(c1 / c2)
                # if n==2 and 24 in possible:
                #     return True
                # for k in range(len(possible)):
                #     nextnum=[]
                #     nextnum.append(possible[k])
                for k in possible:
                    nextnum=[k]
                    for l in range(n):
                        if l not in (i, j):
                            nextnum.append(nums[l])
                    if self.judgePoint24(self,nextnum):
                        return True
        return False

s=Solution
a=[4,1,8,7]
b=[8,1,6,6]
print(s.judgePoint24(s,b))
print(s.judgePoint24(s,a))