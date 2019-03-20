from Constants import NodeType

class Node :
    def __init__(self, node_type: NodeType, value: str = None, left_child: Node = None, right_child: Node = None, parent: Node = None) :
        self.node_type = node_type
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent
    
    @property
    def left_child(self) :
        return self.left_child
    
    @left_child.setter
    def left_child(self, left_child: Node) :
        self.left_child = left_child

        left_child.parent = self
    
    @property
    def right_child(self) :
        return self.right_child
    
    @right_child.setter
    def right_child(self, right_child: Node) :
        self.right_child = right_child

        right_child.parent = self