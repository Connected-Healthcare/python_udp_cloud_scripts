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

sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
firebase= firebase.FirebaseApplication('https://connected-healthcare.firebaseio.com/', None)

while True:
    timestamp = datetime.datetime.now()
    epoch_time = time.time()
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    data_formatted = data.decode(encoding="utf-8")

    # Uncomment for testing only
    # data_formatted = "RLOC16:b000,30.29,47.79,30.50,1013.96,285,-234,-397,-4,-31,1027,1540,-2590,350,1482,0,0,1476,60,3719.95,12154.77"

    data_formatted_list = data_formatted.split(',')
    rloc_id_temp = data_formatted_list[0].split(':') # Splitting of "RLOC16:B600"
    rloc_id_str = rloc_id_temp[1] # Considering only the actual value of B600
    hts221_temperature_str = data_formatted_list[1]
    hts221_humidity_str = data_formatted_list[2]
    lps22hb_temperature_str = data_formatted_list[3]
    lps22hb_pressure_str = data_formatted_list[4]
    magnetometer_axes = list()
    magnetometer_axes.append(data_formatted_list[5])
    magnetometer_axes.append(data_formatted_list[6])
    magnetometer_axes.append(data_formatted_list[7])
    accelerometer_axes = list()
    accelerometer_axes.append(data_formatted_list[8])
    accelerometer_axes.append(data_formatted_list[9])
    accelerometer_axes.append(data_formatted_list[10])
    gyroscope_axes = list()
    gyroscope_axes.append(data_formatted_list[11])
    gyroscope_axes.append(data_formatted_list[12])
    gyroscope_axes.append(data_formatted_list[13])
    time_of_flight = data_formatted_list[14]
    heartRate = data_formatted_list[15]
    oxygen = data_formatted_list[16]
    spec_co_gas_conc = data_formatted_list[17]
    spec_co_temp = data_formatted_list[18]
    latitude_str = data_formatted_list[19]
    longitude_str = data_formatted_list[20]

    rloc_data = rloc_id_str
    hts221_data = hts221_temperature_str + "," + hts221_humidity_str
    lps22hb_data = lps22hb_temperature_str + "," + lps22hb_pressure_str
    magnetometer_data = str(magnetometer_axes[0]) + "," + str(magnetometer_axes[1]) + "," + str(magnetometer_axes[2])
    accelerometer_data = str(accelerometer_axes[0]) + "," + str(accelerometer_axes[1]) + "," + str(accelerometer_axes[2])
    gyroscope_data = str(gyroscope_axes[0]) + "," + str(gyroscope_axes[1]) + "," + str(gyroscope_axes[2])
    tof_data = str(time_of_flight)
    heartbeat_data = str(heartRate) + "," + str(oxygen)
    spec_data = str(spec_co_gas_conc) + "," + str(spec_co_temp)
    gps_data = latitude_str + "," + longitude_str

    firebase_url = "https://connected-healthcare.firebaseio.com/" + "RLOC" + rloc_data.upper()

    print ("EpochTime: {0}".format(str(epoch_time)))
    print ("Timestamp: {0}".format(str(timestamp)))
    print ("RLOC16: {0}\nHTS221: {1}\nLPS22HB: {2}\nMagnetometer: {3}\nAccelerometer: {4}\nGyroscope: {5}\nTime_Of_Flight: {6}\nHeartbeat: {7}\nSpec_CO: {8}\nGPS: {9}".format(rloc_data, hts221_data, lps22hb_data, magnetometer_data, accelerometer_data, gyroscope_data, tof_data, heartbeat_data, spec_data, gps_data))

    print ("\n---------------\n")

    result = firebase.post(firebase_url, {'Timestamp':str(timestamp),'EpochTime':str(epoch_time),'1_RLOC16':rloc_data,'HTS221':hts221_data,'LPS22HB':lps22hb_data,'Magnetometer':magnetometer_data,'Accelerometer':accelerometer_data,'Gyroscope':gyroscope_data,'Time_Of_Flight':tof_data,'Heartbeat':heartbeat_data,'Spec_CO':spec_data,'GPS':gps_data})

    time.sleep (2)

"""
NOTE:
Sample Data Entry in the Firebase Cloud:
1_RLOC16:
"['RLOC16', 'b000']"
Accelerometer:
"-4,-31,1027"
EpochTime:
"1617430182.9081423"
GPS:
"3719.95,12154.77"
Gyroscope:
"1540,-2590,350"
HTS221:
"30.29,47.79"
Heartbeat:
"0,0"
LPS22HB:
"30.50,1013.96"
Magnetometer:
"285,-234,-397"
Spec_CO:
"1476,60"
Time_Of_Flight:
"1482"
Timestamp:
"2021-04-03 07:09:42.908103"
"""