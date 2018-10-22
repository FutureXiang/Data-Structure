#coding=utf-8
#!/usr/bin/env python3


def main():
    #original = "".join(input().split())
    original = input().split()
    marks = input().split()
    marks.append("O")
    begins = []
    ends = []
    begin = end = 0
    flag = False
    for i in range(len(marks)):
        now = marks[i]
        if(now!='I-LOC' and flag):
            flag = False
            end = i
            begins.append(begin)
            ends.append(end)
        if(now=='B-LOC' and not flag):
            begin = i
            flag = True
    
    output_lst = []

    for i in range(len(original)):
        if(i in begins):
            output_lst.append("<LOC>")
        output_lst.append(original[i])
        if(i+1 in ends):
            output_lst.append("</LOC>")
    print("".join(output_lst))

if __name__=='__main__':
    main()
