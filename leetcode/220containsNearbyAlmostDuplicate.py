'''给你一个整数数组 nums 和两个整数k 和 t 。请你判断是否存在 两个不同下标 i 和 j，使得 abs(nums[i] - nums[j]) <= t ，同时又满足 abs(i - j) <= k 。

如果存在则返回 true，不存在返回 false。


输入：nums = [1,2,3,1], k = 3, t = 0
输出：true
示例 2：

输入：nums = [1,0,1,1], k = 1, t = 2
输出：true
示例 3：

输入：nums = [1,5,9,1,5,9], k = 2, t = 3
输出：false'''
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        def iscontain(nums):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if j==k:
                        continue
                    if abs(nums[j]-nums[k])<=t:
                        return True
                    else:
                        continue
        if len(nums)<=k:
            if iscontain(nums):
                return True
            else:
                return False
        for i in range(0,len(nums)-k):
            tem=nums[i:i+k+1]
            if iscontain(tem):
                return True
        return False

if __name__ == '__main__':
    s=Solution
    a=[1,2]
    k=3
    t=1
    print(s.containsNearbyAlmostDuplicate(s,a,k,t))