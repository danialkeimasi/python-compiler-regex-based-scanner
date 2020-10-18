import re


class Token:
    def __init__(self, token, lexim, position):
        self.token = token
        self.lexim = lexim
        self.position = position

    def __str__(self):
        return f'{self.position}\t{self.lexim}\t{self.token}'

    def __repr__(self):
        return self.__str__()


class UnknownTokenError(Exception):
    def __init__(self, buffer, position):
        super().__init__()
        self.buffer = buffer.strip()
        self.position = position

    def __str__(self):
        return f'\nLexerError: Unknown token!\n\n▼\n{self.buffer[self.position:self.position + 30]}'


class Scanner:
    def __init__(self, rules, buffer):
        rules_list = [f'(?P<{typ}>{reg})' for typ, reg in rules]
        self.regex = re.compile('|'.join(rules_list))
        self.buffer = buffer

    def token(self):
        if self.position < len(self.buffer):
            if match := re.compile('\S').search(self.buffer, self.position):
                self.position = match.start()
            else:
                return None

            if match := self.regex.match(self.buffer, self.position):
                token = Token(token=match.lastgroup, lexim=match.group(match.lastgroup), position=self.position)
                self.position = match.end()
                return token
            else:
                raise UnknownTokenError(self.buffer, self.position)

    def tokens_generator(self):
        self.position = 0
        while token := self.token():
            yield token
