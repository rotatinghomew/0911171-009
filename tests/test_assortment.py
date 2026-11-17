import unittest

from assortment.decision import review


class AssortmentTests(unittest.TestCase):
    def test_inactive_product_is_not_presented_as_current_pair(self):
        orders = [{"order_id": "o1", "product_id": "a"}, {"order_id": "o1", "product_id": "b"}]
        result = review(orders, [{"product_id": "a", "active": True}, {"product_id": "b", "active": False}])
        self.assertEqual(result["pairs"], [])
        self.assertEqual(result["excluded_pair_count"], 1)

    def test_duplicate_lines_do_not_inflate_pair_count(self):
        orders = [{"order_id": "o1", "product_id": "a"}, {"order_id": "o1", "product_id": "a"}, {"order_id": "o1", "product_id": "b"}]
        result = review(orders, [{"product_id": "a"}, {"product_id": "b"}])
        self.assertEqual(result["pairs"][0]["orders"], 1)


if __name__ == "__main__":
    unittest.main()
