"""Code Frequency Analysis Tools.

This module provides advanced analysis capabilities for code frequency data.
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple
from datetime import datetime, timedelta
try:
    from .code_frequency_loader import CodeFrequencyLoader
except ImportError:
    from code_frequency_loader import CodeFrequencyLoader


class CodeFrequencyAnalyzer:
    """Analyzer for code frequency patterns and trends."""
    
    def __init__(self, loader: CodeFrequencyLoader = None):
        """Initialize the analyzer.
        
        Args:
            loader: CodeFrequencyLoader instance. Creates new one if None.
        """
        self.loader = loader or CodeFrequencyLoader()
        if self.loader.data is None:
            self.loader.load()
        self.data = self.loader.data
    
    def get_activity_periods(self, min_changes: int = 10) -> pd.DataFrame:
        """Identify periods of significant activity.
        
        Args:
            min_changes: Minimum net changes to consider as active
            
        Returns:
            DataFrame with active periods
        """
        df = self.data.copy()
        df['NetChanges'] = df['Additions'] + df['Deletions']
        df['AbsChanges'] = df['Additions'] + abs(df['Deletions'])
        
        active = df[df['AbsChanges'] >= min_changes].copy()
        return active[['DateTime', 'Additions', 'Deletions', 'NetChanges', 'AbsChanges']]
    
    def get_yearly_stats(self) -> pd.DataFrame:
        """Calculate statistics by year.
        
        Returns:
            DataFrame with yearly statistics
        """
        df = self.data.copy()
        df['Year'] = df['DateTime'].dt.year
        
        yearly = df.groupby('Year').agg({
            'Additions': ['sum', 'mean', 'max'],
            'Deletions': ['sum', 'mean', 'min']
        }).round(2)
        
        yearly.columns = ['_'.join(col).strip() for col in yearly.columns.values]
        yearly['net_changes'] = yearly['Additions_sum'] + yearly['Deletions_sum']
        
        return yearly
    
    def get_monthly_stats(self) -> pd.DataFrame:
        """Calculate statistics by month.
        
        Returns:
            DataFrame with monthly statistics
        """
        df = self.data.copy()
        df['YearMonth'] = df['DateTime'].dt.to_period('M')
        
        monthly = df.groupby('YearMonth').agg({
            'Additions': 'sum',
            'Deletions': 'sum'
        })
        
        monthly['net_changes'] = monthly['Additions'] + monthly['Deletions']
        monthly['abs_changes'] = monthly['Additions'] + abs(monthly['Deletions'])
        
        return monthly
    
    def get_top_activity_weeks(self, n: int = 10) -> pd.DataFrame:
        """Find weeks with most activity.
        
        Args:
            n: Number of top weeks to return
            
        Returns:
            DataFrame with top n active weeks
        """
        df = self.data.copy()
        df['AbsChanges'] = df['Additions'] + abs(df['Deletions'])
        
        top = df.nlargest(n, 'AbsChanges')[['DateTime', 'Additions', 'Deletions', 'AbsChanges']]
        return top.reset_index(drop=True)
    
    def calculate_activity_ratio(self) -> float:
        """Calculate the ratio of active weeks to total weeks.
        
        Returns:
            Ratio of weeks with any changes to total weeks
        """
        df = self.data.copy()
        total_weeks = len(df)
        active_weeks = len(df[(df['Additions'] != 0) | (df['Deletions'] != 0)])
        
        return active_weeks / total_weeks if total_weeks > 0 else 0.0
    
    def get_churn_stats(self) -> Dict:
        """Calculate code churn statistics.
        
        Returns:
            Dictionary with churn metrics
        """
        df = self.data.copy()
        df['Churn'] = df['Additions'] + abs(df['Deletions'])
        
        return {
            'total_churn': int(df['Churn'].sum()),
            'avg_weekly_churn': float(df['Churn'].mean()),
            'max_weekly_churn': int(df['Churn'].max()),
            'weeks_with_churn': int((df['Churn'] > 0).sum()),
            'activity_ratio': self.calculate_activity_ratio()
        }
    
    def detect_sprints(self, window_weeks: int = 4, 
                       threshold_multiplier: float = 2.0) -> List[Dict]:
        """Detect coding sprints (periods of high activity).
        
        Args:
            window_weeks: Size of rolling window in weeks
            threshold_multiplier: Multiplier for mean to detect sprints
            
        Returns:
            List of sprint periods with statistics
        """
        df = self.data.copy()
        df['AbsChanges'] = df['Additions'] + abs(df['Deletions'])
        
        # Calculate rolling average
        df['RollingAvg'] = df['AbsChanges'].rolling(window=window_weeks, center=True).mean()
        
        # Find sprints where activity exceeds threshold
        mean_activity = df['AbsChanges'].mean()
        threshold = mean_activity * threshold_multiplier
        
        df['IsSprint'] = df['RollingAvg'] > threshold
        
        # Group consecutive sprint weeks
        df['SprintGroup'] = (df['IsSprint'] != df['IsSprint'].shift()).cumsum()
        
        sprints = []
        for group_id, group in df[df['IsSprint']].groupby('SprintGroup'):
            sprints.append({
                'start_date': group['DateTime'].min(),
                'end_date': group['DateTime'].max(),
                'duration_weeks': len(group),
                'total_additions': int(group['Additions'].sum()),
                'total_deletions': int(abs(group['Deletions'].sum())),
                'avg_weekly_churn': float(group['AbsChanges'].mean())
            })
        
        return sprints
    
    def get_productivity_trends(self, periods: int = 4) -> pd.DataFrame:
        """Analyze productivity trends across time periods.
        
        Args:
            periods: Number of equal periods to divide timeline into
            
        Returns:
            DataFrame with productivity metrics per period
        """
        df = self.data.copy()
        df['Period'] = pd.cut(range(len(df)), bins=periods, labels=False)
        
        trends = df.groupby('Period').agg({
            'Additions': ['sum', 'mean'],
            'Deletions': ['sum', 'mean']
        })
        
        trends.columns = ['_'.join(col).strip() for col in trends.columns.values]
        trends['net_changes'] = trends['Additions_sum'] + trends['Deletions_sum']
        
        return trends


def main():
    """Main entry point for analysis."""
    analyzer = CodeFrequencyAnalyzer()
    
    print("=" * 60)
    print("CODE FREQUENCY ANALYSIS")
    print("=" * 60)
    
    # Activity ratio
    print(f"\n📊 Activity Ratio: {analyzer.calculate_activity_ratio():.2%}")
    
    # Churn statistics
    print("\n🔄 Churn Statistics:")
    print("-" * 60)
    churn = analyzer.get_churn_stats()
    for key, value in churn.items():
        print(f"  {key.replace('_', ' ').title()}: {value:,.2f}" if isinstance(value, float) 
              else f"  {key.replace('_', ' ').title()}: {value:,}")
    
    # Top activity weeks
    print("\n🏆 Top 10 Most Active Weeks:")
    print("-" * 60)
    top_weeks = analyzer.get_top_activity_weeks(10)
    print(top_weeks.to_string(index=False))
    
    # Yearly statistics
    print("\n📅 Yearly Statistics:")
    print("-" * 60)
    yearly = analyzer.get_yearly_stats()
    print(yearly.to_string())
    
    # Detect sprints
    print("\n🚀 Detected Coding Sprints:")
    print("-" * 60)
    sprints = analyzer.detect_sprints()
    if sprints:
        for i, sprint in enumerate(sprints, 1):
            print(f"\nSprint {i}:")
            for key, value in sprint.items():
                if isinstance(value, datetime):
                    print(f"  {key.replace('_', ' ').title()}: {value.date()}")
                else:
                    print(f"  {key.replace('_', ' ').title()}: {value:,}" if isinstance(value, int)
                          else f"  {key.replace('_', ' ').title()}: {value:.2f}")
    else:
        print("  No significant sprints detected")


if __name__ == "__main__":
    main()
