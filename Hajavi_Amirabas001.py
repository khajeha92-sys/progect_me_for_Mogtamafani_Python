#IN THE NAME OF GOD
#Mean absolute deviation (MAD) is the averageof how much the individual
# scores of a data set differ from the mean of the set.
#  (The mean of the deviations from the mean.)

def s(days):
    print('Day     Temperature     Absolute Deviation')
    print('=' * 43)

    data = (tem for day, tem in days)  
    sum_data = sum(data)
    len_data = len(days)
    m = sum_data / len_data
    
    total = 0
    for day, tem in days:
        p = abs(tem - m)
        #total += p**2
        total += p
        
        print(f'{day}    {tem}             {round(tem)}-{round(m)}={round(p)}')
    
    #g = total / (len_data - 1)
    g = total / len_data
    
    print('_' * 43)
    print(f'Total:    {sum_data}      Total:      {round(total)}')
    print(f'Mean:     {round(m)}       MAD:        {round(g)}')
    print('-' * 43)
    
  
    
### Driver Code ###
#data = [35, 30, 32, 29, 27, 37, 41]
print('-' * 43)    
days = [('Monday   ', 35), ('Tuesday  ', 30), ('Wednesday', 32),
        ('Thursday ', 29), ('Friday   ', 27), ('Saturday ', 37),('Sunday   ', 41)]
s(days)


#Made in Amirabas_Khajeh form Hajavi
