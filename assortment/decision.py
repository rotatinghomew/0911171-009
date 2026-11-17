from .catalog import active_products
from .rules import cooccurrence


def review(transactions_rows: list[dict], catalog_rows: list[dict], minimum: int = 1) -> dict:
    catalog = active_products(catalog_rows)
    pairs = cooccurrence(transactions_rows, minimum)
    visible = [pair for pair in pairs if pair["left"] in catalog and pair["right"] in catalog]
    return {"pairs": visible, "excluded_pair_count": len(pairs) - len(visible), "product_count": len(catalog)}
