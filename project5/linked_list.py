class Node:
   def __init__(self, dataval=None):
      self.data = dataval
      self.next = None


class SingleLL:
    def __init__(self):
        self.head = None

    def printList(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next
			
    def __len__(self):
        k = 0
        cur = self.head
        while cur is not None:
            k+=1
            cur = cur.next
        return k
    
    def insert(self, node, loc):
        if loc==0:
            node.next = self.head
            self.head = node
        else:
            k = 0
            cur = self.head
            while k < loc - 1: # should only iterate to the node prior to the desired one
                k += 1
                cur = cur.next
                if cur.next is None: break  # should check cur.next instead of cur. 
                                            # Otherwise, cur.next became None.next. Seg fault
            if cur.next is None:   # loc > size, append
                cur.next = node
            else:           # insert
                node.next = cur.next
                cur.next = node
    
    def delete(self, loc) -> None:
        if self.__len__ is 0:
            raise MemoryError("The list is empty, nothing to remove")
        elif loc < 1:
            raise IndexError("Bad index, Location is smaller then 1.")
        elif len(self)  < loc:
            raise IndexError("Bad index, Location is out of range of current list.")
        else:
            if loc == 1:
                self.head = self.head.next
            else:
                k = 1
                currentNode = self.head
                while k < loc - 1:  # stop at the node prior to the index
                    k += 1
                    currentNode = currentNode.next
                temp = currentNode.next
                currentNode.next = temp.next

    def delete_alt(self, loc):
        if self.__len__ is 0:
            raise MemoryError("The list is empty, nothing to remove")
        elif loc < 0:
            raise IndexError("Bad index, Location is smaller then 1.")
        else:
            if loc >= len(self):
                loc = len(self) - 1
            if loc == 0:
                temp = self.head
                self.head = temp.next
                return temp
            else:
                k = 0
                currentNode = self.head
                while k < loc - 1:  # stop at the node prior to the index
                    k += 1
                    currentNode = currentNode.next
                temp = currentNode.next
                currentNode.next = temp.next
                return temp
                


mylist = SingleLL()
mylist.head = Node(1)
e2 = Node(2)
e3 = Node(4)
# Link first Node to second node
mylist.head.next = e2

# Link second Node to third node
e2.next = e3
mylist.printList()
print('Len: %d'%(len(mylist)))
mylist.insert(Node(3), 2)
mylist.printList()
print("delete:{}".format(mylist.delete_alt(5).data))
mylist.printList()
# mylist.delete(e2)
# mylist.printList()
# mylist.delete(1)
# mylist.printList()