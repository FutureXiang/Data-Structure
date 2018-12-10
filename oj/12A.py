#coding=utf-8
#!/usr/bin/env python3




def main():
    N = int(input())
    inpline = input()
    arr = inpline.split()
    arr = list(set(arr))
    N = len(arr)
    hash = [[] for i in range(100)]
    for i in arr:
        num = int(i)
        suffix = num%100
        hash[suffix].append(num)
    sum = 0
    for i in arr:
        num = int(i)
        suffix = num%100
        sum += (hash[suffix].index(num)+1)
    print("{:.2f}".format(sum*1.0/N))

if __name__=='__main__':
    main()
