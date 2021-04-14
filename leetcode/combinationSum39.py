class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res=[]
        sorted(candidates)
        def des (path,target,start):
            if target==0:
                self.res.append(path)
                return
            else:
                for i, n in enumerate(candidates[start:]):
                    if n>target:
                        break
                    else:
                        des (path+[n],target-n,start+i)
        des([],target,0)
        return self.res

        # res=[]
        # sorted(candidates)
        # def des(target,path,start):
        #     if not target:
        #         res.append(path[:])
        #     else:
        #         for i,n in enumerate(candidates[start:]):
        #             if n>target:
        #                 break
        #             else:
        #                 des(target-n,path+[n],start+i)
        # des(target,[],0)
        # return res

#2,3,6,7
#7
s=Solution
nums=[2,3,5]
t=8
print(s.combinationSum(s,nums,t))