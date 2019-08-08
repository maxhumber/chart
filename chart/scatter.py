
# ANSI escape SGR Parameters color codes
AVAILABLE_COLORS = {
    'red': 91,
    'blue': 94,
    'green': 92,
    'magenta': 95,
    'yellow': 93,
    'black': 90,
    'cyan': 96
}


color = AVAILABLE_COLORS['cyan']

r = 15
c = r * 3

matrix = [[' '] * c for _ in range(r)]
chart = ''
for row in matrix:
    row_string = ''.join(row)
    chart += row_string
    chart += '\n'

def matrix_to_string(matrix):
    chart = ''
    for row in matrix:
        row_string = ''.join(row)
        chart += row_string
        chart += '\n'
    return chart

sys.stdout.write(f'\033[{color}m') # Start to write colorized.
sys.stdout.write(chart)
sys.stdout.write('\033[0m') # Back to original.

def random_tick():
    return random.choices([' ', '⋄'], weights=[0.5, 0.5])[0]

from itertools import product

list(product([1,2,3], [1, 2,3]))

matrix = [[' '] * c for _ in range(r)]
for (x, y) in product(range(r), range(c)):
    tick = random_tick()
    print(tick)
    matrix[x][y] = tick

chart = matrix_to_string(matrix)

sys.stdout.write(f'\033[{color}m') # Start to write colorized.
sys.stdout.write(chart)
sys.stdout.write('\033[0m') # Back to original.

size = 100
x = np.random.normal(1000, 500, size)
y = x * 3 + 200 + np.random.normal(0, 700, size)

from matplotlib import pyplot as plt
%matplotlib inline

plt.scatter(x, y)

df = pd.DataFrame({'x': x, 'y': y})
df
