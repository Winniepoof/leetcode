
class bst():
    def __init__(self,v):
        self.v=v
        self.left:bst=None
        self.right:bst =None

    def add(self,v):
        if v>=self.v:
            if self.right is not None:
                self.right=bst(v)
            else:
                self.right.add(v)
        else:
            if self.left is not None:
                self.left=bst(v)
            else:
                self.left.add(v)


def mid(tree,array=[]):

    if tree is None:
        return []
    else:
        mid(tree.left,array)
        array.append(tree.value)
        mid(tree.right,array)
    return array




t=bst
# root=bst(10)
# root.left=bst(5)
# root.right=bst(15)
# root.left.left=bst(2)
# root.left.right=(5)
# root.right.right=bst(22)
# root.left.left.left=bst(1)
t.add(t,-2)
t.add(-1)
t.add(0)
t.add(1)
t.add(2)




print(mid(root))