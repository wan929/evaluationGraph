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
        'size': 12,
        }

font3 = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 12,
        }
# -------------------------------
parser = argparse.ArgumentParser(description = '')
parser.add_argument("-p", type = int , default = 6) # all, avg, 50, 95, 99, 999, max
parser.add_argument("-l", type = int , default = 6) #
parser.add_argument("-w", type = str , default = 'Facebook') #WebSearch, Facebook, Google
parser.add_argument("-cc", type = str , default = 'dcqcn' ) #dcqcn, hpcc, dctcp, timely
parser.add_argument("-lossrate", type = int , default = 1000) #dcqcn, hpcc, dctcp, timely
parser.add_argument("-rto", type = int , default = 1) #dcqcn, hpcc, dctcp, timely
args = parser.parse_args()

linewide = 1.5
methods = ['SADR_SV_NF', 'SADR_SV', 'SADR_CV_NF', 'SADR_CV']
# -------------------------------
# Origin SADR_SV SADR_CV SADR_SV_NF SADR_CV_NF LinkGuardian LinkGuardian_NB SADR_CV_SLR
file = "/home/wan/Experimental_Graph/paper/3_Facebook/fh_20ms_1000_dcqcn.csv"
with open(file, 'r') as f:       
        reader = csv.reader(f)
        result = list(reader)

        Origin_avg = result[0]
        Origin_50 = result[1]
        Origin_95 = result[2]
        Origin_99 = result[3]
        Origin_999 = result[4]
        Origin_max = result[5]

        SADR_SV_avg = result[6]
        SADR_SV_50 = result[7]
        SADR_SV_95 = result[8]
        SADR_SV_99 = result[9]
        SADR_SV_999 = result[10]
        SADR_SV_max = result[11]

        SADR_CV_avg = result[12]
        SADR_CV_50 = result[13]
        SADR_CV_95 = result[14]
        SADR_CV_99 = result[15]
        SADR_CV_999= result[16]
        SADR_CV_max = result[17]

        SADR_SV_NF_avg = result[18]
        SADR_SV_NF_50 = result[19]
        SADR_SV_NF_95 = result[20]
        SADR_SV_NF_99 = result[21]
        SADR_SV_NF_999 = result[22]
        SADR_SV_NF_max = result[23]

        SADR_CV_NF_avg = result[24]
        SADR_CV_NF_50 = result[25]
        SADR_CV_NF_95 = result[26]
        SADR_CV_NF_99 = result[27]
        SADR_CV_NF_999= result[28]
        SADR_CV_NF_max = result[29]
# -------------------------------
o_avg = [float(x) for x in Origin_avg]
o_50 = [float(x) for x in Origin_50]
o_95 = [float(x) for x in Origin_95]
o_99 = [float(x) for x in Origin_99]
o_999 = [float(x) for x in Origin_999]
o_max = [float(x) for x in Origin_max]

SV_avg = [float(x) for x in SADR_SV_avg]
SV_50 = [float(x) for x in SADR_SV_50]
SV_95 = [float(x) for x in SADR_SV_95]
SV_99 = [float(x) for x in SADR_SV_99]
SV_999 = [float(x) for x in SADR_SV_999]
SV_max = [float(x) for x in SADR_SV_max]

CV_avg = [float(x) for x in SADR_CV_avg]
CV_50 = [float(x) for x in SADR_CV_50]
CV_95 = [float(x) for x in SADR_CV_95]
CV_99 = [float(x) for x in SADR_CV_99]
CV_999 = [float(x) for x in SADR_CV_999]
CV_max = [float(x) for x in SADR_CV_max]

SV_NF_avg = [float(x) for x in SADR_SV_NF_avg]
SV_NF_50 = [float(x) for x in SADR_SV_NF_50]
SV_NF_95 = [float(x) for x in SADR_SV_NF_95]
SV_NF_99 = [float(x) for x in SADR_SV_NF_99]
SV_NF_999 = [float(x) for x in SADR_SV_NF_999]
SV_NF_max = [float(x) for x in SADR_SV_NF_max]

CV_NF_avg = [float(x) for x in SADR_CV_NF_avg]
CV_NF_50 = [float(x) for x in SADR_CV_NF_50]
CV_NF_95 = [float(x) for x in SADR_CV_NF_95]
CV_NF_99 = [float(x) for x in SADR_CV_NF_99]
CV_NF_999 = [float(x) for x in SADR_CV_NF_999]
CV_NF_max = [float(x) for x in SADR_CV_NF_max]

# l_avg = [float(x) for x in lossless_avg]
# l_50 = [float(x) for x in lossless_50]
# l_95 = [float(x) for x in lossless_95]
# l_99 = [float(x) for x in lossless_99]
# l_max = [float(x) for x in lossless_max]
# -------------------------------
# log(2)处理
o_avg = np.log(o_avg)/np.log(2)
o_50 = np.log(o_50)/np.log(2)
o_95 = np.log(o_95)/np.log(2)
o_99 = np.log(o_99)/np.log(2)
o_999 = np.log(o_999)/np.log(2)
o_max = np.log(o_max)/np.log(2)

SV_avg = np.log(SV_avg)/np.log(2)
SV_50 = np.log(SV_50)/np.log(2)
SV_95 = np.log(SV_95)/np.log(2)
SV_99 = np.log(SV_99)/np.log(2)
SV_999 = np.log(SV_999)/np.log(2)
SV_max = np.log(SV_max)/np.log(2)

CV_avg = np.log(CV_avg)/np.log(2)
CV_50 = np.log(CV_50)/np.log(2)
CV_95 = np.log(CV_95)/np.log(2)
CV_99 = np.log(CV_99)/np.log(2)
CV_999 = np.log(CV_999)/np.log(2)
CV_max = np.log(CV_max)/np.log(2)

SV_NF_avg = np.log(SV_NF_avg)/np.log(2)
SV_NF_50 = np.log(SV_NF_50)/np.log(2)
SV_NF_95 = np.log(SV_NF_95)/np.log(2)
SV_NF_99 = np.log(SV_NF_99)/np.log(2)
SV_NF_999 = np.log(SV_NF_999)/np.log(2)
SV_NF_max = np.log(SV_NF_max)/np.log(2)

CV_NF_avg = np.log(CV_NF_avg)/np.log(2)
CV_NF_50 = np.log(CV_NF_50)/np.log(2)
CV_NF_95 = np.log(CV_NF_95)/np.log(2)
CV_NF_99 = np.log(CV_NF_99)/np.log(2)
CV_NF_999 = np.log(CV_NF_999)/np.log(2)
CV_NF_max = np.log(CV_NF_max)/np.log(2)

# l_avg = np.log(l_avg)/np.log(2)
# l_50 = np.log(l_50)/np.log(2)
# l_95 = np.log(l_95)/np.log(2)
# l_99 = np.log(l_99)/np.log(2)
# l_max = np.log(l_max)/np.log(2)
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
# red, dimgray, magenta, limegreen, orange, dodgerblue
ax1.plot(x, SV_NF_avg, color = 'orange', linestyle = '--', label = 'SADR_SV_NF', marker = 'v', linewidth = linewide)
ax1.plot(x, SV_avg, color = 'orange', linestyle = '-', label = 'SADR_SV', marker = 'v', linewidth = linewide)
ax1.plot(x, CV_NF_avg, color = 'dodgerblue', linestyle = '--', label = 'SADR_CV_NF', marker = '^', linewidth = linewide)
ax1.plot(x, CV_avg, color = 'dodgerblue', linestyle = '-', label = 'SADR_CV', marker = '^', linewidth = linewide)

ax2.plot(x, SV_NF_999, color = 'orange', linestyle = '--', label = 'SADR_SV_NF', marker = 'v', linewidth = linewide)
ax2.plot(x, SV_999, color = 'orange', linestyle = '-', label = 'SADR_SV', marker = 'v', linewidth = linewide)
ax2.plot(x, CV_NF_999, color = 'dodgerblue', linestyle = '--', label = 'SADR_CV_NF', marker = '^', linewidth = linewide)
ax2.plot(x, CV_999, color = 'dodgerblue', linestyle = '-', label = 'SADR_CV', marker = '^', linewidth = linewide)


# -------------------------------
fig.legend(methods, loc='upper center', bbox_to_anchor=(0.5, 1.15), fancybox=True, ncol=4, prop = font3, frameon = False, columnspacing = 1.35)
plt.subplots_adjust(wspace=0.24) #facebook
# plt.subplots_adjust(wspace=0.32) #websearch
# plt.subplots_adjust(wspace=0.26) #google
ax1.tick_params(direction = 'in', top = False, bottom = True, left = True, right = False)
ax2.tick_params(direction = 'in', top = False, bottom = True, left = True, right = False)

ax1.set_xlabel('Flow size(Bytes)', fontproperties = font2)
ax1.set_ylabel('avg. FCT slowdown', fontproperties = font)

ax2.set_xlabel('Flow size(Bytes)', fontproperties = font2)
ax2.set_ylabel('99.9% FCT slowdown', fontproperties = font)
# -------------------------------
if args.w =="Facebook":
    ax1.set_xlim(0, 9)
    ax1.set_xticks(np.arange(10), ('324', '400', '500', '600', '700', '1K', '7K', '46K', '120K', '10M'), fontproperties = font, rotation = 30)
    ax2.set_xlim(0, 9)
    ax2.set_xticks(np.arange(10), ('324', '400', '500', '600', '700', '1K', '7K', '46K', '120K', '10M'), fontproperties = font, rotation = 30)
    if args.lossrate == 1000:
        ax1.set_ylim(0, 3)
        ax1.set_yticks(np.arange(0, 3.1, 1), (1, 2, 4, 8), fontproperties = font)
        ax2.set_ylim(3, 6)
        ax2.set_yticks(np.arange(3, 6.1, 1), (8, 16, 32,64), fontproperties = font)
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
        ax1.set_ylim(0, 7)
        ax1.set_yticks(np.arange(0, 7.1, 1), (1, '', 4, '', 16, '', 64, ''), fontproperties = font)
        ax2.set_ylim(2, 10)
        ax2.set_yticks(np.arange(2, 10.1, 1), (4, '',16,'',64,'',256, '', 1024), fontproperties = font)
# -------------------------------
if args.w == 'WebSearch':
    picture_name = '%s_80ms_%d_%s_filter'%(args.w, args.lossrate, args.cc)
    plt.savefig('/home/wan/Experimental_Graph/paper/2_Websearch/%s.pdf'%picture_name, format = 'pdf' , dpi = 800 ,bbox_inches = 'tight')
elif args.w == 'Facebook':
    picture_name = '%s_20ms_%d_%s_filter'%(args.w, args.lossrate, args.cc)
    plt.savefig('/home/wan/Experimental_Graph/paper/3_Facebook/%s.pdf'%picture_name, format = 'pdf' , dpi = 800 ,bbox_inches = 'tight')
elif args.w == 'Google':
    picture_name = '%s_30ms_%d_%s_filter'%(args.w, args.lossrate, args.cc)
    plt.savefig('/home/wan/Experimental_Graph/paper/4_Google/%s.pdf'%picture_name, format = 'pdf' , dpi = 800 ,bbox_inches = 'tight')

plt.show()