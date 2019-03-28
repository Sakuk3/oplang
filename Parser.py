from Lexer import Lexer
from Token import Token, TokenType as TT
from Node import Node, NodeType as NT

class Parser :
    def __init__(self, lexer: Lexer) :
        self.lexer = lexer
        self.current_token = self.lexer.next_token()
    
    def error(self) :
        raise Exception('Invalid syntax')

    def eat(self, token_type: TT) :
        if self.current_token.token_type == token_type :
            self.current_token = self.lexer.next_token()
        else :
            self.error()
    
    def factor(self) -> Node :
        token = self.current_token

        if token.token_type == TT.PAR_OPEN :
            self.eat(TT.PAR_OPEN)
            expr = self.expr() # Recursively iterate through all parentheses
            self.eat(TT.PAR_CLOSE)
            return expr 
        else :
            self.eat(TT.INTEGER)
            return Node(NT.VALUE, value=token.value)
    
    def term(self) -> Node :
        factor = self.factor() # Each term has to consist of at least one factor

        # If the first factor is followed by an operator, build a branch from bottom to top
        while self.current_token.token_type in (TT.MUL, TT.DIV) :
            token = self.current_token

            self.eat(token.token_type)
                
            factor = Node(NT.OPERATOR, value=token.value, left_child=factor, right_child=self.factor())
        
        return factor

    def expr(self) -> Node :
        term = self.term() # Each expression has to consist of at least one term

        while self.current_token.token_type in (TT.PLUS, TT.MINUS) : # Similar to term()
            token = self.current_token

            self.eat(token.token_type)

            term = Node(NT.OPERATOR, value=token.value, left_child=term, right_child=self.term())
        
        return term