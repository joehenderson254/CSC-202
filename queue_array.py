class Queue:
 '''Implements an array-based, efficient first-in first-out Abstract Data Type
 using a Python array (faked using a List)'''
 def __init__(self, capacity):
  self.capacity = capacity
  self.items = [None] * capacity
  self.num_items = 0
 def is_empty(self):
  if self.num_items == 0:
   return True
 def is_full(self):
  if self.num_items == self.capacity:
   return True
 def enqueue(self, item):
  if Queue.is_full(self) == True:
   return IndexError
  self.items[self.num_items] = item
  self.num_items += 1
 def dequeue(self):
  if Queue.is_empty(self) == True:
   return IndexError
  self.num_items -= 1
  return self.items.pop(0)
 def size(self):
  return self.num_items