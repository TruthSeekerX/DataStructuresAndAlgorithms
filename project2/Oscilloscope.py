class Oscilloscope:
    def __init__(self, brand, model, nc, speed) -> None:
        self.bd = brand
        self.md = model
        self.nc = nc
        self.sp = speed
        pass
    def __str__(self) -> str:
        speed = f"{self.sp}MHz" if float(self.sp) < 1000 else f"{float(self.sp)/1000}GHz"
        return f"{self.bd}-{self.md}, {self.nc} channels, {speed}"
        pass

print(Oscilloscope("Tekronix", "TBS2104B", 4, 2000))
print(Oscilloscope("Agilent", "54616B", 2, 500))