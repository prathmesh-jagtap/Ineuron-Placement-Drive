"""Implementation of Queue using list in python
"""


class Queue:
    """
    Implementation of QUEUE class using list.
    Queue has two ends Front and Rear End. 
    """

    def __init__(self) -> None:
        self.q = []
        self.size = 0
        self.front = 0
        self.rear = self.size - 1

    def __repr__(self) -> str:
        return "".join(str(self.q))

    def IsEmpty(self):
        """This methoda checks that queue is empty or not

        Returns:
            bool: return True or False
        """
        return self.size == 0

    def enqueue(self, val: int):
        """This method insert an new value  in queue 

        Args:
            val (int): a value which is inserted

        Returns:
            list: int
        """
        self.q.append(val)
        self.size += 1
        return self.q

    def dequeue(self):
        """This mehtods remove the elemnt whch is first inserted

        Raises:
            Exception: If queue is empty it throughs Empty

        Returns:
            int: It return the element which is removed.
        """
        if self.IsEmpty():
            raise Exception("Emtpy")

        self.q.pop(self.front)
        self.size -= 1
        return self.q[self.front]


s = Queue()
s.enqueue(1)
s.enqueue(2)
s.enqueue(3)
s.enqueue(5)
s.enqueue(6)
s.dequeue()
s.dequeue()
print(s.IsEmpty())
print(s)
