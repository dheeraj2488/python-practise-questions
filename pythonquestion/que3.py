class Rectangle():
    def __init__(self, lengths, widths):
        self.length = lengths
        self.width  = widths

    def rectangle_area(self):
        return self.length*self.width

newRectangle = Rectangle(12, 10)
print(newRectangle.rectangle_area())