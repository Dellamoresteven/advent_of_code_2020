import numpy as np

lines = open("input.txt").read().split("\n")

slope = ((1,1), (3,1), (5,1), (7,1), (1,2))

x, y, t  = 0, 0, 0

while y < (len(lines) - slope[1][1]):
    if lines[y][x] == "#": t += 1
    y += slope[1][1]
    x = (x+slope[1][0]) % len(lines[0])

print("Part 1: ", t)

prod = 1
for s in slope:
    x, y, t  = 0, 0, 0
    while y < (len(lines) - s[1]):
        y += s[1]
        x = (x+s[0]) % len(lines[0])
        if lines[y][x] == "#": t += 1
    prod *= t

print("Part 2: ", prod)
