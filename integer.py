# integer.py
# Integers. 

class IntegerForChild: 
    def __init__(self, val=0): 
        self.val = val
        self.n_digit = len(str(abs(val)))

    def __add__(self, b): 
        return (
                 IntegerForChild(self.val + b.val) 
                 if isinstance(b, IntegerForChild) 
                 else IntegerForChild(self.val + b)
               )

    def __neg__(self): 
        return IntegerForChild(-self.val)

    def __sub__(self, b): 
        return self + (-b)

    def __mul__(self, b): 
        return (
                 IntegerForChild(self.val * b.val) 
                 if isinstance(b, IntegerForChild) 
                 else IntegerForChild(self.val * b)
               )

    def __str__(self): 
        return str(self.val)

    def str_formula(self, n_empty_digit=0):
        return ' '.join(str(self) + ' ' * n_empty_digit)

    def digits(self): 
        if self.val < 0: 
            raise NotImplementedError('Just wait for negative numbers being supported. ')
        return [int(x) for x in str(self)]

    # TODO Add methods ==, >, <, etc. 


def gotest(): 
    val1, len1 = 3274, 4
    val2, len2 = -4010, 4
    three_spaces1 = '3 2 7 4      '
    three_spaces2 = '- 4 0 1 0      '
    summe = val1 + val2
    negged = -val1
    diff = val1 - val2
    prod = val1 * val2
    integer1 = IntegerForChild(val1)
    integer2 = IntegerForChild(val2)
    assert integer1.val == val1, (
            'IntegerForChild.__init__ val error: {} instead of {}'.format(
                  integer1.val, val1 
                )
            )
    assert integer2.val == val2, (
            'IntegerForChild.__init__ val error: {} instead of {}'.format(
                  integer2.val, val2 
                )
            )
    assert integer1.n_digit == len1, (
            'IntegerForChild.__init__ n_digit error: for {}, {} instead of {}'.format(
                  integer1.val, integer1.n_digit, len1
                )
            )
    assert integer2.n_digit == len2, (
            'IntegerForChild.__init__ n_digit error: for {}, {} instead of {}'.format(
                  integer2.val, integer2.n_digit, len2
                )
            )
    assert (integer1 + integer2).val == summe, (
            'IntergerForChild.__add__ error: {} instead of {}'.format(
                  (integer1 + integer2).val, summe
                )
            )
    assert (integer1 - integer2).val == diff, (
            'IntegerForChild.__sub__ error: {} instead of {}'.format(
                  (integer1 - integer2).val, diff
                )
            )
    assert (-integer1).val == negged, (
            'IntegerForChild.__neg__error: {} instead of {}'.format(
                  (-integer1).val, negged
                )
            )
    assert (integer1 * integer2).val == prod, (
            'IntegerForChild.__mul__ error: {} instead of {}'.format(
                  (integer1 * integer2).val, diff
                )
            )
    assert str(integer1) == str(val1), (
            'IntegerForChild.__str__ error: {} instead of {}'.format(
                  str(integer1), str(val1)
                )
            )
    assert integer1.str_formula(3) == three_spaces1, (
            'IntegerForChild.str_formula error: {} instead of {}'.format(
                  integer1.str_formula(3), three_spaces1
                )
            )
    assert integer2.str_formula(3) == three_spaces2, (
            'IntegerForChild.str_formula error: {} instead of {}'.format(
                  integer2.str_formula(3), three_spaces2
                )
            )
    return True


if __name__ == '__main__': 
    gotest()
