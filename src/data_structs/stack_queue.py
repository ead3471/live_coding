from typing import TypeVar, Generic, Union
import pytest


T = TypeVar("T")


class QueueIsEmptyException(Exception):
    msg = 'The queue is empty!'


class WrongTypeException(Exception):
    pass


class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value: T = value
        self.next: Union[Node[T], None] = None


class Queue(Generic[T], object):
    def __init__(self) -> None:
        self.head: Union[Node[T], None] = None
        self.tail: Union[Node[T], None] = None

    def is_empty(self) -> bool:
        return self.head is None

    def push(self, value: T):
        if not isinstance(value, self.__orig_class__.__args__[0]):
            raise TypeError(
                f"Value must be a {self.__orig_class__.__args__[0]} type")

        new_element = Node[T](value)

        if self.is_empty():
            self.tail = new_element
            self.head = new_element
        else:
            self.tail.next = new_element
            self.tail = new_element

    def pop(self) -> T:
        if self.is_empty():
            raise QueueIsEmptyException("The queue is empty!")
        value = self.head.value
        self.head = self.head.next
        return value


class Stack(Generic[T], object):
    def __init__(self) -> None:
        self.head: Union[Node[T], None] = None

    def is_empty(self) -> bool:
        return self.head is None

    def push(self, value: T):
        if not isinstance(value, self.__orig_class__.__args__[0]):
            raise TypeError(
                f"Value must be a {self.__orig_class__.__args__[0]} type")

        new_element = Node[T](value)

        if self.is_empty():
            self.head = new_element
        else:
            new_element.next = self.head
            self.head = new_element

    def pop(self) -> T:
        if self.is_empty():
            raise QueueIsEmptyException("The queue is empty!")
        value = self.head.value
        self.head = self.head.next
        return value


def test_queue():
    queue = Queue[str]()
    queue.push("1")
    queue.push("2")
    queue.push("4")

    assert (queue.pop() == "1")
    assert (queue.pop() == "2")
    assert (queue.pop() == "4")

    with pytest.raises(TypeError) as exc_info:
        queue.push(4)

    with pytest.raises(QueueIsEmptyException) as exc_info:
        queue.pop()


def test_stack():
    stack = Stack[str]()
    stack.push("1")
    stack.push("2")
    stack.push("4")

    assert (stack.pop() == "4")
    assert (stack.pop() == "2")
    assert (stack.pop() == "1")

    with pytest.raises(TypeError) as exc_info:
        stack.push(4)

    with pytest.raises(QueueIsEmptyException) as exc_info:
        stack.pop()


if __name__ == "__main__":
    test_queue()
    test_stack()
