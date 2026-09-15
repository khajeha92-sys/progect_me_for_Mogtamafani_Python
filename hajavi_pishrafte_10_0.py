# IN THE NAME OF GOD
# MADE IN AMIRABAS FOR MR HAJAVI
# CLASS 10

import xml.etree.ElementTree as ET
import pandas as pd

## 1. "Parse XML from String"
## Create an XML string for a book (title, author, year, price)
## and parse it.
class BookXMLParser:
    def __init__(self, xml_string):
        self.xml_string = xml_string
        self.root = None

    def parse(self):
        self.root = ET.fromstring(self.xml_string)

    def show_book(self):
        print(f"Title: {self.root.find('title').text}")
        print(f"Author: {self.root.find('author').text}")
        print(f"Year: {self.root.find('year').text}")
        print(f"Price: {self.root.find('price').text}")

## 2. "Create XML Dynamically"
## Create an XML file for a library with 5 books
## using a loop.
class LibraryXMLCreate:
    def __init__(self):
        self.root = ET.Element("library")

    def add_book(self, title, author, year, price):
        book = ET.SubElement(self.root, 'book')
        ET.SubElement(book, 'title').text = title
        ET.SubElement(book, 'author').text = author
        ET.SubElement(book, 'year').text = str(year)
        ET.SubElement(book, 'price').text = str(price)

    def save(self, filename):
        tree = ET.ElementTree(self.root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
        print(f"'{filename}' created successfully!")

## 3. "Data Analysis"
## Convert XML to DataFrame and find the average price.
class XMLDataAnalyze:
    def __init__(self, xml_data):
        self.xml_data = xml_data
        self.root = None
        self.df = None

    def parse_xml(self):
        self.root = ET.fromstring(self.xml_data)

    def convert_to_dataframe(self):
        data = {'title' : [],
                'author': [],
                'year'  : [],
                'price' : []}
        
        for book in self.root.findall('book'):
            data['title'].append(book.findtext('title'))
            data['author'].append(book.findtext('author'))
            data['year'].append(int(book.findtext('year')))
            data['price'].append(float(book.findtext('price')))
        self.df = pd.DataFrame(data)

    def show_avrage_price(self):
        average = self.df['price'].mean()
        print(f"Average price: ${average:.2f}")

    def show_most_expensive(self):
        index = self.df['price'].idxmax()
        title = self.df.loc[index,'title']
        price = self.df['price'].max()

        print(f"Most expensive: {title} - ${price:.2f}")


def main():
    print('1. "Parse XML from String"')
    xml_string = """
    <book>
        <title> Python for Every body </title>
        <author> DR.hajavi </author>
        <year> 2016 </year>
        <price> 33.3 </price>
    </book>
    """

    book = BookXMLParser(xml_string)

    book.parse()
    book.show_book()

    print('=' * 63)
    print('2. "Create XML Dynamically"')
    library = LibraryXMLCreate()

    books = [("Python for Every body", "DR.hajavi", 2016, 33.3),
             ("C#", "Vali", 2020, 43),
             ("C++", "Hajavi", 2021, 55),
             ("javas Cript", "Amirabas", 2026, 40),
             ("Json", "Sara", 2004, 33)]

    for title, author, year, price in books:
        library.add_book(title, author, year, price)
    
    library.save('library_crreated.xml')

    print('=' * 63)
    print('3. "Data Analysis"')
    xml_data = """
    <library>
        <book>
            <title>Python for Every body</title>
            <author>DR.hajavi</author>
            <year>2016</year>
            <price>33.3</price>
        </book>

        <book>
            <title>C#</title>
            <author>Vali</author>
            <year>2020</year>
            <price>43</price>
        </book>

        <book>
            <title>C++</title>
            <author>Hajavi</author>
            <year>2021</year>
            <price>55</price>
        </book>
    </library>
    """
    analiz = XMLDataAnalyze(xml_data)

    analiz.parse_xml()
    analiz.convert_to_dataframe()
    analiz.show_avrage_price()
    analiz.show_most_expensive()


### Driver Code ###
main()

print('THE END')
print('\n MADE IN AMIRABAS KHAJEH')
