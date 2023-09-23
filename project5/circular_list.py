class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLL:
    def __init__(self):
        self.head = None
        self.length = 0

    def printList(self):
        cur = self.head
        print(cur.data, end=" ")        # print 1st node
        cur = cur.next
        while cur != self.head:
            print(cur.data, end=" ")
            cur = cur.next

    def append(self, node):
        cur = self.head
        if cur is None:
            self.head = node
            node.next = self.head
            self.length += 1
            return

        while cur.next != self.head:
            cur = cur.next
        cur.next = node
        node.next = self.head
        self.length += 1

    def __len__(self):
        return self.length
    
    def removehead(self):
        temp = self.head
        self.head = self.head.next
        self.length -= 1

    def removetail(self):
        i = 1
        currentNode = self.head
        while i <= self.length - 1:
            currentNode = currentNode.next
        tail = currentNode.next
        currentNode.next = tail.next
        # tail.dispose()
        self.length -= 1

        pass

mylist = CircularLL();
n1 = Node(1)
mylist.append(n1)
mylist.append(Node(2))
mylist.append(Node(4))
mylist.printList()
mylist.append(Node(3))
mylist.printList()
