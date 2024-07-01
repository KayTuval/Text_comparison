import unittest
from src.comparison import compare_claims


class TestComparison(unittest.TestCase):
    def test_compare_claims_identical(self):
        claim1 = "A connector section for a liquid transfer device."
        claim2 = "A connector section for a liquid transfer device."
        diff = compare_claims(claim1, claim2, debug=False)

        expected_diff = [
            ('A', 'unchanged'),
            ('connector', 'unchanged'),
            ('section', 'unchanged'),
            ('for', 'unchanged'),
            ('a', 'unchanged'),
            ('liquid', 'unchanged'),
            ('transfer', 'unchanged'),
            ('device', 'unchanged'),
            ('.', 'unchanged')
        ]

        self.assertEqual(diff, expected_diff, f"Failed test_compare_claims_identical: {diff}")


if __name__ == '__main__':
    unittest.main(failfast=True, verbosity=2)
