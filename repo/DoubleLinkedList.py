#coding=utf-8
#!/usr/bin/env python3

def intput():
    return int(input())
def writeline(list):
    for i in range(len(list)):
        list[i]=str(list[i])
    print(" ".join(list))

class Node():
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None
    def PrintNode(self):
        print("Value: {}, Prev: {}, Next: {}".format(self.value, self.prev.value, self.next.value))
    def Insert(self, new):
        original_next = self.next
        if original_next==None:
            self.next = new
        else:
            original_next.prev = new
        new.next = original_next
        new.prev = self
        self.next = new

class DoubleLL():
    def __init__(self):
        self.Head = Node()
        # Empty Double Linked List
    def Empty(self):
        return (self.Head.next==None)
    def Print(self):
        if self.Empty():
            print("Empty!")
        else:
            now = self.Head
            print_list = [now.value]
            while(now.next!=None):
                now = now.next
                print_list.append(now.value)
            writeline(print_list)
    def InsertFromHead(self, value):
        self.Head.Insert(Node(value))
    def InsertFromTail(self, value):
        self.GetTail().Insert(Node(value))
    def InsertFromNode(self, search, value, Mode="value"):
        assert (Mode in ["value", "index"])
        if Mode=="value":
            insert_node = self.Find(search)
        elif Mode=="index":
            insert_node = self.GetByIndex(search)
        insert_node.Insert(Node(value))
    def GetTail(self):
        now = self.Head
        while(now.next!=None):
            now = now.next
        return now
    def Find(self, value):
        now = self.Head
        Result_Node = None
        while(now.next!=self.Head):
            now = now.next
            if now.value==value:
                Result_Node = now
                break
        return Result_Node
    def GetByIndex(self, index):
        now = self.Head
        now_index = 0
        while(now_index!=index):
            now = now.next
            now_index+=1
        return now
    def DelNode(self, node):
        assert not self.Empty()
        node.prev.next = node.next
        node.next.prev = node.prev

def main():
    my_doublell = DoubleLL()

    N = intput()
    ## INSERT BY HEAD/TAIL
    for i in range(N):
        now = intput()
        my_doublell.InsertFromTail(now)
        my_doublell.InsertFromHead(now)
        my_doublell.Print()
    ## INSERT BY CERTAIN NODE(VALUE / INDEX)
    my_doublell.InsertFromNode(1,5, Mode="value")
    my_doublell.Print()
    my_doublell.InsertFromNode(5,6, Mode="index")
    my_doublell.Print()
    ## FIND BY VALUE
    my_doublell.Find(1).PrintNode()
    ## GET BY INDEX
    my_doublell.GetByIndex(6).PrintNode()
    ## DELETE BY VALUE / INDEX
    my_doublell.DelNode(my_doublell.Find(6))
    my_doublell.Print()
    my_doublell.DelNode(my_doublell.GetByIndex(3))
    my_doublell.Print()

if __name__=='__main__':
    main()
