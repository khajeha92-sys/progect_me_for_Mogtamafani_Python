#Bear

import matplotlib.pyplot as plt

meat=int(input('Enter number of meat:'))
size=float(meat)

total_meat = meat * size
day = 0

days=[]
meat_left = []

while size > 0:
    day += 1
    need = 1 if (day % 2 == 1 )else 0.5
    days.append(day)
    meat_left.append(total_meat)

    if size >= need:
        size -= need
        print(f'Day {day} : the bear are all the meat!')
        #total_meat=0

    else:
        size = 0
        meat += 0.5
        total_meat //=2
        print(f'Day {day} : the bear are half the meat. Meat left: {total_meat}')
        
print(f'/n Your bear will die after {day} days.')


#plot
plt.plot(days, meat_left, marker='o')
plt.title('Bear\'s meat consumption over days')
plt.xlabel('Day')
plt.ylabel('Meat left')
plt.grid(True)
plt.show()





print('*'*90)
#King
