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
    timestamp = datetime.datetime.now()
    epoch_time = time.time()
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    data_formatted = data.decode(encoding="utf-8")
    final_data = "EpochTime:" + str(epoch_time) + ",Timestamp:" + str(timestamp) + ",SensorData:" + str(data_formatted)
    """
    Sample data constructed:
    "EpochTime:1617085464.6055038,Timestamp:2021-03-30 07:24:24.605465,SensorData:RLOC16:b000,30.29,47.79,30.50,1013.96,285,-234,-397,-4,-31,1027,1540,-2590,350,1482,0,0,1476,24,60,3719.95,12154.77"
    """
    result = firebase.post('https://connected-healthcare.firebaseio.com/', {'data':str(final_data)})
    print ("{0}".format(data_formatted))
