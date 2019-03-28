from __future__ import annotations
from Constants import NodeType

class Node :
    __num = 0

    def __init__(self, node_type: NodeType, value: str = None, left_child: 'Node' = None, right_child: 'Node' = None) :
        self.node_type = node_type
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        self.num = self.__num = self.__num + 1
    
    def fill(self, child: Node) -> bool:
        if self.left_child == None :
            self.left_child = child
        elif self.left_child != None and self.left_child == None :
            self.right_child = child
        else :
            return True
        
        return False