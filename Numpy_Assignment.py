import numpy as np

# 1.
vector1 = np.arange(1,11,1)
print("\n Vector \n",vector1)

# 2.

A=np.zeros((10,10))
for i in range(10):
    for j in range(10):
        A[i][j]=A[i][j]+i+j
print(A+2)

# 3

import numpy.random as npr
data1 = np.exp(npr.randn(50, 5))
print("\n 50 x 5 Random Numbers \n",data1)

mean=np.mean(data1,axis=0)
std=np.std(data1,axis=0)
print ('\n Mean - Column wise \n',mean)

# 4.

mean=np.mean(data1,axis=0)
std=np.std(data1,axis=0)
print ('\n Mean - Column wise \n',mean)
print ('\n Standard Deviation - Column wise \n',std)

# 5.

mean_sub=data1-mean

print('\n Matrix After Subtracting Mean Off of Each Coulmn \n',mean_sub)
normalized=mean_sub / std

print('\n Matrix After Dividing STD Off of Each Coulmn \n',normalized)
normalized_mean=np.mean(normalized,axis=0)
normalized_std=np.std(normalized,axis=0)

print('\n Mean After Normalization \n',normalized_mean)
print('\n STD After Normalization \n',normalized_std)