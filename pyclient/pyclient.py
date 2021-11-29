'''
Created on Nov 27, 2021

@author: tran
'''
import sys

import bluetooth

addr = "98:8D:46:C4:8D:D4"

port = 1
sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

sock.connect((addr, port))

sock.send("hello!!")

sock.close()
