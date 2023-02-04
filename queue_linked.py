class node:
 def __init__(self, item):
    self.data = item
    self.next = None


node = node([None])
class Queue:
 '''Implements an link-based ,efficient first-in first-out Abstract Data Type'''
 def __init__(self, capacity):
  self.capacity = capacity
  self.head = None
  self.num_items = 0
 def is_empty(self):
  if self.num_items == 0:
   return True
  return False
 def is_full(self):
  if self.num_items == self.capacity:
   return True
  return False
 def enqueue(self, item):
  '''If Queue is not full, enqueues (adds) item to Queue
  If Queue is full when enqueue is attempted, raises IndexError
  MUST have O(1) performance'''
  if Queue.is_full == True:
   return IndexError
  node.data[self.num_items] = item
  self.num_items += 1
  node.next = self.num_items
 def dequeue(self):
  '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
  If Queue is empty when dequeue is attempted, raises IndexError
  MUST have O(1) performance'''
  if Queue.is_empty == True:
   return IndexError
  self.num_items = self.num_items - 1
  return node.data[0]
 def size(self):
  '''Returns the number of elements currently in the Queue, not the capacity
  MUST have O(1) performance'''
  return self.num_items