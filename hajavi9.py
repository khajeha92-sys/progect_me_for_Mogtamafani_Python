#king
def jos(n, k):
    people = list(range(1, n+1))
    index = 0

    while len(people) > 1:
        index = (index + k - 1) % len(people)
        people.pop(index)
    return people[0]


n = 41
k = 2
survivor = jos(n, k)
print(f' a man will not dei  {survivor}')
