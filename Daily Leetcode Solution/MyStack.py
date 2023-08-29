import collections

"""
    LeetCode Problem - 225. Implement Stack using Queues
    
    Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

    Implement the MyStack class:

    void push(int x) Pushes element x to the top of the stack.
    int pop() Removes the element on the top of the stack and returns it.
    int top() Returns the element on the top of the stack.
    boolean empty() Returns true if the stack is empty, false otherwise.
    Notes:

    You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
    Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
"""


# The `MyStack` class implements a stack using a deque, where elements are pushed to the back and
# popped from the front.
class MyStack:
    def __init__(self):
        self.que = collections.deque()

    def push(self, x: int) -> None:
        """
        The push function appends an element to the end of a queue and then rotates the queue so that
        the newly added element becomes the front.

        :param x: The parameter `x` is an integer value that represents the element to be pushed into
        the queue
        :type x: int
        """
        self.que.append(x)
        for _ in range(len(self.que) - 1):
            self.que.append(self.que.popleft())

    def pop(self) -> int:
        """
        The function `pop` returns and removes the first element from a queue.
        :return: The `pop` method is returning an integer value.
        """
        return self.que.popleft()

    def top(self) -> int:
        # trunk-ignore(ruff/D401)
        """
        "The function returns the first element of a queue."
        :return: the first element of the "que" list.
        """
        return self.que[0]

    def empty(self) -> bool:
        """
        The function checks if a queue is empty by returning True if the length of the queue is 0, and
        False otherwise.
        :return: The code is returning a boolean value indicating whether the "que" attribute of the
        object is empty or not.
        """
        return len(self.que) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
