class S():
    def min(self,data,w):
        res=[]
        for i in range(len(data)-w+1):
            a=data[i:i+w]
            res.append(min(a))
        return res



s=S
a=[17,5,8,11,4,14,13,22,3,10]
w=4
print(s.min(s,a,w))