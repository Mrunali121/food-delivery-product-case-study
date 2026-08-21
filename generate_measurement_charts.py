"""
Generates the before/after measurement charts for the Reorder & Live ETA
Confidence launch — the "Measurement" stage of this case study.

Uses illustrative figures consistent with the targets set in
product-requirements-document.md (Section 2, Goals) and the queries in
analytics/analysis.sql. In a real project, these numbers would come from
running that SQL against the warehouse; here they represent the outcome
the PRD's rollout plan was gated on.

Usage:
    pip install matplotlib
    python analytics/generate_measurement_charts.py
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

INK = "#14213D"
TEAL = "#0E8F7E"
AMBER = "#E2963A"
SLATE = "#5B6472"
LINE = "#D4D9D6"


def build_repeat_rate_chart(output_path="repeat-rate-before-after.png"):
    """30-day repeat order rate, before vs. after launch (PRD Goal #1: 32% -> 45%)."""
    labels = ["Before\n(pre-launch)", "After\n(post-launch)"]
    values = [32, 47]  # slightly beat the 45% target
    target = 45

    fig, ax = plt.subplots(figsize=(6.5, 5.5))
    bars = ax.bar(labels, values, color=[SLATE, TEAL], width=0.5)
    ax.axhline(target, color=AMBER, linestyle="--", linewidth=1.8, label=f"Target: {target}%")

    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, val + 1.2, f"{val}%",
                 ha="center", fontsize=13, fontweight="bold", color=INK)

    ax.set_ylim(0, 55)
    ax.set_ylabel("30-Day Repeat Order Rate")
    ax.set_title("Repeat Order Rate — Before vs. After Launch", fontsize=13, fontweight="bold", loc="left")
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    ax.legend(frameon=False, loc="upper left")
    ax.grid(axis="y", linestyle=":", alpha=0.4)
    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    plt.close(fig)
    print(f"Saved {output_path}")


def build_eta_accuracy_chart(output_path="eta-accuracy-before-after.png"):
    """Average absolute ETA error, before vs. after (PRD Goal #3: +/-15min -> +/-5min)."""
    labels = ["Before", "After"]
    values = [14.2, 4.6]
    target = 5

    fig, ax = plt.subplots(figsize=(6.5, 5.5))
    bars = ax.bar(labels, values, color=[SLATE, TEAL], width=0.5)
    ax.axhline(target, color=AMBER, linestyle="--", linewidth=1.8, label=f"Target: ±{target} min")

    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, val + 0.4, f"{val} min",
                 ha="center", fontsize=13, fontweight="bold", color=INK)

    ax.set_ylim(0, 17)
    ax.set_ylabel("Avg. Absolute ETA Error (minutes)")
    ax.set_title("ETA Accuracy — Before vs. After Launch", fontsize=13, fontweight="bold", loc="left")
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    ax.legend(frameon=False, loc="upper right")
    ax.grid(axis="y", linestyle=":", alpha=0.4)
    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    plt.close(fig)
    print(f"Saved {output_path}")


def build_ticket_trend_chart(output_path="support-ticket-trend.png"):
    """Weekly 'Where is my order?' ticket share through the phased rollout."""
    weeks = ["Wk -2", "Wk -1", "Launch\n(10%)", "Wk 2\n(50%)", "Wk 3", "Wk 4\n(100%)", "Wk 5", "Wk 6"]
    values = [22.4, 21.8, 20.1, 16.3, 14.7, 12.9, 11.8, 11.2]

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(weeks, values, marker="o", color=TEAL, linewidth=2.5)
    ax.axhline(12, color=AMBER, linestyle="--", linewidth=1.5, label="Target: 12%")
    ax.axvline(2, color=LINE, linestyle=":", linewidth=1.5)
    ax.annotate("Phased rollout begins", xy=(2, 21), xytext=(2.3, 24),
                fontsize=9, color=SLATE,
                arrowprops=dict(arrowstyle="->", color=SLATE))

    ax.set_ylim(0, 27)
    ax.set_ylabel("'Where is my order?' tickets (% of total)")
    ax.set_title("Support Ticket Share — Through the Phased Rollout", fontsize=13, fontweight="bold", loc="left")
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    ax.legend(frameon=False, loc="upper right")
    ax.grid(axis="y", linestyle=":", alpha=0.4)
    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    plt.close(fig)
    print(f"Saved {output_path}")


if __name__ == "__main__":
    build_repeat_rate_chart()
    build_eta_accuracy_chart()
    build_ticket_trend_chart()
