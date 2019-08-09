from chart import RangeScaler

def test_range_scaler():
    rs = RangeScaler(out_range=(0, 10), floor=0, round=True)
    x = [30, 50, 100, 90, 80, 40]
    rs.fit(x)
    result = rs.transform(x)
    assert result == [3, 5, 10, 9, 8, 4]

# import random
#
# import chart
# from chart import RangeScaler
#
# random.seed(1993)
# x = [random.gauss(10, 5) for _ in range(50)]
# y = [xi * 2 + 5 for xi in x]
#
# chart.scatter(x, y, width=25)
# chart.scatter(x, y, width=25, mark='🍑')
#
# labels = ['Toronto', 'Hamilton', 'Carlisle', 'Hong Kong']
# values = [3_000_000, 300_000, 3_000, 5_000_000]
#
# chart.bar(values, labels)
# chart.bar(values, labels, width=10, label_width=3, mark='🍑')
#
# x = [40, 25, 80, 60, 100]
# RangeScaler((0, 100)).fit_transform(x)
# RangeScaler((0, 100), 0).fit_transform(x)
# RangeScaler((0, 50), 0).fit_transform(x)
