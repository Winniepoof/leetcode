class S:
    def iss(self,num):
        def s(s):
            if s==s[::-1]:
                return True
            else:
                return False
        if s(num) is True:
            return True
        for i in range(len(num)):
            c=num[0:i]+num[i+1:]
            print(c)
            if s(c)is True:
                return True
            else:
                continue
        return False

if __name__ == '__main__':

    s=S
    a='aba'
    b='abda'
    c='abcd'
    # print(s.iss(s,a))
    # print(s.iss(s,b))
    # print(s.iss(s,c))
    d=input()
    print(s.iss(s,d))
    c=b[0:0]+b[2:]
    #print(c)
