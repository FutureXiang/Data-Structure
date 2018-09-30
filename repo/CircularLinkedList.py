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
    def PrintNode(self):
        print("Value: {}, Next: {}".format(self.value, self.next.value))
    def Insert(self, new):
        original_next = self.next
        new.next = original_next
        self.next = new

class CircLL():
    def __init__(self):
        Head = Node()
        Head.next = Head
        self.Head = Head
        # Empty Circ Linked List
    def Empty(self):
        return (self.Head.next==self.Head)
    def Print(self):
        if self.Empty():
            print("Empty!")
        else:
            now = self.Head
            print_list = [now.value]
            while(now.next!=self.Head):
                now = now.next
                print_list.append(now.value)
            writeline(print_list)
    def InsertFromHead(self, value):
        self.Head.Insert(Node(value))
    def InsertFromTail(self, value):
        self.GetTail().Insert(Node(value))
    def InsertFromNode(self, search, value):
        insert_node = self.Find(search)
        insert_node.Insert(Node(value))
    def GetTail(self):
        now = self.Head
        while(now.next!=self.Head):
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
    def DelByValue(self, value):
        assert not self.Empty()
        now = self.Head
        while(now.next!=self.Head):
            if now.next.value==value:
                prev = now
                found = now.next
                break
            now = now.next
        prev.next = found.next

def main():
    my_circll = CircLL()

    N = intput()
    ## INSERT BY HEAD/TAIL
    for i in range(N):
        now = intput()
        my_circll.InsertFromTail(now)
        my_circll.InsertFromHead(now)
        my_circll.Print()
    ## INSERT BY CERTAIN NODE(VALUE)
    my_circll.InsertFromNode(1,5)
    my_circll.Print()
    ## FIND BY VALUE
    my_circll.Find(1).PrintNode()
    ## DELETE BY VALUE
    my_circll.DelByValue(5)
    my_circll.Print()

if __name__=='__main__':
    main()
