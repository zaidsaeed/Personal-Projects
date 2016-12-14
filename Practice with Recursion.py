def digit_sum(n):
    ''' (int) --> int
    This function calculate the sum of all digits of the
    given non-negative integer n.'''
    if n < 10:
        return n
    return n%10 + digit_sum(n//10)

def digital_root(n):
    ''' (int) --> int
    This function calculate the sum of all digits of the
    given non-negative integer n. It keeps repeating until the result of the
    function is a single integer.'''
    s = n
    while s > 10:
        s = digit_sum(s)
    return s
