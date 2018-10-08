#coding=utf-8
#!/usr/bin/env python3

CamelCase = input()
import re
tail = 0
result = []
while(tail<len(CamelCase)):
    res = re.match(r"([A-Z][a-z]*){1}", CamelCase[tail:])
    tail += res.end()
    result.append(res.group(1).lower())
print('_'.join(result))