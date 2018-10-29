#coding=utf-8
#!/usr/bin/env python3


def main():
    mapping = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
    ans = []
    num = input()
    for i in range(len(num)):
        now = int(num[i]) * 10**(len(num)-1-i)
        dig = int(num[i])
        if(dig==0):
            continue
        elif(dig==9):
            if(now==900):
                ans.append("CM")
            if(now==90):
                ans.append("XC")
            if(now==9):
                ans.append("IX")
        elif(dig>=5):
            if(now>=500):
                ans.append("D")
            elif(now>=50):
                ans.append("L")
            elif(now>=5):
                ans.append("V")
            times = dig-5
            if(now>=100):
                ans.append("C"*times)
            elif(now>=10):
                ans.append("X"*times)
            elif(now>=1):
                ans.append("I"*times)
        elif(dig==4):
            if(now==400):
                ans.append("CD")
            if(now==40):
                ans.append("XL")
            if(now==4):
                ans.append("IV")
        else:
            times = int(num[i])
            if(now>=1000):
                ans.append("M"*times)
            elif(now>=100):
                ans.append("C"*times)
            elif(now>=10):
                ans.append("X"*times)
            elif(now>=1):
                ans.append("I"*times)
    print("".join(ans))
if __name__=='__main__':
    main()
