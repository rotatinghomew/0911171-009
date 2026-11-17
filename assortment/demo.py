from .merchandising import ShelfPlanner


def main() -> None:
    planner = ShelfPlanner([{"product_id": "p1", "width": 2}, {"product_id": "p2", "width": 3}], 10)
    planner.reserve("p1", 2)
    print(planner.related_candidates([{"order_id": "o1", "product_id": "p1"}, {"order_id": "o1", "product_id": "p2"}], "p1"))
    print(planner.plan())


if __name__ == "__main__":
    main()
