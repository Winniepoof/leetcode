class S():
    def s(self):
        # a=int(input('a'))
        # b = int(input('b'))
        # c = int(input('c'))
        # res=[]
        # res.append(a)
        # res.append(a)
        # res.append(a)
        res=[]
        n=int(input('输入几个数?'))
        for i in range(1,n+1):
            print('第',i,'个数为',end='')
            res.append(int(input()))
        print(res)
        return sorted(res)

if __name__ == '__main__':
    s=S

    print(s.s(s))