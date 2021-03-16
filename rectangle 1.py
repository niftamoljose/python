class rectangle1:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2 * (self. length + self. breadth)
print("rectangle")
a=int(input( "enter the length "))
b=int(input("enter the breadth"))
obj=rectangle1(a, b)
print ("area1=", obj.area())
print("perimeter=", obj.perimeter())

print("rectangle1")
a1=int(input("enter the length"))
b1=int(input("enter the breadth"))
obj=rectangle1(a1, b1)
print("area2=", obj.area())
print("perimeter=", obj.perimeter())


if obj.area() == obj.area():
    print("the rectangles have same area")
else:
    print("not equal")