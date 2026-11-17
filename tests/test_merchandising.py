import unittest

from assortment.merchandising import ShelfPlanner


class MerchandisingTests(unittest.TestCase):
    def test_space_is_checked_before_replacing_a_plan(self):
        planner = ShelfPlanner([{"product_id": "a", "width": 3}, {"product_id": "b", "width": 2}], 10)
        planner.reserve("a", 2)
        planner.reserve("b", 2)
        with self.assertRaises(ValueError):
            planner.reserve("a", 3)
        self.assertEqual(planner.plan()["facings"], {"a": 2, "b": 2})

    def test_candidates_only_use_current_catalogue_products(self):
        planner = ShelfPlanner([{"product_id": "a", "width": 1}, {"product_id": "b", "width": 1}], 5)
        transactions = [
            {"order_id": "o1", "product_id": "a"}, {"order_id": "o1", "product_id": "b"},
            {"order_id": "o2", "product_id": "a"}, {"order_id": "o2", "product_id": "retired"},
        ]
        self.assertEqual(planner.related_candidates(transactions, "a"), [{"left": "a", "right": "b", "orders": 1}])
