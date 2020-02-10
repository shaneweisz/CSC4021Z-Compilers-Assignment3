# ------------------------------------------------------------
# Question 1 - Build a Lexer
# Shane Weisz
# WSZSHA001
# ------------------------------------------------------------

'''
Sample input:
-------------
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


def display_token_type(token):
    """
    Returns the token type formatted for required display purposes.

    e.g. "EQUALS" will return "="
    """
    if token == "EQUALS":
        return "="
    if token == "PLUS":
        return "+"
    if token == "LBRACKET":
        return "("
    if token == "RBRACKET":
        return ")"
    else:
        return token


def format_val(val):
    """
    Returns a formatted value for required display format purposes.
    Strings get single quotes surrounding them, whilst ints are left unchanged.

    e.g. "a" becomes "'a'"
    """
    if type(val) == str:
        return "'{}'".format(val)
    return val


def get_formatted_token(token):
    """
    Returns a string with the token displayed in the required format.
    e.g. ('NAME', 'a', 1, 0)
    """
    return "('{}', {}, {}, {})".format(display_token_type(token.type),
                                       format_val(token.value),
                                       token.lineno,
                                       token.lexpos)


def print_tokens(data):
    """
    Prints the tokens of a lexer for a simple adder.
    """
    lexer = build_lexer()
    lexer.input(data)

    for token in lexer:
        print(get_formatted_token(token))


def get_input():
    """
    Returns a single string with the data from the user to be passed into the lexer.
    """
    data = ''
    line = input()
    while(line != '#'):
        data += line + "\n"
        line = input()
    return data


def main():
    data = get_input()
    print_tokens(data)


if __name__ == "__main__":
    main()
