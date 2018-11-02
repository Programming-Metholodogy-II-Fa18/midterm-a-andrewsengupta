class Stack:
    
    def __init__ (self):
        self.stack = []
        
    def add(self,item):
        return self.stack.append(item)
        
    def remove(self,item):
        return self.stack.pop(item)
    
    def getValue(self,index):
        if index > len(self.stack):
            return -1
        else:
            return self.stack.getitem(index)
            
class __main__:
    stack = Stack()
    stack.add(1)
    stack.add(9)
    stack.add(4)
    stack.add(5)
    stack.add(10)
    stack.add(0)
    stack.getValue(0)
    stack.getValue(3)



            
        
    
    
    