
import socket
my_socket = socket.socket()
HOST = 'data.pr4e.org'
PORT = 80
server = (HOST, PORT)
fpath = '/cover.jpg'
my_socket.connect(server)
##print('ok')

##rec

##cmd = f'GET http://{host}/mbox-short.txt HTTP/1.0\r\n\r\n'
cmd = f'GET {fpath} HTTP/1.1\r\nHost: {HOST}\r\n\r\n'
cmd = cmd.encode() #byt
my_socket.send(cmd) #dastor send
##print('sent')


with my_socket:
    while True:
        data = my_socket.recv(512)
        if len(data)<1: break
        data = data.decode()
##        print(data)

with my_socket:
    image = ''
    while True:
        data = my_socket.recv(2**10)
        if len(data)<1: break
        image += data
CR = image.find('\r\n\r\n')
header = image[:CR]
picture = image[CR+4:]


