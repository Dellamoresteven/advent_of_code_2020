groups = open("ex1.txt").read().split("\n\n")
groups = open("index.txt").read().split("\n\n")

group = []
for x in groups:
    ans = ""
    persons = x.split("\n")
    for a in persons:
        for l in a:
            if l not in ans: ans += l
    group.append(ans)

print("part 1:", sum(len(x) for x in group))

part2 = 0
for x in groups:
    num_people = x.count("\n") + 1
    for x in x.split("\n")[0]:
        if persons.count(x) == num_people:
            part2 += 1

print("part 2:", part2)
