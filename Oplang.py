#!/bin/python

from Lexer import Lexer
from Parser import Parser
from Interpreter import Interpeter
from Node import Node

def main() :
    while True :
        try :
            text = input('oplang> ')
        except EOFError : break

        if not text : continue

        lexer = Lexer(text)
        parser = Parser(lexer)
        root_node = parser.expr()
        interpreter = Interpeter()
        result = interpreter.walk_numeric(root_node)

        print(result)

if __name__ == '__main__' :
    main()