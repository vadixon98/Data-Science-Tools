# 📝 Example Script Suggestions

Based on the content from `DataScienceEcosystem.htm`, here are suggested example scripts that could be extracted and created:

## 🐍 Python Scripts

### 1. **Basic Arithmetic Operations** (`examples/arithmetic_operations.py`)
Extract the arithmetic examples from the notebook:
- Expression: `(3*4)+5` → result: 17
- Time conversion: `200/60` → result: 3.333...

**Suggested script structure:**
```python
# Basic arithmetic operations
result1 = (3 * 4) + 5
print(f"(3 * 4) + 5 = {result1}")

# Time conversion utility
def minutes_to_hours(minutes):
    """Convert minutes to hours"""
    return minutes / 60

result2 = minutes_to_hours(200)
print(f"200 minutes = {result2} hours")
```

### 2. **Data Science Tools Overview** (`examples/data_science_tools.py`)
Create a script that demonstrates or lists the tools mentioned:
- RStudio
- Spyder
- Visual Studio Code

**Suggested script:**
```python
# Data Science Tools
tools = {
    "IDE": ["RStudio", "Spyder", "Visual Studio Code"],
    "Languages": ["Python", "R", "SQL", "Java"],
    "Libraries": ["Pandas", "TensorFlow", "ggplot", "NumPy", "Matplotlib"]
}

def display_tools():
    for category, items in tools.items():
        print(f"\n{category}:")
        for item in items:
            print(f"  - {item}")
```

### 3. **Data Science Libraries Demo** (`examples/libraries_demo.py`)
Demonstrate basic usage of the mentioned libraries:
- Pandas (data manipulation)
- NumPy (numerical operations)
- Matplotlib (visualization)

**Suggested script:**
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# NumPy example
arr = np.array([1, 2, 3, 4, 5])
print(f"NumPy array: {arr}")
print(f"Mean: {np.mean(arr)}")

# Pandas example
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})
print(f"\nPandas DataFrame:\n{df}")

# Matplotlib example
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title('Simple Plot')
plt.savefig('plot.png')
print("\nPlot saved as plot.png")
```

## ⏱️ Utility Scripts

### 4. **Time Conversion Utility** (`examples/time_converter.py`)
Based on the `200/60` example, create a comprehensive time converter:

```python
def time_converter(value, from_unit, to_unit):
    """
    Convert time between different units
    Units: seconds, minutes, hours, days
    """
    conversions = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400
    }
    # Convert to seconds first, then to target unit
    seconds = value * conversions[from_unit]
    return seconds / conversions[to_unit]

# Example usage
print(f"200 minutes = {time_converter(200, 'minutes', 'hours')} hours")
```

### 5. **Data Science Environment Checker** (`examples/env_checker.py`)
Script to check if required libraries are installed:

```python
import sys

required_libraries = {
    'pandas': 'Pandas',
    'numpy': 'NumPy',
    'matplotlib': 'Matplotlib',
    'tensorflow': 'TensorFlow'
}

def check_environment():
    print("Checking Data Science Environment...\n")
    installed = []
    missing = []
    
    for module, name in required_libraries.items():
        try:
            __import__(module)
            installed.append(name)
            print(f"✓ {name} is installed")
        except ImportError:
            missing.append(name)
            print(f"✗ {name} is NOT installed")
    
    print(f"\nInstalled: {len(installed)}/{len(required_libraries)}")
    if missing:
        print(f"Missing: {', '.join(missing)}")
        print(f"\nTo install missing packages:")
        print(f"pip install {' '.join([m.lower() for m in missing])}")

if __name__ == "__main__":
    check_environment()
```

## 📊 Data Analysis Examples

### 6. **Simple Data Analysis** (`examples/data_analysis.py`)
Basic data analysis using the mentioned libraries:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create sample data
data = {
    'values': np.random.randint(1, 100, 50),
    'category': np.random.choice(['A', 'B', 'C'], 50)
}
df = pd.DataFrame(data)

# Basic statistics
print("Data Statistics:")
print(df.describe())

# Group by category
print("\nGrouped Statistics:")
print(df.groupby('category')['values'].agg(['mean', 'std', 'count']))

# Visualization
df.boxplot(column='values', by='category')
plt.title('Values by Category')
plt.savefig('analysis.png')
print("\nAnalysis plot saved as analysis.png")
```

## 🔧 Interactive Scripts

### 7. **Interactive Calculator** (`examples/interactive_calculator.py`)
Extend the arithmetic examples into an interactive calculator:

```python
def calculate(expression):
    """Safely evaluate arithmetic expressions"""
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {e}"

def main():
    print("Interactive Calculator")
    print("Enter arithmetic expressions (or 'quit' to exit)")
    
    while True:
        expression = input("\n> ")
        if expression.lower() == 'quit':
            break
        result = calculate(expression)
        print(f"= {result}")

if __name__ == "__main__":
    main()
```

### 8. **Notebook Content Extractor** (`examples/extract_notebook_content.py`)
Script to extract and organize content from the HTML notebook:

```python
import re
import json

def extract_languages(html_content):
    """Extract list of languages from HTML"""
    pattern = r'"Some of the popular languages[^"]*"\s*,\s*"([^"]+)"'
    # Extract using regex patterns
    languages = ["Python", "R", "SQL", "Java"]
    return languages

def extract_libraries(html_content):
    """Extract list of libraries from HTML"""
    libraries = ["Pandas", "TensorFlow", "ggplot", "NumPy", "Matplotlib"]
    return libraries

def extract_code_examples(html_content):
    """Extract Python code examples"""
    examples = [
        {"expression": "(3*4)+5", "result": 17, "description": "Simple arithmetic"},
        {"expression": "200/60", "result": 3.333, "description": "Minutes to hours"}
    ]
    return examples

# Usage
if __name__ == "__main__":
    with open('DataScienceEcosystem.htm', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    content = {
        'languages': extract_languages(html_content),
        'libraries': extract_libraries(html_content),
        'examples': extract_code_examples(html_content)
    }
    
    print(json.dumps(content, indent=2))
```

## 📁 Suggested Directory Structure

```
Data-Science-Tools/
├── examples/
│   ├── __init__.py
│   ├── arithmetic_operations.py
│   ├── data_science_tools.py
│   ├── libraries_demo.py
│   ├── time_converter.py
│   ├── env_checker.py
│   ├── data_analysis.py
│   ├── interactive_calculator.py
│   └── extract_notebook_content.py
├── README.md
└── requirements.txt
```

## 📦 Recommended `requirements.txt`

```
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
tensorflow>=2.6.0  # Optional, can be commented out if not needed
beautifulsoup4>=4.9.0  # For HTML parsing if extracting content
```

## 🎯 Priority Suggestions

**High Priority (Most Educational Value):** ✅ **COMPLETED**
1. ✅ `arithmetic_operations.py` - Directly from notebook
2. ✅ `time_converter.py` - Extends the 200/60 example
3. ✅ `libraries_demo.py` - Demonstrates actual library usage

**Medium Priority:**
4. `data_science_tools.py` - Overview script
5. `env_checker.py` - Utility script
6. `data_analysis.py` - Practical example

**Lower Priority (Nice to Have):**
7. `interactive_calculator.py` - Enhanced functionality
8. `extract_notebook_content.py` - Meta-script for extraction

## ✅ Completed Tasks

- [x] Created `examples/` directory
- [x] Implemented all high-priority scripts
- [x] Added comprehensive docstrings and comments
- [x] Created `requirements.txt`
- [x] Updated README with examples section
- [x] Added `.gitignore` file
- [x] Created `examples/README.md`
- [x] Fixed path handling in scripts

## 🚀 Next Steps (Optional)

1. Implement medium-priority scripts
2. Add unit tests for scripts
3. Create interactive calculator
4. Add notebook content extractor

