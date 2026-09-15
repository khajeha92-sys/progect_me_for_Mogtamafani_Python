# IN THE NAME OF GOD

#IS PRIME
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
                   if n % i == 0:
                       return False
    return True


#Drive:
print(is_prime(2))
print(is_prime(15))
print(is_prime(17))

#PRINT TRIANGLULAR NUMBERS
print('*'*90)


def print_triangular_numbers(n):
    for i in range(1, n+1):
        triangular = i * (i + 1 )//2
        print(i, triangular)


#Driver

print_triangular_numbers(5)        
