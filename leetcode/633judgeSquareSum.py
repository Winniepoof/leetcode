class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i = 0
        while i ** 2 <= c:
            if pow(c - i ** 2, 0.5)-int(pow(c - i ** 2, 0.5))==0:
                return True
            else:
                i += 1
                continue
        return False

if __name__ == '__main__':
    s=Solution
    a=5
    print(s.judgeSquareSum(s,a))