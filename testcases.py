import unittest
from project1 import *

class TestPenguinAnalysis(unittest.TestCase):

    def test_filedic_normal(self):
        data = filedic("penguins.csv")
        self.assertIsInstance(data, list)
        self.assertIsInstance(data[0], dict)

    def test_filedic_oneline(self):
        result = filedic("one_penguin.csv")
        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], dict)

    def test_filedic_empty(self):
        result = filedic("empty.csv")
        self.assertEqual(result, [])

    def test_filedic_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            filedic("no_file.csv")


    def test_avg_general(self):
        self.assertEqual(avg([1, 2, 3]), 2.0)
        self.assertEqual(avg([10, 20, 30]), 20.0)

    def test_avg_large_numbers(self):
        self.assertEqual(avg([1000, 2000, 3000]), 2000.0)

    def test_avg_single_value(self):
        self.assertEqual(avg([100]), 100.0)

    def test_avg_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            avg([])


    def test_avg_mass_general(self):
        data = [{"species": "Adelie", "island": "Dream", "sex": "female", "body_mass_g": "3000"},{"species": "Adelie", "island": "Dream", "sex": "female", "body_mass_g": "3100"},]
        self.assertEqual(avg_mass_Fadelie_Dream(data), "The average mass is 3050.00 grams")

    def test_avg_mass_partial(self):
        data = [{"species": "Adelie", "island": "Dream", "sex": "female", "body_mass_g": "3200"},{"species": "Gentoo", "island": "Dream", "sex": "female", "body_mass_g": "3000"},]
        self.assertEqual(avg_mass_Fadelie_Dream(data), "The average mass is 3200.00 grams")

    def test_avg_mass_none(self):
        data = [{"species": "Chinstrap", "island": "Torgersen", "sex": "male", "body_mass_g": "3500"}]
        self.assertIsNone(avg_mass_Fadelie_Dream(data))

    def test_avg_mass_na_value(self):
        data = [{"species": "Adelie", "island": "Dream", "sex": "female", "body_mass_g": "NA"}]
        self.assertIsNone(avg_mass_Fadelie_Dream(data))


    def test_avg_bill_general(self):
        data = [{"bill_length_mm": "40.5", "flipper_length_mm": "200", "year": "2007"},{"bill_length_mm": "42.0", "flipper_length_mm": "210", "year": "2007"},]
        expect = "The average bill length is 41.25 millimeters, and the max flipper length is 210 millimeters."
        self.assertEqual(avg_bill_maxflip_2007(data), expect)

    def test_avg_bill_with_na(self):
        data = [{"bill_length_mm": "NA", "flipper_length_mm": "220", "year": "2007"},{"bill_length_mm": "44.5", "flipper_length_mm": "230", "year": "2007"},]
        expect = "The average bill length is 44.50 millimeters, and the max flipper length is 230 millimeters."
        self.assertEqual(avg_bill_maxflip_2007(data), expect)

    def test_avg_bill_all_na(self):
        data = [{"bill_length_mm": "NA", "flipper_length_mm": "NA", "year": "2007"}]
        self.assertIsNone(avg_bill_maxflip_2007(data))

    def test_avg_bill_empty(self):
        data = []
        self.assertIsNone(avg_bill_maxflip_2007(data))


    def test_report_general(self):
        report("test_output.txt", "avg1 test", "avg2 test")
        with open("test_output.txt") as f:
            text = f.read()
        self.assertIn("avg1 test", text)
        self.assertIn("avg2 test", text)

    def test_report_empty(self):
        report("empty_report.txt", None, None)
        with open("empty_report.txt") as f:
            text = f.read()
        self.assertIn("No data available", text)


if __name__ == "__main__":
    unittest.main()