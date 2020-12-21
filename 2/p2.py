import numpy as np

# file = "ex1.txt"
file = "real1.txt"
lines = open(file).read().split("\n")[:-1]

rules, passwords = zip(*(s.split(": ") for s in lines))
assert len(rules) == len(passwords)

valid = 0
for i, (r, p) in enumerate(zip(rules, passwords)):
    l, m, letter = int(r[0:r.find("-")])-1, int(r[r.find("-")+1:r.find(" ")])-1, r[r.find(" ")+1:]
    if (p[l] == letter and p[m] != letter) or (p[l] != letter and p[m] == letter):
        valid += 1

print(valid)

