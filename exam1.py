x = 5

print('Smaller' if x < 10 else 'Bigger' if x > 20 else 'Normal' )

print('Finis')


print('Befor 5')
if x == 5:
    print('Equals 5')
    print('Is 5')
    print('Is Still 5')
    print('Third 5')
    
elif x > 4:
    print ('Greater than 4')
elif x >= 5:
    print('Greater than or Equals 5')
elif x < 6 : print ('Less Than 6')
elif x >= 5:
    print ('Less than or Equals 5')
elif x != 6:
    print('Not equal6')
#print ('AfterWards 5 ')
#print ('Before 6')
elif x == 6:
    print('Is 6')
    print('Is Still 6')
    print('Third 6')

#print ('AfterWards 6')
elif x > 2:
    print('Bigger than 2')
    print('Still bigger')
#print('Dont with 2')

for i in range(5):
    print(i)
    if i > 2:
        print ('Bigger than 2')
    print('Done With i',i)
    print('All Done')


y = 42

if y > 1 :
    print('More than one')
    if y < 100:
        print('Less than 100')
print('All done')        
    

if x > 2:
    print('Bigger')
elif x < 2:
    print('smaler')
elif x < 10:
    print('Medium')
else:
    print('larges')
    
print('All done')    


u = 0

if u < 2:
    print('smaler')
elif u < 10:
    print('Medium')
else:
    print('LARGE')
print('All done')


q = 5

if q < 2:
    print('small')
elif q < 10:
    print('Medium')
else:
    print('LARGES')
print('All done')

w = 20

if w < 2:
    print('small')
elif w < 10:
    print('Medium')
else :
    print('LARGES')
print('All done')


astr = '123' #'Hello Bob  
try:
    istr = int(astr)
except:
    ister = -1
print('First', istr)    



ast = 'Bob'

try:
    print('Hello')
    ist = int(ast)
    print('There')
except:
     ist = -1

print('Done', ist)       


rawstr = input('Enter a number:')

try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print('Nice work')
else:
    print('Not a number')

print(' * ' * 33)

#Exercise

#1. Rewrite your pay compulation to give the employe 1.5 times the hourly rate for hours worked above 40 hours.?
#Enter Hours:45
#Enter Rate: 10
#Pay: 475.0
#475 = 40 * 10 + 5 * 15

#2. Rewrite your pay program using try and except so that your program handels non-numeric input gracefully.?


def work (Pay, Hours, pay):
    print(f'Pay: {Pay if Hours > 40 else pay}')
    #if Hours >= 40:
    #    Pay = h * Rate + remain * em
    #else:
    #    Pay = Hours * Rate

    #print(f'Pay: {Pay}')

    
try:
    Hours = int(input('Enter Hours: '))
    Rate = int(input('Enter Rate: '))
    remain = Hours - 40 
    h = 40
    em = 15
    Pay = h * Rate + remain * em
    pay = Hours * Rate
except:
    Hours = 60
#    Rate = 60
    Pay = 'ERROR, please enter numeric input'
    pay = 'ERROR'

### Enter Code ###
work(Pay, Hours, pay)
