"""
This class acts as a mock counter to generate pseudo random counts
"""


class Random:
    """ Random counter mock class """
    def __init__(self, count: int = 0) -> None:
        self.count = count

    def __call__(self, bottom_range: int, up_range: int) -> int:
        self.count += 1
        return min(max(self.count, bottom_range), up_range)
