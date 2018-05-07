from scipy.io import wavfile
import numpy as np
import sys
import socket
import time

seconds = 0.01
fs, data = wavfile.read('C:/Users/edson/Downloads/PISTA2.wav')

data = data + (65535 / 2)
data = data / 16
data2 = np.cast[np.uint16](data)

UDP_IP = "192.168.1.104"
UDP_PORT = 54322

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP

min = 0;
max = 31;
cont = 1;
while True:

    if max <= data2.size:
        sock.sendto(data2[min:max], (UDP_IP, UDP_PORT))
        print(cont,min,max)
        min=max+1;
        max=max+31;
        cont += 1

    else:
        sock.sendto(data2[min:data2.size], (UDP_IP, UDP_PORT))
        print(cont,min,data2.size )
        min = 0;
        max = 31;
        cont = 1;

    time.sleep(seconds)
