class Solution(object):
    def minAbsoluteSumDiff(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """

        sum=0
        res=[]
        resmin=[]
        for i in range(len(nums1)):
            a=abs(nums1[i]-nums2[i])
            res.append(a)

        print(res)
        target1 = res.index(max(res))
        print(target1)

        for j in range(len(nums1)):
            b=abs(nums2[target1]-nums1[j])
            resmin.append(b)
        print(resmin)

        target2=resmin.index(min(resmin))
        print(target2)
        nums1[target1]=nums1[target2]

        for k in range(len(nums1)):
            m=abs(nums1[k]-nums2[k])
            sum+=m
        return sum

s=Solution
nums1 = [1,1,1,1,1,1]
nums2 = [10,10,10,10,10,10]
# nums1 = [2,4,6,8,10]
# nums2 = [2,4,6,8,10]
print(s.minAbsoluteSumDiff(s,nums1,nums2))