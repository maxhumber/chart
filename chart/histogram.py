# HACK: to enable interactive development in Atom/Hydrogen
try:
    from .preprocessing import NumberBinarizer, RangeScaler
except ModuleNotFoundError:
    from chart.preprocessing import NumberBinarizer, RangeScaler

def histogram(x, bins=5, height=10, mark='▇'):
    '''A simple histogram chart that prints to the console

    :param x: list, array or series of numeric values
    :param bins: integer for the number of bins
    :param height: integer for the output height
    :param mark: unicode symbol to mark data values

    >>> from chart import histogram
    >>> x = [1, 2, 4, 3, 3, 1, 7, 9, 9, 1, 3, 2, 1, 2]
    >>> histogram(x)
    ▇
    ▇
    ▇
    ▇
    ▇ ▇
    ▇ ▇
    ▇ ▇
    ▇ ▇     ▇
    ▇ ▇     ▇
    ▇ ▇   ▇ ▇

    >>> import scipy.stats as stats
    >>> import numpy as np
    >>> np.random.seed(14)
    >>> n = stats.norm(loc=0, scale=10)
    >>> histogram(n.rvs(100), bins=14, height=7, mark='🍑')
                🍑
                🍑   🍑
                🍑 🍑 🍑
                🍑 🍑 🍑
            🍑   🍑 🍑 🍑
          🍑 🍑 🍑 🍑 🍑 🍑 🍑 🍑 🍑
          🍑 🍑 🍑 🍑 🍑 🍑 🍑 🍑 🍑   🍑
    '''
    binned_x = NumberBinarizer(bins).fit_transform(x)
    counter = {x: 0 for x in range(bins)}
    for x in binned_x:
        counter[x] += 1
    x, y = list(counter.keys()), list(counter.values())
    y = RangeScaler((0, height), floor=0).fit_transform(y)
    matrix = [[' '] * bins for _ in range(height)]
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
