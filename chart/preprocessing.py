class RangeScaler:
    '''A scaler to coerce values to a target output range

    >>> x = [100, 30, 35, 60, 120, 70, 120]
    >>> rs = RangeScaler()
    >>> rs.fit_transform(x)
    [78, 0, 6, 33, 100, 44, 100]

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
