def is_leap_year(year: int) -> bool:
    """
    this function checks if the input year is a leap year or not
    Examples:
    is_leap_year(2000) -> True
    is_leap_year(1000) -> False
    """
    return year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0)


def main():
    print(is_leap_year(1000))


if __name__ == '__main__':
    main()
