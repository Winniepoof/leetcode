class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=[]
        m=0
        j=1
        def isugly(m):
            if m==0:
                return False
            if m==1 or m==2 or m==3 or m==5:
                return True
            if m%2==0:
                return isugly(m/2)
            if m%3==0:
                return isugly(m/3)
            if m%5==0:
                return isugly(m/5)
            else:
                return False

        #for i in range(0,n):
        while j:
            if len(a)>n:
                break
            if isugly(j)is True:
                a.append(j)
                j+=1
            else:j+=1
        return a[n-1]