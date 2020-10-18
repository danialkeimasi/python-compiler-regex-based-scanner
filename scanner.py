import re


class Token:
    """Represents an token.
    """

    def __init__(self, token_type, value, position):
        """
        Args:
            token_type (str): type of token like: "ID", "SEMICOLON".
            value (str): the actual value of token: "some_variable", ";".
            position (int): location of token in the buffer.
        """
        self.token_type = token_type
        self.value = value
        self.position = position

    def __str__(self):
        return f'{self.position}\t{self.value}\t{self.token_type}'

    def __repr__(self):
        return self.__str__()


class UnknownTokenError(Exception):
    """A custom Exception for reporting scanner error.
    """

    def __init__(self, buffer, position):
        """
        Args:
            buffer (str): we can found the error in the buffer.
            position ([type]): location of error in the buffer.
        """
        super().__init__()
        self.buffer = buffer
        self.position = position

    def __str__(self):
        return f'\nLexerError: Unknown token!\n\n▼\n{self.buffer[self.position:self.position + 30]}'


class Scanner:
    """Lexical analyzer
    """

    def __init__(self, rules, buffer):
        """
        Args:
            rules (list): a list of tuples like this [("token", "regex"),...]
            buffer (str): content that we want to scan.
        """
        rules_list = [f'(?P<{typ}>{reg})' for typ, reg in rules]
        self.regex = re.compile('|'.join(rules_list))
        self.buffer = buffer
        self.position = 0

    def token(self):
        """Get the next token that we found.

        Raises:
            UnknownTokenError: raises if find a token that not matches any rules.

        Returns:
            Token: token that we found.
        """
        if self.position < len(self.buffer):
            if match := re.compile('\S').search(self.buffer, self.position):
                self.position = match.start()
            else:
                return None

            if match := self.regex.match(self.buffer, self.position):
                token = Token(token_type=match.lastgroup, value=match.group(match.lastgroup), position=self.position)
                self.position = match.end()
                return token
            else:
                raise UnknownTokenError(self.buffer, self.position)

    def token_generator(self):
        """generates all the tokens to the end.

        Yields:
            Token: token that we found.
        """
        self.position = 0
        while token := self.token():
            yield token
