from itertools import groupby
from typing import Iterable


def multimax(items: Iterable, key=lambda x: x):
    if not items:
        return []
    items = sorted(items, key=key, reverse=True)
    (_, group) = next(groupby(items, key=key))
    return [value for value in group]


if __name__ == "__main__":
    print(multimax([1,2,3,4,4,4,4,4]))