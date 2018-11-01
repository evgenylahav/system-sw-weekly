"""
this module generates strong random passwords
"""
import random


def password_generator(password_length: int = 32) -> str:
    """
    this function generates random strong passwords with the maximal number of symbols = max_len
    the password can contain lower case letters, upper case letters, numbers and symbols

    example:
    password_generator(16)
    -> b)%U8J7S~M
    """

    if password_length == 0:
        raise Exception('Maximal password length should be higher than 0')

    rand_ascii_codes_list = []
    for _ in range(password_length):
        rand_ascii_codes_list.append(random.randint(33, 127))

    # option 1
    # password = ''.join(chr(i) for i in rand_ascii_codes_list)

    # option 2
    password = ''.join(map(chr, rand_ascii_codes_list))

    return password


def main():
    """ main runner """
    password_length = 16
    new_password = password_generator(password_length)
    print(new_password)


if __name__ == '__main__':
    main()
