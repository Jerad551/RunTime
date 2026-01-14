"""Code Frequency Visualization Tools.

This module provides visualization capabilities for code frequency data.
"""

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import numpy as np
from pathlib import Path
from typing import Optional, Tuple

try:
    from .code_frequency_loader import CodeFrequencyLoader
    from .code_frequency_analyzer import CodeFrequencyAnalyzer
except ImportError:
    from code_frequency_loader import CodeFrequencyLoader
    from code_frequency_analyzer import CodeFrequencyAnalyzer


class CodeFrequencyVisualizer:
    """Visualizer for code frequency data."""

    def __init__(
        self,
        loader: CodeFrequencyLoader = None,
        style: str = "seaborn-v0_8-darkgrid"
    ):
        """Initialize the visualizer.

        Args:
            loader: CodeFrequencyLoader instance
            style: Matplotlib style to use
        """
        self.loader = loader or CodeFrequencyLoader()
        if self.loader.data is None:
            self.loader.data = self.loader.load()

        self.data = self.loader.data
        self.analyzer = CodeFrequencyAnalyzer(self.loader)

        # Set style
        try:
            plt.style.use(style)
        except OSError:
            plt.style.use("default")

        sns.set_palette("husl")

    def plot_timeline(
        self,
        figsize: Tuple[int, int] = (15, 6),
        save_path: Optional[str] = None
    ) -> plt.Figure:
        """Plot additions and deletions over time.

        Args:
            figsize: Figure size (width, height)
            save_path: Path to save figure. If None, displays
                interactively.

        Returns:
            matplotlib Figure object
        """
        fig, ax = plt.subplots(figsize=figsize)

        ax.plot(
            self.data["DateTime"],
            self.data["Additions"],
            label="Additions",
            color="green",
            linewidth=1.5,
            alpha=0.7,
        )
        ax.plot(
            self.data["DateTime"],
            abs(self.data["Deletions"]),
            label="Deletions",
            color="red",
            linewidth=1.5,
            alpha=0.7,
        )

        ax.set_xlabel("Date", fontsize=12)
        ax.set_ylabel("Lines of Code", fontsize=12)
        ax.set_title(
            "Code Frequency Over Time",
            fontsize=14,
            fontweight="bold"
        )
        ax.legend(loc="upper left")
        ax.grid(True, alpha=0.3)

        # Format x-axis
        ax.xaxis.set_major_locator(mdates.YearLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
        plt.xticks(rotation=45)

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches="tight")
            print(f"Saved timeline plot to {save_path}")

        return fig

    def plot_net_changes(
        self,
        figsize: Tuple[int, int] = (15, 6),
        save_path: Optional[str] = None
    ) -> plt.Figure:
        """Plot net changes over time.

        Args:
            figsize: Figure size
            save_path: Path to save figure

        Returns:
            matplotlib Figure object
        """
        fig, ax = plt.subplots(figsize=figsize)

        net_changes = self.data["Additions"] + self.data["Deletions"]
        colors = ["green" if x >= 0 else "red" for x in net_changes]

        ax.bar(
            self.data["DateTime"],
            net_changes,
            color=colors,
            alpha=0.6,
            width=5
        )
        ax.axhline(y=0, color="black", linestyle="-", linewidth=0.5)

        ax.set_xlabel("Date", fontsize=12)
        ax.set_ylabel("Net Changes (Lines)", fontsize=12)
        ax.set_title(
            "Net Code Changes Over Time",
            fontsize=14,
            fontweight="bold"
        )
        ax.grid(True, alpha=0.3, axis="y")

        # Format x-axis
        ax.xaxis.set_major_locator(mdates.YearLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
        plt.xticks(rotation=45)

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches="tight")
            print(f"Saved net changes plot to {save_path}")

        return fig

    def plot_yearly_summary(
        self,
        figsize: Tuple[int, int] = (12, 6),
        save_path: Optional[str] = None
    ) -> plt.Figure:
        """Plot yearly summary statistics.

        Args:
            figsize: Figure size
            save_path: Path to save figure

        Returns:
            matplotlib Figure object
        """
        yearly = self.analyzer.get_yearly_stats()

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize)

        # Total changes by year
        x = yearly.index
        width = 0.35
        x_pos = np.arange(len(x))

        ax1.bar(
            x_pos - width / 2,
            yearly["Additions_sum"],
            width,
            label="Additions",
            color="green",
            alpha=0.7,
        )
        ax1.bar(
            x_pos + width / 2,
            abs(yearly["Deletions_sum"]),
            width,
            label="Deletions",
            color="red",
            alpha=0.7,
        )

        ax1.set_xlabel("Year", fontsize=12)
        ax1.set_ylabel("Total Lines", fontsize=12)
        ax1.set_title(
            "Total Changes by Year", fontsize=12, fontweight="bold"
        )
        ax1.set_xticks(x_pos)
        ax1.set_xticklabels(x, rotation=45)
        ax1.legend()
        ax1.grid(True, alpha=0.3, axis="y")

        # Net changes by year
        ax2.bar(x, yearly["net_changes"], color="blue", alpha=0.7)
        ax2.axhline(y=0, color="black", linestyle="-", linewidth=0.5)
        ax2.set_xlabel("Year", fontsize=12)
        ax2.set_ylabel("Net Changes", fontsize=12)
        ax2.set_title("Net Changes by Year", fontsize=12, fontweight="bold")
        ax2.tick_params(axis="x", rotation=45)
        ax2.grid(True, alpha=0.3, axis="y")

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches="tight")
            print(f"Saved yearly summary to {save_path}")

        return fig

    def plot_activity_heatmap(
        self,
        figsize: Tuple[int, int] = (14, 8),
        save_path: Optional[str] = None
    ) -> plt.Figure:
        """Plot activity heatmap by year and month.

        Args:
            figsize: Figure size
            save_path: Path to save figure

        Returns:
            matplotlib Figure object
        """
        df = self.data.copy()
        df["Year"] = df["DateTime"].dt.year
        df["Month"] = df["DateTime"].dt.month
        df["Activity"] = df["Additions"] + abs(df["Deletions"])

        # Create pivot table
        pivot = df.pivot_table(
            values="Activity",
            index="Month",
            columns="Year",
            aggfunc="sum",
            fill_value=0,
        )

        fig, ax = plt.subplots(figsize=figsize)
        sns.heatmap(
            pivot, cmap="YlOrRd", ax=ax, cbar_kws={"label": "Total Changes"}
        )

        ax.set_xlabel("Year", fontsize=12)
        ax.set_ylabel("Month", fontsize=12)
        ax.set_title("Code Activity Heatmap", fontsize=14, fontweight="bold")

        # Set month labels
        month_names = [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ]
        ax.set_yticklabels(month_names, rotation=0)

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches="tight")
            print(f"Saved activity heatmap to {save_path}")

        return fig

    def create_dashboard(self, save_dir: Optional[str] = None) -> None:
        """Create a comprehensive dashboard with multiple plots.

        Args:
            save_dir: Directory to save plots. If None, displays interactively.
        """
        if save_dir:
            save_dir = Path(save_dir)
            save_dir.mkdir(parents=True, exist_ok=True)

        print("Generating visualizations...")

        # Timeline
        self.plot_timeline(
            save_path=str(save_dir / "timeline.png") if save_dir else None
        )

        # Net changes
        net_path = str(save_dir / "net_changes.png") if save_dir else None
        self.plot_net_changes(save_path=net_path)

        # Yearly summary
        yearly_path = (
            str(save_dir / "yearly_summary.png") if save_dir else None
        )
        self.plot_yearly_summary(save_path=yearly_path)

        # Activity heatmap
        heatmap_path = (
            str(save_dir / "activity_heatmap.png") if save_dir else None
        )
        self.plot_activity_heatmap(save_path=heatmap_path)

        if not save_dir:
            plt.show()
        else:
            print(f"\nAll visualizations saved to {save_dir}/")


def main():
    """Main entry point for visualization."""
    visualizer = CodeFrequencyVisualizer()

    # Create output directory
    output_dir = Path("output/visualizations")

    print("Creating code frequency visualizations...")
    visualizer.create_dashboard(save_dir=str(output_dir))

    print("\n✅ Visualization complete!")


if __name__ == "__main__":
    main()
