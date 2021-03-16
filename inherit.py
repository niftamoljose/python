class parent:
    parentattribute=20
    def __init__(self):
        print("hello")
    def parentmethod(self):
        print("hi")
class child(parent):
    def __init__(self):
        print("hlo")
    def childmethod(self):
        print("ii")
c=child()
c.childmethod()
c.parentmethod()
