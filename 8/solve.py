import numpy as np

lines = open("input.txt").read().split("\n")

def get_acc(l, rec = False):
    times = np.zeros(len(l) + 1)
    acc = 0
    i = 0
    while times[i] < 1 and i <= len(l) - 1:
        x = l[i]
        if x[0:3] == "acc":
            acc += int(x[4:])
        elif x[0:3] == "jmp":
            lines_copy = lines.copy()
            lines_copy[i] = "nop " + x[4:]
            if rec == False:
                index, accc = get_acc(lines_copy, True)
                if index == len(l):
                    return i, accc
            i += (int(x[4:]) - 1)
        times[i] += 1
        i += 1

    return i, acc

print("part1:", get_acc(lines, True)[1])
print("part2:", get_acc(lines, False)[1])
