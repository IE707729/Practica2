from scipy.io import wavfile
import numpy as np
import sys
import socket
import time

seconds = 0.001
fs, data = wavfile.read('C:/Users/edson/Downloads/Practica2-master/Practica2-master/sitar_mono_16bit_44100.wav')
# fs, data = wavfile.read('C:/Users/Cursos/Documents/acch/SEBMII/sitar_mono_16bit_44100.wav')
# fs, data = wavfile.read('C:/Users/Usuario/Downloads/sitar_mono_16bit_44100.wav')

print(data)
print(type(data))
# print(isinstance(data, tuple))
# print(isinstance(data, bytearray))
# print(isinstance(data, list))
# print(isinstance(data, int))
# print(isinstance(data, float))
# print(isinstance(data, enumerate))
print('%d sys.getsizeof(data)' % sys.getsizeof(data))
print(data.shape)  # Tuple of array dimensions
print('el arreglo data tiene: %d muestras' % data.shape[0])
print('the indices of the max values: %d ' % np.argmax(data))
print(data[np.argmax(data)])  # print(data[10645])
print('the indices of the min values: %d ' % np.argmin(data))
print(data[np.argmin(data)])
print(' %s Data-type of the array’s elements' % data.dtype)
print('     %d Number of array dimensions' % data.ndim)
print(' %d Number of elements in the array' % data.size)
print('%d Total bytes consumed by the elements of the array' % data.nbytes)
# print(data[0, 0])  # The element of data in the *first* row, *first* column
# print(data[0, 1])
# print(data[1, 1])
# print(data[1, 2]) # No existe columna 2. Va de 0 a 1

# for i in range(0, data.shape[0]-1):
#     print(data[i])

print('iiiiiiiiiiiiiiiiiiiiiiiiiiiiii cast iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')

data = data + (65535 / 2)
data = data / 16
data2 = np.cast[np.uint16](data)

# print(len(data2))
# print(data2[10000:10005])
print(' %s Data-type of the array’s elements' % data2.dtype)
# for i in range(0, data2.shape[0]-1):
#     print(data2[i])
for i in range(0, 10):
    print(data2[i])

UDP_IP = "192.168.1.104"
UDP_PORT = 54321
# MESSAGE = "Hello, World!"

# print(MESSAGE.encode('utf-8'))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP

min = 0;
max = 31;
cont = 1;
while True:
    # print(1)
    #print(MESSAGE.encode('utf-8'))

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



    # sock.sendto(MESSAGE.encode('utf-8'), (UDP_IP, UDP_PORT))
    time.sleep(seconds)

# while True:
#     print(MESSAGE.encode('utf-8'))
#     for i in range(len(data2)):
#         sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
#         sock.connect((UDP_IP, UDP_PORT))
#         sock.sendto(data[10000:10030], (UDP_IP, UDP_PORT))
#         #sock.sendto(MESSAGE.encode('utf-8'), (UDP_IP, UDP_PORT))
#         time.sleep(seconds)