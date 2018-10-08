#coding=utf-8
#!/usr/bin/env python3

n = int(input())
store = {}
for i in range(n):
    action = input()
    if action=='A':
        inp = input()
        name = inp.split()[0]
        num = inp.split()[1]
        store.update({name:num})
    else:
        inp = input()
        if inp not in store:
            print("NONE")
        else:
            print(store[inp])
