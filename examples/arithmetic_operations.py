"""
Basic Arithmetic Operations
============================
This script demonstrates basic arithmetic operations extracted from the 
Data Science Tools and Ecosystem notebook.

Examples:
- Expression: (3*4)+5 → result: 17
- Time conversion: 200 minutes to hours
"""

import sys

# Check Python version
if sys.version_info < (3, 7):
    sys.exit("Error: Python 3.7+ required. Current version: {}.{}".format(
        sys.version_info.major, sys.version_info.minor
    ))


def main() -> None:
    """Main function to demonstrate arithmetic operations"""
    
    # Basic arithmetic operation from the notebook
    result1: int = (3 * 4) + 5
    print(f"(3 * 4) + 5 = {result1}")
    
    # Time conversion utility
    def minutes_to_hours(minutes: float) -> float:
        """Convert minutes to hours"""
        return minutes / 60
    
    result2: float = minutes_to_hours(200)
    print(f"200 minutes = {result2} hours")
    print(f"200 minutes = {result2:.2f} hours (rounded to 2 decimals)")


if __name__ == "__main__":
    main()

