# Compiler Design Course: Tokenizer

you can read the [repo in github](https://github.com/danialkeimasi/python-regex-based-scanner).

### credits

Danial Keimasi

9612358036

# Grammar

```
program -> Statements
----
Statements -> Statement; Statements | Statement;
----
Statement -> IfStatement | ID(ParamList)
----
IfStatement -> if (Exp) { Statements } | if (Exp) { Statements } else { Statements }
----
Exp -> Param BIN_LOGIC_OP Param | Param
----
ParamList -> Param, ParamList | λ
----
Param -> CONST | ID
----
CONST -> CONSTSTR | CONSTNUM
```

# How to run the program

this is how you can compile your code using compiler_cli.py

```sh
python compiler_cli.py path/to/file
```

# input/output example

- We want to tokenize this file:

random_program/main.cpp

```cpp
some_var = "hello world" * 123;

if (some_var == 2) {
    print("it's equal");
}
```

- Using this command:

```sh

└─ python compiler_cli.py random_program/main.cpp

0     some_var        IDENTIFIER
9       =       ASSIGNMENT_OP
11      "hello world"   CONST_STR
25      *       MULTIPLY_OP
27      123     CONST_NUMBER
30      ;       SEMICOLON
33      if      IF_KW
36      (       LP
37      some_var        IDENTIFIER
46      ==      EQUAL_OP
49      2       CONST_NUMBER
50      )       RP
52      {       LCB
58      print   IDENTIFIER
63      (       LP
64      "it's equal"    CONST_STR
76      )       RP
77      ;       SEMICOLON
79      }       RCB
```

# compiler_cli.py

in this file we just read the file and compile it using Scanner class that we implemented in scanner.py file.

```py
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
        ('IDENTIFIER',     r'[a-zA-Z_]\w*'),
    ]

    scanner = Scanner(rules, open(file_address, 'r').read())
    try:
        for token in scanner.token_generator():
            print(token)
    except UnknownTokenError as error:
        print(error)


if __name__ == '__main__':
    app()

```
