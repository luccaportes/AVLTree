from node import Node

class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def get_size(self):
        return self.size

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            self.size += 1
            return True
        else:
            inserted = self.insert_node(self.root, value)
            if inserted:
                self.size += 1
                return True
            return False

    def insert_node(self, current: Node, value):
        if value < current.get_value():
            if current.get_left_child() is None:
                current.set_left_child(Node(value))
                # return True
            else:
                # return self.insert_node(current.get_left_child(), value)
                self.insert_node(current.get_left_child(), value)
        elif value > current.get_value():
            if current.get_right_child() is None:
                current.set_right_child(Node(value))
                # return True
            else:
                # return self.insert_node(current.get_right_child(), value)
                self.insert_node(current.get_right_child(), value)
        self.balance(current)
        # else:
        #     print("duplicated value")
        #     return False

    def contains(self, value):
        return self.find_node(value) is not None

    def find_parent(self, value):
        return self.__find_parent_node(self.root, value)

    def __find_parent_node(self, current: Node, value):
        if current is None:
            return None
        if value == current.get_value():
            return None
        if value < current.get_value():
            if current.get_left_child() is None:
                return None
            elif current.get_left_child().get_value() == value:
                return current
            else:
                return self.__find_parent_node(current.get_left_child(), value)
        else:
            if current.get_right_child() is None:
                return None
            elif current.get_right_child().get_value() == value:
                return current
            else:
                return self.__find_parent_node(current.get_right_child(), value)

    def find_node(self, value):
        return self.__find_node_tree(self.root, value)

    def __find_node_tree(self, current: Node, value):
        if current is None:
            return None
        if current.get_value() == value:
            return current
        elif value < current.get_value():
            return self.__find_node_tree(current.get_left_child(), value)
        else:
            return self.__find_node_tree(current.get_right_child(), value)

    def remove_node(self, value):
        node_to_remove = self.find_node(value)
        if node_to_remove is None:
            return False
        if node_to_remove is self.root:
            return self.delete_root()
        parent = self.find_parent(value)
        if self.size == 1:
            self.root = None
        elif node_to_remove.get_left_child() is None and node_to_remove.get_right_child() is None:
            if node_to_remove.get_value() < parent.get_value():
                parent.set_left_child(None)
            else:
                parent.right_child(None)
        elif node_to_remove.get_left_child() is None and node_to_remove.get_right_child() is not None:
            if node_to_remove.get_value() < parent.get_value():
                parent.set_left_child(node_to_remove.get_right_child())
            else:
                parent.set_right_child(node_to_remove.get_right_child())
        elif node_to_remove.get_left_child() is not None and node_to_remove.get_right_child() is None:
            if node_to_remove.get_value() < parent.get_value():
                parent.set_left_child(node_to_remove.get_left_child())
            else:
                parent.set_right_child(node_to_remove.get_left_child())
        else:
            largest_value = node_to_remove.get_left_child()
            while largest_value.get_right_child() is not None:
                largest_value = largest_value.get_right_child()
            parent_largest_value = self.find_parent(largest_value.get_value())
            parent_largest_value.set_right_child(None)
            node_to_remove.set_value(largest_value.get_value())
        self.size -= 1
        return True

    def delete_root(self):
        if self.root.get_left_child() is None and self.root.get_right_child() is None:
            self.root = None
            return True
            # Case 2.2: Root node has left child
        elif self.root.get_left_child() and self.root.get_right_child() is None:
            self.root = self.root.get_left_child()
            return True
            # Case 2.3: Root node has right child
        elif self.root.get_left_child() is None and self.root.get_right_child():
            self.root = self.root.get_right_child()
            return True
            # Case 2.4: Root node has two children
        else:
            move_node = self.root.get_right_child()
            move_node_parent = None
            while move_node.get_left_child() is not None:
                move_node_parent = move_node
                move_node = move_node.get_left_child()
            if move_node_parent is not None:
                if move_node.get_value() < move_node_parent.get_value():
                    move_node_parent.set_left_child(None)
                else:
                    move_node_parent.set_right_child(None)
            else:
                if move_node.get_value() < self.root.get_value():
                    self.root.set_left_child(None)
                else:
                    self.root.set_right_child(None)
            self.root.set_value(move_node.get_value())
            return True

    def level_by_level(self, current):
        current_level = [current]
        while len(current_level) > 0:
            print(' '.join(str(node.get_value()) for node in current_level))
            next_level = []
            for n in current_level:
                if n.get_left_child() is not None:
                    next_level.append(n.get_left_child())
                if n.get_right_child() is not None:
                    next_level.append(n.get_right_child())
                current_level = next_level

    def print_(self):
        self.level_by_level(self.root)
    
    # TODO --> rotacoes duplas -- chamar uma apos a outra? se sim com o mesmo node?
    
    def left_rotation(self, current):
        print("Left Rotation!")
        if current.get_right_child() is not None:
            right_child_aux = current.get_right_child()
            current.set_right_child(right_child_aux.get_left_child())
            right_child_aux.set_left_child(current)
        pass

    def right_rotation(self, current):
        print("Right Rotation!")
        if current.get_left_child() is not None:
            left_child_aux = current.get_left_child()
            current.set_left_child(left_child_aux.get_right_child()) 
            left_child_aux.set_right_child(current)
        pass

    def balance(self, current):
        print("Balance")
        # current is the node to start from balancing
        
        left_child = current.get_left_child()
        right_child = current.get_right_child()
        
        #Primeiro ciclo um dos ramos sempre vai ser none
        if left_child is None and right_child is None:
            current.set_height(-1)
        else:
            current.set_height(max(left_child.get_height(), right_child.get_height())+1)
        
        if (left_child.get_height() - right_child.get_height()) > 1:
            if (left_child.get_left_child().get_height() - left_child.get_right_child().get_height()) > 0:
                right_rotation(current)
            else:
                left_rotation(current)
                right_rotation(current)
        elif (left_child.get_height() - right_child.get_height()) < -1:
            if (right_child.get_left_child().get_height() - right_child.get_right_child().get_height()) < 0: 
                left_rotation(current)
            else:
                left_rotation(current)
                right_rotation(current)
        pass
                

    #DISPLAY TREE
    def display(self):
        lines, _, _, _ = self._display_aux(self.root)
        for line in lines:
            print(line)
    def _display_aux(self, current: Node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if current.get_right_child() is None and current.get_left_child() is None:
            line = '%s' % current.get_value()
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if current.get_right_child() is None:
            lines, n, p, x = self._display_aux(current.get_left_child())
            s = '%s' % current.get_value()
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if current.get_left_child() is None:
            lines, n, p, x = self._display_aux(current.get_right_child())
            s = '%s' % current.get_value()
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display_aux(current.get_left_child())
        right, m, q, y = self._display_aux(current.get_right_child())
        s = '%s' % current.get_value()
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






