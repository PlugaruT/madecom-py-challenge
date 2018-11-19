from collections import Counter

def multimax(arr: list):
    # TODO [Tudor] Improve to handle list of lists
    # TODO [Tudor] Improve to receive a kwargs with key to be used for values comparison
    if not arr:
        return []
    counts = Counter(arr)
    max_val = max(counts.keys())
    return [max_val] * counts[max_val]
