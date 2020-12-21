import numpy as np
import math
from itertools import permutations, combinations

file = "ex1.txt"
file = "real1.txt"
lines = open(file).read().split("\n")[:-1]

rules, passwords = zip(*(s.split(": ") for s in lines))
assert len(rules) == len(passwords)

valid = 0
for i, (r, p) in enumerate(zip(rules, passwords)):
    l, m, letter = int(r[0:r.find("-")]), int(r[r.find("-")+1:r.find(" ")]), r[r.find(" ")+1:]
    if p.count(letter) >= l and p.count(letter) <= m:
        valid += 1

print(valid)
