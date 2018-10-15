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

def main():
    road = SQueue()
    N = int(input())
    for i in range(N):
        ch = input()
        road.enqueue(ch)
    line = SQueue()
    M = int(input())
    for i in range(M):
        ch = input()
        line.enqueue(ch)

    oprs = input()
    try:
        for opr in oprs:
            if(opr=='A'):
                road.dequeue()
            else:
                now = line.dequeue()
                road.enqueue(now)
    except:
        print('No')
        return
    
    while(not road.is_empty()):
        print(road.dequeue())


if __name__=='__main__':
    main()
