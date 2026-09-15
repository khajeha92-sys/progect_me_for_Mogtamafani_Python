def kullatz(n):
    print('n\t\toutput printed so far')
    print(f'--\t\t{"-"*20}')
    acc = ''
    while n != 1:
        acc = acc + str(n) + ', '
        print(f'{n}\t\t{acc}')
        if n % 2 != 0:
            n = 3 * n + 1
        else:
            n = n // 2
    print(f'{n}\t\t{acc}1')
        
kullatz(n=3)


print('*'*90)

print('1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12','\n','-'*90)

def mupltipliers(i, ncols):
    for j in range(1, ncols+1, 1):
        print(i * j, end='\t')
        
def print_mult_table(nrows, ncols):
    for i in range(1, nrows+1, 1):
        mupltipliers(i=i, ncols=ncols)
        print(':',i) 
print_mult_table(12, 12)


print('*'*90)

def count_digits(n: int) -> int:
    s = str(n)
    return s.count('0') + s.count('5')

n = 1020305035
c = count_digits(n=n)
print(f'Total number of digits is {c} for {n}.')
