# RunTime Examples

This directory contains advanced usage examples for the RunTime toolkit.

## 📁 Files

### advanced_examples.py
Comprehensive examples demonstrating advanced analysis patterns and custom workflows.

## 🚀 Running Examples

```bash
# Run all examples
python examples/advanced_examples.py

# Run from project root
cd /workspaces/RunTime
python examples/advanced_examples.py
```

## 📚 Examples Included

### Example 1: Basic Analysis Workflow
- Load code frequency data
- Get summary statistics
- Display basic metrics

### Example 2: Sprint Detection
- Detect coding sprint periods
- Analyze sprint characteristics
- Custom sprint parameters

### Example 3: Time-Based Analysis
- Yearly productivity statistics
- Activity patterns and ratios
- Code churn metrics

### Example 4: Custom Visualization
- Create custom plots
- Moving averages
- Multi-panel visualizations

### Example 5: Filtering Analysis
- High-activity period analysis
- Recent activity filtering
- Conditional data selection

### Example 6: Comparative Analysis
- Productivity trends over time
- Period-to-period comparisons
- Growth analysis

## 💡 Usage Patterns

### Loading Data
```python
from src import CodeFrequencyLoader

loader = CodeFrequencyLoader()
data = loader.load()
```

### Running Analysis
```python
from src import CodeFrequencyAnalyzer

analyzer = CodeFrequencyAnalyzer(loader)
sprints = analyzer.detect_sprints()
yearly = analyzer.get_yearly_stats()
```

### Creating Visualizations
```python
from src import CodeFrequencyVisualizer

visualizer = CodeFrequencyVisualizer(loader)
visualizer.plot_timeline()
visualizer.create_dashboard()
```

## 🎯 Custom Analysis Tips

1. **Filter by date range**:
   ```python
   recent = data[data['DateTime'] >= '2023-01-01']
   ```

2. **Calculate custom metrics**:
   ```python
   data['NetChanges'] = data['Additions'] + data['Deletions']
   data['Churn'] = data['Additions'] + abs(data['Deletions'])
   ```

3. **Aggregate by custom periods**:
   ```python
   quarterly = data.groupby(data['DateTime'].dt.quarter)
   ```

## 📊 Output

Examples generate visualizations in `output/visualizations/`:
- `custom_analysis.png` - Custom visualization from Example 4

## 🔧 Customization

Feel free to modify the examples for your specific needs:
- Adjust time windows
- Change filtering criteria
- Create new visualizations
- Combine multiple analyses

## 📖 Further Reading

- See [README.md](../README.md) for full documentation
- Check [QUICKSTART.md](../QUICKSTART.md) for basic usage
- Explore [notebooks/exploration.ipynb](../notebooks/exploration.ipynb) for interactive analysis

## 🤝 Contributing

Have a useful example? Please add it and submit a PR! See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.
