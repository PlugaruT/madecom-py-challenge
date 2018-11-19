from collections import deque
from typing import Iterable
def multimax(items: Iterable):
    # TODO [Tudor] Improve to receive a kwargs with key to be used for values comparison
    if not items:
        return []
    items = deque(items)
    return [val for val in items if val == max(items)]
