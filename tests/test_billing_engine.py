import unittest
from src.billing_engine import calculate_bill

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

if __name__ == "__main__":
    unittest.main()
