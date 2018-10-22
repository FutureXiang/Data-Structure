#coding=utf-8
#!/usr/bin/env python3
import re

def main():
    inp = input()
    res = re.search(r"^(([0-9]){5}|([0-9]){8}|(((ZY)|(SY)|(BY))([0-9]){7}))$", inp)
    print(res!=None)
        

if __name__=='__main__':
    main()
