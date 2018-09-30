#coding=utf-8
#!/usr/bin/env python3

name = input()
names=name.split()
for i in range(len(names)):
    names[i]=names[i].capitalize()

if len(names)<=2:
    print(' '.join(names))
else:
    output=''
    for i in range(len(names)):
        now=names[i]
        if i==0:
            output+=(now+' ')
        elif i==len(names)-1:
            output+=now
        else:
            output+=now[0]+'. '
    print(output)