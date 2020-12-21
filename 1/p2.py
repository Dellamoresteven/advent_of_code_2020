import numpy as np
import math
from itertools import permutations, combinations

# file = "ex.txt"
file = "real2.txt"
ns = open(file).read().split("\n")[:-1]
nums = [int(x) for x in ns]

for x in combinations(nums, 3):
    if sum(x) == 2020:
        print(x, x[0]*x[1]*x[2])
        exit(0)

