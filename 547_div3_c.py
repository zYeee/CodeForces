#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


n = int(input())
input_ = input().split()
input_ = list(map(int, input_))

nums = []
sum_ = 0

flag = True
max_ = min_ = 0
for i in input_:
    if sum_ + i < 0:
        min_ = min(min_, sum_ + i)
    elif sum_ + i > 0:
        max_ = max(max_, sum_ + i)
    elif sum_ + i == 0:
        flag = False
        break
    nums.append(sum_ + i)
    sum_ += i

if -min_ > max_:
    start = -min_ + 1
else:
    start = n - max_

res = []
if not start or start <= 0 or start > n:
    flag = False
else:
    vis = [False] * (n + 1)
    vis[start] = True
    res.append(start)
    for i in nums:
        if not vis[start + i] and start + i > 0 and start + i <= n:
            vis[start + i] = True
            res.append(start + i)
        else:
            flag = False
            break


if not flag:
    print(-1)
else:
    res = list(map(str, res))
    print(' '.join(res))
