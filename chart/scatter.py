import random
from preprocessing import RangeScaler

### just dummy data and a quick peek

import numpy as np
from matplotlib import pyplot as plt
%matplotlib inline

size = 50
x = np.random.normal(1000, 500, size)
y = x * 3 + 200 + np.random.normal(0, 700, size)

plt.scatter(x, y)

#####

width = 30
height = 10

matrix = [[' '] * width for _ in range(height)]

wrs = RangeScaler((0, width-1))
hrs = RangeScaler((0, height-1))

x = wrs.fit_transform(x)
x = [int(round(xi)) for xi in x]
y = hrs.fit_transform(y)
y = [int(round(yi)) for yi in y]

list(zip(x, y))
max(x)
max(y)

mark = '🍑'
for (xi, yi) in zip(x, y):
    matrix[yi][xi] = mark

matrix = [row[::-1] for row in matrix]

xi
yi

def matrix_to_string(matrix):
    chart = ''
    for row in matrix:
        row_string = ''.join(row)
        chart += row_string
        chart += '\n'
    return chart

chart = matrix_to_string(matrix)
print(chart)
