# RunTime Contributing Guide

Thank you for considering contributing to RunTime! This document provides guidelines and instructions for contributing.

## 🚀 Getting Started

1. **Fork the repository**
   ```bash
   gh repo fork Jerad551/RunTime
   ```

2. **Clone your fork**
   ```bash
   git clone git@github.com:YOUR_USERNAME/RunTime.git
   cd RunTime
   ```

3. **Set up development environment**
   ```bash
   bash setup.sh
   ```

## 🔧 Development Setup

### Install Development Dependencies
```bash
pip install -r requirements.txt
pip install black flake8  # Code formatting and linting
```

### Run Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src tests/

# Run specific test file
pytest tests/test_load.py -v
```

### Code Formatting
```bash
# Format code
black src/ tests/

# Check formatting
black --check src/ tests/

# Lint code
flake8 src/ tests/
```

## 📝 Contributing Guidelines

### Code Style
- Follow PEP 8 style guide
- Use type hints where applicable
- Write comprehensive docstrings
- Keep functions focused and small
- Use descriptive variable names

### Testing
- Write tests for new features
- Maintain 100% test coverage for core functions
- Test edge cases and error conditions
- Use pytest fixtures for common setups

### Commit Messages
Follow conventional commit format:
```
type(scope): description

[optional body]

[optional footer]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `test`: Test additions/changes
- `refactor`: Code refactoring
- `style`: Code style changes
- `chore`: Build/tooling changes

Examples:
```bash
git commit -m "feat(analyzer): add quarterly statistics method"
git commit -m "fix(loader): handle missing CSV columns gracefully"
git commit -m "docs(readme): update installation instructions"
```

### Pull Request Process

1. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write code
   - Add tests
   - Update documentation

3. **Verify everything works**
   ```bash
   pytest
   python src/cli.py analyze --all
   ```

4. **Commit and push**
   ```bash
   git add .
   git commit -m "feat: your feature description"
   git push origin feature/your-feature-name
   ```

5. **Create Pull Request**
   - Use a clear title
   - Describe what changed and why
   - Reference related issues
   - Include screenshots for UI changes

## 🎯 Areas for Contribution

### High Priority
- [ ] Web dashboard (Streamlit/Dash)
- [ ] Export reports to PDF/HTML
- [ ] Additional statistical analyses
- [ ] Performance optimizations
- [ ] Docker containerization

### Medium Priority
- [ ] Multi-repository comparison
- [ ] Custom date range filtering
- [ ] Interactive visualizations
- [ ] Configuration file support
- [ ] More test coverage

### Documentation
- [ ] API documentation
- [ ] Video tutorials
- [ ] Blog posts
- [ ] Usage examples
- [ ] Translation to other languages

## 🐛 Reporting Bugs

Create an issue with:
- Clear title and description
- Steps to reproduce
- Expected vs actual behavior
- Environment details (Python version, OS)
- Relevant error messages/logs

## 💡 Suggesting Features

Create an issue with:
- Clear description of the feature
- Use cases and benefits
- Possible implementation approach
- Examples from other tools (if applicable)

## 📚 Documentation

When adding features:
- Update relevant documentation files
- Add docstrings to new functions/classes
- Include examples in QUICKSTART.md if applicable
- Update README.md if needed

## 🎨 Code Examples

### Adding a New Analysis Method

```python
# In src/code_frequency_analyzer.py

def get_quarterly_stats(self) -> pd.DataFrame:
    """Calculate statistics by quarter.
    
    Returns:
        DataFrame with quarterly statistics
    """
    df = self.data.copy()
    df['Quarter'] = df['DateTime'].dt.to_period('Q')
    
    quarterly = df.groupby('Quarter').agg({
        'Additions': 'sum',
        'Deletions': 'sum'
    })
    
    return quarterly
```

### Adding a Test

```python
# In tests/test_analyzer.py

def test_quarterly_stats():
    """Test quarterly statistics calculation."""
    loader = CodeFrequencyLoader()
    analyzer = CodeFrequencyAnalyzer(loader)
    
    quarterly = analyzer.get_quarterly_stats()
    
    assert isinstance(quarterly, pd.DataFrame)
    assert 'Additions' in quarterly.columns
    assert 'Deletions' in quarterly.columns
```

## 🤝 Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Accept constructive criticism
- Focus on what's best for the community
- Show empathy towards others

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## ❓ Questions?

Feel free to:
- Open an issue for questions
- Start a discussion
- Reach out to maintainers

---

Thank you for contributing to RunTime! 🎉
