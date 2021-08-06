class DynamicArray(object):
  def __init__(self, capacity=0):
    self.capacity = capacity
    if not capacity:
      self.arr = None
      self.len = 0
    else:
      self.len = 0
      self.arr = []

  def size(self):
    return self.len

  def isEmpty(self):
    return self.len == 0

  def get(self, index):
    if index >= self.len or index < 0:
      raise ValueError("Index out of range in get")
    return self.arr[index]

  def set(self, index, elem):
    if index >= self.len or index < 0:
      raise ValueError("Index out of range in set")
    self.arr[index] = elem

  def clear(self):
    self.arr = []
    self.len = 0

  def add(self, elem):
    if self.len+1 >= self.capacity:
      self.capacity *= 2
    self.arr.append(elem)

  def removeAt(self, rm_index):
    if rm_index >= self.len or rm_index < 0:
      raise ValueError("Remove Index out of range in removeAt")
    data = self.arr.pop(rm_index)
    self.len -= 1
    return data

  def remove(self, value):
    self.arr.remove(value)

  def indexOf(self, value):
    for i in range(self.len):
      if self.arr[i] == value:
        return i
    return -1

  def contains(self, value):
    return self.indexOf(value) != -1

  def __str__ (self):
    s = "["
    for i in range(self.len-1):
      s += str(self.arr[i]) 
      s += ", "
    s += str(self.arr[self.len -1]
    s += "]"
      
    
    


