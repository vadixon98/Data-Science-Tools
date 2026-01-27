"""
Unit tests for time_converter.py
"""

import sys
import unittest
from unittest.mock import patch
from io import StringIO

# Add parent directory to path to import examples
sys.path.insert(0, 'examples')

from time_converter import time_converter, main


class TestTimeConverter(unittest.TestCase):
    """Test cases for time converter utility"""
    
    def test_minutes_to_hours(self):
        """Test conversion from minutes to hours"""
        result = time_converter(200, 'minutes', 'hours')
        self.assertAlmostEqual(result, 3.3333333333333335, places=10)
    
    def test_hours_to_minutes(self):
        """Test conversion from hours to minutes"""
        result = time_converter(2.5, 'hours', 'minutes')
        self.assertEqual(result, 150.0)
    
    def test_days_to_hours(self):
        """Test conversion from days to hours"""
        result = time_converter(1, 'days', 'hours')
        self.assertEqual(result, 24.0)
    
    def test_seconds_to_hours(self):
        """Test conversion from seconds to hours"""
        result = time_converter(3600, 'seconds', 'hours')
        self.assertEqual(result, 1.0)
    
    def test_minutes_to_seconds(self):
        """Test conversion from minutes to seconds"""
        result = time_converter(45, 'minutes', 'seconds')
        self.assertEqual(result, 2700.0)
    
    def test_same_unit_conversion(self):
        """Test conversion within the same unit"""
        result = time_converter(100, 'minutes', 'minutes')
        self.assertEqual(result, 100.0)
    
    def test_fractional_values(self):
        """Test conversion with fractional input values"""
        result = time_converter(0.5, 'hours', 'minutes')
        self.assertEqual(result, 30.0)
        
        result = time_converter(1.5, 'days', 'hours')
        self.assertEqual(result, 36.0)
    
    def test_zero_value(self):
        """Test conversion with zero value"""
        result = time_converter(0, 'minutes', 'hours')
        self.assertEqual(result, 0.0)
    
    def test_large_values(self):
        """Test conversion with large values"""
        result = time_converter(1000, 'minutes', 'hours')
        self.assertAlmostEqual(result, 16.666666666666668, places=10)
    
    def test_invalid_source_unit(self):
        """Test that invalid source unit raises ValueError"""
        with self.assertRaises(ValueError) as context:
            time_converter(100, 'invalid', 'hours')
        
        self.assertIn("Invalid source unit", str(context.exception))
        self.assertIn("invalid", str(context.exception))
    
    def test_invalid_target_unit(self):
        """Test that invalid target unit raises ValueError"""
        with self.assertRaises(ValueError) as context:
            time_converter(100, 'minutes', 'invalid')
        
        self.assertIn("Invalid target unit", str(context.exception))
        self.assertIn("invalid", str(context.exception))
    
    def test_error_message_contains_valid_units(self):
        """Test that error messages list valid units"""
        with self.assertRaises(ValueError) as context:
            time_converter(100, 'invalid', 'hours')
        
        error_msg = str(context.exception)
        self.assertIn('seconds', error_msg)
        self.assertIn('minutes', error_msg)
        self.assertIn('hours', error_msg)
        self.assertIn('days', error_msg)
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_output(self, mock_stdout):
        """Test that main() produces expected output"""
        main()
        output = mock_stdout.getvalue()
        
        # Check that output contains expected examples
        self.assertIn("Time Conversion Examples", output)
        self.assertIn("200 minutes =", output)
        self.assertIn("hours", output)
        self.assertIn("90 minutes =", output)
        self.assertIn("2.5 hours =", output)
        self.assertIn("1 day =", output)


if __name__ == '__main__':
    unittest.main()
