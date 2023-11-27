import lightFunctions as j
import matplotlib.pyplot as plt
import numpy as np

photos = ['rtyt.jpg', 'naKAL_blye.jpg', 'naKAL_green.jpg', 'naKAL_red.jpg', 'naKAL_bel.jpg', 'naKAL_yelow.jpg']

rgb, I0 = j.read_image(photos[0], 'graph1.png', 'Ртутная лампа', 'белый лист')
I1 = j.read_image(photos[1], 'graph2.png', 'Лампа накаливания', 'синий лист')[-1]
I2 = j.read_image(photos[2], 'graph3.png', 'Лампа накаливания', 'зеленый лист')[-1]
I3 = j.read_image(photos[3], 'graph4.png', 'Лампа накаливания', 'красный лист')[-1]
I4 = j.read_image(photos[4], 'graph5.png', 'Лампа накаливания', 'белый лист')[-1]
I5 = j.read_image(photos[5], 'graph6.png', 'Лампа накаливая', 'желтый лист')[-1]

# Перевод из пикселей в нм
r = [i[0] for i in rgb]
b = [i[2] for i in rgb]
r_max, b_max = max(r), max(b)
i_r, i_b = r.index(r_max), b.index(b_max)
k = (610-435) / i_r

x = np.linspace(0, 264, 264)
x = [(i * k + 435) for i in x]

# Clear
plt.cla()
plt.clf()

# Отраженная интенсивность I

ax = plt.axes()
ax.set_facecolor(color='#E5E4E2')
ax.grid(which='major', linewidth=1)
ax.grid(which='minor', linewidth=0.7, linestyle='--')
ax.minorticks_on()
ax.set_xlim(xmin=435, xmax=650)

plt.plot(x, I1, color='blue', label='blue')
plt.plot(x, I2, color='green', label='green')
plt.plot(x, I3, color='red', label='red')
plt.plot(x, I4, color='white', label='white')
plt.plot(x, I5, color='yellow', label='yellow')

plt.legend()
plt.title('Отражённая интенсивность излучения лампы накаливания')
plt.ylabel('яркость')
plt.xlabel('длина волны, нм')
plt.savefig('I.png')

A1 = [I1[i] / I4[i] for i in range(len(I1))]
A2 = [I2[i] / I4[i] for i in range(len(I1))]
A3 = [I3[i] / I4[i] for i in range(len(I1))]
A4 = [I4[i] / I4[i] for i in range(len(I1))]
A5 = [I5[i] / I4[i] for i in range(len(I1))]

# Зависимость альбедо А

plt.cla()
plt.clf()

ax = plt.axes()
ax.set_facecolor(color='#E5E4E2')
ax.grid(which='major', linewidth=1)
ax.grid(which='minor', linewidth=0.7, linestyle='--')
ax.minorticks_on()
ax.set_xlim(xmin=435, xmax=650)

plt.plot(x, A1, color='blue', label='blue')
plt.plot(x, A2, color='green', label='green')
plt.plot(x, A3, color='red', label='red')
plt.plot(x, A4, color='white', label='white')
plt.plot(x, A5, color='yellow', label='yellow')

plt.legend()
plt.title('Зависимость альбедо поверхностей от длины волны падающего света')
plt.ylabel('альбедо')
plt.xlabel('длина волны, нм')
plt.savefig('A.png')
