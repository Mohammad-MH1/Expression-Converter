class Stack:
  def __init__(self) -> None:
    self.items = []
  
  def push(self,item):
    self.items.append(item)
    return self.items
    
  def pop(self):
    if self.items:
      return self.items.pop()
    else:
      return None
  
  def size(self):
    return len(self.items)
  
  def is_empty(self):
    return True if self.size() == 0 else False
  
  def list(self):
    return self.items