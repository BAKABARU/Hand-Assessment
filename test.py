import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import turtle

df = pd.read_csv("AnkleNormal.csv") # loads data
print(df.head()) # makes sure data is loaded properly

x = [0] * (len(df) + 1)
y = [0] * (len(df) + 1)

# for i in range(0, 700):
#     x[i + 1] = x[i] + df['velocity_x'][i]
#     y[i + 1] = y[i] - df['velocity_y'][i]

plt.scatter(x, y, s=3)
# plt.gcf().set_size_inches(20, 1)
plt.show()