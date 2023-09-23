# If binary tree has N layers
# 1. The number of nodes in a fully-proper binary tree is 2^N - 1
# 2. If this tree is represented by a positional array. The starting index of layer k is 2^(k-1)-1

class Node:
    def __init__(self, dataval=None):
      self.val = dataval
      self.lchild = None
      self.rchild = None
      self.parent = None

def traversal_in_order(root):
    if root:
        traversal_in_order(root.lchild)
        print(root.val, end=" ")
        traversal_in_order(root.rchild)

def insert_in_order(root, node):
    if root:
        if root.lchild == None:
            root.lchild = node
        elif root.rchild == None:
            root.rchild = node
        else:
            insert_in_order(root.lchild, node)

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

def remove_leaf(root, leaf, depth):
    result = None
    if root:
        if root.val == leaf.val and root.lchild is None and root.rchild is None:
            print("remove {} at depth {}".format(root.val, depth))
            return None

        root.lchild = remove_leaf(root.lchild, leaf, depth + 1)
        root.rchild = remove_leaf(root.rchild, leaf, depth + 1)
        result = root
    return result

def find_depth(root, currentDepth) -> int:
    depth = 0
    if root:
        if root.lchild is None and root.rchild is None:
            return currentDepth
        
        ldepth = find_depth(root.lchild, currentDepth + 1)
        rdepth = find_depth(root.rchild, currentDepth + 1)
        depth = ldepth if ldepth > rdepth else rdepth
        return depth
    else:
        return None
    
def count_leaves(root) -> int:
    if root:
        if root.lchild is None and root.rchild is None:
            return 1
        
        lcount = count_leaves(root.lchild)
        rcount = count_leaves(root.rchild)

        return lcount + rcount

if __name__ == "__main__":
    root = Node(1)
    root.lchild = Node(2)
    root.rchild = Node(3)
    root.lchild.lchild = Node(4)
    root.lchild.rchild = Node(5)
 
    # Function call
    print('Inorder traversal: ')    
    traversal_in_order(root)
    print("depth:{}".format(find_depth(root, 0)))
    print("leaves:{}".format(count_leaves(root, )))
    print()
    insert_in_order(root, Node(6))
    insert_in_order(root, Node(7))
    print('New traversal: ')
    traversal_in_order(root)
    print()
    print("depth:{}".format(find_depth(root, 0)))
    print("leaves:{}".format(count_leaves(root, )))
    print("pre_order")
    pre_order(root)
    print()
    print("post_order")
    post_order(root)
    remove_leaf(root, Node(6), 0)
    remove_leaf(root, Node(7), 0)
    print()
    print("depth:{}".format(find_depth(root, 0)))
    print("leaves:{}".format(count_leaves(root, )))
    print('Inorder traversal: ')    
    traversal_in_order(root)




#       1
#     2   3
#    4 5
#   6 7