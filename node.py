class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.height = 0

    def set_left_child(self, node):
        self.left_child = node

    def set_right_child(self, node):
        self.right_child = node

    def set_value(self, value):
        self.value = value

    def set_height(self, height):
        self.height = height
    
    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def get_value(self):
        return self.value

    def get_height(self):
        return self.height
