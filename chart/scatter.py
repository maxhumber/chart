# HACK: to enable interactive development in Atom/Hydrogen
try:
    from .preprocessing import RangeScaler
except ModuleNotFoundError:
    from chart.preprocessing import RangeScaler

def scatter(x, y, width=40, height=None, mark='•'):
    '''A simple scatter plot that prints to the console
    >>> scatter(range(0, 20), range(0, 20))
    '''
    if not height:
        height = int(width / 3 // 1)
    matrix = [[' '] * width for _ in range(height)]
    x = RangeScaler((0, width-1)).fit_transform(x)
    y = RangeScaler((0, height-1)).fit_transform(y)
    for (xi, yi) in zip(x, y):
        matrix[yi][xi] = mark
    matrix = matrix[::-1]
    string_chart = ''
    for row in matrix:
        string_row = ''.join(row)
        string_chart += string_row
        string_chart += '\n'
    print(string_chart)
