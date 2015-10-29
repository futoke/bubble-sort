__author__ = 'ichiro'

INC, DEC = range(2)


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
            st = input('Invalid number {}, please retype again: '.format(st))
        numbers += [float(st)]

    return numbers


def check_number(checking_str):
    res = True
    if checking_str == '':
        res = False
    else:
        for char in checking_str:
            if char not in '0123456789+-eE.':
                res = False
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
    for i in range(len(sequence)):
        for j in range(len(sequence[:-1])):
            if order == DEC:
                if sequence[j] < sequence[j+1]:
                    swap_with_next(sequence, j)
            else:
                if sequence[j] > sequence[j+1]:
                    # print('seq[i] = {}, seq[j] = {}'.format(seq[i], seq[j]))
                    swap_with_next(sequence, j)
    return sequence


def main() -> object:
    seq = input_sequence('Enter the numbers splitted by spaces:\n')
    print(bubble_sort(seq, order=INC))

if __name__ == '__main__':
    main()




