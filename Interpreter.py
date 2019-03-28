from Node import Node, NodeType as NT
from Parser import Parser

class Interpeter :
    def walk_numeric(self, root: Node) -> int :
        if root.node_type == NT.OPERATOR :
            if root.value == "+" :
                return self.walk_numeric(root.left_child) + self.walk_numeric(root.right_child)
            elif root.value == "-" :
                return self.walk_numeric(root.left_child) - self.walk_numeric(root.right_child)
            elif root.value == "*" :
                return self.walk_numeric(root.left_child) * self.walk_numeric(root.right_child)
            elif root.value == "/" :
                return self.walk_numeric(root.left_child) / self.walk_numeric(root.right_child)
            else :
                raise Exception("What the fuck.")
        
        return root.value