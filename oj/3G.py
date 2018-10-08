#coding=utf-8
#!/usr/bin/env python3

n = int(input())
cnt = {}
maxx = -1
for i in range(n):
    inp = input()
    inp = inp.lower()
    strs = inp.split()
    for str_ in strs:
        if str_ not in cnt:
            cnt.update({str_:1})
        else:
            cnt[str_]+=1

maxx = max(cnt.values())
print(maxx)
for x in cnt.keys():
    if cnt[x]==maxx:
        print(x)