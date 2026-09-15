#IN THE NAME OF GOD
#MADE IN AMIRABAS KHAJEH FOR MR HAJAVI
#CLASS 5


#1. Write a program to read though a file and print the contents of
#the countents of the file (line by line) all in upper case.
#Executing the program will look as follows:
def py_shout():
    fh = open('mbox-short.txt','r')
    text = fh.read()
    up = text.upper()
    print(up)
    fh.close()

#2.Write a program to prompt for a file name, and then
#read through the file and look for lines of the form:
def avrag_e():
    inp = input('Enter the name of the file: ')
    fh = open(inp)
    text = fh.read()
    lines = text.splitlines()
    i = 0
    total = 0
    count = 0
    while i<len(lines):
        if lines[i].startswith('X-DSPAM-Confidence'):
            num = float(lines[i].split(':')[1])
            total += num
            count += 1
        i += 1
    fh.close()
    av = total / count
    print(f' The avrage is : {av}')

#3.Sometimes when programmers get bored or want to have a bit of fun,
#they add a harmless Easter Egg to their program. Modify the program
#that prompts the user for the file name so that it prints a funny message
#when the user types in the exact file name "na na boo boo". The program
#shout behave normally for all other files Which exist and don't exist.
#Here is a sample execution of the program:
def haby():
    try:        
        inp = input('Enter th name of the dile: ')
        fh = open(inp)        
        text = fh.read()
        count = 0
        for line in text:
            count += 1

        print(f'Ther were {count} subject lines in {inp}.')
        fh.close
    except FileNotFoundError:
        print("NA NA BOO BOO TO YOU - You have been punk'd!")

   
def mane():
    #1.
##    py_shout()
    #2.
##    avrag_e()
    #3.
    haby()
    print(' AMIRABAS KHAJEH')


###Driver Code###
mane()

#AMIRABAS KHAJEH
   
