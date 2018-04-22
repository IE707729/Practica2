from scipy.io import wavfile
# from numpy import *
# from sympy import *
# from types import *

import socket
fs, data = wavfile.read('/Users/edson/Downloads/audio.wav')
print(data)
print(type(data))
print(isinstance(data, tuple))
print(isinstance(data, list))

UDP_IP = "148.201.215.14"

UDP_PORT = 50005

MESSAGE = "Hello, World!"
while True:
    #print(1)


    sock = socket.socket(socket.AF_INET,  # Internet
    socket.SOCK_DGRAM)  # UDP
    sock.sendto(MESSAGE.encode('utf-8'), (UDP_IP, UDP_PORT))