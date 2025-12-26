"""Code Frequency Data Loader

This module loads and processes code frequency data from CSV files.
"""

import pandas as pd
from pathlib import Path


class CodeFrequencyLoader:
    """Loader for code frequency data."""
    
    def __init__(self, csv_path: str = "Code frequency.csv"):
        """Initialize the loader with a CSV file path.
        
        Args:
            csv_path: Path to the CSV file containing code frequency data
        """
        self.csv_path = Path(csv_path)
        self.data = None
    
    def load(self):
        """Load the code frequency data from CSV.
        
        Returns:
            pandas.DataFrame: Loaded data with DateTime, Additions, and Deletions columns
        """
        if not self.csv_path.exists():
            raise FileNotFoundError(f"CSV file not found: {self.csv_path}")
        
        self.data = pd.read_csv(self.csv_path)
        self.data['DateTime'] = pd.to_datetime(self.data['DateTime'])
        return self.data
    
    def get_summary(self):
        """Get a summary of the code frequency data.
        
        Returns:
            dict: Summary statistics
        """
        if self.data is None:
            self.load()
        
        return {
            'total_additions': self.data['Additions'].sum(),
            'total_deletions': abs(self.data['Deletions'].sum()),
            'net_changes': self.data['Additions'].sum() + self.data['Deletions'].sum(),
            'date_range': {
                'start': self.data['DateTime'].min(),
                'end': self.data['DateTime'].max()
            },
            'num_records': len(self.data)
        }


def main():
    """Main entry point for the script."""
    loader = CodeFrequencyLoader()
    
    print("Loading code frequency data...")
    data = loader.load()
    
    print(f"\nLoaded {len(data)} records")
    print(f"\nFirst 5 rows:")
    print(data.head())
    
    print("\n" + "="*50)
    print("Summary Statistics:")
    print("="*50)
    summary = loader.get_summary()
    print(f"Total Additions: {summary['total_additions']:,}")
    print(f"Total Deletions: {summary['total_deletions']:,}")
    print(f"Net Changes: {summary['net_changes']:,}")
    print(f"Date Range: {summary['date_range']['start'].date()} to {summary['date_range']['end'].date()}")
    print(f"Number of Records: {summary['num_records']}")


if __name__ == "__main__":
    main()
