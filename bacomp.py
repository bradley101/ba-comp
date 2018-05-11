class TokenTypes:
    def __init__(self):
        pass

    DIGIT = 'DIGIT'
    SYMBOL = 'SYMBOL'
    EOT = 'EOT'


class Token:
    def __init__(self, token_type, val=None):
        self.type = token_type
        self.val = val


class Interpreter:
    def __init__(self, text):
        self.text = text
        self.pos = 0

    def eval(self):
        a = self.get_next_token()
        self.check_type(a, TokenTypes.DIGIT)
        o = self.get_next_token()
        self.check_type(o, TokenTypes.SYMBOL)
        b = self.get_next_token()
        self.check_type(b, TokenTypes.DIGIT)
        e = self.get_next_token()
        self.check_type(e, TokenTypes.EOT)

        if o.val == '+':
            return a.val + b.val
        else:
            raise Exception('Invalid arithmetic operator')

    def check_type(self, current_token, required_type):
        if current_token.type == required_type:
            self.pos += 1
            return
        raise Exception('Invalid token at {}'.format(self.pos + 1))

    def get_next_token(self):
        if self.pos >= len(self.text):
            return Token(TokenTypes.EOT)

        elif 48 <= ord(self.text[self.pos]) <= 57:
            return Token(TokenTypes.DIGIT, ord(self.text[self.pos]) - 48)

        elif self.text[self.pos] == '+':
            return Token(TokenTypes.SYMBOL, self.text[self.pos])


def main():
    prompt = 'bcomp > '
    while True:
        input_text = raw_input(prompt)
        if input_text != '':
            interpreter = Interpreter(input_text)
            print interpreter.eval()


if __name__ == '__main__':
    main()
