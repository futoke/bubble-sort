__author__ = 'ichiro'

INC, DEC = range(2)
SIGN, DIGIT, EXP, DOT, ERROR = range(5)
NAME, VALUE = range(2)
SPACES = ' \t\v'

PARER_INVALID_SYMBOL = '[PARSER] Invalid symbol in the position {}:"{}".'
PARSER_ZERO_SYMBOL = \
    PARER_INVALID_SYMBOL + \
    'The first symbol should be a sign or digit.'
PARSER_LAST_SYMBOL = \
    PARER_INVALID_SYMBOL + \
    'The last symbol should be a sign.'
PARSER_SIGN_POSITION = \
    PARER_INVALID_SYMBOL + \
    'The sign should be in the first position or after an exponent.'
PARSER_MULTIPLE_SIGN = \
    PARER_INVALID_SYMBOL + \
    'The multiple signs.\n'
PARSER_EXP_POSITION = \
    PARER_INVALID_SYMBOL + \
    'The exponent sign should be between mantissa and exponent index.'
PARSER_MULTIPLE_EXP = \
    PARER_INVALID_SYMBOL + \
    'The multiple exponent signs.'
PARSER_DOT_POSITION = \
    PARER_INVALID_SYMBOL + \
    'The dot sign should be between digits.'
PARSER_MULTIPLE_DOT = \
    PARER_INVALID_SYMBOL + \
    'The multiple dot signs.'

tokens = []
token_cnt = {DIGIT: 0, EXP: 0, DOT: 0}


def input_sequence(prompt) -> object:
    input_text = input(prompt)
    input_text_len = len(input_text)
    strings = []
    numbers = []
    buffer = ''
    i = 0
    while i < input_text_len:
        print(i)
        char = input_text[i]

        if char in SPACES:
            i += 1
            continue
        else:
            buffer += char

        if (i == (input_text_len - 1)) or (input_text[i + 1] in SPACES):
            strings += [buffer]
            buffer = ''
        i += 1
    for pos, st in enumerate(strings):
        while not check_number(st):
            st = input('Invalid number "{}", please retype again: '.format(st))
    numbers += [float(st)]
    return numbers


def tokenize(checking_str):
    global tokens

    for char in checking_str:
        if char in '0123456789':
            tokens += [{
                NAME : DIGIT,
                VALUE: char
            }]
        elif char in 'eE':
            tokens += [{
                NAME : EXP,
                VALUE: char
            }]
        elif char in '+-':
            tokens += [{
                NAME : SIGN,
                VALUE: char
            }]
        elif char in ',.':
            tokens += [{
                NAME : DOT,
                VALUE: char
            }]
        else:
            tokens += [{
                NAME : ERROR,
                VALUE: char
            }]


def lexer():
    res = True

    for pos, token in enumerate(tokens):
        if token[NAME] == ERROR:
            res = False
            print(
                '[LEXER]Invalid char in position {}:"{}"\n'.format(pos,
                                                                   token[
                                                                       VALUE]))
    return res


def print_err(error, pos):
    print(error.format(pos, tokens[pos][VALUE]))


def check_token(pos, before, after, error):
    if ((tokens[pos-1][NAME] not in before) or
            (tokens[pos+1][NAME] not in after)):
        print(tokens[pos-1][VALUE], tokens[pos+1][VALUE])
        print_err(error, pos)
        return False
    else:
        return True


def check_token_cnt(pos, error):
    global token_cnt

    token = tokens[pos][NAME]
    token_cnt[token] += 1

    if token_cnt[token] > 1:
        print_err(error, pos)
        return False
    else:
        return True


def parser():
    res = True
    pos = 0

    while pos < len(tokens):
        token = tokens[pos][NAME]
        if pos == 0:
            if token not in (DIGIT, SIGN):
                res = False
                print_err(PARSER_ZERO_SYMBOL, pos)

        elif pos == (len(tokens) - 1):
            if token != DIGIT:
                print_err(PARSER_LAST_SYMBOL, pos)

        else:
            if token == SIGN:
                res = (
                    check_token(
                            pos,
                            (EXP,),
                            (DIGIT,),
                            PARSER_SIGN_POSITION
                    ) and
                    check_token_cnt(
                            pos,
                            PARSER_MULTIPLE_SIGN
                    )
                )
            if token == EXP:
                res = (
                    check_token(
                            pos,
                            (DIGIT,),
                            (DIGIT,),
                            PARSER_EXP_POSITION
                    ) and
                    check_token_cnt(
                            pos,
                            PARSER_MULTIPLE_EXP
                    )
                )
            if token == DOT:
                res = (check_token(pos, (DIGIT,), (DIGIT,),
                                   PARSER_DOT_POSITION)
                                   and
                       check_token_cnt(pos, PARSER_MULTIPLE_DOT))
        pos += 1
    return res


def check_number(checking_str):
    """

    :param checking_str:
    :return:
    """
    res = True

    if checking_str == '':
        res = False
    else:
        tokenize(checking_str)
        # res = lexer() and parser()
        res = parser()

    return res


def swap_with_next(seq, src) -> object:
    """This function swaps two elements of the sequence.

    :rtype: object
    :param seq:
    :param src:
    """
    seq[src], seq[src + 1] = seq[src + 1], seq[src]


def bubble_sort(sequence, order=INC):
    """

    :param sequence:
    :param order:
    :return:
    """
    for _ in range(len(sequence)):
        for j in range(len(sequence[:-1])):
            if order == DEC:
                if sequence[j] < sequence[j + 1]:
                    swap_with_next(sequence, j)
            else:
                if sequence[j] > sequence[j + 1]:
                    swap_with_next(sequence, j)
    return sequence


def main() -> object:
    # seq = input_sequence('Enter the numbers split by spaces:\n')
    # print(bubble_sort(seq, order=INC))
    """

    """
    print(token_cnt)
    print(check_number("3e84"))


if __name__ == '__main__':
    main()
