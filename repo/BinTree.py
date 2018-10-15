#coding=utf-8
#!/usr/bin/env python3

def intput():
    return int(input())
def writeline(list):
    for i in range(len(list)):
        list[i]=str(list[i])
    print(" ".join(list))

class Node:
    # size, val, left, right, father
    def __init__(self):
        self.size = 1
        self.val = None
        self.left, self.right = None, None
        self.father = None
    def set_value(self, value):
        self.val = value
    def set_left(self, root_SubTree):
        root_SubTree.father = self
        self.left = root_SubTree
        self.size = 1 + self.left.size + (0 if self.right==None else self.right.size)
    def set_right(self, root_SubTree):
        root_SubTree.father = self
        self.right = root_SubTree
        self.size = 1 + self.right.size + (0 if self.left==None else self.left.size)

class BinTree:
    def __init__(self):
        self.root = None
    def is_empty(self):
        return self.root==None
    def set_root(self, value):
        self.root = Node()
        self.root.set_value(value)
    def size(self):
        if self.is_empty():
            return 0
        else:
            return self.root.size
    

def main():
    pass


if __name__=='__main__':
    main()
