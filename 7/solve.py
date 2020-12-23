# lines = open("ex1.txt").read().split("\n")
# lines = open("ex2.txt").read().split("\n")
lines = open("index.txt").read().split("\n")

dic = {k.split(" contain ")[0]: k.split("bags contain ")[1].split(",") for k in lines}

def rec_part1(bags):
    if bags[0] == "no other bags.":
        return False
    for b in bags:
        b = b.strip()
        b = b[2:]
        b = b[:-1] if b[-1] == "." else b
        if "shiny gold bag" in b:
            return True
        ret = rec_part1(dic[b]) if b[-1] == "s" else rec_part1(dic[b+"s"])
        if ret == True:
            return True
    return False

def rec_part2(bags):
    r = 0
    ret = 0
    if bags[0] == "no other bags.":
        return 1
    for b in bags:
        b = b.strip()
        n = int(b[0:1])
        b = b[2:]
        b = b[:-1] if b[-1] == "." else b
        ret = rec_part2(dic[b]) if b[-1] == "s" else rec_part2(dic[b+"s"])
        r += ret*n
    return r+1

part1 = 0
for d in dic:
    if(rec_part1(dic[d]) == True):
        part1 += 1

print("part1:", part1)
print("part2:", rec_part2(dic["shiny gold bags"]) - 1 )

