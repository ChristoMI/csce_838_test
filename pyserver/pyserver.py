'''
Created on Nov 27, 2021

@author: tran
'''

import bluetooth

server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

port = 1
server_sock.bind(("",port))
server_sock.listen(1)

print("Waiting for connection...")
client_sock,address = server_sock.accept()
print ("Accepted connection from " + str(address))

data = client_sock.recv(1024)
print ("received " + str(data))

client_sock.close()
server_sock.close()