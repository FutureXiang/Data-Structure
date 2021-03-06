#coding=utf-8
#!/usr/bin/env python3

def intput():
    return int(input())
def writeline(list):
    for i in range(len(list)):
        list[i]=str(list[i])
    print(" ".join(list))

class Node:
    # val, left, right, father
    def __init__(self, value):
        self.val = value
        self.left, self.right = None, None
        self.father = None
        self.id = None
    def set_value(self, value):
        self.val = value
    def set_left(self, root_SubTree):
        root_SubTree.father = self
        self.left = root_SubTree
    def set_right(self, root_SubTree):
        root_SubTree.father = self
        self.right = root_SubTree
    def print_mid(self):    #left, mid, right
        if(self.left!=None):
            self.left.print_mid()
        if(self.val!=None):
            print(self.val, end = ' ')
        if(self.right!=None):
            self.right.print_mid()
    def print_pre(self):    # mid, left, right
        if(self.val!=None):
            print(self.val, end = ' ')
        if(self.left!=None):
            self.left.print_pre()
        if(self.right!=None):
            self.right.print_pre()
    def print_fol(self):    # left, right, mid
        if(self.left!=None):
            self.left.print_fol()
        if(self.right!=None):
            self.right.print_fol()
        if(self.val!=None):
            print(self.val, end = ' ')
    def find_node(self, val):
        if(self.val==val):
            return self
        l_res = r_res = None
        if(self.left!=None):
            l_res = self.left.find_node(val)
        if(l_res!=None):
            return l_res
        elif(self.right!=None):
            r_res = self.right.find_node(val)
            if(r_res!=None):
                return r_res
        return None

class BinTree:
    def __init__(self):
        self.root = None
        self.nodes = {} # {id: node}
    def is_empty(self):
        return self.root==None
    def set_root(self, value):
        self.root = Node(value)
        self.root.id = 1
        self.nodes.update({1: self.root})

    def find(self, val):
        return self.root.find_node(val)
    def insert_left(self, x, y):
        node_x = self.find(x)
        node_y = Node(y)
        node_y.id = node_x.id*2
        self.nodes.update({node_y.id: node_y})
        node_x.set_left(node_y)
    def insert_right(self, x, y):
        node_x = self.find(x)
        node_y = Node(y)
        node_y.id = node_x.id*2+1
        self.nodes.update({node_y.id: node_y})
        node_x.set_right(node_y)
    def print_mid(self):
        self.root.print_mid()
        print()
    def print_pre(self):
        self.root.print_pre()
        print()
    def print_fol(self):
        self.root.print_fol()
        print()
    

def main():
    root = intput()
    M = intput()

    Tree = BinTree()
    Tree.set_root(root)

    for i in range(M):
        inp = input().split()
        f = int(inp[0])
        s = int(inp[1])
        op = inp[2]
        if(op=='L'):
            Tree.insert_left(f,s)
        else:
            Tree.insert_right(f,s)
        Tree.print_mid()


if __name__=='__main__':
    main()
