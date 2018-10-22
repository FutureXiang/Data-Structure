#coding=utf-8
#!/usr/bin/env python3


def main():
    inp = input()
    head = inp.split('-')[0]
    tail = inp[len(head)+1:]
    words = tail.split()
    if(head!='114514' or len(words)<3):
        print("No")
    else:
        if(words[0][0]!='g' or words[1][0]!='s' or words[2][0]!='t'):
            print("No")
        else:
            print("Yes")

if __name__=='__main__':
    main()
