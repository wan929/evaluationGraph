#from turtle import color
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib
import csv
import numpy as np
import argparse

font = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 10.5,
        }

font1 = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 10.5,
        }

font2 = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 11.5,
        }

font3 = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 11.5,
        }
# -------------------------------
parser = argparse.ArgumentParser(description = '')
parser.add_argument("-p", type = int , default = 6) #all, avg, 50, 95, 99, 999, max
parser.add_argument("-l", type = int , default = 6) #
parser.add_argument("-w", type = str , default = 'Facebook') #WebSearch, Facebook, Google
parser.add_argument("-cc", type = str , default = 'dcqcn' ) #dcqcn, hpcc, dctcp, timely
parser.add_argument("-lossrate", type = int , default = 1000) #dcqcn, hpcc, dctcp, timely
parser.add_argument("-rto", type = int , default = 1) #dcqcn, hpcc, dctcp, timely
args = parser.parse_args()

linewide = 1.5
methods = ['SkyNet_SLR', 'SkyNet_CV']
# -------------------------------
# SADR_CV SADR_SLR
file = "/home/wan/Experimental_Graph/paper/3_Facebook/fh_20ms_1000_dcqcn_SLR_NACK.csv"
with open(file, 'r') as f:       
        reader = csv.reader(f)
        result = list(reader)

        SADR_CV_avg = result[0]
        SADR_CV_50 = result[1]
        SADR_CV_95 = result[2]
        SADR_CV_99 = result[3]
        SADR_CV_999= result[4]
        SADR_CV_max = result[5]

        SADR_SLR_avg = result[6]
        SADR_SLR_50 = result[7]
        SADR_SLR_95 = result[8]
        SADR_SLR_99 = result[9]
        SADR_SLR_999 = result[10]
        SADR_SLR_max = result[11]

# -------------------------------
CV_avg = [float(x) for x in SADR_CV_avg]
CV_50 = [float(x) for x in SADR_CV_50]
CV_95 = [float(x) for x in SADR_CV_95]
CV_99 = [float(x) for x in SADR_CV_99]
CV_999 = [float(x) for x in SADR_CV_999]
CV_max = [float(x) for x in SADR_CV_max]

SLR_avg = [float(x) for x in SADR_SLR_avg]
SLR_50 = [float(x) for x in SADR_SLR_50]
SLR_95 = [float(x) for x in SADR_SLR_95]
SLR_99 = [float(x) for x in SADR_SLR_99]
SLR_999 = [float(x) for x in SADR_SLR_999]
SLR_max = [float(x) for x in SADR_SLR_max]

# -------------------------------
# log(2)处理
CV_avg = np.log(CV_avg)/np.log(2)
CV_50 = np.log(CV_50)/np.log(2)
CV_95 = np.log(CV_95)/np.log(2)
CV_99 = np.log(CV_99)/np.log(2)
CV_999 = np.log(CV_999)/np.log(2)
CV_max = np.log(CV_max)/np.log(2)

SLR_avg = np.log(SLR_avg)/np.log(2)
SLR_50 = np.log(SLR_50)/np.log(2)
SLR_95 = np.log(SLR_95)/np.log(2)
SLR_99 = np.log(SLR_99)/np.log(2)
SLR_999 = np.log(SLR_999)/np.log(2)
SLR_max = np.log(SLR_max)/np.log(2)
# -------------------------------
PER = ""
if args.w == "Facebook":
    x = [0,1,2,3,4,5,6,7,8,9]
elif args.w == "Google":
    x = [0,1,2,3,4,5,6,7,8,9]
elif args.w == "WebSearch":
    x = [0,1,2,3,4,5,6,7,8,9,10]

fig, (ax1,ax2) = plt.subplots(1,2,figsize=(7,1.8))
# -------------------------------
# red, dimgray, magenta, limegreen, orange, dodgerblue, purple

ax1.plot(x, SLR_avg, color = 'purple', linestyle = '-', label = 'SkyNet_SLR', marker = 'd', linewidth = linewide)
ax1.plot(x, CV_avg, color = 'dodgerblue', linestyle = '-', label = 'SkyNet_CV', marker = '^', linewidth = linewide)


ax2.plot(x, SLR_99, color = 'purple', linestyle = '-', label = 'SkyNet_SLR', marker = 'd', linewidth = linewide)
ax2.plot(x, CV_99, color = 'dodgerblue', linestyle = '-', label = 'SkyNet_CV', marker = '^', linewidth = linewide)
# -------------------------------
fig.legend(methods, loc='upper center', bbox_to_anchor=(0.5, 1.12), fancybox=True, ncol=2, prop = font3, frameon = False)
# plt.subplots_adjust(wspace=0.24) #facebook
# plt.subplots_adjust(wspace=0.24) #websearch
plt.subplots_adjust(wspace=0.24) #google
ax1.tick_params(direction = 'in', top = False, bottom = True, left = True, right = False)
ax2.tick_params(direction = 'in', top = False, bottom = True, left = True, right = False)

ax1.set_xlabel('Flow size (Bytes)', fontproperties = font2)
ax1.set_ylabel('avg. FCT slowdown', fontproperties = font)

ax2.set_xlabel('Flow size (Bytes)', fontproperties = font2)
ax2.set_ylabel('99% FCT slowdown', fontproperties = font)
# -------------------------------

if args.w =="Facebook":
    ax1.set_xlim(0, 9)
    ax1.set_xticks(np.arange(10), ('324', '400', '500', '600', '700', '1K', '7K', '46K', '120K', '10M'), fontproperties = font, rotation = 30)
    ax2.set_xlim(0, 9)
    ax2.set_xticks(np.arange(10), ('324', '400', '500', '600', '700', '1K', '7K', '46K', '120K', '10M'), fontproperties = font, rotation = 30)
    if args.lossrate == 1000:
        ax1.set_ylim(0, 3)
        ax1.set_yticks(np.arange(0, 3.1, 1), (1, 2, 4, 8), fontproperties = font)
        ax2.set_ylim(2, 5)
        ax2.set_yticks(np.arange(2, 5.1, 1), (4, 8, 16, 32), fontproperties = font)
elif args.w == "Google":
    ax1.set_xlim(0, 9)
    ax1.set_xticks(np.arange(10), ('35', '74', '100', '156', '257', '313', '400', '573', '1.7K', '15.2M'), fontproperties = font, rotation = 30)
    ax2.set_xlim(0, 9)
    ax2.set_xticks(np.arange(10), ('35', '74', '100', '156', '257', '313', '400', '573', '1.7K', '15.2M'), fontproperties = font, rotation = 30)
    if args.lossrate == 1000:
        ax1.set_ylim(0, 1)
        ax1.set_yticks(np.arange(0, 1.0001, 1), (1, 2), fontproperties = font)
        ax2.set_ylim(2, 5)
        ax2.set_yticks(np.arange(2, 5.1, 1), (4, 8, 16, 32), fontproperties = font)
elif args.w == "WebSearch":
    ax1.set_xlim(0, 10)
    ax1.set_xticks(np.arange(11), ('7.3K', '20K', '30K', '50K', '73K', '200K', '1M', '2M', '5M', '10M', '30M'), fontproperties = font, rotation = 40)
    ax2.set_xlim(0, 10)
    ax2.set_xticks(np.arange(11), ('7.3K', '20K', '30K', '50K', '73K', '200K', '1M', '2M', '5M', '10M', '30M'), fontproperties = font, rotation = 40)
    if args.lossrate == 1000:
        ax1.set_ylim(0, 4)
        ax1.set_yticks(np.arange(0, 4.1, 1), (1, '', 4, '', 16), fontproperties = font)
        ax2.set_ylim(2, 5)
        ax2.set_yticks(np.arange(2, 5.1, 1), (4, 8, 16, 32), fontproperties = font)
# -------------------------------
if args.w == 'WebSearch':
    picture_name = '%s_80ms_%d_%s_SkyNet_SLR_NACK'%(args.w, args.lossrate, args.cc)
    plt.savefig('/home/wan/Experimental_Graph/paper/2_Websearch/%s.pdf'%picture_name, format = 'pdf' , dpi = 800 ,bbox_inches = 'tight')
elif args.w == 'Facebook':
    picture_name = '%s_20ms_%d_%s_SkyNet_SLR_NACK'%(args.w, args.lossrate, args.cc)
    plt.savefig('/home/wan/Experimental_Graph/paper/3_Facebook/%s.pdf'%picture_name, format = 'pdf' , dpi = 800 ,bbox_inches = 'tight')
elif args.w == 'Google':
    picture_name = '%s_30ms_%d_%s_SkyNet_SLR_NACK'%(args.w, args.lossrate, args.cc)
    plt.savefig('/home/wan/Experimental_Graph/paper/4_Google/%s.pdf'%picture_name, format = 'pdf' , dpi = 800 ,bbox_inches = 'tight')

plt.show()