
from scipy.io import wavfile
from numpy import *
import sys
import socket


fs, data = wavfile.read('C:/Users/Usuario/Documents/Audacity/Fanfare.wav')
# fs, data = wavfile.read('C:/Users/Usuario/Downloads/Fanfare_32bits.wav')
print(data)
print(type(data))
# print(isinstance(data, tuple))
# print(isinstance(data, bytearray))
# print(isinstance(data, list))
# print(isinstance(data, int))
# print(isinstance(data, float))
# print(isinstance(data, enumerate))
print('%d sys.getsizeof(data)' %sys.getsizeof(data))
print(data.shape)  # Tuple of array dimensions
print('%s Data-type of the array’s elements' %data.dtype)
print('%d Number of array dimensions' %data.ndim)  #
print('%d Number of elements in the array' %data.size)
print('%d Total bytes consumed by the elements of the array' %data.nbytes)
# print(data[0, 0])  # The element of data in the *first* row, *first* column
# print(data[0, 1])
# print(data[1, 1])
# print(data[1, 2]) # No existe columna 2. Va de 0 a 1

# for i in range(0, 441000-1):
#     for j in range(0, 2):
#         print(data[i, j])
        # print '%d * %d = %d' % (x, y, x*y)

var1 = str(data[285120-1, 1])
print(var1.encode('utf-8'))

var = str(data[285120-2, 1])
print(var.encode('utf-8'))

var2 = str(data)
print(var2.encode('utf-8'))

# var2 = tostring(data)
# print(var2.encode('utf-8'))

UDP_IP = "148.201.215.14"

UDP_PORT = 50005

MESSAGE = "Hello, World!"
print(MESSAGE.encode('utf-8'))
while True:
    # print(1)

    for i in range(0, 285120-1):
        for j in range(0, 2):
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
            sock.sendto(data[i, j].encode('utf-8'), (UDP_IP, UDP_PORT))
    # sock.sendto(MESSAGE.encode('utf-8'), (UDP_IP, UDP_PORT))
    # sock.sendto(var2.encode('utf-8'), (UDP_IP, UDP_PORT))
