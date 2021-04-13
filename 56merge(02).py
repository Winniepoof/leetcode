class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals or not intervals[0]:
            return intervals
        intervals = sorted(intervals, key=lambda x: x[0])
        res = []
        start, end = intervals[0][0], intervals[0][1]
        for i in range(len(intervals)):
            s, e = intervals[i][0], intervals[i][1]
            if s <= end:  # overlap
                end = max(end, e)
            else:
                res.append([start, end])
                start, end = s, e
        res.append([start, end])
        return res


def takesecond(elem):
    return elem[1]

s=Solution
a= [[1,3],[2,6],[8,10],[15,18]]
b=[[1,4],[4,5]]
c=[[1,3]]
d=[[1,4],[0,4]]
e=[[1,4],[0,1]]
f=[[1,4],[2,3]]
print(a.sort(key=takesecond))
print(sorted(e))
print('--------------------------------')
print(s.merge(s,a))
print(s.merge(s,b))
print(s.merge(s,c))
print(s.merge(s,d))
print(s.merge(s,e))
print(s.merge(s,f))
# b=[1]
# c=[2]
# d=[]
# d.append(b)
# d.append(c)
# a.append(d)
# print(a)
# print(a[0])
# print(a[0][0])
