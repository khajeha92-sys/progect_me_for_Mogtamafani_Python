### Define variable that it's identifier is airtime_remaining
##
##airtime_remaining = 15;
##print(airtime_remaining) #15
##
### Update the value ofairtime_remaining identifier
##
##airtime_remaining = 8
##print(airtime_remaining) #8
##
##
##PI = 3.14
##radius = eval(input('Enter radius of a circle: '))
##
##print(f'The radius of circle is : {radius} ')
##print(f'The perimeter of circle is : {2 * PI * radius} ')
##print(f'The area of circle is : {PI * radius ** 2} ')
##
##
##age = eval(input('Enter your age: '))
##name = input('Enter your name: ' )
##
##print(f'{name} is baby' if age < 12 else  f'{name} is not baby ' )
##
### Grading score
##
##score = eval(input('Enter your score: '))
##
##if   score >= 80 and score <= 100 : print(' A ')
##elif score >= 60 and score < 80 :   print(' B ')
##elif score >= 50 and score < 60 :   print(' C ')
##elif score >= 0  and score < 50 :   print('Failed')
##else:
##    print('Invalid score.')
##    print('Enter valid score in range (0, 101) ' )
##    print('End point of range is\'nt include. ' )
##
##value = eval(input('Enter a number : '))
##
##match value % 2 :
##    case 0 : print('is even')
##    case _ : print('is odd')
##
##    # Enter a number : 33
##    # is odd
##
##
##my_favorite_languages = ['Python', 'SQL', 'C++']
##
###Element base for loop
##for language in my_favorite_languages:
##    print(language)
##
### Get number of items in the my_favorite_languages
##print(len(my_favorite_languages)) #3
##
### Range base for loop
##for index in range(len(my_favorite_languages)):
##    print(index, my_favorite_languages[index])
##
### Get index and corresponding value
##for (index, value) in enumerate(my_favorite_languages):
##    print(index, value)
##
### Linear search for 'SQL' ...
##for languages in my_favorite_languages:
##    if languages == 'SQL':
##        print('I know SQL')
##        break
##else:
##    print('I don\'t know SQL')
##
### Linear search for 'SQL' ...
##
##for index, language in enumerate(my_favorite_languages):
##    if language == 'SQL':
##        print(index)
##        break
##else:
##    print(-1)
##
### guess number
##import random
##x = random.randrange(1, 1001)
### not include 1001
##steps = 0
##while True:
##    steps += 1
##    your_guess = int(input('Enter your guess: '))
##    if   your_guess == x: print(f'won after {steps}. ' ); break
##    elif your_guess  < x: print('Your guss is small. ' )
##    else:                 print('Your guss is larges. ')
def f(x):
    y = x**2
    return y

### Main Program ###
f(2) # Invoke the function f()
print(f(2))


# Python code to illustrate cube of a number
# showing difference between def() and lambada().
def cube(y):
    return y*y*y;

g = lambda x: x*x*x
print(g(7))

print(cube(5))


ages, names = (36, 15, 20), ('hamed', 'hamid', 'maryam')
zipped = zip(ages, names)
zipped_list = list(zipped)

print(zipped_list)
print(sorted(zipped_list))
print(sorted(zipped_list, key = lambda item: item[1]))

# Get unicode ordinal
print('h', ord('h'))
print('m', ord('m'))
print('e', ord('m'))
print('i', ord('i'))


# Get char representation
print(chr(ord('h')))
print(chr(ord('m')))
print(chr(ord('i')))

#
numbers = input('Enter your number:').split(sep = ' ')

for number in numbers:
    print (number, type(number))


mapped = map(int, numbers)
mapped_list = list(mapped)

for number in mapped_list:
    print(number, type(number))


#

class car:
    def __init__(self):
        self.speed = 200  # km/h
        self.color = 'red'

### Driver Code ###
# instantiation
my_car = car()

# access the attributes of instance using dot notation
print(my_car.speed) # output : 200
print(my_car.color) # output : 'red'
    
