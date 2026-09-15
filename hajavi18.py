# IN THE NAME OF GOD

#Exercise 01: Complete the method to comp ute circumference of a circle in the Circle class.?

from math import pi  #that will be used for in the circle methods

#Circle class creation
class Circle :

    #Create constructor
    def __init__(self, radius):
        self.r = radius

    #Create a method to compute the diameter of a circle
    def diameter(self):
        return 2 * self.r

    #Create a method to compute the diameter of a circlr
    def area(self):
       return pi * self.r ** 2

    #exercise 01:
    #Create a method to computer the circumference of circle
    def circumference(self):
        return self.r * 2 * pi

def main():
    #Create a Circle instance and then as sing it to c1
    r = 3
    c1 = Circle(3)
     
    #Compute the dimater of circle c1 using calling the diameter method
    # and then assign it to diam
    diam = round(c1.diameter(), 3)
    area = round(c1.area(), 3)
    circ = round(c1.circumference(), 3)

    #Print the diameter of circle c1 in beautiful formatted version
    print(f'The diameter of circle with radius {r} is : {diam}')
    print(f'The Area of circle with radius {r} is : {area}')
    print(f'The Perimeter of circle with radius {r} is : {circ}')


### Driver Code ###
main()        



print('*'*99)

# Exercise 02 : Impelement class Rectangle based on above like.?

#Class Rectangle creation
class Rectangle:

    #Side-by-side
    def __init__(self, a, b):
        self.a = a
        self.b = b

    #Diameter calculation 
    def Diagonal(self):
        return ((self.a ** 2) + (self.b ** 2)) ** 0.5

    #Area calculation
    def Area(self):
        return self.a * self.b

    #Preimeter calculation
    def Perimeter (self):
        return (self.a + self.b) * 2

#Conclusion
def man ():
    a = 6
    b = 9

    #To value
    c2 = Rectangle(6, 9)

    #To define
    diagonal = round(c2.Diagonal(), 3)
    area = round(c2.Area(), 3)
    perimeter = round(c2.Perimeter(), 3)

    print(f'The diameter of the rectangle {a, b} is : {diagonal}')
    print(f'The area of the rectangle {a, b} is : {area}')
    print(f'The perimeter of the rectangle {a, b} is : {perimeter}')

### Rectangle Deriver Code ###
man()


print('*'*99)
#Exercise 03: implement other operations in different methods besed on its name and concept same as add method...?
#Exercise 04: print other operations results same as a ddition result.?
class Calculator:
    """
    addition : +
    subtraction : -
    multiplication : *
    true division : /
    floor division : //
    remainder : %
    exponentiation : **
    """
    #Create constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #Create addition operation
    def add(self):
        return self.x + self.y

    #Create subtraction operation
    def sub(self):
        return self.x - self.y

    #Create multiplication operation
    def mult(self):
        return self.x * self.y

    #Create true division operation
    def trdi(self):
        return self.x / self.y

    #Create floor division operation
    def fldi(self):
        return self.x // self.y

    #Create remainder operation
    def rema(self):
        return self.x % self.y

    #Create exponentiation operation
    def expo(self):
        return self.x ** self.y

### main program ###
x = 3
y = 4
calculator = Calculator(x, y)

addition = calculator.add()
subition = calculator.sub()
multition = calculator.mult()
trdiition = calculator.trdi()
fldiition = calculator.fldi()
remaition = calculator.rema()
expoition = calculator.expo()

#prints

print(f'The addition of {x} and {y} is : {addition}')
print(f'The subition of {x} and {y} is : {subition}')
print(f'The multition of {x} and {y} is : {multition}')
print(f'The trdiition of {x} and {y} is : {trdiition}')
print(f'The fldiition of {x} and {y} is : {fldiition}')
print(f'The remaition of {x} and {y} is : {remaition}')
print(f'The expoition of {x} and {y} is : {expoition}')


print('*'*99)
#Exercise 05 : Create olympic logo using turtles .?
import turtle

#Definitions
t = turtle.Turtle()
t.speed(5)
t.width(5)

#CSS(Modes)
colors = ['blue', 'black', 'red', 'yellow', 'green']
positions = [(-120, 0), (0, 0), (120, 0), (-60, -60), (60, -62)]

#Command loop
for color, pos in zip(colors, positions):
    t.penup()
    t.goto(pos)
    t.pendown()
    t.color(color)
    t.circle(50)

### Main Code ###
turtle.done()    
