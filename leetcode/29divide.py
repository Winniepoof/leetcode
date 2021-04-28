class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        return int(dividend/divisor)

if __name__ == '__main__':
    s=Solution
    a=7
    b=-3
    print(s.divide(s,a,b))