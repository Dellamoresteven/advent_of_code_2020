import numpy as np
import math
from itertools import permutations, combinations

# file = "ex.txt"
file = "real.txt"
ns = open(file).read().split("\n")[:-1]
nums = [int(x) for x in ns]

for x in combinations(nums, 2):
    if sum(x) == 2020:
        print(x, x[0]*x[1])
        exit(0)
