import sys
import random
import numpy as np
import pandas as pd

DECIMAL_TICKS = {
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

def create_label(label, label_width):
    label = label[:label_width]
    label = label.rjust(label_width)
    label += ': '
    return label

def build_row(data, label, tick, width):
    row = data * tick
    row = row.ljust(width)
    row = label + row
    return row

####

df = pd.DataFrame({
    'x': ['Toronto', 'Hamilton', 'Carlisle', 'Hong Kong'],
    'y': [3_000_000, 300_000, 3_000, 5_000_000]
})

def bar(data, labels, width=30, label_width=None, tick='▇'):
    if not label_width:
        label_width = max([len(l) for l in labels])
    labels = [create_label(l, label_width) for l in labels]
    data = RangeScaler((0, width)).fit_transform(data)
    data = [round(di) for di in data]
    chart = ''
    for d, l in zip(data, labels):
        row = build_row(d, l, tick, width)
        chart += row
        chart += '\n'
    print(chart)

bar(df.y, df.x, width=20, label_width=10, tick='🙈')
bar(df.y, df.x)

# TODO:
# add fractional ticks
# add/remove optional labels
# add data to chart
# posibility to send to std out?



#
