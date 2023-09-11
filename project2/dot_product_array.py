class MyArray:
    def __init__(self, arr):
        self.a = arr

    def __len__(self):
        return len(self.a)
        
    # this method overloads indexing operator [] for a list member
    # a = MyArray([1,2,3])
    # a[1] will give you 2    
    def __getitem__(self, i):
        return self.a[i]
        
    def __mul__(self, other):
        if isinstance(other, MyArray):
            if(len(self.a) > 0 and len(self.a) == len(other.a)):
                arr = 0
                for i in range(0, len(self.a)):
                    arr += self.a[i]*other.a[i]
                return arr
            else:
                raise TypeError("Check array size!")
        else:
            raise TypeError("Unsupported operand type for *")

print(MyArray([1,2,3])*MyArray([4,5]))
