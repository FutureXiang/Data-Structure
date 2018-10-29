#coding=utf-8
#!/usr/bin/env python3


def main():
    lst = input().split()
    for i in range(len(lst)):
        lst[i] = int(lst[i])

    ans = 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            now = min(lst[i],lst[j]) * abs(i-j)
            ans = max(ans, now)
    print(ans)

if __name__=='__main__':
    main()
