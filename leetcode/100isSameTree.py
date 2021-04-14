# Definition for a binary tree node.
import Tree
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    class TreeNode(object):
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    def isSameTree(self,p,q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # if p==q==None:
        #     return
        # p=Tree.stringToTreeNode(p)
        # q=Tree.stringToTreeNode(q)
        def check(p,q):
            if not p and not q:
                return True
            elif p==None or q==None:
                return False
            else:
                if p.val == q.val:
                    return check(p.left,q.left) and check(p.right,q.right)
            return False
        return check(p,q)





#if __name__ == '__main__':
s = Solution
# a = [1, 2, 3]
# b = [1, 2, 3]
a=TreeNode.root=Tree.stringToTreeNode("[1,2,3]")
b=Tree.stringToTreeNode("[1,2,3]")
print('------------------------------')
print(a.val)
print(a.left.val)
print(a.right.val)
print('------------------------------')
# print(a.left.val)
print(s.isSameTree(s,a,b))
