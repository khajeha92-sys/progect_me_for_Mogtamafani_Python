
import matplotlib.pyplot as plt
import numpy as np

class FancyBarChart:
    def __init__(self, data, labels, title):
        self.data = data
        self.labels = labels
        self.title = title

    def show_chart(self):
        plt.style.use('seaborn-v0_8-darkgrid')  
        fig, ax = plt.subplots(figsize=(9, 6))

        
        bars = ax.bar(
            self.labels,
            self.data,
            color=['#green' if v >= 0 else '#red' for v in self.data],
            width=0.6
        )

        
        for bar, value in zip(bars, self.data):
            
            x = bar.get_x() + bar.get_width() / 2
            y = value

           
            if value > 0:
                va = 'bottom'
                y_text = y - (0.02 * max(self.data))  
            
            else:
                va = 'top'
                y_text = y + (0.02 * abs(min(self.data)))

            
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

        
        ax.axhline(0, color='black', linewidth=1.3)

        
        max_val = max(self.data)
        min_val = min(self.data)
        padding = (max_val - min_val) * 0.15
        ax.set_ylim(min_val - padding, max_val + padding)

        
        ax.set_title(self.title, fontsize=16, fontweight='bold', pad=15)
        ax.set_xlabel("Categories", fontsize=13)
        ax.set_ylabel("Values", fontsize=13)

        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.tight_layout()
        plt.show()



values = [15.3, 18.7, 12.5, -4.2, 20.1, -9.8]
labels = ['A', 'B', 'C', 'D', 'E', 'F']

chart = FancyBarChart(values, labels, title='+and-')
chart.show_chart()


