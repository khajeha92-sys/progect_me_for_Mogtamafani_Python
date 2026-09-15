#IN THE NAME OF GOD
#MADE IN AMIRABAS KHAJEH FOR MR HAJAVI
#CLASS_9

##import subprocess
##import sys
import csv
import pandas as pd


def file_name(file):
    with open(file, encoding = 'utf-8') as fh:
        reader = csv.DictReader(fh)
        products = list(reader)
        return products

#Most reviewed
def most_reviewed(products):
    highest_rated = max(products, key=lambda x: float(x['Rating']))
##    print(f"\nHighest Rated: {highest_rated['Product_Name']} ({highest_rated['Rating']})")
    return highest_rated

#Best value(Rating per Million Tomans)
#Scaling factor to convert price-pre-toman to
#price-per-million-tomans for betterreadability
def bestvalue(products):
    best_value = max(products, key=lambda x:float(x['Rating'])/int(x['Price_Tomans'])*1000000)
##    print(f"\nBest Value: {best_value['Product_Name']} - {int(best_value['Price_Tomans']):,} Tomans")
    return best_value

#1.Create iranian_cosmetics.csv with 4 Iranian cosmetic brands.
def four_iranian_cosmetic(file_1):
    with open(file_1, encoding = 'utf-8') as fh:
        render = csv.DictReader(fh)
        products = list(render)
        return products
    
#2. Read iranian_brands.csv with 'next()'
def read_iran_with_next(file_1):
    fh = open(file_1, encoding = 'utf-8')

    header = next(fh)
    print(f'Header: {header.strip()}')

    print('\n=== Brands ===')
    for line in fh:
        print(line.strip())

    fh.close()

##3.Find highest-rated brand in iranian_cosmetics.csv
def highest_ratedd(file):
    with open(file, encoding='utf-8') as fh:
        reader = csv.reader(fh)
        header = next(reader)
        best_value = 0
        best_product = ''

        print('=== iranan Brands Under 10M ===')
        for row in reader:
            name = row[0]
            price = int(row[2])
            brand = row[1]
            rating = float(row[3])
            value_score = (rating / price) * 1_000_000


            if price < 10_000_000:
                print(f'{name:<25} ->\t{price:,} Tomans')

            if value_score > best_value:
                best_value = value_score
                best_product = name
        print('=== Best Value ===')
        print(f'Best Value: {best_value}({best_product})')

#4. Read 'iranian_cosmetics.csv' and find average price by brand.
def find_average_price_brand(file):
    with open(file, encoding='utf-8') as fh:
        reader = csv.DictReader(fh)
        brand_price = {}

        for row in reader:
            brand = row['Brand']
            price = int(row['Price_Tomans'])

            if brand not in brand_price:
                brand_price[brand] = []

            brand_price[brand].append(price)
##            print(brand_price)
            for brand in brand_price:
                avg = sum(brand_price[brand]) / len(brand_price[brand])
            print(f'{brand} -> Avg: {avg:,.0f} Tomans')
        


#5. Use Pandas to find the cheapst Iranian product.
def pandas_to_find_cheapstiranian_product(file):
    df = pd.read_csv(file, encoding='utf-8')
##    print(df)
    cheapst = df.nsmallest(1, 'Price_Tomans')
##    print(cheapst)
    print('=== Cheapst Product ===')
    print(cheapst[['Product_Name', 'Brand', 'Price_Tomans']])
    


    
def main():
    file = r'C:\Users\LENOVO\Desktop\pyhton\iranian_brands.csv'
    file_1 = r"C:\Users\LENOVO\Desktop\pyhton\iranian_cosmetics.csv"
##    four_iranian_cosmetic(file)
    res = file_name(file)
    highest_rated = most_reviewed(res)
    print(f"\nHighest Rated: {highest_rated['Product_Name']} ({highest_rated['Rating']})")
    best_value = bestvalue(res)
    print(f"\nBest Value: {best_value['Product_Name']} - {int(best_value['Price_Tomans']):,} Tomans")
    print('-'*60)
##1.
    print('1.')
    four = four_iranian_cosmetic(file_1)
    print(four)
    print('-'*60)
##2.
    print('2.')
    read_iran_with_next(file_1)
    print('-'*60)
##3.
    print('3.')
    highest_ratedd(file)
    print('-'*60)
##4.
    print('4.Read \'iranian_cosmetics.csv\' and find average price by brand.')
    find_average_price_brand(file)
    print('-'*60)
##5.
    print('5.')
    pandas_to_find_cheapstiranian_product(file)
    print('THE END')
###Driver Code###
main()
    
print('\n MADE IN AMIRANAS KHAJEH')
