#coding=utf-8
#!/usr/bin/env python3
import math
def is_prime(x):
    if x==1 or x==0:
        return False
    elif x==2:
        return True
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True

n = int(input())

if is_prime(n):
    print("Y")
else:
    print("N")