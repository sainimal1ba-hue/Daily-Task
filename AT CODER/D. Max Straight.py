from collections import defaultdict

n = int(input())
nums = list(map(int, input().split()))

map = defaultdict(int)

for x in nums:
    map[x] = map.get(x - 1, 0) + 1

res = 0
for val in map.values():
    res = max(res, val)

print(res)
