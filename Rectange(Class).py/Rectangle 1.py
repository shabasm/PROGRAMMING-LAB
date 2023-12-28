class rectangle():
    def _init_(self):
        self.length = int(input("Enter length of rectangle: "))
        self.breadth = int(input("Enter breadth of rectangle: "))

    def area(self):
        self.a = self.breadth * self.length
        print("Area of rectangle: ", self.a)
        return self.a

    def perimeter(self):
        self.p = 2 * (self.length+self.breadth)
        print("Perimeter of rectangle: ", self.p, "\n")


x = rectangle()
print("\n_Rectangle 1_")
x._init_()
a1 = x.area()
x.perimeter()

y = rectangle()
print("\n_Rectangle 2_")
y._init_()
b1 = y.area()
y.perimeter()
