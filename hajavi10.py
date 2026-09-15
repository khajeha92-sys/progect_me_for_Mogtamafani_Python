class Mean_mad_calculator:
    def __init__(self, data):
        self.data = data
        self.mean = None
        self.mad = None

    def calculate_mean(self):
        self.mean = sum(self.data) / len(self.data)
        return self.mean

    def calculate_mad(self):
        if self.mean is None:
            self.calculate_mean()

        self.mad = sum(abs(x- self.mean) for x in self.data)/len(self.data)
        return self.mad

    def show_results(self):
        print('Mean:',self.mean)
        print('MAD:',self.mad)


#start
temperatures = [35, 30, 32, 29, 27, 37, 41]

calc = Mean_mad_calculator(temperatures)
calc.calculate_mean()
calc.calculate_mad()
calc.show_results()


print('*'*90)
#gges
ages = [1, 4, 7, 7, 8, 19, 38, 40, 60, 66]
mean_age = sum(ages) / len(ages)
deviations = [abs(x  - mean_age) for x in ages]
mad = sum(deviations)/len(deviations)
print('mean:',mean_age)
print('MAD:',mad)
        
