class SomeOperations:
    #constructor ...
    def __init__(self , data ):
        self.data=data

    # a.
    def print_numbers(self):
        """
           Write a loop that prints each of the number on a new  line. 
        """
        for number in self.data:
            print(number)
            print('-'*3)

    #b.
    def print_squares(self):
        """
           Write a loop that prints each number and its aquare on a new line.
        """
        print('number\tsquare')
        print('='*20)
        for number in self.data:
            print(number , '\t' , number**2)


     #c.
    def find_summation(self):
         total = 0
         for number in self.data:
             total+=number
         return total

    #d.
    def find_production(self):
        total = 1
        for number in marks:
            total *= number 
        return total




### Driver Code ###
marks = [ 12 , 10 , 32 , 3 , 66 , 17 , 42 , 99 , 20 ]
print('Our data is: ',marks)

# Create an object of someOperations
computer = SomeOperations(marks)

print('*'*90)
# Tell op1 to apply print_numbers() method
computer.print_numbers()

print('*'*90)
# Tell op1 to apply print_squares() method
computer.print_squares()

print('*'*90)
# Tell op1 to apply find_summation() method
summ = computer.find_summation()
print('sum of marks = ' , summ)


print('*'*90)
#Tell op1 to apply find_production() method
produ = computer.find_production()
print('production of marks = ',produ)
