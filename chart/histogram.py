# HACK: to enable interactive development in Atom/Hydrogen
try:
    from .preprocessing import NumberBinarizer, RangeScaler
except ModuleNotFoundError:
    from chart.preprocessing import NumberBinarizer, RangeScaler

### just looking

import random
import matplotlib.pyplot as plt
%matplotlib inline

random.seed(13)
x = [random.normalvariate(100, 25) for _ in range(20)]

plt.hist(x, bins=5);

#####

bins = 5
height = 10

binned_x = NumberBinarizer(bins).fit_transform(x)

counter = {x: 0 for x in range(bins)}
for x in binned_x:
    counter[x] += 1

x, y = list(counter.keys()), list(counter.values())

y = RangeScaler((0, height), floor=0).fit_transform(y)
# y = RangeScaler((0, height-1), floor=0).fit_transform(y)

list(zip(x, y))

width = bins
matrix = [[' '] * width for _ in range(height)]

mark = '▇'

for xi, yi in zip(x, y):
    if yi == 0:
        continue
    for yii in range(yi):
        matrix[yii][xi] = mark

matrix = matrix[::-1]

string_chart = ''
for row in matrix:
    string_row = ' '.join(row)
    string_chart += string_row
    string_chart += '\n'

print(string_chart)
