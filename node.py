class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def set_left_child(self, node):
        self.left_child = node

    def set_right_child(self, node):
        self.right_child = node

    def set_value(self, value):
        self.value = value

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def get_value(self):
        return self.value
