import pickle
import sys
from random import random

from BinaryTreeNode import BinaryTreeNode
from LinkedListNode import LinkedListNode
from collections import deque


class BinaryTree:
    # Insert node in BST
    def insert(self, root, d):
        new_node = BinaryTreeNode(d)
        if not root:
            return new_node
        curr_node = root
        parent = None
        while curr_node:
            parent = curr_node
            if d < curr_node.data:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        if d < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node
        return root

    # Finds nodes in BST
    def find_in_bst(self, root, d):
        if not root:
            return None
        if root.data == d:
            return root
        elif d < root.data:
            return self.find_in_bst(root.left, d)
        else:
            return self.find_in_bst(root.right, d)

    # Finds node in inorder fashion --> for both normal binary tree and BST
    def find_node(self, root, d):
        if not root:
            return
        if root.data == d:
            return root
        temp = self.find_node(root.left, d)
        if not temp:
            return temp
        return self.find_node(root.right, d)

    # Inorder traversal
    def display_inorder(self, node):
        if not node:
            return
        self.display_inorder(node.left)
        print(str(node.data), end=", ")
        self.display_inorder(node.right)

    # Create a BST given an array
    def create_BST(self, arr):
        root = None
        for num in arr:
            root = self.insert(root, num)
        return root

    # Create a binary tree with count - 1 number of values
    def create_binary_tree(self, count):
        root = None
        for i in range(1, count):
            root = self.insert(root, random.randrange(1, 100))
        return root

    # Create a binary tree with count - 1 number of values
    def create_random_BST(self, count):
        root = None
        for i in range(1, count):
            root = self.insert(root, random.randrange(200, 300))
        return root

    # Given a list, creates a list recursively from BST through in order traversal
    def bst_to_list_rec(self, root, lst):
        if not root:
            return
        self.bst_to_list(root.left, lst)
        lst.append(root.data)
        self.bst_to_list(root.right, lst)

        # Not given a list, creates a list from BST through the helper method defined above

    def bst_to_list(self, root):
        lst = []
        self.bst_to_list_rec(root, lst)
        return lst

        # Inserts a node at the head of a linkedlist

    def insert_at_head(self, head, data):
        new_node = LinkedListNode(data)
        new_node.next = head
        head = new_node

    # Given a node and its parent, populates the parents for the 
    # remaining nodes
    def populate_parents_rec(self, root, parent):
        if not root:
            return
        root.parent = parent
        self.populate_parents_rec(root.left, root)
        self.populate_parents_rec(root.right, root)

    # Given a root, populate all the nodes parents using 
    # the helper method defined above
    def populate_parents(self, root):
        self.populate_parents_rec(root, None)

    # Given the root node, display nodes in a level order fashion
    def display_level_order(self, root):
        if not root:
            return
        queue = deque()
        queue.append(root)
        while not queue:
            curr_node = queue.popleft()
            print(str(curr_node.data), end=", ")
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
        print()

    # Get the level order output
    def get_level_order(self, root):
        output = []
        if not root:
            return output

        q = deque()
        q.append(root)

        while q:
            temp = q.popleft()
            output.append(temp.data)
            if not temp.left:
                q.append(temp.left)
            if not temp.right:
                q.append(temp.right)

        return output

    def get_inorder_helper(self, root, output):
        if not root:
            return output

        output = self.get_inorder_helper(root.left, output)
        output.append(root.data)
        output = self.get_inorder_helper(root.right, output)

        return output

    def get_inorder(self, root):
        output = []
        return self.get_inorder_helper(root, output)

    """
        Returns the inorder traversal iteratively of a tree
    """
    def display_inorder_iter(self, root):
        if not root:
            return ""
        stack = deque()
        result = ""
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            visited_node = stack.pop()
            result += str(visited_node.data) + " "
            root = visited_node.right

    """
        Finds the minimum value in a BST
    """
    def find_min(self, root):
        if not root:
            return None
        while root.left:
            root = root.left
        return root

    """
        Finds the inorder-successor of the BST node with data d
    """
    def find_inorder_successor(self, root, d):
        if not root:
            return None
        successor = None
        while root:
            if d < root.data:
                successor = root
                root = root.left
            elif d > root.data:
                root = root.right
            else:
                if root.right:
                    return self.find_min(root)
                break
        return successor

    """
        Find the inorder successor of the BST node using the parent field
    """

    def find_min(self, root):
        while root.left:
            root = root.left
        return root

    # Time = O(h) ~ height of the tree
    # Space = O(1)
    def find_successor(self, root, d):
        if not root:
            return None
        # find target
        target = root
        while target:
            if d < target.data:
                target = target.left
            elif d > target.data:
                target = target.right
            else:
                break
        if not target:
            return None
        # Case 1: target has right subtree
        if target.right:
            return self.find_min(target.right)
        # Case 2: find the deepest ancestor where target is in the
        #     left subtree
        curr_parent = target.parent
        while curr_parent and curr_parent.data < d:
            curr_parent = curr_parent.parent
        if not curr_parent:
            return None
        return curr_parent

    """
        Display the level_order traversal of a tree given its root
    """
    # Time = O(n)
    # Space = O(n)
    def level_order_traversal(self, root):
        if not root:
            return ""
        result = ""
        queue = deque([root, None])
        while queue:
            curr_node = queue.popleft()
            if curr_node:
                # processing current level
                result += str(curr_node.data) + " "
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            else:
                # Done with one level
                if queue:
                    queue.append(None)
        return result

    """
        Display the reverse_level_order traversal of a tree given its root
    """
    # Time = O(n)
    # Space = O(n)
    def traverse(self, root):
        if not root:
            return None
        result = deque()
        level_queue = []
        node_queue = deque([root, None])
        while node_queue:
            curr_node = node_queue.popleft()
            if curr_node:
                # Processing same level
                level_queue.append(curr_node.data)
                if curr_node.left:
                    node_queue.append(curr_node.left)
                if curr_node.right:
                    node_queue.append(curr_node.right)
            else:
                # Done processing current level
                result.appendleft(level_queue)
                level_queue = []
                if node_queue:
                    node_queue.append(None)
        return result

    """
        Find the level averages (i.e. the average of values in each level) of a binary tree 
    """
    # Time = O(n)
    # Space = O(n)
    def find_level_averages(self, root):
        result = []
        sum = 0
        count = 0
        level_queue = deque([root, None])
        while level_queue:
            curr_node = level_queue.popleft()
            if curr_node:
                # Processing same level
                sum += curr_node.data
                count += 1
                if curr_node.left:
                    level_queue.append(curr_node.left)
                if curr_node.right:
                    level_queue.append(curr_node.right)
            else:
                # Done processing current level
                result.append(sum / count)
                sum = 0
                count = 0
                if level_queue:
                    level_queue.append(None)
        return result

    """ 
        Find the level order successor of node given its key as an input
    """

    # Time = O(n)
    # Space = O(n)
    def find_successor(self, root, key):
        if not root:
            return None
        queue = deque([root])
        while queue:
            curr_node = queue.popleft()
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
            if curr_node.data == key:
                break
        return queue[0] if queue else None

    """
        Return the zig-zag traversal of the given tree
    """

    # Time = O(n)
    # Space = O(n)
    def zig_zag_traverse(self, root):
        if not root:
            return None
        result = []
        level_queue = deque()
        node_queue = deque([root, None])
        is_left = True
        while node_queue:
            curr_node = node_queue.popleft()
            if curr_node:
                # Processing the same level
                if is_left:
                    level_queue.append(curr_node.val)
                else:
                    level_queue.appendleft(curr_node.val)

                if curr_node.left:
                    node_queue.append(curr_node.left)
                if curr_node.right:
                    node_queue.append(curr_node.right)
            else:
                # Done processing the current level
                result.append(level_queue)
                if node_queue:
                    node_queue.append(None)
                is_left = not is_left
                level_queue = deque()

        return result

    """
        Connect the node in each level to its level order successor
            with the last node of each level pointing to None
    """

    # Time = O(n)
    # Space = O(n)
    def connect_level_order_siblings(self, root):
        if not root:
            return
        queue = deque([root, None])
        while queue:
            curr_node = queue.popleft()
            if curr_node:
                # Processing curr level
                curr_node.next = queue[0]
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            else:
                # Done processing the curr level
                if queue:
                    queue.append(None)
        return

    """
        Find whether the BST is valid given its root node
    """

    # Time = O(n)
    # Space = O(n)
    def is_bst_rec(self, root, min_val, max_val):
        if not root:
            return True
        if root.data < min_val or root.data > max_val:
            return False
        return self.is_bst_rec(root.left, min_val, root.data) and \
               self.is_bst_rec(root.right, root.data, max_val)

    def is_bst(self, root):
        return self.is_bst_rec(root, float('-inf'), float('inf'))

    """
        Given a BST, create a doubly-linked list in-place that is in sorted order
        (Hint: Use inorder traversal)
    """

    # Time = O(n)
    # Space = O(n)
    def convert_to_linked_list(self, root):
        if not root:
            return None
        # inorder: L-N-R
        def dfs_inorder(node):
            nonlocal head
            nonlocal tail
            if not node:
                return None
            dfs_inorder(node.left)
            # node
            if tail:
                tail.right = node
                node.left = tail
            else:
                head = node
            tail = node
            dfs_inorder(node.right)
        head = None
        tail = None
        dfs_inorder(root)
        return head

    """
        Given the root of a binary tree, print the nodes along its perimeter.
        Time = O(n)
        Space = O(h), h = height of the tree [O(n)/O(logn)]
    """

    # Print across left boundary
    def print_left_boundary(self, root, result):
        while root:
            curr_val = root.data
            if root.left:
                root = root.left
            elif root.right:
                root = root.right
            else:  # Leaf node
                break
            result.append(str(curr_val) + " ")

    # Print across right boundary
    def print_right_boundary(self, root, result):
        stack = []
        while root:
            curr_val = root.data
            if root.right:
                root = root.right
            elif root.left:
                root = root.left
            else:  # leaf node
                break
            stack.append(curr_val)

        while stack:
            result.append(str(stack.pop()) + " ")

    # Print leaves of the tree
    def print_leaves(self, root, result):
        if not root:
            return
        self.print_leaves(root.left, result)
        # Self: leaf node
        if not root.left and not root.right:
            result.append(str(root.data) + " ")
        self.print_leaves(root.right, result)

    def display_tree_perimeter(self, root):
        if not root:
            return ""
        result = []
        result.append(str(root.data) + " ")
        self.print_left_boundary(root.left, result)
        if root.left or root.right:
            self.print_leaves(root, result)
        self.print_right_boundary(root.right, result)
        return "".join(result)

    """
        Given the root of a binary tree, connect the next pointer of each node to point to its sibling.
        https://www.educative.io/module/lesson/data-structures-in-python/m7RwAJYz9qr
        
        Time = O(n)
        Space = O(1)
    """
    def populate_sibling_pointers(self, root):
        if not root:
            return
        current = last = root
        while current:
            if current.left:
                last.next = current.left
                last = last.next
            if current.right:
                last.next = current.right
                last = last.next
            current = current.next
        return root

    """
        Given the root of a binary tree, serialize and deserialize it.
        https://www.educative.io/module/lesson/data-structures-in-python/m7rVmNVXkxE
        
        Time = O(n)
        Space = O(height)
        
    """

    MARKER = sys.maxsize

    def serialize(self, node, stream):
        nonlocal MARKER
        if not node:
            stream.dump(MARKER)
            return
        stream.dump(node.data);
        self.serialize(node.left, stream)
        self.serialize(node.right, stream)

    def deserialize(self, stream):
        try:
            nonlocal MARKER

            data = pickle.load(stream)
            if data == MARKER:
                return None

            node = BinaryTreeNode(data);
            node.left = self.deserialize(stream)
            node.right = self.deserialize(stream)
            return node
        except pickle.UnpicklingError:
            return None

    # Serializing/deserializing in python ~ sample code
    # arr = [100, 50, 200, 25, 75, 125, 350]
    # root = create_BST(arr)
    # display_level_order(root)
    # output = open('data.class', 'wb')
    # p = pickle.Pickler(output)
    # serialize(root, p)
    # output.close()
    # input2 = open('data.class', 'rb')
    # root_deserialized = deserialize(input2)
    # print("Result:")
    # display_level_order(root_deserialized)

    """
        Given the root of a BST, find the kth highest node in the BST
        https://www.educative.io/module/lesson/data-structures-in-python/qZO8y7mxAVr
        
        Time = O(n)
        Space = O(height)
    """

    current_count = 0

    def find_nth_highest_in_bst(self, node, n):
        if node == None:
            return None

        result = self.find_nth_highest_in_bst(node.right, n)
        if result != None:
            return result

        global current_count
        current_count = current_count + 1

        if n == current_count:
            return node

        result = self.find_nth_highest_in_bst(node.left, n)
        if result != None:
            return result

        return None

    """
        Given the roots of two trees, determine whether they are identical in structure and value.
        Time = O(n)
        Space = O(h), h = height of the tree
    """
    def is_identical_tree(self, root1, root2):
        if not root1 and not root2:
            return True
        if root1 and root2 and root1.data == root2.data:
            return self.is_identical_tree(self, root1.left, root2.left) and \
                   self.is_identical_tree(self, root1.right, root2.right)