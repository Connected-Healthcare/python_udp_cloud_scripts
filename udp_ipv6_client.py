import socket
import time

#UDP_IP = "::1" # localhost
#UDP_IP = "fe80::44a9:f933:cfd6:826c"
#UDP_IP = "fe80:0:0:0:2093:611f:5c5c:3ebc"
#UDP_IP = "fe80::30cc:c6b5:eba5:ca62"
UDP_IP = b"::1"
UDP_PORT = 1234 
# MESSAGE = "Hello, World!"
MESSAGE = b"RLOC16:b400,0.00,0.00,0.00,0.00,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00"

print ("UDP target IP: {0}".format(UDP_IP))
print ("UDP target port: {0}".format(UDP_PORT))
print ("Sending the message: {0}".format(MESSAGE))

while True:
	sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
	sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
	time.sleep(5)
