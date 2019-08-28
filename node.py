class Node(object):
    def __init__(self, parent, k):
        self.value = k
        self.parent = parent
        self.left_child = None
        self.right_child = None
        self.height = -1
