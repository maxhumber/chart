def scale(x, xin=(0, 1), xout=(0, 100)):
    return (x - xin[0]) / (xin[1] - xin[0]) * (xout[1] - xout[0]) + xout[0]

class RangeScaler:
    '''MinMaxScale for a target output range'''
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
