#coding=utf-8
#!/usr/bin/env python3

cnt=[0,0]
while(True):
    now = int(input())
    if now==-1:
        break
    cnt[now]+=1

if cnt[1]*2>=sum(cnt):
    print("Yes")
else:
    print("No")