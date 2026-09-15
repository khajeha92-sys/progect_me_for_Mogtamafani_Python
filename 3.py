number=int(input('Enter your number:.....'))

if number<2:
    print('ERROR')
else :
    is_prime = True

for i in range (2, int(number**0.5)+1):
    if (number%i)==0:
        is_prime = False
        pass
    
if is_prime:
    print(f'{number} عدد اول است')
else:
    print(f'{number}عدد اول نيست')
