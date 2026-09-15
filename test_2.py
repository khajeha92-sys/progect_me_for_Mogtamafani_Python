##pip install jupyter

import urllib.request
import collections #2
import re #3
def m_1():
    #1. URL Discovery: Identify the targeted URLs of the pages you want to extract data from.
    URL="https://data.pr4e.org/romeo.txt"
    ## Downloading: Make HTTP requests to the target URLs to download the HTML/text content from the page.
    ##response=urllib.request.urlopen(URL)
    try:
        with urllib.request.urlopen(URL) as response:
            ##13# Chech status code
            ##response = urllib.resquest.urlopen(URL)
            if response.status == 200:
                print('status code is: ok')
                print("="*50)
            else:
                print("Status Code is not succes")
                exit()
            
            # 3. Extraction: Use parsers to extract pieces of information from the pages that are meaningful to you.

            ##21 22 # It could be text fields, numbers, tables, Links, images etc.
            D={}
            for line in response:
            ##4. Transformation: Clean, sanitize and transfore the extracted data into the desired format,
                line = line.decode()
    ##            line = line.strip() # vagtey split mishe strip lazem ny
    ##            print(line)
                line = line.split()
                for li in line:
                    D[li] = D.get(li, 0) + 1
            print(D)
    except Exception as e:
        print(f"")

def m_2():
    URL="https://data.pr4e.org/romeo.txt"
    try:
        with urllib.request.urlopen(URL) as response:
            word_conter = counter()
            if response.status == 200:
                print('status code is: ok')
                print("="*50)
            else:
                print("Status Code is not succes")
                exit()
            for line in response:
                line = line.decode()
                line = line.lower()
                line = re.sub(r'[a-zA-Z0-9]\S*@\S*[a-zA-Z]','' , line)
                line = line.split()
                word_conter.update(line)
            print(word_conter)
    except Exception as e:
        print(f"")

    
m_1()
m_2()











