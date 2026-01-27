"""
Data Science Libraries Demo
============================
Demonstrates basic usage of the data science libraries mentioned in the notebook:
- Pandas (data manipulation)
- NumPy (numerical operations)
- Matplotlib (visualization)
"""

import sys
from typing import TYPE_CHECKING

# Check Python version
if sys.version_info < (3, 7):
    sys.exit("Error: Python 3.7+ required. Current version: {}.{}".format(
        sys.version_info.major, sys.version_info.minor
    ))

if TYPE_CHECKING:
    import pandas as pd
    import numpy as np

try:
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    LIBRARIES_AVAILABLE: bool = True
except ImportError as e:
    missing_lib = str(e).split("'")[1] if "'" in str(e) else "unknown"
    print(f"\n⚠️  Warning: Required library not installed: {missing_lib}")
    print(f"   Error details: {e}")
    print("\n💡 To fix this, run:")
    print("   pip install pandas numpy matplotlib")
    print("   or")
    print("   pip install -r ../requirements.txt\n")
    LIBRARIES_AVAILABLE: bool = False


def numpy_demo() -> None:
    """Demonstrate NumPy operations"""
    print("=" * 50)
    print("NumPy Examples")
    print("=" * 50)
    
    # Create a NumPy array
    arr: np.ndarray = np.array([1, 2, 3, 4, 5])
    print(f"NumPy array: {arr}")
    print(f"Mean: {np.mean(arr)}")
    print(f"Sum: {np.sum(arr)}")
    print(f"Max: {np.max(arr)}")
    print(f"Min: {np.min(arr)}")
    print()


def pandas_demo() -> None:
    """Demonstrate Pandas operations"""
    print("=" * 50)
    print("Pandas Examples")
    print("=" * 50)
    
    # Create a simple DataFrame
    df: pd.DataFrame = pd.DataFrame({
        'A': [1, 2, 3, 4],
        'B': [4, 5, 6, 7],
        'C': [7, 8, 9, 10]
    })
    print("Pandas DataFrame:")
    print(df)
    print(f"\nDataFrame shape: {df.shape}")
    print(f"Column names: {list(df.columns)}")
    print(f"\nBasic statistics:")
    print(df.describe())
    print()


def matplotlib_demo() -> None:
    """Demonstrate Matplotlib visualization"""
    print("=" * 50)
    print("Matplotlib Examples")
    print("=" * 50)
    
    # Create a simple plot
    x: list = [1, 2, 3, 4]
    y: list = [1, 4, 9, 16]
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, marker='o', linestyle='-', linewidth=2, markersize=8)
    plt.title('Simple Plot: y = x²', fontsize=14, fontweight='bold')
    plt.xlabel('X values', fontsize=12)
    plt.ylabel('Y values', fontsize=12)
    plt.grid(True, alpha=0.3)
    
    # Save the plot
    import os
    script_dir: str = os.path.dirname(os.path.abspath(__file__))
    output_file: str = os.path.join(script_dir, 'plot.png')
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    print(f"Plot saved as '{output_file}'")
    print("Note: Close the plot window to continue (if displayed)")
    plt.close()  # Close to avoid display issues in non-interactive environments
    print()


def main() -> None:
    """Main function to run all demonstrations"""
    if not LIBRARIES_AVAILABLE:
        return
    
    print("\n" + "=" * 50)
    print("Data Science Libraries Demonstration")
    print("=" * 50 + "\n")
    
    numpy_demo()
    pandas_demo()
    matplotlib_demo()
    
    print("=" * 50)
    print("All demonstrations completed!")
    print("=" * 50)


if __name__ == "__main__":
    main()

