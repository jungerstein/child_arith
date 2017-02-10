#

from integer import IntegerForChild


tap_strings = lambda l: map(lambda x: ' ' * (max(list(map(len, l))) - len(x)) + x, l)


def print_formula_general(func, name, integer_aleph, integer_bet): 
    if (integer_aleph.val < 0 or integer_bet.val < 0): 
        raise NotImplementedError('Just wait for negative numbers being supported. ')
    string_aleph = integer_aleph.str_formula()
    string_bet   = integer_bet.str_formula()
    string_ans   = func(integer_aleph, integer_bet).str_formula()
    tap_aleph, tap_bet, tap_ans = tap_strings([string_aleph, string_bet, string_ans])
    tap_bet = name + ' ' + tap_bet
    tap_aleph, tap_bet, tap_ans = tap_strings([tap_aleph, tap_bet, tap_ans])
    separator = '-'*len(tap_ans)
    printout = '\n'.join([tap_aleph, tap_bet, separator, tap_ans])
    print(printout)


print_formula_add = lambda x, y: print_formula_general(lambda a, b: a+b, '+', x, y)
print_formula_sub = lambda x, y: print_formula_general(lambda a, b: a-b, '-', x, y)
print_formula_simple_times = lambda x, y: print_formula_general(lambda a, b: a*b, '*', x, y)


def print_formula_times(integer_aleph, integer_bet): 
    if (integer_aleph.val < 0 or integer_bet.val < 0): 
        raise NotImplementedError('Just wait for negative numbers being supported. ')
    string_aleph = integer_aleph.str_formula()
    string_bet   = integer_bet.str_formula()
    string_ans   = (integer_aleph * integer_bet).str_formula()
    tap_aleph, tap_bet, tap_ans = tap_strings([string_aleph, string_bet, string_ans])
    tap_bet = '* ' + tap_bet
    tap_aleph, tap_bet, tap_ans = tap_strings([tap_aleph, tap_bet, tap_ans])
    separator = '-'*len(tap_ans)

    bet_digits = integer_bet.digits()
    lines = [(integer_aleph * x).str_formula(i) for i, x in enumerate(bet_digits[::-1]) if not x == 0]
    tap_lines = tap_strings(lines + [separator])

    printout = '\n'.join([
          tap_aleph, 
          tap_bet, 
          separator
        ] 
        +
          tap_lines[:-1]
        +
        [
          separator, 
          tap_ans
        ])
    print(printout)


if __name__ == '__main__': 
    print_formula_add(IntegerForChild(1999), IntegerForChild(398))
    print('\n')
    print_formula_sub(IntegerForChild(1999), IntegerForChild(398))
    print('\n')
    print_formula_simple_times(IntegerForChild(1999), IntegerForChild(398))
    print('\n')
    print_formula_times(IntegerForChild(1999), IntegerForChild(398))
    print('\n')
    print_formula_times(IntegerForChild(1999), IntegerForChild(3080))
