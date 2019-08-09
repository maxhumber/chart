import random

import chart
from chart import RangeScaler

random.seed(1993)
x = [random.gauss(10, 5) for _ in range(50)]
y = [xi * 2 + 5 for xi in x]

chart.scatter(x, y, width=25)
chart.scatter(x, y, width=25, mark='🍑')

labels = ['Toronto', 'Hamilton', 'Carlisle', 'Hong Kong']
values = [3_000_000, 300_000, 3_000, 5_000_000]

chart.bar(values, labels)
chart.bar(values, labels, width=10, label_width=3, mark='🍑')
