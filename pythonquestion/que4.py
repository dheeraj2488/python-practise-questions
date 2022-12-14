class Circle():
    def __init__(self, rad):
        self.radius = rad

    def area(self):
        return 3.14*self.radius**2
    
    def perimeter(self):
        return 2*self.radius*3.14

secondcircle = Circle(9)
print(secondcircle.area())
print(secondcircle.perimeter())