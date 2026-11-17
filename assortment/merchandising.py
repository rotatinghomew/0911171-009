from copy import deepcopy

from .decision import review


class ShelfPlanner:
    def __init__(self, catalog: list[dict], capacity: int) -> None:
        if capacity < 0:
            raise ValueError("货架容量不能为负")
        self.catalog = deepcopy(catalog)
        self.capacity = capacity
        self.reservations: dict[str, int] = {}

    def reserve(self, product_id: str, facings: int) -> None:
        products = {row["product_id"]: row for row in self.catalog if row.get("active", True)}
        if product_id not in products or facings <= 0:
            raise ValueError("只能为在售商品分配正数排面")
        proposed = {**self.reservations, product_id: facings}
        used = sum(int(products[identifier]["width"]) * count for identifier, count in proposed.items())
        if used > self.capacity:
            raise ValueError("排面占用超出货架容量")
        self.reservations = proposed

    def related_candidates(self, transactions: list[dict], anchor: str) -> list[dict]:
        results = review(transactions, self.catalog)
        pairs = [row for row in results["pairs"] if anchor in (row["left"], row["right"])]
        return sorted(pairs, key=lambda row: (-row["orders"], row["left"], row["right"]))

    def plan(self) -> dict:
        return {"capacity": self.capacity, "facings": dict(sorted(self.reservations.items()))}
