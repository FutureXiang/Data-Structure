#coding=utf-8
#!/usr/bin/env python3



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
    def print_mid(self):
        if(self.left!=None):
            self.left.print_mid()
        if(self.val!=None):
            print(self.val)
        if(self.right!=None):
            self.right.print_mid()
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
    def print(self):
        self.root.print_mid()



inp = input().split()
Tree = BinTree()
MAX_DEPTH = 1

def dfs(node, DepNow):
    global MAX_DEPTH
    if(node!=None):
        MAX_DEPTH = max(MAX_DEPTH, DepNow)
    if(node.left!=None):
        dfs(node.left, DepNow+1)
    if(node.right!=None):
        dfs(node.right, DepNow+1)

def main():
    son_pointer = 1
    ### Store VALUE

    for i in range(len(inp)):
        if(i==0):
            Tree.set_root(int(inp[i]))
        if(inp[i]=="None"):
            continue
        f = i
        s1 = (son_pointer if son_pointer<len(inp) else None)
        s2 = (son_pointer+1 if son_pointer+1<len(inp) else None)
        son_pointer+=2
        #print(f, s1, s2)
        if(s1!=None and inp[s1]!="None"):
            Tree.insert_left(int(inp[f]),int(inp[s1]))
        if(s2!=None and inp[s2]!="None"):
            Tree.insert_right(int(inp[f]),int(inp[s2]))

    dfs(Tree.root, 1)
    print(MAX_DEPTH)

if __name__=='__main__':
    main()
