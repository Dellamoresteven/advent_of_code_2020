import numpy as np
import re

lines = open("input.txt").read().split("\n")
# lines = open("ex1.txt").read().split("\n\n")
lines = [x.replace("\n", "") for x in lines]

seatsID = []

for x in lines:
    r = np.arange(0, 128)
    c = np.arange(0, 8)
    for l in x:
        if l == "F":
            r = r[0:len(r)//2]
        elif l == "B":
            r = r[len(r)//2:]
        elif l == "R":
            c = c[len(c)//2:]
        elif l == "L":
            c = c[0:len(c)//2]
        # print(l, r, c)
    assert len(r) == len(c) == 1
    # print(r[0] * 8 + c[0])
    seatsID.append(r[0] * 8 + c[0])

print("part 1:", max(seatsID))

seatsID = np.sort(seatsID)

for i, s in enumerate(seatsID):
    if i == 0: continue
    if seatsID[i - 1] != s - 1:
        print("part 2:", s)



