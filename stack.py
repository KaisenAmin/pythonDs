from typing import Any 


class Stack:
    def __init__(self):
        self.stack = [] 
  

    def is_empty(self) -> bool:
        """ this method return stack is empty or not """
        return len(self.stack) == 0
    
    
    def push(self, value: Any) -> None:
        """ this method push new element to the stack """
        self.stack.append(value)

    
    def pop(self) -> Any:
        """ this method pop the last element """

        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"
    

    def size(self) -> int:
        """ this method return size of the stack """
        return len(self.stack)
    

    def peek(self) -> Any:
        """ this method return the last element """

        if not self.is_empty():
            return self.stack[-1]

        else:
            return "Stack is empty"
        
    def __str__(self) -> str:
        """ this magical method return list as string """
        return str(self.stack)
    

    def __len__(self) -> int:
        """ this magical method return size of the stack """
        return len(self.stack)
    

stack = Stack()

stack.push(15)
stack.push("Python programmer")
stack.push(15.32)

print(stack)
print(stack.pop())

if not stack.is_empty():
    print(stack)

print(stack.size())
print(len(stack))

print(stack.peek())
print(stack)

    


    