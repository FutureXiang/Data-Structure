#coding=utf-8
#!/usr/bin/env python3

class Stack:
    def __init__(self):
        self.clear()
    def clear(self):
        self.arr = []
        self.size = 0 
    def empty(self):
        return self.size==0
    def push(self, x):
        self.arr.append(x)
        self.size+=1
    def pop(self):
        assert not self.empty()
        self.size-=1
        return self.arr.pop()
    def top(self):
        assert not self.empty()
        return self.arr[-1]

def main():
    my_stack = Stack()
    in_n_base = input()
    n = int(in_n_base.split()[0])
    base = int(in_n_base.split()[1])
    while(n>0):
        now = n%base
        my_stack.push(now)
        n = n//base
    res = ""
    mapping = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    while(not my_stack.empty()):
        now = my_stack.pop()
        res = res + mapping[now]
    print(res)


if __name__=='__main__':
    main()
