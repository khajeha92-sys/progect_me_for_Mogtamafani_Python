#IN THE NAME OF GOD
#MADE IN AMIRABAS KHAJEH FOR MR HAJAVI
#CLASS 6

#1.Write a program that categorizes each mail message by
#which day of the week the commit was done. To do this
#look for lines that start with ''From'' ,then look for
#the third word and keep a running count of each of the
#days of the week. At the end of the program print out the
#contents of your dictionary (order does not matter).
def email_day(email):
    try:
        with open(file = email,mode='r') as fh:
            D = {}
            for line in fh:
               if line.startswith('From '):
                   words = line.split()
                   day = words[2]
                   D[day] = D.get(day, 0) + 1
                   return D
    except FileNotFoundError:
        return'File not found .'

#2. Write a program to read though a mail log, build a
#histogram using a dictionary to count how may message
#have come from each email address, and print the dictionary.
def coum(email):
    try:
        with open(email, 'r') as fh:
            D = {}
            for line in fh:
                D[line] = D.get(line, 0) + 1
                return D
    except FileNotFoundError:
        return 'File not found . '
    
#3. Add code to the above program to figure out who has
#sent the most messages in the file. After all the data
#has been read and the dictionary has been created, look
#through the dictionary using a maximum loop (see Chapter 5:
#Maximum and minimum loops) to find who has the most message
#and print how many message the person has.
def coum_coum(email):
    try:
        with open(email) as fh:
            D = {}
            for line in fh:
                if line.startswith('From '):
                    words = line.split()
                    sen = words[1]
                    D[sen] = D.get(sen, 0) + 1
            max_email = ''
            max_count = 0
            for key, value in D.items():
                if value > max_count:
                    max_count = value
                    max_email = key

            return max_email, max_count              
    except FileNotFoundError:
        return 'File not found . '

#4. This program records the domain name (instead of the address)
#where the message was send from instead of who the mail came from
#(i.e.,the whole email address).At the end of program, print out
#the contents of your dictinary.
def instead_of_the_address(email):
    try:
        with open(email) as fh:
            D = {}
            for line in fh:
                if line.startswith('From '):
                    words = line.split()
                    sen = words[1]
                    D[sen] = D.get(sen, 0) +1
                return D
    except FileNotFoundError:
        return 'File note found .'

#5. Rewrite the program that prompts the user for a list of numbers and
#prints out the maximum and minimum of the numbers at the end when the user
#enters "done". Write the program to store the numbers the user enfers in
#list and use the max() and min() functions to compute the maximum and
#minimum numbers after the loop completes.
def num_num():
    numbers = []
    while True:
        num = input('Enter the number: ')
        if num.lower() == 'done':
            break
            
        try:
            number = float(num)
            numbers.append(number)
        except ValueError:
            print('Error')
            continue
        
    if numbers:
        print(f'Maximum: {max(numbers)}')
        print(f'Maximum: {min(numbers)}')
    else: print('not number')

        
def main():
    file_name = 'mbox-short.txt'
##    1.
    print('1.')
    res_1 = email_day(file_name)
    print(res_1)
    print('*' * 60)

##    2.
    print('2.')
    res_2 = coum(file_name)
    print(res_2)
    print('*' * 60)
    
##    3.
    print('3.')
    res_3 = coum_coum(file_name)
    print(res_3)
    print('*' * 60)

##    4.
    print('4.')
    res_4 = instead_of_the_address(file_name)
    print(res_4)
    print('*' * 60)

##    5.
    print('5.')
    num_num()
    print('*' * 60)
    
    print('END \n AMIRABAS KHAJEH') 
###Driver Code###
main()

#AMIRABAS KHAJEH
