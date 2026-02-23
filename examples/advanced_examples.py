#!/usr/bin/env python
"""
Advanced Examples for RunTime

This script demonstrates advanced usage patterns and custom analyses.
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src import CodeFrequencyLoader, CodeFrequencyAnalyzer, CodeFrequencyVisualizer
import pandas as pd
import matplotlib.pyplot as plt


def example_1_basic_workflow():
    """Example 1: Basic analysis workflow."""
    print("=" * 70)
    print("Example 1: Basic Analysis Workflow")
    print("=" * 70)

    # Load data
    loader = CodeFrequencyLoader()
    data = loader.load()

    print(f"\n📊 Loaded {len(data)} records")
    print(
        f"Date range: {data['DateTime'].min().date()} to {data['DateTime'].max().date()}"
    )

    # Get summary
    summary = loader.get_summary()
    print(f"\n📈 Summary:")
    print(f"  Total additions: {summary['total_additions']:,}")
    print(f"  Total deletions: {summary['total_deletions']:,}")
    print(f"  Net changes: {summary['net_changes']:,}")


def example_2_sprint_analysis():
    """Example 2: Detailed sprint analysis."""
    print("\n" + "=" * 70)
    print("Example 2: Sprint Detection and Analysis")
    print("=" * 70)

    loader = CodeFrequencyLoader()
    analyzer = CodeFrequencyAnalyzer(loader)

    # Detect sprints with custom parameters
    sprints = analyzer.detect_sprints(window_weeks=3, threshold_multiplier=1.5)

    print(f"\n🚀 Detected {len(sprints)} coding sprints:\n")

    for i, sprint in enumerate(sprints[:5], 1):  # Show top 5
        print(f"Sprint {i}:")
        print(f"  Duration: {sprint['duration_weeks']} weeks")
        print(f"  Period: {sprint['start_date'].date()} to {sprint['end_date'].date()}")
        print(
            f"  Total changes: {sprint['total_additions'] + sprint['total_deletions']:,}"
        )
        print(f"  Avg weekly churn: {sprint['avg_weekly_churn']:,.0f}")
        print()


def example_3_time_analysis():
    """Example 3: Time-based analysis."""
    print("=" * 70)
    print("Example 3: Time-Based Analysis")
    print("=" * 70)

    loader = CodeFrequencyLoader()
    analyzer = CodeFrequencyAnalyzer(loader)

    # Yearly statistics
    yearly = analyzer.get_yearly_stats()
    print("\n📅 Top 3 Most Productive Years:")
    top_years = yearly.nlargest(3, "Additions_sum")

    for year, row in top_years.iterrows():
        print(f"\n{year}:")
        print(f"  Additions: {int(row['Additions_sum']):,}")
        print(f"  Deletions: {int(abs(row['Deletions_sum'])):,}")
        print(f"  Net: {int(row['net_changes']):,}")

    # Activity patterns
    print(f"\n📊 Activity Statistics:")
    print(f"  Activity ratio: {analyzer.calculate_activity_ratio():.2%}")
    churn = analyzer.get_churn_stats()
    print(f"  Total code churn: {churn['total_churn']:,}")
    print(f"  Average weekly churn: {churn['avg_weekly_churn']:.0f}")


def example_4_custom_visualization():
    """Example 4: Custom visualization."""
    print("\n" + "=" * 70)
    print("Example 4: Custom Visualization")
    print("=" * 70)

    loader = CodeFrequencyLoader()
    loader.load()
    data = loader.data.copy()

    # Create custom analysis
    data["NetChanges"] = data["Additions"] + data["Deletions"]
    data["Year"] = data["DateTime"].dt.year

    # Calculate moving average
    data["MA_30"] = data["Additions"].rolling(window=30, center=True).mean()

    # Create custom plot
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 8))

    # Plot 1: Additions with moving average
    ax1.plot(data["DateTime"], data["Additions"], alpha=0.3, label="Additions")
    ax1.plot(data["DateTime"], data["MA_30"], "r-", linewidth=2, label="30-week MA")
    ax1.set_ylabel("Lines Added")
    ax1.set_title("Code Additions with 30-Week Moving Average")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Plot 2: Net changes by year
    yearly_net = data.groupby("Year")["NetChanges"].sum()
    ax2.bar(yearly_net.index, yearly_net.values, color="steelblue", alpha=0.7)
    ax2.axhline(y=0, color="black", linestyle="-", linewidth=0.5)
    ax2.set_xlabel("Year")
    ax2.set_ylabel("Net Changes")
    ax2.set_title("Net Code Changes by Year")
    ax2.grid(True, alpha=0.3, axis="y")

    plt.tight_layout()

    # Save plot
    output_path = Path("output/visualizations/custom_analysis.png")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    print(f"\n✅ Custom visualization saved to {output_path}")
    plt.close()


def example_5_filtering_analysis():
    """Example 5: Filtering and conditional analysis."""
    print("\n" + "=" * 70)
    print("Example 5: Filtering and Conditional Analysis")
    print("=" * 70)

    loader = CodeFrequencyLoader()
    loader.load()
    data = loader.data.copy()

    # Analyze only high-activity periods
    data["AbsChanges"] = data["Additions"] + abs(data["Deletions"])
    high_activity = data[data["AbsChanges"] > data["AbsChanges"].quantile(0.75)]

    print(f"\n📊 High Activity Periods (top 25%):")
    print(f"  Total records: {len(high_activity)}")
    print(
        f"  Date range: {high_activity['DateTime'].min().date()} to {high_activity['DateTime'].max().date()}"
    )
    print(f"  Total changes: {high_activity['AbsChanges'].sum():,.0f}")

    # Analyze recent activity (last 2 years)
    recent_date = data["DateTime"].max() - pd.Timedelta(days=730)
    recent_data = data[data["DateTime"] >= recent_date]

    print(f"\n📅 Recent Activity (last 2 years):")
    print(f"  Records: {len(recent_data)}")
    print(f"  Total additions: {recent_data['Additions'].sum():,}")
    print(f"  Total deletions: {abs(recent_data['Deletions'].sum()):,}")
    print(f"  Active weeks: {(recent_data['AbsChanges'] > 0).sum()}")


def example_6_comparison_analysis():
    """Example 6: Comparative analysis."""
    print("\n" + "=" * 70)
    print("Example 6: Comparative Analysis")
    print("=" * 70)

    loader = CodeFrequencyLoader()
    analyzer = CodeFrequencyAnalyzer(loader)

    # Compare productivity across time periods
    trends = analyzer.get_productivity_trends(periods=4)

    print("\n📊 Productivity Trends (4 periods):")
    for period, row in trends.iterrows():
        print(f"\nPeriod {period + 1}:")
        print(f"  Total additions: {int(row['Additions_sum']):,}")
        print(f"  Average additions/week: {row['Additions_mean']:.0f}")
        print(f"  Total deletions: {int(abs(row['Deletions_sum'])):,}")
        print(f"  Net changes: {int(row['net_changes']):,}")


def main():
    """Run all examples."""
    print("\n╔═══════════════════════════════════════════════════════════════╗")
    print("║                                                               ║")
    print("║              📚 RunTime Advanced Examples 📚                 ║")
    print("║                                                               ║")
    print("╚═══════════════════════════════════════════════════════════════╝\n")

    try:
        example_1_basic_workflow()
        example_2_sprint_analysis()
        example_3_time_analysis()
        example_4_custom_visualization()
        example_5_filtering_analysis()
        example_6_comparison_analysis()

        print("\n" + "=" * 70)
        print("✅ All examples completed successfully!")
        print("=" * 70)

    except Exception as e:
        print(f"\n❌ Error: {e}")
        raise


if __name__ == "__main__":
    main()
