# Show all file sizes formatted
ls -lh output/visualizations/*.png | awk '{print $9 ": " $5}'

# Count total files
ls -1 output/visualizations/*.png | awk 'END {print "Total files:", NR}'

# Show test results summary
pytest tests/ | awk '/passed/ {print "✅", $0}'

# Format CSV data
head -5 "Code frequency.csv" | awk -F',' '{print "Date: " $1 " | Additions: " $2}'

# Extract Python version nicely
python3 --version | awk '{print "Using Python version:", $2}'#!/usr/bin/env bash
# RunTime Setup Script
# Automated setup for the RunTime code frequency analysis toolkit

set -e  # Exit on error

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║                                                               ║"
echo "║              🚀 RunTime Setup & Installation 🚀              ║"
echo "║                                                               ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

# Check Python version
echo "📋 Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "   Found Python $python_version"

# Check if Python is >= 3.9
python3 -c "import sys; exit(0 if sys.version_info >= (3, 9) else 1)" || {
    echo "❌ Error: Python 3.9 or higher is required"
    exit 1
}

# Install dependencies
echo ""
echo "📦 Installing dependencies..."
pip install -q -r requirements.txt
echo "   ✅ Dependencies installed"

# Run tests
echo ""
echo "🧪 Running tests..."
pytest tests/ -q
test_result=$?

if [ $test_result -eq 0 ]; then
    echo "   ✅ All tests passed!"
else
    echo "   ⚠️  Some tests failed (exit code: $test_result)"
fi

# Check data file
echo ""
echo "📊 Checking data file..."
if [ -f "Code frequency.csv" ]; then
    record_count=$(wc -l < "Code frequency.csv")
    echo "   ✅ Found Code frequency.csv with $record_count lines"
else
    echo "   ⚠️  Code frequency.csv not found"
fi

# Quick analysis
echo ""
echo "📈 Running quick analysis..."
python src/cli.py load --summary

# Create output directory
echo ""
echo "📁 Setting up output directories..."
mkdir -p output/visualizations
echo "   ✅ Directories created"

# Success message
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🎉 Setup complete! RunTime is ready to use."
echo ""
echo "Quick commands:"
echo "  • python src/cli.py analyze --all"
echo "  • python src/cli.py visualize --all"
echo "  • pytest                              # Run tests"
echo ""
echo "Documentation:"
echo "  • README.md      - Full documentation"
echo "  • QUICKSTART.md  - Quick start guide"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
