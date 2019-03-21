#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

input_ = input().split()
input_ = list(map(int, input_))

n, m = input_[0], input_[1]

if m % n == 0:
    num = m / n
    res = 0
    while num != 1:
        if num % 3 == 0:
            num /= 3
            res += 1
            continue
        if num % 2 == 0:
            num /= 2
            res += 1
            continue
        break
    if num != 1:
        print(-1)
    else:
        print(res)
else:
    print(-1)
