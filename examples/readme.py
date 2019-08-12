from chart import bar, histogram, scatter
from chart.preprocessing import NumberBinarizer
from chart.preprocessing import RangeScaler

# Example 1A

from chart import bar

x = [500, 200, 900, 400]
y = ['marc', 'mummify', 'chart', 'sausagelink']

bar(x, y)

# Example 1B

from chart import bar
import pandas as pd

df = pd.DataFrame({
    'artist': ['Tame Impala', 'Childish Gambino', 'The Knocks'],
    'listens': [8_456_831, 18_185_245, 2_556_448]
})

bar(df.listens, df.artist, width=20, label_width=11, mark='🔊')

# Example 2A

from chart import histogram

x = [1, 2, 4, 3, 3, 1, 7, 9, 9, 1, 3, 2, 1, 2]

histogram(x)

# Example 2B

from chart import histogram
import scipy.stats as stats
import numpy as np

np.random.seed(14)
n = stats.norm(loc=0, scale=10)

histogram(n.rvs(100), bins=14, height=7, mark='🍑')

# Example 3A

from chart import scatter

x = range(0, 20)
y = range(0, 20)

scatter(x, y)

# Example 3B

from chart import scatter
import numpy as np

np.random.seed(1)
N = 100
x = np.random.normal(100, 50, size=N)
y = x * -2 + 25 + np.random.normal(0, 25, size=N)

scatter(x, y, width=20, height=9, mark='^')

# Preprocessors

from chart.preprocessing import NumberBinarizer

nb = NumberBinarizer(bins=4)
x = range(10)
nb.fit(x)
nb.transform(x)

from chart.preprocessing import RangeScaler

rs = RangeScaler(out_range=(0, 10), round=False)
x = range(50, 59)
rs.fit_transform(x)
