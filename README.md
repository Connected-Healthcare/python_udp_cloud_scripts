# Python UDP and Cloud Connection script
Includes python script that runs on Rapsberry Pi 3B OpenThread Border Router. Its purpose is to:
- Opens UDP port in the Raspberry Pi 3B (OpenThread Border Router)
- Collect the sensor data from the OpenThread network
- Upload to the Firebase cloud instance
- CLI command usage: python3 udp_ipv6_server.py

# Note:
To randomly simulate sensor data (GPS, CO, HB, and ST B-L475E-IOT01A internal sensors) and send to Firebase cloud instance, run python3 udp_ipv6_server_random_data.py
