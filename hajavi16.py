#IN THE NAME OF GOD

#1. Write four names in a text file;?

loc = r"C:\Users\LENOVO\Desktop" # raw string
fname='names.txt'
fpath= loc + '\\' + fname

fh = open(fpath, mode='w')  #file handle

name = 'Amirabas , Hajavi, Baran, Parmis'

#print (name, file = fh)
fh.write(name)

fh.close()
