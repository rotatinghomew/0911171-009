from itertools import combinations

from .baskets import transactions


def cooccurrence(rows: list[dict], minimum: int = 1) -> list[dict]:
    counts: dict[tuple[str, str], int] = {}
    for basket in transactions(rows):
        for pair in combinations(sorted(basket), 2):
            counts[pair] = counts.get(pair, 0) + 1
    return [{"left": left, "right": right, "orders": count} for (left, right), count in sorted(counts.items()) if count >= minimum]
