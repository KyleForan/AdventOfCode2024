import re

data = open("Day03/input").read()
sums = re.findall(r'mul\((\d+),(\d+)\)', data)

total = 0

for x, y in sums:

    total += int(x) * int(y)

print(total)