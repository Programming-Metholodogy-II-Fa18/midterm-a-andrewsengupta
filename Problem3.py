class ProblemThree:
    
    def __init__(self):
        self.stack = []
        
    def ProblemThree(self,x):
        return self.stack.index(x)
    
    def main(self):
        self.stack.append(1)
        self.stack.append(5)
        self.stack.append(8)
        self.stack.append(10)
        self.stack.append(12)
        self.stack.append(14)
        self.stack.append(18)
        self.stack.append(20)
        self.stack.append(33)
        self.stack.append(41)
        print self.stack.index(8)
        print self.stack.index(33)
            