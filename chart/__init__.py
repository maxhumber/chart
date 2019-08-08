import sys
import random
import numpy as np
import pandas as pd

# ANSI escape SGR Parameters color codes
AVAILABLE_COLORS = {
    'red': 91,
    'blue': 94,
    'green': 92,
    'magenta': 95,
    'yellow': 93,
    'black': 90,
    'cyan': 96
}

TICK = '▇'
SM_TICK = '▏'

color = AVAILABLE_COLORS['cyan']

r = 15
c = r * 3

matrix = [[' '] * c for _ in range(r)]
chart = ''
for row in matrix:
    row_string = ''.join(row)
    chart += row_string
    chart += '\n'

def matrix_to_string(matrix):
    chart = ''
    for row in matrix:
        row_string = ''.join(row)
        chart += row_string
        chart += '\n'
    return chart

sys.stdout.write(f'\033[{color}m') # Start to write colorized.
sys.stdout.write(chart)
sys.stdout.write('\033[0m') # Back to original.

def random_tick():
    return random.choices([' ', '⋄'], weights=[0.5, 0.5])[0]

from itertools import product

list(product([1,2,3], [1, 2,3]))

matrix = [[' '] * c for _ in range(r)]
for (x, y) in product(range(r), range(c)):
    tick = random_tick()
    print(tick)
    matrix[x][y] = tick

chart = matrix_to_string(matrix)

sys.stdout.write(f'\033[{color}m') # Start to write colorized.
sys.stdout.write(chart)
sys.stdout.write('\033[0m') # Back to original.

size = 100
x = np.random.normal(1000, 500, size)
y = x * 3 + 200 + np.random.normal(0, 700, size)

from matplotlib import pyplot as plt
%matplotlib inline

plt.scatter(x, y)

df = pd.DataFrame({'x': x, 'y': y})
df

from sklearn.preprocessing import MinMaxScaler

np.set_printoptions(suppress=True)

def scale(x, xmin, xmax, tmin, tmax):
    return (x - xmin) / (xmax - xmin) * (tmax - tmin) + tmin

[scale(xi, x.min(), x.max(), 0, 20) for xi in x]

def scale(x, xin=(0, 1), xout=(0, 100)):
    return (x - xin[0]) / (xin[1] - xin[0]) * (xout[1] - xout[0]) + xout[0]


#####


import numpy as np
size = 100
x = np.random.normal(1000, 500, size)
x = x.tolist()

def scale(x, xin=(0, 1), xout=(0, 100)):
    return (x - xin[0]) / (xin[1] - xin[0]) * (xout[1] - xout[0]) + xout[0]

class RangeScaler:
    def __init__(self, range=(0, 100)):
        self.range = range

    def fit(self, y):
        self.min_ = min(y)
        self.max_ = max(y)
        return self

    def transform(self, y):
        return [scale(yi, (self.min_, self.max_), self.range) for yi in y]

rs = RangeScaler(range=(0, 20))
rs.fit(x)
z = rs.transform(x)

[round(zi) for zi in z]






    # def fit_transform(self, y):
    #     self.fit(y)
    #     return self.transform(y)
    #
    # def inverse_transform(self, y):
    #     decoder = {v:k for k, v in self.encoder.items()}
    #     if not isinstance(y, list):
    #         return decoder.get(y)
    #     return [decoder.get(yi) for yi in y]





#
