#coding=utf-8
#!/usr/bin/env python3

n = int(input())
s = {}
for i in range(n):
    name=input()
    height=float(input())
    s.update({name:height})
sort_s = sorted(s.items(),key=lambda x: x[1], reverse=True)

for item in sort_s:
    print("{}, {:.2f}".format(item[0], item[1]))