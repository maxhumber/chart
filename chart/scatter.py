# HACK: to enable interactive development in Atom/Hydrogen
try:
    from .preprocessing import RangeScaler
except ModuleNotFoundError:
    from chart.preprocessing import RangeScaler

def scatter(x, y, width=40, height=None, mark='•'):
    '''A simple scatter plot that prints to the console

    :param x: list, array or series of numeric values
    :param y: list, array or series of numeric values
    :param width: integer for the character length of the x values
    :param height: integer for the character length of the y values
    :param mark: unicode symbol to mark data values

    >>> from chart import scatter
    >>> x = range(0, 20)
    >>> y = range(0, 20)
    >>> scatter(x, y)
                                           •
                                       • •
                                     •
                                 • •
                             • •
                           •
                      •  •
                    •
                • •
            • •
          •
      • •
    •

    >>> import numpy as np
    >>> np.random.seed(1)
    >>> N = 100
    >>> x = np.random.normal(100, 50, size=N)
    >>> y = x * -2 + 25 + np.random.normal(0, 25, size=N)
    >>> scatter(x, y, width=20, height=9, mark='^')

    ^^
     ^
        ^^^
        ^^^^^^^
           ^^^^^^
            ^^^^^^^
                ^^^^
                 ^^^^^ ^
                    ^^ ^
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
