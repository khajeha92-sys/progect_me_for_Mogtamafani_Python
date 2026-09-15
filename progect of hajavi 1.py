#IN THE NAME OF GOD
#This progect of mogtamaFane of MR Hajavi

import random
import re
#import sys

#1. mohasebate Amare

def bakhshpazir5(x):
    result = 0
    for i in x:
        if i % 5 == 0:
            result += 1
    return result

def miangin(y):
    result = 0
    total = 0
    for i in y:
        if i % 2 != 0:
            result += 1
            total += i
    if result == 0:
        return 0
    return total / result

def zarbManfi (z):
    result = 1
    for i in z:
        if i < 0:
            result *= i
    return result

def tedadCharRagam(tc):
    result = 0
    for i in tc:
        if i > 999 and i < 9999 or i > -9999 and i < -999:
            result += 1
    return result

def tedadBjozAvalinZog(t):
    result = 0
    for i in t:
        if i % 2 == 0:
            return len(t) - 1
    return len(t)

def miane(m):
#    for i in range(len(m)):
#        for j in (i + 1, len(m)):
#            if i in t > j in t:
#                 m[i], m[j] = m[j], m[i]
    nums = sorted(m)
    num = len(m)
    vasat = num // 2
    if num % 2 == 0:
        return ( nums[vasat -1] + nums[vasat]) / 2
    else:
        return nums[vasat]

def information1():
    number = [21, 63, -2, -80, 7, 19, 302, 1001, 6430, -2341, 3, -7]
    ba  = bakhshpazir5(number)
    mi  = miangin(number)
    za  = zarbManfi(number)
    tec = tedadCharRagam(number)
    teb = tedadBjozAvalinZog(number)
    mia = miane(number)
    print('The progect 1.')
    print('The number of list is : 21, 63, -2, -80, 7, 19, 302, 1001, 6430, -2341, 3, -7')
    print(f'The number of numbers divisible by 5 in the list is : {ba} .')
    print(f'The average of the odd numbers in the list is : {mi} .')
    print(f'The multiplication of negative numbers in the list is : {za} .')
    print(f'The number of four-digit numbers in the list is : {tec} .')
    print(f'The total number of numbers other than the first even number : {teb} .')
    print(f'The median of all the numbers in the list is : {mia} .')
    
#2. sang_Kagaz_Gichi

def sang_kagaz_gichi():
    while True:
        play = input('Play(yes/no)? ')
        if play == 'yes':
            info = input('enter your acction (rock, paper, scissors): ')
            print(f'user acction is: {info}')
            sang_kagaz_gichi2(info)
        elif play == 'no':
            return False

def sang_kagaz_gichi2(s2):
    word = ['rock', 'paper', 'scissors']
    com = random.choice(word)
    print(f'computer acction is: {com}')
    if s2 == com:
        print('it is a tie')
    elif s2 == 'rock' and com == 'scissors':
        print('user won')
    elif s2 == 'scissors' and com == 'paper':
        print('user won')
    elif s2 == 'paper' and com == 'rock':
        print('user won')
    else: print('computer won')    

#3.
def josef(n,k):
#    people = list(range(1, n + 1))
#    index = 0
#
#    while len(people) > 1:
#        index = (index + k - 1) % len(people)
#        people.pop(index) #delit
#
#    return people[0]    

    index = 0
    for people in range(1, n + 1):
        index = (index + k) % people
    return index + 1    

def info3():
    n = 10
    k = 2
    print(f'makan amn: {josef(n, k)}')
    
#4.
def guess_generated_number(x):
    num = 0
    while True:
        num += 1
        result = int(input('Enter your guess number in 1 until 1000: '))
        if x > result:
            print('Your guess is too small')
        elif x < result:
            print('Your guess is too large')
        else:
            print('Horra')
            print(f'You woun after {num} steps.')
            return False
        
def info4():
    computer_action = random.randrange(1, 1001)
    guess_generated_number(x = computer_action)

#5.
def quick_sort(l):
    if len(l) <= 1:
        return l

    vasat = l[len(l) // 2]
##    left = []
##    mid = []
##    right = []
##    
##    for x in l :
##        if x < vasat:
##            #left.append(x)
##            left = [x]
##        elif x > vasat:
##            #right.append(x)
##            right = [x]
##        else:
##            #mid.append(x)
##            mid = [x]       

    left = [x for x in l if x < vasat]
    mid = [x for x in l if x == vasat]
    right = [x for x in l if x > vasat]

    return quick_sort(left) + quick_sort(mid) + quick_sort(right)
   
def mergent_sort(l):
    if len(l) <= 1:
        return l
    mid = len(l) // 2
    left = mergent_sort(l[:mid])
    right = mergent_sort(l[mid:])

    return mergent(left, right)

def mergent(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def info5():
    lis = input('Enter your number with kama exampel(3,4,...) : ')
    listt = list(map(int,lis.split(',')))
    print(f'your Quick Sort list is : {quick_sort(listt)}')
    print(f'your Mergent Sort list is : {mergent_sort(listt)}')

#6.
def binarySearch(arr, x , low, high):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:   # x is on the right side
            low = mid + 1
        else:                # x is on the left side
            high = mid - 1
    return -1

def serch_2(arr, x):
    result = binarySearch(arr, x , 0, len(arr) - 1)
    if result != -1:
        print(f'Element is present at index {str(result)}')
    else:
        print('Not found')

def info6():
    arr = [3, 4, 5, 6, 7, 8, 9]
    x = 4
    serch_2(arr , x)

#7.
##def fib_1(n):
##    if n == 0 : return 0
##    if n == 1 : return 1
##    return fib_1(n - 1) + fib_1(n - 2)

      

m = {}
def fib_2(n):
    if n in m : return m[n]
    if n == 0 : return 0
    if n == 1 : return 1

    m[n] = fib_2(n - 1) + fib_2(n - 2)
    return m[n]

def info7():
##    print(f'{fib_1(50)}')
    print(fib_2(1000))

#8.
def read_matrix_shape():
    r = int(input('Enter number of rows of the matrix: '))
    c = int(input('Enter number of cols of the matrix: '))
    return r, c

def read_matrix_entries(shape):
    r, c = shape
    matrix = []

    for i in range(r):
        r = []
        for j in range(c):
            value = int(input(f'Enter matrix [{i}][{j}] : '))

            r.append(value)
        matrix.append(r)
    return matrix    

def is_sparse(matrix):
    total = 0
    zero = 0

    for r in matrix:
        for value in r:
            total += 1
            if value == 0:
                zero += 1
                
    s = zero / total
    print(f'sparsity = {s}, matrix is sparse if sparsity >= 0.8')

    if s >= 0.8 : return 'is sparse'
    else: return 'is not sparse'
        
def info8():
    shape = read_matrix_shape()
    matrix = read_matrix_entries(shape)

    print('nmatrix is : ')
    for r in matrix:
        print(r)
    
    result = is_sparse(matrix)
    print(result)

#9.
class Stak:
    def __init__(self):
        self.item = []
    def push(self, x):
        self.item.append(x)
    def pop(self):
        return self.item.pop()

def eval_postfix(expr):
    s = Stak()
    token_list = expr.split()
    for token in token_list:
        if token == ' ' or token == '' : continue
        elif token == '+' :
            b = s.pop()
            a = s.pop()
            s.push(a + b)
        elif token == '*' :
            b = s.pop()
            a = s.pop()
            s.push(a * b)
        elif token == '/' :
            b = s.pop()
            a = s.pop()
            s.push(a / b)
        elif token == '-' :
            b = s.pop()
            a = s.pop()
            s.push(a - b)
        else : s.push(int(token))
        
    return s.pop()

def info9():
    print(eval_postfix("56 47 + 2 *")) #206
    print(eval_postfix('1 2 + 3 *'))   #9
    print(eval_postfix('2 6 3 / 4 - *')) #-4.0

def check():
    try:
        for i in range(3):
            try:
                1 / 0
            except ZeroDivisionError:
                raise ZeroDivisionError('Error: You divided by zero!')
            finally:
                print('Finally executed')
                break   
    except ZeroDivisionError:
        print('Outer ZerroDivisionError exception caught')

    
###Code ###
def code():    
    #information1()
    print('*'*33)
    print('The progect 2.')
    #sang_kagaz_gichi()
    print('*'*33)
    print('the progect 3.')
    #info3()
    print('*'*33)
    print('the progect 4.')
    #info4()
    print('*'*33)
    print('the progect 5.')
    #info5()
    print('*'*33)
    print('the progect 6.')
    #info6()
    print('*'*33)
    print('the progect 7.')
    #info7()
    print('*'*33)
    print('the progect 8.')
    #info8()
    print('*'*33)
    print('the progect 9.')
    info9()
    print('*'*33)
    print('the progect 10.')
    check()

###Driver Code###
code()    


#MADE OF AMIRABAS KHAJEH
