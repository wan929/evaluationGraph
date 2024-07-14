import matplotlib.pyplot as plt
import numpy as np

font = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 13,
        }

font1 = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 13,
        }

# goodput_avg = []
# goodput_avg_nom = []
# list_s = [1, 0.92, 0.75, 0.6, 0.25, 0.03]
# for list_tmp in list_s:
#         goodput_avg.append(sum(list_tmp) / len(list_tmp))
# a = goodput_avg[0]
# for b in goodput_avg:
#     goodput_avg_nom.append(b / a)
goodput_avg_nom = [1, 0.95, 0.76, 0.6, 0.25, 0.03]
x = [0, 1, 2, 3, 4, 5]
fig, ax = plt.subplots(figsize=(5,2.5))
plt.plot(x, goodput_avg_nom, color = 'red', marker = 'v', markersize = 10, linestyle = '-', linewidth = 1.5, clip_on = False)
# plt.legend()
# ax = plt.gca()
# ax.legend(loc = 'best' , ncol = 1 , prop = font1)
plt.tick_params(direction = 'in', top = False, bottom = True, left = True, right = False)
plt.xlabel('Packet Loss Rate', fontproperties = font)
plt.ylabel('Normalized throughput', fontproperties = font)
plt.xlim(0, 5)
plt.ylim(0, 1)
plt.xticks(np.arange(6), ['0','0.0001', '0.001', '0.002', '0.005', '0.01'], fontproperties = font, rotation = 0)
plt.yticks(np.arange(0,1.001,0.25), ['0','0.25', '0.5', '0.75', '1'], fontproperties = font)
# plt.grid() #网格
plt.savefig('/home/wan/Experimental_Graph/paper/5_throughtput_drop/throughput_drop.pdf', format = 'pdf' , dpi = 800 ,bbox_inches = 'tight')
plt.show()