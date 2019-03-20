from enum import Enum

class TokenType(Enum) :
    INTEGER = 1
    PLUS = 2
    MINUS = 3
    MUL = 4
    DIV = 5
    EOF = 6

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

