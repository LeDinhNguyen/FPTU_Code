class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self, node: Node) -> None:
        self.root = node

    def height(self, node: Node):
        if node is None:
            return 0
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)
            if left_height > right_height:
                return left_height + 1
            else:
                return right_height + 1
    
    def nodeLevel(self, node: Node):
        pass
    
    def levelOrder(self, node: Node):
        pass

    def inOrder(self, node: Node):
        pass

    def preOrder(self, node: Node):
        pass
    
    def postOrder(self, node: Node):
        pass

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.left = Node(6)
    b = BinaryTree(root)
    print(b.height(root))