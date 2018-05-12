class TokenTypes:
    def __init__(self):
        pass

    NUMBER = 'NUMBER'
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

    def skip_spaces(self):
        while self.text[self.pos] == ' ':
            self.pos += 1

    def eval(self):
        a = self.get_next_token()
        self.check_type(a, TokenTypes.NUMBER)
        result = a.val
        while self.has_next_token():
            o = self.get_next_token()
            self.check_type(o, TokenTypes.SYMBOL)
            b = self.get_next_token()
            self.check_type(b, TokenTypes.NUMBER)

            if o.val == '+':
                a = Token(TokenTypes.NUMBER, a.val + b.val)
            elif o.val == '-':
                a = Token(TokenTypes.NUMBER, a.val - b.val)
            elif o.val == '*':
                a = Token(TokenTypes.NUMBER, a.val * b.val)
            elif o.val == '/':
                a = Token(TokenTypes.NUMBER, a.val / b.val)
            else:
                raise Exception('Invalid operator')
            result = a.val
        return result

    def check_type(self, current_token, required_type):
        if current_token.type == required_type:
            self.pos += len(str(current_token.val))
            return
        raise Exception('Invalid token at {}'.format(self.pos + 1))

    def has_next_token(self):
        tp1 = self.pos
        while tp1 < len(self.text) and self.text[tp1] == ' ':
            tp1 += 1
        if tp1 >= len(self.text):
            return False
        return True

    def get_next_token(self):
        if self.pos >= len(self.text):
            return Token(TokenTypes.EOT)

        if self.text[self.pos] == ' ':
            self.skip_spaces()

        if 48 <= ord(self.text[self.pos]) <= 57:
            p1 = self.pos + 1
            while p1 < len(self.text) and 48 <= ord(self.text[p1]) <= 57:
                p1 += 1
            return Token(TokenTypes.NUMBER, int(self.text[self.pos:p1]))

        elif self.text[self.pos] == '+':
            return Token(TokenTypes.SYMBOL, self.text[self.pos])

        elif self.text[self.pos] == '-':
            return Token(TokenTypes.SYMBOL, self.text[self.pos])

        elif self.text[self.pos] == '*':
            return Token(TokenTypes.SYMBOL, self.text[self.pos])

        elif self.text[self.pos] == '/':
            return Token(TokenTypes.SYMBOL, self.text[self.pos])

        else:
            raise Exception('Invalid token')


def main():
    prompt = 'bcomp > '
    while True:
        input_text = raw_input(prompt)
        if input_text != '':
            interpreter = Interpreter(input_text)
            print interpreter.eval()


if __name__ == '__main__':
    main()
