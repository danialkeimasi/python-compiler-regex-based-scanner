from typer import Typer
from scanner import Scanner, UnknownTokenError

app = Typer()


@app.command()
def compile(file_address):
    rules = [
        ('IF_KW',          r'if'),
        ('ELSE_KW',        r'else'),
        ('FOR_KW',         r'for'),
        ('CONST_STR',      r'".*?"|\'.*?\''),
        ('CONST_NUMBER',   r'\d+'),

        ('PLUS_OP',        r'\+'),
        ('MINUS_OP',       r'\-'),
        ('MULTIPLY_OP',    r'\*'),
        ('DIVIDE_OP',      r'\/'),
        ('LP',             r'\('),
        ('LCB',            r'\{'),
        ('RP',             r'\)'),
        ('RCB',            r'\}'),

        ('EQUAL_OP',       r'=='),
        ('ASSIGNMENT_OP',  r'='),
        ('SEMICOLON',      r';'),
        ('IDENTIFIER',     r'[a-zA-Z_]\w+'),
    ]

    scanner = Scanner(rules, open(file_address, 'r').read())
    try:
        for token in scanner.token_generator():
            print(token)
    except UnknownTokenError as error:
        print(error)


if __name__ == '__main__':
    app()
