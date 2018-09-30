#coding=utf-8
#!/usr/bin/env python3

code=input()

flag=True
for i in range(17): # [0,16]
    if code[i].isdigit()==False:
        flag=False
        break
if not(code[17]=='X' or code[17].isdigit()==True):
    flag=False

weight=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
num=['1','0','X','9','8','7','6','5','4','3','2']
calc=0
for i in range(17):
    calc += weight[i]*int(code[i])
calc %= 11

#print(calc, num[calc])

if code[17]!=num[calc]:
    flag=False

if flag==False:
    print("NO")
else:
    print("YES")