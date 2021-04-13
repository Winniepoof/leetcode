'k > s > h > p > q'
class S():
    def min (self,num):
        k=[]
        s=[]
        h=[]
        p=[]
        q=[]
        for i in range(len(num)):
            if num[i][0]=='k':
                k.append(num[i])
            elif num[i][0]=='s':
                s.append(num[i])
            elif num[i][0]=='h':
                h.append(num[i])
            elif num[i][0]=='p':
                p.append(num[i])
            else:
                q.append(num[i])
        res=sorted(k)+sorted(s)+sorted(h)+sorted(p)+sorted(q)
        return res


s=S
a=["s1", "s3", "s9", "s4", "h1", "p3", "p2", "q5", "q4", "q9", "k2", "k1"]
b=['s3','s1','s6','s2']
print(sorted(a,key=lambda x:x[1]))
print(sorted(a,key=lambda x:x[0]))
print(sorted(b))
print(sorted(a))
print(s.min(s,a))