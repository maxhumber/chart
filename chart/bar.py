# HACK: handle interactive development in Atom/Hydrogen
# NOTE: activate at the root of the package directory
try:
    from .preprocessing import RangeScaler
except ModuleNotFoundError:
    from chart.preprocessing import RangeScaler

def create_label(label, label_width):
    '''Add right padding to a text label'''
    label = label[:label_width]
    label = label.rjust(label_width)
    label += ': '
    return label

def build_row(value, label, width, mark):
    '''Build a complete row of data'''
    marks = value * mark
    row = marks.ljust(width)
    row = label + row
    return row

def bar(x, y, width=30, label_width=None, mark='▇'):
    '''A simple bar chart that prints to the console

    :param x: list, array or series of numeric values
    :param y: list, array or series of labels for the numeric values
    :param width: integer for the character length of the x values
    :param label_width: integer for the label character length
    :param mark: unicode symbol to mark data values

    >>> from chart import bar
    >>> bar(x = [100, 80, 20, 60], ['A', 'B', 'C', 'D'])
    '''
    if not label_width:
        label_width = max([len(l) for l in y])
    labels = [create_label(l, label_width) for l in y]
    values = RangeScaler((0, width)).fit_transform(x)
    values = [round(v) for v in values]
    chart = ''
    for value, label in zip(values, labels):
        row = build_row(value, label, width, mark)
        chart += row
        chart += '\n'
    print(chart)
