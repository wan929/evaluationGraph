import pandas as pd
from matplotlib import pyplot as plt
import matplotlib
import csv
import numpy as np
import argparse
import re

font = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 13,
        }

font1 = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 10,
        }

# 文件路径
file_path = "/home/wan/Desktop/High-Precision-Congestion-Control-master/simulation/small_30load_up_qlength.txt"

reordering_size_file = "/home/wan/Desktop/High-Precision-Congestion-Control-master/simulation/small_30load_reordering_buffer_size.txt"

# 读取文件数据
with open(file_path, 'r') as file:
    lines = file.readlines()

with open(reordering_size_file, 'r') as file1:
    lines1 = file1.readlines()

# 解析数据
time = []
queue_length = []
last_recorded_time = 2000002000.0
record_interval = 500.0 # 1微秒

time1 = []
reordering_size = []

for line in lines:
    match = re.match(r'\+(\d+\.\d+)ns', line)
    if match:
        timestamp = float(match.group(1))
        length = float(line.split()[-1])

        # 判断是否满足记录间隔条件
        if timestamp - last_recorded_time >= record_interval:
            time.append(timestamp)
            queue_length.append(length)
            last_recorded_time = timestamp

for line1 in lines1:
     match1 = re.match(r'\+(\d+\.\d+)ns', line1)
     if match1:
        timestamp1 = float(match1.group(1))
        length1 = float(line1.split()[-1])

        time1.append(timestamp1)
        reordering_size.append(length1)

print(len(time))
print(len(time1))


# 绘制图表
fig, ax = plt.subplots(figsize=(5,3))
plt.plot(time, queue_length, linewidth = 1, label = 'queue length of upstream switch')
plt.plot(time1, reordering_size, linewidth = 1, label = 'reordering buffer of downstream switch')
plt.axhline(y = 37, color = 'r', linestyle = '--', label = 'pause threshold')
plt.legend()
ax = plt.gca()
ax.legend(loc = 'best', prop = font1, frameon = False)
plt.tick_params(direction = 'in', top = False, bottom = True, left = True, right = False)
# plt.title("small_30%load", fontproperties = font)
plt.xlabel("Time (s)", fontproperties = font)
plt.ylabel("Queue Length (KB)", fontproperties = font)
plt.xlim(2000000000, 2200000000)
plt.xticks(np.arange(2000000000, 2200000000.1, 25000000),['2', '','2.05','','2.1','','2.15','','2.2'], fontproperties = font)
plt.ylim(0, 220)
plt.yticks(np.arange(0, 220.1, 40), fontproperties = font)

plt.savefig('/home/wan/Experimental_Graph/paper/6_LinkGuardian_buffer/queuelength_time.pdf', format = 'pdf' , dpi = 800 ,bbox_inches = 'tight')
plt.show()