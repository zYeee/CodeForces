#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


import math


def work(n, m):
    len_ = len(m)
    sum_ = sum(m)
    if sum_ >= 0:
        count = 0
        remain = n[0]
        for i in m:
            remain += i
            count += 1
            if remain <= 0:
                return count
        return -1

    maxHurt = 0
    tmp = 0
    for i in m:
        tmp += i
        maxHurt = min(maxHurt, tmp)
    
    maxHurt *= -1
    tmp = n[0] - maxHurt
    if tmp < 0:
        tmp = 0
    count = math.ceil(tmp / -sum_) * len_
    remain = n[0] + count / len_ * sum_
    for i in m:
        remain += i
        count += 1
        if remain <= 0:
            return count
