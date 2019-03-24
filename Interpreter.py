from Lexer import Lexer
from Token import Token, TokenType as TT
from Node import Node, NodeType as NT

class Interpreter :
    def __init__(self, lexer: Lexer) :
        self.lexer = lexer
        self.current_token = self.lexer.next_token()
        self.current_node = Node(NT.UNKNOWN)
        self.root_node = None
    
    def error(self) :
        raise Exception('Invalid syntax')

    def eat(self, token_type: TT) :
        if self.current_token.token_type == token_type :
            self.current_token = self.lexer.next_token()
        else :
            self.error()
    
    def factor(self) :
        token = self.current_token

        if token.token_type == TT.PAR_OPEN :
            self.eat(TT.PAR_OPEN)
            result = self.expr() # Recursively iterate through all parentheses
            self.eat(TT.PAR_CLOSE)
            return result 
        else :
            self.eat(TT.INTEGER)
            return token.value
    
    def term(self) :
        result = self.factor()

        while self.current_token.token_type in (TT.MUL, TT.DIV) :
            token = self.current_token

            if token.token_type == TT.MUL :
                self.eat(TT.MUL)
                result = result * self.factor()
            elif token.token_type == TT.DIV :
                self.eat(TT.DIV)
                result = result / self.factor()
        
        return result

    def expr(self) :
        result = self.term()

        while self.current_token.token_type in (TT.PLUS, TT.MINUS) :
            token = self.current_token

            if token.token_type == TT.PLUS :
                self.eat(TT.PLUS)
                result = result + self.term()
            elif token.token_type == TT.MINUS :
                self.eat(TT.MINUS)
                result = result - self.term()
        
        return result