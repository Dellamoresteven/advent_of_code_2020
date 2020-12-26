from itertools import permutations, combinations

numbers = open("input.txt").read().split("\n")
numbers = [int(x) for x in numbers]

preamble = 25
pre = numbers[0:preamble]

def get_sum(target, nums):
    for x in combinations(nums, 2):
        if sum(x) == target:
            return True
    return False

def get_sum2(target, nums):
    for i in range(0,len(nums) + 1):
        s = 0
        for j in range(i, len(nums) + 1):
            s = sum(nums[i:j])
            if s == target:
                return (max(nums[i:j]) + min(nums[i:j]))
            elif s > target:
                break

for i, x in enumerate(numbers, 1):
    if get_sum(numbers[i + preamble - 1], pre) == False:
        print("part1:",numbers[i + preamble - 1])
        print("part2:",get_sum2(numbers[i + preamble - 1], numbers))
        exit(0)
    pre = numbers[i:i + preamble]

