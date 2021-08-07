

class QuadEqn:

    def __init__(self,a,b,c,name):
        if (a == 0):
            print("This equation is not quadratic !!")
        else:
            self.a = a
            self.b = b
            self.c = c
            self.name = name

    def delta(self):
        return self.b**2 - 4*self.a*self.c

    def sumOfRoots(self):
        return self.b*-1/self.a

    def multOfRoots(self):
        return self.c/self.a


    def solve(self):
        
        if(self.delta() < 0 ):
            print("There is no real roots!")
            return None
        elif(self.delta() == 0):
            root = (-self.b- self.delta()**(1/2))/(2*self.c)    
            return root
        else:
            root1 = (-self.b- self.delta()**(1/2))/(2*self.c)
            root2 = (-self.b+ self.delta()**(1/2))/(2*self.c)

            return [root1,root2]

    def printEquation(self):
        print(f"{self.a}x^2 + {self.b}x + {self.c} = 0 ")
