# -*- coding: utf-8 -*-
"""
Implementation of the Probabilistic Counting Algorithm

@author: Haoran Ding, Petra Kubernatova
"""

import numpy as np
import random
import matplotlib.pyplot as plt
random.seed(17)


def trailing_zeroes(num):
  """Counts the number of trailing 0 bits in num."""
  if num == 0:
    return 32 # Assumes 32 bit integer inputs!
  p = 0
  while (num >> p) & 1 == 0:
    p += 1
  return p
  
def first_zero(array):
    for i in range (len(array)):
        if array[i] == 0:
            return i
            
def pro_counting(values, m):
    counts = [0]*m
    bitmap = np.zeros((m,32))
    for value in values:
        k = hash(value)
        num = random.randint(0,m-1)
        bitmap[num][trailing_zeroes(k)] = 1
    for j in range (0,m):
        counts[j] = first_zero(bitmap[j])
    #print counts
    return 2 ** (np.mean(counts)) * (m / 0.77351)  # 2^x * number of buckets where x is the mean of all buckets

errors = [0]*120
m = [0]*120

for i in range(len(errors)):
    m[i] = 100+5*i
    avg_error = [0]*5
    for r in range (len(avg_error)):
        avg_error[r] = np.abs(500000 - pro_counting([random.random() for j in range(500000)], m[i]))/(500000)
    errors[i] = np.mean(avg_error)
print errors

plt.plot(m,errors)
plt.ylabel('Error rate')
plt.xlabel('m')
plt.show()
#print [100000/pro_counting([random.random() for i in range(100000)], 100) for j in range (10) ]
      
        
        