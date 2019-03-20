from Node import Node, NodeType

block_open = ["(", "[", "{"]
block_close = [")", "]", "}"]
system_operators = ["+", "*", "-", "/", "print", "="]
defined_operators = {} #Contains all custom operators defined in the Oplang code
variables = {} #Contains all variables

code = ""

for line_number, line_code in enumerate(code.splitlines(), 1) :
    tokenized_code = line_code.split()
    current_node = Node(NodeType.UNKNOWN)

    for token in tokenized_code :
        if token in system_operators or token in defined_operators :
            if current_node.node_type == NodeType.UNKNOWN :
                current_node.node_type = NodeType.OPERATOR
                current_node.value = token
                
            else :
                print("Error on line " + line_number)
        else token in block_open :
