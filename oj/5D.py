#coding=utf-8
#!/usr/bin/env python3
import re

def main():
    inp = input()
    res = re.search(r"dividend = ([-]?[1-9][0-9]*){1}, divisor = ([-]?[1-9][0-9]*){1}", inp)
    if(res==None):
        print("No")
    else:
        a = int(res.group(1))
        b = int(res.group(2))
        print(a//b)
if __name__=='__main__':
    main()
