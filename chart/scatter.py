import random
from preprocessing import RangeScaler

### just dummy data and a quick peek

import numpy as np
from matplotlib import pyplot as plt
%matplotlib inline

size = 100
x = np.random.normal(1000, 500, size)
y = x * 3 + 200 + np.random.normal(0, 700, size)

plt.scatter(x, y)

#####

width = 20
height = 20

matrix = [[' '] * width for _ in range(height)]

wrs = RangeScaler((0, width))
hrs = RangeScaler((0, height))

x = wrs.fit_transform(x)
x = [int(round(xi))-1 for xi in x]
y = wrs.fit_transform(y)
y = [int(round(yi))-1 for yi in y]

mark = '⋄'
for (xi, yi) in zip(x, y):
    matrix[xi][yi] = mark

def matrix_to_string(matrix):
    chart = ''
    for row in matrix:
        row_string = ''.join(row)
        chart += row_string
        chart += '\n'
    return chart

chart = matrix_to_string(matrix)
print(chart)
