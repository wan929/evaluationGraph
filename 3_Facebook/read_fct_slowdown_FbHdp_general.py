from os import remove

def get_pctl(a, p):
	i = int(len(a) * p)
	return a[i]

file = open('/home/wan/Experimental_Graph/paper/3_Facebook/fh_20ms_2_1000_1.txt')  #打开文档
data = file.readlines()
tmp = []
a = []
for num in data:
    tmp.append([str(str(num.split(' ')[0])+str(num.split(' ')[1])+str(num.split(' ')[2])+str(num.split(' ')[3])),int(num.split(' ')[4]),float(num.split(' ')[6]),float(num.split(' ')[7])])

r = []
r_1 = []
r_2 = []
r_3 = []
r_4 = []
r_5 = []
r_6 = []
r_7 = []
r_8 = []
r_9 = []
r_10 = []

for item in tmp:
    r.append([int(item[1]), max(1, float(item[2]/item[3]))]) #B,fct_slowdown

for i in r:
    if i[0] <= 324:
        r_1.append(i)
    elif i[0] <= 400:
        r_2.append(i)
    elif i[0] <= 500:
        r_3.append(i)
    elif i[0] <= 600:
        r_4.append(i)
    elif i[0] <= 700:
        r_5.append(i)
    elif i[0] <= 1000:
        r_6.append(i)
    elif i[0] <= 7000:
        r_7.append(i)
    elif i[0] <= 46000:
        r_8.append(i)
    elif i[0] <= 120000:
        r_9.append(i)
    elif i[0] <= 10000000:
        r_10.append(i)

r_1.sort(key=lambda x:x[1])
r_2.sort(key=lambda x:x[1])
r_3.sort(key=lambda x:x[1])
r_4.sort(key=lambda x:x[1])
r_5.sort(key=lambda x:x[1])
r_6.sort(key=lambda x:x[1])
r_7.sort(key=lambda x:x[1])
r_8.sort(key=lambda x:x[1])
r_9.sort(key=lambda x:x[1])
r_10.sort(key=lambda x:x[1])

fct_avg = []
fct_50 = []
fct_95 = []
fct_99 = []
fct_99_9 = []
fct_max = []

r_lists = [r_1, r_2, r_3, r_4, r_5, r_6, r_7, r_8, r_9, r_10]
for r_list in r_lists:
    fct = sorted(map(lambda x: x[1], r_list))
    fct_avg.append(sum(fct) / len(fct))
    fct_50.append(get_pctl(fct, 0.5))
    fct_95.append(get_pctl(fct, 0.95))
    fct_99.append(get_pctl(fct, 0.99))
    fct_99_9.append(get_pctl(fct, 0.999))
    fct_max.append(fct[-1])

fct_lists = [fct_avg, fct_50, fct_95, fct_99, fct_99_9, fct_max]
for fct_list in fct_lists:
    line = "%.9f,%.9f,%.9f,%.9f,%.9f,%.9f,%.9f,%.9f,%.9f,%.9f"%(fct_list[0], fct_list[1], fct_list[2], fct_list[3], fct_list[4], fct_list[5], fct_list[6], fct_list[7], fct_list[8], fct_list[9],)
    print(line)