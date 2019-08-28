from node import Node


class Tree(object):
    def __init__(self):
        self.root = None

    def find(self, k: float):
        return self.__find(k, self.root)

    def __find(self, k: float, current: Node):
        if k == current.value:  # Found it
            return current
        elif k < current.value:  # Value is less than current node value, go left
            if current.left_child is None:  # Value is not in the tree
                return None
            else:
                return self.__find(k, current.left_child)  # Go down another level in the left
        else:
            if current.right_child is None:  # Value is not in the tree
                return None
            else:
                return self.__find(k, current.right_child)  # Go down another level in the right

    def find_min(self, current: Node):
        while current.left_child is not None:  # Go down the tree following the extreme left path until the end
            current = current.left_child
        return current

    def next_value(self, k: float):  # Returns the immediately bigger number of k,
        # example: k = 2, returns 3 (if 3 is in the tree)
        current = self.find(k)
        if current.right_child is not None:  # if there is a right child, the minimum value
            # of the right subtree is the immediately bigger number
            return self.find_min(current.right_child)
        while current.parent is not None and current is current.parent.right_child:  # Goes up the tree until is root
            # or the node is the left child of the parent, if that happens, it means that the parent is the
            # immediately bigger number
            current = current.parent
        return current.parent

    def height(self, node: Node):
        if node is None:
            return -1
        else:
            return node.height

    def new_height(self, node: Node):  # Sets the node with the height of its childs + 1 (inverted height)
        node.height = max(self.height(node.left_child), self.height(node.right_child)) + 1

    def left_rotation(self, to_rotate: Node):
        right_child = to_rotate.right_child
        right_child.parent = to_rotate.parent
        if right_child.parent is None:
            self.root = right_child
        else:
            if right_child.parent.left_child is to_rotate:
                right_child.parent.left_child = right_child
            elif right_child.parent.right_child is to_rotate:
                right_child.parent.right_child = right_child
        to_rotate.right_child = right_child.left_child
        if to_rotate.right_child is not None:
            to_rotate.right_child.parent = to_rotate
        right_child.left_child = to_rotate
        to_rotate.parent = right_child
        self.new_height(to_rotate)
        self.new_height(right_child)

    def right_rotation(self, to_rotate: Node):
        left_child = to_rotate.left_child
        left_child.parent = to_rotate.parent
        if left_child.parent is None:
            self.root = left_child
        else:
            if left_child.parent.left_child is to_rotate:
                left_child.parent.left_child = left_child
            elif left_child.parent.right_child is to_rotate:
                left_child.parent.right_child = left_child
        to_rotate.left_child = left_child.right_child
        if to_rotate.left_child is not None:
            to_rotate.left_child.parent = to_rotate
        left_child.right_child = to_rotate
        to_rotate.parent = left_child
        self.new_height(to_rotate)
        self.new_height(left_child)

    def check_balance(self, node: Node):  # goes up the whole tree rebalancing when necessary
        while node is not None:
            self.new_height(node)
            if self.height(node.left_child) >= 2 + self.height(node.right_child):  # If there is a
                # difference between the two children bigger than 2, needs rebalancing.
                if self.height(node.left_child.left_child) >= self.height(node.left_child.right_child):
                    self.right_rotation(node)
                else:
                    self.left_rotation(node.left_child)
                    self.right_rotation(node)
            elif self.height(node.right_child) >= 2 + self.height(node.left_child):  # If there is a
                # difference between the two children bigger than 2, needs rebalancing.
                if self.height(node.right_child.right_child) >= self.height(node.right_child.left_child):
                    self.left_rotation(node)
                else:
                    self.right_rotation(node.right_child)
                    self.left_rotation(node)
            node = node.parent

    def insert(self, k: float):
        node = Node(None, k)
        if self.root is None:  # if the root doesn't exist, the root becames the only node
            self.root = node
        else:
            self.__insert(node, self.root)
        self.check_balance(node)

    def __insert(self, to_insert: Node, current: Node):
        if to_insert is None:
            return
        if to_insert.value < current.value:  # Is less than, go left
            if current.left_child is None:
                to_insert.parent = current
                current.left_child = to_insert
            else:
                self.__insert(to_insert, current.left_child)
        elif to_insert.value > current.value:  # Is bigger than, go right
            if current.right_child is None:
                to_insert.parent = current
                current.right_child = to_insert
            else:
                self.__insert(to_insert, current.right_child)
        else:
            print("Valor duplicado")
            return

    def delete(self, k: float):
        node = self.find(k) if type(k) is not Node else k
        if node is None:
            return None
        if node is self.root:  # If the node to be deleted is the root
            pseudoroot = Node(None, 0)
            pseudoroot.left_child = self.root
            self.root.parent = pseudoroot
            deleted = self.__delete(self.root)
            self.root = pseudoroot.left_child
            if self.root is not None:
                self.root.parent = None
        else:
            deleted = self.__delete(node)
        self.check_balance(deleted.parent)

    def __delete(self, current: Node):
        if current.left_child is None or current.right_child is None:
            if current is current.parent.left_child:
                current.parent.left_child = current.left_child or current.right_child  # Choose the one that is not None
                if current.parent.left_child is not None:
                    current.parent.left_child.parent = current.parent
            else:
                current.parent.right_child = current.left_child or current.right_child
                if current.parent.right_child is not None:
                    current.parent.right_child.parent = current.parent
            return current
        else:
            s = self.next_value(current.value)
            current.value, s.value = s.value, current.value
            return self.__delete(s)

    def display(self):
        lines, _, _, _ = self._display_aux(self.root)
        for line in lines:
            print(line)

    def _display_aux(self, current: Node):
        # No child.
        if current.right_child is None and current.left_child is None:
            line = '%s' % current.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if current.right_child is None:
            lines, n, p, x = self._display_aux(current.left_child)
            s = '%s' % current.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if current.left_child is None:
            lines, n, p, x = self._display_aux(current.right_child)
            s = '%s' % current.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display_aux(current.left_child)
        right, m, q, y = self._display_aux(current.right_child)
        s = '%s' % current.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '' + s + y * '' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
