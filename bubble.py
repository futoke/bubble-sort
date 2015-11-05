__author__ = 'ichiro'

INC, DEC = range(2)
SIGN, DIGIT, EXP, DOT, ERROR = range(5)


def input_sequence(prompt):
    input_text = input(prompt)
    strings = []
    numbers = []
    buffer = ''

    error = False

    for char in input_text:
        if char != ' ':
            buffer += char
        else:
            strings += [buffer]
            buffer = ''

    for pos, st in enumerate(strings):
        while not check_number(st):
            st = input('Invalid number "{}", please retype again: '.format(st))
        numbers += [float(st)]

    return numbers


def tokenize(checking_str):
    tokens = []
    for char in checking_str:
        if char in '0123456789':
            tokens += [DIGIT]
        elif char in 'eE':
            tokens += [EXP]
        elif char in '+-':
            tokens += [SIGN]
        elif char in ',.':
            tokens += [DOT]
        else:
            tokens += [ERROR]
    return tokens


def lexer(tokens):
    res = True
    for pos, token in enumerate(tokens):
        if token == ERROR:
            res = False
            print('[LEXER]Invalid char in position {}:"{}"\n'.format(pos, token))
    return res


def parser(tokens):
    res = True
    CNT_DOTS = 0
    CNT_EXPS = 0
    CNT_SIGN = 0
    for pos, token in enumerate(tokens):
        if pos == 0:
            if token not in (DIGIT, SIGN):
                res = False
                print('[PARSER]Invalid char in position {}:"{}"\n'.format(pos, token))
        else:
            if token == SIGN:
                CNT_SIGN += 1
                if tokens[pos-1] != EXP:
                    res = False
                    print('[PARSER]Invalid char in position {}:"{}"\n'.format(pos, token))
                if CNT_SIGN > 1:
                    res = False
                    print('[PARSER]Invalid sign in position {}\n'.format(pos))
            if token == EXP:
                CNT_EXPS += 1
                if tokens[pos-1] != DIGIT:
                    res = False
                    print('[PARSER]Invalid char in position {}:"{}"\n'.format(pos, token))
                if CNT_EXPS > 1:
                    res = False
                    print('[PARSER]Invalid exp in position {}\n'.format(pos))
            if token == DOT:
                CNT_DOTS += 1
                if tokens[pos-1] != DIGIT:
                    res = False
                    print('[PARSER]Invalid char in position {}:"{}"\n'.format(pos, token))
                if CNT_EXPS > 1:
                    res = False
                    print('[PARSER]Invalid dot in position {}\n'.format(pos))
    return res


def check_number(checking_str):
    res = True
    if checking_str == '':
        res = False
    else:
        tokens = tokenize(checking_str)
        res = lexer(tokens)
        res = parser(tokens)
    return res


def swap_with_next(seq, src) -> object:
    """This function swaps two elements of the sequence.

    :param seq: Lalalal.
    :param src: Abracadabra.
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
                if sequence[j] < sequence[j+1]:
                    swap_with_next(sequence, j)
            else:
                if sequence[j] > sequence[j+1]:
                    swap_with_next(sequence, j)
    return sequence


def main() -> object:
    seq = input_sequence('Enter the numbers splitted by spaces:\n')
    print(bubble_sort(seq, order=INC))

if __name__ == '__main__':
    main()