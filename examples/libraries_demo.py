"""
Data Science Libraries Demo
============================
Demonstrates basic usage of the data science libraries mentioned in the notebook:
- Pandas (data manipulation)
- NumPy (numerical operations)
- Matplotlib (visualization)
"""

try:
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    LIBRARIES_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Some libraries are not installed. {e}")
    print("Please install required packages: pip install pandas numpy matplotlib")
    LIBRARIES_AVAILABLE = False


def numpy_demo():
    """Demonstrate NumPy operations"""
    print("=" * 50)
    print("NumPy Examples")
    print("=" * 50)
    
    # Create a NumPy array
    arr = np.array([1, 2, 3, 4, 5])
    print(f"NumPy array: {arr}")
    print(f"Mean: {np.mean(arr)}")
    print(f"Sum: {np.sum(arr)}")
    print(f"Max: {np.max(arr)}")
    print(f"Min: {np.min(arr)}")
    print()


def pandas_demo():
    """Demonstrate Pandas operations"""
    print("=" * 50)
    print("Pandas Examples")
    print("=" * 50)
    
    # Create a simple DataFrame
    df = pd.DataFrame({
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


def matplotlib_demo():
    """Demonstrate Matplotlib visualization"""
    print("=" * 50)
    print("Matplotlib Examples")
    print("=" * 50)
    
    # Create a simple plot
    x = [1, 2, 3, 4]
    y = [1, 4, 9, 16]
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, marker='o', linestyle='-', linewidth=2, markersize=8)
    plt.title('Simple Plot: y = x²', fontsize=14, fontweight='bold')
    plt.xlabel('X values', fontsize=12)
    plt.ylabel('Y values', fontsize=12)
    plt.grid(True, alpha=0.3)
    
    # Save the plot
    output_file = 'examples/plot.png'
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    print(f"Plot saved as '{output_file}'")
    print("Note: Close the plot window to continue (if displayed)")
    plt.close()  # Close to avoid display issues in non-interactive environments
    print()


def main():
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

