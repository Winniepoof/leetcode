class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start=0
        l=0
        rec={}
        for i in range(len(s)):
            # if s[i] not in rec:
            #     rec[s[i]]=i
            #     tem=i-start+1
            if s[i] in rec and rec[s[i]]>=start:
                start=rec[s[i]]+1
            else:
                l=max(l,i-start+1)
            rec[s[i]] = i
        return l


if __name__=='__main__':
    s=Solution
    a="abcabcbb"
    b='bbbbb'
    c='pwwkew'
    d='  '
    e='l'
    f="tmmzuxt"
    print(s.lengthOfLongestSubstring(s,a))
    print(s.lengthOfLongestSubstring(s,b))
    print(s.lengthOfLongestSubstring(s,c))
    print(s.lengthOfLongestSubstring(s,d))
    print(s.lengthOfLongestSubstring(s,e))
    print(s.lengthOfLongestSubstring(s,f))
