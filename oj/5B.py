#coding=utf-8
#!/usr/bin/env python3

def intput():
    return int(input())


def main():
    N = intput()
    words = []
    min_len = 1e10
    for i in range(N):
        now = input()
        words.append(now)
        min_len = min(min_len, len(now))
    
    flag = True
    max_match = -1
    for i in range(min_len):
        now = words[0][:i+1] # prefix
        for word in words:
            if(word[:i+1]!=now):
                flag=False
                break
        if(flag==False):
            break
        max_match = max(max_match, i)
    if(max_match==-1):
        print("No")
    else:
        print(words[0][:max_match+1])


if __name__=='__main__':
    main()
