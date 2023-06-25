"""Implementation of Stack using list in python
"""


class Stack:
    """
    Implementation of stack class using list. 
    """

    def __init__(self) -> None:
        self.list1 = []

    def IsEmpty(self):
        """This methoda checks that stack is empty or not

        Returns:
            bool: return True or False
        """
        return len(self.list1) < 1

    def push(self, val: int):
        """This method insert an new value  in stack 

        Args:
            val (int): a value which is inserted

        Returns:
            list: int
        """
        self.list1.append(val)
        return self.list1

    def pop(self):
        """This mehtods pops / remove the last elemnt from stack 

        Raises:
            Exception: If stack is empty it throughs stack underflow

        Returns:
            int: It return the element  whic is removed.
        """
        if self.IsEmpty():
            raise Exception("Stack Underflow")

        else:
            popped_ele = self.list1.pop()
            return popped_ele


s = Stack()
s.push(5)
s.pop()
s.IsEmpty()
