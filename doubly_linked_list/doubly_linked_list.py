from tkinter.messagebox import NO
from traceback import print_list


class Node():
    def __init__(self, value, previous_node = None, next_node = None):
        self.value = value
        self.previous_node = previous_node
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def get_previous_node(self):
        return self.previous_node

    def set_next_node(self, new_next_node):
        self.next_node = new_next_node

    def set_previous_node(self, new_previous_node):
        self.previous_node = new_previous_node

class Doubly_linked_list():
    def __init__(self, value):
        self.head_node = Node(value)
        self.tail_node = self.head_node

    def get_head_node(self):
        return self.head_node

    def get_tail_node(self):
        return self.tail_node

    def add_to_head(self, value):
        new_node = Node(value)
        if self.get_head_node() == None:
            self.head_node = new_node
        else:
            self.head_node.set_previous_node(new_node)
            new_node.set_next_node(self.get_head_node())
            self.head_node = new_node
    
    def add_to_tail(self, value):
        new_node = Node(value)
        if self.get_tail_node() == None:
            self.tail_node = new_node
        else: 
            self.tail_node.set_next_node(new_node)
            new_node.set_previous_node(self.get_tail_node())
            self.tail_node = new_node

    def remove_head(self):
        if self.get_head_node() == None:
            print("Nothing to remove.")
        else:
            new_head = self.head_node.next_node 
            new_head.set_previous_node(None)
            self.head_node.set_next_node(None)
            self.head_node = new_head

    def remove_tail(self):
        if self.get_tail_node() == None:
            print("Nothing to remove.")
        else:
            new_tail = self.tail_node.previous_node
            new_tail.set_next_node(None)
            self.tail_node.set_previous_node(None)
            self.tail_node = new_tail
            
    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        while current_node.get_next_node() != None:
            if current_node.value == value_to_remove:
                current_node.previous_node.set_next_node(current_node.next_node)
                current_node.next_node.set_previous_node(current_node.previous_node)
            current_node = current_node.get_next_node()
    
    def print_list(self):
        current_node = self.get_head_node()
        while current_node.next_node:
            print(current_node.get_value())
            current_node = current_node.next_node
        print(current_node.get_value())

    
            

my_doubly = Doubly_linked_list("paper")
my_doubly.add_to_head("pen")
my_doubly.add_to_head("pencil")

my_doubly.add_to_tail("eraser")
my_doubly.add_to_tail("chalk")
my_doubly.print_list()
print("")
print(my_doubly.head_node.next_node.get_value())
print("")

my_doubly.remove_head()
my_doubly.print_list()

print("")
my_doubly.remove_tail()
my_doubly.print_list()

print("")
my_doubly.remove_node("paper")
my_doubly.print_list()



            

    