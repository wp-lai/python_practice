class BSTNode:
    """A node in Binary Search Tree."""

    def __init__(self, parent, k):
        """Create a node

        Args:
            parent: The node's parent node
            k: The key of the node
        """
        self.key = k
        self.parent = parent
        self.left = None
        self.right = None

    def find(self, k):
        """Finds and returns the node with key k from the subtree
            rooted at this node.

        Args:
            k: The key of the node we want to find.
        """
        if k == self.key:
            return self
        elif k > self.key:
            return self.left.find(k) if self.left is not None else None
        else:
            return self.right.find(k) if self.right is not None else None

    def find_min(self):
        """Finds the node with the minimum key in the subtree rooted
            at this node.

        Returns:
            The node with the minimum key.
        """
        current = self
        while current.left is not None:
            current = current.left
        return current

    def find_max(self):
        """Finds the node with the maximum key in the subtree rooted
            at this node.

        Returns:
            The ndoe with the maximum key.
        """
        current = self
        while current.right is not None:
            current = current.right
        return current

    def next_larger(self):
        """Returns the node with the next larger key (the successor)
            in the BST."""
        # find the min_key in right subtree (if it exists)
        if self.right is not None:
            return self.right.find_min()
        # else search for parent trees
        current = self
        while current.parent is not None and \
              current.parent.right is current:
            current = current.parent
        return current.parent

    def insert(self, node):
        """Inserts a node into the subtree rooted at this node.

        Args:
            node: The node to be inserted.
        """
        if node is None:
            return None

        if node.key < self.key:
            if self.left is None:
                node.parent = self
                self.left = node
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                node.parent = self
                self.right = node
            else:
                self.right.insert(node)

    def delete(self):
        """Deletes and returns this node from the BST."""
        if self.left is None or self.right is None:
            if self is self.parent.left:
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    self.parent.left.parent = self.parent
            else:
                self.parent.right = self.left or self.right
                if self.parent.right is not None:
                    self.parent.right.parent = self.parent
            return self
        else:
            s = self.next_larger()
            s.key, self.key = self.key, s.key
            return s.delete()
