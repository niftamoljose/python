class employee:
    def __init__ (self, name, salary):
        self.name= name
        self.salary= salary
    def displayemployee(self):
        print("Name=", self.name )
        print("salary=", self.salary)
empl1=employee("anju", 3000)
empl2=employee("abu", 4300)
empl3=employee("jain", 5000)

empl1.displayemployee()
empl2.displayemployee()
empl3.displayemployee()