class Solution:
    def twoSum(self , numbers , target ):
        # write code here
        a=[]
        for i in range(len(numbers)):
            if target-numbers[i] in numbers[0:i]+numbers[i+1:]:
                a.append(numbers.index(numbers[i])+1)
                a.append(numbers.index(target-numbers[i])+1)
                return a
            # print(i)
            # b=numbers
            # b.remove(i)
            # print(b)
            # if (target-i) in b:
            #     a.append(numbers.index(i))
            #     a.append(numbers.index(target-i))
            #     return a
            # else:
            #     continue
        return False

s=Solution
a=[3,2,4]
b=[20, 70, 110, 150]
t=6
l=90
# a.remove(3)
# print(a)
print(s.twoSum(s,a,t))
print(s.twoSum(s,b,l))