from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'serif'})
rc('text.latex',preamble=r'\usepackage[utf8]{inputenc}')
rc('text.latex',preamble=r'\usepackage[russian]{babel}')
plt.rcParams['text.usetex'] = True        

def search_first_peak_ind(data):
    for i in range(len(data)):
        if(data[i]!=0):
            if(data[i-1]<data[i]):
                j = i
                while True:
                    if data[j] > data[i]:
                        break
                    if data[j] < data[i]:
                        return i
                    j+=1


n = int(input())

data1 = []
data2 = []
if n==0:
    with open("./rawData/lungs3_0.txt", 'r') as f:
        for line in f.readlines():
            data1.append(int(line.strip()))   
    with open("./rawData/lungs3_1.txt", 'r') as f:
        for line in f.readlines():
            data2.append(int(line.strip())) 
else:
    with open("./rawData/atm_0.txt", 'r') as f:
        for line in f.readlines():
            data1.append(int(line.strip()))   
    with open("./rawData/atm_1.txt", 'r') as f:
        for line in f.readlines():
            data2.append(int(line.strip())) 

data1 = np.array(data1)
data2 = np.array(data2)

n_noise = 200

noise_threshold = 0.2

data1 = (data1 - np.sum(data1[0:n_noise])/n_noise)
data2 = (data2 - np.sum(data2[0:n_noise])/n_noise)
data1 /= max(data1)
data2 /= max(data2)

data1raw = data1.copy()
data2raw = data2.copy()


data1 = np.where(np.abs(data1)<=noise_threshold, np.zeros_like(data1), data1)
data2 = np.where(np.abs(data2)<=noise_threshold, np.zeros_like(data2), data2)

anchor_p1 = search_first_peak_ind(data1)
anchor_p2 = search_first_peak_ind(data2)


# data1c = (data1c - np.sum(data1c[0:n_noise])/n_noise)
# data1c /= max(data1c)
# plt.plot(anchor_p1, 0,'o')
# plt.plot(anchor_p2, 0,'o')

# plt.plot(np.arange(len(data1)), data1c)

# plt.plot(np.arange(len(data1)), data1)
# plt.plot(np.arange(len(data2))-anchor_p2+anchor_p1, data2)

plt.grid(which="both")
plt.xlim(0,0.006)
# plt.ylim(0,1000)
plt.plot(np.arange(len(data1))/(500*10**3), data1raw, label="Первый датчик")
plt.plot((np.arange(len(data2))-anchor_p2+anchor_p1)/(500*10**3), data2raw, label="Второй датчик")
print(1.156 / ((anchor_p2-anchor_p1)/(500*10**3)))
plt.plot([],[],' ',label=f"Скорость: {round(1.156 / ((anchor_p2-anchor_p1)/(500*10**3)),1)} м/с")
plt.legend(loc='upper right')
if n == 0:
    plt.title("Воздух после выдоха")
    plt.xlabel("Время (с)")
    plt.ylabel("Громкость (у.е.)")
    plt.savefig("./ВоздухПослеВыдоха")
else:
    plt.title("Воздух чистый")
    plt.xlabel("Время (с)")
    plt.ylabel("Громкость (у.е.)")
    plt.savefig("./ВоздухЧистый")

plt.show()