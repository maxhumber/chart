class RangeScaler:
    '''MinMaxScale for a target output range'''
    def __init__(self, out_range=(0, 100), floor=None):
        self.out_range = out_range
        self.floor = floor

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
        return y

    def fit_transform(self, y):
        self.fit(y)
        return self.transform(y)

def scale(x, o=(0, 100), i=(0, 1)):
    return (x - i[0]) / (i[1] - i[0]) * (o[1] - o[0]) + o[0]

if __name__ == '__main__':
    x = [40, 25, 80, 60, 100]
    RangeScaler((0, 100)).fit_transform(x)
    RangeScaler((0, 100), 0).fit_transform(x)
    RangeScaler((0, 50), 0).fit_transform(x)
