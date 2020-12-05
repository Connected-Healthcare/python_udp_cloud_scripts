import socket
import serial
import time

import datetime
import re
import sys
import os
import subprocess

from firebase import firebase
 
UDP_IP = "::" # = 0.0.0.0 u IPv4
UDP_PORT = 1234 

sock = socket.socket(socket.AF_INET6, # Internet
						socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
firebase= firebase.FirebaseApplication('https://connected-healthcare.firebaseio.com/', None)

while True:
    timestamp= datetime.datetime.now()
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    data_formatted = data.decode(encoding="utf-8")
    result = firebase.post('https://connected-healthcare.firebaseio.com/', {'datetime':str(timestamp),'BPM':str(data_formatted)})
    print ("received message: {0}".format(data_formatted))
