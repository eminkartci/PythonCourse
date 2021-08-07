

class Line:

    def __init__(self,x1=0,y1=0,x2=1,y2=1):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def length(self):
        # d=√((x_2-x_1)²+(y_2-y_1)²) => Line Length Equation 2 Points
        return ((self.x1-self.x2)**2+(self.y1-self.y2)**2)**(1/2)

    def slope(self):
        if(self.x1 == self.x2):
            print("The slope is undefined !")
            return None

        return (self.y1-self.y2)/(self.x1-self.x2)

    def moveX(self,addX=0,addY=0):
        self.x1 += addX
        self.y1 += addY


line1 = Line()
line2 = Line(2.7,-0.5,2.7,3)

print("Line 1 Length: ",line1.length())
print("Line 2 Length: ",line2.length())

line1.moveX(1,3)

print("Line 1 Length: ",line1.length())
print("Line 2 Slope: ",line2.slope())

