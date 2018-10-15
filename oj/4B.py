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
			raise "QueueUnderflow"
		return self.__elem[self.__head]
		

	def enqueue(self, e):
		if self.__num == self.__len:
			self.__extend()
		self.__elem[(self.__head + self.__num) % self.__len] = e
		self.__num += 1
		
		
	def dequeue(self):
		if self.__num == 0:
			raise "QueueUnderflow"
		e = self.__elem[self.__head]
		self.__head = (self.__head + 1) % self.__len
		self.__num -= 1
		return e

def main():
    N = int(input())
    A = SQueue()
    B = SQueue()
    C = SQueue()
    for i in range(N):
        Id, Prior = input().split()
        Id = int(Id)
        if(Prior=='A'):
            A.enqueue(Id)
        elif(Prior=='B'):
            B.enqueue(Id)
        else:
            C.enqueue(Id)
    while(not A.is_empty()):
        print(A.dequeue())
    while(not B.is_empty()):
        print(B.dequeue())
    while(not C.is_empty()):
        print(C.dequeue())

if __name__=='__main__':
    main()
