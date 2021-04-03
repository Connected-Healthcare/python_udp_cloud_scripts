import socket
import string
import serial
import time
import random
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

    # Randomized SensorData for debugging
    rloc_id_str = str(random.choice(string.ascii_letters[0:6])) + str(random.choice(string.ascii_letters[0:6])) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    hts221_temperature_str = str(round(random.uniform(10, 100),2))
    hts221_humidity_str = str(round(random.uniform(10, 100),2))

    lps22hb_temperature_str = str(round(random.uniform(10, 100),2))
    lps22hb_pressure_str = str(round(random.uniform(10, 100),2))

    magnetometer_axes = []
    for c in range(0, 3):
        magnetometer_axes.append(random.randint(-1000, 1000))

    accelerometer_axes = []
    for c in range(0, 3):
        accelerometer_axes.append(random.randint(-1000, 1000))

    gyroscope_axes = []
    for c in range(0, 3):
        gyroscope_axes.append(random.randint(-1000, 1000))

    time_of_flight = random.randint(10, 1000)

    heartRate = random.randint(10, 120)
    oxygen = random.randint(10, 100)

    spec_co_rel_humidity = random.randint(10, 100)
    spec_co_gas_conc = random.randint(10, 1000)
    spec_co_temp = random.randint(10, 100)

    latitude_str = str(round(random.uniform(-90, 90),2))
    longitude_str = str(round(random.uniform(-180, 180),2))

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

    print ("EpochTime: {0}".format(str(epoch_time)))
    print ("Timestamp: {0}".format(str(timestamp)))
    print ("RLOC16: {0}\nHTS221: {1}\nLPS22HB: {2}\nMagnetometer: {3}\nAccelerometer: {4}\nGyroscope: {5}\nTime_Of_Flight: {6}\nHeartbeat: {7}\nSpec_CO: {8}\nGPS: {9}".format(rloc_data, hts221_data, lps22hb_data, magnetometer_data, accelerometer_data, gyroscope_data, tof_data, heartbeat_data, spec_data, gps_data))
    print ("\n---------------\n")

    # TODO:
    # RLOC5000 in the URL will be replaced by non-changing unique ID of small TI board. For e.g., MAC address.
    # Sleep for 5 seconds in the final script in order to avoid over-usage of the Firebase DB

    result = firebase.post('https://connected-healthcare.firebaseio.com/RLOC5000', {'Timestamp':str(timestamp),'EpochTime':str(epoch_time),'1_RLOC16':rloc_data,'HTS221':hts221_data,'LPS22HB':lps22hb_data,'Magnetometer':magnetometer_data,'Accelerometer':accelerometer_data,'Gyroscope':gyroscope_data,'Time_Of_Flight':tof_data,'Heartbeat':heartbeat_data,'Spec_CO':spec_data,'GPS':gps_data})

    time.sleep(1)
