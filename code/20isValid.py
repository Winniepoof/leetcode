class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        map={'(':')','[':']','{':'}'}
        res=[]
        for i,n in enumerate(s):
            if n in map:
                res.append(n)
            else:
                if not res:
                    return False
                else:
                    b=res.pop()
                    if n==map[b]:
                        return True
                    else:return False
        return len(res)==0

s=Solution
a='(]'
print(s.isValid(s,a))