class S():
    def min(self,start,end):
        res=[]
        sum=0
        for i in range(start-1,end+1):
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                res.append(i)

        for i in res:
            i=str(i)
            if i==i[::-1]:
                sum+=1
        return sum



s=S
a=100
b=200
print(s.min(s,a,b))