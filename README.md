<div align="center">

# 🚀 Data Science Tools & Ecosystem

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=Jupyter&logoColor=white)
![Data Science](https://img.shields.io/badge/Data%20Science-FF6B6B?style=for-the-badge&logo=data&logoColor=white)

**A comprehensive collection of data science tools and ecosystem resources**

[📚 Documentation](#-overview) • [💻 Examples](#-example-scripts) • [🛠️ Quick Start](#-quick-start)

---

</div>

## 📖 Overview

This repository contains educational materials and resources about **Data Science Tools and Ecosystem**. Explore the essential tools, libraries, and frameworks that power modern data science workflows.

## ✨ Features

- 📓 **Interactive Notebook** - HTML notebook exploring data science tools
- 💻 **Example Scripts** - Ready-to-run Python scripts demonstrating key concepts
- 📚 **Educational Resources** - Tools, libraries, and ecosystem overview

## 📁 Repository Contents

```
Data-Science-Tools/
│
├── 📓 DataScienceEcosystem.htm      # Interactive HTML notebook
├── 📄 DataScienceEcosystem (1).pdf  # PDF documentation
├── 📝 README.md                      # This file
├── 📋 requirements.txt               # Python dependencies
├── 🚫 .gitignore                     # Git ignore rules
├── 📜 LICENSE                         # MIT License
├── 📚 EXAMPLE_SCRIPTS_SUGGESTIONS.md  # Future script ideas (optional)
├── 📚 IMPROVEMENTS.md                 # Improvement suggestions and status
├── 📋 CHANGELOG.md                    # Version history and changes
├── 📋 FINAL_SUGGESTIONS.md            # Optional polish suggestions
├── 📂 examples/                       # Example Python scripts
│   ├── README.md                      # Examples documentation
│   ├── __init__.py
│   ├── _version_check.py             # Version check utility
│   ├── arithmetic_operations.py      # Basic arithmetic examples
│   ├── time_converter.py             # Time conversion utility
│   ├── libraries_demo.py              # Pandas, NumPy, Matplotlib demos
│   └── run_all.py                     # Run all examples script
└── 📂 tests/                          # Unit tests
    ├── README.md                      # Test documentation
    ├── __init__.py
    ├── test_arithmetic_operations.py # Tests for arithmetic operations
    ├── test_time_converter.py        # Tests for time converter
    ├── test_libraries_demo.py        # Tests for libraries demo
    └── test_run_all.py                # Tests for run_all script
```

## 🔧 Tools Covered

- **Programming Languages**: Python, R, SQL, Java
- **Notebooks**: Jupyter, Colab, RStudio
- **Libraries**: Pandas, TensorFlow, ggplot2, NumPy, Matplotlib
- **IDEs**: RStudio, Spyder, Visual Studio Code
- **Frameworks**: Scikit-learn, TensorFlow, PyTorch
- **Visualization**: Tableau, Power BI, Plotly
- **Cloud Platforms**: AWS, Azure, GCP

## 💻 Example Scripts

Practical Python scripts extracted from the notebook:

| Script | Description | Dependencies |
|--------|-------------|--------------|
| `arithmetic_operations.py` | Basic arithmetic examples from the notebook | None |
| `time_converter.py` | Convert time between seconds, minutes, hours, days | None |
| `libraries_demo.py` | Demonstrates Pandas, NumPy, and Matplotlib | pandas, numpy, matplotlib |
| `run_all.py` | Run all examples in sequence | See individual scripts |

**Quick run:** `python examples/run_all.py` or run scripts individually.

For future script suggestions, see [EXAMPLE_SCRIPTS_SUGGESTIONS.md](EXAMPLE_SCRIPTS_SUGGESTIONS.md).

## 🚀 Quick Start

1. **Install dependencies** (required for `libraries_demo.py`, optional otherwise)
   ```bash
   pip install -r requirements.txt
   ```

2. **Explore the content**
   - Open `DataScienceEcosystem.htm` in your browser
   - Or view the PDF: `DataScienceEcosystem (1).pdf`

3. **Run example scripts**
   ```bash
   python examples/run_all.py
   ```

## 🔧 Troubleshooting

### Common Issues

**Python Version Error**
- **Problem:** Scripts show "Python 3.7+ required"
- **Solution:** Upgrade Python to 3.7 or higher. Check version with `python --version`

**Import Errors (libraries_demo.py)**
- **Problem:** `ModuleNotFoundError` for pandas, numpy, or matplotlib
- **Solution:** Install dependencies: `pip install -r requirements.txt`
- **Alternative:** Install individually: `pip install pandas numpy matplotlib`

**Permission Errors**
- **Problem:** Permission denied when running scripts
- **Solution:** Ensure you have execute permissions, or use `python examples/script_name.py`

**Plot Not Saving**
- **Problem:** `libraries_demo.py` plot doesn't save
- **Solution:** Check write permissions in the `examples/` directory

### Platform-Specific Notes

- **Windows:** Use `python` instead of `python3` in commands
- **macOS/Linux:** May need `python3` and `pip3` instead of `python` and `pip`
- **Virtual Environments:** Recommended to use a virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  pip install -r requirements.txt
  ```

## 📚 Resources

- [Jupyter Documentation](https://jupyter.org/documentation)
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
- [Data Science Tools Guide](https://www.datacamp.com/learn/data-science-tools)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [NumPy Documentation](https://numpy.org/doc/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)

## 🧪 Testing

Run unit tests to verify everything works:
```bash
# Run all tests
python -m unittest discover tests

# Run with verbose output
python -m unittest discover tests -v
```

See [tests/README.md](tests/README.md) for more details.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest new features
- 📝 Improve documentation
- 🔧 Submit pull requests

## 📋 Changelog

See [CHANGELOG.md](CHANGELOG.md) for a detailed history of changes and versions.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⭐ Show Support

If you find this repository helpful, please give it a ⭐!

---

<div align="center">

**Made with ❤️ for the data science community**

[⬆ Back to Top](#-data-science-tools--ecosystem)

</div>
