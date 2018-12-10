#coding=utf-8
#!/usr/bin/env python3


def main():
    N = int(input())
    inpline = input()
    inpline = inpline.split()
    arr = []
    for i in inpline:
        arr.append(int(i))
    arr.sort()
    
    maxdiff = -2147483648
    for i in range(len(arr)):
        if(i==0):
            maxdiff = max(maxdiff, arr[i+1]-arr[i])
        elif(i==len(arr)-1):
            maxdiff = max(maxdiff, arr[i]-arr[i-1])
        else:
            maxdiff = max(maxdiff, arr[i+1]-arr[i])
            maxdiff = max(maxdiff, arr[i]-arr[i-1])
    for i in range(len(arr)-1):
        if((arr[i+1]-arr[i])==maxdiff):
            print(arr[i], arr[i+1])
        


if __name__=='__main__':
    main()
