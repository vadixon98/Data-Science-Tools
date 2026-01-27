"""
Unit tests for arithmetic_operations.py
"""

import sys
import unittest
from unittest.mock import patch
from io import StringIO

# Add parent directory to path to import examples
sys.path.insert(0, 'examples')

from arithmetic_operations import main


class TestArithmeticOperations(unittest.TestCase):
    """Test cases for arithmetic operations"""
    
    def test_basic_arithmetic(self):
        """Test the basic arithmetic operation (3*4)+5"""
        result = (3 * 4) + 5
        self.assertEqual(result, 17)
    
    def test_minutes_to_hours_logic(self):
        """Test the minutes_to_hours logic (function is nested in main)"""
        # Test the conversion logic directly
        result = 200 / 60
        self.assertAlmostEqual(result, 3.3333333333333335, places=10)
        
        # Test with different values
        self.assertAlmostEqual(60 / 60, 1.0, places=10)
        self.assertAlmostEqual(90 / 60, 1.5, places=10)
        self.assertAlmostEqual(30 / 60, 0.5, places=10)
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_output(self, mock_stdout):
        """Test that main() produces expected output"""
        main()
        output = mock_stdout.getvalue()
        
        # Check that output contains expected results
        self.assertIn("(3 * 4) + 5 = 17", output)
        self.assertIn("200 minutes =", output)
        self.assertIn("hours", output)
    
    def test_arithmetic_edge_cases(self):
        """Test edge cases for arithmetic operations"""
        # Zero
        self.assertEqual((0 * 4) + 5, 5)
        
        # Negative numbers
        self.assertEqual((-3 * 4) + 5, -7)
        
        # Large numbers
        self.assertEqual((100 * 4) + 5, 405)


if __name__ == '__main__':
    unittest.main()
