class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y=str(x)
        if x==y[::-1]:
            print(True)
        else:print(False)

a=123
s=Solution
Solution.isPalindrome(s,a)