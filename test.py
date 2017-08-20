#basic calculator interprator

#token types
INTEGER, PLUS, EOF, MINUS = "INTEGER", "PLUS", "EOF", "MINUS"

class Tokens(object):
    def __init__(self, value, type):
        self.value = value
        self.type = type
        
    def __str__(self):
        return 'Token({value},{type})'.format(value = repr(self.value), type=self.type)
    
    def __repr__(self):
        return self.__str__()
    
class Interprator(object):
    def __init__(self, text):
        self.text = text
        self.position = 0
        self.cur_token=None
        
    def error(self):
        raise Exception("Error parsing the input text")
        
    def get_next_token(self):
        text=self.text
        
        if(self.position>len(text)-1):
            return Token(None, EOF)
        
        cur_char = text[self.position]
        
        if cur_char.isdigit():
            self.position+=1
            return Token(INTEGER, int(cur_char))
            
        elif cur_char =='+':
            self.position+=1
            return Token(PLUS, cur_char)
        
        elif cur_char == '-':
            self.position+=1
            return Token(MINUS, cur_char)
            
        else:
            self.error()
        
    def consume(self,type):
        if(self.cur_token.type==type):
            self.cur_token = self.get_next_token
        else:
            self.error()
        
    def expression(self):
        self.cur_token = self.get_next_token()
        
        left = self.cur_token
        self.consume(INTEGER)
        
        op=self.cur_token
        if(op.value=='+'):
            consume(PLUS)
        elif(op.value=='-'):
            consume(MINUS)
        else:
            self.error()
        
        right=self.cur_token
        consume(INTEGER)
        
        if(op.value=='+'):
            result = left.value + right.value
        elif(op.value=='-'):
            result = left.value - right.value
        
        return result

def main():
    while True:
        try:
            string = input('interprator> ')
        except EOFError:
            break
        if not string:
            continue
        intrp = Interprator(string)
        output = intrp.expression()
        print(output)

if __name__ == '__main__':
    main()
