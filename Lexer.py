from Token import Token, TokenType

class Lexer :
    def __init__(self, text: str) :
        self.text = text
        self.pos = 0
        self.current_char = self.text[0]

    def error(self) :
        raise Exception('Invalid character')
    
    def advance(self) :
        self.pos += 1

        if self.pos > len(self.text) - 1 :
            self.current_char = None
        else :
            self.current_char = self.text[self.pos]
    
    def skip_white(self) :
        while self.current_char is not None and self.current_char.isspace() :
            self.advance()
    
    def integer(self) :
        result = ''

        while self.current_char is not None and self.current_char.isdigit() :
            result += self.current_char
            self.advance()

        return int(result)

    def next_token(self) :
        while self.current_char is not None :
            if self.current_char.isspace() :
                self.skip_white()
                continue

            if self.current_char.isdigit() :
                return Token(TokenType.INTEGER, self.integer())
            
            if self.current_char == '+' :
                self.advance()
                return Token(TokenType.PLUS, '+')
            
            if self.current_char == '-' :
                self.advance()
                return Token(TokenType.MINUS, '-')
            
            if self.current_char == '*' :
                self.advance()
                return Token(TokenType.MUL, '*')
            
            if self.current_char == '/' :
                self.advance()
                return Token(TokenType.DIV, '/')
            
            if self.current_char == '(' :
                self.advance()
                return Token(TokenType.PAR_OPEN, '(')
            
            if (self.current_char == ')') :
                self.advance()
                return Token(TokenType.PAR_CLOSE, ')')
            
            self.error()
        else :
            return Token(TokenType.EOF, None)