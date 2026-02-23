#!/usr/bin/env python
"""Command-line interface for RunTime code frequency analysis."""

import argparse
import sys
from pathlib import Path

try:
    from .code_frequency_loader import CodeFrequencyLoader
    from .code_frequency_analyzer import CodeFrequencyAnalyzer
    from .code_frequency_visualizer import CodeFrequencyVisualizer
except ImportError:
    from code_frequency_loader import CodeFrequencyLoader
    from code_frequency_analyzer import CodeFrequencyAnalyzer
    from code_frequency_visualizer import CodeFrequencyVisualizer


def load_command(args):
    """Execute load command."""
    loader = CodeFrequencyLoader(args.file)
    data = loader.load()

    print(f"✅ Successfully loaded {len(data)} records")
    date_min = data["DateTime"].min().date()
    date_max = data["DateTime"].max().date()
    print(f"\nDate range: {date_min} to {date_max}")

    if args.summary:
        print("\n" + "=" * 60)
        print("SUMMARY STATISTICS")
        print("=" * 60)
        summary = loader.get_summary()
        print(f"Total Additions: {summary['total_additions']:,}")
        print(f"Total Deletions: {summary['total_deletions']:,}")
        print(f"Net Changes: {summary['net_changes']:,}")
        print(f"Number of Records: {summary['num_records']:,}")

    if args.head:
        print(f"\nFirst {args.head} rows:")
        print(data.head(args.head))


def analyze_command(args):
    """Execute analyze command."""
    loader = CodeFrequencyLoader(args.file)
    analyzer = CodeFrequencyAnalyzer(loader)

    print("=" * 60)
    print("CODE FREQUENCY ANALYSIS")
    print("=" * 60)

    if args.activity:
        print(f"\n📊 Activity Ratio: {analyzer.calculate_activity_ratio():.2%}")

    if args.churn:
        print("\n🔄 Churn Statistics:")
        print("-" * 60)
        churn = analyzer.get_churn_stats()
        for key, value in churn.items():
            if isinstance(value, float):
                print(f"  {key.replace('_', ' ').title()}: {value:,.2f}")
            else:
                print(f"  {key.replace('_', ' ').title()}: {value:,}")

    if args.top:
        print(f"\n🏆 Top {args.top} Most Active Weeks:")
        print("-" * 60)
        top = analyzer.get_top_activity_weeks(args.top)
        print(top.to_string(index=False))

    if args.yearly:
        print("\n📅 Yearly Statistics:")
        print("-" * 60)
        yearly = analyzer.get_yearly_stats()
        print(yearly.to_string())

    if args.sprints:
        print("\n🚀 Detected Coding Sprints:")
        print("-" * 60)
        sprints = analyzer.detect_sprints()
        if sprints:
            for i, sprint in enumerate(sprints, 1):
                print(f"\nSprint {i}:")
                for key, value in sprint.items():
                    key_title = key.replace("_", " ").title()
                    if hasattr(value, "date"):
                        print(f"  {key_title}: {value.date()}")
                    elif isinstance(value, int):
                        print(f"  {key_title}: {value:,}")
                    else:
                        print(f"  {key_title}: {value:.2f}")
        else:
            print("  No significant sprints detected")


def visualize_command(args):
    """Execute visualize command."""
    loader = CodeFrequencyLoader(args.file)
    visualizer = CodeFrequencyVisualizer(loader)

    output_dir = Path(args.output)

    if args.all or args.dashboard:
        print("Creating complete dashboard...")
        visualizer.create_dashboard(save_dir=str(output_dir))
        print(f"✅ All visualizations saved to {output_dir}/")
    else:
        output_dir.mkdir(parents=True, exist_ok=True)

        if args.timeline:
            print("Creating timeline plot...")
            timeline_path = str(output_dir / "timeline.png")
            visualizer.plot_timeline(save_path=timeline_path)

        if args.net:
            print("Creating net changes plot...")
            net_path = str(output_dir / "net_changes.png")
            visualizer.plot_net_changes(save_path=net_path)

        if args.yearly:
            print("Creating yearly summary...")
            yearly_path = str(output_dir / "yearly_summary.png")
            visualizer.plot_yearly_summary(save_path=yearly_path)

        if args.heatmap:
            print("Creating activity heatmap...")
            heatmap_path = str(output_dir / "activity_heatmap.png")
            visualizer.plot_activity_heatmap(save_path=heatmap_path)

        print(f"✅ Visualizations saved to {output_dir}/")


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="RunTime - Code Frequency Analysis Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Load and show summary
  %(prog)s load --summary

  # Full analysis with all options
  %(prog)s analyze --all

  # Create all visualizations
  %(prog)s visualize --all

  # Specific analysis
  %(prog)s analyze --top 10 --sprints
        """,
    )

    parser.add_argument("--version", action="version", version="RunTime 1.0.0")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Load command
    load_parser = subparsers.add_parser("load", help="Load and display data")
    load_parser.add_argument(
        "-f",
        "--file",
        default="Code frequency.csv",
        help="CSV file to load (default: Code frequency.csv)",
    )
    load_parser.add_argument(
        "-s", "--summary", action="store_true", help="Show summary statistics"
    )
    load_parser.add_argument("--head", type=int, metavar="N", help="Show first N rows")
    load_parser.set_defaults(func=load_command)

    # Analyze command
    analyze_parser = subparsers.add_parser(
        "analyze", help="Analyze code frequency patterns"
    )
    analyze_parser.add_argument(
        "-f", "--file", default="Code frequency.csv", help="CSV file to analyze"
    )
    analyze_parser.add_argument(
        "-a", "--all", action="store_true", help="Show all analysis"
    )
    analyze_parser.add_argument(
        "--activity", action="store_true", help="Show activity ratio"
    )
    analyze_parser.add_argument(
        "--churn", action="store_true", help="Show churn statistics"
    )
    analyze_parser.add_argument(
        "-t", "--top", type=int, metavar="N", help="Show top N active weeks"
    )
    analyze_parser.add_argument(
        "-y", "--yearly", action="store_true", help="Show yearly statistics"
    )
    analyze_parser.add_argument(
        "-s", "--sprints", action="store_true", help="Detect coding sprints"
    )
    analyze_parser.set_defaults(func=analyze_command)

    # Visualize command
    viz_parser = subparsers.add_parser("visualize", help="Create visualizations")
    viz_parser.add_argument(
        "-f", "--file", default="Code frequency.csv", help="CSV file to visualize"
    )
    viz_parser.add_argument(
        "-o",
        "--output",
        default="output/visualizations",
        help="Output directory (default: output/visualizations)",
    )
    viz_parser.add_argument(
        "-a", "--all", action="store_true", help="Create all visualizations"
    )
    viz_parser.add_argument(
        "-d", "--dashboard", action="store_true", help="Create complete dashboard"
    )
    viz_parser.add_argument(
        "--timeline", action="store_true", help="Create timeline plot"
    )
    viz_parser.add_argument(
        "--net", action="store_true", help="Create net changes plot"
    )
    viz_parser.add_argument(
        "--yearly", action="store_true", help="Create yearly summary"
    )
    viz_parser.add_argument(
        "--heatmap", action="store_true", help="Create activity heatmap"
    )
    viz_parser.set_defaults(func=visualize_command)

    # Parse arguments
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    # Set all flags for analyze if --all is used
    if args.command == "analyze" and args.all:
        args.activity = True
        args.churn = True
        args.top = 10
        args.yearly = True
        args.sprints = True

    # Execute command
    try:
        args.func(args)
        return 0
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
