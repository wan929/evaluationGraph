import matplotlib.pyplot as plt
import numpy as np
def get_pctl(a, p):
	i = int(len(a) * p)
	return a[i]
font = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 8,
        }

font1 = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 8,
        }

font2 = {'family': 'Times New Roman',
        'weight': 'normal',
        'size': 8,
        }
# single_10load
fct_0 = [1.084789970,1.000000000,1.000000000,1.000238796,81.044042281] #O
fct_1_0 = [1.000524625,1.000000000,1.000000000,1.000160102,1.497333439] #CV
fct_1_1 = [1.001203088,1.000000000,1.000000000,1.000238815,2.146679408] #SV
fct_2_0 = [1.002358291,1.000000000,1.000000000,1.119645848,1.256195713] #LG
fct_2_1 = [1.000189537,1.000000000,1.000000000,1.000238815,1.202071713] #LG_NB

# single_30load
# fct_0 = [1.085137064,1.000000000,1.000479386,1.005445227,81.083780537] #O
# fct_1_0 = [1.000686219,1.000000000,1.000479693,1.005441741,1.979738354] #CV
# fct_1_1 = [1.001376708,1.000000000,1.000479962,1.005441741,2.169220945] #SV
# fct_2_0 = [1.327983906,1.000000000,2.534617845,3.016642663,3.797933686] #LG
# fct_2_1 = [1.000377025,1.000000000,1.000559597,1.005732941,1.228384732] #LG_NB

# single_60load
# fct_0 = [1.088453651,1.000000000,1.012698666,1.023203713,81.087548015] #O
# fct_1_0 = [1.002701046,1.000000000,1.012717965,1.023202041,1.612155488] #CV
# fct_1_1 = [1.003409169,1.000000000,1.012711864,1.023203713,2.277180406] #SV
# fct_2_0 = [1.789683981,1.426986914,3.552105010,4.019543714,4.310995602] #LG
# fct_2_1 = [1.002457420,1.000000000,1.013022290,1.023680000,1.282084066] #LG_NB

# single_90load
# fct_0 = [1.356757529,1.256705901,1.506211180,1.572376839,137.752499000] #O
# fct_1_0 = [1.277933321,1.261331841,1.519535629,1.582059694,1.782844388] #CV
# fct_1_1 = [1.307260646,1.286057308,1.546990833,1.614270858,2.478163673] #SV
# fct_2_0 = [15.128046633,15.948832747,25.123772259,26.762148338,27.128324255] #LG
# fct_2_1 = [1.002457420,1.000000000,1.013022290,1.023680000,1.282084066] #LG_NB


methods = ['Libra-S', 'Libra-C', 'LinkGuardian']

load_levels = ['avg', '99%']

fct_values1 = {
    'avg': [1.001203088/1.000524625, 1, 1.002358291/1.000524625],
    '99%': [1.000238815/1.000160102, 1, 1.119645848/1.000160102],
}
fct_values2 = {
    'avg': [1.001376708/1.000686219, 1, 1.327983906/1.000686219],
    '99%': [1.005441741/1.005441741, 1, 3.016642663/1.005441741],
}
fct_values3 = {
    'avg': [1.003409169/1.002701046, 1, 1.789683981/1.002701046],
    '99%': [1.023203713/1.023202041, 1, 4.019543714/1.023202041],
}
fct_values4 = {
    'avg': [1.307260646/1.277933321, 1, 15.128046633/1.277933321],
    '99%': [1.614270858/1.582059694, 1, 26.762148338/1.582059694],
}

# fct_values1 = {
#     'avg': [1.001203088/1.000524625, 1, 1.002358291/1.000524625],
#     '99.9%': [2.146679408/1.497333439, 1, 1.256195713/1.497333439],
# }
# fct_values2 = {
#     'avg': [1.001376708/1.000686219, 1, 1.327983906/1.000686219],
#     '99.9%': [2.169220945/1.979738354, 1, 3.797933686/1.979738354],
# }
# fct_values3 = {
#     'avg': [1.003409169/1.002701046, 1, 1.789683981/1.002701046],
#     '99.9%': [2.277180406/1.612155488, 1, 4.310995602/1.612155488],
# }
# fct_values4 = {
#     'avg': [1.307260646/1.277933321, 1, 15.128046633/1.277933321],
#     '99.9%': [2.478163673/1.782844388, 1, 27.128324255/1.782844388],
# }

colors = ['orange', 'dodgerblue', 'green']#
# red, dimgray, magenta, limegreen, orange, dodgerblue
# 绘制柱状图
bar_width = 0.25
index = np.arange(len(load_levels))
# plt.figure(figsize=(4,2))
fig, (ax1,ax2,ax3,ax4) = plt.subplots(1,4,figsize=(4,1.5))

for i, method in enumerate(methods):
    ax1.bar(index + i * bar_width, [fct_values1[load][i] for load in load_levels], bar_width, color = colors[i])
for i, method in enumerate(methods):
    ax2.bar(index + i * bar_width, [fct_values2[load][i] for load in load_levels], bar_width, color = colors[i])
for i, method in enumerate(methods):
    ax3.bar(index + i * bar_width, [fct_values3[load][i] for load in load_levels], bar_width, color = colors[i])
for i, method in enumerate(methods):
    ax4.bar(index + i * bar_width, [fct_values4[load][i] for load in load_levels], bar_width, color = colors[i])

# 设置图表参数
ax1.set_xlabel('10% load', fontproperties = font)
ax1.set_ylabel('Normalized FCT', fontproperties = font)
ax1.set_xticks(index + bar_width * (len(methods) - 1) / 2, fontproperties = font)
ax1.set_xticklabels(load_levels, fontproperties = font)
ax1.set_ylim(0, 2.1)
ax1.set_yticks(np.arange(0, 2.1, 1), fontproperties = font1)
ax1.set_yticklabels([0, 1, 2],fontproperties = font1)

ax2.set_xlabel('30% load', fontproperties = font)
#ax2.set_ylabel('Normalized FCT', fontproperties = font)
ax2.set_xticks(index + bar_width * (len(methods) - 1) / 2, fontproperties = font)
ax2.set_xticklabels(load_levels, fontproperties = font)
ax2.set_ylim(0, 3.1)
ax2.set_yticks(np.arange(0, 3.1, 1), fontproperties = font1)
ax2.set_yticklabels([0, 1, 2, 3],fontproperties = font1)

ax3.set_xlabel('60% load', fontproperties = font)
#ax3.set_ylabel('Normalized FCT', fontproperties = font)
ax3.set_xticks(index + bar_width * (len(methods) - 1) / 2, fontproperties = font)
ax3.set_xticklabels(load_levels, fontproperties = font)
ax3.set_ylim(0, 4.1)
ax3.set_yticks(np.arange(0, 4.1, 2), fontproperties = font1)
ax3.set_yticklabels([0, 2, 4],fontproperties = font1)

ax4.set_xlabel('90% load', fontproperties = font)
#ax4.set_ylabel('Normalized FCT', fontproperties = font)
ax4.set_xticks(index + bar_width * (len(methods) - 1) / 2, fontproperties = font)
ax4.set_xticklabels(load_levels, fontproperties = font)
ax4.set_ylim(0, 18.5)
ax4.set_yticks(np.arange(0, 18.5, 6), fontproperties = font1)
ax4.set_yticklabels([0, 6, 12, 18],fontproperties = font1)
# plt.ylim(0, 15.1)
# plt.yticks(np.arange(0, 15.1, 5), fontproperties = font1)
#ax.legend()
# 显示图例在图片的外部上层
fig.legend(methods,loc='upper center', bbox_to_anchor=(0.5, 1.07), fancybox=True, ncol=3, prop = font, frameon = False, handlelength = 0.68)
plt.subplots_adjust(wspace=0.5)
ax1.tick_params(direction = 'in', top = False, bottom = False, left = True, right = False)
ax2.tick_params(direction = 'in', top = False, bottom = False, left = True, right = False)
ax3.tick_params(direction = 'in', top = False, bottom = False, left = True, right = False)
ax4.tick_params(direction = 'in', top = False, bottom = False, left = True, right = False)
plt.savefig('/home/wan/Experimental_Graph/paper/1_line_lg/single/allload_only_avg_99_new_Libra.pdf', format = 'pdf' , dpi = 800 ,bbox_inches = 'tight')
# 显示图表
plt.show()