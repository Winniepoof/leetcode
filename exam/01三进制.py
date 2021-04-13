
def min(a,k):
    if a>=0 and a<k:
        return a
    else:
        x=min(a//k,k)*10+a%k
        return x

def ch(x):
    t=str(x)
    # m=t.split()
    # b=m[:]
    # print(b)
    c=[]
    st=''
    for i in range(len(t)):
        if int(t[i])==0:
            #c.append('@')
            st+='@'
        elif int(t[i])==1:
            #c.append('$')
            st += '$'
        else:
            #c.append('&')
            st += '&'
        #n=''.join(c)
    return st






a=int(input('a:'))
b=int(input('b:'))
print(bin(a))
print(oct(a))
print(hex(a))
print(min(a,b))
print(ch(min(a,b)))