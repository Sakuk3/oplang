from Node import Node

class Operator :
    def __init__(self, code: str, left_arg: bool, right_arg: bool) :
        self.code = code
        self.left_arg = left_arg
        self.right_arg = right_arg