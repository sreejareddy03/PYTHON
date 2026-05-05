class Rect:
    def __init__(slef,a,b):
        slef.area=a*b
    def display(self):
        print("Area is ",self.area)

r=Rect(20,30)
r2=Rect(40,67)
r.display()
r2.display()
