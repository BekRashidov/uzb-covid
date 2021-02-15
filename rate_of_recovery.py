import matplotlib.pyplot as plt

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