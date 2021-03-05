# Course: CS 261
# Author: Mark Mendez
# Assignment: 6
# Description: Implements a basic Stack class


class Stack:
    """
    Class to implement a stack
    """
    def __init__(self, starting_list=None):
        """
        Initializes the stack
        :param starting_list: list of elements to add immediately to the stack
        """
        self._data = []

        if starting_list is not None:
            for element in starting_list:
                self._data.append(element)

    def push(self, value):
        """
        Pushes a value onto the stack
        :param value: any value to push
        """
        self._data.append(value)

    def pop(self):
        """
        Removes and returns the value at the top of the stack
        :return: the value which was removed from the stack
        """
        return self._data.pop()

    def is_empty(self):
        """
        Checks whether the stack has any elements in it
        :return: True if the stack is empty; False if not empty
        """
        return len(self._data) < 1
