from typing import Any 


class Queue:
    def __init__(self) -> None:
        self.queue = []

    def is_empty(self) -> bool:
        """ this method check queue is empty or not """
        return len(self.queue) == 0
    
    
    def enqueue(self, item: Any) -> None:
        """ this method push new element in queue """
        self.queue.append(item)


    def dequeue(self) -> Any | str:
        """ this method pop first element from queue """
        if self.is_empty():
            return "Queue is empty!!!"
        else:
            return self.queue.pop(0)
        
        
    def peek(self) -> Any | str:
        """ this method return the first element """
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.queue[0]
        

    def size(self) -> int:
        """ this method return the size of queue """
        return len(self.queue)
    

    def __str__(self) -> str:
        """ this magical method return queue as string """
        return str(self.queue)
    

    def __len__(self) -> int:
        """ this magical method return the size of queue """
        return self.size()
    

    def __contains__(self, item: Any) -> bool:
        """ this magical method is implementing of 'in' operator """
        return item in self.queue
    

    def __eq__(self, an_other_queue: Any) -> bool | str:
        """ this method check two queue are equal """
        if isinstance(an_other_queue, Queue):
            return an_other_queue.queue == self.queue
        else:
            return "no this item is not queue"
        


queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

an_other_queue = Queue()

an_other_queue.enqueue(10)
an_other_queue.enqueue(20)
an_other_queue.enqueue(30)


if queue == an_other_queue:
    print("both of them are equal ")
else:
    print("no not equal")

print(queue)

if 35 in queue:
    print("yes it is here!!!")
else:
    print("what the f!!!")

queue.dequeue()
print(queue)
print(f"the size of queue is {queue.size()}")
print(f"again the size with magical method {len(queue)}")