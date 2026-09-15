#IN THE NAME OF GOD
#MADE IN AMIRABAS KHAJEH FOR MR HAJAVI
#PROGECT FOR CLASS 1

import string

#BMI Chart: Body Mass Index Ranges
def bmi_classification(bmi):
    for bmi in BMIS :
        if bmi < 18.5:
            print(f"{bmi = }\t'Underweight'")
        if 18.5 <= bmi < 24.9:
            print(f"{bmi = }\t'Healthy Weight'")
        if 25.0 <= bmi < 29.9:
            print(f"{bmi = }\t'Overweight'")
        if 30.0 <= bmi < 34.9:
            print(f"{bmi = }\t'Obese Class 1'")
        if 35.0 <= bmi < 39.9:
            print(f"{bmi = }\t'Obese Class 2'")
        if 40.0 <= bmi :
            print(f"{bmi = }\t'Obese Class 3'")


#Write a 'while' loop that starts at the last
#character in the string and works its way backwards to
#the first character in the string. printing each letter
#on a separate line. For reference, the CoodeLens above
#shows an example of a word printer letter by letter.            
def last_character_in_the_string():
    i = len(string.ascii_lowercase)
    while 0 < i:
        i-=1
        print(string.ascii_lowercase[i])

###CHAPTER PROBLEMS (2 PROBLEMS)
#1.Problem 1: Write a Python program that uses the 'print()'
#function to display your full name ,age ,and favorite
#city on three separate lines. Add a commend explaining
#what the program does.
def print_():
    print(""" Amirabas Khajeh
Age: 20
living in Tehran But love Nor in Mazandaran
I want programing...""")

#2.Problem2: Write a program that sets x = 5 and y = 10,
#then calculates and print the result of x * y + 10.
#Also print a message like "The result is : [result]".
def X_and_Y():
    x = 5
    y = 10
    result = x * y + 10
    print(f'{result = }')

#CHAPTER PROJECT
#Project:"My First Conputer Profile"
#Create a complete Python program that:
#1.Stores your name, age, and favorite subject in
#'three different variable.'
#2.Prints a summary using 'print()'statements, like:
#"My name is [name] . I am [age] years old and I love
#[subject]."
#3.Includes at least two comments explaining what the
#program does.
#4.(Bonus) And an input section that asks the user for
#thir name and prints a personalized reply.
def my_first_computer_profile():
    name = input("Enter your name: ")
    age = input('Enter your age: ')
    obj = input('Enter your lovely points:')
    print(f""" My name is {name} . I am {age} years old and
I love {obj}.""")

### Driver Code ###
print("""Project 1.
BMI Chart: Body Mass Index Ranges:""")
BMIS = [10, 20, 30, 44, 22, 70, 90, 100]
bmi_classification(BMIS)
print('*'*90)
print("""Project 2.
Write a 'while' loop that starts at the last
character in the string and works its way backwards to
the first character in the string. printing each letter
on a separate line. For reference, the CoodeLens above
shows an example of a word printer letter by letter.            
""")
last_character_in_the_string()
print('*'*90)
print("""CHAPTER PROBLEMS (2 PROBLEMS)
Project 3.1.
Problem 1: Write a Python program that uses the 'print()'
function to display your full name ,age ,and favorite
city on three separate lines. Add a commend explaining
what the program does.
""")
print_()
print('*'*90)
print("""Project 4.2.
2.Problem2: Write a program that sets x = 5 and y = 10,
then calculates and print the result of x * y + 10.
Also print a message like "The result is : [result]".
""")
X_and_Y()
print('*'*90)
print("""CHAPTER PROJECT
Progect 5.1.
CHAPTER PROJECT
Project:"My First Conputer Profile":
""")
my_first_computer_profile()
print('*'*90)
print("MADE IN AMIRABAS KHAJEH FOR MR HAJAVI ")



