from Lexer import Lexer
from Token import Token, TokenType

class Oplang :
    def __init__(self, lexer: Lexer) :
        self.lexer = lexer
        self.current_token = self.lexer.next_token()
    
    def error(self) :
        raise Exception('Invalid syntax')

    def eat(self, token_type: TokenType) :
        if self.current_token.type == token_type :
            self.current_token = self.lexer.next_token()
        else :
            self.error()
    
    def factor(self) :
        token = self.current_token
        self.eat(TokenType.INTEGER)
        return token.value()
    
    def term(self) 