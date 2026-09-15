#IN THE NAME OF GOD

#8.write function that mirrors its argument?

def mirrors(self):
    mirr = self + self[::-1]
    print(mirr)
    pass


### Drive Code ###

mirrors(input('Enter your mirror:'))

print('*'*90)

#9.write functin that removes all occurrences of a given letter from a string?

def remove_letter(text):
    rem = input('Enter text of remove:')
    text = text.replace(rem,'')
    print(text)
    pass

### Drive Code ###

remove_letter(input('Enter text:'))

print('*'*90)

#10. write a function that recognizes palindromes .(hint :use your reverse function to make thiseasy!)?

def is_palindrome(rev):
    if rev == rev[::-1]:
        print('it\'s palindrome')
    else:
        print('it is not palindrome')
    pass

### Drive Code ###

is_palindrome(input('Enter your revers:'))

print('*'*90)

#11.write a function that counts how many times a substring occurs in a string?

def count(matn):
    sub = input('Enter your substring:')
    coun = matn.count(sub)
    print(coun)
    pass

### Drive Code ###

count(input('Enter your matn:'))

print('*'*90)

#12.write a function that removes the first occurrence of a string from another string?

def remove(man):
    thr = input('Enter your text for first dilit:')
    that = man.replace(thr,'',1)
    print(that)
    pass

### Driver Code ###

remove(input('Enter your man for dlit:'))

print('*'*90)

#13. write a function that removes all occurrences of a string from another string?

def remove_all(there):
    dilit = input('Enter your thext from dilited:')
    dily = there.replace(dilit,'')
    print(dily)
    pass

### Driver Code ###

remove_all(input('Enter your there:'))


print('*'*90)

#10.2 : write a function replace (s, old, new ) that replaces all occurrences of old with new in a strings?

def replace(amirabas):
    kam = input('Enter your kam harf:')
    add = input('Enter your add harf:')
    ram = amirabas.replace(kam,add)
    print(ram)
    pass

### Driver Code ###

replace(input('Enter your harf:'))


print('/'*90)

print('Have good day❤')
