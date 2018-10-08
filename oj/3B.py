#coding=utf-8
#!/usr/bin/env python3

def intput():
    return int(input())

class Stack:
    def __init__(self):
        self.ele=[]
    def empty(self):
        return self.ele==[]
    def size(self):
        return len(self.ele)
    def push_back(self, x):
        self.ele.append(x)
    def pop(self):
        assert not self.empty()
        return self.ele.pop()
    def top(self):
        assert not self.empty()
        return self.ele[-1]

n = intput()

max_n = Stack()

while(True):
    now = intput()
    if(now==0):
        break
    if(max_n.empty()):
        max_n.push_back(now)
    else:
        if(now<=max_n.top()):
            if(max_n.size() < n):
                max_n.push_back(now)
        else:
            max_n.pop()
            max_n.push_back(now)
print(sum(max_n.ele))