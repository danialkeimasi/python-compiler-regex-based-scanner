# Python Regex Based Scanner
an implemention of a lexical analyzer that tokenize a program using some regex rules

# Requirements
Python 3.8

# How to use
you can just put your rules in to the compiler_cli.py file and use it for yourself.
  
this is how you can compile your code using compiler_cli.py
```sh
python compiler_cli.py path/to/file
```

# Example rules
```py
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
```
