#coding=utf-8
#!/usr/bin/env python3

SIZE = int(input())
for i in range(SIZE):
    output_row=''
    for j in range(SIZE):
        if i==j:
            output_row+='1 '
        else:
            output_row+='0 '
    print(output_row)