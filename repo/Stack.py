#coding=utf-8
#!/usr/bin/env python3

def intput():
    return int(input())
def writeline(list):
    for i in range(len(list)):
        list[i]=str(list[i])
    print(" ".join(list))

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
    while(True):
        n = intput()
        if(not n):
            break
        my_stack.push(n)
    
    while(not my_stack.empty()):
        now = my_stack.pop()
        print(now)

if __name__=='__main__':
    main()
