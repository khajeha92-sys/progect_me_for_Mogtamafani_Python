#In the name of GOD

#hour

x = int(input('Enter your number(seconds):'))

if x<0 :
    print('Error')

else:    
    def change(num, n, b):
        hours = num // n
        num = num % n
        minutes = num // b
        second = num % b
        print(f"h:{hours}, m:{minutes}, s:{second}")

        
    change(x,n=3600, b=60)


print('*'*90)

#bank

def bank(p, r, n, t):
    """
    p = principal amount (intial investment)

    r = annual nominal interest rate (as a decimal)

    n = number of times the interest is compounded per year

    t = number of year
    
    """

    a = p * (1 + r/n) ** n*t
    return a

b = bank(p = 2000000, r = 4.5, n = 12, t = 5)
print("The payment for your loan has {} been made".format(b))


print('*'*90)

# chart

import matplotlib.pyplot as plt
import numpy as np

class FancyBarChart:
    def __init__(self, data, labels, title):
        self.data = data
        self.labels = labels
        self.title = title

    def show_chart(self):
        plt.style.use('seaborn-v0_8-darkgrid')#style
        fig, ax = plt.subplots(figsize=(9, 6))

        bars = ax.bar(
            self.labels,
            self.data,
            color = ['green' if v>= 0 else 'red' for v in self.data],
            width = 0.6)
        
        max_val = np.max(np.abs(self.data))
        y_offset = max_val * 0.04


        for bar , value in zip(bars, self.data):

            x = bar.get_x() + bar.get_width() / 2
            y = value

            
            if value >= 0:
                va = 'bottom'
                y_text = y - (0.02*max(self.data))
                
            else:
                va = 'top'
                y_text = y + (0.02* abs(max(self.data)))
                
                

            ax.text(
                x,
                y,
                f'{value:.2f}',  
                ha='center',
                va='bottom' if value >= 0 else 'top',
                fontsize=11,
                fontweight='bold',
                color='black',
                bbox=dict(
                    facecolor='white',
                    alpha=0.8,
                    edgecolor='none',
                    boxstyle='round,pad=0.2'
                )
            )

            #0

        ax.axhline(0, color='black', linewidth=1.3)

        
        max_val = max(self.data)
        min_val = min(self.data)
        padding = (max_val - min_val) * 0.15
        ax.set_ylim(min_val - padding, max_val + padding)

            #style

        ax.set_title(self.title,
                         fontsize = 16,
                         fontweight = 'bold',
                         pad = 15)
        ax.set_xlabel("Categories",fontsize = 13)
        ax.set_ylabel("Values", fontsize = 13)
            
        plt.xticks(fontsize = 12)
        plt.yticks(fontsize = 12)
        plt.tight_layout()
        plt.show()

#data

valus = [15.3, 18.7, 12.5, -4.2, 20.1, -9.8]
labels = ['A', 'B', 'C', 'D', 'E', 'F']

#chart

chart = FancyBarChart(valus, labels, title='+ and -')
chart.show_chart()
    
