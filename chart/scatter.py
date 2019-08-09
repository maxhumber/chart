# HACK: to enable interactive development in Atom/Hydrogen
try:
    from .preprocessing import RangeScaler
except ModuleNotFoundError:
    from chart.preprocessing import RangeScaler

def scale_values(values, scale):
    '''Reusable (x, y) RangeScaler with rounding'''
    values = RangeScaler((0, scale-1)).fit_transform(values)
    values = [int(round(v)) for v in values]
    return values

def matrix_to_string(matrix):
    string = ''
    for row in matrix:
        row_string = ''.join(row)
        string += row_string
        string += '\n'
    return string

def scatter(x, y, width=40, height=None, mark='•'):
    '''A simple scatter plot that prints to the console
    >>> scatter(range(0, 20), range(0, 20))
    '''
    if not height:
        height = int(width / 3 // 1)
    matrix = [[' '] * width for _ in range(height)]
    x = scale_values(x, width)
    y = scale_values(y, height)
    for (xi, yi) in zip(x, y):
        matrix[yi][xi] = mark
    matrix = matrix[::-1]
    chart = matrix_to_string(matrix)
    print(chart)
