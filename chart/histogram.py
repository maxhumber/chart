# HACK: to enable interactive development in Atom/Hydrogen
try:
    from .preprocessing import NumberBinarizer, RangeScaler
except ModuleNotFoundError:
    from chart.preprocessing import NumberBinarizer, RangeScaler

import random
import matplotlib.pyplot as plt
%matplotlib inline

random.seed(10)
x = [random.normalvariate(100, 25) for _ in range(20)]

plt.hist(x, bins=5);

#####

binned_x = NumberBinarizer().fit_transform(x)

from collections import Counter
cx = Counter(binned_x)
values = list(cx.values())
keys = list(cx.keys())

values = RangeScaler((0, 10), floor=0).fit_transform(values)

width = len(keys)
height = max(values)

matrix = [[' '] * width for _ in range(height)]

mark = '▇'

for key, value in zip(keys, values):
    matrix[value][key] = mark

matrix




#
