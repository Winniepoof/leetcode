class S():
    def min (self,num):
        sum1=0
        sum2=0
        k=len(num)
        a=[]
        for i in range(k):
            sum1+=int(num[i][0])
            sum2+=int(num[i][2])
        x=sum1/k
        y=sum2/k
        for i in range(k):
            a.append((int(num[i][0])-x)**2+(int(num[i][2])-y)**2)
        return a.index(min(a))




s=S

a=['1,1','2,2','1,2','1,3']
print(a[:])
print(sorted(a))
print(sorted(a,key=lambda x:x[2]))
print(sorted(a,key=lambda x:x[2],reverse=False))
print(int(a[0][0])+int(a[0][2]))
print(s.min(s,a))

