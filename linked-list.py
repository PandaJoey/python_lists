from collections import deque
from typing import Counter

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node = Node(node)
        node.next = self.head
        self.head = node

    def add_last(self, node):
        node = Node(node)
        if not self.head:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        new_node = Node(new_node)
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_node):
        new_node = Node(new_node)
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def get_node(self, target_node_data):
        target_node = self.head
        count = 0

        if self.head is None:
            raise Exception("List is empty")

        while(target_node):
            if(count == target_node_data):
                return target_node.data
            count += 1
            target_node = target_node.next
        
        raise Exception("target data not found")

    def reverse_list():
        filer = None

    def test_linked_list(self):
        self.add_first("a") 
        self.add_last("b")
        self.add_before("2", "c")
        self.add_after("4", "d")
        self.remove_node("3")
        print(self.get_node(6))
        print(self)   


class Queue():

    queue = deque()

    def add_to_head(self, input):
        for item in input:
            self.queue.appendleft(item)
            print(self.queue)

    def add_to_tail(self, input):
        for item in input:
            self.queue.append(item)
            print(self.queue)

    def remove_from_head(self, input):
        for _ in range(0, input):
            self.queue.popleft()
            print(self.queue)

    def remove_from_tail(self, input):
        for _ in range(0, input):
            self.queue.pop()
            print(self.queue)

    def test_queue(self):
        self.add_to_head(["1", "2", "3", "4", "5"])
        self.add_to_tail(["1", "2", "3", "4", "5"])
        self.remove_from_head(5)
        self.remove_from_tail(5)


class Stack():

    stack = deque()

    def add_to_top(self, input):
        for item in input:
            self.stack.append(item)
            print(self.stack)

    def add_to_bottom(self, input):
        for item in input:
            self.stack.appendleft(item)
            print(self.stack)

    def remove_from_top(self, input):
        for _ in range(0, input):
            self.stack.pop()
            print(self.stack)

    def remove_from_bottom(self, input):
        for _ in range(0, input):
            self.stack.popleft()
            print(self.stack)

    def test_stack(self):
        self.add_to_top(["1", "2", "3", "4", "5"])
        self.add_to_bottom(["1", "2", "3", "4", "5"])
        self.remove_from_top(5)
        self.remove_from_bottom(5)


call_linked = LinkedList(["1", "2", "3", "4", "5"])
print(call_linked)
call_linked.test_linked_list()
print(call_linked)
call_queue = Queue()
call_queue.test_queue()
call_stack = Stack()
call_stack.test_stack()
