#coding=utf-8
#!/usr/bin/env python3

Num_1 = int(input())
dict_1 = {}
for i in range(Num_1):
    in_str = input()
    key = in_str.split()[0]
    value = int(in_str.split()[1])
    dict_1.update({key:value})
Num_2 = int(input())
dict_2 = {}
for i in range(Num_2):
    in_str = input()
    key = in_str.split()[0]
    value = int(in_str.split()[1])
    dict_2.update({key:value})

for key in dict_2:
    if key in dict_1.keys():
        dict_1[key]+=dict_2[key]
    else:
        dict_1.update({key:dict_2[key]})

query=input()
print(dict_1[query])