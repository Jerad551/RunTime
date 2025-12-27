assert ("DateTime" in data.columns and 
        "Additions" in data.columns and 
        "Deletions" in data.columns)        def test_expected_columns_present():
            """Test that the required columns are present."""
            loader = CodeFrequencyLoader()
            data = loader.load()
        
            expected_columns = ["DateTime", "Additions", "Deletions"]
            assert all(col in data.columns for col in expected_columns)"""Tests for CodeFrequencyLoader."""

import sys
from pathlib import Path
import pytest
import pandas as pd

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.code_frequency_loader import CodeFrequencyLoader  # noqa: E402


def test_load_returns_dataframe():
    """Test that load() returns a pandas DataFrame."""
    loader = CodeFrequencyLoader()
    data = loader.load()
    assert isinstance(data, pd.DataFrame)


def test_expected_columns_present():
    """Test that the required columns are present."""
    loader = CodeFrequencyLoader()
    data = loader.load()

    expected_columns = ["DateTime", "Additions", "Deletions"]
    assert all(col in data.columns for col in expected_columns)


def test_datetime_column_is_datetime():
    """Test that DateTime column is converted to datetime type."""
    loader = CodeFrequencyLoader()
    data = loader.load()
    assert pd.api.types.is_datetime64_any_dtype(data["DateTime"])


def test_get_summary_structure():
    """Test that get_summary returns expected keys."""
    loader = CodeFrequencyLoader()
    summary = loader.get_summary()

    expected_keys = [
        "total_additions",
        "total_deletions",
        "net_changes",
        "date_range",
        "num_records",
    ]
    assert all(key in summary for key in expected_keys)


def test_file_not_found():
    """Test that FileNotFoundError is raised for missing file."""
    loader = CodeFrequencyLoader("nonexistent.csv")
    with pytest.raises(FileNotFoundError):
        loader.load()


def test_data_not_empty():
    """Test that loaded data is not empty."""
    loader = CodeFrequencyLoader()
    data = loader.load()
    assert len(data) > 0


def test_summary_calculations():
    """Test that summary calculations are reasonable."""
    loader = CodeFrequencyLoader()
    summary = loader.get_summary()

    # Net changes should be additions + deletions (deletions are negative)
    assert isinstance(summary["total_additions"], (int, float)) or hasattr(
        summary["total_additions"], "__int__"
    )
    assert isinstance(summary["total_deletions"], (int, float)) or hasattr(
        summary["total_deletions"], "__int__"
    )
    assert isinstance(summary["net_changes"], (int, float)) or hasattr(
        summary["net_changes"], "__int__"
    )
    assert summary["num_records"] > 0
    assert summary["total_additions"] > 0
    assert summary["total_deletions"] > 0
