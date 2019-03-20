from enum import Enum

class NodeType(Enum) :
    VALUE = 1
    OPERATOR = 2
    UNKNOWN = 3

class VariableScope(Enum) :
    GLOBAL = 1
    OPERATOR_ARGUMENT = 2
    OPERATOR_LOCAL = 3

class Keyword :
    OPDEF = "opdef"

