class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res=''

        dig=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        map={1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
        for i in dig:
            if i>num:
                continue
            else:
                res+=(num//i)*map[i]
                num-=i*(num//i)
                if num==0:
                    break
        return res





map={1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'CL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
print(10*map[10])

#a=int(input('a:'))
a=40
s=Solution
print(s.intToRoman(s,a))
#print(a/10)