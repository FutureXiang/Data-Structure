#coding=utf-8
#!/usr/bin/env python3

input_string = input()
scores = input_string.split()
for i in range(len(scores)):
    scores[i]=int(scores[i])

max_score=max(scores)

indexs = []
for i in range(len(scores)):
    if scores[i]==max_score:
        indexs.append(str(i+1))

print(' '.join(indexs))