class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        lis=s.split()
        print(lis)
        res=lis[:k]
        a=' '.join(res)
        return a
        # print(s)
        #         # for i in s:
        #         #     print(i,end='\t')

        # while i<k:
        #      print(lis[i],end='\t')
        #      i+=1
        # return



s=Solution
a='Hello how are you Contestant'
k=4
print(a)
res=a.split()
print(res)
print(s.truncateSentence(s,a,k))
print(a.split())