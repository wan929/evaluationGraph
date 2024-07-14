import numpy as np
import matplotlib.pyplot as plt

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
def get_pctl(a, p):
	i = int(len(a) * p)
	return a[i]
# 读取数据文件
def read_data(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        data = [float(line.strip()) / 1000 for line in lines] # 转换为ns单位
    return data

# 计算CDF
def calculate_cdf(data):
    sorted_data = np.sort(data)
    n = len(data)
    print(get_pctl(sorted_data, 0.99))
    cdf = np.arange(1, n + 1) / n
    return sorted_data, cdf

# 画CDF图
def plot_cdf(sorted_data1, cdf1, sorted_data2, cdf2):
    fig, ax = plt.subplots(figsize=(2,1.3))
    plt.plot(sorted_data1, cdf1, label='NetSeer', linewidth = 1.5, color = 'grey')
    plt.plot(sorted_data2, cdf2, label='SkyNet', linewidth = 2, color = 'dodgerblue')
    plt.xlabel('Detection time (us)', fontproperties = font1)
    plt.xlim(2, 2.800000001)
    plt.xticks(np.arange(2,2.800000001,0.2), ('2.0', '2.2', '2.4', '2.6', '2.8'), fontproperties = font1, rotation = 20)
    plt.ylabel('CDF', fontproperties = font1)
    plt.ylim(0, 1.00000001)
    plt.yticks(np.arange(0, 1.00000001, 0.25), ['0','0.25', '0.5', '0.75', '1'], fontproperties = font1)
    plt.legend(loc='best', fancybox=True, ncol=1, prop = font2, frameon = False)
    plt.tick_params(direction = 'in', top = False, bottom = True, left = True, right = False)
    plt.savefig('/home/wan/Experimental_Graph/paper/1_line_lg/detection_time/cdftime_new.pdf', format = 'pdf' , dpi = 800 ,bbox_inches = 'tight')
    plt.show()

# 读取数据
dataset1 = read_data('/home/wan/Experimental_Graph/paper/1_line_lg/detection_time/netseer.txt')
dataset2 = read_data('/home/wan/Experimental_Graph/paper/1_line_lg/detection_time/SADR.txt')

# 计算CDF
sorted_data1, cdf1 = calculate_cdf(dataset1)
sorted_data2, cdf2 = calculate_cdf(dataset2)

# 画图
plot_cdf(sorted_data1, cdf1, sorted_data2, cdf2)