import random
from preprocessing import RangeScaler

def scale_values(values, scale):
    values = RangeScaler((0, scale-1)).fit_transform(values)
    values = [int(round(v)) for v in values]
    return values

def matrix_to_string(matrix):
    string = ''
    for row in matrix:
        row_string = ''.join(row)
        string += row_string
        string += '\n'
    return string

def scatter(x, y, width=40, height=None, mark='•'):
    if not height:
        height = int(width / 3 // 1)
    matrix = [[' '] * width for _ in range(height)]
    x = scale_values(x, width)
    y = scale_values(y, height)
    for (xi, yi) in zip(x, y):
        matrix[yi][xi] = mark
    matrix = matrix[::-1]
    chart = matrix_to_string(matrix)
    print(chart)

if __name__ == '__main__':
    import numpy as np
    from matplotlib import pyplot as plt
    %matplotlib inline

    size = 50
    x = np.random.normal(1000, 500, size)
    y = x * 3 + 200 + np.random.normal(0, 700, size)

    plt.scatter(x, y)

    scatter(x, y, mark='🐞')
