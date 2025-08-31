import numpy as np
from im2col import im2col 

x = np.random.rand(10, 1, 28, 28)
print(x.shape)
print(x[0].shape)
print(x[1].shape)
print(x[0, 0].shape)

print("####### im2col #######")

x1 = np.random.rand(1, 3, 7, 7)
col1 = im2col(x1, 5, 5, stride=1, pad=0)
print(col1.shape)

x2 = np.random.rand(10, 3, 7, 7)
col2 = im2col(x2, 5, 5, stride=1, pad=0)
print(col2.shape)
