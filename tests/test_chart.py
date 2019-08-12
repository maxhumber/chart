import sys, io, random

from chart.preprocessing import RangeScaler, NumberBinarizer
from chart import bar, scatter, histogram

def test_range_scaler():
    rs = RangeScaler(out_range=(0, 10), floor=0, round=True)
    x = [30, 50, 100, 90, 80, 40]
    rs.fit(x)
    result = rs.transform(x)
    assert result == [3, 5, 10, 9, 8, 4]

def test_number_binarizer():
    nb = NumberBinarizer(bins=4)
    result = nb.fit_transform(range(10))
    assert result == [0, 0, 0, 1, 1, 2, 2, 3, 3, 3]

def test_bar():
    stdout = sys.stdout
    sys.stdout = io.StringIO()
    bar([300, 400, 200, 80, 500], ['A', 'B', 'C', 'D', 'E'])
    output = sys.stdout.getvalue()
    sys.stdout = stdout
    assert output == 'A: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇            \nB: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇      \nC: ▇▇▇▇▇▇▇▇▇▇▇▇                  \nD: ▇▇▇▇▇                         \nE: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n\n'

def test_histogram():
    random.seed(13)
    x = [random.normalvariate(100, 25) for _ in range(20)]
    stdout = sys.stdout
    sys.stdout = io.StringIO()
    histogram(x)
    output = sys.stdout.getvalue()
    sys.stdout = stdout
    assert output == '  ▇ ▇    \n  ▇ ▇    \n  ▇ ▇    \n  ▇ ▇    \n  ▇ ▇    \n  ▇ ▇    \n▇ ▇ ▇   ▇\n▇ ▇ ▇   ▇\n▇ ▇ ▇   ▇\n▇ ▇ ▇   ▇\n\n'

def test_scatter():
    stdout = sys.stdout
    sys.stdout = io.StringIO()
    scatter(range(0, 20), range(0, 20), width=15)
    output = sys.stdout.getvalue()
    sys.stdout = stdout
    assert output == '             ••\n         ••••  \n      •••      \n  ••••         \n••             \n\n'
