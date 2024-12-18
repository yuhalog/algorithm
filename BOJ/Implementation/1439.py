# 1439 : 뒤집기

import sys

s = str(sys.stdin.readline())

zero_count = 0
one_count = 0

for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        if s[i] == "1":
            one_count += 1
        if s[i] == "0":
            zero_count += 1

if s[-2] != s[-1]:
    if s[-1] == "1":
        one_count += 1
    if s[-1] == "0":
        zero_count += 1

n = min(zero_count, one_count)
print(n)
