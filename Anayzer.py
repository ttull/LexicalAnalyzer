INT_LIT = 10
IDENT = 11
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
MULT_OP = 23
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26
EOF = 90
LETTER = 0
DIGIT = 1
UNKNOWN = 99
next_token = -1
lexeme = []
lex_len = 0
token = -1
char_class = -1
next_char = ''
f = open('test.txt')


def get_char():
    global next_char, char_class, next_token, f
    next_char = f.read(1)
    if next_char is not None:
        if next_char.isalpha():
            char_class = LETTER
        elif next_char.isdigit():
            char_class = DIGIT
        else:
            char_class = UNKNOWN
    else:
        next_token = EOF


def get_nonblank():
    global next_char
    while next_char is ' ':
        get_char()


def lex():
    global next_token, char_class, lexeme, next_char
    lexeme = []
    get_nonblank()
    if char_class is LETTER:
        add_char()
        get_char()
        while char_class is LETTER or char_class is DIGIT:
            add_char()
            get_char()
        next_token = IDENT
    if char_class is DIGIT:
        add_char()
        get_char()
        while char_class is DIGIT:
            add_char()
            get_char()
        next_token = INT_LIT
    if char_class is UNKNOWN:
        lookup(next_char)
        get_char()
    if char_class is EOF:
        next_token = EOF
        lexeme.append('EOF')
    print("Next token is {0}, Next lexeme is {1}".format(str(next_token), lexeme))


def add_char():
    global lexeme
    lexeme.append(next_char)


def lookup(ch):
    global next_token
    if ch is '(':
        add_char()
        next_token = LEFT_PAREN
    elif ch is ')':
        add_char()
        next_token = RIGHT_PAREN
    elif ch is '+':
        add_char()
        next_token = ADD_OP
    elif ch is '-':
        add_char()
        next_token = SUB_OP
    elif ch is '*':
        add_char()
        next_token = MULT_OP
    elif ch is '/':
        add_char()
        next_token = DIV_OP
    elif ch is '=':
        add_char()
        next_token = ASSIGN_OP
    elif ch is ' ':
        return
    elif ch == ';':
        next_token = EOF
    else:
        next_token = EOF
    return next_token


def main():
    global next_token
    get_char()
    while next_token != EOF:
        lex()


if __name__ == "__main__":
    main()



