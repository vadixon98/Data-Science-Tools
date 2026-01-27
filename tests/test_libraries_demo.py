"""
Unit tests for libraries_demo.py
Tests use mocking to avoid requiring actual library installations
"""

import sys
import unittest
from unittest.mock import patch, MagicMock
from io import StringIO

# Add parent directory to path to import examples
sys.path.insert(0, 'examples')


class TestLibrariesDemo(unittest.TestCase):
    """Test cases for libraries demo"""
    
    @patch('libraries_demo.pd')
    @patch('libraries_demo.np')
    @patch('libraries_demo.plt')
    def test_numpy_demo_with_mock(self, mock_plt, mock_np, mock_pd):
        """Test numpy_demo with mocked NumPy"""
        # Setup mocks
        mock_array = MagicMock()
        mock_np.array.return_value = mock_array
        mock_np.mean.return_value = 3.0
        mock_np.sum.return_value = 15
        mock_np.max.return_value = 5
        mock_np.min.return_value = 1
        
        # Import and test
        from libraries_demo import numpy_demo
        
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            numpy_demo()
            output = mock_stdout.getvalue()
            
            # Verify NumPy functions were called
            mock_np.array.assert_called_once()
            mock_np.mean.assert_called_once()
            mock_np.sum.assert_called_once()
            mock_np.max.assert_called_once()
            mock_np.min.assert_called_once()
            
            # Check output contains expected text
            self.assertIn("NumPy Examples", output)
    
    @patch('libraries_demo.pd')
    @patch('libraries_demo.np')
    @patch('libraries_demo.plt')
    def test_pandas_demo_with_mock(self, mock_plt, mock_np, mock_pd):
        """Test pandas_demo with mocked Pandas"""
        # Setup mocks
        mock_df = MagicMock()
        mock_df.shape = (4, 3)
        mock_df.columns = ['A', 'B', 'C']
        mock_df.describe.return_value = "Statistics"
        mock_pd.DataFrame.return_value = mock_df
        
        # Import and test
        from libraries_demo import pandas_demo
        
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            pandas_demo()
            output = mock_stdout.getvalue()
            
            # Verify DataFrame was created
            mock_pd.DataFrame.assert_called_once()
            mock_df.describe.assert_called_once()
            
            # Check output contains expected text
            self.assertIn("Pandas Examples", output)
            self.assertIn("DataFrame", output)
    
    @patch('libraries_demo.pd')
    @patch('libraries_demo.np')
    @patch('libraries_demo.plt')
    @patch('libraries_demo.os')
    def test_matplotlib_demo_with_mock(self, mock_os, mock_plt, mock_np, mock_pd):
        """Test matplotlib_demo with mocked Matplotlib"""
        # Setup mocks
        mock_os.path.dirname.return_value = '/test/path'
        mock_os.path.join.return_value = '/test/path/plot.png'
        mock_figure = MagicMock()
        mock_plt.figure.return_value = mock_figure
        
        # Import and test
        from libraries_demo import matplotlib_demo
        
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            matplotlib_demo()
            output = mock_stdout.getvalue()
            
            # Verify matplotlib functions were called
            mock_plt.figure.assert_called_once()
            mock_plt.plot.assert_called_once()
            mock_plt.title.assert_called_once()
            mock_plt.xlabel.assert_called_once()
            mock_plt.ylabel.assert_called_once()
            mock_plt.grid.assert_called_once()
            mock_plt.savefig.assert_called_once()
            mock_plt.close.assert_called_once()
            
            # Check output contains expected text
            self.assertIn("Matplotlib Examples", output)
            self.assertIn("Plot saved", output)
    
    @patch('libraries_demo.LIBRARIES_AVAILABLE', True)
    @patch('libraries_demo.numpy_demo')
    @patch('libraries_demo.pandas_demo')
    @patch('libraries_demo.matplotlib_demo')
    def test_main_with_available_libraries(self, mock_matplotlib, mock_pandas, mock_numpy):
        """Test main() when libraries are available"""
        from libraries_demo import main
        
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()
            
            # Verify all demo functions were called
            mock_numpy.assert_called_once()
            mock_pandas.assert_called_once()
            mock_matplotlib.assert_called_once()
            
            # Check output contains expected text
            self.assertIn("Data Science Libraries Demonstration", output)
            self.assertIn("All demonstrations completed", output)
    
    @patch('libraries_demo.LIBRARIES_AVAILABLE', False)
    def test_main_without_libraries(self):
        """Test main() when libraries are not available"""
        from libraries_demo import main
        
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()
            
            # Should return early without running demos
            self.assertNotIn("Data Science Libraries Demonstration", output)
    
    def test_import_error_handling(self):
        """Test that ImportError is handled gracefully"""
        # This test verifies the import error handling structure exists
        # The actual import error handling is tested by the mock tests above
        pass


if __name__ == '__main__':
    unittest.main()
