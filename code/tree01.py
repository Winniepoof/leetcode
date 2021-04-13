class Node():
    def __init__(self,elem=-1,lchild=None,richild=None):
        self.elem=elem
        self.lchild=lchild
        self.rchild=richild

class Tree(Node):
    def __init__(self,elem=-1,lchild=None,richild=None,root=None):
        super().__init__(elem,lchild,richild)
        self.root=root

    def add(self,elem):
        node=Node(elem)
        if self.root==None:
            self.root=node
        else:
            queue=[]
            queue.append(self.root)

            while queue:
                cur=queue.pop(0)

                if cur.lchild==None:
                    cur.lchild=node
                    return
                elif cur.lchild==None:
                    cur.rchild=node
                    return
                else:
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)
t=Tree
a=[1]
print(t.add(t,a))