class Node:
    def __init__(self, dataval=None):
      self.val = dataval
      self.lchild = None
      self.rchild = None
      self.parent = None

    def is_leaf(self):
        if self.lchild is None and self.rchild is None:
            return True
        else:
            return False

def traversal_in_order(root):
    if root:
        traversal_in_order(root.lchild)
        print(root.val, end=" ")
        traversal_in_order(root.rchild)

def insert_in_order(root, node):
    if root:
        if root.lchild == None:
            root.lchild = node
            node.parent = root
        elif root.rchild == None:
            root.rchild = node
            node.parent = root
        elif root.lchild.lchild == None or root.lchild.rchild == None:
            insert_in_order(root.lchild, node)
        elif root.rchild.lchild == None or root.rchild.rchild == None:
            insert_in_order(root.rchild, node)

def pre_order(root):
    if root:
        print(root.val, end = " ")
        pre_order(root.lchild)
        pre_order(root.rchild)
    pass

def post_order(root):
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.val, end = " ")
    pass

# def remove_leaf(root, node, depth=None):
#     result = False
#     if depth is None:
#         depth = 0
#     if root:
#         if root == node:
#             if root.is_leaf():
#                 root = None
#                 return True
#         else: # root is not node
#             if root.is_leaf():
#                 if depth is 0:
#                     raise ValueError("leaf not found")
#                 else:
#                     return False
#             else:   # root is not leaf

#             root.lchild = None
#             return True
#         elif root.rchild == node and root.rchild.lchild is None and root.rchild.richild is None:
#             root.rchild = None
#             return True
#         elif root.lchild.lchild == node or root.lchild.rchild == node:
#             result = remove_leaf(root.lchild, node, depth + 1)
#         elif root.rchild.lchild == None or root.rchild.rchild == None:
#             result = remove_leaf(root.rchild,node, depth + 1)
#     if depth is 0 and result is False:
#         raise ValueError("can not find such a leaf")
#     pass

if __name__ == "__main__":
    root = Node(1)
    root.lchild = Node(2)
    root.rchild = Node(3)
    root.lchild.lchild = Node(4)
    root.lchild.rchild = Node(5)
 
#    1
#  2   3
# 4 5 6
    # Function call
    print('Inorder traversal: ')    
    traversal_in_order(root)
    print()
    insert_in_order(root, Node(6))
    print('New traversal: ')
    traversal_in_order(root)
    print()
    insert_in_order(root, Node(7))
    print('New traversal: ')
    traversal_in_order(root)
    print()
    insert_in_order(root, Node(8))
    print('New traversal: ')
    traversal_in_order(root)
    print()
    insert_in_order(root, Node(9))
    print('New traversal: ')
    traversal_in_order(root)
    print()
    # pre_order(root)
    # print()
    # post_order(root)
    # remove_leaf(root, 2, 0)