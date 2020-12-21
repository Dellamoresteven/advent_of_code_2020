import numpy as np

lines = open("input.txt").read().split("\n\n")
# lines = open("ex1.txt").read().split("\n\n")

lines = [x.replace("\n"," ") for x in lines]

valid = 0
for x in lines:
    if x.count(":") == 8:
        print(x)
        valid += 1
    elif x.count(":") == 7:
        if x.find("cid:") == -1:
            print(x)
            valid += 1

print("Part 1:", valid)


for x in lines:
    dic = {}
    for k in x.split():
        key,value = k.split(":")
        dic[key] = value

