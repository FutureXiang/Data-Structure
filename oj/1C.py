#coding=utf-8
#!/usr/bin/env python3

string = input()
string=string.lower()

def is_space_dot(x):
    if x==' ' or x=='.' or x==',':
        return True
    return False

for i in range(2,len(string)-1):
    if string[i]=='i' and is_space_dot(string[i-1]) and is_space_dot(string[i+1]):
        string=string[:i]+'I'+string[i+1:]
if string[0]=='i' and is_space_dot(string[1]):
    string='I'+string[1:]


sub_strings = string.split('.')
ret_strings = []
for sub_str in sub_strings:
    L=0
    R=len(sub_str)-1
    for i in range(len(sub_str)):
        if sub_str[i].isalpha():
            L=i
            break
    for i in range(L,len(sub_str)):
        if is_space_dot(sub_str[i]):
            R=i
            break
    new_str=sub_str[:L] + sub_str[L:R].title() + sub_str[R:]
    ret_strings.append(new_str)

print('.'.join(ret_strings))