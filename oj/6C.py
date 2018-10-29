#coding=utf-8
#!/usr/bin/env python3

def main():
    mapping = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    arab = input()
    ans = 0
    i = 0
    while(i<len(arab)):
        now = mapping[arab[i]]
        nex = (mapping[arab[i+1]] if i!=len(arab)-1 else 0)
        if(now>=nex):
            ans += now
            i+=1
        else:
            ans += nex-now
            i+=2
    print(ans)


if __name__=='__main__':
    main()
