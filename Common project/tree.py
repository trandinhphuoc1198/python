class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
aaa=(((1,3,None),2,((None,3,4),5,(6,7,8))))
def parse(node):
   
    if node is None:
        return None
    elif isinstance(node,tuple) and len(node)==3:
        a=Node(node[1])
        a.left=parse(node[0])
        a.right=parse(node[2])
    else:
        return Node(node)
    return a
c=parse(aaa)
cc=[]
def to_tuple(tree):
    if tree is None:
        return 
    if tree.left is None and tree.right is None:
        return tree.data
    return to_tuple(tree.left),tree.data,to_tuple(tree.right)

def remove(nums):
    return [x for x in nums if x is not None]
def abb(node):
    if node is None:
        print("None")
        return True,None,None
    else:
        print(node.data)
    
    isbst_l,l_min,l_max=abb(node.left)
    isbst_r,r_min,r_max=abb(node.right)
    min_key=min(remove([l_min,r_min,node.data]))
    max_key=max(remove([l_max,r_max,node.data]))
    print(min_key,max_key)
    return isbst_l,min_key,max_key
abb(c)