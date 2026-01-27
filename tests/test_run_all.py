"""
Unit tests for run_all.py
"""

import sys
import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
import os

# Add parent directory to path to import examples
sys.path.insert(0, 'examples')

from run_all import run_script, main


class TestRunAll(unittest.TestCase):
    """Test cases for run_all.py"""
    
    @patch('run_all.os.path.exists')
    @patch('run_all.subprocess.run')
    def test_run_script_success(self, mock_subprocess, mock_exists):
        """Test run_script when script runs successfully"""
        mock_exists.return_value = True
        mock_result = MagicMock()
        mock_result.returncode = 0
        mock_subprocess.return_value = mock_result
        
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = run_script('test_script.py')
            
            self.assertTrue(result)
            mock_subprocess.assert_called_once()
            output = mock_stdout.getvalue()
            self.assertIn("Running: test_script.py", output)
            self.assertIn("completed successfully", output)
    
    @patch('run_all.os.path.exists')
    @patch('run_all.subprocess.run')
    def test_run_script_failure(self, mock_subprocess, mock_exists):
        """Test run_script when script fails"""
        mock_exists.return_value = True
        mock_result = MagicMock()
        mock_result.returncode = 1
        mock_subprocess.return_value = mock_result
        
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = run_script('test_script.py')
            
            self.assertFalse(result)
            output = mock_stdout.getvalue()
            self.assertIn("failed with exit code", output)
    
    @patch('run_all.os.path.exists')
    def test_run_script_not_found(self, mock_exists):
        """Test run_script when script doesn't exist"""
        mock_exists.return_value = False
        
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = run_script('nonexistent_script.py')
            
            self.assertFalse(result)
            output = mock_stdout.getvalue()
            self.assertIn("Script not found", output)
    
    @patch('run_all.os.path.exists')
    @patch('run_all.subprocess.run')
    def test_run_script_exception(self, mock_subprocess, mock_exists):
        """Test run_script when subprocess raises exception"""
        mock_exists.return_value = True
        mock_subprocess.side_effect = Exception("Test exception")
        
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = run_script('test_script.py')
            
            self.assertFalse(result)
            output = mock_stdout.getvalue()
            self.assertIn("Error running", output)
    
    @patch('run_all.run_script')
    def test_main_all_success(self, mock_run_script):
        """Test main() when all scripts succeed"""
        mock_run_script.return_value = True
        
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()
            
            # Should be called 3 times (one for each script)
            self.assertEqual(mock_run_script.call_count, 3)
            self.assertIn("All scripts ran successfully", output)
            self.assertIn("Successful: 3/3", output)
    
    @patch('run_all.run_script')
    def test_main_some_failures(self, mock_run_script):
        """Test main() when some scripts fail"""
        # First succeeds, second fails, third succeeds
        mock_run_script.side_effect = [True, False, True]
        
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()
            
            self.assertIn("Successful: 2/3", output)
            self.assertIn("Failed: 1/3", output)
            self.assertIn("Some scripts failed", output)


if __name__ == '__main__':
    unittest.main()
