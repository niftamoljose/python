class rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        area = self.length * self.breadth
        print("Area of Rectangle: " + str(area) + "m^2")

    def perimeter(self):
        peri = 2 * (self.length + self.breadth)
        print("Perimeter of Rectangle:" + str(peri) + "m")

    def __lt__(self, other):
        a1 = self.length * self.breadth
        a2 = other.length * other.breadth
        if a1 > a2:
            print("The greater is the first one" + str(a1) + "m^2")
        else:
            print("The greater is the second one" + str(a2) + "m^2")


leng1 = int(input("Enter length of First Rectangle:"))
bred1 = int(input("Enter breadth of First Rectangle:"))
leng2 = int(input("Enter length of Second Rectangle:"))
bred2 = int(input("Enter breadth of Second rectangle:"))

rect1 = rectangle(leng1, bred1)
rect2 = rectangle(leng2, bred2)
print("FIRST RECTANGLE\n\n")
rect1.area()
rect1.perimeter()
print("\n\nSECOND RECTANGLE\n\n")
rect2.area()
rect2.perimeter()
print(rect1 < rect2)