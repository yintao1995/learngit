import time
import struct


header = 32768
samples = 520
lines = 696
bands = 128
datalength = lines*bands
t1 = time.time()
with open('C:/Users/YINTAO/Desktop/test.cube', 'rb') as file_obj:
    # file_obj.read(header)
    file_obj.seek(header)
    j = 0
    data_list = []
    while j < datalength:
        j += 1
        data_flow = file_obj.read(2*samples)
        temp = struct.unpack('<'+str(samples)+'H', data_flow)
        # for i in range(0, len(data_flow), 2):
        #     # print(data_flow[i:i+2])
        #     temp.append(int.from_bytes(data_flow[i:i+2], byteorder='little', signed=False))
        data_list.extend(temp)
print(len(data_list))
print(data_list[:10])
t2 = time.time()
print(t2-t1)
