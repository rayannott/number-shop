from enum import Enum, auto


class ReturnType(Enum):
    RANDOM_NUMS = auto() # list-of-random-numbers
    PRIME_NUM = auto() # one-random-prime-number
    CLONE = auto() # duplicate-all-nums (3, 5) -> [3, 3, 5, 5]
    ADD_ONE = auto() # return num+1
    SUBTRACT_ONE = auto() # return num+1
    DOUBLE = auto() # return num*2 % 100
    DIGITIZE = auto() # return [d for d in digits(num)] * 2
    FACTORIZE = auto() # return [p for p in all_prime_factors(num)] * 2
    SUM = auto() # sum all nums, return sum_ % 100
    CLOSEST_PRIME = auto() # returns prime p closest to num
    MULT_NUMS = auto() # returns a multiple of nums % 100
    MEAN_NUMS = auto() # returns a mean of nums rounded to closest
    SQUARE = auto()


GROUPS_BY_PAYMENT_LEN: dict[str, list[ReturnType] | list[int]] = {
    'any': 
    [
        ReturnType.RANDOM_NUMS,
        ReturnType.PRIME_NUM,
        ReturnType.CLONE,
        ReturnType.SUM,
        ReturnType.MULT_NUMS,
        ReturnType.MEAN_NUMS,
        ReturnType.SQUARE,
    ],
    'any_weights': [10, 7, 20, 7, 20, 7, 7],
    'one':
    [
        ReturnType.RANDOM_NUMS,
        ReturnType.ADD_ONE,
        ReturnType.SUBTRACT_ONE,
        ReturnType.DOUBLE,
        ReturnType.DIGITIZE,
        ReturnType.FACTORIZE,
        ReturnType.CLOSEST_PRIME,
        ReturnType.SQUARE,
    ],
    'one_weights': [10, 10, 10, 15, 20, 20, 7, 7]
}


assert len(GROUPS_BY_PAYMENT_LEN['any']) == len(GROUPS_BY_PAYMENT_LEN['any_weights']) and \
    len(GROUPS_BY_PAYMENT_LEN['one']) == len(GROUPS_BY_PAYMENT_LEN['one_weights'])
