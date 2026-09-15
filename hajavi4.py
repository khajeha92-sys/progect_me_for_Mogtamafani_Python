# inde name of GOD

#3.

print('3.Giv the logical opposites of these conditions.')
print('1. a > b  =>  a <= b \n2. a >= b => a < b \n3. a >= 18 and day == 3 => a < 18 or day != 3 \n4. a >= 18 and day != 3 => a < 18 or day == 3 \n')

print('*'*60)

#4.

print('\n4. What do these expessions evaluate to?')
print('1. 3 == 3 => True \n2. 3 != 3 => False \n3. 3 >= 4 => False \n4. not( 3 < 4 ) => False ')

print('*'*60)

#5.

print('\n5.Complete this truth table:')
print('p   q   r   (not(p and q))or r')
print('='*30)
print(f"F   F   F   T\n{'-'*30}\nF   F   T   T\n{'-'*30}\nF   T   F   T\n{'-'*30}\nF   T   T   T\n{'-'*30}\nT   F   F   T\n{'-'*30}\nT   F   T   T\n{'-'*30}\nT   T   F   F\n{'-'*30}\nT   T   T   T")

print('*'*60)

#6.

print('\n6.Write a function which is give an exam make , and it returns a string-the grate for that mark-according to this scheme:')

def grade(mark):
    if mark >= 75:
        return 'First'
    elif 70 <= mark < 75:
        return 'Upper Second'
    elif 60 <= mark <70:
        return 'Second'
    elif 50 <= mark <60:
        return 'Third'
    elif 45 <= mark <50:
        return '4'
    elif 40 <= mark <45:
        return '5'
    else:
        return '6'

xs =[83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

print('Mark   Grade\n'+'='*30)
for x in xs:
    print(x,'=> ',grade(x),'\n','-'*30)


print('*'*60)    

#7. 8. 9.

print('\n7.Modify the turtle bar chart program so that the pen is up for the small gaps between each bar .\n8.Modify the turtle bar chart program so that the bar for any value of 200 or more is filled with red, valuse between [100and200] \n are filled with yeyellow , and bars representing values less than 100 are filled with green.\n9. In the turtle bar chart program, what do you expect to happend if one or more of the data values in the list is negative? Try it \n out .Change the program so that when it prints the text value for the negative bars , it puts the text below the bottom of the \n bar.')

import turtle

def color(tr,h):
    if h >= 200:
        tr.fillcolor('red')
    elif 100 <= h < 200:
        tr.fillcolor('yellow')
    elif 0 <= h < 100:
        tr.fillcolor('green')
    else:
        tr.fillcolor('gray')

def mark_bar(tr, hs:list, bar_width,gap):
    for h in hs:
        color(tr,h)
        tr.begin_fill()
        tr.lt(90)
        tr.fd(h)
        tr.write('   '+str(h),font=('times new roman',10,'italic'))
        tr.rt(90)
        tr.fd(bar_width)
        tr.rt(90)
        tr.fd(h)
        tr.end_fill()
        tr.lt(90)
        tr.fd(gap)

wn = turtle.Screen()
amirabas = turtle.Turtle()
amirabas.speed('fastest')
amirabas.pencolor('gold')
amirabas.pensize(3)
hs=[48, 117, -30, 200, 240, -60, 160, 260,-90, 220]
mark_bar(tr=amirabas, hs=hs, bar_width=40,gap=10)

wn.mainloop()





