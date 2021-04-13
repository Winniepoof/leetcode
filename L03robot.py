class Solution(object):
    def robot(self, command, obstacles, x, y):
        """
        :type command: str
        :type obstacles: List[List[int]]
        :type x: int
        :type y: int
        :rtype: bool
        """
        m = 0
        n = 0
        # path=[m,n]
        while True:
            for i in command:
                if i == 'U':
                    n += 1
                    if n > y:
                        return False
                    if m == x and n == y:
                        return True
                    if len(obstacles) != 0:
                        for i in range(len(obstacles)):
                            if m == obstacles[i][0] and n == obstacles[i][1]:
                                return False
                else:
                    m += 1
                    if m > x:
                        return False
                    if m == x and n == y:
                        return True
                    if len(obstacles) != 0:
                        for i in range(len(obstacles)):
                            if m == obstacles[i][0] and n == obstacles[i][1]:
                                return False

s=Solution
a="URR"
o=[[5, 5], [9, 4], [9, 7], [6, 4], [7, 0], [9, 5], [10, 7], [1, 1], [7, 5]]
x=3
y=2
b=[[1,2]]
print(b[0][1])
print(s.robot(s,a,o,x,y))



