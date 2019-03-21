#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


n = input()
input_ = input().split()
input_ = list(map(int, input_))


count = 0
max_ = 0
for i in input_:
    if i == 0:
        count = 0
    if i == 1:
        count += 1
        max_ = max(count, max_)

count = 0
for i in input_:
    if i == 1:
        count += 1
    else:
        break
for i in input_[::-1]:
    if i == 1:
        count += 1
    else:
        break

max_ = max(count, max_)


print(max_)

