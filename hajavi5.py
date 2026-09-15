#10. 11. 12.


def find_hypot(a, b):
    """
    Calculate the length of the hypotenuse of a right-angled triangle
    given the lengths of the other two sides.
    """
    return (a**2 + b**2) ** 0.5


def is_rightangled(a, b, c):
    """
    Check if a triangle with sides a, b, and c is right-angled.
    (The order of the sides does not matter.)
    """
    sides = sorted([a, b, c])
    x, y, z = sides
    return abs((x**2 + y**2) - (z**2)) < 0.000001


#start

print('Right-Angled Triangle Checker')

# Get sides from user
a = float(input('Enter the first side: '))
b = float(input('Enter the second side: '))
c = float(input('Enter the third side: '))

# Check if the triangle is right-angled
if is_rightangled(a, b, c):
    print('True')
else:
    print('False')

# Also calculate the hypotenuse (from the two smallest sides)
sides = sorted([a, b, c])
x, y, z = sides
hyp = find_hypot(x, y)
print(f"The hypotenuse from sides {x} and {y} is: {hyp:.4f}")
