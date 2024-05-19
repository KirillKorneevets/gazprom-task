import numpy as np


a = [[1, 2, 3], [4, 5, 6]]

b = [{'k1': x[0], 'k2': x[1], 'k3': x[2]} for x in np.array(a)]

print(b)
