from preprocessing import RangeScaler

def create_label(label, label_width):
    '''Add right padding to a text label'''
    label = label[:label_width]
    label = label.rjust(label_width)
    label += ': '
    return label

# label = create_label('Toronto', label_width=10)

def build_row(value, label, width, mark, display_labels):
    '''Build a complete row of data'''
    marks = value * mark
    row = marks.ljust(width)
    if display_labels:
        row = label + row
    return row

# build_row(20, label, mark='🍑', width=20, display_labels=True)
# build_row(20, label, mark='🍑', width=20, display_labels=False)

def bar(values, labels, width=30, label_width=None, mark='▇',
            display_labels=True):
    '''Create a simple bar chart'''
    if not label_width:
        label_width = max([len(l) for l in labels])
    labels = [create_label(l, label_width) for l in labels]
    values = RangeScaler((0, width)).fit_transform(values)
    values = [round(v) for v in values]
    chart = ''
    for value, label in zip(values, labels):
        row = build_row(value, label, width, mark, display_labels)
        chart += row
        chart += '\n'
    print(chart)

if __name__ == '__main__':
    import pandas as pd
    df = pd.DataFrame({
        'x': ['Toronto', 'Hamilton', 'Carlisle', 'Hong Kong'],
        'y': [3_000_000, 300_000, 3_000, 5_000_000]
    })
    bar(df.y, df.x, width=20, label_width=10, mark='🙈')
    bar(df.y, df.x)
    bar(df.y, df.x, display_labels=False, mark='🎑')

# TODO:
# add fractional marks
# add data to chart

# DECIMAL_MARKS = {
#     1: '▏',
#     2: '▏',
#     3: '▎',
#     4: '▍',
#     5: '▌',
#     6: '▋',
#     7: '▊',
#     8: '▉',
#     9: '█'
# }
#
# MARK = '▇'

#
