#coding=utf-8
#!/usr/bin/env python3

n=int(input())
k=int(input())
in_x=[]
cnt={}
for i in range(n):
    in_x.append(int(input()))
    cnt[in_x[i]]=0

for i in range(n):
    if cnt[in_x[i]]==k:
        continue
    else:
        print(in_x[i])
        cnt[in_x[i]]+=1