# HACK: to enable interactive development in Atom/Hydrogen
try:
    from .preprocessing import RangeScaler, Binarizer
except ModuleNotFoundError:
    from chart.preprocessing import RangeScaler, Binarizer

import random
import matplotlib.pyplot as plt
%matplotlib inline

random.seed(10)
x = [random.normalvariate(100, 25) for _ in range(20)]

plt.hist(x, bins=5);

#####




binned_x = Binarizer().fit_transform(x)


x[4]
x

bin_number = int(nbins * ((xi - min_) / (max_ - min_)))








from decimal import Decimal

precision = 3

x = [Decimal(xi).quantize(Decimal(f'1.{"0"*precision}')) for xi in x]

min_ = min(x)
max_ = max(x)

bins = 5

width = (max_ - min_) / bins

[(i * width, i * width + width) for i in range(1, bins+1)]
x[4]

max_

x[4] / width

binned_x = [int(xi / width // 1) for xi in x]






x = [round(xi, precision) for xi in x]



min_ = min(x)
max_ = max(x)

width = (max_ - min_) / bins
[(i * width, i * width + width) for i in range(1, bins+1)]

binned_x = [int(xi / width // 1) for xi in x]
binned_x.index(6)
x[4]


from collections import Counter
cx = Counter(binned_x)
values = list(cx.values())
keys = list(cx.keys())

RangeScaler((0, 20), floor=0).fit_transform(values)



import pandas as pd
import numpy as np

pd.cut(x, bins=5)




#
