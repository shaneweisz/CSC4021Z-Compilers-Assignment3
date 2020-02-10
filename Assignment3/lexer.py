# ------------------------------------------------------------
# Question 1 - Build a Lexer
# Shane Weisz
# WSZSHA001
# ------------------------------------------------------------

'''
a=45
b=a+(78-a)*2
#
'''

import ply.lex as lex


def build_lexer():
    """
    Returns the ply.lex lexer for the adder.
    """
    tokens = ['NAME', 'NUMBER', 'PLUS', 'EQUALS', 'LBRACKET', 'RBRACKET']

    t_ignore = ' \t'
    t_NAME = r'[a-zA-Z_]\w*'  # \w matches any alphanumeric character (equivalent to [a-zA-Z0-9_])
    t_PLUS = r'\+'
    t_EQUALS = r'='
    t_LBRACKET = r'\('
    t_RBRACKET = r'\)'

    def t_NUMBER(t):
        r'\d+'  # \d matches any decimal digit (equivalent to [0-9])
        t.value = int(t.value)
        return t

    def t_error(t):
        print("Illegal character '{0}'".format(t.value[0]))
        t.lexer.skip(1)

    def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    return lex.lex()


def format_val(val):
    """
    Returns a formatted value for required display format purposes.
    Strings get single quotes surrounding them, whilst ints are left unchanged.

    e.g. "a" becomes "'a'"
    """
    if type(val) == str:
        return "'{}'".format(val)
    return val


def main():
    """
    Prints the tokens of a lexer for a simple adder.
    """
    data = ''
    line = input()
    while(line != '#'):
        data += line + "\n"
        line = input()

    lexer = build_lexer()
    lexer.input(data)

    for token in lexer:
        print("('{}', {}, {}, {})".format(token.type,
                                          format_val(token.value),
                                          token.lineno,
                                          token.lexpos))


if __name__ == "__main__":
    main()
