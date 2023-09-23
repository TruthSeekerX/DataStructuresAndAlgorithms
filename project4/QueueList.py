class QueueList:
    def __init__(self, maxsize):
        self.size = maxsize
        self.start = 0
        self.len = 0
        self.qlist = [None]*maxsize

    def __len__(self):
        return self.len

    def print(self):
        for i in range(self.len):   # print all elements
            loc = (self.start+i)%self.size
            print(self.qlist[loc], end=' ')
        print()     # print a new line
    
    def first(self):    # return (not remove) the 1st element
        return self.qlist[self.start]

    def is_empty(self):
        return self.len == 0
    
    def enqueue(self, e):       # add an element at end
        if self.len == self.size:
            print("Queue is full")
            return
        else: # add the element at end
            loc = (self.start+self.len)%self.size
            self.qlist[loc]=e
            self.len += 1

    def dequeue(self):          # remove an element from head
        if(self.is_empty()):
            print("Queue is empty")
            return
        else:
            a = self.qlist[self.start]
            self.qlist[self.start] = None
            self.start += 1
            if self.start == self.size: self.start = 0
            self.len -= 1
            return a

    def drop(self):  # please implement this function
        if self.len != 0:
            index = (self.start+self.len-1)%self.size
            self.qlist[index] = None
            self.len -= 1

a = QueueList(5)
for i in range(6):
  a.enqueue(i)  

a.dequeue()
a.drop()
a.print()
