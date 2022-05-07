from gettext import find
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def display(self,node,level=0,space='\t'):
        if node is None:
            print(space*level,'None')
            return
        self.display(node.left,level+1,space)
        print(space*level,node.data)
        self.display(node.right,level+1,space)
    def find_max(self,node,maximun):
        if node is None:
            return maximun
        maximun=self.find_max(node.left,maximun)
        maximun=self.find_max(node.right,maximun)
        if node.data>maximun:
            maximun=node.data
        return maximun
    def find_max_2(self,node,previous=None,max=None):
        global prev
        global maxx
        if node is None:
            return
        if max is None:
            maxx=node.data
        if previous and maxx and maxx<node.data:
            maxx=node.data
        prev=node.data
        print(prev)
        self.find_max_2(node.left,prev,maxx)
        self.find_max_2(node.right,prev,maxx)
        return maxx
    def insert_node(self,node,value):
        if node is None:
            node=Node(value)
        elif value>node.data:
            node.right=self.insert_node(node.right,value)
        else:
            node.left=self.insert_node(node.left,value)
        return node
def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [node.data] + list_all(node.right)
def BST_from_sortedList(list,start,end):
    mid=(start+end)//2
    if start>end:
        return None
    node=Node(list[mid])
    node.left=BST_from_sortedList(list,start,mid-1)
    node.right=BST_from_sortedList(list,mid+1,end)
    return node
def find_node(node,value):
    if node is None:
        return None
    if node.data==value:
        return node
    elif node.data>value:
        node=find_node(node.left,value)
    else:
        node=find_node(node.right,value)
    return node
def parse_tuple(tupleTarge,node=None):
        if isinstance(tupleTarge,tuple):
            node=Node(tupleTarge[1])
            node.left=parse_tuple(tupleTarge[0],node.left)
            node.right=parse_tuple(tupleTarge[2],node.right)
            return node
        else:
            return Node(tupleTarge)
def check_balance(node,height=0):
    if node is None:
        return height,True
    height_left,is_balance_l=check_balance(node.left,height+1)
    height_right,is_balance_r=check_balance(node.right,height+1)
    is_balance=is_balance_r and is_balance_l and abs(height_right-height_left)<=1
    return max(height_left,height_right),is_balance
binary=Node(100000)
left1=Node(5000)
left2=Node(4)
left3=Node(50)
right1=Node(55)
right2=Node(41)
right3=Node(42)
binary.left=left1
binary.right=right1
right1.left=left2
binarytuple=((1,2,(1,2,(1,2,7))),6,((1,2,7),2,(1,2,7)))
b=[0,1,2,3,4,5,6,7,8]
d=BST_from_sortedList(b,0,len(b)-1)
tree=parse_tuple(binarytuple)
# c=parse_tuple(None,binarytuple)
# c.display(c,0)
# b=find_node(c,-12000)
def count_height(node,height=0):
    if node is None:
        return height
    left=count_height(node.left,height+1)
    right=count_height(node.right,height+1)
    return max(left,right)
def avl_tree(node,height=0):
    print('-----------------------')
    if node.left is None and node.right is None:
        return node,height
    node.left,height_left=avl_tree(node.left,height+1)
    node.right,height_right=avl_tree(node.right,height+1)
    is_balance=height_left-height_right
    if is_balance>=2:
        print(is_balance,node.data)
        left=count_height(node.left.left)
        right=count_height(node.left.right)
        if left<right:
            prev=node.left.right.left
            node.left,node.left.left=node.left.right,node.left
            node.left.left.right=prev
        prev=node.left.right
        node,node.right=node.left,node
        node.right.left=prev
    elif is_balance<-1:
        print(is_balance,node.data)
        left=count_height(node.right.left)
        right=count_height(node.right.right)
        if left>right:
            prev=node.right.left.right
            node.right,node.right.right=node.right.left,node.right
            node.right.right.left=prev
            node.display(node)
            node.display(node)
        prev=node.right.left
        node,node.left=node.right,node
        node.left.right=prev
        
    return node,max(height_left,height_right)
tree.display(tree)
e=avl_tree(tree)[0]
print('----------------------')
e.display(e)
#hi2