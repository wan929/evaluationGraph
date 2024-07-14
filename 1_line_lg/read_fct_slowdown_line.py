from os import remove

def get_pctl(a, p):
	i = int(len(a) * p)
	return a[i]

file = open('/home/wan/Desktop/High-Precision-Congestion-Control-master/simulation/mix/fct_topology_line_lg_flow_small_line_66ms_90load_dcqcn_1_1000_1_1000_10000_50_0.txt')  #打开文档
data = file.readlines()
tmp = []
a = []
for num in data:
    tmp.append([str(str(num.split(' ')[0])+str(num.split(' ')[1])+str(num.split(' ')[2])+str(num.split(' ')[3])),int(num.split(' ')[4]),float(num.split(' ')[6]),float(num.split(' ')[7])])

# test = []
# for item in tmp:
#     test.append([item[0], max(1,float(item[2]/item[3]))]) #fct_slowdown
# test.sort(key=lambda x:x[1])
# print(test[-1][0])

fct = []

for item in tmp:
    fct.append(max(1,float(item[2]/item[3]))) #fct_slowdown
fct.sort()
print(len(fct))
line = "%.9f,%.9f,%.9f,%.9f,%.9f"%(sum(fct) / len(fct), get_pctl(fct, 0.5), get_pctl(fct, 0.95), get_pctl(fct, 0.99), fct[-1])
print(line)