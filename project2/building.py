class building():
    def __init__(self, size, year, floor):
        self.size = size
        self.year = year
        self.floor = floor
        pass
    def __str__(self):
        floor = "floor" if int(self.floor) == 1 else "floors"
        return f"Building, size:{self.size}, year:{self.year}, {self.floor} {floor}"

class office(building):
    def __init__(self, size, year, floor, type):
        super().__init__(size, year, floor)
        self.type = type
        pass
    def __str__(self):
        offset = len("Building, ")
        return f"Office (type:{self.type}), {super().__str__()[offset:]}"

class townhouse(building):
    def __init__(self, size, year, floor, division):
        super().__init__(size, year, floor)
        self.division = division
        pass
    def __str__(self):
        offset = len("Building, ")
        return f"Townhouse (division:{self.division}), {super().__str__()[offset:]}"

class singlehouse(building):
    def __init__(self, size, year, floor, material):
        super().__init__(size, year, floor)
        self.material = material
        pass
    def __str__(self):
        offset = len("Building, ")
        return f"Singlehouse (material:{self.material}), {super().__str__()[offset:]}"


if __name__ == '__main__' :
    a=[]
    a.append(building(100,1990,3))
    a.append(office(3000,1963,4,"school"))
    a.append(singlehouse(103,2010,1,"wood"))
    a.append(townhouse(408,1999,2,5))
    # for i in range(len(a)):
    #     print(a[i])
    
    for i in a:
        print(i)