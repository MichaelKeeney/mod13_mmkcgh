import unittest
import datetime

def validate_chart_type(chart_type):
    return chart_type in ['1', '2']

def validate_time_series(time_series):
    return time_series in ['1', '2', '3', '4']

def validate_date(date_text):
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

class TestStockVisualizerInputs(unittest.TestCase):

    # Tests for chart type
    def test_valid_chart_type(self):
        self.assertTrue(validate_chart_type("1"))
        self.assertTrue(validate_chart_type("2"))
        self.assertFalse(validate_chart_type("3"))
        self.assertFalse(validate_chart_type("m"))

    # Tests for time series
    def test_valid_time_series(self):
        self.assertTrue(validate_time_series("1"))
        self.assertTrue(validate_time_series("2"))
        self.assertTrue(validate_time_series("3"))
        self.assertTrue(validate_time_series("4"))
        self.assertFalse(validate_time_series("5"))
        self.assertFalse(validate_time_series("m"))
    # Tests for start date
    def test_valid_start_date(self):
        self.assertTrue(validate_date("2023-01-01"))
        self.assertTrue(validate_date("2020-12-31"))
        self.assertFalse(validate_date("01-01-2023"))  
        self.assertFalse(validate_date("2023/01/01"))
        self.assertFalse(validate_date("2023-13-01")) 
        self.assertFalse(validate_date("2027-00-01"))
        
    # Tests for end date
    def test_valid_end_date(self):
        self.assertTrue(validate_date("2024-01-01"))
        self.assertTrue(validate_date("2023-12-31"))
        self.assertFalse(validate_date("01-01-2024"))  
        self.assertFalse(validate_date("2024/01/01"))  
        self.assertFalse(validate_date("2023-27-08"))  
        self.assertFalse(validate_date("2027-00-01"))
        
if __name__ == '__main__':
    unittest.main()