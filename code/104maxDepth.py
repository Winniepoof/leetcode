import Tree
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sum1=0
        sum2=0
        su=0
        if not root:
            return 1
        if root.left is not None or root.right is not None:
            sum1+=self.maxDepth(self,root.left)
            sum2+=self.maxDepth(self,root.right)
            su=max(sum1,sum2)
        return su


        # a=[root]
        # sum=1
        # while a is not None:
        #     b=[]
        #     for node in a:
        #         if not node:
        #             b.append(None)
        #             continue
        #         b.append(node.left)
        #         b.append(node.right)
        #     sum+=1
        #     a=b
        # return sum

s = Solution

a=TreeNode.root=Tree.stringToTreeNode("[1,2,3]")

print(s.maxDepth(s,a))
