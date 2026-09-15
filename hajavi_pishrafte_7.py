#IN THE NAME OF GOD
#MADE IN AMIRABAS KHAJEH FOR HAJAVI
#CLASS_7

import re

def email_correct(file):
    with open(file,'r') as fh:
        for line in fh:
            line = line.strip()
            reg = r'[a-zA-Z0-9]\S*@\S*[a-zA-Z]'   #\S+@\S+
            lst = re.findall(reg, line)
            if lst : print(lst)



###Driver Code###
res = 'mbox-short.txt'
email_correct(res)
print('THE END \n AMIRABAS KHAJEH')
#AMIRABAS KHAJEH
