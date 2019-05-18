import time
import struct
import sys
import numpy as np

header = int(32768/2)
samples = 520
lines = 696
bands = 128
datalength = lines*bands*samples
t1 = time.time()

filename = 'C:/Users/YINTAO/Desktop/test.cube'
# data_list = np. fromfile(filename, 'uint16')[header: header+datalength]
data_list = np. fromfile(filename, dtype='<u2', )[header: header+datalength]
print(len(data_list))
print(data_list[:10])
print(sys.getsizeof(data_list[0]))
print(sys.getsizeof(data_list[9]))
t2 = time.time()
print(t2-t1)
a = input('quit?')
print(a)
