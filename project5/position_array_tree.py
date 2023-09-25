# If binary tree has N layers
# 1. The number of nodes in a fully-proper binary tree is 2^N - 1
# 2. If this tree is represented by a positional array. The starting index of layer k is 2^(k-1)-1

def is_leaf(positional_array, index):
    # Check if the index is within the bounds of the array
    if index >= len(positional_array):
        return False  # Index out of bounds, not a leaf

    # Check if both left and right children are None or out of bounds
    left_child_index = 2 * index + 1    # If 𝑝 is the left child of position 𝑞, then 𝑓(𝑝)=2𝑓(𝑞)+1
    right_child_index = 2 * index + 2   # If 𝑝 is the right child of position 𝑞, then 𝑓(𝑝)=2𝑓(𝑞)+2

    left_child_is_none = (left_child_index >= len(positional_array)) or (positional_array[left_child_index] is None)
    right_child_is_none = (right_child_index >= len(positional_array)) or (positional_array[right_child_index] is None)

    return left_child_is_none and right_child_is_none

def evaluate_position_array(array, index):
    result = float()
    if index < len(array):
        if array[index] is not None:
            if is_leaf(array, index):
                return array[index] # all the number are leaves (external nodes)
            else:
                # all the operators are internal nodes
                lchild = evaluate_position_array(array, 2 * index + 1) # If 𝑝 is the left child of position 𝑞, then 𝑓(𝑝)=2𝑓(𝑞)+1
                rchild = evaluate_position_array(array, 2 * index + 2) # If 𝑝 is the right child of position 𝑞, then 𝑓(𝑝)=2𝑓(𝑞)+2
                if array[index] == '+':    
                    result = lchild + rchild
                elif array[index] == '-':
                    result = lchild - rchild
                elif array[index] == '*':
                    result = lchild * rchild
                elif array[index] == '/':
                    result = lchild / rchild
                return result
        else:
            return None
        
def traversal_in_order(array, index):
    result = str()
    if index < len(array):
        if array[index] is not None:
            if is_leaf(array, index):
                return str(array[index]) # all the number are leaves (external nodes)
            else:
                # all the operators are internal nodes
                lchild = traversal_in_order(array, 2 * index + 1) # If 𝑝 is the left child of position 𝑞, then 𝑓(𝑝)=2𝑓(𝑞)+1
                rchild = traversal_in_order(array, 2 * index + 2) # If 𝑝 is the right child of position 𝑞, then 𝑓(𝑝)=2𝑓(𝑞)+2
                if lchild is not None and rchild is not None:
                    result = '(' + lchild + array[index] + rchild + ')'
                return result
        else:
            return None

def count_leaves_array(array) -> int:
    count = 0
    treeLength = len(array)
    for i in range(treeLength):
        lchild = i * 2 + 1
        rchild = i * 2 + 2
        if lchild >= treeLength and rchild >= treeLength and array[i] is not None:
            count += 1
        elif array[i] is not None and lchild < treeLength and rchild < treeLength and array[lchild] is None and array[rchild] is None:
            count += 1
    return count


btree = ['-', '/', '+', '*', '+', '*', 6, '+', 3, '-', 2, 3,
            '-', None, None, 3, 1, None, None, 9, 5, None, None, 
            None, None, 7, 4, None, None, None, None]


result = evaluate_position_array(btree, 0)
print(result)

result = traversal_in_order(btree, 0)
print(result)

t = [3, 1, 2, 4, 5, None, 6, 7, None, None, 8]
print("leaves:{}".format(count_leaves_array(btree)))
print("leaves:{}".format(count_leaves_array(t)))