from collections import deque


class Queue:
    def __init__(self, size):
        """
        Queue class to create a queue with user-defined size
        :param size: The maximum size of the queue
        """
        self.queue = deque(maxlen=size)
        self.size = size

    def add_element(self, data) -> None:
        """
        Adds data to the queue
        :param data: The data to add
        :return: Displays the final state of the queue or a full message
        """
        if len(self.queue) == self.size:
            print("Queue is Full!")
        else:
            self.queue.append(data)  # FIFO behavior: append to the right
            print(f"{data} added to queue. Final queue is {self.queue}")

    def remove_element(self) -> None:
        """
        Removes the oldest element from the queue (FIFO)
        :return: Displays the element removed or an empty message
        """
        if not self.queue:
            print("Queue is Empty!")
        else:
            removed_element = self.queue.popleft()  # FIFO behavior: remove from the left
            print(f"{removed_element} removed from queue. Final queue is {self.queue}")

    def display(self):
        """
        Displays the current state of the queue
        """
        if not self.queue:
            print("Queue is empty!")
        else:
            print(f"Queue: {self.queue}")
