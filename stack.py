class stack:
    def _init_(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "cannot pop fromm empty stack"
    def is_empty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)
    def peek(self):
        if not slef.is_empty():
            return self.items[-1]
        else:
            return "empty stack"
s=stack()
s.push(2)
s.push(3)
print(s.pop())
print(s.is_empty())
