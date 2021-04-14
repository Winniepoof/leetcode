class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals=sorted(intervals,key= lambda x:x[0])
        res=[]
        if len(intervals)<=1:
            return intervals
        else:
            start=intervals[0][0]
            end=intervals[0][1]
            for i in range(len(intervals)):
                s,e=intervals[i][0],intervals[i][1]
                if s<=end:
                    end=max(end,e)
                else:
                    res.append([start,end])
                    start=s
                    end=e
            res.append([start,end])
        return res



'''
        from operator import itemgetter
        a = []
        def takeSecond(elem):
            return elem[1]
        #intervals=sorted(intervals)
        intervals=sorted(intervals,key=lambda x:x[0])
        #intervals.sort(key=takeSecond)
        print(intervals)

      def min(intervals):
            b = []
            i = 0
            while i < len(intervals) - 1:
                if intervals[i][0] >= intervals[i + 1][0]:
                    a.append(intervals[i+1])
                    i=i+1
                elif intervals[i][1] >= intervals[i + 1][0]:
                    c = intervals[i][0]
                    d = intervals[i + 1][1]
                    b.append(c)
                    b.append(d)
                    a.append(b)
                    i += 2
                    continue
                else:
                    a.append(intervals[i])
                    a.append(intervals[i + 1])
                    i += 2
                    break
            return a

        if len(intervals) <= 1:
            return intervals
        else:
            min(intervals)
        return a
'''




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
