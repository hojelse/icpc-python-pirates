
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.red = True
        self.left = None
        self.right = None

    def rotate_left(self):
        root = self.right
        self.right = root.left
        root.red = self.red
        root.left = self
        self.red = True
        return root

    def rotate_right(self):
        root = self.left
        self.left = root.right
        root.red = self.red
        root.right = self
        self.red = True
        return root

    def shift_left(self):
        self.flip()
        if (self.right and self.right.left and self.right.left.red):
            self.right = self.right.rotate_right()
            self = self.rotate_left()
            self.flip()
        return self

    def shift_right(self):
        self.flip()
        if (self.left and self.left.left and self.left.left.red):
            self = self.rotate_right()
            self.flip()
        return self

    def split(self):
        self.red = True
        self.left.red = False
        self.right.red = False

    def flip(self):
        self.red = not self.red
        if self.left: self.left.red = not self.left.red
        if self.right: self.right.red = not self.right.red

    def balance(self, strict):
        if (self.right and self.right.red) and not (strict and self.left and self.left.red):
            self = self.rotate_left()
        if (self.left and self.left.red) and (self.left.left and self.left.left.red):
            self = self.rotate_right()
        if (self.left and self.left.red) and (self.right and self.right.red):
            self.split()
        return self


class TreeSet:

    def __init__(self, key=lambda x: x):
        self.root = None
        self.key = key

    def __contains__(self, value):
        return self.search(value) is not None

    def add(self, value):
        stack = [self.root]
        key = self.key(value)
        result = None

        while result is None:
            node = stack[-1]
            if node is None:
                stack.pop()
                result = Node(key, value)
            elif key <= node.key:
                stack.append(node.left)
            else:
                stack.append(node.right)

        while len(stack) > 0:
            node = stack.pop()
            if key <= node.key:
                node.left = result
            else:
                node.right = result
            result = node.balance(True)
        self.root = result
        self.root.red = False

    def search(self, value):
        stack = [self.root]
        key = self.key(value)
        while len(stack) > 0:
            node = stack.pop()
            if node is None:
                return None
            elif key < node.key:
                stack.append(node.left)
            elif key > node.key:
                stack.append(node.right)
            else:
                return node.value

    def range(self, lo, hi):
        stack = [self.root]
        lo = self.key(lo)
        hi = self.key(hi)
        results = []
        while len(stack) > 0:
            node = stack.pop()
            if node is None: 
                continue
            if lo <= node.key <= hi:
                results.append(node.value)
            if lo < node.key:
                stack.append(node.left)
            if node.key < hi:
                stack.append(node.right)
        return results

    def remove(self, value):
        if self.root is None: return None
        if not (self.root and self.root.left and self.root.left.red) and not (self.root and self.root.right and self.root.right.red):
            self.root.red = True
        self.root = self._remove(self.root, self.key(value))
        if self.root is not None:
            self.root.red = False

    def _remove(self, node, key):
        if node is None: return None
        if key < node.key:
            if not (node.left and node.left.red) and not (node.left and node.left.left and node.left.left.red):
                node = node.shift_left()
            node.left = self._remove(node.left, key)
        else:
            if node.left and node.left.red:
                node = node.rotate_right()
            if key == node.key and node.right is None:
                return None
            if not (node.right and node.right.red) and not (node.right and node.right.left and node.right.left.red):
                node = node.shift_right()
            if key == node.key:
                nxt = self._min(node.right)
                node.key = nxt.key
                node.value = nxt.value
                node.right = self._remove_min(node.right)
            else:
                node.right = self._remove(node.right, key)
        return node.balance(False)

    def min(self):
        return self._min(self.root)

    def _min(self, node):
        if node is None:
            return None 
        stack = [node]
        while len(stack) > 0:
            node = stack.pop()
            if node.left is None:
                return node
            else:
                stack.append(node.left)

    def remove_min(self):
        if not (self.root and self.root.left and self.root.left.red) and not (self.root and self.root.right and self.root.right.red):
            self.root.red = True
        self.root = self._remove_min(self.root)
        self.root.red = False

    def _remove_min(self, node):
        if node.left is None:
            return None
        if not (node.left and node.left.red) and not (node.left and node.left.left and node.left.left.red):
            node = node.shift_left()
        node.left = self._remove_min(node.left)
        return node.balance(False)

    def max(self):
        return self._max(self.root)

    def _max(self, node):
        if node is None:
            return None 
        stack = [node]
        while len(stack) > 0:
            node = stack.pop()
            if node.right is None:
                return node
            else:
                stack.append(node.right)
    
    def remove_max(self):
        if not (self.root and self.root.left and self.root.left.red) and not (self.root and self.root.right and self.root.right.red):
            self.root.red = True
        self.root = self._remove_max(self.root)
        self.root.red = False
        
    def _remove_max(self, node):
        if node.left and node.left.red:
            node = node.rotate_right()
        if node.right is None:
            return None
        if not (node.right and node.right.red) and not (node.right and node.right.left and node.right.left.red):
            node = node.shift_right()
        node.right = self._remove_max(node.right)
        return node.balance(False)