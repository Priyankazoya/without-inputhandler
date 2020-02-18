# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 15:38:26 2020

@author: Priyanka Zoya
"""

'''
stack data structure

D
C
B
A
'''

class Stack():
    def __init__(self):
        self.items = []
        
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def get_stack(self):
        return self.items
    
s = Stack()
s.push("A")
s.push("B")
s.push("c")
s.push("D")

print(s.get_stack())

s.push("E")
print(s.get_stack())
s.pop()
print(s.get_stack())



class Stack():
    def __init__(self):
        self.items = []
        
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items==[]
    
    
    
    def get_stack(self):
        return self.items
    
s = Stack()
print(s.is_empty())
# s.push("A")
# s.push("B")
# s.push("c")
# s.push("D")

print(s.get_stack())


class Stack():
    def __init__(self):
        self.items = []
        
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items==[]
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    
    
    def get_stack(self):
        return self.items
    
s = Stack()
print(s.is_empty())
s.push("A")
s.push("B")
s.push("c")
s.push("D")

print(s.peek())




class Stack():
    def __init__(self):
        self.items = []
        
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items==[]
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    
    
    def get_stack(self):
        return self.items
    
s = Stack()
s.push(11)
s.push(12)
s.push(13)
s.push(14)
print(s.get_stack())
s.pop() 
print(s.get_stack())


class Queue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items == []
    def enqueue(self,item):
        self.items.insert(0,item)
    def peek(self):
        self.items.pop()
    def size(self):
        return len(self.items)
    def printqueue(self):
        for items in self.items:
            print(items)
            

q=Queue()
print(q.isEmpty())

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.printqueue()
q.peek()
q.printqueue()


 