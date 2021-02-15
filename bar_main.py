import matplotlib.pyplot as plt
import numpy as np

# creating a data
col_count = 3
bar_width = .2

korea_scores = (554, 536, 538)
canada = (518, 523, 525)
china_scores = (613, 570, 580)
france_scores = (495, 505, 499)

# putting a data into visualization
index = np.arange(col_count)

k1 = plt.bar(index, korea_scores, bar_width,
             alpha=.4,
             label="Korea")
c1 = plt.bar(index + 0.2, canada, bar_width, alpha=.4,
             label="Canada")
ch1 = plt.bar(index + 0.4, china_scores, bar_width, alpha=.3,
              label="China")
f1 = plt.bar(index + 0.6, france_scores, bar_width, alpha=.4,
             label="France")


# configuring the data

def CreateLabels(data):
    for item in data:
        height = item.get_height()
        plt.text(item.get_x() + item.get_width() / 2., height * 1.05,
                 '%d' % int(height),
                 ha='center', va='bottom')


CreateLabels(k1)
CreateLabels(c1)
CreateLabels(ch1)
CreateLabels(f1)

plt.ylabel("Mean Score in PISA 2021")
plt.xlabel("Subjects")
plt.title("Test Scores by Country")
plt.xticks(index + .3 / 2, ("Math", "Reading", "Science"))
plt.legend(frameon=False, bbox_to_anchor=(1, 1), loc=2)
plt.grid(True)
plt.show()
