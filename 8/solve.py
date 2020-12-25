import numpy as np


lines = open("input.txt").read().split("\n")


# Part 1
# times = np.zeros(len(lines))
# acc = 0
# i = 0
# while times[i] < 1 or i >= len(lines):
    # x = lines[i]
    # print(i, x, x[0:3])
    # if x[0:3] == "acc":
        # # print("acc:",int(x[4:]))
        # acc += int(x[4:])
    # elif x[0:3] == "jmp":
        # # print("Jump:",int(x[4:]))
        # i += (int(x[4:]) - 1)
    # times[i] += 1
    # i += 1


def get_acc():
    times = np.zeros(len(lines))
    print(len(times))
    acc = 0
    i = 0
    while i <= len(lines):
        x = lines[i]
        times[i] += 1
        j = i
        if x[0:3] == "acc":
            acc += int(x[4:])
        elif x[0:3] == "jmp":
            i += (int(x[4:]) - 1)
        i += 1
        if times[i] == 10:
            print("MAYBE:", j)


    return i, acc

# print(len(lines))
# j, a = get_acc()
# print(j,a)
# lines[364] = "nop +0"
# j, a = get_acc()
# print(j,a)
lol = '''
1. 1. 1. 1. 0. 0. 8. 8. 0. 0. 8. 8. 8. 8. 8. 0. 0. 0. 0. 8. 8. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 8. 8. 0. 0. 0. 0. 0. 0. 0. 0. 8. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 8. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 8. 8. 8. 0. 0. 8. 8. 8. 8. 0. 8. 8. 8. 8. 8. 0. 0. 0. 8.
 8. 8. 8. 0. 0. 0. 0. 8. 8. 8. 8. 0. 0. 0. 0. 0. 1. 0. 0. 8. 8. 0. 0. 0.
 0. 0. 8. 8. 8. 8. 8. 0. 0. 0. 0. 0. 0. 0. 0. 8. 8. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 8. 8. 8. 8. 8. 0. 0. 0. 0. 8. 8. 8. 8. 0. 0. 0. 0. 0. 0. 8. 8. 8.
 0. 0. 0. 0. 0. 0. 0. 8. 8. 8. 8. 0. 8. 8. 8. 0. 0. 0. 0. 0. 8. 8. 8. 8.
 8. 0. 0. 8. 8. 8. 8. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 8. 8. 8. 0. 0. 0. 0. 0. 8. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 1. 0. 8. 8. 8. 8. 0. 0. 0. 0. 8. 8. 7
'''
lol = lol.replace(" ", "").replace("\n","").replace(".", "")
print(len(lol))
j, a = get_acc()
# print(j,a)
print(lines[254])
