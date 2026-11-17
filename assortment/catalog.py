def active_products(rows: list[dict]) -> dict[str, dict]:
    current: dict[str, dict] = {}
    for row in rows:
        if row.get("active", True):
            current[row["product_id"]] = row
    return current
