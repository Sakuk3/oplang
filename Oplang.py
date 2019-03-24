#!/bin/python

from Lexer import Lexer
from Interpreter import Interpreter

def main() :
    while True :
        try :
            text = input('oplang> ')
        except EOFError : break

        if not text : continue

        lexer = Lexer(text)
        interpreter = Interpreter(lexer)
        result = interpreter.expr()

        print(result)

if __name__ == '__main__' :
    main()