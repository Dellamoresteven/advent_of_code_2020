import numpy as np

lines = open("input.txt").read().split("\n")
lines = [int(x) for x in lines]
lines.extend([0, max(lines)+3])

lines.sort()

ones = [1 if (lines[i] - lines[i-1]) == 1 else 0 for i in range(1, len(lines))]
three = [1 if (lines[i] - lines[i-1]) == 3 else 0 for i in range(1, len(lines))]

print("part1:", sum(ones) * (sum(three)))
