class Bike:
    def __init__(self,name, color):
        self.name = name
        self.color = color


    def display(self):
        print(f"Name  ={self.name}, Color = {self.color}")


    def __str__(self, other):
        return self.name == other.name and self.color == other.color


    def __eq__(self, other):
        return self.name == other.name and self.color == other.color


bike1 = Bike("R15,FZ","Blue")
bike2 = Bike("Yamaha fz,","Blue")
print(bike1 == bike2)
print(bike1 != bike2)
