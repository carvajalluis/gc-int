def is_balanced(expr):
    """ Check if a string of parenthesis is balanced correctly"""
    while '()' in expr:
        expr = expr.replace('()', '')
    return not expr


def can_jump(nums):
    """ Check if there is a valid jump path in the array"""
    n = len(nums) - 1
    for i in range(n - 1, -1, -1):
        if nums[i] + i >= n:
            n = i
    return n == 0


def nearest_power_of_two(n):
    """ Check the power of two number smaller than n"""
    nearest = 2
    result = 2
    while n > nearest:
        nearest *= 2
        if nearest >= n:
            break
        result = nearest
    return result
