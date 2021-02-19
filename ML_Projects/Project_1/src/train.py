from pathlib import Path

import pandas as pd

path = Path('./ML_Projects/Project_1/input/mnist_test.csv')
df = pd.read_csv(path)
print(df.shape)
