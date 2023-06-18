class Node:
    def __init__(self, data: str) -> None:
        self.data = data
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self, node: Node) -> None:
        self.root = node

    def height(self, node: Node):
        if self.root is None:
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