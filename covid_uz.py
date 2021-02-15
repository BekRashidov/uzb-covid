import numpy as np
import matplotlib.pyplot as plt

data = {'Tashkent': 56324,
        'Namangan': 2547,
        'Samarkand': 2437,
        'Andijan': 2059,
        'Kashkadarya': 1505,
        'Bukhara': 1414,
        'Sirdarya': 1254,
        'Surkhandarya': 1038,
        'Karakalpakistan': 817,
        'Kherazm': 758,
        'Jizzakh': 739,
        'Fergana': 684,
        'Navai': 651}

group_data = list(data.values())
group_names = list(data.keys())
group_mean = np.mean(group_data)

plt.rcParams.update({'figure.autolayout': True})

fig, ax = plt.subplots()
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
ax.set(xlim=[0, 60000], xlabel='Infection Number per Region', ylabel='REGIONS',
       title='Covid-19 Infection (UZBEKISTAN)')
plt.show()
names = ['12-20', '30-50', '60-70']

values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.ylabel('Rate of Recovery in percent')
plt.subplot(132)
plt.scatter(names, values)
plt.xlabel('AGES')
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('RECOVERY RATE FROM COVID-19 (UZBEKISTAN)')

plt.show()
