# RunTime Quick Start Guide

Welcome to RunTime! This guide will get you up and running in minutes.

## 🚀 Installation

```bash
# Clone the repository (if applicable)
git clone <your-repo-url>
cd RunTime

# Install dependencies
pip install -r requirements.txt
```

## 📊 Quick Commands

### 1. Load Your Data
```bash
# View summary statistics
python src/cli.py load --summary

# See first 10 rows
python src/cli.py load --head 10
```

### 2. Analyze Code Patterns
```bash
# Complete analysis (recommended)
python src/cli.py analyze --all

# Specific analyses
python src/cli.py analyze --top 10      # Top 10 active weeks
python src/cli.py analyze --sprints     # Detect coding sprints
python src/cli.py analyze --yearly      # Yearly breakdown
python src/cli.py analyze --churn       # Churn statistics
```

### 3. Create Visualizations
```bash
# Create all visualizations (recommended)
python src/cli.py visualize --all

# Specific plots
python src/cli.py visualize --timeline
python src/cli.py visualize --heatmap
python src/cli.py visualize --yearly
```

## 🎯 Common Use Cases

### Daily Development Insights
```bash
# Morning routine: check yesterday's stats
python src/code_frequency_loader.py
```

### Weekly Review
```bash
# Analyze the week's productivity
python src/cli.py analyze --top 5 --activity
```

### Project Report
```bash
# Generate comprehensive report
python src/cli.py analyze --all > report.txt
python src/cli.py visualize --all
```

## 📁 Output Files

Visualizations are saved to `output/visualizations/`:
- **timeline.png** - Complete history of additions/deletions
- **net_changes.png** - Net code changes over time
- **yearly_summary.png** - Yearly comparison charts
- **activity_heatmap.png** - Monthly activity heatmap

## 🧪 Testing

```bash
# Run all tests
pytest

# With verbose output
pytest -v

# With coverage report
pytest --cov=src tests/
```

## 💡 Tips

1. **Custom CSV File**: Use `-f` flag to specify a different file
   ```bash
   python src/cli.py load -f my_data.csv --summary
   ```

2. **Change Output Directory**: Use `-o` flag
   ```bash
   python src/cli.py visualize --all -o my_charts/
   ```

3. **Combine Options**: Most flags can be combined
   ```bash
   python src/cli.py analyze --top 10 --sprints --yearly
   ```

## 🔧 Direct Python Usage

```python
# In your own scripts
from src import CodeFrequencyLoader, CodeFrequencyAnalyzer

loader = CodeFrequencyLoader()
data = loader.load()
summary = loader.get_summary()

analyzer = CodeFrequencyAnalyzer(loader)
sprints = analyzer.detect_sprints()
yearly = analyzer.get_yearly_stats()
```

## 📚 Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check [tests/test_load.py](tests/test_load.py) for usage examples
- Explore the source code in `src/` directory

## ❓ Getting Help

```bash
# Command help
python src/cli.py --help
python src/cli.py load --help
python src/cli.py analyze --help
python src/cli.py visualize --help
```

## 🎉 Example Session

```bash
# 1. Check your data
$ python src/cli.py load --summary
✅ Successfully loaded 427 records
Date range: 2017-10-22 to 2025-12-21

# 2. Analyze patterns
$ python src/cli.py analyze --top 5
🏆 Top 5 Most Active Weeks:
...

# 3. Generate charts
$ python src/cli.py visualize --all
Creating complete dashboard...
✅ All visualizations saved to output/visualizations/
```

Happy analyzing! 🎯
