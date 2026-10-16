
"""Plot positional-priority scores for candidate genes."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = PROJECT_ROOT / "reports" / "candidate_gene_scored.csv"
OUTPUT_FILE = (
    PROJECT_ROOT
    / "results"
    / "figures"
    / "candidate_gene_positional_scores.png"
)


def main():
    candidates = pd.read_csv(INPUT_FILE)
    candidates["gene"] = candidates["gene"].astype(str).str.strip()
    candidates = candidates.sort_values(
        "distance_from_lead_bp", ascending=True
    )

    fig, ax = plt.subplots(figsize=(9, 5))

    bars = ax.barh(
        candidates["gene"],
        candidates["positional_score"],
    )

    ax.set_xlabel("Project-defined positional-priority score")
    ax.set_ylabel("Candidate gene")
    ax.set_title("Candidate-gene positional prioritization")
    ax.set_xlim(0, 2.5)

    for bar, distance in zip(
        bars, candidates["distance_from_lead_bp"]
    ):
        ax.text(
            bar.get_width() + 0.04,
            bar.get_y() + bar.get_height() / 2,
            f"{int(bar.get_width())} | {distance:,} bp",
            va="center",
            fontsize=9,
        )

    fig.text(
        0.01,
        0.01,
        "Heuristic score based on gene overlap and distance; "
        "not a measure of causality.",
        fontsize=8,
    )

    fig.tight_layout(rect=(0, 0.06, 1, 1))
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT_FILE, dpi=300, bbox_inches="tight")
    plt.close(fig)

    print(f"Saved plot to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
