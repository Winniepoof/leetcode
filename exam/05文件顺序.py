class S():
    def min (self,input):

        res = []
        res1=[]
        a = input.split(',')
        b=[]
        for i in a:
            b.append(int(i))
        def r(a,k):
            return a.index(k)
        res+=[i for i,x in enumerate(c) if x==-1]
        while len(res)<len(b):
            res+=[i for i,x in enumerate(c) if x==res[-1]]
        for i in res:
            res1.append(str(i))
        s=','.join(res1)
        return s




s=S

a='1,2,1,-1'
b=a.split(',')
c=[]
for i in b:
    c.append(int(i))
print(b)
print(c)
print([i for i,x in enumerate (c) if x==1])
print(s.min(s,a))