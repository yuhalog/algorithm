# 18870 : μ’ν μμΆ

import sys
n = int(sys.stdin.readline().rstrip())
num = list(map(int, sys.stdin.readline().split()))
set_num = sorted(set(num))

dic = {set_num[i]:i for i in range(len(set_num))}

for i in num:
    sys.stdout.write(str(dic[i])+' ')