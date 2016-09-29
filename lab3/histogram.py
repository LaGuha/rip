import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import lab3

fig, ax = plt.subplots()
rects1 = ax.bar(lab3.old.keys(), lab3.old.values(), 0.5)

plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Histogram of Ages')

plt.subplots_adjust()
plt.show()