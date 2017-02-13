"""
Implementation of the LogLog Counting Algorithm

@author: Haoran Ding, Petra Kubernatova
"""


import numpy as np
import random
import matplotlib.pyplot as plt

def trailing_zeroes(num):
  """Counts the number of trailing 0 bits in num."""
  if num == 0:
    return 32 # Assumes 32 bit integer inputs!
  p = 0
  while (num >> p) & 1 == 0:
    p += 1
  return p


def estimate_cardinality(values, k):
  """Estimates the number of unique elements in the input set values.

  Arguments:
    values: An iterator of hashable elements to estimate the cardinality of.
    k: The number of bits of hash to use as a bucket number; there will be 2**k buckets.
  """
  num_buckets = 2 ** k # number of buckets
  max_zeroes = [0] * num_buckets # make an array of the size of the number of buckets
  for value in values:
    h = hash(value)
    bucket = h & (num_buckets - 1) # Mask out the k least significant bits as bucket ID
    bucket_hash = h >> k
    max_zeroes[bucket] = max(max_zeroes[bucket], trailing_zeroes(bucket_hash))
  return 2 ** (float(sum(max_zeroes)) / num_buckets) * num_buckets * 0.79402  # 2^x * number of buckets where x is the mean of all buckets

errors = [0]*15
m = [0]*15

for i in range(len(errors)):
    m[i] = 3+i
    avg_error = [0]*20
    for r in range (len(avg_error)):
        avg_error[r] = np.abs(100000 - estimate_cardinality([random.random() for j in range(100000)], m[i]))/(100000)
    errors[i] = np.mean(avg_error)
print errors

plt.plot(m,errors)
plt.ylabel('Error rate')
plt.xlabel('m')
plt.show()

##print [estimate_cardinality([random.random() for i in range(100000)], 10) for j in range(10)]

