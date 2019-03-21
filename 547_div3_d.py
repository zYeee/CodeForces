#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

n = int(input())
str1 = input()
str2 = input()

len1_ = len(str1)
len2_ = len(str2)

dict1 = {}
dict2 = {}

for i in range(len1_):
    mapp = dict1.get(str1[i], [])
    mapp.append(i)
    dict1[str1[i]] = mapp

    mapp = dict2.get(str2[i], [])
    mapp.append(i)
    dict2[str2[i]] = mapp

letters = [chr(i) for i in range(97, 123)]

res = []
for i in letters:
    if i in dict1 and i in dict2:
        l1 = dict1[i]
        l2 = dict2[i]
        while l1 and l2:
            res.append([l1.pop() + 1, l2.pop() + 1])

if "?" in dict1:
    l1 = dict1["?"]
else:
    l1 = []
if "?" in dict2:
    l2 = dict2["?"]
else:
    l2 = []

for i in letters:
    if i in dict1:
        ss = dict1[i]
        while ss and l2:
            res.append([ss.pop() + 1, l2.pop() + 1])

for i in letters:
    if i in dict2:
        ss = dict2[i]
        while l1 and ss:
            res.append([l1.pop() + 1, ss.pop() + 1])

while l1 and l2:
    res.append([l1.pop() + 1, l2.pop() + 1])

print(len(res))
for i in res:
    out = list(map(str, i))
    print(' '.join(out))
