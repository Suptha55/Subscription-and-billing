import unittest
from src.billing_engine import calculate_bill
from src.billing_engine import calculate_prorated_fee

class TestBillingEngine(unittest.TestCase):

    def test_bill_without_overage(self):
        overage, bill = calculate_bill("ACTIVE", 50, 100, 200)
        self.assertEqual(overage, 0)
        self.assertEqual(bill, 200)

    def test_bill_with_overage(self):
        overage, bill = calculate_bill("ACTIVE", 150, 100, 200)
        self.assertEqual(overage, 50)
        self.assertEqual(bill, 200 + 50*10)

    def test_suspended_subscription_billing(self):
        overage, bill = calculate_bill("SUSPENDED", 200, 100, 200)
        self.assertEqual(overage, 0)
        self.assertEqual(bill, 200)

    def test_cancelled_subscription_billing(self):
        overage, bill = calculate_bill("CANCELLED", 200, 100, 200)
        self.assertEqual(overage, 0)
        self.assertEqual(bill, 0)

    #Test cases for pro rated billing

    def test_prorated_full_month(self):
     fee = calculate_prorated_fee(310, "2024-03-01", None)
     self.assertAlmostEqual(fee, 310)

    def test_prorated_mid_month_start(self):
     fee = calculate_prorated_fee(310, "2024-03-16", None)
     expected = 310 * (16 / 31)
     self.assertAlmostEqual(fee, expected)

    def test_prorated_mid_month_end(self):
     fee = calculate_prorated_fee(310, "2024-03-01", "2024-03-10")
     expected = 310 * (10 / 31)
     self.assertAlmostEqual(fee, expected)

    def test_prorated_outside_march(self):
     fee = calculate_prorated_fee(310, "2024-04-01", None)
     self.assertEqual(fee, 0)


if __name__ == "__main__":
    unittest.main()
