""" secret handshake module """

import math
from typing import List

CODES: List[str] = ["wink", "double blink", "close your eyes", "jump"]


def handshake(code: int) -> List[str]:
    """
    this function translates the input binary code to a list of jesters
    >>> handshake(3)
    ['wink', 'double blink']
    >>> handshake(19)
    ['double blink', 'wink']
    """
    bin_num = decimal_to_binary(code)
    secret_handshake = []

    for i in range(len(CODES)):
        if i + 1 > len(bin_num):
            break
        if bin_num[-i-1] == 1:
            secret_handshake.append(CODES[i])

    if len(bin_num) > 4 and bin_num[0] == 1:
        secret_handshake.reverse()

    return secret_handshake


def decimal_to_binary(dec_num: int) -> List[int]:
    """
    this function translates the input decimal number to its
    binary representation
    """

    if dec_num == 0:
        return [False]

    bin_num = []
    while dec_num > 0:
        bin_num.append(dec_num % 2)
        dec_num = math.floor(dec_num / 2)

    bin_num.reverse()
    return bin_num


if __name__ == '__main__':
    import doctest
    doctest.testmod()
