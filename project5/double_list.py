class Node:
   def __init__(self, postCode, officeName):
      self.postcode = postCode
      self.officeName = officeName
      self.prev = None
      self.next = None

class DoulbleLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def printList(self):
        cur = self.head
        while cur is not None:
            print(cur.officeName, end="")
            if cur is not self.tail:
                print('-',end="")
            cur = cur.next

    def printListRev(self):
        cur = self.tail
        while cur is not None:
            print(cur.officeName, end="")
            if cur is not self.head:
                print('-',end="")
            cur = cur.prev
			
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
            self.tail = node
        else:
            k = 0
            cur = self.head
            while k<loc:
                k += 1
                cur = cur.next
                if cur == None: break
            if cur==None:   # loc > size, append
                cur.next = node
            else:           # insert
                node.next = cur.next
                cur.next = node

    def append(self, node):
            if self.head is None:
                self.head = node
                self.tail = node
            else:
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
    
    # def delete(self, node) -> bool:
    #     result = False
    #     if self.head is node:
    #         temp = self.head
    #         self.head = self.head.next
    #         # temp.dispose() # How to release memory here?
    #         return True
    #     else:
    #         currentNode = self.head
    #         if currentNode.next is None:
    #             return False
            
    #         while currentNode.next is not node:
    #             currentNode = currentNode.next
    #             if currentNode.next is None:
    #                 return False
    #         temp = currentNode.next
    #         currentNode.next = temp.next
    #         # temp.dispose()
    #         return result
    
    def delete(self, loc) -> None:
        if self.__len__ == 0:
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
                # temp.dispose()

track = DoulbleLL()
track.append(Node(15100, "HEL"))
track.append(Node(25100, "TAM"))
track.append(Node(35100, "SEI")) 
track.append(Node(65100, "VAA"))  

track.printList()
print()
track.printListRev()