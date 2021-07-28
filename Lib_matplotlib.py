import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Pandas & matplotlib
s = pd.Series([18, 42, 9, 32, 81, 64, 3])
s.plot(kind='bar')
plt.savefig('file/plot01.png')
plt.savefig('file/plot01.pdf')

df = pd.DataFrame(
    {
        'a': [10, 20, 30, 40, 50, 60, 70, 80, 90],
        'b': [22, 63, 98, 54, 63, 75, 11, 52, 39],
        'c': [99, 88, 77, 66, 55, 44, 33, 22, 11]
    }
)

df[['a', 'b', 'c']].plot()
plt.savefig('file/plot02.png')
plt.savefig('file/plot02.pdf')

df[['a', 'c']].plot(kind='bar', stacked=True)
plt.savefig('file/plot03.png')
plt.savefig('file/plot03.pdf')

df[['a', 'c']].plot(kind='hist', stacked=True)
plt.savefig('file/plot04.png')
plt.savefig('file/plot04.pdf')

df[['b']].plot(kind='area', stacked=True)
plt.savefig('file/plot05.png')
plt.savefig('file/plot05.pdf')

df[['a', 'c']].plot(kind='scatter', x='a', y='c')
plt.savefig('file/plot06.png')
plt.savefig('file/plot06.pdf')

df[['a', 'c']].plot(kind='pie', x='a', y='c')
plt.savefig('file/plot07.png')
plt.savefig('file/plot07.pdf')

# Numpy and Matplotlib

t = np.arange(0, 16, 0.5)
print(t.shape)
List = [2, 10, 1, 15, 6, 7, 8, 9, 4, 19]
data = np.random.choice(List, size=(4, 32))
print(data.shape)

F1 = data[0]
F2 = data[1]
F3 = data[2]
F4 = data[3]


plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.style"] = "normal"
fig, axs = plt.subplots(2, 2, figsize=(15, 7))

# Col Right

axs[0, 0].plot(t, F1, color='#ea4335', linewidth=0.3)
axs[0, 0].set_xlim(0, 15)
axs[0, 0].set_ylim(0, 20)
axs[0, 0].set_yticks([0, 5, 10, 15, 20])
axs[0, 0].set_xticks([0, 5, 10, 15])
# axs[0, 2].set_title('(c)')

axs[1, 0].plot(t, F2, color='#ea4335', linewidth=0.3)
axs[1, 0].set_xlim(0, 15)
axs[1, 0].set_ylim(0, 20)
axs[1, 0].set_yticks([0, 5, 10, 15, 20])
axs[1, 0].set_xticks([0, 5, 10, 15])

axs[1, 1].plot(t, F3, color='#9256d9', linewidth=0.3)
axs[1, 1].set_xlim(0, 15)
axs[1, 1].set_ylim(0, 20)
axs[1, 1].set_yticks([0, 5, 10, 15, 20])
axs[1, 1].set_xticks([0, 5, 10, 15])

# Col middle

axs[0, 1].plot(t, F4, color='#34a853', linewidth=0.3)
axs[0, 1].set_xlim(0, 15)
axs[0, 1].set_ylim(0, 20)
axs[0, 1].set_yticks([0, 5, 10, 15, 20])
axs[0, 1].set_xticks([0, 5, 10, 15])
# axs[0, 1].set_title('(b)')

i = 0
for ax in axs.flat:
    i+=1
    if i==7:
        ax.set(xlabel='Time', ylabel='random number')
    elif i==8:
        ax.set(xlabel='Time', ylabel='random number')
    elif i==9:
        ax.set(xlabel='Time', ylabel='random number')
    else:
        ax.set(xlabel='Time', ylabel='random number')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()

plt.savefig('file/plot08.pdf', transparent=True, pad_inches=0)
plt.savefig('file/plot08.svg', transparent=True, dpi=1200, pad_inches=0)
