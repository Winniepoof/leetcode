class Solution(object):
    def countDifferentSubsequenceGCDs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import math

        def a(ori):
            fin=[[]]
            for i in range(len(ori)):
                for j in range(len(fin)):
                    fin.append(fin[j]+[ori[i]])
            return fin

        def gcd(a,b):
            a,b=max(a,b),min(a,b)
            if a%b==0:
                return b
            else:
                return gcd(a%b,b)


        def b(num):
            temp=[]
            if len(num)==1:
                temp.append(num[0])
            else:
                for i in range(len(num)-1):
                    for j in range(i+1,len(num)):
                        gbs=gcd(num[i],num[j])
                        temp.append(gbs)
                print(temp)

            return max(temp)

        s=a(nums)
        print(s)
        res=[]
        for i in range(len(s)-1):
            r=s[i+1]
            #print(r)
            x=b(r)
            print(x)
            if x not in res:
                res.append(x)
        print(res)
        m=len(res)
        return m




s=Solution

a=[6,10,3]


print(s.countDifferentSubsequenceGCDs(s,a))

# print(len(a))
# print(range(len(a)))

#print(c)