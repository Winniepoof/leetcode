class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def ispartition(a):
            if a == a[::-1]:
                return True
        res = []
        def mainpartition(s):
            res1=[]
            for i in range(len(s)):
                k = s[0:i+1]
                if ispartition(k):
                    res1.append(k)
            return res1

        for i in range(len(s)):
            k = s[0:i + 1]
            if ispartition(k):
                res.append([k])
        for i in range(len(res)):
            t = s
            m = t.removeprefix(res[i][0])
            res[i].append(mainpartition(m))

        return res



s=Solution
a='aab'
b='ababaa'
c='aba'
d=[['a'],['aba'],['ababa']]
print(b.removeprefix(d[0][0]))
print(b.removeprefix(c))
print(a[0])
print(b[0:2])
print(s.partition(s,a))