# 🧪 Unit Tests

Unit tests for the Data Science Tools example scripts.

## Running Tests

### Run all tests
```bash
python -m unittest discover tests
```

### Run specific test file
```bash
python -m unittest tests.test_arithmetic_operations
python -m unittest tests.test_time_converter
python -m unittest tests.test_libraries_demo
python -m unittest tests.test_run_all
```

### Run with verbose output
```bash
python -m unittest discover tests -v
```

## Test Coverage

- **test_arithmetic_operations.py**: Tests basic arithmetic operations
- **test_time_converter.py**: Tests time conversion utility with edge cases
- **test_libraries_demo.py**: Tests library demos using mocks (no actual libraries required)
- **test_run_all.py**: Tests the script runner utility

## Requirements

Tests use Python's built-in `unittest` module - no additional dependencies required.

For `test_libraries_demo.py`, libraries are mocked, so you don't need pandas, numpy, or matplotlib installed to run tests.
