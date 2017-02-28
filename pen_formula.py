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
    tap_bet = ' ' + name + ' ' + tap_bet
    tap_aleph, tap_bet, tap_ans = tap_strings([tap_aleph, tap_bet, tap_ans])
    separator = '-'*len(tap_ans)
    printout = '\n'.join([tap_aleph, tap_bet, separator, tap_ans])
    print(printout)
    return printout


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
    tap_bet = ' * ' + tap_bet
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
    return printout


def print_formula_div(integer_aleph, integer_bet): 
    if (integer_aleph.val < 0 or integer_bet.val < 0): 
        raise NotImplementedError('Just wait for negative numbers being supported. ')
    if (integer_bet.val == 0): 
        raise ValueError('Cannot div by 0. ')
        raise NotImplementedError('Just wait for negative numbers being supported. ')
    string_aleph = integer_aleph.str_formula()
    string_bet   = integer_bet.str_formula()
    string_q     = IntegerForChild(integer_aleph.val // integer_bet.val).str_formula()
    tap_aleph, tap_ans = tap_strings([string_aleph, string_q])
    separator = '-'*len(tap_ans)
    def lines_div(aleph, bet): 
        res = []
        i_space_right = aleph.n_digit - 1
        i_digit_left = 0
        digits_aleph = aleph.digits()
        remnant = digits_aleph[0]
        def str_line_val(val, i_space_right): 
            return IntegerForChild(val).str_formula(n_empty_digit = i_space_right)
        def separator_line_for_val(val, i_space_right): 
            return '-' * (IntegerForChild(val).n_digit * 2 - 1) + ' ' * (2 * i_space_right)
        while (True): 
            if (i_space_right == 0 and remnant < bet.val): 
                res.append(str_line_val(remnant, 0))
                break
            if (remnant < bet.val): 
                remnant *= 10
                i_digit_left += 1
                i_space_right -= 1
                remnant += digits_aleph[i_digit_left]
                continue
            the_digit = remnant // bet.val
            if (res): 
                res.append(str_line_val(remnant, i_space_right))
            res.append(str_line_val(the_digit * bet.val, i_space_right))
            res.append(separator_line_for_val(remnant, i_space_right))
            remnant = remnant % bet.val
        return res
    middle_lines = lines_div(integer_aleph, integer_bet)
    line_b = integer_bet.str_formula() + ' ) ' + tap_aleph
    lines = [tap_ans, separator, line_b] + middle_lines
    tapped_lines = tap_strings(lines)
    print_out = '\n'.join(tapped_lines) 
    print(print_out)
    return(print_out)



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
    print('\n')
    print_formula_div(IntegerForChild(6303*9200850 + 1025), IntegerForChild(6303))
    print('\n')
    print_formula_div(IntegerForChild(9), IntegerForChild(5))
    print('\n')
