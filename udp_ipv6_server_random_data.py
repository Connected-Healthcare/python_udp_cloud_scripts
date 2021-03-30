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
    rloc_id_str = "RLOC16:" + str(random.choice(string.ascii_letters[0:6])) + str(random.choice(string.ascii_letters[0:6])) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    hts221_temperature_str = str(round(random.uniform(10, 100),2))
    hts221_humidity_str = str(round(random.uniform(10, 100),2))

    lps22hb_temperature_str = str(round(random.uniform(10, 100),2))
    lps22hb_humidity_str = str(round(random.uniform(10, 100),2))

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

    data_formatted = rloc_id_str + "," + hts221_temperature_str + "," + hts221_humidity_str + "," + lps22hb_temperature_str + "," + lps22hb_humidity_str + "," + str(magnetometer_axes[0]) + "," + str(magnetometer_axes[1]) + "," + str(magnetometer_axes[2]) + "," + str(accelerometer_axes[0]) + "," + str(accelerometer_axes[1]) + "," + str(accelerometer_axes[2]) + "," + str(gyroscope_axes[0]) + "," + str(gyroscope_axes[1]) + "," + str(gyroscope_axes[2]) + "," + str(time_of_flight) + "," + str(heartRate) + "," + str(oxygen) + "," + str(spec_co_rel_humidity) + "," + str(spec_co_gas_conc) + "," + str(spec_co_temp) + "," + latitude_str + "," + longitude_str
    
    print ("{0}".format(data_formatted))

    final_data = "EpochTime:" + str(epoch_time) + ",Timestamp:" + str(timestamp) + ",SensorData:" + str(data_formatted)

    result = firebase.post('https://connected-healthcare.firebaseio.com/', {'EpochTime':str(epoch_time),'Timestamp':str(timestamp),'SensorData':str(data_formatted)})
    result = firebase.post('https://connected-healthcare.firebaseio.com/', {'data':str(final_data)})
    time.sleep(1)

