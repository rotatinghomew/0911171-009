def transactions(rows: list[dict]) -> list[set[str]]:
    by_order: dict[str, set[str]] = {}
    for row in rows:
        by_order.setdefault(row["order_id"], set()).add(row["product_id"])
    return [items for _, items in sorted(by_order.items())]
