import matplotlib.pyplot as plt

labels = 'Python', 'C++', 'Ruby', 'Perl', 'Java', 'PHP'

sizes = [33, 55, 12, 17, 62, 68]
separated = (.1, 0, 0, 0, 0, 0,)

plt.pie(sizes, labels=labels, autopct='%1.1f%%', explode=separated)
plt.axis('equal')
plt.show()
