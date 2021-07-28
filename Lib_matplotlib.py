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

