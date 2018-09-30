#coding=utf-8
#!/usr/bin/env python3

inp = []
while True:
    a = input()
    if a=='':
        break
    inp.append(int(a))

n=len(inp)+1

print(max(inp))
print(min(inp))
print(inp[int(n/2)-1])

b = sorted(inp)
b.reverse()

for i in range(len(b)):
    b[i]=str(b[i])
out = ' '.join(b)
print(out)