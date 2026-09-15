left=int(input('type the first number:'))
right=int(input('type the second number:'))

if right==0:
    print('ERROR')
else:
    negative_result =(left<0) != (right<0)
    
dividend=abs(left)
divisor=abs(right)
quotient=0


while dividend>=divisor:
    dividend=dividend-divisor
    quotient=quotient+1

if negative_result:
    quotient= -quotient
remainder=dividend if left>=0 else -dividend

print('anser is :', quotient)
print('remainder is :', remainder)
    
