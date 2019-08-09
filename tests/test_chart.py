import sys, io

from chart import RangeScaler, scatter, bar
from chart import bar, scatter

def test_range_scaler():
    rs = RangeScaler(out_range=(0, 10), floor=0, round=True)
    x = [30, 50, 100, 90, 80, 40]
    rs.fit(x)
    result = rs.transform(x)
    assert result == [3, 5, 10, 9, 8, 4]

def test_scatter():
    # redirect sys.stdout to a buffer
    stdout = sys.stdout
    sys.stdout = io.StringIO()
    # call scatter which will print to console
    scatter(range(0, 20), range(0, 20), width=15)
    # capture that output and restore sys.stdout
    output = sys.stdout.getvalue()
    sys.stdout = stdout
    assert output == '             ••\n         ••••  \n      •••      \n  ••••         \n••             \n\n'

def test_bar():
    stdout = sys.stdout
    sys.stdout = io.StringIO()
    bar([300, 400, 200, 80, 500], ['A', 'B', 'C', 'D', 'E'])
    output = sys.stdout.getvalue()
    sys.stdout = stdout
    assert output == 'A: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇            \nB: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇      \nC: ▇▇▇▇▇▇▇▇▇▇▇▇                  \nD: ▇▇▇▇▇                         \nE: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n\n'
