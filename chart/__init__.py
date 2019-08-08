import sys
import random
import numpy as np
import pandas as pd

decimal_ticks = {
    1: '▏',
    2: '▏',
    3: '▎',
    4: '▍',
    5: '▌',
    6: '▋',
    7: '▊',
    8: '▉',
    9: '█'
}

TICK = '▇'

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
        y = [scale(yi, (self.min_, self.max_), self.range) for yi in y]
        return y

    def fit_transform(self, y):
        self.fit(y)
        return self.transform(y)

def create_label(label, padding=10):
    label = label[:padding]
    label = label.rjust(padding)
    label += ': '
    return label

def build_row(label, data):
    label = create_label(label)
    row = ''
    row += label
    row_data = data * TICK
    row_data = row_data.ljust(20)
    row += row_data
    return row

df = pd.DataFrame({
    'x': ['Toronto', 'Hamilton', 'Carlisle', 'Hong Kong'],
    'y': [3_000_000, 300_000, 3_000, 5_000_000]
})

rs = RangeScaler((0, 20))
y = rs.fit_transform(df.y)
data = [round(yi) for yi in y]
labels = [create_label(l) for l in df.x]

chart = ''
for d, l in zip(data, labels):
    row = build_row(l, d)
    chart += row
    chart += '\n'

print(chart)
