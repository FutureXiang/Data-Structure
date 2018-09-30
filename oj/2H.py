#coding=utf-8
#!/usr/bin/env python3

n=int(input())
original=[]
queue=[]
for i in range(n):
    original.append(int(input()))

for i in range(n):
    if len(queue)==0:
        queue.append(i)
    else:
        now=original[i]
        while(len(queue)>=1 and original[queue[-1]]<now):
            queue.pop()
        queue.append(i)

print(len(queue))
for i in queue:
    print(i+1)