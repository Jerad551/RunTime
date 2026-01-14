# RunTime API Reference

Complete API documentation for all RunTime modules.

## Table of Contents

- [CodeFrequencyLoader](#codefrequencyloader)
- [CodeFrequencyAnalyzer](#codefrequencyanalyzer)
- [CodeFrequencyVisualizer](#codefrequencyvisualizer)
- [CLI Reference](#cli-reference)

---

## CodeFrequencyLoader

**Module**: `src.code_frequency_loader`

Handles loading and basic processing of code frequency data from CSV files.

### Class: `CodeFrequencyLoader`

```python
CodeFrequencyLoader(file_path: str = "Code frequency.csv")
```

#### Parameters
- **file_path** (str, optional): Path to the CSV file. Default: `"Code frequency.csv"`

#### Attributes
- **file_path** (str): Path to the data file
- **data** (pd.DataFrame | None): Loaded DataFrame (None until `load()` is called)

#### Methods

##### `load() -> pd.DataFrame`
Load the CSV data into a pandas DataFrame with proper datetime parsing.

**Returns**: 
- `pd.DataFrame`: DataFrame with columns `['DateTime', 'Additions', 'Deletions']`

**Raises**:
- `FileNotFoundError`: If the specified file doesn't exist
- `pd.errors.EmptyDataError`: If the CSV file is empty
- `pd.errors.ParserError`: If the CSV format is invalid

**Example**:
```python
loader = CodeFrequencyLoader()
data = loader.load()
print(data.head())
```

##### `get_summary() -> dict`
Get summary statistics from the loaded data.

**Returns**: 
- `dict`: Dictionary containing:
  - `total_additions` (int): Total lines added
  - `total_deletions` (int): Total lines deleted (absolute value)
  - `net_changes` (int): Net change (additions - deletions)
  - `start_date` (str): First date in dataset
  - `end_date` (str): Last date in dataset
  - `num_records` (int): Total number of records

**Raises**:
- `ValueError`: If data hasn't been loaded yet

**Example**:
```python
loader = CodeFrequencyLoader()
loader.load()
summary = loader.get_summary()
print(f"Total additions: {summary['total_additions']:,}")
```

##### `get_head(n: int = 10) -> pd.DataFrame`
Get the first n rows of the dataset.

**Parameters**:
- **n** (int, optional): Number of rows to return. Default: 10

**Returns**: 
- `pd.DataFrame`: First n rows of the dataset

**Example**:
```python
loader = CodeFrequencyLoader()
loader.load()
print(loader.get_head(5))
```

---

## CodeFrequencyAnalyzer

**Module**: `src.code_frequency_analyzer`

Provides advanced analysis capabilities for code frequency data.

### Class: `CodeFrequencyAnalyzer`

```python
CodeFrequencyAnalyzer(loader: CodeFrequencyLoader)
```

#### Parameters
- **loader** (CodeFrequencyLoader): Initialized loader with data

#### Attributes
- **loader** (CodeFrequencyLoader): Reference to the data loader
- **data** (pd.DataFrame): Reference to the loaded data

#### Methods

##### `get_yearly_stats() -> pd.DataFrame`
Calculate statistics grouped by year.

**Returns**: 
- `pd.DataFrame`: DataFrame with columns:
  - `Year` (int): Year
  - `Additions` (int): Total additions for the year
  - `Deletions` (int): Total deletions for the year
  - `Net_Changes` (int): Net changes for the year
  - `Num_Weeks` (int): Number of active weeks

**Example**:
```python
analyzer = CodeFrequencyAnalyzer(loader)
yearly = analyzer.get_yearly_stats()
print(yearly)
```

##### `get_monthly_stats() -> pd.DataFrame`
Calculate statistics grouped by month.

**Returns**: 
- `pd.DataFrame`: DataFrame with year, month, and statistics

**Example**:
```python
monthly = analyzer.get_monthly_stats()
print(monthly.tail())
```

##### `get_top_activity_weeks(n: int = 10) -> pd.DataFrame`
Find the weeks with the most coding activity.

**Parameters**:
- **n** (int, optional): Number of top weeks to return. Default: 10

**Returns**: 
- `pd.DataFrame`: Top n weeks sorted by total activity (additions + |deletions|)

**Example**:
```python
top_weeks = analyzer.get_top_activity_weeks(5)
print(top_weeks)
```

##### `calculate_activity_ratio() -> float`
Calculate the ratio of active weeks to total weeks in the date range.

**Returns**: 
- `float`: Activity ratio as a percentage (0-100)

**Example**:
```python
ratio = analyzer.calculate_activity_ratio()
print(f"Activity ratio: {ratio:.2f}%")
```

##### `get_churn_stats() -> dict`
Calculate code churn statistics.

**Returns**: 
- `dict`: Dictionary containing:
  - `total_churn` (int): Total lines changed (additions + |deletions|)
  - `avg_weekly_churn` (float): Average weekly churn
  - `max_weekly_churn` (int): Maximum churn in a single week
  - `weeks_with_activity` (int): Number of weeks with any activity
  - `activity_ratio` (float): Percentage of weeks with activity

**Example**:
```python
churn = analyzer.get_churn_stats()
print(f"Total churn: {churn['total_churn']:,}")
```

##### `detect_sprints(threshold_percentile: int = 75) -> pd.DataFrame`
Detect coding sprint periods based on activity threshold.

**Parameters**:
- **threshold_percentile** (int, optional): Percentile for activity threshold. Default: 75

**Returns**: 
- `pd.DataFrame`: DataFrame of sprint periods with start/end dates and stats

**Example**:
```python
sprints = analyzer.detect_sprints(threshold_percentile=80)
print(f"Found {len(sprints)} sprint periods")
```

##### `get_activity_periods() -> pd.DataFrame`
Identify all periods of significant activity.

**Returns**: 
- `pd.DataFrame`: DataFrame with activity period information

**Example**:
```python
periods = analyzer.get_activity_periods()
print(periods)
```

##### `get_productivity_trends() -> dict`
Analyze productivity trends across different time periods.

**Returns**: 
- `dict`: Dictionary with trend analysis data

**Example**:
```python
trends = analyzer.get_productivity_trends()
print(trends)
```

---

## CodeFrequencyVisualizer

**Module**: `src.code_frequency_visualizer`

Creates publication-quality visualizations of code frequency data.

### Class: `CodeFrequencyVisualizer`

```python
CodeFrequencyVisualizer(loader: CodeFrequencyLoader, style: str = 'seaborn-v0_8-darkgrid')
```

#### Parameters
- **loader** (CodeFrequencyLoader): Initialized loader with data
- **style** (str, optional): Matplotlib style. Default: `'seaborn-v0_8-darkgrid'`

#### Attributes
- **loader** (CodeFrequencyLoader): Reference to the data loader
- **data** (pd.DataFrame): Reference to the loaded data
- **style** (str): Matplotlib style being used

#### Methods

##### `plot_timeline(save_path: str = None) -> None`
Plot additions and deletions over time as a line chart.

**Parameters**:
- **save_path** (str, optional): Path to save the plot. If None, displays interactively

**Example**:
```python
visualizer = CodeFrequencyVisualizer(loader)
visualizer.plot_timeline(save_path="output/visualizations/timeline.png")
```

##### `plot_net_changes(save_path: str = None) -> None`
Plot net code changes (additions - deletions) as a bar chart.

**Parameters**:
- **save_path** (str, optional): Path to save the plot. If None, displays interactively

**Example**:
```python
visualizer.plot_net_changes(save_path="output/visualizations/net_changes.png")
```

##### `plot_yearly_summary(save_path: str = None) -> None`
Create grouped bar charts showing yearly statistics.

**Parameters**:
- **save_path** (str, optional): Path to save the plot. If None, displays interactively

**Example**:
```python
visualizer.plot_yearly_summary(save_path="output/visualizations/yearly.png")
```

##### `plot_activity_heatmap(save_path: str = None) -> None`
Generate a heatmap showing activity by month and year.

**Parameters**:
- **save_path** (str, optional): Path to save the plot. If None, displays interactively

**Example**:
```python
visualizer.plot_activity_heatmap(save_path="output/visualizations/heatmap.png")
```

##### `create_dashboard(save_dir: str = "output/visualizations") -> None`
Generate all visualizations and save them to a directory.

**Parameters**:
- **save_dir** (str, optional): Directory to save all plots. Default: `"output/visualizations"`

**Example**:
```python
visualizer = CodeFrequencyVisualizer(loader)
visualizer.create_dashboard(save_dir="my_charts")
```

---

## CLI Reference

**Module**: `src.cli`

Command-line interface for RunTime toolkit.

### Commands

#### `load`
Load and display code frequency data.

**Usage**:
```bash
python src/cli.py load [OPTIONS]
```

**Options**:
- `-f, --file <path>`: Path to CSV file (default: "Code frequency.csv")
- `--summary`: Display summary statistics
- `--head <n>`: Display first n rows (default: 10)

**Examples**:
```bash
# Show summary
python src/cli.py load --summary

# Show first 5 rows
python src/cli.py load --head 5

# Use custom file
python src/cli.py load -f data/my_data.csv --summary
```

#### `analyze`
Perform analysis on code frequency data.

**Usage**:
```bash
python src/cli.py analyze [OPTIONS]
```

**Options**:
- `-f, --file <path>`: Path to CSV file (default: "Code frequency.csv")
- `--all`: Run all analyses
- `--top <n>`: Show top n active weeks
- `--yearly`: Show yearly statistics
- `--monthly`: Show monthly statistics
- `--sprints`: Detect coding sprints
- `--churn`: Calculate churn statistics
- `--activity`: Show activity ratio
- `--trends`: Show productivity trends

**Examples**:
```bash
# Run all analyses
python src/cli.py analyze --all

# Show top 10 weeks and sprints
python src/cli.py analyze --top 10 --sprints

# Yearly and monthly breakdown
python src/cli.py analyze --yearly --monthly
```

#### `visualize`
Create visualizations of code frequency data.

**Usage**:
```bash
python src/cli.py visualize [OPTIONS]
```

**Options**:
- `-f, --file <path>`: Path to CSV file (default: "Code frequency.csv")
- `-o, --output <dir>`: Output directory (default: "output/visualizations")
- `--all`: Create all visualizations
- `--timeline`: Create timeline plot
- `--net-changes`: Create net changes plot
- `--yearly`: Create yearly summary
- `--heatmap`: Create activity heatmap

**Examples**:
```bash
# Create all visualizations
python src/cli.py visualize --all

# Create specific plots
python src/cli.py visualize --timeline --heatmap

# Custom output directory
python src/cli.py visualize --all -o charts/
```

### Global Options

- `-h, --help`: Show help message
- `--version`: Show version information

---

## Data Format Specification

### CSV Input Format

**Required Columns**:
1. **DateTime** (string): Date in format "YYYY-MM-DD"
2. **Additions** (integer): Number of lines added
3. **Deletions** (integer): Number of lines deleted (typically negative)

**Example**:
```csv
"DateTime","Additions","Deletions"
"2017-10-22",1123,-155
"2017-10-29",11,-1
"2017-11-05",543,-89
```

**Notes**:
- Deletions are typically stored as negative numbers
- Dates should be in ISO format (YYYY-MM-DD)
- Headers are required
- Quotes around values are optional but recommended

---

## Error Handling

### Common Exceptions

**FileNotFoundError**
```python
# Raised when CSV file doesn't exist
try:
    loader = CodeFrequencyLoader("missing.csv")
    loader.load()
except FileNotFoundError as e:
    print(f"File not found: {e}")
```

**ValueError**
```python
# Raised when trying to use methods before loading data
loader = CodeFrequencyLoader()
try:
    loader.get_summary()  # Data not loaded yet!
except ValueError as e:
    print(f"Error: {e}")
```

**pd.errors.ParserError**
```python
# Raised when CSV format is invalid
try:
    loader = CodeFrequencyLoader("invalid.csv")
    loader.load()
except pd.errors.ParserError as e:
    print(f"CSV parsing error: {e}")
```

---

## Type Hints

All modules use Python type hints for better code clarity:

```python
from typing import Optional
import pandas as pd

def load(self) -> pd.DataFrame: ...
def get_summary(self) -> dict: ...
def get_top_activity_weeks(self, n: int = 10) -> pd.DataFrame: ...
def plot_timeline(self, save_path: Optional[str] = None) -> None: ...
```

---

## Dependencies

### Required Packages

- **pandas** (>=2.0.0): Data manipulation and analysis
- **numpy** (>=1.24.0): Numerical computing
- **matplotlib** (>=3.7.0): Plotting and visualization
- **seaborn** (>=0.12.0): Statistical data visualization

### Development Packages

- **pytest** (>=7.4.0): Testing framework
- **black** (>=23.0.0): Code formatting
- **flake8** (>=6.0.0): Code linting

---

## Version History

**v1.0.0** (Current)
- Initial release
- Full data loading, analysis, and visualization capabilities
- CLI interface
- Comprehensive test suite

---

## See Also

- [README.md](README.md) - Project overview and documentation
- [QUICKSTART.md](QUICKSTART.md) - Quick start guide
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines
- [LICENSE.md](LICENSE.md) - License information

---

**Last Updated**: December 26, 2025
