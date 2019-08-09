class RangeScaler:
    '''A scaler to coerce values to a target output range

    >>> rs = RangeScaler(out_range=(0, 50), floor=0, round=False)
    >>> rs.fit(x)
    >>> rs.transform([18, 24, 75])
    [7.5, 10.0, 31.25]
    '''
    def __init__(self, out_range=(0, 100), floor=None, round=True):
        self.out_range = out_range
        self.floor = floor
        self.round = round

    def fit(self, y):
        if not self.floor and self.floor != 0:
            min_ = min(y)
        else:
            min_ = self.floor
        max_ = max(y)
        self.in_range_ = (min_, max_)
        return self

    def transform(self, y):
        y = [scale(yi, self.out_range, self.in_range_) for yi in y]
        if self.round:
            y = [int(round(yi)) for yi in y]
        return y

    def fit_transform(self, y):
        self.fit(y)
        return self.transform(y)

def scale(x, o=(0, 100), i=(0, 1)):
    return (x - i[0]) / (i[1] - i[0]) * (o[1] - o[0]) + o[0]

class Binarizer:
    def __init__(self, bins=5):
        self.bins = bins

    def fit(self, y):
        self.min_ = min(y)
        self.max_ = max(y)
        return self

    def transform(self, y):
        y = [bin(yi, self.bins, self.min_, self.max_) for yi in y]
        y = [yi - 1 if yi == self.bins else yi for yi in y]
        return y

    def fit_transform(self, y):
        self.fit(y)
        return self.transform(y)

def bin(x, bins, min_, max_):
    return int(bins * ((x - min_) / (max_ - min_)))
