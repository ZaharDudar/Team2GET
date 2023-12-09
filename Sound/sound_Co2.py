from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'serif'})
rc('text.latex',preamble=r'\usepackage[utf8]{inputenc}')
rc('text.latex',preamble=r'\usepackage[russian]{babel}')
plt.rcParams['text.usetex'] = True        


def speed_sound(T,nu, c_co2):
    c_h20 = nu * 2642.4/101325
    c_o2 = 1 - (78.99+0.93)*10**-2 - c_co2
    c_nar = (78.99+0.93)*(1-c_h20)*10**-2
    c_noar = c_o2*(1-c_h20) + c_nar
    c_co2*=(1-c_h20)
    # print(c_h20+c_noar+c_co2)
    M = (28.97*c_noar + 18.01*c_h20 + 44.01*c_co2) * 10**-3
    gamma_1 =  28.97*c_noar*1.0036 + 18.01*c_h20*1.863 + 44.01*c_co2*0.838
    gamma_2 =  28.97*c_noar*0.7166 + 18.01*c_h20*1.403 + 44.01*c_co2*0.649
    gamma = gamma_1/gamma_2
    return sqrt(gamma*8.314462*T/M)

co2_conc = np.linspace(0,0.05,100)
v_of_co2_27 = []
for c in co2_conc:
    v_of_co2_27.append(speed_sound(22.6+273,0.278,c))

v_of_co2_100 = []
for c in co2_conc:
    v_of_co2_100.append(speed_sound(22.6+273,1,c))

# plt.plot(co2_conc*100,np.polyval(np.polyfit(co2_conc,v_of_co2_27,1),co2_conc),'o')


plt.plot(co2_conc*100, v_of_co2_27, label = "27\% влажности")
plt.plot(co2_conc*100, v_of_co2_100, label = "100\% влажности")


v_clear, v_dirt = 344.9, 342.8
p27 =  np.polyfit(co2_conc,v_of_co2_27,1)
p100 =  np.polyfit(co2_conc,v_of_co2_100,1)

c_clear = (v_clear - p27[1])/p27[0] * 100
c_dirt = (v_dirt - p100[1])/p100[0] * 100

plt.plot(c_clear,v_clear,'*', label=f"Чистый воздух: {v_clear} м/с, [{round(c_clear,2)}\%]")
plt.plot(c_dirt,v_dirt,'*', label=f"Выдыхаемый воздух: {v_dirt} м/с, [{round(c_dirt,2)}\%]")

plt.grid()
plt.minorticks_on()
plt.grid(which="minor",linestyle='--',)
plt.legend(loc="upper right")
plt.xlabel(r"Концентрация $CO_2$ (\%)")
plt.ylabel("Скорость звука (м/с)")
plt.title(r"Зависимость скорости звука \\от концентрации углекислого газа")
plt.savefig("АналитическийГрафик")

plt.show()