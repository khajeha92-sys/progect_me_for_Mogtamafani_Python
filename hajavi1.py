class Calculator:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y

    def mul(self):
        return self.x * self.y

    def truediv(self):
        return self.x / self.y

    def floordiv(self):
        return self.x // self.y

    def rem (self):
        return self.x % self.y

    def exp(self):
        return self.x ** self.y



### main program ###
while True:

    computer = Calculator(int(input('x=')),int(input('y=')))
    
    operation=input("Enter operation (+,-,*,/,//,%,**)or(q) to quit:")

    if operation == '+':
        print("Result:",computer.add())
        
    elif operation == '-':
        print("Result:",computer.sub())
        
    elif operation == '*':
        print("Result:",computer.mul())
        
    elif operation == '/':
        print("Result:",computer.truediv())
        
    elif operation == '//':
        print("Result:",computer.floordiv())
        
    elif operation == '%':
        print("Result:",computer.rem())
        
    elif operation == '**':
        print("Result:",computer.exp())

    elif operation == 'q' :
        print('Goodbye!')
        break
        
    else :
        print("ERORE")


    print('------------------------')    




    
    



