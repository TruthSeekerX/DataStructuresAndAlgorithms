class city:
    def __init__(self, name, country, population):
        self.n = name
        self.c = country
        self.p = population
    def __gt__(self, other):
        if isinstance(other, city):
            return self.p > other.p
        else:
            raise TypeError("Unsupported operand type for >")

print( city("Vaasa", "Finland", 60308) > city("Kajaani", "Finland", 49831))