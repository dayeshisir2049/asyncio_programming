import numpy as np
import time

data_points = 4e8
rows = 50

columns = int(data_points/rows)

matrix = np.arange(data_points).reshape(rows, columns)

s = time.time()
res = np.mean(matrix, axis=1)
e = time.time()

print(f'finished in {e-s:.4f} second(s)')
