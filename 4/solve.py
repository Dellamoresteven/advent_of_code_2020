import numpy as np
import re

lines = open("input.txt").read().split("\n\n")
# lines = open("ex1.txt").read().split("\n\n")

lines = [x.replace("\n"," ") for x in lines]

valid = 0
for x in lines:
    if x.count(":") == 8:
        valid += 1
    elif x.count(":") == 7:
        if x.find("cid:") == -1:
            valid += 1

print("Part 1:", valid)

valid = 0

for x in lines:
    dic = {}
    for k in x.split():
        key, value = k.split(":")
        dic[key] = value

    try:
        hgt = False
        if dic["hgt"][-2:] == "cm":
            if 150 <= int(dic["hgt"][0:-2]) <= 193:
                hgt = True
        if dic["hgt"][-2:] == "in":
            if 59 <= int(dic["hgt"][0:-2]) <= 76:
                hgt = True
        hcl = re.fullmatch(r'#[0-9a-f]{6}', dic["hcl"])

        ecl_list = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
        ecl = False
        if dic["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
            ecl = True

        pid = re.fullmatch(r'[0-9]{9}', dic["pid"])

        if 1920 <= int(dic["byr"]) <= 2002 and 2010 <= int(dic["iyr"]) <= 2020 and 2020 <= int(dic["eyr"]) <= 2030 and hgt and hcl and ecl and pid:
            valid += 1
    except Exception:
        print("EERORR")


print(valid)
