"""Kontrollerar källmärkt Cereno-data och transparent Fenja-modell."""
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
MODEL = json.loads((ROOT / "data" / "financing_model.json").read_text(encoding="utf-8"))
MILESTONES = json.loads((ROOT / "data" / "milestones.json").read_text(encoding="utf-8"))

def offset(other):
    return max(0, min(70, 70 - .5 * max(0, other - 125)))

class TestFinance(unittest.TestCase):
    def test_source_and_cash(self):
        self.assertAlmostEqual(MODEL["company"]["cash_msek"], 40.238566)
        self.assertAlmostEqual(
            MODEL["company"]["operating_cashflow_q3_msek"] +
            MODEL["company"]["investment_cashflow_q3_msek"], -57.742150
        )
        self.assertTrue(MODEL["issue"]["shares_price_known"] is False)
    def test_fenja_terms(self):
        self.assertEqual(offset(125), 70)
        self.assertEqual(offset(195), 35)
        self.assertEqual(offset(265), 0)
        self.assertEqual(offset(400), 0)
        self.assertEqual(400 - (70 - offset(400)), 330)
    def test_milestones(self):
        entries = MILESTONES["milestones"]
        self.assertGreaterEqual(len(entries), 20)
        self.assertTrue(all(m["url"].startswith("https://") for m in entries))
        cs014 = next(m for m in entries if m["title"].startswith("CS014 fas IIb"))
        self.assertEqual(cs014["originalQuarter"], "Q1 2027")
        self.assertEqual(cs014["currentQuarter"], "Q3 2027")
        self.assertEqual(cs014["delayQuarters"], 2)
        self.assertTrue(any(m["status"] == "future" and "Q4 2028" in m["date"] for m in entries))
if __name__ == "__main__":
    unittest.main()
