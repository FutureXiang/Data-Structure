#coding=utf-8
#!/usr/bin/env python3

def solve(pre, mid):
    if(pre==[] or mid==[]):
        return
    sub_root = pre[0]
    pos_root = mid.index(sub_root)
    left_size = pos_root
    right_size = len(mid)-1-left_size
    
    if(left_size!=0):
        solve(pre[1:left_size+1], mid[:pos_root])
    
    if(right_size!=0):
        solve(pre[left_size+1:], mid[pos_root+1:])
    
    print(sub_root, end=' ') # print_following
    
def main():
    pre = input().split()
    mid = input().split()
    ### UNIQUE, Store VALUE
    ### Given PRE & MID, Query FOL
    solve(pre, mid)
    print()
    

if __name__=='__main__':
    main()
