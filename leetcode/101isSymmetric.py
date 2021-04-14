# Definition for a binary tree node.
import Tree
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res=[]
        a=[]
        b=[]
        a.append(root)



        while True:
            a.append(root)
            # if a==a[::-1]:
            #     return True
            b=a.pop(0)
            a.append(b.left)
            res.append(b.left)
            a.append(b.right)
            res.append(b.right)


        if root.left.val==root.right.val:
            return