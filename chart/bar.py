# HACK: to enable interactive development in Atom/Hydrogen
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
    >>> x = [500, 200, 900, 400]
    >>> y = ['marc', 'mummify', 'chart', 'sausagelink']
    >>> bar(x, y)
           marc: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
        mummify: ▇▇▇▇▇▇▇
          chart: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
    sausagelink: ▇▇▇▇▇▇▇▇▇▇▇▇▇

    >>> import pandas as pd
    >>> df = pd.DataFrame({
        'artist': ['Tame Impala', 'Childish Gambino', 'The Knocks'],
        'listens': [8_456_831, 18_185_245, 2_556_448]
    })
    >>> bar(df.listens, df.artist, width=20, label_width=11, mark='🔊')
    Tame Impala: 🔊🔊🔊🔊🔊🔊🔊🔊🔊
    Childish Ga: 🔊🔊🔊🔊🔊🔊🔊🔊🔊🔊🔊🔊🔊🔊🔊🔊🔊🔊🔊🔊
     The Knocks: 🔊🔊🔊                 
    '''
    if not label_width:
        label_width = max([len(l) for l in y])
    labels = [create_label(l, label_width) for l in y]
    values = RangeScaler((0, width), 0).fit_transform(x)
    string_chart = ''
    for value, label in zip(values, labels):
        string_row = build_row(value, label, width, mark)
        string_chart += string_row
        string_chart += '\n'
    print(string_chart)
