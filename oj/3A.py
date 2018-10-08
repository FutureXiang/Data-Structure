#coding=utf-8
#!/usr/bin/env python3


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

max_5 = Stack()
top_num = 1

input_ABC = input()
flag = "Yes"
arr = []

for i in range(len(input_ABC)):
    # i+1
    now = input_ABC[i]
    if now=='A':
        arr.append(top_num)
        top_num+=1
    elif now=='B':
        max_5.push_back(top_num)
        top_num+=1
        if(max_5.size()>=6):
            flag = "No"
            break
    elif now=='C':
        if(max_5.empty()):
            flag = "No"
            break
        arr.append(max_5.pop())

print(flag)
if flag =='Yes':
    for x in arr:
        print(x)