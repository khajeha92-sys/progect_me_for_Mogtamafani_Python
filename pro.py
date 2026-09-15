# IN THE NAME OF GAD
#1.
def calculate_average(numbers):
    total = sum (numbers)
    length = len (numbers)
    average = total / length
    return average

#2.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

#3.
def even_odd(numbers):
    even = []
    odd = []
    for num in numbers :
        if num % 2 == 0 :
            even.append(num)
        else :
            odd.append(num)
    return even, odd       



###Code Driver###1.
list_of_numbers = [3, 5, 7, 9, 12]
result = calculate_average(list_of_numbers)
print(f'avrage of num: {result}')

print('*'* 30)


###Code Driver###2.
m = int(input("Enter your number:"))
h = factorial(m)
print(f'factorial of number {m} is {h}')

print('*' *30)


###Code Driver###3.
numbers = input("Enter your numbers with kama:").split(",")
numbers = [int(num) for num in numbers]
even, odd = even_odd(numbers)
print(f'even numbers : {even}')
print(f'odd numbers : {odd}')
