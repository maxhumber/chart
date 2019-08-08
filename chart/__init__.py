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

def build_row(data, label, width=20):
    row = data * TICK
    row = row.ljust(width)
    row = label + row
    return row

TICK = '▇'

df = pd.DataFrame({
    'x': ['Toronto', 'Hamilton', 'Carlisle', 'Hong Kong'],
    'y': [3_000_000, 300_000, 3_000, 5_000_000]
})
#
# width = 40
# labels = df.x.values.tolist()
# max_label_len = max([len(l) for l in labels])
#
# labels = [create_label(l, padding=max_label_len) for l in labels]
#
# rs = RangeScaler((0, 20))
# y = rs.fit_transform(df.y)
# data = [round(yi) for yi in y]

#
# chart = ''
# for d, l in zip(data, labels):
#     row = build_row(d, l)
#     chart += row
#     chart += '\n'
#
# print(chart)

def bar(data, labels, width=30, label_width=None):
    if not label_width:
        label_width = max([len(l) for l in labels])
    labels = [create_label(l, padding=label_width) for l in labels]
    data = RangeScaler((0, width)).fit_transform(data)
    data = [round(di) for di in data]
    chart = ''
    for d, l in zip(data, labels):
        row = build_row(d, l)
        chart += row
        chart += '\n'
    print(chart)

bar(df.y, df.x)












#
