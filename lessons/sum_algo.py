"""EXamples of list and loop algorithms"""

def sum_algo(xs: list[int]) -> int:
    """Summation of input list is returned"""
    # 1. Initialize total and index i to 0
    total: int = 0
    i: int = 0
    # 2. While index i is valid, i< len(xs)
    while i < len(xs):
        #   2.True) Take xs[i] and add to total
        total += xs[i]
        #   2.True) Increase i by 1, moving it to the next index
        i += 1

    #2.False) Result is stored in total variable
    return total

odds: list[int] = [1, 3, 5, 7]
odds_sum: int = sum_algo(odds)
print(odds_sum)
