class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max=0
        res=""
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                sub=s[i:j+1]
                if sub==sub[::-1]:
                    if max<j+1-i:
                        max==j+1-i
                        res=sub
        return res