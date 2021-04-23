class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=0
        for i in range(len(s)-1):
            for j in range(i,len(s)):
                if s[j] not in s[i:j]:
                    continue
                else:
                    if l<len(s[i:j]):
                        l=len(s[i:j])
                    break
        return l

if __name__=='__main__':
    s=Solution
    a="abcabcbb"
    b='bbbbb'
    c='pwwkew'
    d=''
    print(s.lengthOfLongestSubstring(s,a))
    print(s.lengthOfLongestSubstring(s,b))
    print(s.lengthOfLongestSubstring(s,c))
    print(s.lengthOfLongestSubstring(s,d))
    print(len(' '))