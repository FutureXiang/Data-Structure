#coding=utf-8
#!/usr/bin/env python3

class SQueue(object):
	def __init__(self, init_len=8):
		self.__elem = [0] * init_len
		self.__len = init_len
		self.__head = 0
		self.__num = 0


	def __extend(self):
		old_len = self.__len
		self.__len *= 2
		new_elems = [0] * self.__len
		for i in range(old_len):
			new_elems[i] = self.__elem[(self.__head + i) % old_len]
		self.__elem, self.__head = new_elems, 0


	def is_empty(self):
		return self.__num == 0


	def peek(self):
		if self.__num == 0:
			raise MemoryError
		return self.__elem[self.__head]
		

	def enqueue(self, e):
		if self.__num == self.__len:
			self.__extend()
		self.__elem[(self.__head + self.__num) % self.__len] = e
		self.__num += 1
		
		
	def dequeue(self):
		if self.__num == 0:
			raise MemoryError
		e = self.__elem[self.__head]
		self.__head = (self.__head + 1) % self.__len
		self.__num -= 1
		return e

# stack.pop() <=> q2.push_back(q1.pop()) for n-1 times

def writeline(list):
    for i in range(len(list)):
        list[i]=str(list[i])
    print(" ".join(list))

def main():
    q1 = SQueue()
    q2 = SQueue()
    q1_size = 0
    N = int(input())
    for i in range(N):
        ch = int(input())
        q1.enqueue(ch)
        q1_size+=1
    
    res1 = []
    res2 = []

    M = int(input())
    try:
        for i in range(M):
            oprs = input()
            opr = oprs.split()[0]
            if(opr=='A'):
                num = int(oprs.split()[1])
                q1.enqueue(num)
                q1_size+=1
            else:
                q1_size_temp = q1_size
                if(q1.is_empty()):
                    raise MemoryError
                while(not q1.is_empty()):
                    now = q1.dequeue()
                    q1_size_temp-=1
                    if(q1_size_temp==0):
                        res1.append(now)
                        break
                    else:
                        q2.enqueue(now)
                q1 = q2
                q1_size -= 1
        writeline(res1)
        while(q1_size!=0):
            q1_size_temp = q1_size
            while(not q1.is_empty()):
                now = q1.dequeue()
                q1_size_temp-=1
                if(q1_size_temp==0):
                    res2.append(now)
                    break
                else:
                    q2.enqueue(now)
            q1 = q2
            q1_size -= 1
        writeline(res2)
    except:
        print("No")
        return

if __name__=='__main__':
    main()
