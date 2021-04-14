class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        t1=0
        t2=0
        t3=0
        a=[1]
        while len(a)<=n:
            a.append(min(a[t1]*2,a[t2]*3,a[t3]*5))
            if a[-1]==a[t1]*2:
                t1+=1
            if a[-1]==a[t2]*3:
                t2+=1
            if a[-1]==a[t3]*5:
                t3+=1
        return a[-1]

s=Solution
n=100
print(s.nthUglyNumber(s,n))

