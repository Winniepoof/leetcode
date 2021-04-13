
def min(a,k):
    if a>=0 and a<k:
        return a
    else:
        x=min(a//k,k)*10+a%k
        return x

def ch(x):
    map = {0: '@', 1: '$', 2: '&'}
    b = str(x)
    print(b)
    res = ""
    for i in b:
        print(i)
        res+=map[int(i)]
    return res










a=int(input('a:'))
b=int(input('b:'))
print(bin(a))
print(oct(a))
print(hex(a))
print(min(a,b))
print(ch(min(a,b)))